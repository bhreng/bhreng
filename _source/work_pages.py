# -*- coding: utf-8 -*-
"""One page per assignment, with a stable URL and a downloads box.

Why this exists: Dan needs to link a single assignment to somebody -- in a
Classroom post, in an email, on a QR code taped to a machine -- without
sending them to a grade page and saying "scroll to Term 2". So every entry in
grade_work.WORK gets its own page at

    work/<grade>-<slug>.html

The slug is derived from the title and is STABLE: it is written down in
SLUG_OVERRIDE below for anything whose title might get edited later, so that
a link Dan sent in October still resolves in April. If you rename an
assignment, add the old slug to SLUG_OVERRIDE pointing at the new one rather
than letting the URL move.

Attachments: each assignment may carry a list of filenames in ATTACH. Those
files are copied out of ./attachments/ into site/files/ at build time and
offered as direct downloads on the assignment page. A filename that is
declared but missing from ./attachments/ is reported by the build and simply
not rendered, so a half-finished attachment list never produces a dead link.
"""

import os
import re
import unicodedata

# --------------------------------------------------------------------- slugs

SLUG_OVERRIDE = {
    # 'old-slug': 'new-slug',   # keep old links alive after a rename
}

_STRIP = re.compile(r'<[^>]+>')
_KEEP = re.compile(r'[^a-z0-9]+')


def _plain(s):
    s = _STRIP.sub('', s)
    for a, b in (('&amp;', 'and'), ('&mdash;', ' '), ('&ndash;', ' '),
                 ('&rsquo;', ''), ('&ldquo;', ''), ('&rdquo;', ''),
                 ('&hellip;', ''), ('&middot;', ' '), ('&rarr;', ' ')):
        s = s.replace(a, b)
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c))


def slug(title):
    s = _KEEP.sub('-', _plain(title).lower()).strip('-')
    return SLUG_OVERRIDE.get(s, s)


def page_name(grade_key, title):
    return 'work/%s-%s.html' % (grade_key, slug(title))


# ---------------------------------------------------------------- attachments
# filename -> (label, one line saying what it is and when you want it)
# The file itself must exist in ./attachments/ or it is skipped with a warning.

FILE_INFO = {
    'BHR27-Daily-Logbook.docx': (
        'Daily Logbook',
        'The running record of every shop day. Print it or keep it in Drive.'),
    'BHR27-Weekly-Planner.docx': (
        'Weekly Planner',
        'What you intend to get done this shop week, before the week starts.'),
    'BHR27-Weekly-Reflection.docx': (
        'Weekly Reflection',
        'The Friday counterpart to the planner: what actually happened.'),
    'BHR27-Project-Reflection.docx': (
        'Project Reflection',
        'At the end of a project. What worked, what you would change.'),
    'BHR27-Do-Now-Reflection.docx': (
        'Do Now Reflection',
        'The short write-up after a Do Now session.'),
    'BHR27-Mid-Project-Design-Review.docx': (
        'Mid-Project Design Review',
        'Partway through: where you are, and the one thing most likely '
        'to fail.'),
    'BHR27-Design-Brief-and-Initial-Planner.docx': (
        'Design Brief and Initial Planner',
        'The document that fixes what &ldquo;finished&rdquo; means, before '
        'you start.'),
    'BHR27-Instructor-Meeting-Notes.docx': (
        'Instructor Meeting Notes',
        'After a one-on-one. Action items with names and dates on them.'),
    'BHR27-Research-Log.xlsx': (
        'Research Log',
        'A spreadsheet. One new source a day is the target.'),
    'BHR27-Order-Request-Form.xlsx': (
        'Order Request Form',
        'A spreadsheet. The &ldquo;why you need it&rdquo; column is the one '
        'that gets it approved.'),
    'BHR27-Project-Gantt-Chart.xlsx': (
        'Project Gantt Chart',
        'A spreadsheet. Tasks on a calendar, to find where two of them '
        'collide.'),
    'BHR27-Part-List.xlsx': (
        'Part List',
        'A spreadsheet. Every part including the fasteners, made or bought.'),
    'BHR27-Independent-Focus-Proposal.docx': (
        'Independent Focus Proposal',
        'First day of the term. The idea, the work, the five weeks, and a '
        'review box for your instructor.'),
    'BHR27-Independent-Focus-Reflection.docx': (
        'Independent Focus Reflection',
        'Last day of the term. What got done, what changed, and where next '
        'term starts.'),
    'BHR27-Project-Rubric.pdf': (
        'Project Rubric',
        'The five criteria every project is graded on, with what each level '
        'means. The same rubric Classroom uses.'),
    'BHR27-Weekly-Grade-Rubric.pdf': (
        'Weekly Grade Rubric',
        'The six things assessed every shop week, level by level.'),
    'BHR27-Project-Rubric.xlsx': (
        'Project Rubric (Classroom import)',
        'The rubric in the shape Google Classroom reads. For instructors.'),
    'BHR27-Weekly-Grade-Rubric.xlsx': (
        'Weekly Grade Rubric (Classroom import)',
        'For instructors.'),
    'BHR27-Independent-Focus-Record.pdf': (
        'Independent Focus Record',
        'One page, one row per term, kept in your binder. The shape of what '
        'you chose across two years.'),
    'BHR27-Decision-Matrix.xlsx': (
        'Decision Matrix',
        'A spreadsheet. Weighted criteria against your concepts; the totals '
        'decide.'),
    'BHR27-Test-Log.xlsx': (
        'Test and Measurement Log',
        'A spreadsheet. Predicted, measured, and the difference &mdash; one '
        'row per reading.'),
    'BHR27-IO-Map-and-Commissioning.xlsx': (
        'I/O Map and Commissioning Checklist',
        'A spreadsheet. Every input and output on the system, and the '
        'checklist you commission it against.'),
    'BHR27-Welcome-Families.pdf': (
        'Welcome to BHR Engineering',
        'Three pages for parents and prospective students: what the shop is, '
        'the four years, and how choosing us works.'),
    'BHR27-Which-Document-When.pdf': (
        'Which document, and when',
        'One page. The whole document set and the moment each one is for.'),
}

# grade key -> { assignment title -> [filenames] }
# Everything here is a document THIS PROJECT built. Nothing is invented:
# if an assignment is not listed, it simply has no attachment yet.
LOG = 'BHR27-Daily-Logbook.docx'
PLAN = 'BHR27-Weekly-Planner.docx'
WREF = 'BHR27-Weekly-Reflection.docx'
PREF = 'BHR27-Project-Reflection.docx'
DONOW = 'BHR27-Do-Now-Reflection.docx'
MID = 'BHR27-Mid-Project-Design-Review.docx'
BRIEF = 'BHR27-Design-Brief-and-Initial-Planner.docx'
MEET = 'BHR27-Instructor-Meeting-Notes.docx'
RLOG = 'BHR27-Research-Log.xlsx'
ORDER = 'BHR27-Order-Request-Form.xlsx'
GANTT = 'BHR27-Project-Gantt-Chart.xlsx'
PARTS = 'BHR27-Part-List.xlsx'
DMX = 'BHR27-Decision-Matrix.xlsx'
TLOG = 'BHR27-Test-Log.xlsx'
IOMAP = 'BHR27-IO-Map-and-Commissioning.xlsx'
PROP = 'BHR27-Independent-Focus-Proposal.docx'
REFL = 'BHR27-Independent-Focus-Reflection.docx'
RUB = 'BHR27-Project-Rubric.pdf'
WRUB = 'BHR27-Weekly-Grade-Rubric.pdf'
RECORD = 'BHR27-Independent-Focus-Record.pdf'
GUIDE = 'BHR27-Which-Document-When.pdf'

# What each KIND of assignment offers by default. A short project gets the
# brief and the reflection; a long one adds the mid-project review and the
# planning sheets; a course or admin entry gets only the logbook.
KIND_ATTACH = {
    'project':    [RUB, LOG, BRIEF, PREF],
    'skills':     [LOG, DONOW],
    'reflection': [LOG, PREF],
    'course':     [LOG],
    'admin':      [LOG],
}

# Per-assignment overrides, by exact title. These are sensible defaults, not
# a teaching decision -- retune freely.
ATTACH = {
    '11': {
        'Full Scope Project':      [RUB, LOG, BRIEF, GANTT, PARTS, MID, PREF],
        'ADU Design Project':      [RUB, LOG, BRIEF, MID, PREF],
        'City Design':             [RUB, LOG, BRIEF, MID, PREF],
        'Tiny House':              [RUB, LOG, BRIEF, PARTS, PREF],
        'Speaker Design':          [RUB, LOG, BRIEF, DMX, TLOG, PARTS, PREF],
        'Intro to ESEC: Arduino':  [LOG, TLOG],
        'Elegoo Uno Project Kit':  [LOG, TLOG],
        'VEX V5 Clawbot Project':  [RUB, LOG, IOMAP, TLOG],
        'Robotic Arm Build':       [RUB, LOG, IOMAP, TLOG, PARTS],
        'Simple Machines to Functional Mechanisms': [RUB, LOG, DMX, TLOG, PREF],
        'Grade 11 Capstone':       [RUB, LOG, BRIEF, GANTT, PARTS, ORDER, MID,
                                    RLOG, PREF],
        'Reflection Portfolio Presentation': [LOG, PREF],
        'Independent Focus':       [PROP, REFL, RECORD, LOG, PLAN, WREF, MEET],
        'Gmetrix':                 [LOG],
    },
    '12': {
        'Design a Laptop':         [RUB, LOG, BRIEF, PREF],
        'Shop Equipment Project':  [RUB, LOG, PLAN, WREF, PREF],
        'Industrial Design Challenge: The LED Desk Lamp':
                                   [RUB, LOG, BRIEF, DMX, PARTS, TLOG, PREF],
        'Research &amp; Analysis: LTT Screwdriver': [LOG, RLOG],
        'Holiday Collaborative Rube Goldberg Machine': [RUB, LOG, PARTS, TLOG],
        'Mars Colony Design':      [RUB, LOG, BRIEF, MID, PREF],
        'Bunker House Design':     [RUB, LOG, BRIEF, PREF],
        'Senior Capstone':         [RUB, LOG, BRIEF, GANTT, PARTS, ORDER, RLOG,
                                    MID, MEET, PREF],
        'Independent Focus':       [PROP, REFL, RECORD, LOG, PLAN, WREF, MEET],
        'Platform training':       [LOG],
    },
}

# Files offered on every assignment page that has no specific list of its own.
# The logbook is genuinely universal; the rest are opt-in per assignment.
DEFAULT_ATTACH = ['BHR27-Daily-Logbook.docx']

SRC_DIR = 'attachments'
OUT_DIR = 'files'


def declared_files():
    """Every filename any assignment asks for, plus the defaults."""
    seen = set(DEFAULT_ATTACH)
    for grade in ATTACH.values():
        for names in grade.values():
            seen.update(names)
    return sorted(seen)


def available(root='.'):
    """Every file sitting in ./attachments/.

    All of them are copied to site/files/ and are therefore linkable, whether
    or not any assignment currently declares them -- so a file Dan drops in
    is immediately available to attach, and a link he writes by hand to
    files/<name> works straight away.
    """
    d = os.path.join(root, SRC_DIR)
    if not os.path.isdir(d):
        return set()
    return {f for f in os.listdir(d)
            if not f.startswith('.') and os.path.isfile(os.path.join(d, f))}


def files_for(grade_key, title, have, kind=None):
    names = ATTACH.get(grade_key, {}).get(title)
    if names is None:
        names = KIND_ATTACH.get(kind, DEFAULT_ATTACH)
    return [n for n in names if n in have]


# ------------------------------------------------------------------ rendering

CSS = '''
/* --- one assignment, on its own page ----------------------------------- */
.workpage{--accent:var(--g-ink);--accent-soft:var(--g-soft)}
.wtop{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 0 14px}
.wtop a.back{font-family:var(--mono);font-size:10.5px;letter-spacing:.11em;
  text-transform:uppercase;color:var(--g-ink);font-weight:700;
  text-decoration:none;border:1px solid var(--rule);border-radius:3px;
  padding:4px 9px}
.wtop a.back:hover{background:var(--g-soft);border-color:var(--g-ink)}
.wtop .crumb{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink-3)}

.whero{border:1px solid var(--rule);border-left:5px solid var(--g-ink);
  border-radius:0 8px 8px 0;background:var(--card);padding:22px 26px 24px;
  margin:0 0 20px}
.whero .wtags{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 10px}
.whero .wtags span{font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;
  text-transform:uppercase;font-weight:700;border:1px solid var(--rule);
  border-radius:2px;padding:2px 7px;color:var(--ink-3)}
.whero .wtags span.k{color:var(--g-ink);border-color:var(--g-ink)}
.whero h1{margin:0;font-family:var(--sans);font-weight:var(--w-heavy);
  font-size:clamp(24px,3.6vw,34px);line-height:1.1;letter-spacing:-.02em;
  color:var(--ink)}
.whero .whook{margin:11px 0 0;font-size:17.5px;line-height:1.5;
  color:var(--ink-2);max-width:60ch}

/* the downloads box */
.dlbox{border:1px solid var(--rule);border-radius:7px;overflow:hidden;
  margin:22px 0 0;background:var(--card)}
.dlbox .dlh{margin:0;padding:10px 16px;background:var(--g-soft);
  font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--g-ink);font-weight:700}
.dlbox a{display:flex;align-items:baseline;gap:12px;padding:13px 16px;
  text-decoration:none;border-top:1px solid var(--rule-soft)}
.dlbox a:hover{background:var(--g-soft)}
.dlbox a b{font-family:var(--sans);font-size:15.5px;color:var(--g-ink);
  flex:none}
.dlbox a span{font-size:14px;line-height:1.45;color:var(--ink-2)}
.dlbox a em{margin-left:auto;flex:none;font-style:normal;font-family:var(--mono);
  font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--ink-3);border:1px solid var(--rule);border-radius:2px;
  padding:1px 6px}

/* prev / next along the term */
.wnav{display:flex;gap:12px;margin:24px 0 0;flex-wrap:wrap}
.wnav a{flex:1 1 240px;border:1px solid var(--rule);border-radius:6px;
  padding:12px 15px;text-decoration:none;background:var(--card)}
.wnav a:hover{border-color:var(--g-ink);background:var(--g-soft)}
.wnav .lb{display:block;font-family:var(--mono);font-size:9.5px;
  letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);
  margin:0 0 3px}
.wnav .tt{display:block;font-family:var(--sans);font-weight:600;font-size:15px;
  color:var(--g-ink);line-height:1.3}
.wnav a.nx{text-align:right}
'''


def _dl_box(names, depth):
    if not names:
        return ''
    r = '../' * depth
    o = ['<div class="dlbox">',
         '  <p class="dlh">Download</p>']
    for n in names:
        label, what = FILE_INFO.get(n, (n, ''))
        ext = n.rsplit('.', 1)[-1].upper()
        o.append('  <a href="%s%s/%s" download><b>%s</b><span>%s</span>'
                 '<em>%s</em></a>' % (r, OUT_DIR, n, label, what, ext))
    o.append('</div>')
    return '\n'.join(o)


def render(g, a, full, body_html, prev_a, next_a, dl_names, depth=1):
    """One assignment page body.

    g          the grade dict
    a          the assignment dict
    full       the full brief HTML, or ''
    body_html  the shared .asg block, already rendered by build_grades
    prev/next  neighbouring assignment dicts within the same term, or None
    dl_names   attachment filenames that exist
    """
    r = '../' * depth
    style = ('--g-lt:%s;--g-dk:%s;--g-slt:%s;--g-sdk:%s'
             % (g['ink'], g['ink_dark'], g['soft'], g['soft_dark']))
    o = ['<div class="wrap gradepage workpage" style="%s">' % style,
         '<div class="wtop">',
         '  <a class="back" href="%sgrades/%s.html">&larr; Grade %d</a>'
         % (r, g['key'], g['num']),
         '  <span class="crumb">%s &middot; %s</span>' % (g['course'], a['w']),
         '</div>',
         body_html,
         _dl_box(dl_names, depth)]

    nav = []
    if prev_a:
        nav.append('  <a class="pv" href="%s%s"><span class="lb">Previous'
                   '</span><span class="tt">%s</span></a>'
                   % (r, page_name(g['key'], prev_a['title']),
                      prev_a['title']))
    if next_a:
        nav.append('  <a class="nx" href="%s%s"><span class="lb">Next</span>'
                   '<span class="tt">%s</span></a>'
                   % (r, page_name(g['key'], next_a['title']),
                      next_a['title']))
    if nav:
        o.append('<div class="wnav">')
        o.extend(nav)
        o.append('</div>')

    o.append(
        '<section><div class="note acc"><p><strong>This is the reference '
        'copy, not the gradebook.</strong> What is due, and when, lives in '
        'Google Classroom. This page exists so the brief stays findable, and '
        'so it can be linked to on its own.</p></div></section>')
    o.append('</div>')
    return '\n'.join(o)
