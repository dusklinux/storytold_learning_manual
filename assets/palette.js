/* Shared offline appearance; independent of authored learning records. */
(() => {
 'use strict';
 const palettes=[{"id": "ember-dark", "label": "Ember \u00b7 dark", "mode": "dark"}, {"id": "ember-light", "label": "Ember \u00b7 light", "mode": "light"}, {"id": "woodland-dark", "label": "Woodland \u00b7 dark", "mode": "dark"}, {"id": "woodland-light", "label": "Woodland \u00b7 light", "mode": "light"}, {"id": "ocean-dark", "label": "Ocean \u00b7 dark", "mode": "dark"}, {"id": "ocean-light", "label": "Ocean \u00b7 light", "mode": "light"}];
 let current='ember-dark';
 try{const saved=localStorage.getItem('dusky-adobe-palette');if(palettes.some(p=>p.id===saved))current=saved;}catch{}
 function labels(){const dark=current.endsWith('-dark');for(const button of document.querySelectorAll('[data-action="theme"],#themeToggle')){const text=button.id==='themeToggle'?(dark?'☀':'◐'):(dark?'☀ Light':'◐ Dark');if(button.textContent!==text)button.textContent=text;button.setAttribute('aria-label',dark?'Switch to light palette':'Switch to dark palette');}}
 function apply(){document.documentElement.dataset.palette=current;document.documentElement.dataset.paletteMode=palettes.find(p=>p.id===current).mode;labels();}
 function set(id){if(!palettes.some(p=>p.id===id)||id===current)return;current=id;apply();try{localStorage.setItem('dusky-adobe-palette',id);}catch{}document.dispatchEvent(new CustomEvent('palette-change',{detail:id}));}
 document.addEventListener('DOMContentLoaded',()=>{labels();new MutationObserver(labels).observe(document.body,{childList:true,subtree:true});});
 window.ManualPalette={palettes,current:()=>current,set};apply();
 // Existing reader light/dark buttons select the matching palette family.
 document.addEventListener('click',e=>{if(e.target.closest('[data-action="theme"],#themeToggle')){e.preventDefault();e.stopImmediatePropagation();set(current.replace(/(dark|light)$/,document.documentElement.dataset.paletteMode==='dark'?'light':'dark'));}},true);
})();
