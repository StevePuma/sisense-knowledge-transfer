#!/usr/bin/env python3
"""Check repository links, skill contracts, NG mappings and obvious credential patterns."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in root.rglob('*') if p.is_file() and not any(x in {'.git', '__pycache__', 'node_modules'} for x in p.relative_to(root).parts)]
patterns = [
    r'https?://[^\s/]+:[^\s/@]+@',
    r'[?&](?:secret|token|api_key)=[A-Za-z0-9_\-]{12,}',
    r'gh[pousr]_[A-Za-z0-9]{20,}',
    r'github_pat_[A-Za-z0-9_]{20,}',
    r'lk-dls-[A-Za-z0-9]{16,}',
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
]
for p in files:
    try:
        text = p.read_text()
    except UnicodeDecodeError:
        errors.append(f'Unexpected binary: {p.relative_to(root)}')
        continue
    if any(re.search(pattern, text) for pattern in patterns):
        errors.append(f'Possible credential: {p.relative_to(root)} (value suppressed)')
    if p.suffix != '.md':
        continue
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('http:', 'https:', '#', 'mailto:')):
            continue
        dest = (p.parent / unquote(target.split('#')[0])).resolve()
        if not dest.is_relative_to(root.resolve()) or not dest.exists():
            errors.append(f'Broken/outside link: {p.relative_to(root)} -> {target}')
    if p.name == 'SKILL.md':
        m = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n', text)
        if not m or m[1] != p.parent.name:
            errors.append(f'Invalid skill frontmatter: {p.relative_to(root)}')
ng = root / 'customers/northrop-grumman'
cfg = json.loads((ng / 'config.snapshot.json').read_text())
schema = json.loads((ng / 'schema.json').read_text())
attrs = {a['path']: a for a in schema['attributes']}
model = cfg['dataModels']['hierarchical']
roles = model['fieldRoles']
for role, field in roles.items():
    key = field if '.' in field else model['dimension'] + '.' + field
    if key not in attrs:
        errors.append(f'Unresolved role: {role} -> {key}')
for mode, data in cfg['hierarchicalViz']['hierarchy'].items():
    for level in data['levels']:
        if level['nameRole'] not in roles:
            errors.append(f'Missing name role: {mode}/{level}')
for mode, tiers in cfg['hierarchicalViz']['riskFieldRoles'].items():
    for tier, metrics in tiers.items():
        for role in metrics.values():
            if role not in roles:
                errors.append(f'Missing metric role: {mode}/{tier}/{role}')
for fields in cfg['hierarchicalViz']['analyticsDashboard']['analyticsFilterFields'].values():
    for path in fields.values():
        if path not in attrs:
            errors.append(f'Missing analytics attribute: {path}')
# These are snapshot assertions: a refresh must update the corresponding case study.
checks = {
    'NG client': cfg['clientId'] == 'ng_subtier_demo',
    'live model': schema['type'] == 'live',
    'matching source': schema['data_source'] == model['dataSourceTitle'],
    'part levels': [x['tier'] for x in cfg['hierarchicalViz']['hierarchy']['parts']['levels']] == list(range(10)),
    'supplier tiers': [x['tier'] for x in cfg['hierarchicalViz']['hierarchy']['suppliers']['levels']] == list(range(1, 11)),
    'dashboard tiers': set(cfg['hierarchicalViz']['analyticsDashboard']['byTier']) == {'1', '2', '3'},
    'no supplier metric mapping': cfg['hierarchicalViz']['riskFieldRoles']['suppliers'] == {},
    'capacity not registered': 'capacity' not in {m['id'] for m in cfg['risk']['metrics']},
}
for name, ok in checks.items():
    if not ok:
        errors.append(f'Snapshot behavior changed; review case study: {name}')
for source in json.loads((ng / 'provenance.json').read_text())['sources']:
    if not re.fullmatch(r'[0-9a-f]{64}', source['sha256']):
        errors.append(f'Invalid source hash: {source["path"]}')
    if source.get('excerpt') and not (ng / source['excerpt']).exists():
        errors.append(f'Missing excerpt: {source["excerpt"]}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(files)} files; local links; 7 skill contracts; {len(roles)} roles; {len(attrs)} attributes; snapshot invariants; credential patterns.')
