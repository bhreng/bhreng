# -*- coding: utf-8 -*-
"""The site-wide navigation rail.

One sidebar on every page, listing the whole site, so any page is one click from
any other. The current section expands to show its pages, and the current page
expands to show its own sections -- so the rail is a map of the site AND a map of
where you are, without ever being a wall of two hundred links.

Rendered per page at build time. No JavaScript is needed to open the right
branch, which means it works with JS off and it cannot flash the wrong state.
"""

import build_hubs as B
import equipment_data as EQ

# (key, label, href, [(href, label), ...])
def tree():
    paths = [('pathways/%s.html' % p['key'], p['nav'], p['std']) for p in B.P]
    checks = [('shop/check-%s.html' % k, n)
              for k, (n, _b, _q) in EQ.QUIZZES.items()]
    return [
        ('home', 'Home', 'index.html', []),
        ('start', 'Start here', 'start/welcome.html', [
            ('start/welcome.html', 'Welcome to the shop'),
            ('start/how-class-works.html', 'How this class works'),
            ('start/engineering.html', 'What engineering is'),
        ]),
        ('grades', 'Your year', 'grades/index.html', [
            ('grades/index.html', 'Which year are you?'),
            ('grades/9.html', 'Grade 9 \u2014 Engineering I'),
            ('grades/10.html', 'Grade 10 \u2014 Engineering II'),
            ('grades/11.html', 'Grade 11 \u2014 Engineering III'),
            ('grades/12.html', 'Grade 12 \u2014 Engineering IV'),
        ]),
        ('staff', 'Your instructors', 'staff/frank.html', [
            ('staff/frank.html', 'Mr. Frank \u2014 EDF'),
            ('staff/dryer.html', 'Mr. Dryer \u2014 ESEC'),
        ]),
        ('logbook', 'Logbook', 'logbook/index.html', []),
        ('pathways', 'The seven pathways', 'pathways/index.html',
         [('pathways/index.html', 'Which one is for you?')] +
         [(h, n) for h, n, s in paths]),
        ('shop', 'Shop safety', 'shop/index.html', [
            ('shop/makerspace.html', 'Makerspace rules'),
            ('shop/equipment.html', 'Equipment checks'),
            ('shop/technology.html', 'Technology use'),
            ('shop/3d-printing.html', '3D printer certification'),
            ('shop/sds.html', 'Safety data sheets'),
            ('shop/themes.html', 'Which theme? (practice)'),
        ] + checks),
        ('resources', 'Training and credentials', 'resources/index.html', []),
        ('extras', 'More', 'extras/do-nows.html', [
            ('extras/do-nows.html', 'Do Nows and bonus work'),
            ('extras/links.html', 'Links'),
        ]),
    ]


# checks hang off the equipment page rather than sitting loose in the list
CHECK_PARENT = 'shop/equipment.html'

CSS = '''
/* --- the site rail ------------------------------------------------------ */
.shell{max-width:1280px;margin:0 auto;display:grid;
  grid-template-columns:232px minmax(0,1fr);gap:0}
.rail{border-right:1px solid var(--rule);font-family:var(--sans)}
.railin{position:sticky;top:var(--barh);padding:22px 14px 40px 24px;
  max-height:calc(100vh - var(--barh));overflow-y:auto}
.rail ul{list-style:none;margin:0;padding:0}
.rail>ul>li{margin-bottom:3px}
.rail a{display:block;text-decoration:none;color:var(--ink-2);
  font-size:14px;font-weight:500;padding:6px 10px;border-radius:3px;line-height:1.35}
.rail a:hover{background:var(--accent-soft);color:var(--ink)}
.rail>ul>li>a{font-weight:600;color:var(--ink)}
.rail>ul>li>a.sec{color:var(--ink)}
.rail a.here{background:var(--accent-soft);color:var(--accent);font-weight:700}
.rail .kids{margin:2px 0 10px;padding-left:10px;border-left:1px solid var(--rule)}
.rail .kids a{font-size:13.5px;font-weight:500;padding:5px 10px}
.rail .kids .kids{margin:1px 0 6px}
.rail .kids .kids a{font-size:13px;color:var(--ink-3)}
.rail .kids .kids a:hover{color:var(--ink-2)}
.rail .grp{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-3);margin:14px 0 5px;padding-left:10px}
.rail .anch a{font-family:var(--serif);font-size:13px}
.rail .anch a .n{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);
  margin-right:6px}
.rail a.on{color:var(--accent);font-weight:700}
.rail a.on .n{color:var(--accent)}
.main{min-width:0;padding:0 8px}
.main .wrap{max-width:820px;margin:0;padding-left:34px;padding-right:24px}
.main .wrap.wide{max-width:960px}

/* The toggle. Hidden on desktop, where the rail is simply always open.
   A checkbox rather than JavaScript, so the menu opens with scripting off and
   cannot flash open on load. */
.railtog{position:absolute;width:1px;height:1px;opacity:0;pointer-events:none}
.railbtn{display:none}

@media(max-width:940px){
  .shell{display:block;max-width:1040px}
  .rail{border-right:0;border-bottom:1px solid var(--rule)}
  .railin{position:static;max-height:none;overflow:visible;padding:0 24px 14px}
  .rail>.railin>nav>ul{display:grid;
    grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:0 14px}
  .rail .kids{margin-bottom:4px}
  .main .wrap,.main .wrap.wide{max-width:900px;margin:0 auto;padding-left:24px}

  /* Closed by default. Without this a phone gets a screen and a half of link
     list on top of every page before a word of the actual content. */
  .railin{display:none}
  .railtog:checked~.railin{display:block}
  .railbtn{display:flex;align-items:center;gap:10px;cursor:pointer;
    padding:11px 24px;font-size:14px;font-weight:600;color:var(--ink-2);
    user-select:none;-webkit-user-select:none}
  .railbtn:hover{color:var(--accent)}
  .railbtn .bars{position:relative;width:16px;height:2px;flex:none;
    background:currentColor;box-shadow:0 -5px 0 currentColor,0 5px 0 currentColor}
  .railbtn .chev{margin-left:auto;font-size:11px;transition:transform .15s}
  .railtog:checked~.railbtn .chev{transform:rotate(180deg)}
  .railtog:checked~.railbtn{color:var(--accent)}
  .railtog:focus-visible~.railbtn{outline:2px solid var(--accent);outline-offset:-2px}
}
@media(prefers-reduced-motion:reduce){.railbtn .chev{transition:none}}
@media print{.rail{display:none}.shell{display:block}
  .main .wrap{max-width:none;padding:0}}
'''


def _a(href, label, rel, current, extra=''):
    cls = ' class="here"' if href == current else (' class="%s"' % extra if extra else '')
    return '<a href="%s%s"%s>%s</a>' % (rel, href, cls, label)


def render(current, rel, anchors=None):
    """current: page path from the site root. anchors: [(id, label, num)]."""
    # NOT a <details>: Chrome's ::details-content establishes containment, which
    # silently breaks position:sticky for anything inside it.
    out = ['<div class="rail">',
           '  <input type="checkbox" id="railtog" class="railtog"'
           ' aria-label="Show site navigation">',
           '  <label for="railtog" class="railbtn"><span class="bars"></span>'
           'Browse the site<span class="chev">&#9660;</span></label>',
           '  <div class="railin">',
           '  <nav aria-label="Site"><ul>']
    for key, label, href, kids in tree():
        child_hrefs = {k for k, _ in kids}
        active = href == current or current in child_hrefs
        # if a child points at this same page, let the child carry "you are here"
        # rather than lighting up two rows for one page
        parent_current = current if current not in child_hrefs else ''
        out.append('    <li>' + _a(href, label, rel, parent_current, 'sec'))
        if active and kids:
            out.append('      <ul class="kids">')
            for khref, klabel in kids:
                if khref.startswith('shop/check-'):
                    continue
                out.append('        <li>' + _a(khref, klabel, rel, current))
                # the equipment checks live under their own page
                if khref == CHECK_PARENT and current.startswith('shop/check-'):
                    out.append('          <ul class="kids">')
                    for c, cl in kids:
                        if c.startswith('shop/check-'):
                            out.append('            <li>' + _a(c, cl, rel, current) + '</li>')
                    out.append('          </ul>')
                # in-page sections for the page you are actually on
                if khref == current and anchors:
                    out.append('          <ul class="kids anch">')
                    for aid, alabel, anum in anchors:
                        out.append('            <li><a href="#%s"><span class="n">%s</span>%s</a></li>'
                                   % (aid, anum, alabel))
                    out.append('          </ul>')
                out.append('        </li>')
            out.append('      </ul>')
        out.append('    </li>')
    out.append('  </ul></nav>')
    out.append('  </div>')
    out.append('</div>')
    return '\n'.join(out)


JS = '''
<script defer>
// Track which in-page section you are actually looking at and mark it in the
// rail. Only runs where the rail has anchor links.
(function(){
  function ready(fn){ document.readyState !== 'loading'
    ? fn() : document.addEventListener('DOMContentLoaded', fn); }
  ready(function(){
    var links = [].slice.call(document.querySelectorAll('.rail .anch a'));
    if (!links.length || !('IntersectionObserver' in window)) return;
    var map = {}, pos = {};
    links.forEach(function(a){ map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        pos[e.target.id] = e.isIntersecting ? e.boundingClientRect.top : null;
      });
      var best = null, near = Infinity;
      Object.keys(pos).forEach(function(id){
        if (pos[id] === null) return;
        var d = Math.abs(pos[id] - 90);
        if (d < near){ near = d; best = id; }
      });
      links.forEach(function(a){ a.classList.remove('on'); });
      if (best && map[best]) map[best].classList.add('on');
    }, {rootMargin:'-70px 0px -55% 0px', threshold:[0,1]});
    Object.keys(map).forEach(function(id){
      var el = document.getElementById(id); if (el) io.observe(el);
    });
  });
})();
</script>'''
