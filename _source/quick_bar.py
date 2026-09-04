# -*- coding: utf-8 -*-
"""The quick links: the four grades and the two instructors.

They live INSIDE the sticky site bar, beside the logo and the search box, so
they stay on screen while you scroll. A second strip underneath would scroll
away, which defeats the point of a shortcut.

The rail already lists the whole site, but the rail is a map you read; this is
a set of doors you hit without reading. A student who knows they are in
Grade 11 should never have to think about navigation at all.

Each grade pill carries its own colour, taken from that grade's Classroom
banner, so the bar is recognisable by shape and colour before it is read.
"""

import grade_data as GD

CSS = '''
/* --- quick links, inside the sticky site bar ---------------------------- */
.qnav{display:flex;align-items:center;gap:6px;flex-wrap:wrap;
  font-family:var(--sans);margin-right:auto}
.qnav .lbl{font-family:var(--mono);font-size:9px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-3);margin-right:2px;flex:none}
.qnav a{display:inline-flex;align-items:center;gap:5px;text-decoration:none;
  font-size:12.5px;font-weight:600;color:var(--ink-2);padding:5px 10px;
  border:1px solid var(--rule);border-radius:999px;line-height:1;
  white-space:nowrap}
/* the pill colour follows the theme, same pair of values the grade pages use */
.qnav a{--q:var(--ql);--qs:var(--qsl)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .qnav a{
  --q:var(--qd);--qs:var(--qsd)}}
:root[data-theme="dark"] .qnav a{--q:var(--qd);--qs:var(--qsd)}
.qnav a:hover{border-color:var(--q);color:var(--q);background:var(--qs)}
.qnav a[aria-current="page"]{border-color:var(--q);color:var(--q);
  background:var(--qs)}
.qnav a .dot{width:7px;height:7px;border-radius:50%;background:var(--q);flex:none}
.qnav .sep{width:1px;height:16px;background:var(--rule);margin:0 3px;flex:none}
.qnav .who{--ql:var(--accent);--qd:var(--accent);
  --qsl:var(--accent-soft);--qsd:var(--accent-soft)}
/* the long form of a label, dropped first when the bar runs out of room */
.qnav .lg{display:inline}
.qnav .sm{display:none}

/* The bar is one row up to here. Below it, the words go before the pills do:
   a coloured dot and a number still identifies a grade. */
@media(max-width:1180px){
  .qnav .lbl{display:none}
  .qnav .lg{display:none}
  .qnav .sm{display:inline}
  .qnav a{padding:5px 9px;gap:4px}
}
@media(max-width:900px){
  /* search has already gone full width on its own row; the pills follow it */
  .qnav{order:4;width:100%;margin:7px 0 0}
  .qnav .lbl{display:inline}
  .qnav .lg{display:inline}
  .qnav .sm{display:none}
}
@media(max-width:640px){
  .qnav{margin-top:6px;gap:5px}
  .qnav .lbl{display:none}
  .qnav .lg{display:none}
  .qnav .sm{display:inline}
}
@media print{.qnav{display:none}}
'''

STAFF = [
    ('Mr. Frank', 'staff/frank.html'),
    ('Mr. Dryer', 'staff/dryer.html'),
]


def render(current, rel):
    out = ['<nav class="qnav" aria-label="Quick links">',
           '  <span class="lbl">Go to</span>']
    for g in GD.GRADES:
        href = 'grades/%s.html' % g['key']
        cur = ' aria-current="page"' if href == current else ''
        out.append(
            '  <a href="%s%s" style="--ql:%s;--qd:%s;--qsl:%s;--qsd:%s"%s>'
            '<span class="dot"></span>'
            '<span class="lg">Grade %d</span><span class="sm">Gr %d</span></a>'
            % (rel, href, g['ink'], g['ink_dark'], g['soft'], g['soft_dark'],
               cur, g['num'], g['num']))
    out.append('  <span class="sep"></span>')
    for name, href in STAFF:
        cur = ' aria-current="page"' if href == current else ''
        short = name.replace('Mr. ', '')
        out.append('  <a class="who" href="%s%s"%s>'
                   '<span class="lg">%s</span><span class="sm">%s</span></a>'
                   % (rel, href, cur, name, short))
    out.append('</nav>')
    return '\n'.join(out)
