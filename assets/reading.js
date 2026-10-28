/* Space-efficient reading and non-destructive practice navigation. */
(() => {
 'use strict';
 const root=document.documentElement;
 const framed=parent!==window, reader=!!document.getElementById('main');
 let state={focus:false,map:'auto'};
 if(!framed)try{const saved=JSON.parse(localStorage.getItem('dusky-adobe-layout'));if(saved&&typeof saved.focus==='boolean'&&['auto','show','hide'].includes(saved.map))state=saved;}catch{}
 function apply(){
  root.classList.toggle('reader-focus',state.focus);
  root.classList.toggle('reader-map-hide',state.map==='hide');
  root.classList.toggle('reader-map-show',state.map==='show');
  if(state.focus&&document.activeElement?.closest('.topbar,.library-bar,.keyboard-bar'))(document.getElementById('main')||document.querySelector('#readers iframe:not([hidden])'))?.focus({preventScroll:true});
  if(state.map!=='auto')document.querySelectorAll('#toggleMenu,#menuToggle,[data-action="menu"]').forEach(b=>b.setAttribute('aria-expanded',String(state.map==='show')));
  const toolbar=document.getElementById('reading-tools');
  if(toolbar){const focus=toolbar.querySelector('[data-layout="focus"]'),map=toolbar.querySelector('[data-layout="map"]');focus.textContent=state.focus?'Show bars':'Hide bars';focus.setAttribute('aria-pressed',String(state.focus));map.textContent=state.map==='hide'?'Show map':state.map==='show'?'Hide map':'Study map';map.setAttribute('aria-pressed',String(state.map==='hide'));}
 }
 function set(value){if(!value||typeof value.focus!=='boolean'||!['auto','show','hide'].includes(value.map))return;state={focus:value.focus,map:value.map};apply();if(!framed)try{localStorage.setItem('dusky-adobe-layout',JSON.stringify(state));}catch{}}
 function toggle(what){if(what==='map'&&reader){const sidebar=document.querySelector('.sidebar'),box=sidebar?.getBoundingClientRect();what=box&&box.width>0&&box.right>0&&getComputedStyle(sidebar).display!=='none'?'map-hide':'map-show';}document.dispatchEvent(new CustomEvent('reading-layout',{detail:what}));}
 window.ManualReading={set,state:()=>({...state}),toggle,move};
 const css=document.createElement('style');css.textContent=`
 body.reading #reading-tools,html.reader-standalone #reading-tools{display:block}#reading-tools{display:none;position:fixed;bottom:10px;right:12px;z-index:40;color:var(--ink)}#reading-tools summary{display:grid;place-items:center;width:36px;height:36px;list-style:none;cursor:pointer;border-radius:50%;background:var(--paper);border:1px solid var(--line);box-shadow:0 2px 8px #0002}#reading-tools summary::-webkit-details-marker{display:none}#reading-tools>div{position:absolute;bottom:44px;right:0;min-width:140px;padding:6px;display:grid;gap:5px;background:var(--paper);border:1px solid var(--line);border-radius:8px}#reading-tools button{font:12px system-ui;padding:8px;text-align:left}
 html.reader-focus body.reading>.library-bar,html.reader-focus body.reading>.keyboard-bar,html.reader-focus body.reading>#reader-controls{display:none!important}
 html.reader-focus .topbar{display:none!important}
 html.reader-map-hide .sidebar,html.reader-map-hide .right-rail,html.reader-map-hide aside.sticky,html.reader-map-hide .menu-backdrop{display:none!important}
 html.reader-map-hide .app-shell,html.reader-map-hide .shell{grid-template-columns:minmax(0,1fr)!important}
 html.reader-map-hide #main{max-width:none;width:100%}html.reader-map-hide .two-col{grid-template-columns:minmax(0,1fr)!important}
 html.reader-map-show .sidebar{display:flex!important;transform:none!important;visibility:visible!important}
 html.reader-map-show .app-shell>.sidebar{display:block!important}
 html.reader-map-show .menu-backdrop{display:none!important}
 html.reader-focus #main{padding:24px clamp(16px,3vw,40px) 64px}
 html.reader-focus .sticky{top:12px}
 .reader-step-current{outline:2px solid var(--t-accent,var(--accent));outline-offset:4px;scroll-margin-block:20px}
 body.one-step .practice-step.reader-step-hidden{display:none!important}body.one-step .practice-step.reader-step-current{display:list-item!important}
 @media print{html.reader-focus #main{padding:5mm 8mm}html.reader-map-show .sidebar{display:none!important}#reading-tools{display:none!important}.reader-step-current{outline:none}html body.one-step .practice-step.reader-step-hidden{display:list-item!important}}
 `;document.head.append(css);
 if(reader&&!framed)root.classList.add('reader-standalone');
 if(!reader||!framed){const bar=document.createElement('details');bar.id='reading-tools';bar.innerHTML='<summary aria-label="Reading controls" title="Reading controls · Alt+Shift+F bars · Alt+Shift+B map"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5M8 8h8v8H8z"/></svg></summary><div><button type="button" data-layout="focus" title="Hide/show all top bars (Alt+Shift+F)">Hide bars</button><button type="button" data-layout="map" title="Hide/show study map (Alt+Shift+B)">Hide map</button></div>';document.body.append(bar);bar.addEventListener('click',e=>{const button=e.target.closest('[data-layout]');if(button){toggle(button.dataset.layout);bar.open=false;bar.querySelector('summary').focus({preventScroll:true});}});}
 document.addEventListener('click',e=>{if(reader&&state.map!=='auto'&&e.target.closest('#toggleMenu,#menuToggle,[data-action="menu"]')){e.preventDefault();e.stopImmediatePropagation();toggle('map');}},true);
 document.addEventListener('keydown',e=>{if(reader&&e.key==='Escape'&&state.map==='show'&&getComputedStyle(document.querySelector('.sidebar')).position==='fixed')toggle('map');if(e.key==='Escape'&&e.target.closest('#reading-tools')){const bar=document.getElementById('reading-tools');bar.open=false;bar.querySelector('summary').focus();return;}if(e.isComposing||e.repeat)return;if(e.altKey&&e.shiftKey&&!e.ctrlKey&&!e.metaKey&&['f','b'].includes(e.key.toLowerCase())){e.preventDefault();e.stopImmediatePropagation();toggle(e.key.toLowerCase()==='f'?'focus':'map');}},true);
 let lastRoute='',position=-1;
 function mark(step){document.querySelectorAll('.reader-step-current').forEach(x=>x.classList.remove('reader-step-current'));step.classList.add('reader-step-current');step.tabIndex=-1;step.focus({preventScroll:true});step.scrollIntoView({block:'center',behavior:'instant'});}
 function move(direction){
  const route=location.hash;if(route!==lastRoute){lastRoute=route;position=-1;}
  const steps=[...document.querySelectorAll('#main .step-list>li,#main .steps>.step,#main .practice-step')];
  const bottom=scrollY+innerHeight>=document.documentElement.scrollHeight-3,top=scrollY<3;
  const native=document.querySelector(direction>0?'[data-action="stepnext"],[data-pointer="next"]':'[data-action="stepback"],[data-pointer="prev"]');
  if(steps.length&&!(direction>0&&bottom)&&!(direction<0&&top)){
   const later=[...document.querySelectorAll('#main h2,#main h3')].filter(x=>steps.at(-1).compareDocumentPosition(x)&Node.DOCUMENT_POSITION_FOLLOWING);
   if(position>=steps.length){const next=position+direction;if(next>=steps.length&&next<steps.length+later.length){position=next;mark(later[next-steps.length]);return;}if(next===steps.length-1){position=next;mark(steps[next]);return;}if(direction>0){window.scrollTo({top:document.documentElement.scrollHeight,behavior:'instant'});return;}}
   if(native){if(!native.disabled){native.click();requestAnimationFrame(()=>{const step=[...document.querySelectorAll('#main .step-list>li,#main .steps>.step')].find(x=>!x.hidden&&!x.classList.contains('focus-hidden'));if(step)mark(step);});return;}}
   else{
    const focused=steps.findIndex(x=>x===document.activeElement||x.contains(document.activeElement));if(focused>=0)position=focused;
    const next=position<0?(direction>0?0:steps.length-1):position+direction;
    if(next>=0&&next<steps.length){position=next;if(document.body.classList.contains('one-step'))steps.forEach((x,i)=>x.classList.toggle('reader-step-hidden',i!==next));mark(steps[next]);return;}
   }
   if(direction>0&&later.length){position=steps.length;mark(later[0]);return;}
  }
  const links=[...document.querySelectorAll('#main .prevnext a,#main .bottom-nav a,#main .two-col>div>.actions:last-child a')];
  const link=links.find(x=>direction>0?/Next|Finished|Knowledge check|Stage review/i.test(x.textContent):/Previous/i.test(x.textContent));
  if(link)link.click();
 }
 document.addEventListener('vim-step',e=>{if(reader)move(e.detail);});
 apply();
})();
