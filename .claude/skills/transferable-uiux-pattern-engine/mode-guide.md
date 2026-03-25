# Mode Guide

## Purpose
Detailed explanation of each skill mode with realistic examples, inputs, outputs, and edge cases.

---

## Mode 1: NEW_BRAND_MODE

### When to Use
When building UI for a **different brand from scratch** — different company, different industry, different audience. The extraction system provides quality intelligence; the output is entirely new.

### Required Inputs
```
brand: [name of the product/company]
industry: [industry sector]
page_type: [homepage | pricing | dashboard | docs | landing]
audience: [specific target user]
tone: [confident | technical | warm | playful | minimal]
cta_style: [freemium | trial | demo | contact | buy]
```

### Optional Inputs
```
palette_hint: "deep purple authority + warm coral action"
density: [airy | medium | dense]
stack: [React + Tailwind | Vue + CSS | etc.]
dark_mode: [yes | no]
a11y_target: [WCAG_AA | WCAG_AAA]
trust_signals: ["SOC 2", "10k+ users", "4.8 rating"]
```

### What Claude Does
1. Reads MASTER.md + relevant page override
2. Adapts token colors to palette_hint (keeps roles, changes hues)
3. Selects section blueprint from page type
4. Writes original headlines, features, copy (NOT from Sample)
5. Generates component breakdown + Tailwind code plan
6. Runs originality + accessibility checks

### What You Get
- Full page spec with adapted tokens
- React component tree
- Tailwind class plan (ready to implement)
- Accessibility checklist (page-specific)
- Self-audit score

### Example
```
[NEW_BRAND_MODE] Brand: Mosaic (content analytics for media companies)
Industry: B2B SaaS | Audience: Editorial directors | Tone: Professional
CTA: Freemium | Palette: Charcoal + amber | Stack: Next.js + Tailwind
```

### What Output Looks NOT like
- ❌ Has orange #fe6724 as primary
- ❌ Mentions "Sample Infinity" or exam names
- ❌ Has "3.2 Crore students" as a trust signal
- ❌ Looks like Sample with a different logo

### What Output Looks like
- ✅ Different industry positioning, different palette adaptation
- ✅ B2B trust signals (case studies, company logos, G2 rating)
- ✅ B2B CTA copy ("Start free trial" not "for Free")
- ✅ Same structural quality (hierarchy, spacing, hover, trust sequence)

---

## Mode 2: TEMPLATE_MODE

### When to Use
When you need a **reusable, brand-agnostic starting point** — all content as placeholders, all structure and interaction rules applied. Good for design agencies, template marketplaces, or starting multiple projects.

### Required Inputs
```
template_type: [homepage | pricing | dashboard | docs | landing]
industry_range: [B2C SaaS | EdTech | Healthcare | Any | etc.]
sections_needed: [list or "standard" or "minimal"]
stack: [React + Tailwind]
```

### What You Get
- Page structure with `[PLACEHOLDER]` everywhere content should go
- `[YOUR_ACTION_COLOR]`, `[YOUR_AUTHORITY_COLOR]`, `[YOUR_FONT]` tokens
- All component interaction rules applied
- Tailwind config with fill-in slots
- Fill-in instructions for each section

### Use Cases
- Design agency billing templates to clients
- Open-source UI starter kits
- Bootstrap projects quickly without brand decisions yet

### What Makes a Good Template Output
- Zero brand-specific content (no colors, no copy, no logos)
- All interaction rules applied (hover states, transitions, mobile behavior)
- Clear fill-in instructions next to every placeholder
- Works for different industries with only content changes

---

## Mode 3: PAGE_GEN_MODE

### When to Use
When you have a specific product and need one specific page **right now**. The most common mode — you know what you're building, you just need a premium result.

### Required Inputs
```
product: [what it does in 1 sentence]
page: [which page]
goal: [what the page should achieve]
audience: [who sees this]
```

### Optional Inputs
```
existing_system: [describe current design system if any]
constraints: [must use X, can't use Y]
stack: [React + Tailwind]
```

### What You Get
- Complete page blueprint (section by section)
- Component breakdown (named components + their props)
- Tailwind class plan
- Content hierarchy plan
- CTA and trust signal placement
- Responsive behavior notes
- Accessibility checklist

### Best For
- Homepage for a product that's ready to launch
- Pricing page update
- Feature landing page for a campaign
- Docs page for a new feature

---

## Mode 4: SYSTEM_EXPAND_MODE

### When to Use
When you have an **existing design system** and need to add something new without creating visual inconsistency.

### Required Inputs
```
existing_system: [describe it or paste MASTER.md equivalent]
new_addition: [what page/feature to add]
```

### What You Get
- Gap analysis (what the existing system needs for this new page)
- Page spec that uses existing tokens
- Notes on any overrides needed
- Warning if the new page requires breaking the system

### Common Uses
- Adding a blog page to an existing product site
- Adding a settings page to a dashboard
- Adding a changelog page to a docs site

### Important Rule
The skill will flag if a requested addition fundamentally breaks the existing system design. Example: "You've asked for a playful, high-radius landing page, but your existing system uses tight radius and professional tone — this will feel inconsistent."

---

## Mode 5: AUDIT_MODE

### When to Use
When you have existing UI that feels mediocre, generic, or broken — and need an expert critique with actionable fixes.

### Required Inputs
```
[paste existing UI code]
OR
[describe the current page in detail]
```

### Optional Inputs
```
focus: [all | visual | UX | accessibility | conversion | mobile]
priority: [ship fast | comprehensive | accessibility-first]
```

### What You Get
- 10-dimension score table (1-10 each, see evaluation-rubric.md)
- Total score + verdict (ship / polish / rework)
- Ranked issues list (top 5-8 by user impact)
- For each issue:
  - What the problem is
  - Which MASTER.md rule it violates
  - Current state → recommended fix
  - Code example for the fix
- Quick wins (fixes taking < 1 hour)
- Strategic improvements (longer term)

### Audit Output Structure
```
## Audit Score
Originality:  [X]/10  [why]
Hierarchy:    [X]/10  [why]
Spacing:      [X]/10  [why]
CTA Logic:    [X]/10  [why]
Trust:        [X]/10  [why]
Accessibility:[X]/10  [why]
Motion:       [X]/10  [why]
Responsive:   [X]/10  [why]
Components:   [X]/10  [why]
Code:         [X]/10  [why]

Total: [XX]/100 — [verdict]

## Top Issues (by impact)
1. [CRITICAL] [Issue] → [Fix] → [Code]
2. [HIGH] [Issue] → [Fix]
...
```

### What Makes a Good Audit
- References specific MASTER.md rules being violated
- Provides exact code fixes (not just descriptions)
- Prioritizes by user impact (not aesthetics)
- Treats accessibility as non-negotiable

---

## Mode Inference (When Not Specified)

If the user doesn't specify a mode, Claude infers:

| Signal | Mode |
|--------|------|
| "Build a homepage for [Brand]" | NEW_BRAND |
| "Create a reusable template" | TEMPLATE |
| "I need a pricing page for my SaaS" | PAGE_GEN |
| "Add a blog to our existing site" | SYSTEM_EXPAND |
| "Review this code" / "What's wrong with this page" | AUDIT |
| "Redesign this" / "This feels generic" | AUDIT → then PAGE_GEN |

---

## Mode Chaining

Modes can chain:
```
AUDIT → PAGE_GEN (audit existing, then rebuild)
NEW_BRAND → SYSTEM_EXPAND (build homepage, then add pricing)
TEMPLATE → NEW_BRAND (start with template, adapt to brand)
```

In chained mode, the skill maintains context from the earlier mode output.
