# -*- coding: utf-8 -*-
"""The Documents page: every template, in one place, with the guide on top.

Until this page existed, thirteen finished templates sat in files/ and the
only route to any of them was the download box on an assignment page. This
is the shelf. It is grouped by WHEN you reach for a document rather than by
file type, because that is how a student looks: "it's Monday, which one".
"""

import os
import work_pages as WP
import generation as G

CSS = '''
.docs .lede{font-size:17.5px;line-height:1.55;color:var(--ink-2);max-width:62ch;margin:0 0 18px}
.docs .guide{display:flex;align-items:center;gap:18px;flex-wrap:wrap;
  border:1px solid var(--rule);border-left:5px solid var(--accent);
  border-radius:0 8px 8px 0;background:var(--accent-soft);padding:18px 22px;margin:0 0 26px}
.docs .guide b{font-family:var(--sans);font-size:17px;color:var(--ink);display:block}
.docs .guide span{font-size:14.5px;color:var(--ink-2);line-height:1.5}
.docs .guide a{margin-left:auto;flex:none;font-family:var(--mono);font-size:11px;
  letter-spacing:.1em;text-transform:uppercase;font-weight:700;text-decoration:none;
  color:#fff;background:var(--accent);border-radius:5px;padding:10px 16px}
.docs .guide a:hover{background:var(--ink)}
.docs h2{margin:26px 0 4px}
.docs .when{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--ink-3);margin:0 0 12px}
.docs .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:12px}
.docs .card{border:1px solid var(--rule);border-radius:7px;background:var(--card);
  padding:14px 16px 13px;display:flex;flex-direction:column;gap:6px;text-decoration:none;
  color:inherit;transition:border-color .12s}
.docs .card:hover{border-color:var(--accent)}
.docs .card .t{font-family:var(--sans);font-weight:700;font-size:15.5px;color:var(--accent);
  display:flex;align-items:baseline;gap:8px}
.docs .card .ext{font-family:var(--mono);font-size:9px;letter-spacing:.09em;padding:1px 5px;
  border:1px solid var(--rule);border-radius:2px;color:var(--ink-3);flex:none}
.docs .card .d{font-size:14px;line-height:1.5;color:var(--ink-2)}
.docs .posters{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:9px}
.docs .posters a{display:block;border:1px solid var(--rule);border-radius:6px;padding:10px 13px;
  text-decoration:none;color:var(--ink);font-size:14px;background:var(--card)}
.docs .posters a:hover{border-color:var(--accent);color:var(--accent)}
.docs .note{margin-top:22px}
'''

GROUPS = [
    ('Every shop day', 'The two you never skip',
     ['BHR27-Daily-Logbook.docx', 'BHR27-Which-Document-When.pdf']),
    ('Monday and Friday of a shop week', 'Plan it, then say what happened',
     ['BHR27-Weekly-Planner.docx', 'BHR27-Weekly-Reflection.docx']),
    ('When a project starts', 'Fix what &ldquo;finished&rdquo; means before you touch anything',
     ['BHR27-Design-Brief-and-Initial-Planner.docx',
      'BHR27-Decision-Matrix.xlsx', 'BHR27-Project-Gantt-Chart.xlsx',
      'BHR27-Part-List.xlsx', 'BHR27-Order-Request-Form.xlsx']),
    ('While you build and test', 'The evidence',
     ['BHR27-Test-Log.xlsx', 'BHR27-IO-Map-and-Commissioning.xlsx',
      'BHR27-Research-Log.xlsx', 'BHR27-Mid-Project-Design-Review.docx',
      'BHR27-Instructor-Meeting-Notes.docx']),
    ('When something ends', 'Short, and where the grade comes from',
     ['BHR27-Project-Reflection.docx', 'BHR27-Do-Now-Reflection.docx']),
    ('Your Independent Focus', 'A proposal, a reflection, and one page for two years',
     ['BHR27-Independent-Focus-Proposal.docx',
      'BHR27-Independent-Focus-Reflection.docx',
      'BHR27-Independent-Focus-Record.pdf']),
    ('How you are graded', 'The rubrics Classroom uses, in plain sight',
     ['BHR27-Project-Rubric.pdf', 'BHR27-Weekly-Grade-Rubric.pdf']),
]

POSTERS = [
    ('primary-rules.pdf', 'Primary shop rules'),
    ('shop-rules.pdf', 'Shop rules'),
    ('emergency.pdf', 'Emergency'),
    ('ppe-dress-right.pdf', 'PPE: dress right'),
    ('trained-and-authorized.pdf', 'Trained and authorised'),
    ('clean-up.pdf', 'Clean-up'),
    ('engineers-logbook.pdf', 'The engineer&rsquo;s logbook'),
    ('grading.pdf', 'How you are graded'),
    ('weekly-grade.pdf', 'The weekly grade'),
    ('project-rubric.pdf', 'Project rubric'),
    ('seven-pathways.pdf', 'The seven pathways'),
    ('roles-of-an-engineer.pdf', 'Roles of an engineer'),
    ('edf-and-esec.pdf', 'EDF and ESEC'),
    ('3d-printer-levels.pdf', '3D printer levels'),
    ('resin-j55.pdf', 'Resin: the J55'),
    ('laser.pdf', 'The laser'),
    ('cobots.pdf', 'Cobots'),
    ('soldering-hot-glue.pdf', 'Soldering and hot glue'),
]


def page(have, posters_have, depth=1):
    r = '../' * depth
    o = ['<div class="wrap docs">',
         '<h1>Documents</h1>',
         '<p class="lede">Every template the shop uses, grouped by when you '
         'reach for it. Download, fill in, hand in. If you are not sure which '
         'one, the guide at the top says.</p>']
    if 'BHR27-Which-Document-When.pdf' in have:
        o.append('<div class="guide"><div><b>Which document, and when</b>'
                 '<span>One page. The whole set and the moment each one is '
                 'for. Read this once.</span></div>'
                 '<a href="%sfiles/BHR27-Which-Document-When.pdf" download>'
                 'Download PDF</a></div>' % r)
    for title, when, names in GROUPS:
        names = [n for n in names if n in have
                 and n != 'BHR27-Which-Document-When.pdf']
        if not names:
            continue
        o.append('<h2>%s</h2><p class="when">%s</p><div class="grid">'
                 % (title, when))
        for n in names:
            label, what = WP.FILE_INFO.get(n, (n, ''))
            ext = n.rsplit('.', 1)[-1].upper()
            o.append('<a class="card" href="%sfiles/%s" download>'
                     '<span class="t">%s<span class="ext">%s</span></span>'
                     '<span class="d">%s</span></a>' % (r, n, label, ext, what))
        o.append('</div>')

    ps = [(f, l) for f, l in POSTERS if f in posters_have]
    if ps:
        o.append('<h2>For the walls</h2><p class="when">Print files, letter '
                 'and tabloid</p><div class="posters">')
        for f, l in ps:
            o.append('<a href="%sposters/%s" download>%s</a>' % (r, f, l))
        o.append('</div>')

    o.append('<div class="note"><p><strong>Is this the current one?</strong> '
             'Every document in this year&rsquo;s set is tagged <b>%s</b> '
             '&mdash; in the file name and printed in the footer. Search your '
             'Drive for %s and you get only the current forms. A file without '
             'it is an older version.</p></div>' % (G.TAG, G.TAG))
    o.append('<div class="note"><p><strong>Google Docs.</strong> These are '
             'Word and Excel files so they download anywhere. Upload one to '
             'Drive and it converts to a Doc or a Sheet; the logbook is '
             'worth keeping as a Doc so the status-code dropdowns can be '
             'added once and inherited by every copy.</p></div>')
    o.append('</div>')
    return '\n'.join(o)
