'use strict';
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'..'),context={window:{}};vm.createContext(context);
for(const file of ['assets/matcher.js','assets/search.js','assets/catalog.js'])vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'),context);
const engine=context.window.LibrarySearchEngine,records=context.window.LIBRARY_SEARCH;
const index=engine.prepare(records,Object.fromEntries(context.window.LIBRARY_MANUALS.map(x=>[x.id,x.name])));
function search(q,app='',kind=''){return engine.search(index,q,app,kind);}
for(const [q,title] of [['gsblur','Gaussian Blur'],['gausian blur','Gaussian Blur'],['curvs','Curves']]){
 const result=search(q);assert(result.length,q);assert(result.slice(0,5).some(x=>x.record.title.includes(title)),q);assert(result[0].positions.size,q);
}
for(const app of ['photoshop','premiere','after-effects']){
 const result=search('alpha',app);assert(result.length);assert(result.every(x=>x.record.app===app));
}
assert(search('1001','','Field guide').length);
assert(search('Ctrl+S','','Shortcut').length>=3);
assert.equal(search('zzqqxxvvzzqqxxvv').length,0);assert.equal(search('   ').length,0);
assert.equal(search('Gaussian Blur')[0].record.title,'Gaussian Blur');
const synthetic=engine.prepare([{app:'a',kind:'Term',title:'Résumé 🌈',body:'café'},{app:'a',kind:'Lesson',title:'Other',body:'Résumé'}],{});
assert.equal(engine.search(synthetic,'resume')[0].record.title,'Résumé 🌈');
assert.equal(engine.search(synthetic,'cafe').length,1);
assert.equal(engine.literalPositions('Résumé','resume').size,6);
// Literal full-text results are never lost when fuzzy titles are added.
for(const q of ['alpha','mask','color','ripple','1001','Ctrl+S','GPU','export']){
 const tokens=q.toLowerCase().split(/\s+/);const before=records.filter(x=>tokens.every(t=>(x.title+' '+x.body).toLowerCase().includes(t)));
 const after=new Set(search(q).map(x=>x.record));assert(before.every(x=>after.has(x)),q);
}
const samples=[];for(let i=0;i<45;i++){const start=performance.now();search(['mask','gsblur','color','gausian blur','zzqqxxvv'][i%5]);samples.push(performance.now()-start);}
samples.sort((a,b)=>a-b);console.log(`PASS ranking, abbreviations, exact/full-text retention, filters, Unicode, empty/no-match; ${records.length} records; median ${samples[22].toFixed(2)} ms, max ${samples.at(-1).toFixed(2)} ms (Node fixture)`);
