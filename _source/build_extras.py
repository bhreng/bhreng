# -*- coding: utf-8 -*-
"""Instructor pages, the Do Now / bonus shelf, and the links shelf."""

import build_hubs as B
import staff_data as SD
import extras_data as ED
import grade_data as GD

PATH_NAMES = {p['key']: p['nav'] for p in B.P}
PATH_LEAD = {p['key']: p.get('lead', '') for p in B.P}
PATH_TAG = {p['key']: p.get('tag', '') for p in B.P}

CSS = '''
/* --- instructor pages --------------------------------------------------- */
/* same light/dark pair the grade pages use; --w-band stays deep in both */
.who{--w-ink:var(--w-lt);--w-soft:var(--wsl);--w-band:var(--w-lt);
  --accent:var(--w-ink);--accent-soft:var(--w-soft)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .who{
  --w-ink:var(--w-dk);--w-soft:var(--wsd)}}
:root[data-theme="dark"] .who{--w-ink:var(--w-dk);--w-soft:var(--wsd)}
.whohd{border:1px solid var(--rule);border-top:5px solid var(--w-band);
  border-radius:0 0 8px 8px;background:var(--card);padding:22px 26px 24px}
.whohd .ax{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--w-ink);font-weight:700;margin:0}
.whohd h1{margin:5px 0 0;font-size:clamp(30px,4.4vw,42px);letter-spacing:-.02em}
.whohd .rl{margin:4px 0 0;font-family:var(--sans);font-size:14px;
  color:var(--ink-3);font-weight:600}
.whohd .bl{margin:14px 0 0;font-size:17.5px;line-height:1.55;color:var(--ink-2);
  max-width:56ch}
.whohd .gr{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 0}
.whohd .gr a{display:inline-flex;align-items:center;gap:7px;text-decoration:none;
  font-family:var(--sans);font-size:13.5px;font-weight:600;color:var(--ink-2);
  border:1px solid var(--rule);border-radius:999px;padding:7px 13px;line-height:1}
.whohd .gr a:hover{border-color:var(--g);color:var(--g)}
.whohd .gr .dot{width:8px;height:8px;border-radius:50%;background:var(--g)}

.asklist{display:grid;gap:10px}
.askrow{border:1px solid var(--rule);border-left:4px solid var(--w-ink);
  border-radius:0 6px 6px 0;background:var(--card);padding:15px 18px}
.askrow b{display:block;font-family:var(--sans);font-size:16.5px;
  letter-spacing:-.01em;color:var(--ink)}
.askrow span{display:block;margin-top:5px;font-size:14.5px;line-height:1.5;
  color:var(--ink-2)}

/* --- shelves ------------------------------------------------------------ */
.shelf{border:1px solid var(--rule);border-radius:7px;background:var(--card);
  overflow:hidden}
.shelf .row{display:flex;gap:16px;padding:15px 19px;
  border-bottom:1px solid var(--rule-soft);align-items:flex-start}
.shelf .row:last-child{border-bottom:0}
.shelf .row:hover{background:var(--accent-soft)}
.shelf .bd{min-width:0;flex:1}
.shelf .ti{font-family:var(--sans);font-weight:700;font-size:16.5px;
  letter-spacing:-.01em;margin:0;color:var(--ink)}
.shelf a.ti{text-decoration:none;color:var(--accent)}
.shelf a.ti:hover{text-decoration:underline}
.shelf .ds{margin:5px 0 0;font-size:14.5px;line-height:1.55;color:var(--ink-2)}
.shelf .tg{display:flex;flex-wrap:wrap;gap:6px 12px;margin:8px 0 0;
  font-family:var(--mono);font-size:10px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-3)}
.shelf .tg a{color:var(--accent);text-decoration:none;font-weight:700}
.shelf .gbadge{flex:none;font-family:var(--mono);font-size:10px;font-weight:700;
  letter-spacing:.06em;border:1px solid var(--rule);border-radius:3px;
  padding:3px 7px;color:var(--ink-3);white-space:nowrap;margin-top:2px}
.shelf .host{font-family:var(--mono);font-size:11px;color:var(--ink-3);
  margin:5px 0 0;word-break:break-all}

@media(max-width:640px){
  .whohd{padding:18px 17px 20px}
  .shelf .row{padding:14px 16px;gap:11px}
}
'''


# ------------------------------------------------------------- instructors

def staff_page(key, depth=1):
    s = SD.by_key(key)
    r = '../' * depth
    style = ('--w-lt:%s;--w-dk:%s;--wsl:%s;--wsd:%s'
             % (s['tone'], s['tone_dark'], s['soft'], s['soft_dark']))
    out = ['<div class="wrap who" style="%s">' % style,
           '<div class="whohd">',
           '  <p class="ax">%s &middot; %s</p>' % (s['axis'], s['axis_full']),
           '  <h1>%s</h1>' % s['name'],
           '  <p class="rl">%s &middot; Engineering Technology &middot; '
           'Room E-126</p>' % s['role'],
           '  <p class="bl">%s</p>' % s['blurb'],
           '  <div class="gr">']
    for n in s['grades']:
        g = GD.by_key(str(n))
        out.append('    <a href="%sgrades/%s.html" style="--g:%s">'
                   '<span class="dot"></span>Grade %d &mdash; %s</a>'
                   % (r, g['key'], g['ink'], g['num'], g['course']))
    out.append('  </div>')
    out.append('</div>')

    out.append('<section><h2>What he covers</h2>'
               '<p class="sub">Both instructors are in the shop with all four '
               'years. This is the half of the work that is his.</p>'
               '<ul class="ticks">')
    for c in s['covers']:
        out.append('  <li>%s</li>' % c)
    out.append('</ul></section>')

    mine = [p for p in B.P if s['name'] in PATH_LEAD.get(p['key'], '')]
    if mine:
        out.append('<section><h2>Pathways he leads</h2>'
                   '<p class="sub">Where a project in this area goes first.</p>'
                   '<div class="shelf">')
        for p in mine:
            shared = ' and ' in PATH_LEAD.get(p['key'], '')
            out.append(
                '  <div class="row"><div class="bd">'
                '<a class="ti" href="%spathways/%s.html">%s</a>'
                '<p class="ds">%s</p>'
                '<div class="tg"><span>Standard %s</span>%s</div>'
                '</div></div>'
                % (r, p['key'], p['nav'], PATH_TAG.get(p['key'], ''),
                   p['std'],
                   '<span>Shared with the other instructor</span>'
                   if shared else ''))
        out.append('</div></section>')

    out.append('<section><h2>Good questions to bring him</h2>'
               '<p class="sub">And what to have with you when you do. Bringing '
               'the thing beats describing the thing.</p>'
               '<div class="asklist">')
    for q, bring in s['ask']:
        out.append('  <div class="askrow"><b>&ldquo;%s&rdquo;</b>'
                   '<span>%s</span></div>' % (q, bring))
    out.append('</div></section>')

    if s['also']:
        out.append('<section><div class="note acc"><p>%s</p></div></section>'
                   % s['also'])

    other = [x for x in SD.STAFF if x['key'] != key][0]
    out.append('<section><div class="note"><p><strong>Not sure which of '
               'them?</strong> Describe the thing you want to build and either '
               'one will point you at the right pathway. If the problem is '
               'code, circuits or why a system misbehaves, start with '
               '<a href="%sstaff/%s.html">%s</a>. The '
               '<a href="%spathways/index.html">pathways page</a> lists who '
               'leads each area.</p></div></section>'
               % (r, other['key'], other['name'], r)
               if key == 'frank' else
               '<section><div class="note"><p><strong>Not sure which of '
               'them?</strong> Describe the thing you want to build and either '
               'one will point you at the right pathway. If the problem is '
               'CAD, fabrication, structures or a print that came out wrong, '
               'start with <a href="%sstaff/%s.html">%s</a>. The '
               '<a href="%spathways/index.html">pathways page</a> lists who '
               'leads each area.</p></div></section>'
               % (r, other['key'], other['name'], r))
    out.append('</div>')
    return '\n'.join(out)


STAFF_INDEX_NOTE = (
    'Both instructors work with every student in the shop. The grade decides '
    'whose Google Classroom your assignments come from; the problem decides '
    'which one you walk over to.')


# --------------------------------------------------------- do nows / bonus

def donows(depth=1):
    r = '../' * depth
    out = ['<div class="wrap">',
           '<section class="hero">',
           '  <p class="eyebrow">Short work</p>',
           '  <h1>Do Nows and bonus work</h1>',
           '  <p class="lede">The short tasks that open a session, and the '
           'assignments that are not part of a project. In Classroom these are '
           'scattered across eighty weekly topics and titled by date, which '
           'makes them impossible to find again. Here they are grouped by what '
           'they actually build.</p>',
           '</section>',
           '<div class="note"><p><strong>Most of these are skill practice, '
           'not assessment.</strong> They are the fastest way to pick up a '
           'tool you have not used &mdash; and several of them are worth '
           'doing again on your own time, before a project needs them.</p>'
           '</div>']
    for grp in ED.GROUPS:
        out.append('<section id="%s">' % grp['key'])
        out.append('  <h2>%s</h2>' % grp['title'])
        out.append('  <p class="sub">%s</p>' % grp['blurb'])
        out.append('  <div class="shelf">')
        for title, tool, desc, grade, path in grp['items']:
            tags = []
            if tool:
                tags.append('<span>%s</span>' % tool)
            if path:
                tags.append('<a href="%spathways/%s.html">%s</a>'
                            % (r, path, PATH_NAMES.get(path, path)))
            out.append(
                '    <div class="row">'
                '<span class="gbadge">GR %s</span>'
                '<div class="bd"><p class="ti">%s</p><p class="ds">%s</p>'
                '%s</div></div>'
                % (grade, title, desc,
                   ('<div class="tg">%s</div>' % ''.join(tags)) if tags else ''))
        out.append('  </div>')
        out.append('</section>')
    out.append(
        '<section><div class="note acc"><p><strong>Where the actual '
        'instructions are.</strong> Most Do Nows keep their brief in a '
        'Classroom attachment rather than in the post, so this page describes '
        'them rather than reproducing them. Open the item in Classroom for the '
        'file itself &mdash; and if a task here sounds useful and you are not '
        'in that grade, ask. Nobody minds.</p></div></section>')
    out.append('</div>')
    return '\n'.join(out)


# --------------------------------------------------------------- the links

def links(depth=1):
    out = ['<div class="wrap">',
           '<section class="hero">',
           '  <p class="eyebrow">Worth a look</p>',
           '  <h1>Links</h1>',
           '  <p class="lede">Reference, channels, model libraries and career '
           'data. Not courses &mdash; those live on the '
           '<a href="../resources/index.html">training page</a>. These are the '
           'things worth keeping a tab open for.</p>',
           '</section>']
    for grp in ED.LINKS:
        out.append('<section>')
        out.append('  <h2>%s</h2>' % grp['title'])
        out.append('  <p class="sub">%s</p>' % grp['blurb'])
        out.append('  <div class="shelf">')
        for title, url, desc in grp['items']:
            host = url.split('//')[-1].split('/')[0].replace('www.', '')
            out.append(
                '    <div class="row"><div class="bd">'
                '<a class="ti" href="%s" target="_blank" rel="noopener">%s</a>'
                '<p class="ds">%s</p><p class="host">%s</p></div></div>'
                % (url, title, desc, host))
        out.append('  </div>')
        out.append('</section>')
    out.append(
        '<section><div class="note"><p><strong>Every link here was opened and '
        'checked.</strong> They still rot &mdash; if one is dead, say so and '
        'it gets fixed. Suggestions for the shelf are welcome; the bar is that '
        'it has to be something you would actually go back to.</p></div>'
        '</section>')
    out.append('</div>')
    return '\n'.join(out)
