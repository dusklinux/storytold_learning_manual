/* Buildless offline library. Native readers own their lessons; this owns the shared desk. */
(() => {
  'use strict';
  const manuals=window.LIBRARY_MANUALS, byId=Object.fromEntries(manuals.map(m=>[m.id,m]));
  const $=id=>document.getElementById(id), workspace=$('workspace'), readers=$('readers');
  const escape=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const key='dusky-adobe-library-v1', frames=new Map(), requests=new Map();
  let storage=true, timer, searchUrlTimer, renderGeneration=0, focusSearch=false, busy='', requestId=0, searchPromise, searchData, searchLimit=40, compareLimit=30;
  let query='', appFilter='', kindFilter='', compareQuery='', allKeys=false, importing=false;
  let saved={manuals:{}, preferences:null};
  try {
    const raw=localStorage.getItem(key);
    if(raw){
      let data;
      try{data=JSON.parse(raw);}catch{notify('Malformed saved library data was ignored. Individual reader records remain available.');}
      if(data&&typeof data==='object'&&data.manuals&&typeof data.manuals==='object'&&!Array.isArray(data.manuals)){
        saved={manuals:Object.fromEntries(Object.entries(data.manuals).filter(([id,v])=>byId[id]&&v&&typeof v==='object'&&v.state)),preferences:validPreferences(data.preferences)?data.preferences:null};
      }
    }
    localStorage.setItem(key,JSON.stringify(saved));
  } catch {storage=false;}
  function validPreferences(x){return x&&typeof x==='object'&&['large','contrast','oneStep'].every(k=>typeof x[k]==='boolean');}
  function writeSaved(){
    const wasAvailable=storage;
    try{localStorage.setItem(key,JSON.stringify(saved));storage=true;}catch{storage=false;}
    if(wasAvailable&&!storage)notify('Library progress could not be saved. Export all progress before closing.');
    const indicator=$('library-storage-state');if(indicator)indicator.textContent=storage?'Available in this browser.':'Unavailable. Export before closing this page.';
  }
  function persist(){clearTimeout(timer);timer=setTimeout(writeSaved,200);}
  function setBusy(value){busy=value;for(const button of document.querySelectorAll('[data-action="export-library"],[data-action="import-library"],[data-action="apply-preferences"]'))button.disabled=!!busy;}
  function backupStatus(message){notify(message);const status=$('backup-status');if(status)status.textContent=message;}
  function standaloneURL(id,path){return 'manuals/'+id+'/index.html#'+(id==='photoshop'?'/':'')+(path||byId[id].home);}
  function updateStandalone(id,path){const link=$('reader-controls')?.querySelector('a');if(link)link.setAttribute('href',standaloneURL(id,path));}

  function notify(message){$('notice').textContent=message;clearTimeout(notify.timer);notify.timer=setTimeout(()=>{$('notice').textContent='';},6500);}
  function route(){const pieces=location.hash.slice(1).split('/');return {name:pieces[0]||'home',id:pieces[1],path:pieces.slice(2).join('/')};}
  function readLink(id,path){return '#read/'+id+'/'+(path||byId[id].home);}
  function lastRoute(id){return saved.manuals[id]?.route||byId[id].home;}
  function send(id,message){frames.get(id)?.element.contentWindow.postMessage({channel:'dusky-library-v1',...message},'*');}
  function ensureFrame(id){
    if(frames.has(id))return frames.get(id).ready;
    let resolve,reject;
    const ready=new Promise((a,b)=>{resolve=a;reject=b;});
    const frame=document.createElement('iframe');frame.title=byId[id].name+' offline manual';frame.dataset.app=id;frame.hidden=true;frame.inert=true;
    // Each reader is loaded once per session and retained, including when storage is blocked.
    const record={element:frame,ready,resolve,reject,loaded:false,navigation:0};frames.set(id,record);
    record.timeout=setTimeout(()=>{frames.delete(id);frame.remove();reject(Error(byId[id].name+' did not finish opening. Keep the full folder together and retry.'));},15000);
    frame.src='manuals/'+id+'/index.html';readers.append(frame);
    return ready;
  }
  function ask(id,type,value,extra={}){return new Promise((resolve,reject)=>{
    const request=++requestId,timeout=setTimeout(()=>{requests.delete(request);reject(Error(byId[id].name+' did not respond.'));},10000);
    requests.set(request,{id,resolve,reject,timeout});send(id,{type,value,request,...extra});
  });}
  window.addEventListener('message',event=>{
    const m=event.data;
    if(m?.channel!=='dusky-manual-v1'||!byId[m.app])return;
    const frame=frames.get(m.app);
    if(!frame||event.source!==frame.element.contentWindow)return;
    if(m.type==='ready'){
      const r=route();send(m.app,{type:'initialize',navigation:frame.navigation,updatedAt:saved.manuals[m.app]?.updatedAt||0,state:saved.manuals[m.app]?.state,preferences:saved.manuals[m.app]?.state?null:saved.preferences,route:r.name==='read'&&r.id===m.app?(r.path||byId[m.app].home):lastRoute(m.app)});
    }else if(m.type==='snapshot'){
      saved.manuals[m.app]={updatedAt:m.updatedAt,state:m.state,route:m.route,progress:m.progress,storage:m.storage};
      persist();
      if(!frame.loaded){frame.loaded=true;clearTimeout(frame.timeout);frame.resolve();}
      const r=route();
      if(r.name==='read'&&r.id===m.app){
        // Only the latest requested navigation may update the library URL.
        if(m.navigation===frame.navigation){
          frame.route=m.route;updateStandalone(m.app,m.route);const next=readLink(m.app,m.route);if(location.hash!==next)history.replaceState(null,'',next);
        }
      }
      updateProgress();
    }else if(m.type==='navigate'){
      if(route().name==='read'&&route().id===m.app&&m.navigation===frame.navigation){const next=readLink(m.app,m.route);if(location.hash===next)send(m.app,{type:'navigate',navigation:frame.navigation,route:m.route});else location.hash=next;}
    }else if(m.type==='warning'){notify(byId[m.app].name+': '+m.error);
    }else if(m.type==='response'){
      const req=requests.get(m.request);if(!req||req.id!==m.app)return;requests.delete(m.request);clearTimeout(req.timeout);m.ok?req.resolve(m.value):req.reject(Error(m.error));
    }
  });
  function status(id){const p=saved.manuals[id]?.progress;return p?`${p.done} / ${p.total} ${p.unit} complete`:'Ready when you are';}
  function updateProgress(){for(const m of manuals){const el=document.querySelector('[data-progress="'+m.id+'"]');if(el){el.textContent=status(m.id);const p=saved.manuals[m.id]?.progress;const bar=document.querySelector('[data-bar="'+m.id+'"]');if(bar)bar.style.width=p?Math.round(p.done/p.total*100)+'%':'0%';}}}
  const footer=()=>'<footer class="footer">Independent learning manuals · Windows Adobe workflows · Linux / Windows reader<br>Research snapshots: 28 October 2026. Source links are optional online reading; lessons, references and included practice assets stay local. <a href="docs/SECOND_PASS.md" target="_blank">Integration audit</a> · <a href="README.md" target="_blank">Project guide</a></footer>';
  function home(){return '<div class="page"><section class="hero"><div class="eyebrow">The offline creative library</div><h1>Three crafts.<br>One place to learn.</h1><p>Choose your workspace. Follow a complete learning path, look up a tool, or connect the ideas across image making, editing and motion.</p><div class="meta"><span class="dot">Everything needed to read is included</span><span>'+manuals.reduce((n,m)=>n+m.lessons,0)+' guided lessons</span><span>No server or installation</span></div></section><div class="manual-grid">'+manuals.map(m=>`<article class="manual-card" style="--app-color:${m.color};--app-bg:${m.bg}"><div class="app-icon" aria-hidden="true">${m.mark}</div><h2>${m.name}</h2><p class="version">Windows · research target ${m.version}</p><p class="description">${m.description}</p><ul><li>${m.lessons} lessons through ${m.stages} stages</li>${m.highlights.map(x=>'<li>'+escape(x)+'</li>').join('')}</ul><div class="reading-progress"><span data-progress="${m.id}">${status(m.id)}</span><div class="track"><span data-bar="${m.id}" style="width:0%"></span></div></div><a class="button primary" href="${readLink(m.id,lastRoute(m.id))}">${saved.manuals[m.id]?'Continue':'Open'} ${m.name} →</a><div class="card-actions"><a href="${readLink(m.id,m.start)}">First lesson</a><a href="manuals/${m.id}/ALL_CONTENT.md" target="_blank">Text edition</a><a href="${readLink(m.id,m.settings)}">App progress</a></div></article>`).join('')+'</div><div class="twocol"><section class="panel"><h2>A reference desk for all three apps</h2><p>Search full lesson text, references and Premiere’s technical field guides together. Every result names its app and opens the matching entry.</p><div class="inline-links"><a href="#search">Search the library →</a><a href="#compare">Compare Windows keys →</a></div></section><section class="panel"><h2>Read on Linux. Practice in Windows.</h2><p>Keep this folder on your host while working in your Windows VM. Export one progress backup to carry all three learning records between browsers or machines.</p><a href="#settings">Reading settings & progress →</a></section></div>'+footer()+'</div>';}
  async function loadSearch(){
    if(!searchPromise)searchPromise=new Promise((resolve,reject)=>{
      const script=document.createElement('script');script.src='assets/search.js';
      script.onload=()=>{searchData=window.LIBRARY_SEARCH.map(x=>({...x,normalized:(x.title+' '+x.body).toLocaleLowerCase('en')}));resolve();};
      script.onerror=()=>{script.remove();searchPromise=null;reject(Error('Search data could not load. Keep assets/search.js with this folder.'));};document.head.append(script);
    });
    return searchPromise;
  }
  function excerpt(text,q){const tokens=q.trim().toLowerCase().split(/\s+/);const i=Math.max(0,text.toLowerCase().indexOf(tokens[0]||''));const start=Math.max(0,i-45);return (start?'…':'')+text.slice(start,start+230)+(text.length>start+230?'…':'');}
  function searchPage(){return '<div class="page"><div class="eyebrow">One local index · three manuals</div><h1>Find the idea. Open the exact entry.</h1><p class="lede">Search every word in lessons, recipes, references and field guides. App names and context stay attached to each result.</p><div class="search-form"><input id="library-search" type="search" placeholder="Try: alpha, mask, ripple, Ctrl+S…" aria-label="Search all manuals" value="'+escape(query)+'"><select id="app-filter" aria-label="Filter by application"><option value="">All applications</option>'+manuals.map(m=>`<option value="${m.id}" ${m.id===appFilter?'selected':''}>${m.name}</option>`).join('')+'</select><select id="kind-filter" aria-label="Filter by entry type"><option value="">All entry types</option>'+[...new Set(searchData.map(x=>x.kind))].sort().map(k=>`<option ${k===kindFilter?'selected':''}>${k}</option>`).join('')+'</select></div><div id="search-results"></div>'+footer()+'</div>';}
  function searchResults(){
    const tokens=query.toLocaleLowerCase('en').trim().split(/\s+/).filter(Boolean);
    const target=$('search-results');if(!target)return;
    if(!tokens.length){target.innerHTML='<div class="empty">Search '+searchData.length.toLocaleString()+' records. Try a shared concept to see how each app teaches it: <a href="#search/alpha">alpha</a>, <a href="#search/mask">mask</a>, <a href="#search/color">color</a> or <a href="#search/keyframe">keyframe</a>.</div>';return;}
    const matches=searchData.filter(x=>(!appFilter||x.app===appFilter)&&(!kindFilter||x.kind===kindFilter)&&tokens.every(t=>x.normalized.includes(t))).map(x=>({...x,score:tokens.reduce((n,t)=>n+(x.title.toLowerCase().includes(t)?10:0),0)})).sort((a,b)=>b.score-a.score);
    target.innerHTML='<p class="result-count" role="status">'+matches.length+' matches'+(matches.length>searchLimit?' · showing '+searchLimit:'')+'</p><div class="results">'+matches.slice(0,searchLimit).map(x=>`<a class="result" href="${escape(readLink(x.app,x.route))}"><small>${byId[x.app].name} · ${escape(x.kind)}</small><strong>${escape(x.title)}</strong><p>${escape(excerpt(x.body,query))}</p></a>`).join('')+'</div>'+(matches.length>searchLimit?'<button class="more" data-action="more-search">Show 40 more results</button>':'')+(!matches.length?'<div class="empty">No matches. Try fewer words or clear a filter.</div>':'');
  }
  function comparePage(){return '<div class="page"><div class="eyebrow">Muscle memory, with context</div><h1>Same keys. Check the task.</h1><p class="lede">Compare the documented Windows bindings side by side. A shared binding can perform different tasks. Focus, selection, custom presets and the installed app determine what happens.</p><div class="panel"><p>This groups exact key labels from the supplied manuals, ignoring case, spaces and code formatting. It does not infer equivalent commands or merge different gestures. Each link opens the original context.</p></div><input class="compare-search" id="compare-search" type="search" aria-label="Filter shortcut comparisons" placeholder="Filter keys, commands or contexts…" value="'+escape(compareQuery)+'"><p><label><input type="checkbox" id="all-keys" '+(allKeys?'checked':'')+'> Include bindings listed in only one app</label></p><div id="key-results"></div>'+footer()+'</div>';}
  function compareResults(){
    const groups=new Map();for(const record of window.LIBRARY_KEYS){const normalized=record.key.replace(/[`\s]/g,'').toLowerCase();if(!groups.has(normalized))groups.set(normalized,[]);groups.get(normalized).push(record);}
    const q=compareQuery.toLowerCase().trim();const selected=[...groups.values()].filter(rows=>(allKeys||new Set(rows.map(x=>x.app)).size>1)&&(!q||rows.some(x=>(x.key+' '+x.action+' '+x.context).toLowerCase().includes(q)))).sort((a,b)=>new Set(b.map(x=>x.app)).size-new Set(a.map(x=>x.app)).size||a[0].key.localeCompare(b[0].key));
    $('key-results').innerHTML='<p class="result-count" role="status">'+selected.length+' matching key groups'+(selected.length>compareLimit?' · showing '+compareLimit:'')+'</p>'+selected.slice(0,compareLimit).map(rows=>'<section class="key-group"><h2><kbd>'+escape(rows[0].key)+'</kbd> · '+new Set(rows.map(x=>x.app)).size+' app(s)</h2>'+rows.map(x=>`<div class="key-record"><strong>${byId[x.app].name}</strong><div><a href="${escape(readLink(x.app,x.route))}">${escape(x.action)}</a><small>${escape(x.context)}</small></div></div>`).join('')+'</section>').join('')+(selected.length>compareLimit?'<button data-action="more-keys">Show 30 more groups</button>':'')+(!selected.length?'<div class="empty">No matching bindings. Try a shorter key label or include single-app bindings.</div>':'');
  }
  function settingsPage(){const p=saved.preferences||{};return '<div class="page"><div class="eyebrow">Your portable learning desk</div><h1>Progress & reading</h1><p class="lede">One backup carries all three manuals’ checkmarks, quiz answers, bookmarks, Premiere notes and reading preferences. It stays on your device.</p><section class="panel"><h2>Library backup</h2><p>Export loads any unopened manuals to include their current records. Import validates all three records before replacing progress. Existing single-manual backups can still be imported inside their own manual.</p><div class="actions"><button class="primary" data-action="export-library">Export all progress</button><button data-action="import-library">Import library backup</button></div><p id="backup-status" role="status"></p><p><strong>Library storage:</strong> <span id="library-storage-state">'+(storage?'Available in this browser.':'Unavailable. Export before closing this page.')+'</span> File URLs can have different storage rules in different browsers. There is no automatic host/VM sync.</p></section><section class="panel"><h2>Apply reading preferences to all manuals</h2><p>These controls set all three readers together. Individual manuals also retain their own reading controls.</p><div class="settings-grid">'+[['large','Larger text'],['contrast','Higher contrast'],['oneStep','One step at a time']].map(([k,name])=>`<label><input data-library-preference="${k}" type="checkbox" ${p[k]?'checked':''}> ${name}</label>`).join('')+'</div><div class="actions"><button data-action="apply-preferences">Apply to all three</button></div></section><section class="panel"><h2>Individual learning records</h2>'+manuals.map(m=>`<p><a href="${readLink(m.id,m.settings)}">${m.name} — app progress & single-manual import</a><br><small data-progress="${m.id}">${status(m.id)}</small></p>`).join('')+'</section><section class="panel"><h2>Print the active lesson</h2><p>While reading, use the button below the library header to print that manual. Its print layout expands every practice step. You can also open the standalone reader and use your browser’s Print command.</p></section>'+footer()+'</div>';}
  function applyLibraryPreferences(){const p=saved.preferences||{};document.body.classList.toggle('large-reading',!!p.large);document.body.classList.toggle('high-contrast',!!p.contrast);}
  async function render(){
    const generation=++renderGeneration,r=route(), reading=r.name==='read'&&!!byId[r.id];
    document.body.classList.toggle('reading',reading);workspace.hidden=reading;readers.hidden=!reading;
    for(const [id,frame] of frames){frame.element.hidden=!reading||id!==r.id;frame.element.inert=!reading||id!==r.id;}
    $('switcher').value=reading?r.id:'';
    document.querySelectorAll('[data-nav]').forEach(a=>{if(a.dataset.nav===r.name)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
    document.title=reading?byId[r.id].name+' · Dusky Adobe Manual':'Dusky Adobe Manual';
    applyLibraryPreferences();
    if(reading){
      workspace.innerHTML='<p>To print the current manual, use its <strong>Print manual</strong> button or open its standalone reader.</p>';
      let controls=$('reader-controls');if(!controls){controls=document.createElement('div');controls.id='reader-controls';controls.className='reader-controls';readers.before(controls);}
      controls.innerHTML='<span>'+byId[r.id].name+' · Windows '+byId[r.id].version+'</span><button data-action="print-manual">Print manual</button><a href="manuals/'+r.id+'/index.html#'+(r.id==='photoshop'?'/':'')+escape(r.path||byId[r.id].home)+'" target="_blank">Open standalone ↗</a>';
      controls.hidden=false;
      let loading=$('reader-loading');if(!loading){loading=document.createElement('p');loading.id='reader-loading';loading.className='reader-loading';loading.setAttribute('role','status');readers.prepend(loading);}loading.textContent='Opening '+byId[r.id].name+'…';loading.hidden=!!frames.get(r.id)?.loaded;
      const ready=ensureFrame(r.id),record=frames.get(r.id);const navigation=++record.navigation;
      try{await ready;if(generation!==renderGeneration)return;loading.hidden=true;record.element.hidden=false;record.element.inert=false;send(r.id,{type:'navigate',navigation,route:r.path||byId[r.id].home});}
      catch(error){if(generation!==renderGeneration)return;notify(error.message);document.body.classList.remove('reading');readers.hidden=true;controls.hidden=true;workspace.hidden=false;workspace.innerHTML='<div class="page"><h1>Manual could not open</h1><p>'+escape(error.message)+'</p><button data-action="retry-reader">Retry opening manual</button> <a href="#home">Return to library</a></div>';}
      return;
    }
    if($('reader-controls'))$('reader-controls').hidden=true;
    if(r.name==='home')workspace.innerHTML=home();
    else if(r.name==='settings')workspace.innerHTML=settingsPage();
    else if(r.name==='search'||r.name==='compare'){
      workspace.innerHTML='<div class="page" role="status">Opening the local reference index…</div>';
      try{await loadSearch();if(generation!==renderGeneration)return;
        if(r.name==='search'){query='';if(r.id){try{query=decodeURIComponent([r.id,r.path].filter(Boolean).join('/'));}catch{query='';}}workspace.innerHTML=searchPage();searchResults();if(focusSearch){$('library-search').focus();focusSearch=false;}}
        else{workspace.innerHTML=comparePage();compareResults();}
      }catch(error){if(generation!==renderGeneration)return;workspace.innerHTML='<div class="page"><h1>Reference index unavailable</h1><p>'+escape(error.message)+'</p><a href="#home">Return to library</a></div>';}
    }else workspace.innerHTML='<div class="page"><h1>That page was not found</h1><a href="#home">Choose a manual</a></div>';
    updateProgress();setBusy(busy);window.scrollTo(0,0);
  }
  async function readAll(){
    await Promise.all(manuals.map(m=>ensureFrame(m.id)));
    const records=await Promise.all(manuals.map(m=>ask(m.id,'read')));
    for(let i=0;i<manuals.length;i++)saved.manuals[manuals[i].id]=records[i];
    persist();return records;
  }
  async function exportLibrary(){
    if(busy)return;setBusy('export');
    notify('Collecting all three learning records…');
    try{
      await readAll();
      const payload={format:'dusky-adobe-library',schema:1,exportedAt:new Date().toISOString(),preferences:saved.preferences,manuals:Object.fromEntries(manuals.map(m=>[m.id,{version:m.version,state:saved.manuals[m.id].state,route:lastRoute(m.id)}]))};
      const url=URL.createObjectURL(new Blob([JSON.stringify(payload,null,2)],{type:'application/json'}));const link=document.createElement('a');link.href=url;link.download='dusky-adobe-progress.json';document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);backupStatus('All three learning records exported.');
    }catch(error){backupStatus('Export failed: '+error.message);}finally{setBusy('');}
  }
  async function importLibrary(file){
    if(!file||importing||busy)return;importing=true;setBusy('import');backupStatus('Validating the library backup…');
    try{
      if(file.size>8*1024*1024)throw Error('Backup exceeds 8 MB.');
      const value=JSON.parse(await file.text());
      if(value?.format!=='dusky-adobe-library'||value.schema!==1||!value.manuals||typeof value.manuals!=='object'||Array.isArray(value.manuals))throw Error('Choose a Dusky Adobe library backup. Import single-manual backups inside their app.');
      if(value.preferences!==null&&!validPreferences(value.preferences))throw Error('Invalid library reading preferences.');
      if(Object.keys(value.manuals).length!==manuals.length)throw Error('Backup must contain exactly three manuals.');
      for(const m of manuals){const record=value.manuals[m.id];if(!record||record.version!==m.version||!record.state||typeof record.route!=='string'||record.route.length>3000)throw Error('Missing or incompatible '+m.name+' record.');}
      await Promise.all(manuals.map(m=>ensureFrame(m.id)));
      await Promise.all(manuals.map(m=>ask(m.id,'validate',value.manuals[m.id].state)));
      if(!confirm('Replace all three manuals’ progress, bookmarks, notes and reading preferences with this validated library backup?'))return;
      // All validation completes before the first state change; keep the current session for rollback.
      await readAll();const previous=structuredClone(saved);
      try{await Promise.all(manuals.map(m=>ask(m.id,'restore',value.manuals[m.id].state,{route:value.manuals[m.id].route})));}
      catch(error){await Promise.allSettled(manuals.map(m=>ask(m.id,'restore',previous.manuals[m.id].state,{route:previous.manuals[m.id].route})));saved=previous;persist();throw error;}
      for(const m of manuals)saved.manuals[m.id].route=value.manuals[m.id].route;
      saved.preferences=value.preferences;persist();applyLibraryPreferences();
      if(route().name==='settings')workspace.innerHTML=settingsPage();
      backupStatus('All three validated learning records imported.');
    }catch(error){backupStatus('Import rejected: '+error.message);}finally{importing=false;setBusy('');$('import-library').value='';}
  }
  document.addEventListener('click',event=>{
    const action=event.target.closest('[data-action]')?.dataset.action;
    if(action==='more-search'){searchLimit+=40;searchResults();}
    if(action==='more-keys'){compareLimit+=30;compareResults();}
    if(action==='export-library')exportLibrary();
    if(action==='import-library')$('import-library').click();
    if(action==='retry-reader')render();
    if(action==='apply-preferences'){
      if(busy)return;
      saved.preferences=Object.fromEntries([...document.querySelectorAll('[data-library-preference]')].map(x=>[x.dataset.libraryPreference,x.checked]));persist();applyLibraryPreferences();
      for(const [id,f] of frames)if(f.loaded)send(id,{type:'preferences',value:saved.preferences});notify('Reading preferences applied to all three manuals.');
    }
    if(action==='print-manual')send(route().id,{type:'print'});
    if(event.target.closest('.skip')){event.preventDefault();if(route().name==='read'){frames.get(route().id)?.element.focus();send(route().id,{type:'focus'});}else workspace.focus();}
  });
  document.addEventListener('input',event=>{
    if(event.target.id==='library-search'){query=event.target.value;searchLimit=40;clearTimeout(searchUrlTimer);searchUrlTimer=setTimeout(()=>{if(route().name==='search')history.replaceState(null,'','#search'+(query?'/'+encodeURIComponent(query):''));},200);searchResults();}
    if(event.target.id==='compare-search'){compareQuery=event.target.value;compareLimit=30;compareResults();}
  });
  document.addEventListener('change',event=>{
    if(event.target.id==='switcher'){const id=event.target.value;location.hash=id?readLink(id,lastRoute(id)):'#home';}
    if(event.target.id==='app-filter'){appFilter=event.target.value;searchLimit=40;searchResults();}
    if(event.target.id==='kind-filter'){kindFilter=event.target.value;searchLimit=40;searchResults();}
    if(event.target.id==='all-keys'){allKeys=event.target.checked;compareLimit=30;compareResults();}
    if(event.target.id==='import-library')importLibrary(event.target.files[0]);
  });
  document.addEventListener('keydown',event=>{if((event.ctrlKey||event.metaKey)&&event.key.toLowerCase()==='p'&&route().name==='read'){event.preventDefault();send(route().id,{type:'print'});return;}if(event.key==='/'&&!event.ctrlKey&&!event.metaKey&&!event.altKey&&!event.target.matches('input,textarea,select,[contenteditable="true"]')){event.preventDefault();if(route().name==='search')$('library-search')?.focus();else{focusSearch=true;location.hash='#search';}}});
  window.addEventListener('hashchange',()=>{clearTimeout(searchUrlTimer);searchLimit=40;compareLimit=30;render();});
  window.addEventListener('pagehide',()=>{clearTimeout(timer);writeSaved();});
  render();
})();
