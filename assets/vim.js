/* Optional, shared navigation. Editing controls always retain their ordinary keys. */
(() => {
 'use strict';
 let enabled=false;
 try{enabled=localStorage.getItem('dusky-adobe-vim')==='true';}catch{}
 function set(value){value=value===true;if(value===enabled)return;enabled=value;try{localStorage.setItem('dusky-adobe-vim',String(value));}catch{}document.dispatchEvent(new CustomEvent('vim-change',{detail:value}));}
 function scroll(key){const page=document.scrollingElement;if(!page)return;if(key==='g'||key==='G')window.scrollTo({top:key==='g'?0:page.scrollHeight,behavior:'instant'});else window.scrollBy({top:key==='j'?70:-70,behavior:'instant'});}
 window.ManualVim={enabled:()=>enabled,set,scroll};
 document.addEventListener('keydown',event=>{
  if(event.isComposing||event.defaultPrevented)return;
  if(event.altKey&&!event.ctrlKey&&!event.metaKey&&event.key.toLowerCase()==='m'){event.preventDefault();event.stopImmediatePropagation();set(!enabled);return;}
  if(!enabled||event.ctrlKey||event.altKey||event.metaKey)return;
  const target=event.target,editing=target.closest('input,textarea,select,[contenteditable]:not([contenteditable="false"]),[role="textbox"]');
  const results=[...document.querySelectorAll('#search-results .result')];
  if(editing){
   if(event.key==='Escape'&&target.id==='library-search'){
    event.preventDefault();event.stopImmediatePropagation();(results[0]||document.getElementById('workspace')).focus();
   }
   return;
  }
  if(!['j','k','g','G','/','h','l'].includes(event.key)||event.shiftKey&&event.key!=='G')return;
  event.preventDefault();event.stopImmediatePropagation();
  if(event.key!=='/'&&!document.dispatchEvent(new CustomEvent('vim-card',{detail:event.key,cancelable:true})))return;
  if(event.key==='/'){document.dispatchEvent(new Event('vim-search'));return;}
  if(event.key==='h'||event.key==='l'){if(event.repeat)return;document.dispatchEvent(new CustomEvent('vim-step',{detail:event.key==='l'?1:-1}));return;}
  if(results.length){
   const at=results.indexOf(document.activeElement);
   const next=event.key==='g'?0:event.key==='G'?results.length-1:event.key==='j'?Math.min(results.length-1,at+1):Math.max(0,at<0?results.length-1:at-1);
   results[next].focus();return;
  }
  if(document.dispatchEvent(new CustomEvent('vim-scroll',{detail:event.key,cancelable:true})))scroll(event.key);
 },true);
})();
