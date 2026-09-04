#!/usr/bin/env python3
"""
Builds the BHR Engineering Shop Hub as a plain folder of HTML files.

Host-agnostic on purpose: every link is relative and every page ends in
.html, so the site works three ways with no changes --
  * opened straight off disk (file://)
  * pushed to GitHub Pages
  * pushed to GitLab Pages (the included .gitlab-ci.yml handles it)

Run:  python3 build_site.py
Out:  ./site/
"""

import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_hubs as B          # noqa: E402  (pathway content lives there)
import build_resources as RES   # noqa: E402  (training platforms and credentials)
import build_safety as SAFE     # noqa: E402  (shop safety, rules, SDS, quizzes)
import build_search as SEARCH   # noqa: E402  (the static search index)
import search_ui as SUI         # noqa: E402  (search box, styles, behaviour)
import pathway_nav as PNAV      # noqa: E402  (per-hub section summaries)
import site_nav as SNAV        # noqa: E402  (the site-wide rail)
import theme_ui as THEME       # noqa: E402  (light / dark switch)
import build_grades as GR      # noqa: E402  (the four grade homes)
import grade_data as GD        # noqa: E402
import build_extras as EX      # noqa: E402  (instructors, Do Nows, links)
import quick_bar as QBAR       # noqa: E402  (the grade / instructor strip)

FONTS = {
    'a': dict(name='Space Grotesk + Literata',
              google='family=Space+Grotesk:wght@500;600;700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=JetBrains+Mono:wght@400;500;700',
              sans='"Space Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif',
              serif='"Literata",Georgia,"Times New Roman",serif',
              mono='"JetBrains Mono",ui-monospace,Consolas,monospace', heavy='800'),
    'b': dict(name='Chakra Petch + Source Serif',
              google='family=Chakra+Petch:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Space+Mono:wght@400;700',
              sans='"Chakra Petch",system-ui,-apple-system,"Segoe UI",sans-serif',
              serif='"Source Serif 4",Georgia,"Times New Roman",serif',
              mono='"Space Mono",ui-monospace,Consolas,monospace', heavy='700'),
    'c': dict(name='Outfit + Newsreader',
              google='family=Outfit:wght@500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=IBM+Plex+Mono:wght@400;500;600',
              sans='"Outfit",system-ui,-apple-system,"Segoe UI",sans-serif',
              serif='"Newsreader",Georgia,"Times New Roman",serif',
              mono='"IBM Plex Mono",ui-monospace,Consolas,monospace', heavy='800'),
}
FONT = os.environ.get('BHR_FONT', 'b')

SRC = '/tmp/outputs'
OUT = '/tmp/outputs/site'

# ---------------------------------------------------------------- site chrome

NAV = [
    ('Home',        'index.html',                  'home'),
    ('Start here',  'start/welcome.html',          'start'),
    ('Grades',      'grades/index.html',           'grades'),
    ('Logbook',     'logbook/index.html',          'logbook'),
    ('Pathways',    'pathways/index.html',         'pathways'),
    ('Safety',      'shop/index.html',             'shop'),
    ('Training',    'resources/index.html',        'resources'),
]


def rel(depth):
    return '../' * depth


BUILD = ''     # a visible stamp so anyone can tell which build they are seeing
ASSET_V = {}   # filled in at build time: filename -> short content hash


def v(name):
    """Cache-busting suffix. Browsers hold on to a stylesheet by filename, which
    is why a rebuilt site can look unchanged until a hard reload; a hash in the
    query string makes a changed file a different URL."""
    return '?v=' + ASSET_V.get(name, '0')


def shell(title, body, depth=0, section='', page_css='', desc='',
          path='', anchors=None):
    r = rel(depth)
    rail = SNAV.render(path, r, anchors)
    qbar = QBAR.render(path, r)
    css = '\n<style>\n%s\n</style>' % page_css.strip() if page_css.strip() else ''
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s &middot; BHR Engineering</title>
<meta name="description" content="%(desc)s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?%(gf)s&display=swap">
<link rel="icon" href="%(r)sassets/icon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="%(r)sassets/icon-180.png">
<link rel="stylesheet" href="%(r)sassets/site.css%(v)s">%(css)s
%(themehead)s
</head>
<body>

<header class="sitebar">
  <div class="in">
    <a class="brand" href="%(r)sindex.html">
      <img class="mark" src="%(r)sassets/logo-96.png" alt="" width="34" height="29">
      <span>Engineering&nbsp;Technology</span>
    </a>
%(srch)s
%(themebtn)s
  </div>
</header>
%(qbar)s

<div class="shell">
%(rail)s
<div class="main">
%(body)s
</div>
</div>

<footer class="sitefoot">
  <div class="in">
    <span>Blue Hills Regional Technical School</span>
    <span>Engineering Technology &middot; Room E-126</span>
    <span>Mr. Frank &middot; Mr. Dryer</span>
    <span class="build">Build %(build)s</span>
  </div>
</footer>

%(js)s
</body>
</html>
''' % dict(title=title, desc=desc, r=r, css=css, rail=rail, body=body, qbar=qbar,
                gf=FONTS[FONT]['google'], srch=SUI.BOX, v=v('site.css'),
                build=BUILD, themehead=THEME.HEAD, themebtn=THEME.BUTTON,
                js=SUI.JS % dict(r=r, rel=repr(r), sv=v('search-index.js')) + SNAV.JS + THEME.JS)


def label_table_cells(html):
    """Stamp each <td> with the text of its column heading.

    On a phone a four-column table has to stack, and a stacked cell with no
    column name is meaningless -- "35%" on its own line tells a student
    nothing. The stylesheet prints these labels back in at narrow widths.
    Done here, at build time, so no page has to remember to do it and a table
    added later gets it for free.
    """
    def one(m):
        table = m.group(0)
        head = re.search(r'<thead>(.*?)</thead>', table, re.S)
        if not head:
            return table
        heads = [re.sub(r'<[^>]+>', '', h).strip()
                 for h in re.findall(r'<th[^>]*>(.*?)</th>', head.group(1), re.S)]
        if not heads:
            return table

        body_start = table.find('</thead>')
        head_part, body_part = table[:body_start], table[body_start:]

        def row(rm):
            col = [0]

            def cell(cm):
                i = col[0]
                col[0] += 1
                if i >= len(heads) or 'data-label' in cm.group(1):
                    return cm.group(0)
                lbl = heads[i].replace('"', '&quot;')
                return '<td%s data-label="%s">%s</td>' % (cm.group(1), lbl,
                                                          cm.group(2))
            return re.sub(r'<td([^>]*)>(.*?)</td>', cell, rm.group(0), flags=re.S)

        body_part = re.sub(r'<tr.*?</tr>', row, body_part, flags=re.S)
        return head_part + body_part

    return re.sub(r'<table.*?</table>', one, html, flags=re.S)


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if path.endswith('.html'):
        text = label_table_cells(text)
    open(full, 'w', encoding='utf-8').write(text)
    print('  %-42s %6d' % (path, len(text)))


# ------------------------------------------------- porting existing artifacts

STRIP_SELECTORS = (':root', '@media (prefers-color-scheme', 'body', '*', 'html')


LEGACY_FONTS = [
    ('"Archivo",system-ui,sans-serif', 'var(--sans)'),
    ('"Archivo",sans-serif', 'var(--sans)'),
    ('"Archivo"', 'var(--sans)'),
    ('"Spectral",Georgia,serif', 'var(--serif)'),
    ('"Spectral"', 'var(--serif)'),
    ('"IBM Plex Mono",monospace', 'var(--mono)'),
    ('"IBM Plex Mono"', 'var(--mono)'),
]


def tokenise_fonts(css):
    """Legacy artifact CSS names the old typefaces directly. Point every one of
    them at the palette tokens so a font change is still a single switch."""
    for old, new in LEGACY_FONTS:
        css = css.replace(old, new)
    # no face is guaranteed to have an 800
    css = css.replace('font-weight:800', 'font-weight:var(--w-heavy)')
    return css


def strip_globals(css):
    """Remove rules that site.css now owns, so the shared palette wins.

    Anything else in the page's original stylesheet is page-specific layout
    and is kept, sitting after site.css in the cascade."""
    out, i, n = [], 0, len(css)
    while i < n:
        # find the start of the next top-level rule
        j = css.find('{', i)
        if j == -1:
            out.append(css[i:])
            break
        sel = css[i:j].strip()
        # walk to the matching close brace
        depth, k = 0, j
        while k < n:
            if css[k] == '{':
                depth += 1
            elif css[k] == '}':
                depth -= 1
                if depth == 0:
                    break
            k += 1
        block = css[i:k + 1]
        drop = any(sel.startswith(s) for s in STRIP_SELECTORS)
        # keep @media blocks that are not the colour-scheme ones
        if sel.startswith('@media') and 'prefers-color-scheme' not in sel:
            drop = False
        if not drop:
            out.append(block)
        i = k + 1
    return tokenise_fonts('\n'.join(x.strip() for x in out if x.strip()))


def port(filename):
    """Pull the page CSS and the .wrap body out of one of the artifacts."""
    t = open(os.path.join(SRC, filename), encoding='utf-8').read()
    css = ''
    m = re.search(r'<style>(.*?)</style>', t, re.S)
    if m:
        css = strip_globals(m.group(1))
    # body = everything from the first <div class="wrap"> to its close
    m = re.search(r'<div class="wrap"[^>]*>', t)
    if not m:
        raise SystemExit('no .wrap in ' + filename)
    start = m.start()
    # last </div> before any trailing <script>
    tail = t.rfind('</div>')
    body = t[start:tail + 6]
    scripts = re.findall(r'<script>.*?</script>', t, re.S)
    return css, body + ('\n' + '\n'.join(scripts) if scripts else '')


# ---------------------------------------------------------------- home page

HOME_CSS = '''
.doors{display:grid;grid-template-columns:repeat(auto-fit,minmax(292px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.doors a{background:var(--card);padding:22px 22px 24px;text-decoration:none;color:inherit;
  display:flex;flex-direction:column;gap:7px;box-shadow:0 0 0 1px var(--rule);
  transition:background .12s ease}
.doors a:hover{background:var(--accent-soft)}
.doors .n{font-family:var(--mono);font-size:10px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--ink-3)}
.doors b{font-family:var(--sans);font-weight:700;font-size:19px;line-height:1.2;
  letter-spacing:-.015em}
.doors span{font-size:15px;color:var(--ink-2);line-height:1.5}
.quicklinks{display:grid;grid-template-columns:repeat(auto-fit,minmax(152px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.quicklinks a{background:var(--card);box-shadow:0 0 0 1px var(--rule);
  padding:13px 17px;text-decoration:none;
  color:var(--ink-2);font-size:15px;font-family:var(--sans);font-weight:500}
.quicklinks a:hover{background:var(--accent-soft);color:var(--accent)}
.stripe{display:flex;height:6px;margin-top:-24px}
.stripe i{flex:1}
'''

HOME = '''
<div class="wrap wide">

  <header class="hero">
    <p class="kicker">Blue Hills Regional Technical School</p>
    <h1>The Shop Hub</h1>
    <p>Everything for Engineering Technology in one place &mdash; how the shop runs,
      what is expected, and where to go deep. Your assignments live in Google Classroom
      and link back here.</p>
  </header>

  <section>
    <h2>Start here</h2>
    <p class="sub">Seven doors. If you are new, take the first one.</p>
    <div class="doors">
      <a href="start/welcome.html">
        <span class="n">New here</span>
        <b>Welcome to the shop</b>
        <span>Who to ask for what, what to wear, what you can earn, and how the first week goes.</span>
      </a>
      <a href="start/how-class-works.html">
        <span class="n">The ground rules</span>
        <b>How this class works</b>
        <span>The rules, the uniform, and exactly how your grade is put together.</span>
      </a>
      <a href="grades/index.html">
        <span class="n">Your year</span>
        <b>Grade 9, 10, 11 or 12</b>
        <span>Each year has its own home: the units it covers, and the assignments that fill them.</span>
      </a>
      <a href="logbook/index.html">
        <span class="n">Every day</span>
        <b>Your engineering logbook</b>
        <span>The status codes, the three intervals, and what a real entry looks like.</span>
      </a>
      <a href="pathways/index.html">
        <span class="n">Juniors and seniors</span>
        <b>Pick a pathway</b>
        <span>Seven fields to spend a term going deep on. Start with the chooser.</span>
      </a>
      <a href="shop/index.html">
        <span class="n">Before you build</span>
        <b>Shop safety</b>
        <span>The Makerspace rules, machine certification, and the safety data sheets.</span>
      </a>
      <a href="resources/index.html">
        <span class="n">Go further</span>
        <b>Training and credentials</b>
        <span>Every platform and certificate the shop uses or recommends, and what each
          one is actually good for.</span>
      </a>
    </div>
  </section>

  <section>
    <h2>The seven pathways</h2>
    <p class="sub">Each one is the home of one state technical standard. Straight to a guide:</p>
    <div class="quicklinks">
      __PATHLINKS__
    </div>
  </section>

  <section>
    <h2>Where things live</h2>
    <dl class="defs">
      <dt>This site</dt>
      <dd>Instructions, rules, guides, examples and rubrics &mdash; everything that is the same
        for everyone. It is always the current version, so an old assignment still points at
        the right thing.</dd>
      <dt>Google Classroom</dt>
      <dd>Your assignments, your copies of the templates, and turning work in. Grades are there,
        not here.</dd>
      <dt>Your Google Drive</dt>
      <dd>Your own work. Your logbook, your CAD, your reports. Nothing of yours is ever
        posted on this site.</dd>
    </dl>
    <p class="note">Something out of date, wrong, or missing? Tell Mr. Frank &mdash; pages here
      get fixed the same day rather than at the end of the year.</p>
  </section>

</div>
'''


NOTFOUND = '''
<div class="wrap">
  <section class="hero">
    <p class="eyebrow">404</p>
    <h1>That page isn&rsquo;t here</h1>
    <p class="lede">The link you followed is out of date, or the address has a
    typo in it. Nothing is broken &mdash; the page just moved or never existed.</p>
  </section>

  <div class="nf">
    <h2>Try one of these</h2>
    <ul>
      <li><a href="index.html">The Shop Hub home page</a> &mdash; the four doors</li>
      <li><a href="start/how-class-works.html">How the class works</a> &mdash; rules, uniform, grading</li>
      <li><a href="shop/index.html">Safety</a> &mdash; rules, equipment checks, SDS sheets</li>
      <li><a href="pathways/index.html">The seven pathways</a> &mdash; find a project</li>
      <li><a href="resources/index.html">Training and certification</a></li>
    </ul>
    <p class="nfp">Or use the search box at the top of any page &mdash; it
    covers every page on the site.</p>
  </div>
</div>
'''

NOTFOUND_CSS = '''
.nf{max-width:640px;padding:26px 28px;background:var(--card);
border:1px solid var(--rule);border-radius:10px}
.nf h2{margin:0 0 14px;font-size:1.15rem}
.nf ul{margin:0;padding-left:20px}
.nf li{margin:0 0 9px;line-height:1.5}
.nfp{margin:18px 0 0;color:var(--ink2);font-size:.94rem}
'''


def build_404():
    """GitHub Pages serves /404.html for any path it cannot find.

    The links below are relative and correct from the site root, which is
    where the overwhelming majority of bad links land. Absolute paths would
    be wrong, because this site also has to work from a file:// folder and
    from a project subpath like /bhr-hub/. The search box in the header works
    from any depth regardless.
    """
    write('404.html', shell('Page not found', NOTFOUND, depth=0, section='',
                            path='404.html', page_css=NOTFOUND_CSS,
                            desc='That page is not here — try the hub, safety, '
                                 'the pathways, or the search box.'))


def build_grades():
    write('grades/index.html',
          shell('Find your year', GR.index(), depth=1, section='grades',
                path='grades/index.html', page_css=GR.INDEX_CSS,
                desc='The four grade homes -- Engineering I to IV, who '
                     'delivers each, and what the year holds.'))
    for g in GD.GRADES:
        write('grades/%s.html' % g['key'],
              shell('Grade %d &mdash; %s' % (g['num'], g['course']),
                    GR.page(g['key']), depth=1, section='grades',
                    path='grades/%s.html' % g['key'], page_css=GR.CSS,
                    desc='Grade %d Engineering Technology at Blue Hills '
                         'Regional: units, assignments and what each one asks '
                         'for.' % g['num']))


def build_extras():
    for k, name in (('frank', 'Mr. Frank'), ('dryer', 'Mr. Dryer')):
        write('staff/%s.html' % k,
              shell(name, EX.staff_page(k), depth=1, section='staff',
                    path='staff/%s.html' % k, page_css=EX.CSS,
                    desc='%s: what he covers, which grades he delivers, which '
                         'pathways he leads, and what to bring him.' % name))
    write('extras/do-nows.html',
          shell('Do Nows and bonus work', EX.donows(), depth=1,
                section='extras', path='extras/do-nows.html', page_css=EX.CSS,
                desc='The short skill tasks and the assignments outside the '
                     'project spine, grouped by what they build.'))
    write('extras/links.html',
          shell('Links', EX.links(), depth=1, section='extras',
                path='extras/links.html', page_css=EX.CSS,
                desc='Reference, channels, model libraries and career data '
                     'worth keeping a tab open for.'))


def build_home():
    links = '\n      '.join(
        '<a href="pathways/%s.html">%s</a>' % (p['key'], p['nav']) for p in B.P)
    body = HOME.replace('__PATHLINKS__', links)
    write('index.html', shell('The Shop Hub', body, depth=0, section='home',
                              path='index.html',
                              page_css=HOME_CSS,
                              desc='Engineering Technology at Blue Hills Regional — rules, '
                                   'logbook, grading and the seven pathway guides.'))


# ---------------------------------------------------------------- pathways

PATH_CSS_EXTRA = '''
.pathnav{display:grid;grid-template-columns:repeat(auto-fit,minmax(158px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule);margin-top:-18px}
.pathnav a{background:var(--card);box-shadow:0 0 0 1px var(--rule);
  padding:10px 14px;text-decoration:none;
  color:var(--ink-2);font-size:13.5px;font-family:var(--sans);font-weight:500;
  display:flex;gap:8px;align-items:baseline}
.pathnav a:hover{background:var(--accent-soft);color:var(--accent)}
.pathnav a[aria-current="page"]{background:var(--accent-soft);color:var(--accent);font-weight:600}
.pathnav .std{font-family:var(--mono);font-size:11px;color:var(--ink-3);flex:none}
.pathnav a[aria-current="page"] .std{color:var(--accent)}
.pagebody{display:flex;flex-direction:column}
'''


def anchor_topics(html):
    """Give every topic block an id so the sidebar can jump to it.

    The id comes from the number the block actually displays, so it cannot drift
    if the order changes; the unnumbered training block becomes ttrain."""
    def sub(m):
        num = m.group(1).strip()
        tid = 't' + num if num.isdigit() else 'ttrain'
        return '<div class="topic" id="%s"><div class="th"><span class="tn">%s</span>' % (
            tid, m.group(1))
    return re.sub(r'<div class="topic">\s*<div class="th"><span class="tn">([^<]*)</span>',
                  sub, html)


def pathway_nav(current):
    return ('<div class="pathnav">\n' + '\n'.join(
        '  <a href="%s.html"%s><span class="std">%s</span>%s</a>' % (
            p['key'], ' aria-current="page"' if p['key'] == current else '',
            p['std'], p['nav'])
        for p in B.P) + '\n</div>')


def build_pathways():
    # the guide CSS, minus the tabbed-view machinery the single-page version needed
    m = re.search(r'<style>(.*?)</style>', open(os.path.join(SRC, 'eep-guides.html'),
                                                encoding='utf-8').read(), re.S)
    css = strip_globals(m.group(1))
    for dead in ('.shell', 'nav{', 'nav button', '.nt', '.navgroup', '.view'):
        css = '\n'.join(ln for ln in css.split('\n') if not ln.strip().startswith(dead))
    css = css.replace('.view{display:none}', '').replace('.view.on{display:block}', '')
    css += PATH_CSS_EXTRA + RES.CSS + RES.SRC_CSS + PNAV.CSS + PNAV.FIRST_CSS

    for p in B.P:
        inner = B.render_pathway(p)
        inner = re.sub(r'^<section class="view" id="v-[a-z]+">', '', inner).rstrip()
        if inner.endswith('</section>'):
            inner = inner[:-len('</section>')]
        # sources for each of the five topics, injected inside that topic
        keys = ['field', 'learn', 'skills', 'build', 'files']
        for i, k in enumerate(keys, start=1):
            blk = RES.sources_block(p['key'], k)
            if not blk:
                continue
            nxt = '<div class="topic"><div class="th"><span class="tn">%d</span>' % (i + 1)
            if nxt in inner:
                inner = inner.replace(nxt, blk + '\n' + nxt, 1)
            else:
                inner += '\n' + blk

        tb = RES.train_block(p['key'])
        marker = '<div class="topic"><div class="th"><span class="tn">4</span>'
        if tb and marker in inner:
            inner = inner.replace(marker, tb + '\n' + marker, 1)
        else:
            inner += '\n' + tb
        # a concrete opening move, before the five topics
        fm = PNAV.first_move(p)
        k = inner.find('<div class="topic">')
        inner = (inner[:k] + fm + '\n' + inner[k:]) if k > -1 else (fm + inner)
        inner = anchor_topics(inner)
        anchors = [(it['id'], it['name'], it['num'])
                   for it in PNAV.items(p['key'], bool(tb))]
        body = ('<div class="wrap">\n<div class="pagebody">' + inner
                + '</div>\n</div>')
        write('pathways/%s.html' % p['key'],
              shell(p['title'], body, depth=1, section='pathways', page_css=css,
                    path='pathways/%s.html' % p['key'], anchors=anchors,
                    desc='%s pathway guide — Standard %s. %s' %
                         (p['title'], p['std'][1:], p['tag'])))

    # pathways/index.html — the chooser, with the overview appended
    ch_css, ch_body = port('eep-chooser.html')
    ov = B.overview
    ov = ov.replace('<section class="view on" id="v-overview">', '<section>')
    ov = re.sub(r'<div class="ph">.*?</div>\s*(?=<div class="topic">)', '', ov, flags=re.S)
    ch_body = ch_body.rstrip()
    assert ch_body.endswith('</div>')
    ch_body = ch_body[:-6] + '\n' + pathway_nav(None) + '\n' + ov + '\n</div>'
    write('pathways/index.html',
          shell('Pick Your Pathway', ch_body, depth=1, section='pathways',
                path='pathways/index.html', page_css=ch_css + css,
                desc='Choose one of the seven Elective Engineering Pathways, and what '
                     'each hub is for.'))


# ---------------------------------------------------------------- other pages

def build_ported():
    css, body = port('logbook.html')
    write('logbook/index.html',
          shell('Your Engineering Logbook', body, depth=1, section='logbook', page_css=css,
                path='logbook/index.html',
                desc='How to keep the daily engineering logbook: status codes, the three '
                     'intervals, the rules, and a worked example.'))

    css, body = port('how-class-works.html')
    write('start/how-class-works.html',
          shell('How This Class Works', body, depth=1, section='start', page_css=css,
                path='start/how-class-works.html',
                desc='Classroom rules, uniform expectations, and exactly how the grade '
                     'is calculated.'))


# ---------------------------------------------------------------- repo files

GITLAB_CI = '''# GitLab Pages. Ignored by GitHub Pages, which needs no config at all.
# The site is plain HTML, so there is nothing to build -- this job just moves
# the files into the "public" folder GitLab publishes from.
pages:
  stage: deploy
  image: alpine:latest
  script:
    - mkdir -p public
    - cp -r index.html 404.html assets start logbook pathways shop resources public/
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
'''

README = '''# BHR Engineering Technology — Shop Hub

The public reference site for the Engineering Technology program at
Blue Hills Regional Technical School. Google Classroom assignments link here
instead of repeating instructions; this site holds the version that is current.

## The one rule

**No student data, ever.** No names, no rosters, no submitted work, no grades,
no photographs of students, no contact details. A public repository keeps every
file in its history permanently — deleting something later does not remove it.
Everything here is material any student would be handed on day one.

Also not here: budget, purchasing, personnel documents, recommendation letters.

## Working on it locally

There is no build step and no dependencies. Open `index.html` in a browser and
the whole site works off disk — every link is relative and every page ends in
`.html`, which is also why it works unchanged on any host.

## Layout

    index.html                 home — the doors
    404.html                   served for any address that does not exist
    grades/index.html          the four grade homes
    grades/<9|10|11|12>.html   units, and assignments by term
    staff/frank.html           Mr. Frank — EDF, grades 11 and 12
    staff/dryer.html           Mr. Dryer — ESEC, grades 9 and 10
    extras/do-nows.html        Do Nows and bonus work, grouped by skill
    extras/links.html          reference, channels, model libraries, careers
    assets/site.css            palette, base type, site chrome, shared components
    start/welcome.html         welcome packet
    start/how-class-works.html rules, uniform, grading
    logbook/index.html         the daily logbook guide
    pathways/index.html        chooser + how the hubs are organised
    pathways/<name>.html       one per pathway, seven of them
    shop/index.html            safety hub
    shop/makerspace.html       the 32 Makerspace rules + self-check
    shop/sds.html              safety data sheet library
    shop/3d-printing.html      3D printer certification ladder

Page-specific layout lives in a `<style>` block in that page. Anything shared —
colour, type, tables, notes, the header and footer — lives in `assets/site.css`,
so a palette change is one edit.

Shop colour is purple (`--accent`). School colours, blue and green, are accents
only. Both light and dark themes are defined; test any change in both.

## Putting it on GitHub, from nothing

1. New repository. Any name — `bhr-shop-hub` reads well in the URL. **Public**:
   Pages on a private repo needs a paid plan, and nothing here is sensitive.
   Do not let GitHub add a README, a `.gitignore` or a licence — this folder
   already has what it needs and the extra files only cause a merge conflict
   on the first push.
2. Drag **the contents of this folder** into the upload box — `index.html` has
   to land at the top level of the repository, not inside a `site` folder.
   Dotfiles (`.nojekyll`, `.gitignore`) do not always come along in a drag on
   Windows; if `.nojekyll` is missing afterwards, add it with **Add file →
   Create new file**, name it `.nojekyll`, leave it empty, commit. Without it
   GitHub runs Jekyll over the site and refuses to serve the `_source` folder.
3. Settings → Pages → Source: **Deploy from a branch**, branch `main`, folder
   `/ (root)`. Save.
4. Wait a minute or two, then load the URL it shows you. The first build is
   the slow one.

The address will be `https://<your-account>.github.io/<repo-name>/`. Every link
on the site is relative, so the subfolder in that address changes nothing — the
same files work from a repo subpath, from a custom domain, and from your own
disk with no edits.

**Before you hand the URL to students**, open it once on the school network and
once off it. Some districts filter `github.io` wholesale. If it is blocked,
that is a conversation with IT rather than a problem with the site, and it is
worth having before the QR-code poster gets printed.

## Publishing elsewhere

**GitLab Pages** — `.gitlab-ci.yml` is already here and does the whole job. Push
to the default branch and the pipeline publishes. Check with your administrator
that Pages is enabled, and that a Pages site is reachable from off the school
network — students need this at home.

Leave Pages Access Control **off**. Nothing on this site is sensitive, and a
login wall between a student and their instructions costs more than it protects.

## Linking a Drive template so each student gets their own copy

1. Set the template to "anyone with the link — viewer".
2. Take its URL and replace everything from `/edit` onward with `/copy`.
3. Put that link on a page here.

Note this only works from a link on this site. Attaching a `/copy` link inside a
Google Classroom assignment does not work — Classroom overrides it and shares
the original. For work you collect and grade, use Classroom's own
"make a copy for each student" attachment.

## Rebuilding

Most pages are generated by `build_site.py` (which pulls pathway content from
`build_hubs.py`). Editing the generated HTML directly is fine for a quick fix,
but a rebuild overwrites it — put lasting changes in the source scripts.
'''


def build_resources():
    write('resources/index.html',
          shell('Training and Credentials', RES.page_body(), depth=1,
                section='resources', path='resources/index.html', page_css=RES.CSS,
                desc='Every training platform and credential the shop uses or '
                     'recommends, with what it actually costs.'))


GITIGNORE = '''# Nothing here needs building, so this list is short on purpose.
__pycache__/
*.pyc
.DS_Store
Thumbs.db
desktop.ini
*.zip
.assets-stash/
'''


def build_repo_files():
    write('.gitlab-ci.yml', GITLAB_CI)
    write('README.md', README)
    write('.gitignore', GITIGNORE)
    write('.nojekyll', '')          # stops GitHub Pages running Jekyll over it


# ---------------------------------------------------------------- welcome page

WELCOME_CSS = '''
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.two article{background:var(--card);padding:18px 20px;box-shadow:0 0 0 1px var(--rule);
  display:flex;flex-direction:column;gap:8px}
.two .who{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink-3)}
.two b{font-family:var(--sans);font-weight:600;font-size:16px;line-height:1.35}
.two ul{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:4px;
  font-size:15px;color:var(--ink-2)}
.two li{line-height:1.5}
.pdf{display:inline-flex;align-items:center;gap:9px;text-decoration:none;
  font-family:var(--sans);font-weight:600;font-size:15px;color:var(--accent);
  background:var(--accent-soft);border:1px solid var(--rule);padding:11px 17px;
  align-self:flex-start;margin-top:4px}
.pdf:hover{background:var(--card)}
'''

WELCOME = '''
<div class="wrap">

  <header class="hero">
    <p class="kicker">Engineering Technology &middot; Welcome</p>
    <h1>Welcome to the shop</h1>
    <p>Everything you need for your first week: who to ask for what, what to wear,
      how the shop runs, and how you are graded.</p>
  </header>

  <section>
    <h2>What this program is</h2>
    <p>You are joining a program that treats you like an engineer rather than a student
      who happens to be in a shop. You will design things, build them, test them, and
      explain why they worked or did not. Some of what you make will fail. That is part
      of it &mdash; what matters is that you can say why.</p>
  </section>

  <section>
    <h2>Who to ask for what</h2>
    <p class="sub">Both of us teach across all four years. Go to whoever fits the problem in
      front of you &mdash; you will not be sent away for asking the wrong one.</p>
    <div class="two">
      <article>
        <span class="who">Mr. Frank &middot; Grades 11 &amp; 12</span>
        <b>Helps you make it real</b>
        <ul>
          <li>Designing in CAD so it works and looks right</li>
          <li>Getting a part ready to 3D print or laser cut</li>
          <li>Making a structure that holds up</li>
          <li>Drawings someone else could build from</li>
          <li>Fixing a prototype that came out wrong</li>
        </ul>
      </article>
      <article>
        <span class="who">Mr. Dryer &middot; Grades 9 &amp; 10</span>
        <b>Helps you make it work</b>
        <ul>
          <li>Designing or troubleshooting a circuit</li>
          <li>Writing and debugging code for a board or robot</li>
          <li>Working out why a system misbehaves</li>
          <li>Getting sensors and motors working together</li>
          <li>Showing with data that it does what you claim</li>
        </ul>
      </article>
    </div>
  </section>

  <section>
    <h2>What you can earn here</h2>
    <dl class="defs">
      <dt>OSHA 10 &mdash; Construction</dt>
      <dd>In Grade 10. The credential that lets you work on the equipment, and it is
        recognized well outside this building.</dd>
      <dt>Autodesk Certified User</dt>
      <dd>In Inventor, Fusion 360 and Revit Architecture. Which ones you go for depends on
        the work you are doing and when you are ready.</dd>
      <dt>Cooperative education</dt>
      <dd>Working in a real engineering setting for part of your schedule. Available to
        juniors from Term 3 and seniors from Term 1.</dd>
    </dl>
  </section>

  <section>
    <h2>What to wear</h2>
    <p class="sub">You wear a uniform during your shop week. It is not about looking smart
      &mdash; it is about being dressed for a room with machines in it.</p>
    <div class="tw"><table>
      <thead><tr><th>Item</th><th>What is required</th></tr></thead>
      <tbody>
        <tr><td class="k">Shop attire</td><td>Anything carrying the Engineering Technology logo, bought through the school store &mdash; T-shirts long or short sleeve, hoodies, crew necks, quarter-zips, sweaters. Any of it counts.</td></tr>
        <tr><td class="k">Footwear</td><td>Shoes, sneakers or work boots. <strong>No open-toed shoes, sandals or Crocs</strong> in the Makerspace.</td></tr>
        <tr><td class="k">Eye protection</td><td>Required in the Makerspace. Situational in the main shop &mdash; if you are unsure, put them on.</td></tr>
      </tbody>
    </table></div>
    <p class="note"><strong>Ordering.</strong> Uniforms are ordered at
      <a href="https://store.bluehills.org/">store.bluehills.org</a> during the window posted
      on the website &mdash; that is when pricing is best and delivery to the school is free.
      There is no limit on how many you buy; most students get at least two. Refer to the
      Blue Hills Parent/Student Handbook for anything else about attire.</p>
  </section>

  <section>
    <h2>Safety, in short</h2>
    <p class="sub">The full rules are posted in the shop and you will be trained on them.
      These are the ones that matter before you touch anything.</p>
    <ul class="ticks">
      <li>Report every injury immediately, however small. If a chemical gets in your eyes,
        wash for <strong>15 minutes</strong> before seeking treatment.</li>
      <li>Never use a tool you have not been trained and authorized on.</li>
      <li>Never work alone with power tools &mdash; two people, both visible to each other.</li>
      <li>Machines run only with all guards and shields in place. Never walk away from a
        running tool.</li>
      <li>Clean your area every time you leave it, including the floor.</li>
    </ul>
  </section>

  <section>
    <h2>Next</h2>
    <p class="sub">Two things worth reading in your first week.</p>
    <div class="grid">
      <article>
        <b><a href="how-class-works.html">How this class works</a></b>
        <p>The classroom rules, and exactly how your grade is put together &mdash; including
          why half of it is about how you work rather than what you make.</p>
      </article>
      <article>
        <b><a href="../logbook/index.html">Your engineering logbook</a></b>
        <p>You fill one in every shop day. Read this before your first one, not after.</p>
      </article>
    </div>
  </section>

</div>
'''


def build_welcome():
    write('start/welcome.html',
          shell('Welcome to the Shop', WELCOME, depth=1, section='start',
                path='start/welcome.html',
                page_css=WELCOME_CSS,
                desc='Who to ask for what, what to wear, what you can earn, and the safety '
                     'essentials for your first week.'))


# ------------------------------------------------------- 3D printer access

PRINT_CSS = '''
.ladder{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.ladder article{background:var(--card);padding:19px 21px 21px;box-shadow:0 0 0 1px var(--rule);
  display:flex;flex-direction:column;gap:8px}
.ladder .lv{font-family:var(--mono);font-size:10px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--ink-3)}
.ladder b{font-family:var(--sans);font-weight:700;font-size:18px;line-height:1.25;
  letter-spacing:-.015em}
.ladder p{margin:0;color:var(--ink-2);font-size:15px;line-height:1.5}
.seq{display:flex;flex-wrap:wrap;align-items:stretch;gap:0;
  border:1px solid var(--rule);background:var(--card)}
.seq .m{flex:1 1 180px;padding:17px 20px;display:flex;flex-direction:column;gap:5px;
  border-right:1px solid var(--rule)}
.seq .m:last-child{border-right:0}
.seq .n{font-family:var(--mono);font-size:10px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--ink-3)}
.seq b{font-family:var(--sans);font-weight:700;font-size:19px;letter-spacing:-.02em}
.seq span.d{font-size:14.5px;color:var(--ink-2);line-height:1.45}
.gate{background:var(--accent);color:#fff;border:1px solid var(--accent);
  padding:16px 21px;font-family:var(--sans);font-weight:600;font-size:16.5px;
  line-height:1.45}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .gate{color:#150f22}}
:root[data-theme="dark"] .gate{color:#150f22}
.eg{background:var(--accent-soft);border:1px solid var(--rule);padding:15px 20px;
  font-size:15.5px;color:var(--ink-2);line-height:1.55}
.eg b{color:var(--ink);font-family:var(--sans)}
'''

PRINTING = '''
<div class="wrap">

  <header class="hero">
    <p class="kicker">Shop access &middot; Makerspace</p>
    <h1>3D printer certification</h1>
    <p>How much you can do on a printer on your own depends on how much training you
      have done on that machine. This page is the whole rule.</p>
  </header>

  <section>
    <p class="gate">Every print job is approved by an instructor first &mdash; at every
      level, on every machine, no exceptions. Certification changes who has to stand
      next to you, not whether you need approval.</p>
  </section>

  <section>
    <h2>The three levels</h2>
    <p class="sub">You earn these one machine at a time. Being certified on the A1 Mini
      says nothing about the X1C.</p>
    <div class="ladder">
      <article>
        <span class="lv">Level one</span>
        <b>Beginner</b>
        <p>You can print <strong>with an instructor helping you</strong>. This is the
          minimum to touch the machine at all.</p>
      </article>
      <article>
        <span class="lv">Level two</span>
        <b>Intermediate</b>
        <p>You can print <strong>with an approved peer helping you</strong> &mdash; another
          student who is certified on that machine.</p>
      </article>
      <article>
        <span class="lv">Level three</span>
        <b>Advanced</b>
        <p>You can print <strong>on your own</strong>. Still with an approved job, but
          nobody has to be standing there.</p>
      </article>
    </div>
  </section>

  <section>
    <h2>The machine order</h2>
    <p class="sub">You work through the printers in sequence, smallest and simplest first.
      Think of it as unlocking the next level of complexity and size.</p>
    <div class="seq">
      <div class="m">
        <span class="n">Level 1</span>
        <b>A1 Mini</b>
        <span class="d">Where everyone starts.</span>
      </div>
      <div class="m">
        <span class="n">Level 2</span>
        <b>X1C</b>
        <span class="d">Bigger, faster, enclosed.</span>
      </div>
      <div class="m">
        <span class="n">Level 3</span>
        <b>H2D</b>
        <span class="d">The largest machine in the room.</span>
      </div>
    </div>
    <p class="note">You cannot skip a machine. The X1C is not open to you until you have
      certified on the A1 Mini, and the H2D is not open until the X1C.</p>
  </section>

  <section>
    <h2>How the two combine</h2>
    <p>Once you complete a level on a machine, you have two ways to go next: <strong>up a
      level on the same machine</strong>, or <strong>the same level on the next
      machine</strong>. Your choice.</p>
    <p class="eg"><b>For example:</b> after Beginner on the A1 Mini you may go on to
      Intermediate on the A1 Mini, or start Beginner on the X1C. Whichever is more useful
      for the project in front of you.</p>
    <p>Most students go up on the A1 Mini first, because printing unsupervised on a
      machine you know well is worth more day to day than supervised access to a bigger
      one. But if your project needs the build volume, take the other route.</p>
  </section>

  <section>
    <h2>How you get certified</h2>
    <p>Training is the free courses at the
      <a href="https://bambulab.com/en/support/academy">Bambu Lab Academy</a>, run by the
      company that makes our printers. Work through the course for the machine you want,
      then show Mr. Frank what you completed.</p>
    <p>Bambu Lab issues a printable Certificate of Completion for each course, so you have
      something to keep as well as the shop access it unlocks.</p>
    <ul class="ticks">
      <li>Do the course for the specific machine &mdash; the A1 Mini course does not
        certify you on the X1C.</li>
      <li>Bring your completion evidence to Mr. Frank. He records the level.</li>
      <li>Your current level is tracked by your instructor, not on this site.</li>
    </ul>
  </section>

  <section>
    <h2>Where your status is kept</h2>
    <p>Ask Mr. Frank &mdash; he keeps the class record. It is not published here, and it
      never will be. <strong>Nothing on this site is about any individual student</strong>:
      no names, no progress, no grades. This page is the rule; your record stays where
      student records belong.</p>
  </section>

  <section>
    <h2>Also worth knowing</h2>
    <div class="grid">
      <article>
        <b><a href="../pathways/mechanical.html">Designing for print</a></b>
        <p>Parts that have to move need clearance built in &mdash; around 0.3&nbsp;mm
          between surfaces that touch. Get it wrong in CAD and the print fuses solid.</p>
      </article>
      <article>
        <b><a href="../start/welcome.html">Makerspace rules</a></b>
        <p>Eye protection is required in the Makerspace, and open-toed shoes are not
          allowed in there at all.</p>
      </article>
    </div>
  </section>

</div>
'''


def build_printing():
    write('shop/3d-printing.html',
          shell('3D Printer Certification', PRINTING, depth=1, section='shop',
                path='shop/3d-printing.html',
                page_css=PRINT_CSS,
                desc='The shop 3D printer certification ladder: three access levels '
                     'across the A1 Mini, X1C and H2D, and how to earn them.'))


def build_safety():
    write('shop/index.html',
          shell('Safety', SAFE.HUB_BODY, depth=1, section='shop',
                path='shop/index.html',
                page_css=HOME_CSS + SAFE.CSS,
                desc='Shop safety at BHR Engineering: the Makerspace rules, machine '
                     'certification, and the safety data sheets.'))
    write('shop/makerspace.html',
          shell('Makerspace Rules', SAFE.makerspace_body(), depth=1, section='shop',
                path='shop/makerspace.html',
                page_css=SAFE.CSS,
                desc='The thirty-two Makerspace rules, plus a self-check you must get '
                     'entirely right.'))
    write('shop/technology.html',
          shell('Technology Use', SAFE.tech_body(), depth=1, section='shop',
                path='shop/technology.html',
                page_css=SAFE.CSS,
                desc='Safe and appropriate technology use: scanning, cameras, AI, '
                     'licences and accounts.'))
    write('shop/equipment.html',
          shell('Equipment Checks', SAFE.equipment_index(), depth=1, section='shop',
                path='shop/equipment.html',
                page_css=SAFE.EQ_CSS,
                desc='A safety check for every machine and tool group in the shop.'))
    for _k, (_n, _b, _q) in SAFE.EQ.QUIZZES.items():
        write('shop/check-%s.html' % _k,
              shell(_n, SAFE.check_body(_k), depth=1, section='shop',
                    path='shop/check-%s.html' % _k,
                    page_css=SAFE.EQ_CSS,
                    desc='Shop safety check: %s. %s' % (_n, _b.replace('&mdash;', '-'))))
    write('shop/themes.html',
          shell('Which Theme?', SAFE.themes_body(), depth=1, section='shop',
                path='shop/themes.html',
                page_css=SAFE.CSS,
                desc='Practice for the shop safety test: sort ten rules into the five '
                     'themes from the Makerspace rules.'))
    write('shop/sds.html',
          shell('Safety Data Sheets', SAFE.sds_body(), depth=1, section='shop',
                path='shop/sds.html',
                page_css=SAFE.CSS,
                desc='The shop safety data sheet library, and how to read a sheet when '
                     'you need one.'))


# ---------------------------------------------------------------- go

if __name__ == '__main__':
    assets = os.path.join(OUT, 'assets')
    stash = None
    if os.path.isdir(assets):
        stash = os.path.join(SRC, '.assets-stash')
        if os.path.isdir(stash):
            shutil.rmtree(stash)
        shutil.copytree(assets, stash)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(assets, exist_ok=True)
    if stash:
        for f in sorted(os.listdir(stash)):
            shutil.copy2(os.path.join(stash, f), os.path.join(assets, f))
            print('  %-42s %6d' % ('assets/' + f, os.path.getsize(os.path.join(assets, f))))
        shutil.rmtree(stash)

    # stamp the chosen font stack into the stylesheet
    css_path = os.path.join(OUT, 'assets', 'site.css')
    c = open(css_path, encoding='utf-8').read()
    f = FONTS[FONT]
    c = re.sub(r'--serif:[^;]+;', '--serif:%s;' % f['serif'], c)
    c = re.sub(r'--sans:[^;]+;', '--sans:%s;' % f['sans'], c)
    c = re.sub(r'--mono:[^;]+;', '--mono:%s;' % f['mono'], c)
    c = re.sub(r'--w-heavy:[^;]+;', '--w-heavy:%s;' % f['heavy'], c)
    # the search styles live in search_ui.py; the stylesheet only reserves a slot
    c = re.sub(r'/\* @@SEARCH@@ \*/.*?(?=/\* --- site chrome)',
               '/* @@SEARCH@@ */\n' + SUI.CSS.strip() + '\n'
               + SNAV.CSS.strip() + '\n' + THEME.CSS.strip() + '\n'
               + QBAR.CSS.strip() + '\n\n', c, flags=re.S)
    # every stamp must actually land; a silent no-op here is how the stylesheet
    # and the modules drift apart without anyone noticing
    for token in ('--serif:', '--sans:', '--mono:', '--w-heavy:', '--barh:'):
        if token not in c:
            raise SystemExit('build: %s missing from site.css' % token)
    if '.srch{' not in c or '.railin{' not in c or '.themebtn{' not in c \
            or '.qbar{' not in c:
        raise SystemExit('build: search, rail, theme or quick-bar CSS did not '
                         'get stamped in')
    open(css_path, 'w', encoding='utf-8').write(c)
    print('  fonts: %s' % f['name'])

    rows, n = SEARCH.emit(os.path.join(OUT, 'assets', 'search-index.js'))
    print('  %-42s %6d  (%d entries)' % ('assets/search-index.js', n, len(rows)))

    import hashlib, datetime
    # Stamped in SCHOOL time, not the build machine's. The builder runs UTC,
    # four hours ahead of Massachusetts, so a UTC stamp reads as a different
    # time from the one Windows shows for the same file -- which makes a build
    # that just landed look hours old.
    try:
        from zoneinfo import ZoneInfo
        _now = datetime.datetime.now(ZoneInfo('America/New_York'))
        BUILD = _now.strftime('%d %b %Y, %-I:%M %p').replace('AM', 'am') \
                    .replace('PM', 'pm')
    except Exception:
        BUILD = datetime.datetime.now().strftime('%d %b %Y, %H:%M UTC')
    globals()['BUILD'] = BUILD
    for _f in ('site.css', 'search-index.js'):
        _p = os.path.join(OUT, 'assets', _f)
        ASSET_V[_f] = hashlib.sha1(open(_p, 'rb').read()).hexdigest()[:8]
    print('  cache tags: %s' % ', '.join('%s=%s' % kv for kv in sorted(ASSET_V.items())))

    build_home()
    build_grades()
    build_extras()
    build_404()
    build_welcome()
    build_ported()
    build_pathways()
    build_printing()
    build_safety()
    build_resources()
    build_repo_files()

    # Ship the build scripts inside the site, so the repository carries what
    # made it. Automated rather than copied by hand -- a _source folder that
    # silently goes stale is worse than none at all.
    src_out = os.path.join(OUT, '_source')
    os.makedirs(src_out, exist_ok=True)
    for f in sorted(os.listdir(SRC)):
        if f.endswith('.py') and not f.startswith(('make_', 'test_')):
            shutil.copy2(os.path.join(SRC, f), os.path.join(src_out, f))
    print('  %-42s %6d files' % ('_source/', len(os.listdir(src_out))))

    print('\ndone ->', OUT)
