# -*- coding: utf-8 -*-
"""The "What engineering is" page, and the short version for exploratory."""

import engineering_data as ED

CSS = '''
/* --- what engineering is ------------------------------------------------ */
.wgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));
  gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:7px;
  overflow:hidden}
.wgrid article{background:var(--card);padding:19px 21px}
.wgrid b{display:block;font-family:var(--sans);font-weight:700;font-size:17px;
  line-height:1.28;color:var(--accent);letter-spacing:-.01em}
.wgrid p{margin:7px 0 0;font-size:15.5px;line-height:1.58;color:var(--ink-2)}

/* the eight steps */
.steps{counter-reset:st;border:1px solid var(--rule);border-radius:7px;
  overflow:hidden;background:var(--card)}
.steps .st{display:grid;grid-template-columns:52px minmax(0,1fr) minmax(0,.8fr);
  gap:0 18px;padding:17px 20px;border-bottom:1px solid var(--rule-soft);
  align-items:start}
.steps .st:last-child{border-bottom:0}
.steps .no{font-family:var(--mono);font-size:22px;font-weight:700;
  color:var(--accent);line-height:1.1}
.steps h3{margin:0;font-family:var(--sans);font-weight:700;font-size:17.5px;
  letter-spacing:-.01em;line-height:1.25}
.steps .wh{margin:6px 0 0;font-size:15px;line-height:1.55;color:var(--ink-2)}
.steps .out{font-size:14px;line-height:1.5;color:var(--ink-2);
  background:var(--accent-soft);border-radius:5px;padding:10px 13px}
.steps .out b{display:block;font-family:var(--mono);font-size:9px;
  letter-spacing:.13em;text-transform:uppercase;color:var(--accent);
  margin-bottom:4px}

/* the seven roles */
.roles{border:1px solid var(--rule);border-radius:7px;overflow:hidden;
  background:var(--card)}
.roles .rw{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);
  gap:4px 20px;padding:15px 20px;border-bottom:1px solid var(--rule-soft)}
.roles .rw:last-child{border-bottom:0}
.roles b{font-family:var(--sans);font-weight:700;font-size:16.5px;
  letter-spacing:-.01em;color:var(--ink)}
.roles .wd{grid-column:1;font-size:15px;line-height:1.5;color:var(--ink-2)}
.roles .dv{grid-column:2;grid-row:1 / span 2;font-size:14.5px;line-height:1.5;
  color:var(--ink-2);border-left:3px solid var(--accent);padding-left:14px}
.roles .dv em{display:block;font-family:var(--mono);font-size:9px;
  font-style:normal;letter-spacing:.13em;text-transform:uppercase;
  color:var(--ink-3);margin-bottom:4px}

@media(max-width:720px){
  .steps .st{grid-template-columns:40px minmax(0,1fr)}
  .steps .out{grid-column:1 / -1;margin-top:10px}
  .roles .rw{grid-template-columns:minmax(0,1fr)}
  .roles .dv{grid-column:1;grid-row:auto;margin-top:8px}
}
'''


def page(depth=1):
    r = '../' * depth
    o = ['<div class="wrap">',
         '<section class="hero">',
         '  <p class="eyebrow">Before anything else</p>',
         '  <h1>What engineering actually is</h1>',
         '  <p class="lede">And the design process this shop runs on. Every '
         'project brief here assumes you know both, so this is the page they '
         'assume.</p>',
         '</section>',
         '<section>',
         '  <h2>Six things worth knowing</h2>',
         '  <div class="wgrid">']
    for t, d in ED.WHAT:
        o.append('    <article><b>%s</b><p>%s</p></article>' % (t, d))
    o.append('  </div>')
    o.append('</section>')

    o.append('<section id="process">')
    o.append('  <h2>The engineering design process</h2>')
    o.append('  <p class="sub">Eight steps. When a brief says &ldquo;use the '
             'design process&rdquo;, this is the process it means &mdash; and '
             'the right-hand column is what each step has to leave behind.</p>')
    o.append('  <div class="steps">')
    for i, (name, what, out) in enumerate(ED.STEPS, 1):
        o.append('    <div class="st"><span class="no">%d</span>'
                 '<div><h3>%s</h3><p class="wh">%s</p></div>'
                 '<div class="out"><b>Leaves behind</b>%s</div></div>'
                 % (i, name, what, out))
    o.append('  </div>')
    o.append('  <div class="note acc"><p><strong>It is a loop, not a '
             'line.</strong> Step 7 sends you back to step 3, or 4, or 1. A '
             'project that went straight through once has almost certainly '
             'skipped step 6.</p></div>')
    o.append('</section>')

    o.append('<section id="roles">')
    o.append('  <h2>The seven roles of an engineer</h2>')
    o.append('  <p class="sub">One project can need all seven. Knowing which '
             'one you are being asked to be &mdash; and what that role owes '
             'the project &mdash; is most of knowing what to hand in.</p>')
    o.append('  <div class="roles">')
    for name, what, deliv in ED.ROLES:
        o.append('    <div class="rw"><b>%s</b><p class="wd">%s</p>'
                 '<div class="dv"><em>Produces</em>%s</div></div>'
                 % (name, what, deliv))
    o.append('  </div>')
    o.append('  <p class="note">The Grade 11 <b>Full Scope Project</b> runs '
             'three weeks with you taking a different role each week and '
             'producing exactly these deliverables. That is where this list '
             'stops being a list.</p>')
    o.append('</section>')

    o.append('<section id="managing">')
    o.append('  <h2>Managing a project is engineering too</h2>')
    o.append('  <p class="sub">Six documents. They are not paperwork around '
             'the work &mdash; each one is a decision that has to be made '
             'anyway, written down.</p>')
    o.append('  <dl class="defs">')
    for t, d in ED.MANAGEMENT:
        o.append('    <dt>%s</dt><dd>%s</dd>' % (t, d))
    o.append('  </dl>')
    o.append('</section>')

    o.append('<section><h2>Where to go next</h2><div class="doors">'
             '<a href="%spathways/index.html"><span class="n">The seven '
             'areas</span><b>Pick a pathway</b><span>Which kind of '
             'engineering suits you, and what you would spend the term '
             'on.</span></a>'
             '<a href="%sgrades/index.html"><span class="n">Your year</span>'
             '<b>Grade 9 to 12</b><span>The units each year covers and the '
             'projects that fill them.</span></a>'
             '<a href="%slogbook/index.html"><span class="n">Every day</span>'
             '<b>The logbook</b><span>The documentation half of the job, '
             'which is half the grade.</span></a>'
             '</div></section>' % (r, r, r))
    o.append('</div>')
    return '\n'.join(o)
