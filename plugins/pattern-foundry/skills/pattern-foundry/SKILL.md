---
name: pattern-foundry
description: Generate original premium UI/UX using Pattern Foundry modes (NEW_BRAND_MODE, AUDIT_MODE, PAGE_GEN_MODE, TEMPLATE_MODE, SYSTEM_EXPAND_MODE)
---

# Pattern Foundry (Packaged Skill)

Use this skill for UI/UX generation, audits, and design-system expansion.

> This packaged marketplace skill is intentionally prompt-driven. It should still return structured, implementation-ready outputs in chat even when no external generator/MCP server is present.

## Invocation Format
Start prompts with:

`Using pattern-foundry [MODE]:`

Supported modes:
- `NEW_BRAND_MODE`
- `AUDIT_MODE`
- `PAGE_GEN_MODE`
- `TEMPLATE_MODE`
- `SYSTEM_EXPAND_MODE`

---

## Non-Negotiable Behavior

1. Produce original output; never clone source-brand identity.
2. Keep strong hierarchy, spacing discipline, and clear CTA logic.
3. Include accessibility defaults (`focus-visible`, semantic landmarks, reduced motion support).
4. Prefer token-driven decisions over arbitrary values.
5. If inputs are partial, infer conservatively and list assumptions explicitly.
6. Never stop at “skill instructions only” — always produce concrete deliverables for the requested mode.

---

## Required Output Contracts (Deterministic)

### AUDIT_MODE (must output all sections)
1. **Scorecard (10 dimensions)**: table with score (/10), evidence, and impact.
2. **Top 5 issues by impact**: ranked with severity and user/business consequence.
3. **Upgraded spec**: revised IA/layout, token updates, component updates.
4. **Implementation plan**: phased tasks with effort/risk and acceptance criteria.
5. **Quick wins in 60 minutes**: minimum 3 concrete actions.

### PAGE_GEN_MODE (must output all sections)
1. **Page objective and target user**
2. **Section-by-section blueprint**
3. **Token map** (color/type/spacing/radius/motion)
4. **Component map** (states + interactions)
5. **Build handoff** (semantic HTML/Tailwind-ready structure + checklist)

### NEW_BRAND_MODE (must output all sections)
1. Brand adaptation assumptions
2. Token palette with semantic roles
3. Homepage structure + CTA rhythm
4. Component grammar + motion rules
5. Implementation checklist

### TEMPLATE_MODE (must output all sections)
1. Generic reusable structure
2. Placeholder copy model
3. Token defaults and variant knobs
4. Accessibility baseline
5. Reuse instructions

### SYSTEM_EXPAND_MODE (must output all sections)
1. Existing system constraints
2. New page/feature fit analysis
3. Minimal override spec
4. Integration risks and mitigations
5. Regression checklist

---

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

```text
Using pattern-foundry [PAGE_GEN_MODE]:
Page: <page type>
Product: <product>
Audience: <target users>
Tone: <tone>
Stack: <framework + styling>
Generate: <structured blueprint + implementation handoff>
```

---

## Scoring Dimensions (use in audits)

1. Originality
2. Hierarchy
3. Spacing consistency
4. CTA clarity
5. Trust sequencing
6. Responsiveness
7. Accessibility
8. Component coherence
9. Motion restraint
10. Implementation cleanliness

Ship threshold: every dimension >= 7/10 with clear remediation for any lower score.

---

## Local References (packaged)

Primary packaged references:
- `references/mode-guide.md`
- `references/output-contracts.md`
- `references/evaluation-rubric.md`

Bundled full engine references (synced from source skill):
- `engine/design-system/MASTER.md`
- `engine/design-system/pages/*.md`
- `engine/docs/*.md`
- `engine/templates/*`
- `engine/samples/*`

Read order:
1. mode contract in `references/`
2. global rules in `engine/design-system/MASTER.md`
3. page override in `engine/design-system/pages/<page>.md` (if relevant)

Load only sections required for the active mode.
