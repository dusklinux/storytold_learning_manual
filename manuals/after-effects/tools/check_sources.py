#!/usr/bin/env python3
"""Record HTTP provenance; this does not certify the truth of page contents."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import content


def check(entry):
    key, source = entry
    try:
        request = urllib.request.Request(source['url'], headers={'User-Agent': 'AE-Offline-Manual-Source-Check/2'})
        with urllib.request.urlopen(request, timeout=25) as response:
            payload = response.read()
            return {'source': key, 'url': source['url'], 'resolvedURL': response.url,
                    'status': response.status, 'bytes': len(payload),
                    'sha256': hashlib.sha256(payload).hexdigest()}
    except Exception as error:
        return {'source': key, 'url': source['url'], 'status': 'unavailable', 'error': str(error)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'data/source_checks.json')
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        records = list(pool.map(check, ((k, v) for k, v in content.SOURCES.items() if v['url'])))
    args.output.write_text(json.dumps({'checkedAt': datetime.datetime.now(datetime.UTC).isoformat(),
        'method': 'HTTP GET; status and hash establish retrieval only. Facts require editorial comparison; see AUDIT.md.',
        'sources': records}, indent=2)+'\n', encoding='utf-8')
    for record in records:
        print(record['source'], record['status'])


if __name__ == '__main__':
    main()
