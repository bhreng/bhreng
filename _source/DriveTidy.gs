/**
 * DriveTidy — clears My Drive's root into the BHR ENG folder structure.
 *
 * WHY THIS EXISTS
 * The root had 57 folders and several hundred loose files. Moving them one
 * at a time through an API is hundreds of round trips; this does the whole
 * pass server-side in one run, and it is re-runnable — anything that lands
 * at the root later gets filed the next time you run it.
 *
 * WHAT IT WILL NOT DO
 *   - It never deletes anything. Junk goes to _to_delete for you to review.
 *   - It never touches the Classroom folder, or BHR ENG 2026-2027 SY.
 *   - Anything it cannot classify goes to _unsorted rather than being
 *     guessed at. Check that folder when it finishes.
 *
 * HOW TO RUN
 *   1. script.google.com  ->  New project
 *   2. Paste this in, replacing the default myFunction().
 *   3. Run  ->  tidyRoot.  Approve the permission prompt (it needs Drive).
 *   4. View -> Logs to see what moved where.
 *
 * Run it twice if it times out — Apps Script caps a run at ~6 minutes and
 * the script picks up where it left off, because moved files are no longer
 * at the root.
 */

// ---------------------------------------------------------------- targets
// These are the folders already created in your Drive. If you rename a
// folder that is fine — these are IDs, not names. If you DELETE one, the
// script will stop with a clear error rather than putting files somewhere
// unexpected.
var F = {
  program:     '16F_MIRWhVebywfyYC69h85_XBMvaOgGF',
  curriculum:  '1JELx9D9r-jkvfXAGmqC7YoOvPwJhq5s_',
  templates:   '1DNIlM3DHcJ6-0PAHYNoe9gsIsr9Tqti8',
  branding:    '113yuBg0T06QFTU-gxGf3Znhd6SnVYqHg',
  equipment:   '1ZRviGfoSRPagxRmFRGReqOoPEZBbM0X5',
  festo:       '1VFNj4SFktdxgRqQGYaLuw0kg4dbF6BRi',
  projects:    '1MdiIR9ugPnaRpEJEZ9OWM0w74WO3fb7t',

  admin:       '1CNqF3-Iw4Bg6Wjy2iifGhSymCAwMPO78',
  budgets:     '1nyl7aWzB-t7jSgvK_nMt6rWtmXMOTP7n',
  eoy:         '1INXjmAi7Ah2h5yyXvE9sUp1mxAB5oqQo',
  advisory:    '1mpaL1RlIBYZ6Ipx3Mofvf31nSiqBPGlN',
  openhouse:   '1IS-pmVd4RlHErWxU_Qp8qGbkQROXKq5l',
  skills:      '1oufUuq5elC7EIOcyaacjN0obMEeNn7DK',

  students:    '1PR6einuoZzY6BWMEToswiecFs0fPx7Cl',

  archive:     '1nR5GWAr-5eKiWPFJlTq7_HBruHWj-i3-',
  pastwork:    '1vRgfyWnCC5w3iNDKRryGtTBo8wCTaRSO',
  media:       '12QbYm7B6_jAfKLL9LM6PkcVAGKI97oFl',

  todelete:    '1R93iED79-Yss6pPgEwyXn2XdgzD3qvaZ'
};

// Folders at the root that must be left exactly where they are.
var LEAVE_ALONE = {
  '0B9T1lRc3Pf4lflVhdlkxRVZFWm9CLUlsUlFmRVIwOWZKUW5wVUs3bnlkb1Q3aVZJZVVlOTA': 'Classroom',
  '1rxF32VDv_aVzQDow82Hyw9vVnY2JuIMQ': 'BHR ENG 2026-2027 SY'
};

// --------------------------------------------------------------- the rules
// First match wins, so order matters: the most specific patterns are first.
// Student data is matched before anything else so it can never be caught by
// a looser rule further down.
var RULES = [
  // ---- student data. Always first. -------------------------------------
  {to: 'students',   re: /recommendation letter/i},
  {to: 'students',   re: /enrollment letter/i},
  {to: 'students',   re: /scholarship .*letter|letter.*scholarship/i},
  {to: 'students',   re: /final placement|class of 20\d\d/i},
  {to: 'students',   re: /\broster\b|\bgrades?\b.*\blist\b/i},

  // ---- obvious junk ----------------------------------------------------
  {to: 'todelete',   re: /^untitled (document|presentation|spreadsheet)/i},
  {to: 'todelete',   re: /^google keep document$/i},
  {to: 'todelete',   re: /^(vd|vd2)\.pdf$/i},
  {to: 'todelete',   re: /^copy of .*by slidesgo/i},

  // ---- equipment, software, print --------------------------------------
  {to: 'festo',      re: /^(handling|conveyor|stacking_magazine)_/i},
  {to: 'equipment',  re: /3d print calculator|print farm/i},
  {to: 'equipment',  re: /\.stl$|\.obj$|\.mtl$|\.fbx$|\.dwt$/i},
  {to: 'equipment',  re: /dogbot|drone program|urbot|ur5|bambu|elegoo|vex/i},

  // ---- curriculum and standards ----------------------------------------
  {to: 'curriculum', re: /curriculum map|priority standards|voc standards/i},
  {to: 'curriculum', re: /unit template|scope and sequence|frameworks/i},
  {to: 'curriculum', re: /overview of program|structure \d/i},

  // ---- the documents students fill in ----------------------------------
  {to: 'templates',  re: /design brief|initial planner/i},
  {to: 'templates',  re: /weekly planner|weekly reflection|daily journal/i},
  {to: 'templates',  re: /logbook|research log|order request/i},
  {to: 'templates',  re: /lesson plan template|lesson template/i},
  {to: 'templates',  re: /work breakdown structure|gantt chart/i},

  // ---- administration --------------------------------------------------
  {to: 'budgets',    re: /budget|money spent/i},
  {to: 'eoy',        re: /e\.?o\.?y\.? report|end of year report/i},
  {to: 'skills',     re: /skills ?usa|^skills ?-|skills \d{4}|industrial review/i},
  {to: 'advisory',   re: /advisory/i},
  {to: 'openhouse',  re: /open house|showcase/i},
  {to: 'admin',      re: /grant|partner letter|newsletter|dsc update/i},
  {to: 'admin',      re: /sub plan|instructor rotation|resume|schedule/i},
  {to: 'admin',      re: /meeting|shop redesign/i},

  // ---- teaching material -----------------------------------------------
  {to: 'projects',   re: /roles of an engineer|full scope|reflection essay/i},
  {to: 'projects',   re: /welcome to bhr|videos for engineering|bookmarks/i},
  {to: 'projects',   re: /planner text|daily planner|project timeline/i},
  {to: 'media',      re: /\.(png|jpe?g|gif|mp4|mov|mp3|wav)$/i}
];

// Files with no rule match land here so nothing is silently misfiled.
var UNSORTED_NAME = '_unsorted — review me';

// ------------------------------------------------------------------- main

function tidyRoot() {
  var root = DriveApp.getRootFolder();
  var dest = resolveTargets_();
  var unsorted = getOrCreateChild_(root, UNSORTED_NAME);

  var counts = {};
  var moved = 0, skipped = 0, failed = 0;

  // --- loose files -------------------------------------------------------
  var files = root.getFiles();
  while (files.hasNext()) {
    var file = files.next();
    var name = file.getName();
    var key = classify_(name, file.getMimeType());
    var target = key ? dest[key] : unsorted;
    var label = key || 'unsorted';

    try {
      file.moveTo(target);
      counts[label] = (counts[label] || 0) + 1;
      moved++;
    } catch (e) {
      Logger.log('COULD NOT MOVE  ' + name + '  —  ' + e.message);
      failed++;
    }
  }

  // --- folders -----------------------------------------------------------
  // Any folder still at the root is either one of ours, one to leave alone,
  // or something new. New ones go to _unsorted so you can look at them.
  var ours = {};
  for (var k in F) ours[F[k]] = true;

  var folders = root.getFolders();
  while (folders.hasNext()) {
    var folder = folders.next();
    var id = folder.getId();
    if (ours[id] || LEAVE_ALONE[id] || folder.getName() === UNSORTED_NAME) {
      skipped++;
      continue;
    }
    try {
      folder.moveTo(unsorted);
      counts['unsorted (folder)'] = (counts['unsorted (folder)'] || 0) + 1;
      moved++;
    } catch (e) {
      Logger.log('COULD NOT MOVE FOLDER  ' + folder.getName() + '  —  ' + e.message);
      failed++;
    }
  }

  // --- report ------------------------------------------------------------
  Logger.log('');
  Logger.log('=== DriveTidy finished ===');
  Logger.log('moved:   ' + moved);
  Logger.log('left as-is: ' + skipped + '  (your folders, Classroom, the SY folder)');
  if (failed) Logger.log('failed:  ' + failed + '  — see the lines above');
  Logger.log('');
  Logger.log('where things went:');
  var keys = Object.keys(counts).sort();
  for (var i = 0; i < keys.length; i++) {
    Logger.log('  ' + pad_(keys[i], 22) + counts[keys[i]]);
  }
  Logger.log('');
  Logger.log('Nothing was deleted. Review "_to_delete" and');
  Logger.log('"' + UNSORTED_NAME + '" before emptying either.');
}


/** Dry run: logs what WOULD happen and changes nothing. Run this first. */
function previewTidyRoot() {
  var root = DriveApp.getRootFolder();
  var files = root.getFiles();
  var counts = {}, examples = {};
  var n = 0;

  while (files.hasNext()) {
    var file = files.next();
    var key = classify_(file.getName(), file.getMimeType()) || 'unsorted';
    counts[key] = (counts[key] || 0) + 1;
    if (!examples[key]) examples[key] = file.getName();
    n++;
  }

  Logger.log('=== PREVIEW — nothing has been moved ===');
  Logger.log(n + ' loose files at the root');
  Logger.log('');
  var keys = Object.keys(counts).sort();
  for (var i = 0; i < keys.length; i++) {
    Logger.log(pad_(keys[i], 22) + pad_(String(counts[keys[i]]), 6)
               + 'e.g. ' + examples[keys[i]]);
  }
  Logger.log('');
  Logger.log('Happy with that? Run tidyRoot.');
}


// ------------------------------------------------------------------ helpers

function classify_(name, mime) {
  // Shortcuts are pointers to other people's files. Yours are all bulk
  // shares from May 2024 and none of them resolve to anything you own.
  if (mime === 'application/vnd.google-apps.shortcut') return 'todelete';

  for (var i = 0; i < RULES.length; i++) {
    if (RULES[i].re.test(name)) return RULES[i].to;
  }
  return null;
}

function resolveTargets_() {
  var dest = {};
  for (var key in F) {
    try {
      dest[key] = DriveApp.getFolderById(F[key]);
    } catch (e) {
      throw new Error('Target folder "' + key + '" (' + F[key] + ') is gone. '
        + 'Recreate it or fix the ID at the top of this script before running.');
    }
  }
  return dest;
}

function getOrCreateChild_(parent, name) {
  var it = parent.getFoldersByName(name);
  return it.hasNext() ? it.next() : parent.createFolder(name);
}

function pad_(s, n) {
  while (s.length < n) s += ' ';
  return s;
}


/* ======================================================================
 *  BLANK TEMPLATE SWEEP  —  built for thousands of files
 *
 *  WHAT HAPPENED
 *  Every time a doc is attached to a Classroom assignment, Classroom
 *  duplicates it into that class's Drive folder. Do that across several
 *  years and several classes and you get thousands of copies. None of
 *  them was ever opened.
 *
 *  THE ONE SAFETY RULE
 *  A file is only swept if it was NEVER EDITED after it was created —
 *  modified within two minutes of creation. One keystroke of a student's
 *  work, or a version you tweaked, has a later modified time and is left
 *  exactly where it is. Everything the sweep declines to touch is
 *  reported so you can see it.
 *
 *  IT FINISHES ITSELF
 *  Apps Script stops any single run at six minutes, which is nowhere near
 *  enough for thousands of files. So this saves its place, schedules
 *  itself to pick up a minute later, and repeats until it is done. You
 *  click Run once and walk away. When it finishes it removes its own
 *  schedule and writes a final total to the log.
 *
 *  NOTHING IS TRASHED. Everything lands in _to_delete. To reclaim the
 *  storage afterwards: right-click the _to_delete FOLDER, move it to
 *  trash, then empty the trash. One action, however many thousand files
 *  are inside it.
 *
 *  START WITH previewSweep — it counts and changes nothing.
 * ====================================================================== */

// The templates that got duplicated. Whole-title match, case-insensitive.
// Add a line here if you spot another one; re-running is safe.
var SWEEP_TITLES = [
  /^BHR ENG - Engineering Daily Journal$/i,
  /^\d{4} Engineering Daily Journal$/i,
  /^Day \d+ Engineering Daily Journal$/i,
  /^Project Reflection Engineering Journal \d{4}$/i,
  /^BHR ENG Document - Logbook Template$/i,
  /^Senior Capstone - (Daily Journal|Weekly Planner|Weekly Reflection|Project Reflection|Design Brief|Instructor Meeting Notes|Research Log|Order Request Form)$/i,
  /^Independent Study - (Weekly Journal|Term Reflection|Initial Planner)$/i,
  /^Engineering (Project|Field Trip) Reflection$/i,
  /^Shop Equipment Project (Reflection|- Weekly Planner)$/i,
  /^Roles of an Engineer Project - Weekly Planner$/i,
  /^Roles of an Engine+r Project Reflection$/i,
  /^Mid-Project Design Review & Feasibility Check$/i,
  /^Engineering Do Now! - Reflection$/i,
  /^BHR ENG - Instructor Meeting Notes$/i,
  /^Grade 1[12] Capstone - Weekly (Planner|Reflection)$/i,
  /^Grade 1[12] BHR Engineering - Weekly Task Tracker \d{4}$/i,
  /^Grade 11 Capstone - (Unique Concept|Revitalization) Design Brief & Initial Planner\s*$/i,
  /^(BHR Engineering |Senior Capstone BHR Engineering )?Design Brief( & Initial Planner)?\s*$/i,
  /^What is a Design Brief$/i,
  /^Full Scope Project - Gantt chart$/i
];

var UNTOUCHED_MS   = 120 * 1000;   // "never edited" margin
var RUN_BUDGET_MS  = 4.5 * 60000;  // stop before Apps Script's 6-min cap
var PROP           = PropertiesService.getUserProperties();


// ---------------------------------------------------------------- entry

/** Counts only. Changes nothing. Run this first. */
function previewSweep() {
  var started = Date.now(), n = 0, kept = 0, bytes = 0;
  var byTitle = {};
  var it = DriveApp.searchFiles('"me" in owners and trashed = false');

  while (it.hasNext() && Date.now() - started < RUN_BUDGET_MS) {
    var f = it.next();
    if (!matches_(f.getName())) continue;
    if (edited_(f)) { kept++; continue; }
    byTitle[f.getName()] = (byTitle[f.getName()] || 0) + 1;
    bytes += f.getSize();
    n++;
  }

  Logger.log('=== PREVIEW — nothing has moved ===');
  Logger.log('');
  Logger.log('blank duplicates found : ' + n);
  Logger.log('space they occupy      : ' + mb_(bytes));
  Logger.log('skipped, because edited : ' + kept);
  if (it.hasNext()) {
    Logger.log('');
    Logger.log('(ran out of time before reaching the end — the real total is');
    Logger.log(' higher than this. sweepBlankTemplates handles that properly.)');
  }
  Logger.log('');
  logCounts_(byTitle);
  Logger.log('');
  Logger.log('Happy with that? Run sweepBlankTemplates once and leave it.');
}


/** The real thing. Click Run once — it reschedules itself until done. */
function sweepBlankTemplates() {
  PROP.deleteAllProperties();
  clearSweepTriggers_();
  Logger.log('Sweep started. It will keep going by itself; check back in a');
  Logger.log('few minutes and look at the execution log for the final total.');
  sweepChunk();
}


/** Stop a sweep that is part-way through. Safe — nothing is undone. */
function stopSweep() {
  clearSweepTriggers_();
  Logger.log('Stopped. ' + (PROP.getProperty('moved') || 0)
             + ' files already moved are in _to_delete. Nothing was undone.');
  Logger.log('Run sweepBlankTemplates again to resume from scratch, or');
  Logger.log('leave it — re-running only ever finds what is still out there.');
}


// ------------------------------------------------------------- the work

function sweepChunk() {
  var started = Date.now();
  var bin = DriveApp.getFolderById(F.todelete);

  var token = PROP.getProperty('token');
  var it = token ? DriveApp.continueFileIterator(token)
                 : DriveApp.searchFiles('"me" in owners and trashed = false');

  var moved  = Number(PROP.getProperty('moved')  || 0);
  var kept   = Number(PROP.getProperty('kept')   || 0);
  var bytes  = Number(PROP.getProperty('bytes')  || 0);
  var passes = Number(PROP.getProperty('passes') || 0) + 1;

  while (it.hasNext()) {
    if (Date.now() - started > RUN_BUDGET_MS) {
      PROP.setProperties({
        token: it.getContinuationToken(),
        moved: String(moved), kept: String(kept),
        bytes: String(bytes), passes: String(passes)
      });
      scheduleNext_();
      Logger.log('pass ' + passes + ': ' + moved + ' moved so far ('
                 + mb_(bytes) + '). Continuing in about a minute.');
      return;
    }

    var f = it.next();
    if (!matches_(f.getName())) continue;
    if (edited_(f)) { kept++; continue; }

    try {
      bytes += f.getSize();
      f.moveTo(bin);
      moved++;
    } catch (e) {
      // A file inside a Classroom folder can refuse to move. Skip it and
      // carry on rather than losing the whole run to one bad file.
      Logger.log('skipped (' + e.message + '): ' + f.getName());
    }
  }

  // Finished.
  clearSweepTriggers_();
  PROP.deleteAllProperties();

  Logger.log('');
  Logger.log('=== SWEEP COMPLETE ===');
  Logger.log('passes taken           : ' + passes);
  Logger.log('blank duplicates moved : ' + moved);
  Logger.log('space freed once you empty _to_delete : ' + mb_(bytes));
  Logger.log('left alone, because edited            : ' + kept);
  Logger.log('');
  Logger.log('Nothing is trashed yet. To finish: right-click the _to_delete');
  Logger.log('FOLDER in Drive, Move to trash, then empty the trash. One');
  Logger.log('action, however many thousand files are inside.');
}


// ---------------------------------------------------------------- bits

function matches_(name) {
  for (var i = 0; i < SWEEP_TITLES.length; i++) {
    if (SWEEP_TITLES[i].test(name)) return true;
  }
  return false;
}

function edited_(file) {
  return file.getLastUpdated().getTime()
       - file.getDateCreated().getTime() > UNTOUCHED_MS;
}

function scheduleNext_() {
  ScriptApp.newTrigger('sweepChunk').timeBased().after(60 * 1000).create();
}

function clearSweepTriggers_() {
  var all = ScriptApp.getProjectTriggers();
  for (var i = 0; i < all.length; i++) {
    if (all[i].getHandlerFunction() === 'sweepChunk') {
      ScriptApp.deleteTrigger(all[i]);
    }
  }
}

function mb_(bytes) {
  return bytes > 1073741824
    ? (bytes / 1073741824).toFixed(2) + ' GB'
    : Math.round(bytes / 1048576) + ' MB';
}

function logCounts_(byTitle) {
  var keys = Object.keys(byTitle).sort(function (a, b) {
    return byTitle[b] - byTitle[a];
  });
  for (var i = 0; i < keys.length; i++) {
    Logger.log('  ' + pad_(String(byTitle[keys[i]]), 7) + keys[i]);
  }
}
