#!/usr/bin/env python3
"""Reproducible self-contained ZIP with SHA-256 manifest; no Internet or packages.
Run: python scripts/package.py --output /path/to/revised.zip
"""
from pathlib import Path
import argparse,hashlib,zipfile,sys
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=ROOT.parent/'Premiere_Explained_Windows_Offline_Manual_26.5.2_Audited_v3.zip')
args=parser.parse_args()
files=sorted((p for p in ROOT.rglob('*') if p.is_file() and p.name not in {'.DS_Store','MANIFEST.sha256'} and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.suffix!='.zip'),key=lambda p:p.relative_to(ROOT).as_posix())
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix()+'\n' for p in files)
(ROOT/'MANIFEST.sha256').write_text(manifest,encoding='utf-8')
files.append(ROOT/'MANIFEST.sha256')
args.output.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(args.output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=8,strict_timestamps=False) as z:
 for p in files:
  arc='Premiere_Explained/'+p.relative_to(ROOT).as_posix()
  info=zipfile.ZipInfo(arc,date_time=(2026,10,28,0,0,0))
  info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=(0o100644<<16)
  info.create_system=3
  z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=8)
with zipfile.ZipFile(args.output) as z:
 if z.testzip() is not None:sys.exit('FAIL: ZIP CRC integrity error')
 names=set(z.namelist());expected={'Premiere_Explained/'+p.relative_to(ROOT).as_posix() for p in files}
 if names!=expected:sys.exit('FAIL: archive file list mismatch')
 for p in files:
  if z.read('Premiere_Explained/'+p.relative_to(ROOT).as_posix())!=p.read_bytes():sys.exit('FAIL: ZIP payload mismatch')
print(f'PASS: {args.output.name} | {len(files)} verified files | {args.output.stat().st_size:,} bytes')
