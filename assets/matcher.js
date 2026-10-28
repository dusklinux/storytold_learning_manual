/* Offline title abbreviations plus full-text matching; no runtime dependencies. */
(() => {
  'use strict';
  const fold=text=>String(text).normalize('NFD').replace(/\p{M}/gu,'').toLowerCase();
  function titleIndex(text){
    let value='',offset=0;const positions=[];
    for(const character of text){const normalized=fold(character);value+=normalized;for(let i=0;i<normalized.length;i++)positions.push(offset);offset+=character.length;}
    return {value,positions};
  }
  function prepare(records,names){return records.map((record,order)=>({record,order,title:titleIndex(record.title),body:fold(record.body),context:fold((names[record.app]||record.app)+' '+record.kind)}));}
  function fuzzy(text,token){
    if(token.length<3)return null;
    let best=null;
    // Try each start so an early loose match cannot hide a later compact match.
    for(let start=text.indexOf(token[0]);start>=0;start=text.indexOf(token[0],start+1)){
      let at=start;const positions=[at];
      for(let i=1;i<token.length;i++){at=text.indexOf(token[i],at+1);if(at<0)break;positions.push(at);}
      if(positions.length!==token.length)continue;
      const span=at-start+1;
      if(span>token.length*3+4)continue;
      const score=200-(span-token.length)*5-Math.min(start,40)+(!start||/[^\p{L}\p{N}]/u.test(text[start-1])?25:0);
      if(!best||score>best.score)best={score,positions};
    }
    return best;
  }
  function search(index,query,app='',kind=''){
    const phrase=fold(query).trim(),tokens=[...new Set(phrase.split(/\s+/u).filter(Boolean))];
    if(!tokens.length)return [];
    const results=[];
    for(const item of index){
      if(app&&item.record.app!==app||kind&&item.record.kind!==kind)continue;
      let score=0,matched=true,titleOnly=true;const positions=new Set();
      for(const token of tokens){
        const at=item.title.value.indexOf(token);
        if(at>=0){score+=400;for(let i=at;i<at+token.length;i++)positions.add(item.title.positions[i]);continue;}
        const abbreviation=fuzzy(item.title.value,token);
        if(abbreviation){score+=abbreviation.score;for(const i of abbreviation.positions)positions.add(item.title.positions[i]);continue;}
        titleOnly=false;
        if(item.body.includes(token)||item.context.includes(token)){score+=10;continue;}
        matched=false;break;
      }
      if(!matched)continue;
      if(item.title.value===phrase)score+=4000;
      else if(item.title.value.includes(phrase))score+=2000;
      if(titleOnly)score+=500;
      results.push({record:item.record,score,positions,order:item.order});
    }
    return results.sort((a,b)=>b.score-a.score||a.order-b.order);
  }
  function literalPositions(text,query){
    const indexed=titleIndex(text),positions=new Set();
    for(const token of fold(query).trim().split(/\s+/u).filter(Boolean)){
      for(let at=indexed.value.indexOf(token);at>=0;at=indexed.value.indexOf(token,at+token.length))for(let i=at;i<at+token.length;i++)positions.add(indexed.positions[i]);
    }
    return positions;
  }
  window.LibrarySearchEngine={fold,prepare,search,literalPositions};
})();
