#!/usr/bin/env python3
"""Bundle first-party Markdown field guides as static HTML usable from file://.
Requires mistune only when rebuilding; the published manual has no dependencies.
"""
from pathlib import Path
import json,re
import mistune
ROOT=Path(__file__).resolve().parent.parent
result=[]
for f in sorted((ROOT/'guides').glob('*.md')):
    body=f.read_text(encoding='utf-8')
    head=body.splitlines()[0].lstrip('# ').strip()
    title=head.split(' — ',1)[-1]
    preview=re.sub(r'[#*`\[\]]','',body)
    summary=re.sub(r'\s+',' ',preview).strip()[0:220]
    renderer=mistune.create_markdown(escape=True,plugins=['table'])
    result.append({'id':f.stem,'title':title,'filename':str(f.relative_to(ROOT)),
                   'markdown':body,'html':renderer(body),'description':summary})
(ROOT/'data'/'guides.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'guides.js').write_text('window.PREMIERE_GUIDES = '+json.dumps([{'id':x['id'],'title':x['title'],'filename':x['filename'],'html':x['html'],'description':x['description']} for x in result],ensure_ascii=False)+';\n',encoding='utf-8')
# The full text edition is made from the course builder; replace any prior guide section on repeat runs.
allfile=ROOT/'ALL_CONTENT.md'
if allfile.exists():
 text=allfile.read_text(encoding='utf-8')
 text=text.split('\n\n# FIELD GUIDES (COMPLETE TEXT)')[0]
 text+='\n\n# FIELD GUIDES (COMPLETE TEXT)\n'
 for g in result:
  text+='\n\n---\n\n'+g['markdown'].strip()+'\n'
 allfile.write_text(text,encoding='utf-8')
print(f'Bundled {len(result)} field guides in guides.js and ALL_CONTENT.md')
