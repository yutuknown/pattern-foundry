# SKILL: Pattern Foundry

> **Version:** 2.0 | **Design source:** Curated Sample.in audit snapshot
> **Stack:** React + Tailwind CSS | **Confidence:** High (manual verification)

---

## What This Skill Is

A **user-adaptive, brand-neutral UI/UX generation engine** trained on design intelligence extracted from a high-quality consumer EdTech product. It does NOT clone the source site. It extracts the *quality system* — spacing discipline, component grammar, conversion architecture, interaction model — and applies that system to generate **original work** for entirely different brands, industries, and contexts.

**The difference:** Most "design inspiration" tools make you copy. This skill makes you *understand* — then generate something new that operates at the same quality level.

---

## When to Use This Skill

- Building a new homepage, landing page, or marketing site
- Creating a SaaS pricing page or feature page
- Designing a freemium conversion flow
- Generating a docs/notes reading page layout
- Building a dashboard shell
- Auditing and upgrading weak or generic UI
- Enforcing design consistency across a multi-page product
- Creating generic, reusable templates at premium quality

---

## Quality Bar Enforced

Every output must pass this standard:

| Dimension | Requirement |
|-----------|-------------|
| Hierarchy | Clear dominant element per section; heading levels sequential |
| Spacing | System-consistent section padding; no arbitrary values |
| Clarity | User understands page purpose in <5 seconds |
| Consistency | Same component variant used throughout |
| CTA Logic | Trust signal adjacent to every CTA; correct placement rhythm |
| Accessibility | Focus states, alt text, labels, skip link, `prefers-reduced-motion` |
| Motion | Physical hover on interactive cards; fast color, slow spatial |
| Responsiveness | Grid collapses correctly; above-fold complete at 1024px |
| Originality | No brand-specific assets; principles adapted, not copied |
| Implementation | Semantic HTML; Tailwind tokens; no magic numbers |

**Minimum:** 7/10 per dimension before output is finalized.

---

## Supported Modes

### 1. NEW BRAND MODE
Generate original UI for a new company using the extracted quality system.
```
Input: brand_name, industry, page_type, audience, tone, trust_level, cta_style, density, palette_hint, stack
Output: Original page spec + component plan + Tailwind implementation
```

### 2. TEMPLATE MODE
Create a reusable, brand-agnostic template that can be dropped into any project.
```
Input: template_type, industry_range, sections_needed, complexity, stack
Output: Generic template with premium structure, no brand-specific content
```

### 3. PAGE GENERATION MODE
Generate a specific page for a given product/goal with implementation guidance.
```
Input: page_type, product, audience, goal, constraints, stack
Output: Page blueprint + design token application + component breakdown + code plan
```

### 4. SYSTEM EXPANSION MODE
Add a new page or feature to an existing system while maintaining consistency.
```
Input: existing_system_description, new_page/feature, constraints
Output: Consistent addition using the DNA — no drift from system
```

### 5. AUDIT / UPGRADE MODE
Critique and upgrade weak or generic UI against the extracted quality bar.
```
Input: existing_UI_code_or_description
Output: Scored critique + prioritized fixes + upgraded spec + implementation diff
```

---

## Input Schema

| Input | Type | Required | Default |
|-------|------|----------|---------|
| `mode` | enum: NEW_BRAND, TEMPLATE, PAGE_GEN, EXPAND, AUDIT | Yes | Infer from context |
| `page_type` | enum: homepage, pricing, dashboard, docs, landing, other | Yes | homepage |
| `product` | string | No | generic |
| `industry` | string | No | saas |
| `audience` | string | No | "professionals" |
| `tone` | enum: confident, technical, warm, playful, minimal | No | confident |
| `trust_level` | enum: startup, established, enterprise | No | established |
| `density` | enum: airy, medium, dense | No | medium |
| `cta_style` | enum: freemium, trial, demo, contact, buy | No | freemium |
| `palette_hint` | string (e.g., "warm blue + orange") | No | adapt from context |
| `stack` | string | No | React + Tailwind |
| `dark_mode` | boolean | No | false |
| `a11y_target` | enum: WCAG_AA, WCAG_AAA | No | WCAG_AA |

---

## Workflow (What Claude Does When Invoked)

```
Step 1:  Detect mode from context or explicit input
Step 2:  Identify page type and primary user goal
Step 3:  Infer missing inputs conservatively (don't assume bold choices)
Step 4:  Load MASTER.md → load page-specific override (if exists)
Step 5:  Adapt color tokens to brand palette (keep warm-cool role logic)
Step 6:  Select blueprint from page-blueprints.md
Step 7:  Compose section sequence (trust before CTA, value before gate)
Step 8:  Apply component grammar (correct radius per context, states complete)
Step 9:  Write content following rhythm rules (outcome-first, specific, free-led)
Step 10: Apply interaction layer (hover physics, transitions, loading states)
Step 11: Apply accessibility pass (skip link, labels, focus, reduced-motion)
Step 12: Apply responsive rules (correct breakpoints, grid collapse)
Step 13: Run originality check (no brand assets, no copied copy, adapted not cloned)
Step 14: Self-score against 10-dimension rubric
Step 15: Output result — correct any dimension below 7/10 before finalizing
```

---

## Anti-Copy Guardrails

Before generating ANY content, confirm:
- ❌ No Sample logo, branding, or "Education Revolution" language
- ❌ No `#fe6724` as output color — it's their brand orange (use adapted warm)
- ❌ No "Sample Infinity" product naming
- ❌ No Y Combinator badge reuse
- ❌ No exact exam category structure (NEET/UPSC/JEE/CAT) unless user is in EdTech
- ❌ No exact copy: "Stop Wasted Effort Start Scoring More"
- ❌ No 3.2 Crore student count or other Sample-specific stats
- ✅ DO adapt: warm-cool pairing logic, fluid hero type, freemium CTA structure
- ✅ DO adapt: trust signal stacking sequence, hover lift, section rhythm
- ✅ DO adapt: bimodal radius, content page ToC layout, dark mode toggle

---

## Output Types

| Mode | Output |
|------|--------|
| NEW_BRAND | Page spec + token adaptation + component list + Tailwind code plan |
| TEMPLATE | Generic page structure + blank-fill sections + implementation notes |
| PAGE_GEN | Full page blueprint + JSX component breakdown + Tailwind classes |
| EXPAND | Consistent addition spec + override notes + integration checklist |
| AUDIT | 10-dimension score table + ranked issues + fix recommendations + code diffs |

---

## Self-Critique Dimensions

Before finalizing any output, score 1–10 on each:

1. **Originality** — no brand duplication, adapted not cloned
2. **Hierarchy** — clear dominant element per section, heading levels correct
3. **Spacing** — section padding consistent (from MASTER.md scale), no arbitrary px
4. **CTA clarity** — trust adjacent, copy follows formula, 3+ placements on long pages
5. **Trust placement** — volume → authority → specificity → risk-reduction sequence
6. **Responsiveness** — grids collapse correctly, mobile-first layout
7. **Accessibility** — skip link, focus states, labels, alt text, reduced-motion
8. **Component coherence** — bimodal radius, hover states complete, no random variants
9. **Motion restraint** — physical hover, no distracting loops, `prefers-reduced-motion`
10. **Implementation cleanliness** — semantic HTML, tokens not magic numbers

**Ship threshold:** All dimensions ≥ 7. Fix any below 7 before output.

---

## Design System Persistence

### Reading Order
```
1. design-system/MASTER.md        → global rules, all tokens, all defaults
2. design-system/pages/{page}.md  → overrides ONLY where page-specific
3. Apply. Do not duplicate MASTER rules into page files.
```

### MASTER.md is authoritative. Page files override minimally.

---

## Invocation Examples

```
# New brand homepage
Using pattern-foundry [NEW_BRAND_MODE]:
Product: LearnPath — AI-powered skill training for engineers
Industry: EdTech/SaaS
Audience: Mid-career software engineers, 25-40
Tone: Technical but approachable
CTA: Freemium ("Start free")
Palette: Deep teal + warm amber
Stack: Next.js + Tailwind CSS
Generate: Complete homepage spec + React component breakdown

# Template mode
Using pattern-foundry [TEMPLATE_MODE]:
Template: SaaS freemium marketing homepage
Industry range: B2C/B2B SaaS, EdTech, Productivity
Sections: hero, trust, features, pricing preview, CTA, footer
Stack: React + Tailwind
Generate: Reusable template with fill-in placeholders, no brand content

# Audit
Using pattern-foundry [AUDIT_MODE]:
[Paste existing UI code or describe existing page]
Score it. List top 5 issues by impact. Provide upgraded spec.

# Dashboard
Using pattern-foundry [PAGE_GEN_MODE]:
Page: Dashboard shell
Product: Analytics platform for marketing teams
Tone: Professional, data-dense
Dark mode: yes
Stack: React + Tailwind
Generate: Full dashboard shell spec with sidebar, top bar, stats cards
```
