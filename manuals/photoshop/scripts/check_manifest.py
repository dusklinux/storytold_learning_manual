"""Write or verify SHA-256 checksums of all shipped project payloads.

Run from any folder: python scripts/check_manifest.py --write or --check.
"""
from pathlib import Path
import hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'MANIFEST.sha256'

def files():
 return [f for f in sorted(ROOT.rglob('*')) if f.is_file() and f.name not in {'MANIFEST.sha256','.DS_Store'} and '__pycache__' not in f.parts and f.suffix not in {'.pyc'} and not f.name.startswith('progress-smoke')]

def record(f):
 h=hashlib.sha256(f.read_bytes()).hexdigest()
 return f'{h}  {f.relative_to(ROOT).as_posix()}'

def main():
 expected='\n'.join(record(f) for f in files())+'\n'
 if sys.argv[1:]==['--write']:
  MANIFEST.write_text(expected,encoding='utf-8');print('WROTE',len(files()),'SHA-256 entries');return
 if sys.argv[1:]==['--check']:
  if not MANIFEST.exists() or expected!=MANIFEST.read_text(encoding='utf-8'):
   print('ERROR: checksum mismatch, missing, or unexpected files; check extraction and rebuild.');sys.exit(1)
  print('PASS:',len(files()),'SHA-256 entries match');return
 sys.exit('Usage: python scripts/check_manifest.py --write|--check')
if __name__=='__main__':main()
