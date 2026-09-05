/**
 * BHR ENG — Google Classroom Archiver
 * -----------------------------------------------------------------------------
 * Exports the STRUCTURE of your Classroom courses — the part Google gives you
 * no way to download and that Takeout does not meaningfully cover.
 *
 * Captures, per course:
 *   - course metadata
 *   - topics (and their order)
 *   - assignments, materials, questions: title, FULL description text,
 *     topic, state, due date, points, work type
 *   - every attachment: Drive files, links, YouTube videos, Forms
 *   - announcements
 *
 * Deliberately does NOT touch:
 *   - students, rosters, submissions, grades, guardians
 * Nothing student-identifying is read or written. This is course design only.
 *
 * The output is shaped to be RESTORABLE: the Coursework sheet carries the same
 * fields the Classroom Builder publishes from, so this doubles as a rebuild
 * path rather than a museum piece.
 *
 * SETUP (once):
 *   1. Extensions -> Apps Script
 *   2. Services (+) -> Google Classroom API -> v1 -> Add
 *   3. Save, reload the sheet, use the "Classroom Archive" menu
 */

const SH_COURSES     = 'Courses';
const SH_TOPICS      = 'Topics';
const SH_COURSEWORK  = 'Coursework';
const SH_ATTACHMENTS = 'Attachments';
const SH_ANNOUNCE    = 'Announcements';
const SH_SUMMARY     = 'Archive Summary';

const P = PropertiesService.getScriptProperties();
const BUDGET_MS = 4.5 * 60 * 1000;

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Classroom Archive')
    .addItem('1. List my courses', 'listCourses')
    .addItem('2. Archive all active courses', 'archiveAll')
    .addItem('2b. Continue (if it timed out)', 'archiveAll')
    .addSeparator()
    .addItem('Archive ARCHIVED courses too', 'archiveAllIncludingArchived')
    .addItem('Export attachment file list', 'exportAttachmentList')
    .addSeparator()
    .addItem('Reset progress', 'resetProgress')
    .addToUi();
}

/* ------------------------------------------------------------------- courses */

function listCourses() {
  const courses = fetchCourses_(false);
  const sh = resetSheet_(SH_COURSES, [
    'Course Name', 'Section', 'Room', 'State', 'Course ID',
    'Created', 'Updated', 'Link', 'Archive?'
  ]);
  const rows = courses.map(function (c) {
    return [
      c.name || '', c.section || '', c.room || '', c.courseState || '',
      c.id, dateOnly_(c.creationTime), dateOnly_(c.updateTime),
      c.alternateLink || '', 'YES'
    ];
  });
  if (rows.length) sh.getRange(2, 1, rows.length, 9).setValues(rows);
  sh.autoResizeColumns(1, 4);
  ui_('Found ' + rows.length + ' active courses.\n\n' +
      'Set the "Archive?" column to NO for any you want skipped, then run ' +
      '"2. Archive all active courses".');
}

function fetchCourses_(includeArchived) {
  const out = [];
  let token = null;
  do {
    const res = Classroom.Courses.list({
      teacherId: 'me',
      pageSize: 100,
      pageToken: token,
      courseStates: includeArchived ? ['ACTIVE', 'ARCHIVED'] : ['ACTIVE']
    });
    (res.courses || []).forEach(function (c) { out.push(c); });
    token = res.nextPageToken;
  } while (token);
  return out;
}

/* ------------------------------------------------------------------ archiving */

function archiveAllIncludingArchived() { archive_(true); }
function archiveAll()                  { archive_(false); }

function archive_(includeArchived) {
  const started = Date.now();
  const ss = SpreadsheetApp.getActive();

  let queue = P.getProperty('queue');
  if (queue) {
    queue = JSON.parse(queue);
  } else {
    queue = buildQueue_(includeArchived);
    if (!queue.length) { ui_('No courses to archive.'); return; }
    initSheets_();
    P.setProperty('total', String(queue.length));
  }

  const total = Number(P.getProperty('total') || queue.length);

  while (queue.length) {
    if (Date.now() - started > BUDGET_MS) {
      P.setProperty('queue', JSON.stringify(queue));
      ui_('Paused — ' + (total - queue.length) + ' of ' + total + ' courses done.\n\n' +
          'Run "2b. Continue" to keep going.');
      return;
    }

    const course = queue.shift();
    try {
      archiveCourse_(course);
    } catch (err) {
      appendRow_(SH_SUMMARY, ['ERROR', course.name, err.message, '', '']);
    }
    SpreadsheetApp.flush();
  }

  P.deleteProperty('queue');
  P.deleteProperty('total');
  finishSummary_();
  ui_('Archive complete — ' + total + ' courses.\n\n' +
      'Next: "Export attachment file list" to get the Drive files your ' +
      'coursework actually depends on.');
}

function buildQueue_(includeArchived) {
  const ss = SpreadsheetApp.getActive();
  const listSheet = ss.getSheetByName(SH_COURSES);

  // Honour the YES/NO column if the user ran step 1 first.
  if (listSheet && listSheet.getLastRow() > 1 && !includeArchived) {
    const data = listSheet.getRange(2, 1, listSheet.getLastRow() - 1, 9).getValues();
    return data
      .filter(function (r) { return String(r[8]).toUpperCase() !== 'NO'; })
      .map(function (r) { return { id: String(r[4]), name: r[0], section: r[1] }; });
  }
  return fetchCourses_(includeArchived).map(function (c) {
    return { id: c.id, name: c.name, section: c.section || '' };
  });
}

function archiveCourse_(course) {
  const topics = fetchTopics_(course.id);
  const topicName = {};
  topics.forEach(function (t) {
    topicName[t.topicId] = t.name;
    appendRow_(SH_TOPICS, [course.name, t.name, t.topicId, dateOnly_(t.updateTime)]);
  });

  let cwCount = 0, matCount = 0, annCount = 0, attCount = 0;

  // --- Assignments / questions -------------------------------------------
  let token = null;
  do {
    const res = Classroom.Courses.CourseWork.list(course.id, {
      pageSize: 100, pageToken: token,
      courseWorkStates: ['PUBLISHED', 'DRAFT']
    });
    (res.courseWork || []).forEach(function (w) {
      appendRow_(SH_COURSEWORK, [
        course.name,
        w.workType === 'ASSIGNMENT' ? 'Assignment' : titleCase_(w.workType || 'Assignment'),
        w.title || '',
        w.description || '',
        topicName[w.topicId] || '',
        w.state || '',
        dueString_(w.dueDate, w.dueTime),
        (w.maxPoints === 0 || w.maxPoints) ? w.maxPoints : '',
        dateOnly_(w.creationTime),
        dateOnly_(w.updateTime),
        w.alternateLink || '',
        w.id
      ]);
      cwCount++;
      attCount += writeMaterials_(course.name, w.title, w.materials);
    });
    token = res.nextPageToken;
  } while (token);

  // --- Material posts ------------------------------------------------------
  token = null;
  do {
    const res = Classroom.Courses.CourseWorkMaterials.list(course.id, {
      pageSize: 100, pageToken: token,
      courseWorkMaterialStates: ['PUBLISHED', 'DRAFT']
    });
    (res.courseWorkMaterial || []).forEach(function (m) {
      appendRow_(SH_COURSEWORK, [
        course.name, 'Material', m.title || '', m.description || '',
        topicName[m.topicId] || '', m.state || '', '', '',
        dateOnly_(m.creationTime), dateOnly_(m.updateTime),
        m.alternateLink || '', m.id
      ]);
      matCount++;
      attCount += writeMaterials_(course.name, m.title, m.materials);
    });
    token = res.nextPageToken;
  } while (token);

  // --- Announcements -------------------------------------------------------
  token = null;
  do {
    const res = Classroom.Courses.Announcements.list(course.id, {
      pageSize: 100, pageToken: token,
      announcementStates: ['PUBLISHED', 'DRAFT']
    });
    (res.announcements || []).forEach(function (a) {
      appendRow_(SH_ANNOUNCE, [
        course.name, a.text || '', a.state || '',
        dateOnly_(a.creationTime), dateOnly_(a.updateTime),
        a.alternateLink || '', a.id
      ]);
      annCount++;
      attCount += writeMaterials_(course.name, '(announcement)', a.materials);
    });
    token = res.nextPageToken;
  } while (token);

  appendRow_(SH_SUMMARY, [
    course.name, cwCount, matCount, annCount, attCount
  ]);
}

function fetchTopics_(courseId) {
  const out = [];
  let token = null;
  do {
    const res = Classroom.Courses.Topics.list(courseId, {
      pageSize: 100, pageToken: token
    });
    (res.topic || []).forEach(function (t) { out.push(t); });
    token = res.nextPageToken;
  } while (token);
  return out;
}

/**
 * Writes one row per attachment. This is the sheet that tells you which Drive
 * files your coursework actually depends on.
 */
function writeMaterials_(courseName, parentTitle, materials) {
  if (!materials || !materials.length) return 0;
  let n = 0;
  materials.forEach(function (m) {
    let type = '', title = '', driveId = '', url = '';

    if (m.driveFile && m.driveFile.driveFile) {
      type    = 'Drive file';
      title   = m.driveFile.driveFile.title || '';
      driveId = m.driveFile.driveFile.id || '';
      url     = m.driveFile.driveFile.alternateLink || '';
    } else if (m.youtubeVideo) {
      type  = 'YouTube';
      title = m.youtubeVideo.title || '';
      url   = m.youtubeVideo.alternateLink || '';
    } else if (m.link) {
      type  = 'Link';
      title = m.link.title || '';
      url   = m.link.url || '';
    } else if (m.form) {
      type  = 'Form';
      title = m.form.title || '';
      url   = m.form.formUrl || '';
    } else {
      type = 'Other';
    }

    appendRow_(SH_ATTACHMENTS, [courseName, parentTitle || '', type, title, driveId, url]);
    n++;
  });
  return n;
}

/* ------------------------------------------------- attachment file shortlist */

/**
 * Deduplicates the Attachments sheet into a unique list of Drive files —
 * the actual "these matter" set for any local backup.
 */
function exportAttachmentList() {
  const ss = SpreadsheetApp.getActive();
  const src = ss.getSheetByName(SH_ATTACHMENTS);
  if (!src || src.getLastRow() < 2) { ui_('Run the archive first.'); return; }

  const data = src.getRange(2, 1, src.getLastRow() - 1, 6).getValues();
  const seen = {};

  data.forEach(function (r) {
    const id = String(r[4] || '').trim();
    if (!id) return;
    if (!seen[id]) seen[id] = { title: r[3], url: r[5], uses: 0, courses: {} };
    seen[id].uses++;
    seen[id].courses[r[0]] = true;
  });

  const rows = Object.keys(seen).map(function (id) {
    const s = seen[id];
    return [s.title, id, s.uses, Object.keys(s.courses).join(', '), s.url];
  }).sort(function (a, b) { return b[2] - a[2]; });

  const sh = resetSheet_('Files To Back Up',
    ['File Title', 'Drive File ID', 'Times Attached', 'Used In Courses', 'URL']);
  if (rows.length) sh.getRange(2, 1, rows.length, 5).setValues(rows);
  sh.autoResizeColumns(1, 4);

  ui_(rows.length + ' unique Drive files are attached to your coursework.\n\n' +
      'This is the shortlist worth backing up locally — everything else in ' +
      'Drive is optional by comparison.');
}

/* ---------------------------------------------------------------- sheet setup */

function initSheets_() {
  resetSheet_(SH_TOPICS, ['Course', 'Topic', 'Topic ID', 'Updated']);
  resetSheet_(SH_COURSEWORK, [
    'Course', 'Type', 'Title', 'Description / Prompt', 'Topic', 'State',
    'Due', 'Points', 'Created', 'Updated', 'Link', 'ID'
  ]);
  resetSheet_(SH_ATTACHMENTS,
    ['Course', 'Attached To', 'Type', 'Title', 'Drive File ID', 'URL']);
  resetSheet_(SH_ANNOUNCE,
    ['Course', 'Text', 'State', 'Created', 'Updated', 'Link', 'ID']);
  resetSheet_(SH_SUMMARY,
    ['Course', 'Assignments', 'Materials', 'Announcements', 'Attachments']);
}

function resetSheet_(name, headers) {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName(name);
  if (sh) ss.deleteSheet(sh);
  sh = ss.insertSheet(name);
  sh.appendRow(headers);
  sh.getRange(1, 1, 1, headers.length).setFontWeight('bold');
  sh.setFrozenRows(1);
  return sh;
}

function appendRow_(sheetName, row) {
  const sh = SpreadsheetApp.getActive().getSheetByName(sheetName);
  if (sh) sh.appendRow(row);
}

function finishSummary_() {
  const sh = SpreadsheetApp.getActive().getSheetByName(SH_SUMMARY);
  if (!sh || sh.getLastRow() < 2) return;
  const n = sh.getLastRow() - 1;
  const data = sh.getRange(2, 2, n, 4).getValues();
  const tot = [0, 0, 0, 0];
  data.forEach(function (r) {
    for (let i = 0; i < 4; i++) tot[i] += Number(r[i]) || 0;
  });
  sh.appendRow(['— TOTAL —', tot[0], tot[1], tot[2], tot[3]]);
  sh.getRange(sh.getLastRow(), 1, 1, 5).setFontWeight('bold');
}

function resetProgress() {
  P.deleteProperty('queue');
  P.deleteProperty('total');
  ui_('Progress reset.');
}

/* ----------------------------------------------------------------- utilities */

function dueString_(d, t) {
  if (!d) return '';
  const pad = function (n) { return String(n).padStart(2, '0'); };
  let s = d.year + '-' + pad(d.month) + '-' + pad(d.day);
  if (t && (t.hours || t.minutes)) {
    s += ' ' + pad(t.hours || 0) + ':' + pad(t.minutes || 0) + ' UTC';
  }
  return s;
}

function dateOnly_(iso) { return iso ? String(iso).substring(0, 10) : ''; }

function titleCase_(s) {
  return String(s).charAt(0) + String(s).slice(1).toLowerCase().replace(/_/g, ' ');
}

function ui_(msg) {
  try { SpreadsheetApp.getUi().alert(msg); }
  catch (e) { Logger.log(msg); }
}
