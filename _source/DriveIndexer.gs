/**
 * BHR ENG — Drive Indexer
 * -----------------------------------------------------------------------------
 * Builds a complete inventory of Drive files into this spreadsheet.
 *
 * Why Apps Script rather than a connector: this runs as YOU, inside Google.
 * No third-party OAuth token to expire, and — importantly — it can see
 * Shared Drive content, which Google Takeout does not export by default.
 *
 * Resumable: Drive listing can exceed the 6-minute execution limit. The script
 * saves its position and picks up where it left off. Just run "Continue" until
 * it reports Done.
 *
 * SETUP (once):
 *   1. Extensions -> Apps Script
 *   2. Services (+) -> Drive API -> version v3 -> Add
 *   3. Save, reload the spreadsheet, use the "Drive Index" menu
 */

const SHEET_FILES   = 'Drive Index';
const SHEET_DUPES   = 'Possible Duplicates';
const SHEET_SUMMARY = 'Summary';
const PROPS         = PropertiesService.getScriptProperties();
const TIME_BUDGET_MS = 4.5 * 60 * 1000;   // stop before the 6-minute wall
const PAGE_SIZE      = 200;

const HEADERS = [
  'Name', 'Type', 'Size (bytes)', 'Created', 'Last Modified',
  'Owner', 'Location', 'Drive', 'Folder Path', 'URL', 'File ID'
];

// Folder id -> {name, parent} cache, persisted across resumed runs.
let FOLDER_CACHE = null;

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Drive Index')
    .addItem('1. Start fresh index', 'startIndex')
    .addItem('2. Continue (if it timed out)', 'continueIndex')
    .addSeparator()
    .addItem('Find possible duplicates', 'findDuplicates')
    .addItem('Build summary', 'buildSummary')
    .addSeparator()
    .addItem('Reset', 'resetIndex')
    .addToUi();
}

/* ------------------------------------------------------------------ indexing */

function startIndex() {
  const ss = SpreadsheetApp.getActive();
  let sheet = ss.getSheetByName(SHEET_FILES);
  if (sheet) ss.deleteSheet(sheet);
  sheet = ss.insertSheet(SHEET_FILES);
  sheet.appendRow(HEADERS);
  sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
  sheet.setFrozenRows(1);

  PROPS.deleteProperty('pageToken');
  PROPS.deleteProperty('folderCache');
  PROPS.setProperty('count', '0');
  runIndex_();
}

function continueIndex() {
  if (!PROPS.getProperty('pageToken')) {
    ui_('Nothing to continue — the index either finished or was never started.');
    return;
  }
  runIndex_();
}

function resetIndex() {
  PROPS.deleteProperty('pageToken');
  PROPS.deleteProperty('folderCache');
  PROPS.deleteProperty('count');
  ui_('Reset. Run "Start fresh index" to begin again.');
}

function runIndex_() {
  const started = Date.now();
  const ss      = SpreadsheetApp.getActive();
  const sheet   = ss.getSheetByName(SHEET_FILES);
  if (!sheet) { ui_('Run "Start fresh index" first.'); return; }

  loadFolderCache_();

  let pageToken = PROPS.getProperty('pageToken') || null;
  let count     = Number(PROPS.getProperty('count') || 0);
  let buffer    = [];

  try {
    do {
      const res = Drive.Files.list({
        q: 'trashed = false',
        pageSize: PAGE_SIZE,
        pageToken: pageToken,
        corpora: 'allDrives',
        includeItemsFromAllDrives: true,
        supportsAllDrives: true,
        fields: 'nextPageToken, files(id,name,mimeType,size,createdTime,' +
                'modifiedTime,owners(emailAddress),parents,webViewLink,driveId)'
      });

      (res.files || []).forEach(function (f) {
        buffer.push(rowFor_(f));
        count++;
      });

      pageToken = res.nextPageToken || null;

      if (buffer.length >= 500) {
        flush_(sheet, buffer);
        buffer = [];
      }

      if (Date.now() - started > TIME_BUDGET_MS) {
        flush_(sheet, buffer);
        saveState_(pageToken, count);
        ui_('Paused at ' + count + ' files (6-minute limit).\n\n' +
            'Run "2. Continue" to keep going.');
        return;
      }
    } while (pageToken);

    flush_(sheet, buffer);
    saveState_(null, count);
    PROPS.deleteProperty('pageToken');

    sheet.autoResizeColumns(1, 2);
    ui_('Done. Indexed ' + count + ' files.\n\n' +
        'Next: "Find possible duplicates" and "Build summary".');

  } catch (err) {
    flush_(sheet, buffer);
    saveState_(pageToken, count);
    ui_('Stopped on an error at ' + count + ' files:\n\n' + err.message +
        '\n\nProgress is saved — "2. Continue" will resume.');
  }
}

function rowFor_(f) {
  const isFolder = f.mimeType === 'application/vnd.google-apps.folder';
  return [
    f.name || '',
    isFolder ? 'Folder' : friendlyType_(f.mimeType),
    f.size ? Number(f.size) : '',
    f.createdTime  ? f.createdTime.substring(0, 10)  : '',
    f.modifiedTime ? f.modifiedTime.substring(0, 10) : '',
    (f.owners && f.owners[0]) ? f.owners[0].emailAddress : '',
    f.driveId ? 'Shared Drive' : 'My Drive',
    f.driveId ? driveName_(f.driveId) : '',
    folderPath_(f.parents),
    f.webViewLink || '',
    f.id
  ];
}

function flush_(sheet, rows) {
  if (!rows.length) return;
  sheet.getRange(sheet.getLastRow() + 1, 1, rows.length, HEADERS.length)
       .setValues(rows);
  SpreadsheetApp.flush();
}

function saveState_(pageToken, count) {
  if (pageToken) PROPS.setProperty('pageToken', pageToken);
  PROPS.setProperty('count', String(count));
  saveFolderCache_();
}

/* -------------------------------------------------------------- folder paths */

function loadFolderCache_() {
  if (FOLDER_CACHE) return;
  const raw = PROPS.getProperty('folderCache');
  FOLDER_CACHE = raw ? JSON.parse(raw) : {};
}

function saveFolderCache_() {
  if (!FOLDER_CACHE) return;
  try {
    PROPS.setProperty('folderCache', JSON.stringify(FOLDER_CACHE));
  } catch (e) {
    // Properties cap out around 9KB per value. If the cache outgrows it,
    // drop it — paths just get resolved again next run.
    PROPS.deleteProperty('folderCache');
  }
}

function folderPath_(parents) {
  if (!parents || !parents.length) return '';
  const segments = [];
  let id = parents[0];
  let guard = 0;

  while (id && guard++ < 12) {
    const meta = folderMeta_(id);
    if (!meta) break;
    segments.unshift(meta.name);
    id = meta.parent;
  }
  return segments.join(' / ');
}

function folderMeta_(id) {
  loadFolderCache_();
  if (FOLDER_CACHE[id] !== undefined) return FOLDER_CACHE[id];
  try {
    const f = Drive.Files.get(id, {
      fields: 'id,name,parents',
      supportsAllDrives: true
    });
    FOLDER_CACHE[id] = { name: f.name, parent: (f.parents && f.parents[0]) || null };
  } catch (e) {
    FOLDER_CACHE[id] = null;   // no access, or it's a drive root
  }
  return FOLDER_CACHE[id];
}

function driveName_(driveId) {
  loadFolderCache_();
  const key = 'drive:' + driveId;
  if (FOLDER_CACHE[key] !== undefined) {
    return FOLDER_CACHE[key] ? FOLDER_CACHE[key].name : '';
  }
  try {
    const d = Drive.Drives.get(driveId);
    FOLDER_CACHE[key] = { name: d.name, parent: null };
    return d.name;
  } catch (e) {
    FOLDER_CACHE[key] = null;
    return '';
  }
}

/* ----------------------------------------------------------------- duplicates */

/**
 * Flags files sharing a name, and files sharing name AND byte size —
 * the latter being near-certain duplicates.
 */
function findDuplicates() {
  const ss    = SpreadsheetApp.getActive();
  const src   = ss.getSheetByName(SHEET_FILES);
  if (!src || src.getLastRow() < 2) { ui_('Build the index first.'); return; }

  const data  = src.getRange(2, 1, src.getLastRow() - 1, HEADERS.length).getValues();
  const byName = {};

  data.forEach(function (r) {
    if (r[1] === 'Folder') return;
    const key = String(r[0]).trim().toLowerCase();
    (byName[key] = byName[key] || []).push(r);
  });

  const out = [['Name', 'Copies', 'Same size?', 'Sizes', 'Dates modified', 'File IDs']];

  Object.keys(byName).forEach(function (key) {
    const group = byName[key];
    if (group.length < 2) return;
    const sizes = group.map(function (r) { return r[2]; });
    const allSame = sizes.every(function (s) { return s === sizes[0]; });
    out.push([
      group[0][0],
      group.length,
      allSame ? 'YES — likely identical' : 'no',
      sizes.join(', '),
      group.map(function (r) { return r[4]; }).join(', '),
      group.map(function (r) { return r[10]; }).join(', ')
    ]);
  });

  let sheet = ss.getSheetByName(SHEET_DUPES);
  if (sheet) ss.deleteSheet(sheet);
  sheet = ss.insertSheet(SHEET_DUPES);
  sheet.getRange(1, 1, out.length, out[0].length).setValues(out);
  sheet.getRange(1, 1, 1, out[0].length).setFontWeight('bold');
  sheet.setFrozenRows(1);
  sheet.autoResizeColumns(1, 3);

  ui_('Found ' + (out.length - 1) + ' names with more than one copy.');
}

/* -------------------------------------------------------------------- summary */

function buildSummary() {
  const ss  = SpreadsheetApp.getActive();
  const src = ss.getSheetByName(SHEET_FILES);
  if (!src || src.getLastRow() < 2) { ui_('Build the index first.'); return; }

  const data = src.getRange(2, 1, src.getLastRow() - 1, HEADERS.length).getValues();

  const byType = {}, byYear = {}, byOwner = {}, byLocation = {};
  let totalBytes = 0;

  data.forEach(function (r) {
    byType[r[1]]     = (byType[r[1]]     || 0) + 1;
    byOwner[r[5]]    = (byOwner[r[5]]    || 0) + 1;
    byLocation[r[6]] = (byLocation[r[6]] || 0) + 1;
    const year = String(r[4]).substring(0, 4);
    if (year) byYear[year] = (byYear[year] || 0) + 1;
    if (typeof r[2] === 'number') totalBytes += r[2];
  });

  const out = [];
  out.push(['DRIVE INDEX SUMMARY', '']);
  out.push(['Generated', new Date()]);
  out.push(['Total items', data.length]);
  out.push(['Total size', (totalBytes / 1073741824).toFixed(2) + ' GB']);
  out.push(['', '']);

  out.push(['LOCATION', 'Count']);
  Object.keys(byLocation).sort().forEach(function (k) { out.push([k, byLocation[k]]); });
  out.push(['', '']);

  out.push(['BY TYPE', 'Count']);
  Object.keys(byType).sort(function (a, b) { return byType[b] - byType[a]; })
    .forEach(function (k) { out.push([k, byType[k]]); });
  out.push(['', '']);

  out.push(['BY YEAR LAST MODIFIED', 'Count']);
  Object.keys(byYear).sort().forEach(function (k) { out.push([k, byYear[k]]); });
  out.push(['', '']);

  out.push(['BY OWNER', 'Count']);
  Object.keys(byOwner).sort(function (a, b) { return byOwner[b] - byOwner[a]; })
    .forEach(function (k) { out.push([k || '(unknown)', byOwner[k]]); });

  let sheet = ss.getSheetByName(SHEET_SUMMARY);
  if (sheet) ss.deleteSheet(sheet);
  sheet = ss.insertSheet(SHEET_SUMMARY, 0);
  sheet.getRange(1, 1, out.length, 2).setValues(out);
  sheet.getRange(1, 1, 1, 2).setFontWeight('bold');
  sheet.autoResizeColumns(1, 2);

  ui_('Summary built. Check the "By Owner" section — anything not owned by you ' +
      'is likely student work or a colleague\'s file.');
}

/* ----------------------------------------------------------------- utilities */

function friendlyType_(mime) {
  const map = {
    'application/vnd.google-apps.document':     'Google Doc',
    'application/vnd.google-apps.spreadsheet':  'Google Sheet',
    'application/vnd.google-apps.presentation': 'Google Slides',
    'application/vnd.google-apps.form':         'Google Form',
    'application/vnd.google-apps.drawing':      'Google Drawing',
    'application/vnd.google-apps.script':       'Apps Script',
    'application/vnd.google-apps.shortcut':     'Shortcut',
    'application/pdf':                          'PDF',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document':   'Word',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':         'Excel',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'PowerPoint'
  };
  if (map[mime]) return map[mime];
  if (!mime) return 'Unknown';
  if (mime.indexOf('image/') === 0) return 'Image';
  if (mime.indexOf('video/') === 0) return 'Video';
  if (mime.indexOf('audio/') === 0) return 'Audio';
  return mime;
}

function ui_(msg) {
  try {
    SpreadsheetApp.getUi().alert(msg);
  } catch (e) {
    Logger.log(msg);   // running without a UI (e.g. from the editor)
  }
}
