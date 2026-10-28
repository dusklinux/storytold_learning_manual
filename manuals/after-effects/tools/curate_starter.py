#!/usr/bin/env python3
"""Inspect a Markdown coverage seed without replacing durable curated catalog IDs.

A note is an editorial input, not a source of version truth. This tool prints its
headings and table-row counts for coverage comparison. Edit content.py/data by
hand after checking Adobe's stable release and feature-specific documentation.
"""
import argparse
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--notes',required=True,type=Path)
    args=parser.parse_args()
    rows=0
    for line in args.notes.read_text(encoding='utf-8').splitlines():
        if line.startswith('#'):
            if rows:print(f'  {rows} table lines')
            print(line);rows=0
        elif line.startswith('|'):rows+=1
    if rows:print(f'  {rows} table lines')


if __name__=='__main__':main()
