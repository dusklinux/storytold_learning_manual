#!/usr/bin/env python3
"""Rebuild structured course data, CSV/Markdown, and bundled field guides from first-party sources.
Run: python scripts/rebuild.py. Requires the standard library and `mistune` for guide Markdown-to-HTML.
This is a maintenance utility; *reading* the manual has zero runtime dependencies.
"""
from pathlib import Path
import subprocess,sys
HERE=Path(__file__).parent
for name in ('build_content.py','build_guides.py','build_project_docs.py'):
 p=subprocess.run([sys.executable,str(HERE/name)],check=True)
print('Content and guides rebuilt. Run scripts/validate.py before redistribution.')
