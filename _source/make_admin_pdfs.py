# -*- coding: utf-8 -*-
"""The teacher- and admin-facing set, as PDFs, in one look.

One rendering path for everything: Markdown (or an existing HTML body) ->
HTML with the site's palette and type -> Chromium print -> PDF. So the
binder, the pathway reports and the working notes come out of the same
mould, and none of them need to live on the student site.

The complete binder is assembled here from the section sources:
  Sections 1-4   binder/01 (draft scaffolding stripped)
  Section 5      binder/02
  Section 6      binder/03
  Section 7      Drive: "Binder 7: Curriculum Standards Analysis Report"
  Section 8      Drive: "Binder 8: DESE Voc Standards"
  Appendix A     the Word List (glossary)
The editorial matter that was inside the drafts -- change logs, open items,
notes to Dan -- is moved into its own document rather than deleted.
"""

import os
import re
import io
import glob
import subprocess
import markdown
import generation as G

HERE = os.path.dirname(os.path.abspath(__file__))
import paths
BIN = paths.BINDER
OUT = os.path.join(HERE, 'admin')
GF = paths.FONTS
LOGO = os.path.join(HERE, 'logo', 'header.png')

CSS = '''
@font-face{font-family:"Poppins";src:url("file://%(gf)s/Poppins-Regular.ttf");font-weight:400}
@font-face{font-family:"Poppins";src:url("file://%(gf)s/Poppins-Medium.ttf");font-weight:500}
@font-face{font-family:"Poppins";src:url("file://%(gf)s/Poppins-Bold.ttf");font-weight:700}
@font-face{font-family:"Lora";src:url("file://%(gf)s/Lora-Variable.ttf");font-weight:400 700}
@font-face{font-family:"Lora";src:url("file://%(gf)s/Lora-Italic-Variable.ttf");font-weight:400 700;font-style:italic}
:root{--ink:#262b39;--ink2:#4f5566;--ink3:#7d8394;--rule:#dedbd5;--accent:#6b4785;--soft:#f1ebf7;--paper:#fff}
@page{size:letter;margin:0.9in 0.8in 0.9in 0.8in}
html{font-size:10.2pt}
body{font-family:"Lora",Georgia,serif;color:var(--ink);line-height:1.5;margin:0}
h1,h2,h3,h4{font-family:"Poppins",sans-serif;color:var(--ink);line-height:1.15;margin:0}
h1{font-size:22pt;font-weight:700;letter-spacing:-.01em;margin:0 0 6pt;page-break-before:always;
   padding-bottom:8pt;border-bottom:2.5px solid var(--accent)}
h1.first,h1.nobreak{page-break-before:auto}
h2{font-size:14pt;font-weight:700;color:var(--accent);margin:18pt 0 5pt;page-break-after:avoid}
h3{font-size:11.2pt;font-weight:700;margin:13pt 0 3pt;page-break-after:avoid}
h4{font-size:10pt;font-weight:600;color:var(--ink2);margin:11pt 0 2pt;page-break-after:avoid}
p{margin:0 0 7pt}
ul,ol{margin:0 0 8pt;padding-left:18pt}
li{margin:0 0 3pt}
li p{margin:0}
strong{font-weight:700;color:var(--ink)}
em{font-style:italic}
code{font-family:"DejaVu Sans Mono",monospace;font-size:8.6pt;background:var(--soft);padding:0 3px;border-radius:2px}
pre{font-family:"DejaVu Sans Mono",monospace;font-size:8.4pt;background:var(--soft);padding:8pt 10pt;border-radius:4px;white-space:pre-wrap}
blockquote{margin:8pt 0;padding:7pt 12pt;border-left:3px solid var(--accent);background:var(--soft);color:var(--ink2)}
blockquote p{margin:0 0 4pt}
hr{border:0;border-top:1px solid var(--rule);margin:14pt 0}
table{border-collapse:collapse;width:100%%;margin:6pt 0 12pt;font-size:8.8pt;page-break-inside:auto}
tr{page-break-inside:avoid}
th{font-family:"Poppins",sans-serif;font-weight:600;font-size:8pt;text-align:left;color:#fff;background:var(--accent);
   padding:5pt 7pt;vertical-align:bottom}
td{padding:4.5pt 7pt;border-bottom:1px solid var(--rule);vertical-align:top}
tbody tr:nth-child(even) td{background:#f7f4fa}
td:first-child{font-family:"Poppins",sans-serif;font-weight:500;font-size:8.6pt;color:var(--accent)}
a{color:var(--accent);text-decoration:none}
del{color:var(--ink3)}
.cover{page-break-after:always;height:8.6in;display:flex;flex-direction:column;justify-content:flex-end}
.cover .band{background:var(--accent);color:#fff;padding:30pt 32pt 34pt;border-radius:8px}
.cover .kick{font-family:"Poppins";font-size:8.5pt;letter-spacing:.16em;text-transform:uppercase;opacity:.8;margin:0 0 10pt}
.cover h1{color:#fff;border:0;page-break-before:auto;font-size:30pt;margin:0 0 8pt;padding:0}
.cover .sub{font-family:"Poppins";font-weight:400;font-size:12.5pt;opacity:.92;margin:0}
.cover .meta{font-family:"Poppins";font-size:9pt;color:var(--ink2);margin:16pt 0 0}
.toc{page-break-after:always}
.toc h1{page-break-before:auto}
.toc ol{list-style:none;padding:0;margin:10pt 0}
.toc li{font-family:"Poppins";font-size:11pt;padding:6pt 0;border-bottom:1px solid var(--rule);display:flex;gap:12pt}
.toc li span.n{color:var(--accent);font-weight:700;width:26pt;flex:none}
.toc li span.d{color:var(--ink3);font-weight:400;font-size:9.5pt;margin-left:auto}
.note{border:1px solid var(--rule);border-left:4px solid var(--accent);background:var(--soft);padding:8pt 12pt;margin:10pt 0;border-radius:0 4px 4px 0}
.docmeta{font-family:"Poppins";font-size:8.6pt;color:var(--ink3);margin:0 0 14pt}
/* classes used by the inlined site reports */
.tw{margin:6pt 0 12pt}
td.k,th.k{font-family:"Poppins";font-weight:600;color:var(--accent)}
td.n,td.s{font-family:"Poppins";text-align:center}
td.old{color:var(--ink3);text-decoration:line-through}
td.use{font-family:"Poppins";font-weight:600;color:var(--accent)}
.mono{font-family:"DejaVu Sans Mono",monospace;font-size:8.4pt}
.eyebrow,.kicker{font-family:"Poppins";font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);margin:0 0 4pt}
.chip{display:inline-block;font-family:"Poppins";font-size:7.6pt;padding:1px 6px;border-radius:3px;background:var(--soft);color:var(--accent)}
.chip.c-ok{background:#e4f0e6;color:#2f6b3a}.chip.c-bad{background:#f8e6e6;color:#99332b}.chip.c-warn{background:#faf3e0;color:#8a6410}
.ntag{font-family:"Poppins";font-size:8pt;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700;margin:0 0 4pt}
dl.defs dt,dl dt{font-family:"Poppins";font-weight:700;margin:8pt 0 2pt}
dl.defs dd,dl dd{margin:0 0 6pt 0}
.lede,.intro,.tag,.blurb,.mh-sub{color:var(--ink2)}
.tq{font-style:italic;color:var(--ink3);margin:0 0 6pt}
.topic{margin:10pt 0 14pt}
.th{margin:0 0 4pt}.th .tn{display:inline-block;font-family:"Poppins";font-weight:700;color:var(--accent);margin-right:6pt}
.hero,.ph{margin:0 0 12pt}
.grid,.cards{display:block}
ul.files li,ul.ticks li{list-style:none;padding:3pt 0;border-bottom:1px solid var(--rule)}
.section,section{page-break-inside:auto}
.ban{display:grid;grid-template-columns:1.6in 1fr;gap:10pt;padding:5pt 0;border-bottom:1px solid var(--rule)}
.ban .term{font-family:"Poppins";font-weight:600;color:var(--ink3);text-decoration:line-through}
.ban .fix{color:var(--ink)}
td.dese{font-family:"DejaVu Sans Mono",monospace;font-size:8pt;color:var(--ink2)}
.rule-bar{height:2px;background:var(--accent);margin:8pt 0 14pt}
.masthead,.mh-top{display:none}
''' % {'gf': GF}

HEADER_TPL = '''<div style="font-family:Poppins,sans-serif;font-size:7.2px;color:#7d8394;
  width:100%%;padding:0 0.8in;display:flex;justify-content:space-between">
  <span>BHR Engineering Technology &middot; %s</span><span>Teacher and administration copy</span></div>'''
FOOTER_TPL = '''<div style="font-family:Poppins,sans-serif;font-size:7.2px;color:#7d8394;
  width:100%%;padding:0 0.8in;display:flex;justify-content:space-between">
  <span>Blue Hills Regional Technical School &middot; Room E-126 &middot; %s</span>
  <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'''


def _node_cwd():
    """playwright must be resolvable from where node runs. Try this folder
    (npm install here), then the user's home, then the global root."""
    for d in (HERE, os.path.expanduser('~')):
        if os.path.isdir(os.path.join(d, 'node_modules', 'playwright')):
            return d
    try:
        g = subprocess.run(['npm', 'root', '-g'], capture_output=True,
                           text=True).stdout.strip()
        if g and os.path.isdir(os.path.join(g, 'playwright')):
            os.environ['NODE_PATH'] = g
    except Exception:
        pass
    return HERE


def md2html(text):
    return markdown.markdown(text, extensions=['tables', 'sane_lists'])


def read(p):
    return io.open(p, encoding='utf-8').read()


# ------------------------------------------------------- binder assembly

def _strip_draft_scaffold(text, cut_headings):
    """Remove a top-of-file preamble and any named editorial sections
    (change log, open items, notes to Dan). Returns (clean, removed)."""
    removed = []
    # drop everything before the first "# Section" / "# 1.0" heading
    m = re.search(r'^# (?:Section|1\.0)', text, re.M)
    if m and m.start() > 0:
        removed.append(text[:m.start()])
        text = text[m.start():]
    for h in cut_headings:
        pat = re.compile(r'^(#{1,3} %s.*?)(?=^#{1,2} |\Z)' % re.escape(h),
                         re.S | re.M)
        mm = pat.search(text)
        if mm:
            removed.append(mm.group(1))
            text = text[:mm.start()] + text[mm.end():]
    return text, removed


def build_binder_md():
    s1, r1 = _strip_draft_scaffold(read(os.path.join(BIN, '01 - Sections 1-4 - Framework (DRAFT).md')),
                                   ['Change log'])
    s5, r5 = _strip_draft_scaffold(read(os.path.join(BIN, '02 - Section 5 - Program Overview (DRAFT).md')),
                                   ['What changed, and why', 'Open items'])
    s6, r6 = _strip_draft_scaffold(read(os.path.join(BIN, '03 - Section 6 - Scope and Sequence (DRAFT).md')),
                                   ['What changed', 'Notes for Dan'])
    s7 = read(os.path.join(BIN, '07 - Section 7 - Curriculum Standards Analysis.md'))
    s8 = read(os.path.join(BIN, '08 - Section 8 - DESE Standards and Skills.md'))

    # the five "NEW -- needs approval" task types are accepted into Section 4
    s1 = s1.replace('⚠ **The five entries below are new — they appear in Section 2 as pillar activities but have never been classified here. Approve, amend, or cut.**\n\n', '')
    s1 = s1.replace(' ⚠ NEW', '')
    s1 = s1.replace('including Independent Study reflections.', 'including the Independent Focus Reflection.')
    s1 = s1.replace('**Note:** the crosswalk names the Engineering Daily Logbook as the documentation requirement for Standard 3, which makes this the most consequential of the five omissions — the program\'s core documentation instrument had no entry in the document that classifies work.\n', '')
    s1 = s1.replace('**Replaces:** the Engineering Notebook, retired this past year.', '**Replaces:** the Engineering Notebook and the Engineering Daily Journal, both retired.')

    # Section 5 §6.3: the document set is now this project's set
    s5 = re.sub(r'## 6\.3 Documentation Templates.*?(?=\n---|\Z)',
                '## 6.3 Documentation Templates\n\n'
                'The full template set is maintained as Word and Excel files, '
                'downloadable from the program website (*Documents* page) and '
                'distributed through Google Classroom. The Daily Logbook is kept '
                'as a Google Doc master so its status-code dropdowns are inherited '
                'by every student copy.\n\n'
                '| Document | When |\n|---|---|\n'
                '| Daily Logbook | Every shop day |\n'
                '| Weekly Planner · Weekly Reflection | Monday and Friday of a shop week |\n'
                '| Design Brief and Initial Planner · Decision Matrix · Project Gantt Chart · Part List · Order Request Form | When a project starts |\n'
                '| Test and Measurement Log · I/O Map and Commissioning Checklist · Research Log · Mid-Project Design Review · Instructor Meeting Notes | While building and testing |\n'
                '| Project Reflection · Do Now Reflection | When something ends |\n'
                '| Independent Focus Proposal · Independent Focus Reflection · Independent Focus Record | First and last day of a term; the Record across two years |\n'
                '| Project Rubric · Weekly Grade Rubric | The rubrics Classroom grades against, in student-facing form |\n\n'
                'Their required fields are described in **4.3** above.\n',
                s5, flags=re.S)

    # the binder proper
    parts = [
        '# Section 1 — Instructor Specialization Overview' if not s1.startswith('# Section 1') else '',
        s1, s5.replace('# 1.0 Purpose', '# Section 5 — Program Overview\n\n## 1.0 Purpose', 1),
        s6.replace('# 1.0 Program Philosophy', '# Section 6 — Four-Year Scope and Sequence\n\n## 1.0 Program Philosophy', 1),
        s7, s8,
    ]
    body = '\n\n---\n\n'.join(p for p in parts if p)
    # demote the numbered top-level headings inside 5 and 6 to h2 so each
    # SECTION is the h1 (and the page break)
    body = re.sub(r'^# (\d\.0 .+)$', r'## \1', body, flags=re.M)
    body = body.replace('# Section 5 — Program Overview\n\n## 1.0 Purpose', '# Section 5 — Program Overview\n\n## 1.0 Purpose')
    editorial = '\n\n---\n\n'.join(r1 + r5 + r6)
    return body, editorial


def glossary_html():
    h = read(os.path.join(HERE, 'bhr-glossary.html'))
    m = re.search(r'<body[^>]*>(.*)</body>', h, re.S)
    b = m.group(1) if m else h
    b = re.sub(r'<(header|nav|style|script)[^>]*>.*?</\1>', '', b, flags=re.S)
    b = re.sub(r'<h1[^>]*>.*?</h1>', '', b, count=1, flags=re.S)
    return b


def wrap(title, body_html, subtitle='', cover=False, toc=None, docmeta=''):
    o = ['<!doctype html><html><head><meta charset="utf-8"><title>%s</title>'
         '<style>%s</style></head><body>' % (title, CSS)]
    if cover:
        o.append('<div class="cover"><div class="band">'
                 '<p class="kick">Blue Hills Regional Technical School &middot; Engineering Technology</p>'
                 '<h1>%s</h1><p class="sub">%s</p></div>'
                 '<p class="meta">%s</p></div>' % (title, subtitle, docmeta))
    if toc:
        o.append('<div class="toc"><h1 class="nobreak">Contents</h1><ol>')
        for n, t, d in toc:
            o.append('<li><span class="n">%s</span><span>%s</span><span class="d">%s</span></li>' % (n, t, d))
        o.append('</ol></div>')
    if not cover:
        o.append('<h1 class="first">%s</h1>' % title)
        if docmeta:
            o.append('<p class="docmeta">%s</p>' % docmeta)
    o.append(body_html)
    o.append('</body></html>')
    return '\n'.join(o)


def print_pdf(html_path, pdf_path, title):
    js = '''
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://%s', { waitUntil: 'load' });
  await p.pdf({ path: '%s', format: 'Letter', printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: `%s`, footerTemplate: `%s`,
    margin: { top: '0.9in', bottom: '0.9in', left: '0.8in', right: '0.8in' } });
  await b.close();
})();
''' % (html_path, pdf_path, HEADER_TPL % title, FOOTER_TPL % G.STAMP)
    jsp = html_path + '.js'
    io.open(jsp, 'w').write(js)
    subprocess.run(['node', jsp], check=True, cwd=_node_cwd())
    os.remove(jsp)


def render(name, title, body_html, **kw):
    hp = os.path.join(OUT, name + '.html')
    pp = os.path.join(OUT, G.TAG + '-' + name + '.pdf')
    io.open(hp, 'w', encoding='utf-8').write(wrap(title, body_html, **kw))
    print_pdf(hp, pp, title)
    os.remove(hp)
    print('%-52s %7d' % (os.path.basename(pp), os.path.getsize(pp)))
    return pp


def existing_html_body(path):
    h = read(path)
    m = re.search(r'<body[^>]*>(.*)</body>', h, re.S)
    b = m.group(1) if m else h
    b = re.sub(r'<(nav|style|script)[^>]*>.*?</\1>', '', b, flags=re.S)
    # the standalone reports use h1 for their own title; demote so the
    # document title stays the only h1 and sections do not each page-break
    b = re.sub(r'<h1([^>]*)>', r'<h2\1>', b); b = b.replace('</h1>', '</h2>')
    return b


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    import datetime
    today = datetime.date.today().strftime('%d %B %Y')

    body, editorial = build_binder_md()
    binder_html = md2html(body)
    binder_html += '\n<h1>Appendix A — Word List</h1>\n' + glossary_html()
    toc = [
        ('1', 'Instructor Specialization Overview', 'EDF and ESEC'),
        ('2', 'Foundational Pillars', 'KC · AL · S&amp;O · PP · A&amp;R'),
        ('3', 'Program Content Categories', 'the ten PCCs'),
        ('4', 'Core Class Tasks and Their Classification', 'fourteen task types'),
        ('5', 'Program Overview', 'purpose, framework, grading, documentation, resources'),
        ('6', 'Four-Year Scope and Sequence', 'Grade 9 to 12'),
        ('7', 'Curriculum Standards Analysis', 'Standards 3–10 mapped to units'),
        ('8', 'DESE Standards and Skills', 'the July 2025 framework, verbatim'),
        ('A', 'Word List', 'current and retired terms'),
    ]
    render('Engineering-Technology-Binder',
           'BHR Engineering Technology Binder', binder_html,
           subtitle='Program framework, overview, scope and sequence, standards analysis, and the DESE framework. Complete edition.',
           cover=True, toc=toc, docmeta='Complete edition · %s · Sections 1–8 and Appendix A' % today)

    render('Binder-Editorial-Notes', 'Binder — Editorial Notes',
           md2html(editorial + '\n\n---\n\n' + read(os.path.join(BIN, '04 - Findings - Sections 5-7.md'))),
           docmeta='Change logs, open items and findings removed from the binder sections. %s.' % today)

    render('Pathway-Hubs-Report', 'Pathway Hubs — Source Report',
           existing_html_body(os.path.join(HERE, 'eep-hubs.html')),
           docmeta='What the seven Independent Focus hubs were built from. %s.' % today)
    render('Pathway-Guides', 'Pathway Guides',
           existing_html_body(os.path.join(HERE, 'eep-guides.html')),
           docmeta='The seven pathway hubs as one document. %s.' % today)

    for fn, title, sub in [
        ('INDEPENDENT-FOCUS-STRUCTURE.md', 'Independent Focus — How It Runs', 'The current position, in one page.'),
        ('GOOGLE-DOCS-SETUP.md', 'Google Docs Setup for the Templates', 'Dropdowns, collapsing, and where the masters live.'),
        ('FINAL-AUDIT.md', 'Final Audit', 'What was found, fixed, built, and left to decide.'),
        ('ASSIGNMENT-PAGE-URLS.md', 'Assignment Page URLs', 'Every assignment page, and how to attach a file.'),
        ('MAINTAINING.md', 'Maintaining the Site', 'How to change things without breaking them.'),
        ('HANDOFF.md', 'Handoff', 'Everything a new session needs to pick this up.'),
    ]:
        render(os.path.splitext(fn)[0].title().replace('_', '-'), title,
               md2html(read(os.path.join(HERE, fn))), docmeta='%s %s.' % (sub, today))
