# -*- coding: utf-8 -*-
"""The grade pages: an index and one home per grade.

Each grade page is coloured by its own banner. The colour is set as a local
override of --accent inside .gradepage, so every shared component -- links,
current state, numerals, the callouts -- picks it up without any of them
needing to know about grades.
"""

import grade_data as GD
import grade_work as GW
import build_hubs as B
import brief_text as BT
import shop_projects as SP
import work_pages as WP

PATH_NAMES = {p['key']: p['nav'] for p in B.P}

CSS = '''
/* --- grade pages -------------------------------------------------------- */
/* Three variables per grade, set inline on the page:
     --g-lt / --g-dk   the grade colour for light and for dark paper
     --g-slt / --g-sdk its soft panel background, likewise
   --g-band stays the deep colour in BOTH themes, because the hero scrim is a
   solid block with white text on it -- swapping that to the light-theme-dark
   variant would leave white on lilac. */
.gradepage,.gcard{--g-ink:var(--g-lt);--g-soft:var(--g-slt);--g-band:var(--g-lt)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .gradepage,
  :root:not([data-theme="light"]) .gcard{--g-ink:var(--g-dk);--g-soft:var(--g-sdk)}}
:root[data-theme="dark"] .gradepage,:root[data-theme="dark"] .gcard{
  --g-ink:var(--g-dk);--g-soft:var(--g-sdk)}
.gradepage{--accent:var(--g-ink);--accent-soft:var(--g-soft)}

.ghero{position:relative;margin:0 0 4px;border:1px solid var(--rule);
  border-radius:8px;overflow:hidden;background:var(--g-soft)}
.ghero img{display:block;width:100%;height:158px;object-fit:cover;
  /* 84%, not centre: the left of every banner is the AI-generated tablet, whose
     invented labels do not survive a close look. The right side -- the drawings,
     the turbine, the panels -- is clean. */
  object-position:84% 50%}
.ghero .scrim{position:absolute;inset:0;display:flex;flex-direction:column;
  justify-content:center;padding:0 26px;
  background:linear-gradient(90deg,var(--g-band) 0%,var(--g-band) 34%,
    rgba(0,0,0,0) 78%)}
.ghero .gnum{font-family:var(--mono);font-size:11px;letter-spacing:.16em;
  text-transform:uppercase;color:rgba(255,255,255,.82);margin:0 0 4px}
.ghero h1.gname{font-family:var(--sans);font-weight:var(--w-heavy);
  font-size:clamp(26px,4.4vw,40px);line-height:1.02;color:#fff;margin:0;
  letter-spacing:-.02em;text-shadow:0 1px 14px rgba(0,0,0,.3)}
.ghero .gwho{font-family:var(--sans);font-size:13.5px;font-weight:600;
  color:rgba(255,255,255,.88);margin:7px 0 0}

.gradepage .lede,.gi .lede{font-size:18px;line-height:1.62;color:var(--ink-2);
  max-width:64ch;margin:0}

/* the grade chooser on the index */
.gcards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:16px}
.gcard{display:block;text-decoration:none;color:inherit;border:1px solid var(--rule);
  border-radius:8px;overflow:hidden;background:var(--card);transition:transform .12s}
.gcard:hover{transform:translateY(-2px);border-color:var(--g-ink)}
.gcard img{display:block;width:100%;height:96px;object-fit:cover;object-position:88% 50%}
.gcard .cb{padding:14px 17px 16px}
.gcard .cn{font-family:var(--mono);font-size:10px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--g-ink);font-weight:700}
.gcard .ct{font-family:var(--sans);font-weight:700;font-size:19px;margin:3px 0 0;
  color:var(--ink);letter-spacing:-.01em}
.gcard .cs{font-size:14px;color:var(--ink-2);margin:6px 0 0;line-height:1.45}
.gcard .cw{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--ink-3);margin:9px 0 0}

/* a term block */
.term{margin:0 0 6px}
.termhd{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;
  padding:0 0 9px;border-bottom:2px solid var(--g-ink);margin:0 0 16px}
.termhd h2{margin:0;font-size:1.5rem;letter-spacing:-.015em}
.termhd .tc{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--ink-3);margin-left:auto}

/* one assignment */
.asg{border:1px solid var(--rule);border-left:4px solid var(--g-ink);
  border-radius:0 6px 6px 0;background:var(--card);margin:0 0 12px;
  padding:17px 20px 18px}
.asg .ah{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.asg h3{margin:0;font-family:var(--sans);font-weight:700;font-size:18.5px;
  letter-spacing:-.01em;line-height:1.25}
.asg .wk{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-3);border:1px solid var(--rule);
  border-radius:2px;padding:1px 6px;flex:none}
.asg .kind{font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--g-ink);font-weight:700;margin-left:auto;
  flex:none}
.asg .hook{margin:8px 0 0;font-size:16px;line-height:1.5;color:var(--ink)}
.asg .bd{margin:12px 0 0}
.asg .bd p{margin:0 0 9px;font-size:15px;line-height:1.6;color:var(--ink-2)}
.asg .bd p:last-child{margin-bottom:0}
.asg .gives{margin:13px 0 0;padding:13px 16px;background:var(--g-soft);
  border-radius:5px}
.asg .gives .gl{font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--g-ink);font-weight:700;margin:0 0 7px;
  max-width:none}
.asg .gives ul{margin:0;padding-left:18px}
.asg .gives li{font-size:14.5px;line-height:1.5;color:var(--ink);margin:0 0 5px}
.asg .gives li:last-child{margin:0}
.asg .meta{display:flex;flex-wrap:wrap;gap:7px 16px;margin:13px 0 0;
  padding-top:11px;border-top:1px solid var(--rule-soft);
  font-family:var(--sans);font-size:12.5px;color:var(--ink-3)}
.asg .meta b{color:var(--ink-2);font-weight:600}
.asg .meta a{color:var(--g-ink);font-weight:600}
.asg .anote{margin:12px 0 0;padding:10px 14px;border-left:3px solid var(--blue);
  background:var(--blue-soft);font-size:14px;line-height:1.5;color:var(--ink)}

.asg h3 a.asglink{color:inherit;text-decoration:none;
  border-bottom:1.5px solid transparent}
.asg h3 a.asglink:hover{color:var(--g-ink);border-bottom-color:var(--g-ink)}
.asg h3 a.asglink::after{content:"\2192";margin-left:7px;font-size:.86em;
  color:var(--g-ink);opacity:0;transition:opacity .12s}
.asg h3 a.asglink:hover::after{opacity:1}
.asg.solo{border:1px solid var(--rule);border-left:5px solid var(--g-ink);
  padding:24px 26px 26px}
.asg.solo h1.asgt{margin:0;font-family:var(--sans);font-weight:var(--w-heavy);
  font-size:clamp(24px,3.6vw,33px);line-height:1.1;letter-spacing:-.02em;
  color:var(--ink)}
.asg.solo .hook{font-size:17.5px;margin-top:11px}

/* the full brief */
.brief{margin:14px 0 0;border-top:1px solid var(--rule-soft);padding-top:12px}
.brief>summary{cursor:pointer;list-style:none;font-family:var(--mono);
  font-size:10px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--g-ink);font-weight:700;padding:3px 0;user-select:none}
.brief>summary::-webkit-details-marker{display:none}
/* a CSS caret rather than a glyph: the mono face has no triangle and renders
   a tofu box in its place */
.brief>summary::after{content:"";display:inline-block;margin:0 0 2px 8px;
  width:5px;height:5px;border-right:1.5px solid currentColor;
  border-bottom:1.5px solid currentColor;transform:rotate(-135deg)}
.brief:not([open])>summary::after{transform:rotate(45deg);margin-bottom:0}
.brief>summary:hover{text-decoration:underline}
.brief .sm-c{display:none}
.brief:not([open]) .sm-c{display:inline}
.brief:not([open]) .sm-o{display:none}
.bt{padding-top:6px}
.bt p{margin:0 0 11px;font-size:15.5px;line-height:1.62;color:var(--ink)}
.bt ul{margin:0 0 12px;padding-left:20px}
.bt li{margin:0 0 7px;font-size:15px;line-height:1.55;color:var(--ink-2)}
.bt li strong,.bt p strong{color:var(--ink);font-weight:600}
.bt code{font-size:.86em}
.bt .tw{margin:0 0 13px}
.bt table{font-size:14.5px;min-width:0}

/* the meaningful attachments and references */
.alinks{margin:14px 0 0;border:1px solid var(--rule);border-radius:6px;
  overflow:hidden}
.alinks .gl{margin:0;max-width:none;padding:9px 15px;background:var(--g-soft);
  font-family:var(--mono);font-size:9.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--g-ink);font-weight:700}
.alinks a{display:block;padding:12px 15px;text-decoration:none;
  border-top:1px solid var(--rule-soft)}
.alinks a:hover{background:var(--g-soft)}
.alinks b{display:block;font-family:var(--sans);font-size:15.5px;
  color:var(--g-ink)}
.alinks span{display:block;margin-top:3px;font-size:14px;line-height:1.5;
  color:var(--ink-2);max-width:62ch}
.alinks em{display:block;margin-top:4px;font-family:var(--mono);font-size:10.5px;
  font-style:normal;color:var(--ink-3)}

/* the unit map, used on every grade */
.units{border:1px solid var(--rule);background:var(--card);border-radius:6px;
  overflow:hidden}
.units .u{display:flex;gap:15px;padding:14px 18px;border-bottom:1px solid var(--rule-soft)}
.units .u:last-child{border-bottom:0}
.units .n{font-family:var(--mono);font-size:12px;font-weight:700;color:var(--g-ink);
  flex:none;padding-top:2px;width:20px}
.units .ut{font-family:var(--sans);font-weight:700;font-size:16px;margin:0;
  color:var(--ink);line-height:1.3}
.units .ud{margin:4px 0 0;font-size:14.5px;line-height:1.5;color:var(--ink-2)}

/* the exploratory section: for students in their exploratory week */
.expl .exgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:6px;
  overflow:hidden}
.expl .exgrid article{background:var(--card);padding:16px 19px}
.expl .exgrid b{display:block;font-family:var(--sans);font-weight:700;
  font-size:16px;line-height:1.3;color:var(--g-ink)}
.expl .exgrid p{margin:6px 0 0;font-size:15px;line-height:1.55;color:var(--ink-2)}
.expl .note ul{margin:8px 0 0;padding-left:20px}
.expl .note li{margin:0 0 6px;font-size:15px;line-height:1.5}

.gempty{border:1px dashed var(--rule);border-radius:6px;padding:20px 22px;
  background:var(--card)}
.gempty p{margin:0 0 9px;font-size:15px;line-height:1.6;color:var(--ink-2)}
.gempty p:last-child{margin:0}

/* On paper: a collapsed brief must still print, the control that collapses it
   must not, and the blocks that are read as a unit should not be split across
   a page break. */
@media print{
  .brief>summary{display:none}
  .brief{border-top:0;padding-top:0}
  .brief[open]>.bt,.brief:not([open])>.bt{display:block}
  .asg{break-inside:auto;page-break-inside:auto}
  .asg .gives,.asg .alinks,.asg .anote,.units .u{break-inside:avoid;
    page-break-inside:avoid}
  .asg .ah,.termhd{break-after:avoid;page-break-after:avoid}
  .ghero img{height:96px}
  .alinks a::after{content:" (" attr(href) ")";font-family:var(--mono);
    font-size:10px;color:#555;word-break:break-all}
}

@media(max-width:640px){
  .ghero img{height:124px}
  .ghero .scrim{padding:0 18px;
    background:linear-gradient(90deg,var(--g-band) 0%,var(--g-band) 52%,
      rgba(0,0,0,.15) 100%)}
  .asg{padding:15px 16px 16px}
  .asg .kind{margin-left:0}
}
'''

KIND_LABEL = {'project': 'Project', 'skills': 'Skills', 'course': 'Course',
              'reflection': 'Reflection', 'admin': 'Admin'}


def hero(g, depth):
    r = '../' * depth
    return (
        '<div class="ghero">\n'
        '  <img src="%sassets/%s" alt="" loading="lazy">\n'
        '  <div class="scrim">\n'
        '    <p class="gnum">Grade %d &middot; %s</p>\n'
        '    <h1 class="gname">%s</h1>\n'
        '    <p class="gwho">Delivered by %s</p>\n'
        '  </div>\n'
        '</div>' % (r, g['banner'], g['num'], g['course'], g['course'],
                    g['teacher']))


def assignment(a, depth, full='', gkey=None, standalone=False):
    r = '../' * depth
    if standalone:
        head = '<h1 class="asgt">%s</h1>' % a['title']
    elif gkey:
        head = ('<h3><a class="asglink" href="%s%s">%s</a></h3>'
                % (r, WP.page_name(gkey, a['title']), a['title']))
    else:
        head = '<h3>%s</h3>' % a['title']
    out = ['<article class="asg%s">' % (' solo' if standalone else ''),
           '  <div class="ah">',
           '    ' + head,
           '    <span class="wk">%s</span>' % a['w'],
           '    <span class="kind">%s</span>' % KIND_LABEL.get(a['kind'], ''),
           '  </div>']
    if a['hook']:
        out.append('  <p class="hook">%s</p>' % a['hook'])
    if a['body']:
        out.append('  <div class="bd">')
        for p in a['body']:
            out.append('    <p>%s</p>' % p)
        out.append('  </div>')
    if a['gives']:
        out.append('  <div class="gives"><p class="gl">What you hand in</p><ul>')
        for gv in a['gives']:
            out.append('    <li>%s</li>' % gv)
        out.append('  </ul></div>')
    if full:
        # The brief as Classroom actually words it. Open by default -- a
        # student who came here for the instructions should not have to find
        # and click a control to reach them. The <details> is for scrolling
        # past a brief you have already read, not for hiding it.
        out.append('  <details class="brief" open>')
        out.append('    <summary><span class="sm-o">Hide</span>'
                   '<span class="sm-c">Read</span> the full brief</summary>')
        out.append('    <div class="bt">%s</div>' % full)
        out.append('  </details>')
    if a.get('links'):
        out.append('  <div class="alinks"><p class="gl">Files and links</p>')
        for label, url, what in a['links']:
            host = url.split('//')[-1].split('/')[0].replace('www.', '')
            out.append('    <a href="%s" target="_blank" rel="noopener">'
                       '<b>%s</b><span>%s</span><em>%s</em></a>'
                       % (url, label, what, host))
        out.append('  </div>')
    if a['note']:
        out.append('  <p class="anote">%s</p>' % a['note'])
    meta = []
    if a['tool']:
        meta.append('<span><b>Tools</b> %s</span>' % a['tool'])
    if a['path']:
        meta.append('<span><b>Pathway</b> <a href="%spathways/%s.html">%s</a></span>'
                    % (r, a['path'], PATH_NAMES.get(a['path'], a['path'])))
    if meta:
        out.append('  <div class="meta">%s</div>' % ''.join(meta))
    out.append('</article>')
    return '\n'.join(out)


def unit_list(g):
    out = ['<div class="units">']
    for i, (t, d) in enumerate(g['units'], 1):
        out.append('  <div class="u"><span class="n">%d</span><div>'
                   '<p class="ut">%s</p>%s</div></div>'
                   % (i, t, ('<p class="ud">%s</p>' % d) if d else ''))
    out.append('</div>')
    return '\n'.join(out)


def page(key, depth=1):
    g = GD.by_key(key)
    r = '../' * depth
    style = ('--g-lt:%s;--g-dk:%s;--g-slt:%s;--g-sdk:%s'
             % (g['ink'], g['ink_dark'], g['soft'], g['soft_dark']))
    out = ['<div class="wrap gradepage" style="%s">' % style,
           hero(g, depth),
           '<section>',
           '  <p class="lede">%s</p>' % g['lede'],
           '</section>']

    work = GW.WORK.get(key)
    briefs = BT.briefs(key)
    if work:
        out.append('<section>')
        out.append('  <h2>The units this year</h2>')
        out.append('  <p class="sub">The frame the assignments hang on.</p>')
        out.append(unit_list(g))
        out.append('</section>')
        n_full = sum(1 for a in work if a['title'] in briefs)
        if n_full:
            out.append(
                '<div class="note acc"><p><strong>%d of these carry the full '
                'brief</strong> &mdash; the instructions exactly as Classroom '
                'words them, not a summary. Where a brief is missing it is '
                'because Classroom has none either, and the entry says so.'
                '</p></div>' % n_full)
        else:
            out.append(
                '<div class="note"><p><strong>These are the assignments and '
                'their shape, not yet their full instructions.</strong> The '
                'briefs live inside each Classroom post and are being moved '
                'here the same way Grade 11&rsquo;s were. Until then, open the '
                'assignment in Classroom for the wording.</p></div>')
        if any('[&hellip;]' in v or '[…]' in v for v in briefs.values()):
            out.append(
                '<div class="note warn"><p><strong>Where you see '
                '&ldquo;[&hellip;]&rdquo;, a word is missing in the original '
                'Classroom post</strong> &mdash; not here. Those assignments '
                'were pasted in from a document and Classroom dropped some of '
                'the key terms on save, so the gap is in what you are reading '
                'in Classroom too. Ask Mr. Frank for the missing word rather '
                'than guessing at it.</p></div>')
        for tkey, tlabel in GW.TERMS:
            items = [a for a in work if a['t'] == tkey]
            if not items:
                continue
            n = len(items)
            out.append('<section class="term" id="term-%s">' % tkey)
            out.append('  <div class="termhd"><h2>%s</h2>'
                       '<span class="tc">%d %s</span></div>'
                       % (tlabel, n, 'entry' if n == 1 else 'entries'))
            for a in items:
                out.append(assignment(a, depth,
                                      full=briefs.get(a['title'], ''),
                                      gkey=key))
            out.append('</section>')
        out.append(
            '<section><div class="note acc"><p><strong>This is the reference '
            'copy, not the gradebook.</strong> What is due, and when, lives in '
            'Google Classroom. This page is here so that a brief you half '
            'remember from November is still findable in April &mdash; and so '
            'you can read next term before you get there.</p></div></section>')
    else:
        out.append('<section>')
        out.append('  <h2>The units for the year</h2>')
        out.append('  <p class="sub">Quoted from the shop&rsquo;s Grade %d unit '
                   'breakdown. The order is the plan, not a promise.</p>' % g['num'])
        out.append(unit_list(g))
        out.append('</section>')
        out.append('<section><div class="gempty">'
                   '<p><strong>Assignments for this year live in Google '
                   'Classroom.</strong> %s delivers Grade %d, and this page '
                   'deliberately stops at the unit map rather than guessing at '
                   'his assignments.</p>'
                   '<p>If you want the briefs here too, they can be added the '
                   'same way Grades 11 and 12 were.</p></div></section>'
                   % (g['teacher'], g['num']))
        if g.get('exploratory'):
            e = SP.EXPLORATORY
            out.append('<section id="exploratory" class="expl">')
            out.append('  <h2>%s</h2>' % e['title'])
            out.append('  <p class="sub">%s</p>' % e['lede'])
            out.append('  <div class="exgrid">')
            for t, d in e['what']:
                out.append('    <article><b>%s</b><p>%s</p></article>' % (t, d))
            out.append('  </div>')
            out.append('  <div class="note acc"><p><strong>Three things worth '
                       'doing while you are here.</strong></p><ul>')
            for a in e['ask']:
                out.append('    <li>%s</li>' % a)
            out.append('  </ul></div>')
            out.append(
                '  <div class="doors" style="margin-top:20px">'
                '<a href="%sstart/engineering.html"><span class="n">The real '
                'answer</span><b>What engineering actually is</b>'
                '<span>The design process, the seven roles, and what the job '
                'is once you are doing it.</span></a>'
                '<a href="%spathways/index.html"><span class="n">Seven '
                'areas</span><b>Pick a pathway</b><span>The clearest picture '
                'of where this shop can take you.</span></a>'
                '</div>' % (r, r))
            out.append('</section>')

    out.append(
        '<section><h2>Wherever you are in the shop</h2>'
        '<div class="doors">'
        '<a href="%sshop/index.html"><b>Safety</b>'
        '<span>Rules, equipment checks, SDS sheets</span></a>'
        '<a href="%sstart/how-class-works.html"><b>How this class works</b>'
        '<span>Rules, uniform, grading</span></a>'
        '<a href="%slogbook/index.html"><b>The logbook</b>'
        '<span>What goes in it, every day</span></a>'
        '<a href="%sresources/index.html"><b>Training and credentials</b>'
        '<span>Every platform the shop uses</span></a>'
        '</div></section>' % (r, r, r, r))
    out.append('</div>')
    return '\n'.join(out)


INDEX_CSS = CSS + '''
.gi .lede{max-width:640px}
'''


def index(depth=1):
    r = '../' * depth
    out = ['<div class="wrap gi">',
           '<section class="hero">',
           '  <p class="eyebrow">Blue Hills Regional Technical School</p>',
           '  <h1>Find your year</h1>',
           '  <p class="lede">Four years, four homes. Both instructors work '
           'with every student in the shop &mdash; the grade tells you whose '
           'Google Classroom your assignments come from, and which units you '
           'are working through.</p>',
           '</section>',
           '<section>',
           '  <div class="gcards">']
    for g in GD.GRADES:
        work = GW.WORK.get(g['key'])
        count = ('%d assignments listed' % len(work)) if work \
            else '%d units mapped' % len(g['units'])
        out.append(
            '    <a class="gcard" href="%s.html" style="%s">'
            '<img src="%sassets/%s" alt="" loading="lazy">'
            '<div class="cb"><p class="cn">Grade %d</p>'
            '<p class="ct">%s</p>'
            '<p class="cw">%s &middot; %s</p></div></a>'
            % (g['key'],
               '--g-lt:%s;--g-dk:%s;--g-slt:%s;--g-sdk:%s'
               % (g['ink'], g['ink_dark'], g['soft'], g['soft_dark']),
               r, g['banner'], g['num'], g['course'],
               g['teacher'], count))
    out.append('  </div>')
    out.append('</section>')
    out.append(
        '<section><h2>How the four years fit together</h2>'
        '<p>Grade 9 is the half-year you join the shop and start building in '
        'it. Grade 10 adds the certifications &mdash; OSHA among them &mdash; '
        'and raises the documentation standard. '
        'Grade 11 is the widest year, with projects across every '
        'pathway. Grade 12 narrows again: two terms of sharp briefs, then one '
        'capstone you choose and run yourself.</p>'
        '<div class="note"><p><strong>Who teaches what.</strong> '
        'Mr. Dryer delivers Grades 9 and 10; Mr. Frank delivers Grades 11 and '
        '12. That is about whose Classroom the work comes from, not about who '
        'you can ask &mdash; both are in the shop with all four years, and '
        '<a href="' + r + 'pathways/index.html">the pathways page</a> says '
        'which of them to go to for which kind of problem.</p></div></section>')
    out.append('</div>')
    return '\n'.join(out)
