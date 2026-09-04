#!/usr/bin/env python3
"""Renders the training-and-credentials directory, plus the per-pathway
'Where to train' block that gets injected into each pathway page."""

import resources_data as RD
import build_hubs as B

CSS = '''
.filters{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 20px}
.filters button{font-family:var(--sans);font-size:13px;font-weight:500;
  background:var(--card);color:var(--ink-2);border:1px solid var(--rule);
  padding:6px 13px;border-radius:20px;cursor:pointer;line-height:1.3}
.filters button:hover{border-color:var(--accent);color:var(--accent)}
.filters button.on{background:var(--accent);border-color:var(--accent);color:#fff}

.rlist{display:flex;flex-direction:column;gap:1px;background:var(--rule);
  border:1px solid var(--rule)}
.r{background:var(--card);padding:17px 20px;display:flex;flex-direction:column;gap:8px}
.r.hide{display:none}
.rhead{display:flex;flex-wrap:wrap;align-items:baseline;gap:9px}
.r h3{margin:0;font-size:17px}
.r h3 a{text-decoration:none}
.r h3 a:hover{text-decoration:underline}
.pill{font-family:var(--mono);font-size:9.5px;letter-spacing:.11em;text-transform:uppercase;
  padding:3px 8px;border-radius:3px;white-space:nowrap}
.pill.ok{color:var(--green);background:var(--green-soft)}
.pill.deep{color:var(--blue);background:var(--blue-soft)}
.pill.hard{color:var(--ink-2);background:transparent;box-shadow:inset 0 0 0 1px var(--rule)}
.pill.warn{color:var(--warm);background:var(--warm-soft)}
.pill.school{color:var(--accent);background:var(--accent-soft)}
.rcost{font-size:13.5px;color:var(--ink-3);font-family:var(--sans)}
.r p{margin:0;font-size:15.5px;color:var(--ink-2);line-height:1.55;max-width:70ch}
.r .meta{display:flex;flex-wrap:wrap;gap:5px 18px;font-size:13.5px;color:var(--ink-3);
  font-family:var(--sans)}
.r .meta b{font-weight:600;color:var(--ink-2)}
.r .why{font-size:15px;color:var(--ink);background:var(--paper);border-left:2px solid var(--accent);
  padding:8px 13px;line-height:1.5;max-width:70ch}
.tags{display:flex;flex-wrap:wrap;gap:4px}
.tags i{font-style:normal;font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--ink-3);border:1px solid var(--rule);
  padding:2px 6px;border-radius:2px}

.creds{display:flex;flex-direction:column;gap:1px;background:var(--rule);
  border:1px solid var(--rule)}
.creds div{background:var(--card);padding:16px 20px;display:grid;
  grid-template-columns:minmax(0,210px) minmax(0,1fr);gap:6px 24px;align-items:start}
.creds b{font-family:var(--sans);font-weight:600;font-size:15.5px;line-height:1.35}
.creds .who{font-size:13.5px;color:var(--ink-3);font-family:var(--sans);display:block;
  margin-top:2px}
.creds .cost{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--accent);display:block;margin-top:5px}
.creds p{margin:0;font-size:15.5px;color:var(--ink-2);line-height:1.55}
.creds .cnote{margin-top:7px;font-size:14.5px;color:var(--warm)}
@media(max-width:620px){.creds div{grid-template-columns:1fr}}

.trainbox{display:flex;flex-direction:column;gap:1px;background:var(--rule);
  border:1px solid var(--rule)}
.trainbox a{background:var(--card);padding:13px 18px;text-decoration:none;color:inherit;
  display:grid;grid-template-columns:minmax(0,190px) minmax(0,1fr) auto;gap:4px 18px;
  align-items:baseline}
.trainbox a:hover{background:var(--accent-soft)}
.trainbox b{font-family:var(--sans);font-weight:600;font-size:15px}
.trainbox span{font-size:14.5px;color:var(--ink-2);line-height:1.5}
@media(max-width:620px){.trainbox a{grid-template-columns:1fr}}
'''

PATH_LABEL = {p['key']: p['nav'].replace('&amp;', '&') for p in B.P}


def _pill(cost):
    label, cls = RD.COST_LABEL[cost]
    return '<span class="pill %s">%s</span>' % (cls, label)


def entry(r):
    tags = ''.join('<i>%s</i>' % PATH_LABEL[k] for k in r['paths']) \
        if len(r['paths']) < len(RD.ALL) else '<i>Every pathway</i>'
    meta = []
    if r.get('cred'):
        meta.append('<span><b>Credential:</b> %s</span>' % r['cred'])
    if r.get('age'):
        meta.append('<span><b>Sign-up:</b> %s</span>' % r['age'])
    return '''  <article class="r" data-p="%(dp)s">
    <div class="rhead">
      <h3><a href="%(url)s" target="_blank" rel="noopener">%(name)s</a></h3>
      %(pill)s
      <span class="rcost">%(cost_note)s</span>
    </div>
    <p>%(what)s</p>
    %(why)s
    %(meta)s
    <div class="tags">%(tags)s</div>
  </article>''' % dict(
        dp=' '.join(r['paths']), url=r['url'], name=r['name'], pill=_pill(r['cost']),
        cost_note=r.get('cost_note', ''), what=r['what'],
        why='<p class="why">%s</p>' % r['note'] if r.get('note') else '',
        meta='<div class="meta">%s</div>' % ''.join(meta) if meta else '',
        tags=tags)


def cred_row(c):
    link = ('<b><a href="%s" target="_blank" rel="noopener">%s</a></b>'
            % (c['url'], c['name'])) if c['url'] else '<b>%s</b>' % c['name']
    return '''  <div>
    <div>%(link)s<span class="who">%(who)s</span><span class="cost">%(cost)s</span></div>
    <div><p>%(what)s</p>%(note)s</div>
  </div>''' % dict(link=link, who=c['who'], cost=c['cost'], what=c['what'],
                   note='<p class="cnote">%s</p>' % c['note'] if c.get('note') else '')


def page_body():
    filters = ['<button class="on" data-f="all">Everything</button>']
    filters += ['<button data-f="%s">%s</button>' % (p['key'], p['nav'])
                for p in B.P]
    return '''
<div class="wrap">

  <header class="hero">
    <p class="kicker">Training &amp; Credentials</p>
    <h1>Where to learn it, and what you can earn</h1>
    <p>Every platform the shop uses or recommends. All of it is either free or already
      paid for by the shop &mdash; none of it costs you anything. Filter by pathway, or
      read the lot.</p>
  </header>

  <section>
    <h2>Read the labels</h2>
    <p class="sub">Plenty of things online are advertised as free and are not. These
      labels mean exactly what they say, and none of them means you pay.</p>
    <dl class="defs">
      <dt><span class="pill ok">Free</span></dt>
      <dd>Costs nothing, including any badge or certificate it awards. No card, no trial
        that turns into a bill.</dd>
      <dt><span class="pill warn">Free, with limits</span></dt>
      <dd>You can use it without paying, but there is a cap you will hit. The cap is
        stated. Do not pay for anything yourself before asking.</dd>
      <dt><span class="pill school">School provides</span></dt>
      <dd>The shop already pays for this. Ask Mr. Frank for access rather than signing
        up yourself &mdash; there is nothing for you to buy.</dd>
    </dl>
    <p class="note warn"><strong>You should never need to pay for anything on this
      page.</strong> Everything here is either free or already covered by the shop. If a
      site starts asking you for card details, stop and ask Mr. Frank &mdash; there is
      almost always a free school route that is not obvious from the website.</p>
  </section>

  <section>
    <h2>The platforms</h2>
    <p class="sub">%(n)d of them. Filter to your pathway if the full list is too much.</p>
    <div class="filters">
      %(filters)s
    </div>
    <div class="rlist" id="rlist">
%(entries)s
    </div>
  </section>

  <section>
    <h2>Credentials you can actually earn here</h2>
    <p class="sub">The difference between training and a credential is that someone else
      vouches for the second one.</p>
    <div class="creds">
%(creds)s
    </div>
    <p class="note">Some pathways have excellent free training but no widely respected
      free credential &mdash; Mechanical, Electrical and Architecture are the honest
      examples. That is a fact about the industry rather than a gap in the programme. In
      those pathways the Autodesk certification is the one to go for, and the school
      covers it.</p>
  </section>

  <section>
    <h2>A word on AI tools</h2>
    <p class="sub">Worth being straight with you about this.</p>
    <p>Most of the well-known AI assistants, Claude included, require you to be
      <strong>18 or older</strong> to hold an account. That is their rule, not the
      school&rsquo;s, and it applies at home as much as here. If you are under 18, do not
      sign up for one and do not use a family member&rsquo;s account to get around it.</p>
    <p>There is good AI <em>learning</em> that is open to you now &mdash; IBM
      SkillsBuild&rsquo;s AI Literacy credential is free, built for ages 13 to 18, and
      gives you a badge at the end. Start there. Ask Mr. Frank before using any AI tool
      for schoolwork, in this shop or any other class.</p>
  </section>

</div>

<script>
(function(){
  var btns=document.querySelectorAll('.filters button');
  var items=document.querySelectorAll('#rlist .r');
  btns.forEach(function(b){
    b.addEventListener('click',function(){
      btns.forEach(function(x){x.classList.remove('on');});
      b.classList.add('on');
      var f=b.dataset.f;
      items.forEach(function(it){
        var show = f==='all' || it.dataset.p.split(' ').indexOf(f)!==-1;
        it.classList.toggle('hide', !show);
      });
    });
  });
})();
</script>
''' % dict(n=len(RD.R), filters='\n      '.join(filters),
           entries='\n'.join(entry(r) for r in RD.R),
           creds='\n'.join(cred_row(c) for c in RD.CREDS))


def train_block(path_key):
    """The 'Where to train' block injected into one pathway page."""
    rows = [r for r in RD.R if path_key in r['paths']]
    # everything-pathway entries go last; pathway-specific first
    rows.sort(key=lambda r: (len(r['paths']) == len(RD.ALL), r['name']))
    if not rows:
        return ''
    links = '\n'.join(
        '  <a href="../resources/index.html"><b>%s</b><span>%s</span>%s</a>'
        % (r['name'], r['what'].split('.')[0] + '.', _pill(r['cost']))
        for r in rows)
    return '''<div class="topic">
<div class="th"><span class="tn">&mdash;</span><div><h3>Where to train</h3>
<p class="tq">Platforms that serve this pathway. Full details, costs and sign-up notes on
the <a href="../resources/index.html">Training &amp; Credentials</a> page.</p></div></div>
<div class="trainbox">
%s
</div>
</div>''' % links


# ---------------------------------------------------------------- pathway sources

import pathway_sources as PS  # noqa: E402

SRC_CSS = '''
.srcs{display:flex;flex-direction:column;gap:1px;background:var(--card);
  border:1px solid var(--rule);margin-top:14px}
.srcs a{background:var(--card);box-shadow:0 0 0 1px var(--rule);padding:14px 18px;
  text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:5px}
.srcs a:hover{background:var(--accent-soft)}
.srcs .top{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px}
.srcs b{font-family:var(--sans);font-weight:600;font-size:15.5px;line-height:1.3}
.srcs .kind{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-3)}
.srcs p{margin:0;font-size:14.5px;color:var(--ink-2);line-height:1.5;max-width:70ch}
.srchead{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px;margin-top:20px}
.srchead h4{margin:0;font-family:var(--sans);font-weight:700;font-size:14px;
  letter-spacing:.04em;text-transform:uppercase;color:var(--accent)}
.srchead span{font-size:13.5px;color:var(--ink-3)}
'''


def sources_block(path_key, topic_key):
    rows = PS.by(path_key, topic_key)
    if not rows:
        return ''
    order = {'start': 0, 'deeper': 1, 'college': 2}
    rows = sorted(rows, key=lambda r: order.get(r['level'], 3))
    out = ['<div class="srchead"><h4>Go and look</h4>'
           '<span>%d checked links &mdash; every one opens, free.</span></div>'
           % len(rows), '<div class="srcs">']
    for r in rows:
        label, cls = PS.LEVELS[r['level']]
        out.append(
            '  <a href="%s" target="_blank" rel="noopener">'
            '<span class="top"><b>%s</b><span class="pill %s">%s</span>'
            '<span class="kind">%s</span></span>%s</a>'
            % (r['url'], r['title'], cls, label, r['kind'],
               '<p>%s</p>' % r['note'] if r['note'] else ''))
    out.append('</div>')
    return '\n'.join(out)
