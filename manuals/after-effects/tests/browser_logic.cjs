/* Offline app logic smoke test with a minimal DOM mock; no browser engine required. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const DATA=JSON.parse(fs.readFileSync(path.join(root,'manual_data.json'),'utf8'));
const elements={
 guideData:{textContent:JSON.stringify(DATA)},
 main:{innerHTML:'',addEventListener(){},querySelector(){return null},querySelectorAll(){return []}},
 nav:{innerHTML:''},
 toggleMenu:{setAttribute(){},addEventListener(){}},
 globalSearch:{value:'',addEventListener(){},focus(){},setSelectionRange(){}}
};
let storage={};const mockClassList={toggle(){},remove(){},contains(){return false}};
const ctx={
 document:{title:'',querySelector(){return null},getElementById(id){return elements[id]??null},body:{classList:mockClassList},addEventListener(){}},
 window:{scrollTo(){},addEventListener(){}},
 localStorage:{getItem(k){return storage[k]??null},setItem(k,v){storage[k]=v}},
 location:{hash:''},history:{replaceState(){}},
 console,Number,Math,Date,JSON,encodeURIComponent,decodeURIComponent,Array,Set,Map,URL,
 confirm(){return true},alert(){},setTimeout(){}
};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root,'web/app.js'),'utf8'),ctx,{timeout:5000});
assert.match(elements.main.innerHTML,/Learn the system/);
const visit=(route)=>{
 ctx.location.hash='#'+route;
 vm.runInContext('render(false)',ctx,{timeout:5000});
 assert.ok(elements.main.innerHTML.length>200,'Empty view '+route);
};
for(const route of ['home','lessons','topics','recipes','effects','shortcuts','troubleshoot','glossary','quiz','lab','audit','settings'])visit(route);
for(const ch of DATA.chapters){visit('lesson/'+ch.id);assert.ok(elements.main.innerHTML.includes(ch.title))}
for(const topic of DATA.topics){visit('topic/'+topic.id);assert.ok(elements.main.innerHTML.includes(topic.title))}
for(const recipe of DATA.recipes){visit('recipe/'+recipe.id);assert.ok(elements.main.innerHTML.includes(recipe.title))}
visit('search/'+encodeURIComponent('graph editor'));
assert.ok(elements.main.innerHTML.includes('Graph Editor'));
visit('lesson/'+DATA.chapters[0].id);
vm.runInContext(`updateStep('${DATA.chapters[0].id}:0',true)`,ctx,{timeout:5000});
assert.ok(JSON.parse(storage['ae_26_5_windows_manual_progress_v2']).steps[DATA.chapters[0].id+':0']);
visit('quiz');vm.runInContext('updateQuiz(0,1)',ctx,{timeout:5000});
assert.equal(JSON.parse(storage['ae_26_5_windows_manual_progress_v2']).answers[0],1);
ctx.location.hash='#%bad%zz';vm.runInContext('render(false)',ctx,{timeout:5000});
assert.match(elements.main.innerHTML,/Learn the system/);
console.log(`PASS: ${12+DATA.chapters.length+DATA.topics.length+DATA.recipes.length+2} routes, search, step state, quiz state, malformed URL hash`);

const old={manualVersion:'25.6',edition:1,steps:{'logic:0':true,'install:0':true,'color:4':true,'advanced3d:5':true},answers:{'0':1,'1':2}};
ctx.old=old;
assert.equal(vm.runInContext("JSON.stringify(normalizedProgress(old,true).steps)",ctx),'{'+'"logic:0":true}');
assert.equal(vm.runInContext("Object.keys(normalizedProgress(old,true).answers).length",ctx),1);
for(const bad of [null,[],{version:'26.5',edition:2,steps:[]},{version:'26.5',edition:2,steps:{'logic:999':true}},{version:'26.5',edition:2,steps:{},answers:[]},{version:'26.5',edition:2,steps:{},large:'yes'}]){
 ctx.bad=bad;assert.throws(()=>vm.runInContext('normalizedProgress(bad)',ctx));
}
console.log('PASS: legacy migration and malformed progress rejection');
