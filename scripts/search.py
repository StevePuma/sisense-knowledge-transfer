#!/usr/bin/env python3
"""Search curated text and schema without dependencies or network access."""
import argparse
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('query')
p.add_argument('--limit', type=int, default=30)
a = p.parse_args()
if not a.query.strip() or a.limit < 1:
    p.error('Provide a nonempty query and positive limit')
needle = a.query.casefold()
hits = 0
for path in sorted(root.rglob('*')):
    rel = path.relative_to(root)
    if any(part in {'.git', 'node_modules', '__pycache__'} for part in rel.parts):
        continue
    if path.suffix not in {'.md', '.json'} or not path.is_file():
        continue
    if path.name == 'schema.json':
        for field in json.loads(path.read_text())['attributes']:
            if needle in json.dumps(field).casefold():
                print(f'{rel}: {field["path"]} ({field["type"]}); original model line {field["source_line"]}')
                hits += 1
                if hits >= a.limit:
                    raise SystemExit(0)
        continue
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if needle in line.casefold():
            print(f'{rel}:{n}: {line.strip()}')
            hits += 1
            if hits >= a.limit:
                raise SystemExit(0)
if not hits:
    print('No matching knowledge found.')
