# -*- coding: utf-8 -*-
"""The Families page: for parents, guardians and students choosing a shop.

Everything on the rest of this site is addressed to a student who is already
in the program. This page is the one exception -- it is written for somebody
standing outside it deciding, and for the adult standing next to them.

It also holds the material that used to sit at the bottom of the printed
open-house handout: what to ask, what to look at. That belongs here rather
than on paper, because it changes and paper does not.
"""

CSS = '''
.fam .hero{background:var(--accent);border-radius:9px;padding:30px 32px 32px;
  margin:0 0 22px}
.fam .hero .eyebrow{font-family:var(--mono);font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:rgba(255,255,255,.72);margin:0 0 8px}
.fam .hero h1{font-family:var(--sans);font-weight:var(--w-heavy);
  font-size:clamp(27px,4.6vw,40px);line-height:1.04;letter-spacing:-.022em;
  color:#fff;margin:0}
.fam .hero p.t{font-size:17px;line-height:1.5;color:rgba(255,255,255,.9);
  margin:12px 0 0;max-width:56ch}

.fam .qa{border:1px solid var(--rule);border-radius:8px;background:var(--card);
  overflow:hidden;margin:0 0 18px}
.fam .qa details{border-top:1px solid var(--rule-soft)}
.fam .qa details:first-child{border-top:0}
.fam .qa summary{cursor:pointer;list-style:none;padding:15px 20px;
  font-family:var(--sans);font-weight:700;font-size:16.5px;color:var(--ink);
  display:flex;align-items:center;gap:12px}
.fam .qa summary::-webkit-details-marker{display:none}
.fam .qa summary::after{content:"";margin-left:auto;flex:none;width:7px;
  height:7px;border-right:2px solid var(--accent);
  border-bottom:2px solid var(--accent);transform:rotate(45deg);
  transition:transform .14s}
.fam .qa details[open] summary::after{transform:rotate(-135deg)}
.fam .qa summary:hover{background:var(--accent-soft)}
.fam .qa .a{padding:0 20px 17px}
.fam .qa .a p{margin:0 0 10px;font-size:15.5px;line-height:1.62;
  color:var(--ink-2)}
.fam .qa .a p:last-child{margin:0}
.fam .qa .a b{color:var(--ink)}

.fam .ask{border:1px solid var(--rule);border-left:4px solid var(--accent);
  border-radius:0 8px 8px 0;background:var(--accent-soft);padding:20px 24px;
  margin:0 0 18px}
.fam .ask h3{margin:0 0 4px;font-size:18px}
.fam .ask ul{margin:12px 0 0;padding-left:20px}
.fam .ask li{margin:0 0 9px;font-size:15.5px;line-height:1.55;color:var(--ink)}
.fam .ask li:last-child{margin:0}
.fam .ask .why{font-size:14px;color:var(--ink-2);display:block;margin-top:3px}

.fam .dl{display:flex;align-items:center;gap:16px;flex-wrap:wrap;
  border:1px solid var(--rule);border-radius:8px;background:var(--card);
  padding:18px 22px;margin:0 0 18px}
.fam .dl b{font-family:var(--sans);font-size:16.5px;color:var(--ink)}
.fam .dl span{font-size:14.5px;color:var(--ink-2);line-height:1.5}
.fam .dl a{margin-left:auto;flex:none;font-family:var(--mono);font-size:11px;
  letter-spacing:.1em;text-transform:uppercase;font-weight:700;
  text-decoration:none;color:#fff;background:var(--accent);
  border-radius:5px;padding:10px 16px}
.fam .dl a:hover{background:var(--ink)}
'''

QA = [
    ('Is this a college track or a career track?',
     ['Both, and we do not make students pick early. Most students who leave '
      'this shop go on to college, and they go with four years of CAD, '
      'documentation and project work already behind them. Others decide on '
      'a more direct route into the field.',
      'The program is built so that both stay open. We would rather a '
      'student arrive at that decision having tried several kinds of '
      'engineering than having been told which one to want.']),
    ('What would my child actually be doing?',
     ['Designing something in professional CAD software, then making it '
      '&mdash; printed, cut, machined or wired &mdash; and then measuring it '
      'against what it was meant to do.',
      'That last step is what makes it engineering rather than art class. '
      '<b>Every project ends with data</b>, and the data is what points to '
      'the next change. Analyse, adjust, improve, measure again. Getting '
      'comfortable with that loop is the skill we are actually teaching.']),
    ('How is it graded?',
     ['Four categories: the project itself (35%), a weekly grade for how '
      'they work (30%), classwork (15%), and employability (20%).',
      '<b>Half the grade is how they work, not what they make.</b> Safety, '
      'initiative, preparation, attitude, teamwork and professionalism '
      'together outweigh the projects. A student can build something '
      'impressive and still not do well here, and can have a project come '
      'out nothing like they planned and still have a strong term. That is '
      'deliberate &mdash; '
      'it is how they would be judged in a real shop. Both rubrics are on '
      'the Documents page, level by level.']),
    ('Is it safe?',
     ['This is a room with a laser cutter, a CNC machine, power tools, '
      'heated printers and a collaborative robot in it, so the honest answer '
      'is that it is safe <em>because</em> the rules are strict.',
      'Nothing gets switched on by a student who has not been trained and '
      'authorised on that specific machine. Eye protection is required in '
      'the Makerspace. Closed-toe shoes always. Nobody uses power tools '
      'alone. Every injury is reported, however small. And every Grade 10 '
      'student earns an <b>OSHA 10 card</b>, whichever shop they are in.']),
    ('How does choosing a shop work?',
     ['Grade 9 students get more than a glance. Two mini exploratory days, '
      'one in each of the first two terms, show them all eighteen shops in '
      'the school. From each of those days they pick four or five to spend a '
      'full week in &mdash; nine week-long visits in all. Then they choose, '
      'and join their shop for Terms 3 and 4.',
      'If your child spends their week with us they are not sitting at the '
      'back watching. They are in the room with upperclassmen, '
      'working.']),
    ('What does a week look like?',
     ['One week in the shop &mdash; all five days, all day &mdash; then one '
      'week in academics with no shop at all. A term works out at about '
      'twenty-five full shop days.',
      'The week away is why we are strict about the logbook. Whatever a '
      'student is halfway through goes cold for a week, and their notes are '
      'the difference between a fast restart and losing a morning.']),
    ('Does my child need to be &ldquo;good at math&rdquo; already?',
     ['No. They need to be curious about why a result came out the way it '
      'did, which is a different quality and is not always found in the same '
      'students.',
      'The maths and science that this work needs get taught alongside the '
      'projects that need them, at the point where the student can see what '
      'they are for.']),
    ('What does it cost us?',
     ['Students wear shop attire carrying the Engineering Technology logo, '
      'ordered through the school store during the ordering window. Most buy '
      'a couple of items. Closed-toe shoes they will already own.',
      'Everything else &mdash; software, materials, machine time, the '
      'certifications &mdash; is provided by the program.']),
]

ASK = [
    ('What is a student in here actually doing at 9am on a Tuesday?',
     'The answer to this tells you more than any brochure.'),
    ('What happens when a design does not perform the way a student '
     'expected?',
     'How a shop answers this is how it treats your child on a hard day.'),
    ('What do the students who are not sure what they want get out of this?',
     'Most eighth graders are in exactly that position.'),
    ('Can I see something a student built, and the notes behind it?',
     'The logbook is more revealing than the object.'),
]


def page(depth=1):
    r = '../' * depth
    o = ['<div class="wrap fam">',
         '<div class="hero">',
         '  <p class="eyebrow">For parents, guardians and eighth graders</p>',
         '  <h1>Thinking about Engineering Technology?</h1>',
         '  <p class="t">What the shop is, what your child would actually do '
         'in it, and the questions worth asking before you decide.</p>',
         '</div>']

    o.append('<div class="dl"><div><b>Take the handout</b><br>'
             '<span>Three pages covering all of this, printable, for the '
             'fridge or the guidance meeting.</span></div>'
             '<a href="%sfiles/BHR27-Welcome-Families.pdf" download>'
             'Download PDF</a></div>' % r)

    o.append('<section><h2>The questions we get asked most</h2>')
    o.append('<div class="qa">')
    for i, (q, ans) in enumerate(QA):
        o.append('  <details%s><summary>%s</summary><div class="a">%s</div>'
                 '</details>'
                 % (' open' if i == 0 else '', q,
                    ''.join('<p>%s</p>' % a for a in ans)))
    o.append('</div></section>')

    o.append('<section><h2>If you are visiting the shop</h2>')
    o.append('<div class="ask"><h3>Four questions worth asking</h3>'
             '<p>Ask us, and ask the students &mdash; they are the better '
             'source.</p><ul>')
    for q, why in ASK:
        o.append('  <li>&ldquo;%s&rdquo;<span class="why">%s</span></li>'
                 % (q, why))
    o.append('</ul></div>')
    o.append('<p>The most useful two minutes you can spend is asking a '
             'student in the room what they are building and why they chose '
             'it. They will tell you more than we can.</p>')
    o.append('</section>')

    o.append('<section><h2>Where to look next</h2>'
             '<div class="quicklinks">'
             '<a href="%sstart/engineering.html">What engineering actually is</a>'
             '<a href="%spathways/index.html">The seven pathways</a>'
             '<a href="%sgrades/index.html">What each year holds</a>'
             '<a href="%sstart/how-class-works.html">How the class works</a>'
             '<a href="%sshop/index.html">Shop safety</a>'
             '<a href="%sstaff/frank.html">Who teaches it</a>'
             '<a href="%slogbook/documents.html">The documents students use</a>'
             '</div></section>' % (r, r, r, r, r, r, r))

    o.append('</div>')
    return '\n'.join(o)
