#!/usr/bin/env python3
"""Check every released file against the SHA-256 manifest. Standard library only."""
from pathlib import Path
import hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
manifest=ROOT/'MANIFEST.sha256'
if not manifest.is_file():sys.exit('FAIL: MANIFEST.sha256 missing')
rows={}
for row in manifest.read_text(encoding='utf-8').splitlines():
 if not row.strip():continue
 digest,sep,path=row.partition('  ')
 if len(digest)!=64 or not sep or not path or path in rows:sys.exit('FAIL: malformed manifest line')
 rows[path]=digest
skip={'.DS_Store','MANIFEST.sha256'}
actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name not in skip and '__pycache__' not in p.parts and not p.suffix=='.pyc'}
if set(rows)!=actual:
 sys.exit('FAIL: manifest entry mismatch: missing '+str(sorted(actual-set(rows)))+' extra '+str(sorted(set(rows)-actual)))
for name,digest in rows.items():
 p=ROOT/name
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:sys.exit('FAIL: checksum mismatch '+name)
print('PASS MANIFEST.sha256:',len(rows),'files match, no unlisted payload files')
