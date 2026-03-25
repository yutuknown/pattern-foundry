# Release Checklist: v0.2.1 (In Progress)

This checklist governs the next Pattern Foundry release. Reset all checkboxes for a new cycle so nothing is skipped.

## Pre-Release

- [ ] Ensure all Python scripts (`inspect_site.py`, `extract_tokens.py`, etc.) run without throwing unhandled exceptions.
- [ ] Verify that `design-system/tokens.json` parses correctly.
- [ ] Run a brand-leakage scan across `samples/` and `templates/` to ensure no source site naming remains.
- [ ] Confirm `.gitignore` excludes `.claude/settings.local.json`, `node_modules`, `__pycache__`, raw manual audit data, and `.agent/`.
- [ ] Confirm README + assets (`assets/readme/*`) reflect current workflows and diagrams.
- [ ] Verify all docs under `docs/audits/` and `docs/releases/` reference current paths/version numbers.

## Launch

- [ ] Run `python3 scripts/sync_plugin_engine.py` followed by `python3 scripts/verify_packaged_plugin.py` on the release commit.
- [ ] Create a GitHub Release referencing `release-notes/v0.2.1.md`.
- [ ] Publish the release and verify the associated Git tag (`v0.2.1`).
- [ ] Update the repository "About" section, website URL, and tags (topics) on GitHub (if needed).
- [ ] Confirm the latest release entry on GitHub is **v0.2.1** with correct notes.

## Post-Release

- [ ] Monitor the issue tracker for early bug reports.
- [ ] Announce the release on relevant community channels (e.g., Anthropic Developer Discord, Reddit, X/Twitter).
- [ ] Archive the completed checklist (commit or tag) before starting the next version.
