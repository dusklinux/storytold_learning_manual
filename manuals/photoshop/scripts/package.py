"""Produce deterministic single ZIP, including sources, tests, and SHA-256 manifest.

Run after build and tests: python scripts/check_manifest.py --write; python scripts/package.py.
"""
from pathlib import Path
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
import sys
from check_manifest import files,ROOT,MANIFEST
out=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT.parent/'Photoshop_Field_Manual_Windows_Offline_27.11_v1.2.zip'
if not MANIFEST.exists():raise SystemExit('Create MANIFEST.sha256 first')
with ZipFile(out,'w') as z:
 for path in sorted(files()+[MANIFEST]):
  arc='Photoshop_Field_Manual/'+path.relative_to(ROOT).as_posix()
  info=ZipInfo(arc,date_time=(2026,10,28,0,0,0))
  info.compress_type=ZIP_DEFLATED;info.external_attr=0o644<<16
  z.writestr(info,path.read_bytes(),compresslevel=9)
print('WROTE',out,'entries',len(files())+1,'bytes',out.stat().st_size)
