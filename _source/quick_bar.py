# -*- coding: utf-8 -*-
"""The quick bar: direct links to the four grades and the two instructors.

Sits under the site header on every page. The rail already lists the whole
site, but the rail is a map you read; this is a set of doors you hit without
reading. A student who knows they are in Grade 11 should never have to think
about navigation at all.

Each grade pill carries its own colour, taken from that grade's Classroom
banner, so the bar is recognisable by shape and colour before it is read.
"""

import grade_data as GD

CSS = '''
/* --- quick bar ---------------------------------------------------------- */
.qbar{border-bottom:1px solid var(--rule);background:var(--paper)}
.qbar .in{max-width:1280px;margin:0 auto;padding:8px 24px;
  display:flex;align-items:center;gap:7px;flex-wrap:wrap;
  font-family:var(--sans)}
.qbar .lbl{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-3);margin-right:3px;flex:none}
.qbar a{display:inline-flex;align-items:center;gap:6px;text-decoration:none;
  font-size:13px;font-weight:600;color:var(--ink-2);padding:6px 11px;
  border:1px solid var(--rule);border-radius:999px;line-height:1;white-space:nowrap}
/* the pill colour follows the theme, same pair of values the grade pages use */
.qbar a{--q:var(--ql);--qs:var(--qsl)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .qbar a{
  --q:var(--qd);--qs:var(--qsd)}}
:root[data-theme="dark"] .qbar a{--q:var(--qd);--qs:var(--qsd)}
.qbar a:hover{border-color:var(--q);color:var(--q);background:var(--qs)}
.qbar a[aria-current="page"]{border-color:var(--q);color:var(--q);
  background:var(--qs)}
.qbar a .dot{width:8px;height:8px;border-radius:50%;background:var(--q);flex:none}
.qbar .sep{width:1px;height:18px;background:var(--rule);margin:0 5px;flex:none}
.qbar .who,.qbar .who{--ql:var(--accent);--qd:var(--accent);
  --qsl:var(--accent-soft);--qsd:var(--accent-soft)}

@media(max-width:640px){
  .qbar .in{padding:7px 16px;gap:6px}
  .qbar .lbl{display:none}
  .qbar a{font-size:12.5px;padding:6px 10px}
  .qbar .sep{margin:0 2px}
}
@media print{.qbar{display:none}}
'''

STAFF = [
    ('Mr. Frank', 'staff/frank.html'),
    ('Mr. Dryer', 'staff/dryer.html'),
]


def render(current, rel):
    out = ['<nav class="qbar" aria-label="Quick links"><div class="in">',
           '  <span class="lbl">Go to</span>']
    for g in GD.GRADES:
        href = 'grades/%s.html' % g['key']
        cur = ' aria-current="page"' if href == current else ''
        out.append(
            '  <a href="%s%s" style="--ql:%s;--qd:%s;--qsl:%s;--qsd:%s"%s>'
            '<span class="dot"></span>Grade %d</a>'
            % (rel, href, g['ink'], g['ink_dark'], g['soft'], g['soft_dark'],
               cur, g['num']))
    out.append('  <span class="sep"></span>')
    for name, href in STAFF:
        cur = ' aria-current="page"' if href == current else ''
        out.append('  <a class="who" href="%s%s"%s>%s</a>'
                   % (rel, href, cur, name))
    out.append('</div></nav>')
    return '\n'.join(out)
