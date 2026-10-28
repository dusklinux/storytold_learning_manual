/* A small message protocol keeps file:// readers independent of shared-origin rules. */
(() => {
  'use strict';
  const adapter = window.ManualAdapter;
  if (!adapter) return;
  if (window.parent === window) {
    const link = document.createElement('a');
    link.href = '../../index.html';
    link.textContent = '← Dusky Adobe Manual · choose another app';
    link.className='library-return';
    link.style.cssText = 'display:block;padding:12px 18px;background:#212e29;color:#fff;font:14px system-ui;text-decoration:none;position:fixed;bottom:16px;right:16px;border-radius:8px;box-shadow:0 2px 12px #0003;z-index:100';
    const style=document.createElement('style');style.textContent='@media print{.library-return{display:none!important}}';document.head.append(style);
    document.body.prepend(link);
    return;
  }
  let initialized = false, last = '', scheduled = false;
  const send = value => parent.postMessage({channel:'dusky-manual-v1', app:adapter.id, ...value}, '*');
  const route = () => location.hash.replace(/^#\/?/, '') || adapter.home;
  function publish() {
    if (!initialized) return;
    const status = {state:adapter.get(), route:route(), progress:adapter.progress(), storage:adapter.storage()};
    const key = JSON.stringify(status);
    if (key !== last) { last = key; send({type:'snapshot', ...status}); }
  }
  window.manualChanged = () => {
    if (scheduled) return;
    scheduled = true;
    queueMicrotask(() => {scheduled = false; publish();});
  };
  function navigate(value) {
    const hash = '#' + (adapter.id === 'photoshop' ? '/' : '') + value;
    if (location.hash !== hash) {
      history.replaceState(null, '', hash);
      window.dispatchEvent(new HashChangeEvent('hashchange'));
    }
    publish();
  }
  window.addEventListener('message', event => {
    if (event.source !== parent || event.data?.channel !== 'dusky-library-v1') return;
    const m = event.data;
    try {
      if (m.type === 'initialize') {
        if (m.state) {
          try {adapter.set(adapter.validate(m.state));}
          catch (error) {send({type:'warning',error:'Saved library progress was invalid; the reader’s own record was retained. '+error.message});}
        }
        if (m.preferences) adapter.preferences(m.preferences);
        initialized = true;
        if (m.route) navigate(m.route);
        publish();
      } else if (m.type === 'navigate') navigate(m.route);
      else if (m.type === 'preferences') {adapter.preferences(m.value); publish();}
      else if (m.type === 'validate') {
        adapter.validate(m.value);
        send({type:'response', request:m.request, ok:true});
      } else if (m.type === 'restore') {
        adapter.set(adapter.validate(m.value)); publish();
        send({type:'response', request:m.request, ok:true});
      } else if (m.type === 'print') window.print();
    } catch (error) {send({type:'response', request:m.request, ok:false, error:error.message});}
  });
  document.addEventListener('click', event => {
    const link=event.target.closest('a[href]');
    if(link&&/^https?:/.test(link.href)){link.target='_blank';link.rel='noopener noreferrer';}
  }, true);
  // Keep one parent history entry per link; native readers retain their hash routers.
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link || event.ctrlKey || event.metaKey || event.altKey || event.shiftKey || event.button !== 0 || link.target === '_blank' || link.classList.contains('skip') || link.id === 'skipContent' || link.id === 'skip-link') return;
    const value = link.getAttribute('href').replace(/^#\/?/, '');
    // Markdown guide fragments are document anchors, not application routes.
    if (adapter.id === 'premiere' && link.closest('.guide-article')) return;
    event.preventDefault();
    send({type:'navigate', route:value || adapter.home});
  }, true);
  document.addEventListener('keydown', event => {if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'p') {event.preventDefault();window.print();}});
  window.addEventListener('hashchange', publish);
  document.addEventListener('change', window.manualChanged);
  document.addEventListener('input', window.manualChanged);
  document.addEventListener('click', window.manualChanged);
  send({type:'ready'});
})();
