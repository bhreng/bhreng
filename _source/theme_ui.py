# -*- coding: utf-8 -*-
"""Light / dark switch.

The stylesheet has always supported three states -- follow the system, forced
light, forced dark -- but nothing ever let a person choose. Which meant anyone
whose computer is set to dark mode only ever saw the dark palette and had no
way to know a light one existed.

The choice is remembered per browser and applied before first paint, so the
page never flashes the wrong theme on the way in.
"""

# Runs in <head>, before any painting. Deliberately tiny and synchronous.
HEAD = '''<script>
(function(){try{var t=localStorage.getItem('bhr-theme');
if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}
catch(e){}})();
</script>'''

BUTTON = '''      <button class="themebtn" id="theme" type="button"
              title="Switch between light and dark" aria-label="Switch theme">
        <span class="ico" aria-hidden="true"></span><span class="lbl">Theme</span>
      </button>'''

CSS = '''
.themebtn{display:inline-flex;align-items:center;gap:7px;flex:none;margin-left:10px;
  font-family:var(--sans);font-weight:600;font-size:13px;color:var(--ink-2);
  background:var(--paper);border:1px solid var(--rule);border-radius:3px;
  padding:6px 11px;cursor:pointer;line-height:1}
.themebtn:hover{background:var(--accent-soft);color:var(--accent);
  border-color:var(--accent)}
.themebtn .ico{width:14px;height:14px;flex:none;border-radius:50%;
  background:var(--ink-2);
  box-shadow:inset -4px -4px 0 0 var(--paper)}
.themebtn:hover .ico{background:var(--accent)}
:root[data-theme="dark"] .themebtn .ico{box-shadow:none;background:var(--cream)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .themebtn .ico{
  box-shadow:none;background:var(--cream)}}
@media(max-width:640px){.themebtn .lbl{display:none}}
@media print{.themebtn{display:none}}
'''

JS = '''
<script defer>
// Three states, cycled by one button: follow the system, force light, force dark.
(function(){
  function ready(fn){ document.readyState !== 'loading'
    ? fn() : document.addEventListener('DOMContentLoaded', fn); }
  ready(function(){
    var btn = document.getElementById('theme'), root = document.documentElement;
    if (!btn) return;
    function get(){ try { return localStorage.getItem('bhr-theme') || 'system'; }
                    catch(e){ return 'system'; } }
    function label(){
      var m = get();
      btn.querySelector('.lbl').textContent =
        m === 'system' ? 'Theme' : (m === 'light' ? 'Light' : 'Dark');
      btn.title = m === 'system'
        ? 'Following your computer. Click for light.'
        : (m === 'light' ? 'Light. Click for dark.'
                         : 'Dark. Click to follow your computer.');
    }
    function set(m){
      try { m === 'system' ? localStorage.removeItem('bhr-theme')
                           : localStorage.setItem('bhr-theme', m); } catch(e){}
      if (m === 'system') root.removeAttribute('data-theme');
      else root.setAttribute('data-theme', m);
      label();
    }
    label();
    btn.addEventListener('click', function(){
      var m = get();
      set(m === 'system' ? 'light' : (m === 'light' ? 'dark' : 'system'));
    });
  });
})();
</script>'''
