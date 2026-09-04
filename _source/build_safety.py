# -*- coding: utf-8 -*-
"""Renders the safety pages: hub, Makerspace rules, SDS index, and quizzes."""

import json
import safety_data as S

FOLDER = 'https://drive.google.com/drive/folders/'

CSS = '''
.rulegroup{border:1px solid var(--rule);background:var(--card);margin-bottom:1px}
.rulegroup .rh{padding:15px 20px 13px;border-bottom:1px solid var(--rule-soft);
  display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 14px}
.rulegroup .rh b{font-family:var(--sans);font-weight:700;font-size:18px;
  letter-spacing:-.015em}
.rulegroup .rh span{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--ink-3)}
.rulegroup ul{margin:0;padding:6px 0;list-style:none}
.rulegroup li{padding:8px 20px 8px 42px;position:relative;font-size:15.5px;
  line-height:1.5;color:var(--ink-2)}
.rulegroup li::before{content:"";position:absolute;left:22px;top:16px;width:6px;height:6px;
  border-radius:50%;background:var(--accent)}
ol.primary{list-style:none;counter-reset:pr;margin:0;padding:0;
  border:1px solid var(--rule);background:var(--card)}
ol.primary li{counter-increment:pr;position:relative;padding:14px 20px 14px 58px;
  border-bottom:1px solid var(--rule-soft);font-size:16px;line-height:1.5}
ol.primary li:last-child{border-bottom:0}
ol.primary li::before{content:counter(pr);position:absolute;left:20px;top:14px;
  width:26px;height:26px;display:grid;place-items:center;
  background:var(--accent);color:#fff;border-radius:50%;
  font-family:var(--sans);font-weight:700;font-size:13px}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) ol.primary li::before{color:#150f22}}
:root[data-theme="dark"] ol.primary li::before{color:#150f22}
ol.primary li.gate{background:var(--accent-soft)}
.gatedefs{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:1px;background:var(--rule);border:1px solid var(--rule);margin-top:14px}
.gatedefs div{background:var(--card);padding:16px 20px}
.gatedefs b{display:block;font-family:var(--sans);font-weight:700;font-size:17px;
  color:var(--accent);margin-bottom:4px}
.gatedefs span{font-size:15px;color:var(--ink-2);line-height:1.5}
.occ{display:flex;flex-wrap:wrap;gap:14px;align-items:baseline;margin-top:16px;
  border:1px solid var(--rule);border-left:3px solid var(--blue);
  background:var(--card);padding:15px 20px}
.occ b{font-family:var(--sans);font-weight:800;font-size:30px;color:var(--blue);
  line-height:1}
.occ span{font-size:15px;color:var(--ink-2);line-height:1.5;max-width:56ch}
.emerg{background:var(--warm-soft);border:1px solid var(--warm);
  border-left-width:4px;padding:16px 21px;font-size:16px;line-height:1.5}
.emerg b{font-family:var(--sans)}

.sdslist{display:grid;grid-template-columns:repeat(auto-fit,minmax(258px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.sdslist a{background:var(--card);box-shadow:0 0 0 1px var(--rule);padding:17px 20px;
  text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:6px}
.sdslist a:hover{background:var(--accent-soft)}
.sdslist b{font-family:var(--sans);font-weight:700;font-size:16.5px;color:var(--ink)}
.sdslist a:hover b{color:var(--accent)}
.sdslist span{font-size:14.5px;color:var(--ink-2);line-height:1.5}

/* --- quiz ------------------------------------------------------------- */
.quiz{border:1px solid var(--rule);background:var(--card);box-shadow:var(--shadow)}
.qbar{display:flex;gap:4px;padding:14px 20px;border-bottom:1px solid var(--rule-soft);
  align-items:center;flex-wrap:wrap}
.qbar .dot{width:9px;height:9px;border-radius:50%;background:var(--rule);flex:none}
.qbar .dot.done{background:var(--moss)}
.qbar .dot.now{background:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
.qbar .count{margin-left:auto;font-family:var(--mono);font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-3)}
.qbody{padding:22px 24px 24px}
.qtext{font-family:var(--sans);font-weight:700;font-size:20px;line-height:1.3;
  letter-spacing:-.02em;margin:0 0 18px;max-width:44ch}
.opts{display:flex;flex-direction:column;gap:9px}
.opt{display:block;width:100%;text-align:left;font:inherit;font-size:16px;line-height:1.45;
  background:var(--card);color:var(--ink);border:1.5px solid var(--rule);
  padding:13px 17px;cursor:pointer;transition:border-color .12s,background .12s}
.opt:hover:not(:disabled){border-color:var(--accent);background:var(--accent-soft)}
.opt:disabled{cursor:default}
.opt.wrong{border-color:var(--warm);background:var(--warm-soft);color:var(--ink-2);
  text-decoration:line-through;text-decoration-color:var(--warm)}
.opt.right{border-color:var(--moss);background:var(--moss-soft);font-weight:600}
.why{margin-top:14px;border-left:4px solid var(--warm);background:var(--warm-soft);
  padding:14px 18px;font-size:15.5px;line-height:1.55}
.why.good{border-left-color:var(--moss);background:var(--moss-soft)}
.why .lbl{display:block;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;
  text-transform:uppercase;margin-bottom:5px;color:var(--ink-3)}
.qnext{margin-top:16px;font-family:var(--sans);font-weight:600;font-size:15.5px;
  background:var(--accent);color:#fff;border:0;padding:12px 22px;cursor:pointer}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .qnext{color:#150f22}}
:root[data-theme="dark"] .qnext{color:#150f22}
.qnext:hover{filter:brightness(1.1)}
.done-card{padding:30px 26px;text-align:center;display:flex;flex-direction:column;
  gap:10px;align-items:center}
.done-card .tick{width:46px;height:46px;border-radius:50%;background:var(--moss);
  color:var(--paper);display:grid;place-items:center;font-size:25px;font-weight:700}
.done-card h3{font-family:var(--sans);font-weight:var(--w-heavy);font-size:24px;margin:4px 0 0;
  letter-spacing:-.02em}
.done-card p{color:var(--ink-2);max-width:46ch;margin:0}
.done-card .stamp{font-family:var(--mono);font-size:12.5px;color:var(--ink-3);
  border:1px dashed var(--rule);padding:9px 15px;margin-top:6px}
.whoami{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:center;
  margin-top:14px}
.whoami label{font-family:var(--sans);font-weight:600;font-size:14px;color:var(--ink-2)}
.whoami input{font:inherit;font-family:var(--sans);font-size:15px;padding:8px 12px;
  border:1.5px solid var(--rule);background:var(--card);color:var(--ink);
  border-radius:3px;width:230px;max-width:70vw}
.whoami input:focus{outline:2px solid var(--accent);outline-offset:1px;
  border-color:var(--accent)}
.slip{margin-top:16px;width:100%;max-width:500px;height:auto;
  border:1px solid var(--rule);box-shadow:var(--shadow);display:block;
  margin-left:auto;margin-right:auto}
.sliphint{margin:10px 0 0;font-size:13px;color:var(--ink-3);display:none}
@media(hover:none) and (pointer:coarse){.sliphint{display:block}}
.slipbtns{display:flex;gap:9px;flex-wrap:wrap;justify-content:center;margin-top:13px}
.slipbtns button{font-family:var(--sans);font-weight:600;font-size:14.5px;
  padding:10px 18px;border:1.5px solid var(--accent);background:var(--card);
  color:var(--accent);cursor:pointer;border-radius:3px}
.slipbtns button:hover{background:var(--accent-soft)}
.slipbtns button.solid{background:var(--accent);color:#fff;border-color:var(--accent)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .slipbtns button.solid{color:#150f22}}
:root[data-theme="dark"] .slipbtns button.solid{color:#150f22}
.slipnote{font-family:var(--sans);font-size:13px;color:var(--ink-3);margin-top:10px;
  max-width:44ch}
.qagain{background:none;border:0;color:var(--ink-3);font:inherit;font-size:14px;
  text-decoration:underline;cursor:pointer;padding:4px}
@media print{.quiz{display:none}}
'''


def primary_body():
    li = '\n'.join('      <li%s>%s</li>'
                   % (' class="gate"' if i in (0, 7) else '', r)
                   for i, r in enumerate(S.PRIMARY_RULES))
    defs = '\n'.join('      <div><b>%s</b><span>%s</span></div>' % (t, d)
                     for t, d in S.TRAINED_AUTHORIZED)
    return """  <section>
    <h2>The ten primary rules</h2>
    <p class="sub">These are the conditions of entry. They are the shortest list
      in the shop and the one you are actually tested on.</p>
    <ol class="primary">
%s
    </ol>

    <h3 style="margin-top:26px">What rule 8 means</h3>
    <p class="sub">Two different words, and you need both before you touch a
      machine.</p>
    <div class="gatedefs">
%s
    </div>
    <p class="note">Training is the instruction. Authorization is the check that
      you took it in. The <a href="equipment.html">equipment checks</a> on this
      site are practice for the second half &mdash; the acknowledgement in Google
      Classroom is what actually authorizes you.</p>

    <p class="occ"><b>%s</b><span><strong>Maximum occupancy.</strong> Not a hard
      count on the door &mdash; if the room goes over, whether it carries on is
      the instructor&rsquo;s call.</span></p>
  </section>""" % (li, defs, S.MAX_OCCUPANCY)


def rules_body():
    out = []
    for title, when, items in S.MAKERSPACE_RULES:
        lis = '\n'.join('        <li>%s</li>' % i for i in items)
        out.append(
            '    <div class="rulegroup">\n'
            '      <div class="rh"><b>%s</b><span>%s</span></div>\n'
            '      <ul>\n%s\n      </ul>\n'
            '    </div>' % (title, when, lis))
    return '\n'.join(out)


def quiz_html(key, table=None):
    name, blurb, qs = (table or S.QUIZZES)[key]
    data = json.dumps(qs, ensure_ascii=False)
    return '''
  <section>
    <h2>Check yourself</h2>
    <p class="sub">%s Every question has to be right before you finish &mdash; a wrong
      answer tells you why, and you pick again. There is no score and no time limit.</p>
    <div class="quiz" id="quiz"></div>
    <p class="note">This check is not a record. Nothing you do here is sent anywhere or
      stored. When you finish, screenshot the completion panel and attach it to the
      acknowledgement in Google Classroom &mdash; that is what counts.</p>
  </section>

<script>
(function(){
  var Q = %s;
  var TITLE = %s;
  var root = document.getElementById('quiz');
  var order, idx;

  function shuffle(a){ a = a.slice();
    for (var i = a.length - 1; i > 0; i--){ var j = Math.floor(Math.random()*(i+1));
      var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  function start(){ order = shuffle(Q.map(function(_,i){return i;})); idx = 0; draw(); }

  function bar(){
    var s = '<div class="qbar">';
    for (var i = 0; i < order.length; i++)
      s += '<span class="dot' + (i < idx ? ' done' : i === idx ? ' now' : '') + '"></span>';
    s += '<span class="count">' + Math.min(idx+1, order.length) + ' of ' + order.length + '</span></div>';
    return s;
  }

  function draw(){
    if (idx >= order.length) return finish();
    var q = Q[order[idx]];
    var opts = shuffle(q.o.map(function(_,i){return i;}));
    var s = bar() + '<div class="qbody"><p class="qtext">' + q.q + '</p><div class="opts">';
    opts.forEach(function(oi){
      s += '<button class="opt" type="button" data-i="' + oi + '">' + q.o[oi][0] + '</button>';
    });
    s += '</div><div id="why"></div></div>';
    root.innerHTML = s;
    root.querySelectorAll('.opt').forEach(function(b){
      b.addEventListener('click', function(){ pick(q, b); });
    });
  }

  function pick(q, btn){
    var o = q.o[+btn.dataset.i], ok = o[1], why = document.getElementById('why');
    btn.disabled = true;
    btn.className = 'opt ' + (ok ? 'right' : 'wrong');
    why.innerHTML = '<div class="why' + (ok ? ' good' : '') + '">' +
      '<span class="lbl">' + (ok ? 'That is right' : 'Not that one') + '</span>' + o[2] +
      '</div>' + (ok ? '<button class="qnext" type="button" id="nx">Next question</button>' : '');
    if (ok){
      root.querySelectorAll('.opt').forEach(function(b){ b.disabled = true; });
      document.getElementById('nx').addEventListener('click', function(){ idx++; draw(); });
      document.getElementById('nx').focus();
    }
  }

  // Draw the completion slip as a real image so it can be saved or pasted,
  // rather than relying on the student cropping a screenshot. Everything is
  // drawn with canvas primitives -- no external image is loaded, because a
  // file:// page that draws one taints the canvas and toBlob then throws.
  function drawSlip(canvas, name, dateStr){
    var W = 1000, H = 520, S = 2;           // S = supersample for a crisp PNG
    canvas.width = W * S; canvas.height = H * S;
    canvas.style.width = '100%%'; canvas.style.maxWidth = W + 'px';
    var c = canvas.getContext('2d');
    c.scale(S, S);
    c.fillStyle = '#faf8f4'; c.fillRect(0, 0, W, H);
    c.fillStyle = '#8d63ab'; c.fillRect(0, 0, W, 14);
    c.strokeStyle = '#dedbd5'; c.lineWidth = 2; c.strokeRect(1, 1, W - 2, H - 2);

    c.fillStyle = '#7d8394';
    c.font = '600 17px "Space Mono", ui-monospace, monospace';
    c.fillText('BHR ENGINEERING TECHNOLOGY', 56, 82);

    c.fillStyle = '#262b39';
    c.font = '700 30px "Chakra Petch", system-ui, sans-serif';
    c.fillText('Safety check complete', 56, 132);

    c.strokeStyle = '#dedbd5'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(56, 162); c.lineTo(W - 56, 162); c.stroke();

    c.fillStyle = '#7d8394';
    c.font = '600 14px "Space Mono", ui-monospace, monospace';
    c.fillText('CHECK', 56, 208);
    c.fillStyle = '#6b4785';
    c.font = '700 40px "Chakra Petch", system-ui, sans-serif';
    var t = TITLE, max = W - 112;
    while (c.measureText(t).width > max && t.length > 8){ t = t.slice(0, -2); }
    if (t !== TITLE) t += '…';
    c.fillText(t, 56, 254);

    c.fillStyle = '#7d8394';
    c.font = '600 14px "Space Mono", ui-monospace, monospace';
    c.fillText('COMPLETED BY', 56, 318);
    c.fillStyle = name ? '#262b39' : '#a9adb8';
    c.font = (name ? '600 ' : 'italic 600 ') + '30px "Source Serif 4", Georgia, serif';
    c.fillText(name || 'add your name above', 56, 358);
    c.strokeStyle = '#dedbd5';
    c.beginPath(); c.moveTo(56, 374); c.lineTo(560, 374); c.stroke();

    c.fillStyle = '#7d8394';
    c.font = '600 14px "Space Mono", ui-monospace, monospace';
    c.fillText('ON', 620, 318);
    c.fillStyle = '#262b39';
    c.font = '600 26px "Source Serif 4", Georgia, serif';
    c.fillText(dateStr, 620, 356);

    c.fillStyle = '#7d8394';
    c.font = '400 15px "Source Serif 4", Georgia, serif';
    c.fillText('A self-check on the shop hub, not a graded record. The acknowledgement',
               56, 442);
    c.fillText('in Google Classroom is what goes on file.', 56, 466);
  }

  function finish(){
    var d = new Date().toLocaleDateString(undefined,
      {year:'numeric', month:'long', day:'numeric'});
    root.innerHTML = '<div class="done-card"><div class="tick">&#10003;</div>' +
      '<h3>All correct</h3>' +
      '<p>You answered every question in <strong>' + TITLE + '</strong>. ' +
      'Put your name on it, then save or copy the slip and attach it to the ' +
      'acknowledgement in Google Classroom.</p>' +
      '<div class="whoami"><label for="nm">Your name</label>' +
      '<input id="nm" type="text" autocomplete="name" placeholder="First and last"></div>' +
      // The canvas draws it; a plain <img> displays it. On a phone that is the
      // whole difference between a slip you can keep and one you cannot: iOS
      // has no press-and-hold "Save Image" on a <canvas>, and its Save button
      // opens the file rather than saving it.
      '<canvas id="slip" hidden></canvas>' +
      '<img class="slip" id="slipimg" alt="Completion slip">' +
      '<div class="slipbtns">' +
      '<button type="button" class="solid" id="save">Save image</button>' +
      '<button type="button" id="copy">Copy image</button></div>' +
      '<p class="sliphint">On a phone: press and hold the slip, then choose ' +
      'Save Image.</p>' +
      '<p class="slipnote" id="snote"></p>' +
      '<button class="qagain" type="button" id="ag">Run through it again</button></div>';

    var canvas = document.getElementById('slip'),
        shown = document.getElementById('slipimg'),
        nm = document.getElementById('nm'),
        note = document.getElementById('snote');

    function redraw(){
      drawSlip(canvas, nm.value.trim(), d);
      try { shown.src = canvas.toDataURL('image/png'); } catch (e) {}
    }
    // webfonts may still be loading when the panel first appears
    redraw();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(redraw);
    nm.addEventListener('input', redraw);

    function fileName(){
      var who = nm.value.trim().replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '');
      var what = TITLE.replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '');
      return ('BHR-' + what + (who ? '-' + who : '') + '.png').toLowerCase();
    }

    document.getElementById('save').addEventListener('click', function(){
      canvas.toBlob(function(blob){
        var url = URL.createObjectURL(blob), a = document.createElement('a');
        a.href = url; a.download = fileName();
        document.body.appendChild(a); a.click(); a.remove();
        setTimeout(function(){ URL.revokeObjectURL(url); }, 1000);
        note.textContent = 'Saved as ' + fileName();
      }, 'image/png');
    });

    document.getElementById('copy').addEventListener('click', function(){
      if (!navigator.clipboard || !window.ClipboardItem){
        note.textContent = 'This browser will not let a page copy an image. ' +
                           'Use Save image instead.';
        return;
      }
      canvas.toBlob(function(blob){
        navigator.clipboard.write([new ClipboardItem({'image/png': blob})]).then(
          function(){ note.textContent = 'Copied. Paste it straight into Classroom.'; },
          function(){ note.textContent = 'Copying was blocked. Use Save image instead.'; });
      }, 'image/png');
    });

    document.getElementById('ag').addEventListener('click', start);
  }

  start();
})();
</script>''' % (blurb, data, json.dumps(name))


MAKERSPACE_BODY = '''
<div class="wrap">
  <a class="back" href="index.html">&larr; Safety</a>

  <header class="hero">
    <p class="kicker">Shop safety &middot; Makerspace</p>
    <h1>Makerspace rules</h1>
    <p>These apply the moment you walk in. Not while you are working &mdash; from the
      door.</p>
  </header>

  <section>
    <p class="emerg"><b>If someone is hurt:</b> report it, however small it seems.
      The school nurse is extension&nbsp;__EXT__. Do not attempt to remove a foreign
      object from an eye or from the body. If a chemical gets in the eyes, wash them
      under open flowing water for <strong>15 minutes</strong> before going for
      treatment.</p>
  </section>

__PRIMARY__

  <section>
    <h2>The complete set</h2>
    <p class="sub">Thirty-two rules in five groups &mdash; how to behave once you
      are inside. Posted in the room as well; this is the same list, always
      current.</p>
__RULES__
  </section>

__QUIZ__

  <section>
    <h2>Related</h2>
    <div class="grid">
      <article>
        <b><a href="sds.html">Safety data sheets</a></b>
        <p>What is in the materials you use, and what to do if one ends up somewhere it
          should not.</p>
      </article>
      <article>
        <b><a href="themes.html">Which theme?</a></b>
        <p>Ten rules from the shop safety test. Practice sorting them into the five
          groups before you sit it.</p>
      </article>
      <article>
        <b><a href="3d-printing.html">3D printer certification</a></b>
        <p>What you are allowed to print on which machine, and how to move up.</p>
      </article>
    </div>
  </section>

</div>
'''


def makerspace_body():
    b = MAKERSPACE_BODY.replace('__EXT__', S.NURSE_EXT)
    b = b.replace('__PRIMARY__', primary_body())
    b = b.replace('__RULES__', rules_body())
    return b.replace('__QUIZ__', quiz_html('makerspace'))


THEMES_BODY = '''
<div class="wrap">
  <a class="back" href="makerspace.html">&larr; Makerspace rules</a>

  <header class="hero">
    <p class="kicker">Shop safety &middot; Practice</p>
    <h1>Which theme?</h1>
    <p>The rules are grouped for a reason: the group tells you <em>when</em> to be
      thinking about a rule. Ten of them, taken from the shop safety test.</p>
  </header>

  <section>
    <h2>The five groups</h2>
    <p class="sub">In the order they appear in the rules document.</p>
    <ol class="rules">
__THEMELIST__
    </ol>
    <p class="note">Read the <a href="makerspace.html">rules</a> first. This is
      practice for the shop safety test, not a substitute for it.</p>
  </section>

__QUIZ__

</div>
'''


TECH_BODY = '''
<div class="wrap">
  <a class="back" href="index.html">&larr; Safety</a>

  <header class="hero">
    <p class="kicker">Shop safety &middot; General</p>
    <h1>Safe and appropriate technology use</h1>
    <p>Most shop safety is about not hurting yourself. This part is about not
      hurting anyone else &mdash; with a scanner, a camera, an account, or
      something you make and send out into the world.</p>
  </header>

  <section>
    <h2>What this covers</h2>
    <dl class="defs">
      <dt>Scanning and photographing people</dt>
      <dd>A 3D scan is a record of someone&rsquo;s body and a photo is a record of
        their face. Both need asking first, and both need taking no for an answer.</dd>
      <dt>Other people&rsquo;s designs</dt>
      <dd>Almost every model you download carries a licence saying what you may do
        with it. Read it, follow it, and never present someone else&rsquo;s work as
        your own.</dd>
      <dt>AI tools</dt>
      <dd>Use them, say you used them, and check the output. A confident wrong
        answer is still wrong, and the engineer who signs it owns it.</dd>
      <dt>Accounts and machines</dt>
      <dd>A signed-in account is your name on whatever happens next. Sign out.
        And never bypass a safety feature in software &mdash; that is the same act
        as taping a switch down, with less evidence.</dd>
      <dt>What gets made</dt>
      <dd>If you are not sure something should be made here, ask before you start
        rather than after it exists.</dd>
    </dl>
  </section>

__QUIZ__

  <section>
    <h2>Related</h2>
    <div class="grid">
      <article>
        <b><a href="makerspace.html">Makerspace rules</a></b>
        <p>The thirty-two rules that keep you in one piece. This page is the other
          half.</p>
      </article>
      <article>
        <b><a href="equipment.html">Equipment checks</a></b>
        <p>One check per machine, from craft knives to the cobots.</p>
      </article>
    </div>
  </section>

</div>
'''


def tech_body():
    return TECH_BODY.replace('__QUIZ__', quiz_html('tech'))


def themes_body():
    items = '\n'.join('      <li><strong>%s</strong></li>' % t for t in S.THEMES)
    b = THEMES_BODY.replace('__THEMELIST__', items)
    return b.replace('__QUIZ__', quiz_html('themes'))


def sds_body():
    cards = '\n'.join(
        '      <a href="%s%s"><b>%s</b><span>%s</span></a>' % (FOLDER, fid, name, desc)
        for name, fid, desc in S.SDS_FOLDERS)
    return '''
<div class="wrap">
  <a class="back" href="index.html">&larr; Safety</a>

  <header class="hero">
    <p class="kicker">Shop safety &middot; Materials</p>
    <h1>Safety data sheets</h1>
    <p>Every material in the shop has a sheet saying what is in it, what it does to you,
      and what to do about it. Find one before you need it, not during.</p>
  </header>

  <section>
    <p class="emerg"><b>In an incident, go to Section 4 of the sheet</b> &mdash; First Aid
      Measures. It is written for exactly this moment. Then report the injury; the nurse
      is extension&nbsp;%s. Tell whoever treats you the product name, and bring the sheet
      if you can.</p>
  </section>

  <section>
    <h2>The library</h2>
    <p class="sub">Six categories, held in the shop Drive. Open the category, then the
      product. <strong>Sign in with your school account first</strong> &mdash; these
      folders are shared with the school, not with the open internet, so a personal
      Google account will be told to request access.</p>
    <div class="sdslist">
%s
    </div>
    <p class="note"><strong>The 3D printing folder is for the Stratasys J55.</strong>
      The Vero, Elastico, DraftGrey, ContactClear and SUP710 sheets are all PolyJet
      resins and support material for that machine, so they are exactly right &mdash;
      and they matter, because uncured resin is a skin sensitiser and a Category 1 eye
      hazard. See the <a href="check-polyjet.html">resin printing check</a>.</p>
    <p class="note warn"><strong>What is missing is the filament side.</strong> For the
      Bambu Lab printers there is one sheet, for PLA, and nothing for PETG, ABS, ASA,
      TPU or any of the Bambu-branded materials. The set is also labelled MSDS, which is
      the pre-2015 naming &mdash; the current standard is a 16-section SDS. Both are
      worth fixing before students are told to rely on this library.</p>
  </section>

  <section>
    <h2>How to read one</h2>
    <p class="sub">Sixteen sections, always in the same order. In practice you will use
      four of them.</p>
    <dl class="defs">
      <dt>Section 2 &mdash; Hazard identification</dt>
      <dd>The short version: what this stuff can do to you, with the pictograms and the
        signal word. Read this before you open the container.</dd>
      <dt>Section 4 &mdash; First aid measures</dt>
      <dd>What to do for skin, eyes, breathing it in, swallowing it. This is the section
        that matters in an emergency, which is why it is near the front.</dd>
      <dt>Section 7 &mdash; Handling and storage</dt>
      <dd>How to use it without creating the problem in the first place, and where it
        lives when you are done.</dd>
      <dt>Section 8 &mdash; Exposure controls and PPE</dt>
      <dd>What protection you need. Gloves, ventilation, eye protection &mdash; and which
        kind, because not all gloves stop all chemicals.</dd>
    </dl>
    <p class="note">The other twelve sections cover firefighting, spills, physical
      properties, toxicology, disposal and transport. They matter, but they are written
      for people who handle the material in quantity.</p>
  </section>

  <section>
    <h2>The rule</h2>
    <p>If you are about to use something and you do not know what it is, look it up first.
      That includes anything you bring in from home &mdash; a material with no sheet does
      not go in this shop.</p>
  </section>

</div>
''' % (S.NURSE_EXT, cards)


HUB_BODY = '''
<div class="wrap">

  <header class="hero">
    <p class="kicker">Engineering Technology</p>
    <h1>Safety</h1>
    <p>The rules, the materials, and the training that unlocks each machine. Every
      piece of equipment you use needs a check on record before you use it.</p>
  </header>

  <section>
    <p class="emerg"><b>Right now, if someone is hurt:</b> report it, however small.
      School nurse, extension&nbsp;%s. Chemical in the eyes &mdash; flush with open
      flowing water for <strong>15 minutes</strong> before seeking treatment. Never
      try to remove a foreign object from an eye yourself.</p>
  </section>

  <section>
    <h2>Where to go</h2>
    <div class="doors">
      <a href="makerspace.html">
        <span class="n">Start here</span>
        <b>Makerspace rules</b>
        <span>The thirty-two rules that apply from the door, in five groups &mdash; with
          a check you can run through yourself.</span>
      </a>
      <a href="equipment.html">
        <span class="n">Every machine</span>
        <b>Equipment checks</b>
        <span>One check per machine or tool group &mdash; nine of them, from craft
          knives to the cobots.</span>
      </a>
      <a href="technology.html">
        <span class="n">General</span>
        <b>Technology use</b>
        <span>Scanning, cameras, AI, licences and accounts &mdash; the part of shop
          practice that affects other people.</span>
      </a>
      <a href="3d-printing.html">
        <span class="n">Machine access</span>
        <b>3D printer certification</b>
        <span>Three levels across three machines, what each one unlocks, and how to
          move up.</span>
      </a>
      <a href="sds.html">
        <span class="n">Materials</span>
        <b>Safety data sheets</b>
        <span>What is in the things you handle, and what Section 4 says to do when
          something goes wrong.</span>
      </a>
      <a href="themes.html">
        <span class="n">Practice</span>
        <b>Which theme?</b>
        <span>Sort ten rules into the five groups. Practice for the shop safety
          test.</span>
      </a>
  </section>

  <section>
    <h2>How the checks work</h2>
    <p>Each machine has its own check, and you have to get every question right to
      finish it. Get one wrong and you are told why before you pick again &mdash; the
      point is that you leave knowing it, not that we find out who did not.</p>
    <p>The checks on this site are for you. <strong>They are not the record.</strong>
      When you finish one, screenshot the completion panel and attach it to the matching
      acknowledgement in Google Classroom. That is what goes on file.</p>
    <p class="note">More machine checks are being written. If the machine you need is not
      listed yet, the acknowledgement in Classroom still applies &mdash; ask Mr. Frank.</p>
  </section>

</div>
''' % S.NURSE_EXT


# ------------------------------------------------------- equipment pages

import equipment_data as EQ  # noqa: E402

EQ_CSS = CSS + '''
.eqgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1px;
  background:var(--card);border:1px solid var(--rule)}
.eqgrid a,.eqgrid div.na{background:var(--card);box-shadow:0 0 0 1px var(--rule);
  padding:17px 20px;text-decoration:none;color:inherit;
  display:flex;flex-direction:column;gap:6px}
.eqgrid a:hover{background:var(--accent-soft)}
.eqgrid b{font-family:var(--sans);font-weight:700;font-size:16.5px;line-height:1.25}
.eqgrid a b{color:var(--ink)}
.eqgrid a:hover b{color:var(--accent)}
.eqgrid span{font-size:14.5px;color:var(--ink-2);line-height:1.5}
.eqgrid .grp{font-family:var(--mono);font-size:10px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-3)}
.eqgrid div.na b{color:var(--ink-3)}
.srcs{font-size:14px;color:var(--ink-3);line-height:1.6}
.srcs a{color:var(--ink-3)}
'''


def sources_block():
    li = '\n'.join('      <li><a href="%s">%s</a></li>' % (u, n)
                    for n, u in EQ.SOURCES)
    return ('  <section>\n    <h2>Where this comes from</h2>\n'
            '    <p class="sub">Every fact in these checks traces to a manufacturer '
            'document, a standards body or a government source. Nothing is invented, '
            'and where a widely repeated &ldquo;fact&rdquo; turned out to be wrong '
            'the check says so.</p>\n'
            '    <ul class="srcs">\n%s\n    </ul>\n  </section>' % li)


def equipment_index():
    cards = []
    for key, name, group, blurb, has in EQ.EQUIPMENT:
        if has:
            cards.append('      <a href="check-%s.html"><span class="grp">%s</span>'
                         '<b>%s</b><span>%s</span></a>' % (key, group, name, blurb))
        else:
            cards.append('      <div class="na"><span class="grp">%s</span>'
                         '<b>%s</b><span>%s</span></div>' % (group, name, blurb))
    return '''
<div class="wrap">
  <a class="back" href="index.html">&larr; Safety</a>

  <header class="hero">
    <p class="kicker">Shop safety &middot; Equipment</p>
    <h1>Equipment checks</h1>
    <p>One check per machine or group of tools. Every question has to be right
      before you finish, and a wrong answer tells you why before you pick again.</p>
  </header>

  <section>
    <p class="emerg"><b>These checks are not the record.</b> Nothing here is
      stored or sent anywhere. Finish one, screenshot the completion panel, and
      attach it to the matching acknowledgement in Google Classroom &mdash; that
      is what goes on file, and you need one for every machine you use.</p>
  </section>

  <section>
    <h2>The machines</h2>
    <p class="sub">Start with the <a href="makerspace.html">Makerspace rules</a>
      &mdash; they apply everywhere and the rest assumes them.</p>
    <div class="eqgrid">
%s
    </div>
  </section>

%s

</div>
''' % ('\n'.join(cards), sources_block())


EQ_HEADS = {
    'fdm': '<p class="note">Temperature figures here come from a third-party '
           'specification table, because Bambu\'s own pages block automated reading. '
           'Worth a confirm before this is graded.</p>',
    'polyjet': '<p class="note">The safety data sheets for these materials are in the '
               '<a href="sds.html">SDS library</a> under 3D Printing &mdash; the Vero, '
               'Elastico, DraftGrey and SUP710 sheets are all for this machine. '
               'Stratasys also publishes '
               '<a href="https://support.stratasys.com/en/Welcome/Training/PolyJet/J5-Series">'
               'training for the J5 series</a>, which is our J55: Getting Started, '
               'Operating, Designing and Post-Processing.</p>',
}


def check_body(key):
    name, blurb, _ = EQ.QUIZZES[key]
    head = EQ_HEADS.get(key, '')
    return '''
<div class="wrap">
  <a class="back" href="equipment.html">&larr; All equipment checks</a>

  <header class="hero">
    <p class="kicker">Equipment check</p>
    <h1>%s</h1>
    <p>%s</p>
  </header>

%s

%s

  <section>
    <p class="note">Finished? Screenshot the completion panel and attach it to the
      acknowledgement in Google Classroom. Read the
      <a href="makerspace.html">Makerspace rules</a> too &mdash; they apply on top
      of everything here.</p>
  </section>

</div>
''' % (name, blurb, ('  <section>\n    ' + head + '\n  </section>') if head else '',
        quiz_html(key, EQ.QUIZZES))
