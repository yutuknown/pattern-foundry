#!/usr/bin/env python3
"""Sync transferable-uiux-pattern-engine assets into the packaged marketplace skill.

This keeps the installable plugin payload self-contained so marketplace installs
include the same design-system knowledge files, templates, docs, and samples that
exist in the repository source skill.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '.claude' / 'skills' / 'transferable-uiux-pattern-engine'
TARGET = ROOT / 'plugins' / 'pattern-foundry' / 'skills' / 'pattern-foundry' / 'engine'

EXCLUDE_NAMES = {
    '__pycache__',
}


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)

    def _ignore(path: str, names: list[str]) -> set[str]:
        return {name for name in names if name in EXCLUDE_NAMES}

    shutil.copytree(src, dst, ignore=_ignore)


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f'Source skill not found: {SOURCE}')

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    copy_tree(SOURCE, TARGET)

    file_count = sum(1 for p in TARGET.rglob('*') if p.is_file())
    print(f'Synced {file_count} files to {TARGET.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
