# Pattern Foundry Audit Report (March 25, 2026)

## Scope

## Audit Status

- **Status:** Complete
- **Completed on:** 2026-03-25 (UTC)
- **Outcome:** Root cause identified (packaging mismatch), remediation plan documented, and packaged skill hardening work landed in follow-up commits.

This audit reviews why the installed `pattern-foundry` plugin appears to load successfully but produces only the skill description instead of actionable design outputs.

Reviewed areas:
- Marketplace and plugin manifests
- Packaged plugin file tree
- Skill prompt contract quality
- Alignment between repository docs and installed artifact

## Executive Summary

The core issue is a **packaging/portability mismatch**:
- The repository contains a rich engine at `.claude/skills/transferable-uiux-pattern-engine/`.
- The installable plugin package currently ships only a thin `SKILL.md` and `plugin.json`.
- The shipped `SKILL.md` points to deeper materials that are not part of the plugin payload.

Result: Invocation succeeds, but generation quality is shallow and often stalls at high-level instructions.

## Scorecard (10 dimensions)

| Dimension | Score (/10) | Notes |
|---|---:|---|
| Installability | 8 | Plugin installs/reloads successfully. |
| Packaging completeness | 2 | Plugin payload omits design-system docs, samples, and scripts. |
| Skill clarity | 5 | Mode names and templates exist but output contract is too light. |
| Prompt robustness | 4 | Missing strict input schema fallback and completion checklist. |
| Deterministic outputs | 3 | No mandatory output structure per mode in packaged skill. |
| Documentation accuracy | 4 | README promises full engine behavior that plugin package does not include. |
| UX audit quality potential | 6 | Underlying engine is strong, but not actually shipped in plugin path. |
| Safety/originality guardrails | 6 | Present but brief in packaged skill. |
| Maintainer ergonomics | 5 | Repo has rich assets, but split creates confusion in release process. |
| User trust/confidence | 3 | “Installed but no output files” experience feels broken to end users. |

## Top 5 Issues by Impact

1. **Plugin ships only a minimal skill definition**
   - High impact because users install the plugin expecting the full engine.
2. **Packaged skill references materials outside plugin payload**
   - High impact because runtime cannot follow those references in many environments.
3. **No strict output contract in shipped skill**
   - Leads to generic responses rather than concrete specs/diffs/components.
4. **Versioning/release metadata does not reflect capability gaps**
   - Users cannot tell “lite wrapper” vs “full engine” behavior before install.
5. **README positioning over-promises for marketplace install path**
   - Causes expectation mismatch and repeated failed attempts.

## Root Cause Analysis

The repository currently mixes two distribution models:
1. **Full local engine model** (`.claude/skills/transferable-uiux-pattern-engine/`) with deep assets and workflows.
2. **Marketplace plugin model** (`plugins/pattern-foundry/`) with minimal files.

These models are not synchronized at release time, so the marketplace artifact lacks the content needed to behave like the full local engine.

## Recommended Fix Strategy

### Priority 0 (Immediate)
- Make the plugin skill self-sufficient by embedding:
  - explicit mode workflows,
  - mandatory output schema per mode,
  - deterministic checklist before final response.
- Remove/replace references to non-packaged paths unless bundled.

### Priority 1 (Short-term)
- Add a build/release step that copies required engine assets into `plugins/pattern-foundry/` before tagging releases.
- Introduce a packaging validation script that fails CI if referenced files are missing from plugin payload.

### Priority 2 (Medium-term)
- Decide and document product tiers explicitly:
  - **Lite plugin** (single-file guidance), and/or
  - **Full engine plugin** (bundled docs + templates + samples).
- Update README install sections with capability matrix so users choose the right path.

## Implementation Direction (Concrete)

1. Create `plugins/pattern-foundry/skills/pattern-foundry/references/` and include curated minimal assets:
   - `mode-guide.md`
   - `evaluation-rubric.md`
   - `design-system-mini.md`
2. Expand packaged `SKILL.md` with strict output blocks:
   - `AUDIT_MODE` must return: score table, top-5 fixes, upgraded spec, implementation plan.
   - `PAGE_GEN_MODE` must return: IA map, section spec, token map, component map, handoff checklist.
3. Add release check command in CI:
   - Verify all relative links in packaged `SKILL.md` exist under `plugins/pattern-foundry/`.
4. Update README wording to distinguish:
   - “Marketplace install (lightweight)” vs “Repo-local full engine”.

## Verification Checklist After Fix

- Install plugin in a clean environment.
- Invoke `Using pattern-foundry [AUDIT_MODE]:` with a sample UI snippet.
- Confirm output includes all required structured sections.
- Invoke `PAGE_GEN_MODE` and verify non-generic section blueprint is returned.
- Confirm no references to missing paths appear in output.


## Comparison: `ui-ux-pro-max-skill` (inspiration)

Yes — reviewing `https://github.com/nextlevelbuilder/ui-ux-pro-max-skill` is useful here.

What that project does differently (structurally):
- Ships a larger distribution surface (CLI + templates + scripts + source folders) instead of only a thin packaged skill file.
- Documents install and runtime pathways for multiple environments, including explicit commands and generated artifacts.
- Keeps contributor guidance around syncing source assets into distributable locations before release.

What this means for Pattern Foundry:
- Your concept is valid, but your plugin package currently behaves like a lightweight prompt wrapper.
- To match reliability expectations set by larger projects, add a release pipeline that bundles the runtime-critical references and validates packaged paths.
- If you stay prompt-only (no runtime scripts), make that explicit and strengthen deterministic output contracts (already started in packaged SKILL updates).

## Applied Fixes in Repository

- Added `scripts/sync_plugin_engine.py` to copy the full source engine into the packaged plugin path.
- Added bundled engine assets at `plugins/pattern-foundry/skills/pattern-foundry/engine/`.
- Updated packaged `SKILL.md` to load deterministic contracts first, then bundled engine references in a defined read order.
- Added README maintainer instruction for running the sync step before release.

## Conclusion

Your diagnosis is correct: something is missing, and it is primarily **release packaging and output-contract strictness**, not the core concept. The core skill system in the repository is strong; the install artifact needs to ship enough of that system (or clearly scope itself as a lightweight variant).
