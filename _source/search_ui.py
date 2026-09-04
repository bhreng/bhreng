# -*- coding: utf-8 -*-
"""Search box markup, styles and behaviour. One box in the header of every page."""

CSS = '''
/* --- search ------------------------------------------------------------- */
.srch{position:static;flex:none;margin-left:10px}
.srch input{
  font:inherit;font-family:var(--sans);font-size:13.5px;font-weight:500;
  width:136px;padding:6px 10px 6px 28px;color:var(--ink);
  background:var(--paper) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='none' stroke='%237d8394' stroke-width='1.7'%3E%3Ccircle cx='7' cy='7' r='4.5'/%3E%3Cpath d='M10.5 10.5 14 14'/%3E%3C/svg%3E") no-repeat 8px 50%/13px;
  border:1px solid var(--rule);border-radius:3px;transition:width .15s ease}
.srch input:focus{width:212px;outline:2px solid var(--accent);outline-offset:1px}
.srch input::placeholder{color:var(--ink-3)}
.srch .sbox{position:relative;display:inline-block}
.srch kbd{position:absolute;right:8px;top:50%;transform:translateY(-50%);
  font-family:var(--mono);font-size:10px;color:var(--ink-3);pointer-events:none;
  border:1px solid var(--rule);border-radius:3px;padding:1px 4px;background:var(--card)}
.srch input:focus~kbd,.srch input:not(:placeholder-shown)~kbd{display:none}

.sres{position:absolute;right:24px;left:auto;top:calc(100% + 6px);
  width:min(520px,calc(100vw - 48px));z-index:60;
  background:var(--card);border:1px solid var(--rule);box-shadow:var(--shadow);
  max-height:min(70vh,540px);overflow-y:auto}
.sres[hidden]{display:none}
.sres .hd{padding:9px 15px;border-bottom:1px solid var(--rule-soft);
  font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-3);position:sticky;top:0;background:var(--card)}
.sres a{display:block;padding:11px 15px;text-decoration:none;color:inherit;
  border-bottom:1px solid var(--rule-soft)}
.sres a:last-child{border-bottom:0}
.sres a:hover,.sres a.on{background:var(--accent-soft)}
.sres .ti{font-family:var(--sans);font-weight:600;font-size:15px;line-height:1.3;
  display:block;color:var(--ink)}
.sres a:hover .ti,.sres a.on .ti{color:var(--accent)}
.sres .me{display:flex;gap:8px;align-items:baseline;margin-top:3px;flex-wrap:wrap}
.sres .kd{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-3);border:1px solid var(--rule);
  padding:1px 5px;border-radius:2px;flex:none}
.sres .wh{font-size:12.5px;color:var(--ink-3)}
.sres .nt{font-size:13.5px;color:var(--ink-2);line-height:1.45;margin-top:4px;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sres mark{background:var(--cream);color:inherit;padding:0 1px;border-radius:2px}
:root[data-theme="dark"] .sres mark,
@media (prefers-color-scheme:dark){.sres mark{background:#4a4526;color:#f6f4cd}}
.sres .none{padding:22px 16px;color:var(--ink-2);font-size:14.5px;text-align:center}
.sres .ext{opacity:.6;font-size:11px}
@media(max-width:900px){
  .srch{order:3;width:100%;margin:8px 0 0}
  .srch .sbox{display:block}
  .srch input,.srch input:focus{width:100%}
  .srch kbd{display:none}
  .sres{right:24px;left:24px;width:auto}
}
@media print{.srch{display:none}}
'''

BOX = '''      <div class="srch">
        <span class="sbox">
          <input type="search" id="q" placeholder="Search" autocomplete="off"
                 aria-label="Search the site" aria-expanded="false" aria-controls="sres">
          <kbd>/</kbd>
        </span>
        <div class="sres" id="sres" role="listbox" hidden></div>
      </div>'''

JS = '''
<script src="%(r)sassets/search-index.js%(sv)s" defer></script>
<script defer>
(function(){
  var REL = %(rel)s;
  function ready(fn){ document.readyState !== 'loading'
    ? fn() : document.addEventListener('DOMContentLoaded', fn); }
  ready(function(){
    var box = document.getElementById('q'), out = document.getElementById('sres');
    if (!box || !window.BHR_INDEX) return;
    var IDX = window.BHR_INDEX, cur = -1, rows = [];

    var KIND = {video:'Video',course:'Course',site:'Site',tool:'Tool',read:'Reading',
      podcast:'Podcast',book:'Book',data:'Data',comp:'Competition',doc:'Doc',
      software:'Software',page:'Page',rule:'Rule',check:'Safety check',
      platform:'Training',sds:'Safety data',pathway:'Pathway',talk:'Talk',
      playlist:'Playlist'};

    function esc(s){ return s.replace(/[&<>"]/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

    function hi(s, terms){
      s = esc(s);
      terms.forEach(function(t){
        if (t.length < 2) return;
        s = s.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&') + ')', 'ig'),
                      '<mark>$1</mark>');
      });
      return s;
    }

    // Score by where the match lands: a title hit beats a note hit, and a hit at
    // the start of the title beats one in the middle. Every term must appear
    // somewhere, so multi-word queries narrow rather than widen.
    function score(r, terms){
      var t = r.t.toLowerCase(), n = (r.n + ' ' + r.x).toLowerCase(),
          w = r.w.toLowerCase(), s = 0;
      for (var i = 0; i < terms.length; i++){
        var q = terms[i], hit = 0;
        if (t.indexOf(q) === 0) hit = 100;
        else if (t.indexOf(' ' + q) > -1) hit = 70;
        else if (t.indexOf(q) > -1) hit = 50;
        else if (w.indexOf(q) > -1) hit = 30;
        else if (n.indexOf(q) > -1) hit = 20;
        if (!hit) return 0;
        s += hit;
      }
      if (r.k === 'page' || r.k === 'pathway') s += 12;   // structure floats up
      return s;
    }

    function run(){
      var qv = box.value.trim().toLowerCase();
      if (qv.length < 2){ close(); return; }
      var terms = qv.split(/\\s+/);
      rows = IDX.map(function(r){ return {r:r, s:score(r, terms)}; })
                .filter(function(x){ return x.s > 0; })
                .sort(function(a,b){ return b.s - a.s || a.r.t.length - b.r.t.length; })
                .slice(0, 30);
      draw(terms);
    }

    function draw(terms){
      if (!rows.length){
        out.innerHTML = '<p class="none">Nothing matches &ldquo;' +
          esc(box.value.trim()) + '&rdquo;.</p>';
      } else {
        var h = '<div class="hd">' + rows.length +
                (rows.length === 30 ? '+ matches' : ' match' + (rows.length>1?'es':'')) +
                '</div>';
        rows.forEach(function(x, i){
          var r = x.r,
              ext = /^https?:/.test(r.u),
              href = ext ? r.u : REL + r.u;
          h += '<a href="' + esc(href) + '"' + (ext ? ' target="_blank" rel="noopener"' : '') +
               ' data-i="' + i + '" role="option">' +
               '<span class="ti">' + hi(r.t, terms) +
                 (ext ? ' <span class="ext">&#8599;</span>' : '') + '</span>' +
               '<span class="me"><span class="kd">' + (KIND[r.k] || r.k) + '</span>' +
               '<span class="wh">' + hi(r.w, terms) + '</span></span>' +
               (r.n ? '<span class="nt">' + hi(r.n, terms) + '</span>' : '') +
               '</a>';
        });
        out.innerHTML = h;
      }
      out.hidden = false; box.setAttribute('aria-expanded','true'); cur = -1;
    }

    function close(){ out.hidden = true; box.setAttribute('aria-expanded','false'); cur = -1; }

    function move(d){
      var links = out.querySelectorAll('a');
      if (!links.length) return;
      if (cur > -1) links[cur].classList.remove('on');
      cur = (cur + d + links.length) %% links.length;
      links[cur].classList.add('on');
      links[cur].scrollIntoView({block:'nearest'});
    }

    box.addEventListener('input', run);
    box.addEventListener('focus', function(){ if (box.value.trim().length > 1) run(); });
    box.addEventListener('keydown', function(e){
      if (e.key === 'ArrowDown'){ e.preventDefault(); move(1); }
      else if (e.key === 'ArrowUp'){ e.preventDefault(); move(-1); }
      else if (e.key === 'Enter'){
        var links = out.querySelectorAll('a');
        if (cur > -1 && links[cur]){ e.preventDefault(); links[cur].click(); }
      }
      else if (e.key === 'Escape'){ close(); box.blur(); }
    });
    document.addEventListener('click', function(e){
      if (!e.target.closest('.srch')) close();
    });
    // "/" from anywhere jumps to the box, the way every developer tool does it
    document.addEventListener('keydown', function(e){
      if (e.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)){
        e.preventDefault(); box.focus(); box.select();
      }
    });
  });
})();
</script>'''
