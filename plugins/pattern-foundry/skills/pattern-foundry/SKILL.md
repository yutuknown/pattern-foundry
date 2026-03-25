---
name: pattern-foundry
description: Generate original premium UI/UX using Pattern Foundry modes (NEW_BRAND_MODE, AUDIT_MODE, PAGE_GEN_MODE, TEMPLATE_MODE, SYSTEM_EXPAND_MODE)
---

# Pattern Foundry

Use this skill when the user wants high-quality UI/UX generation, audits, or design-system expansion.

## Invocation Format
Start prompts with:

`Using pattern-foundry [MODE]:`

Supported modes:
- `NEW_BRAND_MODE`
- `AUDIT_MODE`
- `PAGE_GEN_MODE`
- `TEMPLATE_MODE`
- `SYSTEM_EXPAND_MODE`

## Required Behavior
- Produce original output; never clone source-brand identity.
- Keep strong hierarchy, spacing discipline, and clear CTA logic.
- Include accessibility defaults (`focus-visible`, semantic landmarks, reduced motion support).
- Prefer token-driven decisions over arbitrary values.

## Prompt Templates

```text
Using pattern-foundry [NEW_BRAND_MODE]:
Brand: <name>
Industry: <industry>
Audience: <target users>
Tone: <tone>
Stack: <framework + styling>
Generate: <deliverable>
```

```text
Using pattern-foundry [AUDIT_MODE]:
[Paste existing UI code/spec]
Score it on 10 dimensions.
List top 5 issues by impact.
Provide upgraded spec and implementation direction.
```

## Notes
For full methodology and deeper artifacts, use this repository's `.claude/skills/transferable-uiux-pattern-engine/` materials.
