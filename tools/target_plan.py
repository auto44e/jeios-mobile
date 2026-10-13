# SPDX-License-Identifier: Apache-2.0
"""Display native target blockers. Never build, fetch or flash."""
from validate import load, validate

core, registry = load()
validate(core, registry)
print(f"Shared fresh kernel: {core['repository']} @ {core['commit']}")
for t in registry['targets']:
    print(f"{t['id']}: {t['status']}; NOT BUILD/BOOT QUALIFIED")
    for blocker in t['blockers']:
        print(f'  - {blocker}')
