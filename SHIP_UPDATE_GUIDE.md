# Ship Update Guide (Pattern Foundry)

Use this checklist to publish the changes from your local branch to the real GitHub repo and marketplace consumers.

## 1) Confirm local branch has the fixes

```bash
git checkout work
git log --oneline -n 5
python3 scripts/verify_packaged_plugin.py
```

Expected: `OK: packaged plugin contains required engine assets`.

## 2) Configure remote and authenticate

```bash
git remote add origin https://github.com/yutuknown/pattern-foundry.git 2>/dev/null || true
git remote -v
```

If HTTPS pushes ask for credentials, use a GitHub Personal Access Token (classic: `repo` scope).

## 3) Push branch with all commits

```bash
git push -u origin work
```

If push is rejected because branch protection requires PR, continue to step 4.

## 4) Open Pull Request

Create PR: `work` -> `master` (or `main`, whichever is default).

Recommended PR title:

`Bundle full engine into packaged plugin + add sync/verify release checks`

## 5) Merge and tag release

After PR merge:

```bash
git checkout master
git pull origin master
git tag -a v0.1.2 -m "Bundle packaged engine + add release verification"
git push origin v0.1.2
```

## 6) Create GitHub Release notes

In GitHub Releases, draft `v0.1.2` and include:
- packaged engine added under `plugins/pattern-foundry/skills/pattern-foundry/engine/`
- `scripts/sync_plugin_engine.py`
- `scripts/verify_packaged_plugin.py`
- deterministic output contracts in packaged `SKILL.md`

## 7) Validate from a clean Claude environment

In Claude Code:

```text
/plugin marketplace add https://github.com/yutuknown/pattern-foundry.git
/plugin install pattern-foundry@pattern-foundry
/reload-plugins
```

Then run an audit invocation and verify structured output sections are returned.

## Troubleshooting

- `CONNECT tunnel failed, response 403` on push:
  - indicates network/proxy restriction in your runtime; push from your local machine with normal GitHub access.
- `permission denied` on push:
  - ensure repo access and PAT scope.
- plugin still old after release:
  - bump plugin `version` in manifests and reinstall/reload plugins.
