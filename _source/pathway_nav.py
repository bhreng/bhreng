# -*- coding: utf-8 -*-
"""The per-hub sidebar: what is actually in each section, in plain words.

The counts are generated from the source data rather than typed by hand, so a
sidebar can never drift out of step with the page it describes.
"""

from collections import Counter
import pathway_sources as PS

TOPICS = [
    ('field',  '1', 'Explore the Field',   'What the work is really like'),
    ('learn',  '2', 'Learn the Concepts',  'The ideas behind it'),
    ('skills', '3', 'Build Your Skills',   'Things to practise until you can do them'),
    ('build',  '4', 'Find a Project',      'Things you could actually go and build'),
    ('files',  '5', 'Get the Files',       'Tools and references to keep open'),
]

# how each source kind reads in a sentence
NOUN = {
    'video': ('video', 'videos'),
    'playlist': ('playlist', 'playlists'),
    'course': ('course', 'courses'),
    'talk': ('talk', 'talks'),
    'podcast': ('podcast', 'podcasts'),
    'doc': ('reference', 'references'),
    'read': ('article', 'articles'),
    'book': ('book', 'books'),
    'tool': ('tool', 'tools'),
    'software': ('program', 'programs'),
    'data': ('data set', 'data sets'),
    'comp': ('competition', 'competitions'),
    'site': ('site', 'sites'),
}

ORDER = ['video', 'playlist', 'course', 'talk', 'podcast', 'comp', 'tool',
         'software', 'data', 'doc', 'read', 'book', 'site']


def phrase(rows):
    """'8 videos and 2 courses' -- the two biggest kinds, then a remainder."""
    if not rows:
        return ''
    c = Counter(r.get('kind', 'site') for r in rows)
    parts, used = [], 0
    for k in sorted(c, key=lambda k: (-c[k], ORDER.index(k) if k in ORDER else 99)):
        if len(parts) == 2:
            break
        n = c[k]
        one, many = NOUN.get(k, (k, k + 's'))
        parts.append('%d %s' % (n, one if n == 1 else many))
        used += n
    rest = sum(c.values()) - used
    if rest:
        parts.append('%d more' % rest)
    if len(parts) == 1:
        return parts[0]
    return ', '.join(parts[:-1]) + ' and ' + parts[-1]


def build_phrase(rows):
    """Find a Project is about what you would DO, so the medium of the link is
    beside the point -- a video of a build is still a build. Count competitions
    separately, because entering one is a different decision."""
    comps = sum(1 for r in rows if r.get('kind') == 'comp')
    rest = len(rows) - comps
    bits = []
    if comps:
        bits.append('%d competition%s' % (comps, '' if comps == 1 else 's'))
    if rest:
        bits.append('%d project idea%s' % (rest, '' if rest == 1 else 's'))
    return ' and '.join(bits)


def items(key, has_training):
    out = []
    for tkey, num, name, plain in TOPICS:
        rows = PS.by(key, tkey)
        ph = build_phrase(rows) if tkey == 'build' else phrase(rows)
        out.append(dict(id='t' + num, num=num, name=name, plain=plain,
                        count=len(rows), phrase=ph))
        if tkey == 'skills' and has_training:
            out.append(dict(id='ttrain', num='&middot;', name='Where to train',
                            plain='Platforms that serve this pathway',
                            count=0, phrase=''))
    return out


CSS = '''
.pathlayout{display:grid;grid-template-columns:250px minmax(0,1fr);gap:40px;
  align-items:start}
.pside{position:sticky;top:74px;font-family:var(--sans)}
.pside .lbl{font-family:var(--mono);font-size:10px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--ink-3);margin:0 0 9px;padding-left:2px}
.pside ol{list-style:none;margin:0 0 16px;padding:0;
  border:1px solid var(--rule);background:var(--card)}
.pside li{border-bottom:1px solid var(--rule-soft)}
.pside li:last-child{border-bottom:0}
.pside a{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;
  padding:11px 13px;text-decoration:none;color:inherit;align-items:start}
.pside a:hover{background:var(--accent-soft)}
.pside .n{font-family:var(--mono);font-size:11px;color:var(--ink-3);
  padding-top:2px;min-width:9px}
.pside b{font-weight:600;font-size:14.5px;line-height:1.25;color:var(--ink);
  display:block}
.pside .pl{display:block;font-family:var(--serif);font-size:13px;color:var(--ink-2);
  line-height:1.4;margin-top:2px}
.pside .ct{display:block;font-family:var(--mono);font-size:10.5px;color:var(--ink-3);
  margin-top:4px}
.pside a.on{background:var(--accent-soft)}
.pside a.on .n,.pside a.on b{color:var(--accent)}
.pside a.on b{font-weight:700}
.pside .up{font-size:13px;color:var(--ink-2);text-decoration:none;
  display:inline-block;padding:2px}
.pside .up:hover{color:var(--accent)}
.topic{scroll-margin-top:78px}
@media(max-width:900px){
  .pathlayout{grid-template-columns:1fr;gap:26px}
  .pside{position:static}
  .pside ol{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
    gap:1px;background:var(--rule)}
  .pside li{border-bottom:0;background:var(--card)}
}
@media print{.pside{display:none}.pathlayout{display:block}}
'''

JS = '''
<script defer>
// Highlight whichever section is actually in view. Plain IntersectionObserver,
// picking the entry nearest the top of the viewport so it does not flicker
// between two visible sections.
(function(){
  function ready(fn){ document.readyState !== 'loading'
    ? fn() : document.addEventListener('DOMContentLoaded', fn); }
  ready(function(){
    var links = [].slice.call(document.querySelectorAll('.pside a[href^="#"]'));
    if (!links.length || !('IntersectionObserver' in window)) return;
    var map = {}, seen = {};
    links.forEach(function(a){ map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ seen[e.target.id] = e.isIntersecting ? e.boundingClientRect.top : null; });
      var best = null, bestTop = Infinity;
      Object.keys(seen).forEach(function(id){
        var t = seen[id];
        if (t === null) return;
        var d = Math.abs(t - 90);
        if (d < bestTop){ bestTop = d; best = id; }
      });
      links.forEach(function(a){ a.classList.remove('on'); });
      if (best && map[best]) map[best].classList.add('on');
    }, {rootMargin: '-80px 0px -55% 0px', threshold: [0, 1]});
    Object.keys(map).forEach(function(id){
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  });
})();
</script>'''


def render(key, has_training, std):
    li = []
    for it in items(key, has_training):
        ct = ('<span class="ct">%s</span>' % it['phrase']) if it['phrase'] else ''
        li.append(
            '        <li><a href="#%(id)s"><span class="n">%(num)s</span>'
            '<span><b>%(name)s</b>'
            '<span class="pl">%(plain)s</span>%(ct)s</span></a></li>'
            % dict(it, ct=ct))
    return ('''    <aside class="pside" aria-label="On this page">
      <p class="lbl">On this page</p>
      <ol>
%s
      </ol>
      <a class="up" href="index.html">&larr; All seven pathways</a>
    </aside>''' % '\n'.join(li))


# --------------------------------------------------------------- first moves

FIRST_CSS = '''
.firstmove{border:1px solid var(--rule);border-left:4px solid var(--brand);
  background:var(--card);padding:20px 24px 22px;margin:0 0 34px}
.firstmove h2{font-family:var(--sans);font-weight:700;font-size:19px;margin:0 0 4px;
  color:var(--ink);letter-spacing:-.01em;max-width:none;text-wrap:pretty}
.firstmove>p{margin:0 0 14px;color:var(--ink-2);font-size:15.5px;max-width:64ch}
.firstmove ol{list-style:none;counter-reset:fm;margin:0;padding:0;
  display:flex;flex-direction:column;gap:11px}
.firstmove li{counter-increment:fm;position:relative;padding-left:34px;
  font-size:15.5px;line-height:1.55;max-width:66ch}
.firstmove li::before{content:counter(fm);position:absolute;left:0;top:1px;
  width:22px;height:22px;display:grid;place-items:center;border-radius:50%;
  background:var(--accent-soft);color:var(--accent);
  font-family:var(--sans);font-weight:700;font-size:12px}
.firstmove .ask{margin:16px 0 0;font-size:14.5px;color:var(--ink-3);
  padding-top:13px;border-top:1px solid var(--rule-soft)}
'''

TEMPLATE = '''  <section class="firstmove">
    <h2>New to this pathway? Start here.</h2>
    <p>Nothing on this page is compulsory and there is no order you have to follow.
      If you want a way in, this is the one I would take.</p>
    <ol>
      <li>%s</li>
      <li>%s</li>
      <li>%s</li>
      <li>Write down what you did in your logbook, including what did not work.</li>
    </ol>
    <p class="ask">Stuck, or want to talk it through? Ask <strong>%s</strong>.</p>
  </section>'''


def first_move(p):
    """A concrete opening move, built from the pathway's own first source so it
    names a real thing rather than saying 'have a look around'."""
    field = PS.by(p['key'], 'field')
    learn = PS.by(p['key'], 'learn')
    skills = PS.by(p['key'], 'skills')
    starters = [r for r in field if r.get('level') == 'start'] or field
    first = starters[0] if starters else None

    if first:
        step1 = ('Open <a href="%s"><strong>%s</strong></a> from Explore the Field, '
                 'and ask yourself honestly whether that work appeals to you.'
                 % (first['url'], first['title']))
    else:
        step1 = ('Read Explore the Field and ask yourself honestly whether this work '
                 'appeals to you.')

    if learn:
        step2 = ('If it does, pick <strong>one</strong> thing from Learn the Concepts '
                 '&mdash; there are %d to choose from &mdash; and actually finish it.'
                 % len(learn))
    else:
        step2 = 'If it does, pick one thing from Learn the Concepts and finish it.'

    if skills:
        step3 = ('Then go to Build Your Skills and do something with your hands. '
                 '%d options, and you do not have to take them in order.' % len(skills))
    else:
        step3 = 'Then go to Build Your Skills and do something with your hands.'

    return TEMPLATE % (step1, step2, step3, p.get('lead', 'an instructor'))
