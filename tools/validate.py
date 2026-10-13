# SPDX-License-Identifier: Apache-2.0
"""Validate the planning scaffold, not kernel or device readiness."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(core, registry):
    if core.get('schema') != 1 or registry.get('schema') != 1:
        raise ValueError('unsupported schema')
    if core.get('kernel') != 'jeios-fresh-c' or core.get('arm64_ready') is not False:
        raise ValueError('scaffold must not claim ARM64 execution or another kernel')
    if not re.fullmatch(r'[0-9a-f]{40}', core.get('commit', '')):
        raise ValueError('core requires an immutable commit')
    targets = registry.get('targets')
    if not isinstance(targets, list) or not targets:
        raise ValueError('targets required')
    seen = set()
    for t in targets:
        name = t.get('id')
        if not isinstance(name, str) or not name or name in seen:
            raise ValueError('invalid or duplicate target')
        seen.add(name)
        if t.get('kernel') != 'jeios-fresh-c' or t.get('lunch') is not None:
            raise ValueError('fresh-kernel targets cannot claim Android lunch products')
        if t.get('status') not in ('planned', 'research'):
            raise ValueError('execution readiness needs a new evidence schema')
        if t.get('architecture') != 'aarch64':
            raise ValueError('unexpected architecture')
        if not isinstance(t.get('blockers'), list) or not t['blockers'] or not all(isinstance(x, str) and x.strip() for x in t['blockers']):
            raise ValueError('unqualified targets must record blockers')


def load():
    return tuple(json.loads((ROOT / 'config' / name).read_text())
                 for name in ('core.json', 'targets.json'))


def check_links():
    for p in ROOT.rglob('*.md'):
        if '.git' in p.parts:
            continue
        for link in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            if '://' not in link and not link.startswith('#'):
                if not (p.parent / link.split('#')[0]).exists():
                    raise ValueError(f'{p}: missing {link}')


if __name__ == '__main__':
    validate(*load())
    check_links()
    print('PASS: planning manifests and relative links; no boot/device claim')
