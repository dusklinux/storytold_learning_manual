/* Shared recall controls; native shortcut references retain their exact source text. */
(() => {
 'use strict';
 function reveal(card,show){if(!card)return;card.querySelector('[data-test-answer]').hidden=!show;const button=card.querySelector('[data-action="reveal-key"]');button.textContent=show?'Hide answer':'Reveal answer';button.setAttribute('aria-expanded',String(show));if(show&&card.contains(document.activeElement))card.scrollIntoView({block:'nearest',behavior:'instant'});}
 function key(value){const cards=[...document.querySelectorAll('.key-test')].filter(c=>c.getClientRects().length);if(!cards.length)return false;let at=cards.findIndex(c=>c===document.activeElement||c.contains(document.activeElement));if(['l','Enter','h'].includes(value)){const card=cards[Math.max(0,at)];if(at<0)card.focus();reveal(card,value!=='h');}else{at=value==='g'?0:value==='G'?cards.length-1:value==='j'||value==='ArrowDown'?Math.min(cards.length-1,at+1):Math.max(0,at<0?cards.length-1:at-1);cards[at].focus({preventScroll:true});cards[at].scrollIntoView({block:'center',behavior:'instant'});}return true;}
 window.ShortcutStudy={reveal};
 document.addEventListener('vim-card',e=>{if(key(e.detail))e.preventDefault();});
 document.addEventListener('keydown',e=>{if(e.altKey||e.ctrlKey||e.metaKey||e.isComposing||e.target.closest('input,textarea,select,[contenteditable]'))return;if(!['ArrowDown','ArrowUp','Enter'].includes(e.key)||!e.target.closest('.key-test'))return;if(e.key==='Enter'&&e.target.matches('button,a'))return;if(key(e.key))e.preventDefault();});
 let main=document.getElementById('main');if(!main)return;const host=document.body;
 const style=document.createElement('style');style.textContent=`.shortcut-category{font-size:1.1rem;margin:24px 0 8px;color:var(--t-accent)}.shortcut-study-tools{display:flex;align-items:center;flex-wrap:wrap;gap:10px;margin:16px 0}.shortcut-study-tools button,.shortcut-study-tools select,.key-test button{font:inherit;color:var(--t-ink);background:var(--t-paper);padding:8px 12px;border:1px solid var(--t-line);border-radius:7px}.key-test{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;border:1px solid var(--t-line);background:var(--t-paper);border-radius:10px;padding:18px;margin:12px 0;scroll-margin:24px}.key-test h2{align-self:center;font-size:1.1rem;margin:0}.key-test:focus,.key-test:focus-within{outline:2px solid var(--t-accent);outline-offset:3px}.key-test [data-test-answer]{grid-column:1/-1;border-top:1px solid var(--t-line);margin-top:14px;padding-top:12px}.key-test [hidden],[data-native-shortcut-reference][hidden],#native-recall[hidden]{display:none!important}.catalog-item .splitrow{flex-wrap:wrap}.catalog-item .shortcut-key{white-space:normal;overflow-wrap:anywhere}@media print{.shortcut-study-tools,.key-test button{display:none!important}.key-test [data-test-answer]{display:block!important}}`;
 document.head.append(style);
 let mode='reference',lastRoute='';
 function button(text,action){const b=document.createElement('button');b.type='button';b.textContent=text;b.dataset.studyAction=action;return b;}
 function enhance(){
  main=document.getElementById('main');if(!main)return;
  const route=location.hash.replace(/^#\/?/,'');
  if(route!==lastRoute){mode='reference';lastRoute=route;}
  const ae=route.split('/')[0]==='shortcuts',ps=route==='library/shortcuts',pr=route.startsWith('ref/shortcuts');
  if(!ae&&!ps&&!pr)return;
  const reference=ae?main.querySelector('.catalog'):ps?main.querySelector('#ref-results'):main.querySelector('#refRows');
  if(!reference)return;const table=reference.querySelector('table');if(ae?reference.dataset.studyReady:!table||table.dataset.studyReady)return;if(table)table.dataset.studyReady='true';
  reference.dataset.studyReady='true';reference.dataset.nativeShortcutReference='';
  const records=[];
  if(ae){
   const groups=new Map();
   for(const card of reference.querySelectorAll('.catalog-item')){const label=card.querySelector('.label'),category=label?.textContent||'Shortcuts';const record={category,key:card.querySelector('.shortcut-key')?.textContent||'',action:card.querySelector('h3')?.textContent||'',context:[...card.querySelectorAll('p')].map(x=>x.textContent).join('\n')};records.push(record);label?.remove();if(!groups.has(category))groups.set(category,[]);groups.get(category).push(card);}
   reference.replaceChildren();for(const [category,cards] of groups){const heading=document.createElement('h2');heading.className='shortcut-category';heading.textContent=category;reference.append(heading,...cards);}
  }else{
   const table=reference.querySelector('table');if(!table)return;const groupIndex=ps?0:2,groups=new Map();
   for(const row of table.querySelectorAll('tbody tr')){const cells=[...row.cells];if(cells.length<5)continue;const text=cells.map(c=>c.textContent);const category=text[groupIndex];records.push({category,key:text[2-(pr?1:0)],action:text[ps?1:0],context:text.slice(3).join('\n')});cells[groupIndex].remove();if(!groups.has(category))groups.set(category,[]);groups.get(category).push(row);}
   table.querySelectorAll('thead tr').forEach(row=>row.cells[groupIndex]?.remove());table.querySelectorAll('tbody').forEach(body=>body.remove());
   for(const [category,rows] of groups){const body=document.createElement('tbody'),tr=document.createElement('tr'),heading=document.createElement('th');heading.colSpan=4;heading.scope='rowgroup';heading.className='shortcut-category';heading.textContent=category;tr.append(heading);body.append(tr,...rows);table.append(body);}
  }
  // A native rerender may replace only the filtered table, so replace its controls too.
  main.querySelectorAll('.shortcut-study-tools,#native-recall').forEach(x=>x.remove());
  const tools=document.createElement('div');tools.className='shortcut-study-tools';
  const label=document.createElement('label');label.textContent='Shortcut view ';
  const select=document.createElement('select');select.setAttribute('aria-label','Shortcut view');for(const [value,text] of [['reference','Reference'],['test','Self-test']]){const option=document.createElement('option');option.value=value;option.textContent=text;select.append(option);}select.value=mode;label.append(select);tools.append(label,button('Reveal all answers','reveal'),button('Hide all answers','hide'));
  const hint=document.createElement('small');hint.textContent='Recall the action, then reveal it. With Vim on: j/k move · l reveal · h hide. Arrows/Enter also work.';hint.style.cssText='flex-basis:100%;color:var(--t-muted)';tools.append(hint);
  const tests=document.createElement('div');tests.id='native-recall';
  const ordered=[...new Set(records.map(r=>r.category))].flatMap(category=>records.filter(r=>r.category===category));
  let category='',answerIndex=0;for(const record of ordered){if(record.category!==category){category=record.category;const heading=document.createElement('h2');heading.className='shortcut-category';heading.textContent=category;tests.append(heading);}const card=document.createElement('section');card.className='key-test';card.tabIndex=0;const heading=document.createElement('h2');heading.textContent=record.key;const show=button('Reveal answer','one');show.dataset.action='reveal-key';show.setAttribute('aria-expanded','false');const answer=document.createElement('div');answer.id='native-answer-'+answerIndex++;show.setAttribute('aria-controls',answer.id);answer.dataset.testAnswer='';answer.hidden=true;const action=document.createElement('strong');action.textContent=record.action;const detail=document.createElement('p');detail.textContent=record.context;answer.append(action,detail);card.append(heading,show,answer);tests.append(card);}
  reference.before(tools);reference.after(tests);
  function display(){hint.hidden=mode!=='test';reference.hidden=mode==='test';tests.hidden=mode!=='test';tools.querySelectorAll('button').forEach(b=>b.hidden=mode!=='test');}
  select.addEventListener('change',()=>{mode=select.value;tests.querySelectorAll('.key-test').forEach(c=>reveal(c,false));display();if(mode==='test')tests.querySelector('.key-test')?.focus();});
  tools.addEventListener('click',e=>{const action=e.target.dataset.studyAction;if(action==='reveal'||action==='hide')tests.querySelectorAll('.key-test').forEach(c=>reveal(c,action==='reveal'));});
  tests.addEventListener('click',e=>{if(e.target.dataset.studyAction==='one'){const card=e.target.closest('.key-test');reveal(card,card.querySelector('[data-test-answer]').hidden);}});
  display();
 }
 const observer=new MutationObserver(()=>{observer.disconnect();try{enhance();}finally{observer.observe(host,{childList:true,subtree:true});}});
 enhance();observer.observe(host,{childList:true,subtree:true});
})();
