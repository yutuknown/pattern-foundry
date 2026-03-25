# Release Checklist: v0.1.1

This checklist ensures that all repositories, documentation, and metadata are ready for the public OSS launch and follow-up patch release cycle of Pattern Foundry.

## Pre-Release

- [x] Ensure all Python scripts (`inspect_site.py`, `extract_tokens.py`, etc.) run without throwing unhandled exceptions.
- [x] Verify that `tokens.json` parses correctly.
- [x] Run a final brand-leakage scan across `samples/` and `templates/` to ensure no source site naming remains.
- [x] Ensure `.gitignore` successfully excludes `.claude/settings.local.json`, `node_modules`, `__pycache__`, and raw Playwright extraction data.
- [x] Confirm all `[nooaeclipse]` and `[REPO]` placeholders in `README.md` have been updated with the actual GitHub organization and repository name.
- [x] Replace the placeholder `LICENSE` file with the official MIT or Apache 2.0 license text.

## Launch

- [x] Create a GitHub Release referencing `release-notes/v0.1.1.md`.
- [x] Publish the release and verify the associated Git tag (`v0.1.1`).
- [x] Update the repository "About" section, website URL, and tags (topics) on GitHub.
- [x] Confirm the latest release is **v0.1.1** and all launch items are completed.

## Post-Release

- [ ] Monitor the issue tracker for early bug reports.
- [ ] Announce the release on relevant community channels (e.g., Anthropic Developer Discord, Reddit, X/Twitter).
