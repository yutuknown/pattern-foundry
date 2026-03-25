#!/usr/bin/env python3
"""Verify that marketplace plugin payload contains required engine assets."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'plugins' / 'pattern-foundry' / 'skills' / 'pattern-foundry'

REQUIRED = [
    BASE / 'SKILL.md',
    BASE / 'references' / 'mode-guide.md',
    BASE / 'references' / 'output-contracts.md',
    BASE / 'references' / 'evaluation-rubric.md',
    BASE / 'engine' / 'design-system' / 'MASTER.md',
    BASE / 'engine' / 'design-system' / 'tokens.json',
    BASE / 'engine' / 'templates' / 'tailwind.config.js',
]

missing = [p for p in REQUIRED if not p.exists()]

engine_files = sum(1 for p in (BASE / 'engine').rglob('*') if p.is_file()) if (BASE / 'engine').exists() else 0

if missing:
    print('FAIL: missing required packaged files:')
    for p in missing:
        print(f'- {p.relative_to(ROOT)}')
    print(f'Engine file count: {engine_files}')
    sys.exit(1)

print('OK: packaged plugin contains required engine assets')
print(f'Engine file count: {engine_files}')
