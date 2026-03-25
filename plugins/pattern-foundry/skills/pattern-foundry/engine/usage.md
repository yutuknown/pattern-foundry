# Usage Guide

## Purpose
How to invoke the pattern-foundry skill effectively across all 5 modes.

---

## Quick Start

Prefix any request:
```
Using the pattern-foundry skill in [MODE]:
```

Or just describe your task and Claude will infer the mode.

---

## Design System Persistence Model

### Always load in this order:
```
1. design-system/MASTER.md      → global tokens, rules, defaults
2. design-system/pages/{page}.md → page-specific overrides ONLY
```

Page override files are intentionally minimal. If a rule isn't in the page file, it comes from MASTER.md.

**NEVER duplicate MASTER.md rules into page files.**

---

## Mode Reference

### NEW_BRAND_MODE
Use when: Building something completely new for a different brand/industry.
```
Skill: pattern-foundry [NEW_BRAND_MODE]
Brand: [your brand name]
Industry: [your industry]
Page: [homepage | pricing | dashboard | docs | landing]
Audience: [who will use this]
Palette hint: [describe color direction: "warm teal + cool charcoal"]
Stack: [React + Tailwind | Vue + CSS | etc.]
```
What you get: Original page spec + adapted token set + component breakdown + Tailwind code plan

### TEMPLATE_MODE
Use when: Creating a reusable starting point (no specific brand yet).
```
Skill: pattern-foundry [TEMPLATE_MODE]
Template: [homepage | pricing | dashboard | docs | landing]
Industry range: [B2C SaaS | EdTech | Healthcare | any]
Sections needed: [list or "standard"]
Stack: [React + Tailwind]
```
What you get: Fill-in-the-blank template with all [PLACEHOLDER] slots, premium structure, full implementation notes

### PAGE_GEN_MODE
Use when: You have a product and need a specific page generated right now.
```
Skill: pattern-foundry [PAGE_GEN_MODE]
Product: [what it does in 1 sentence]
Page: [what page to build]
Goal: [what the page should achieve]
Audience: [who sees this page]
```
What you get: Complete page spec + JSX component breakdown + Tailwind classes + accessibility checklist

### SYSTEM_EXPAND_MODE
Use when: You have an existing design system and need to add a new page consistently.
```
Skill: pattern-foundry [SYSTEM_EXPAND_MODE]
Existing system: [brief description or paste current MASTER.md]
New page/feature: [what to add]
Constraints: [any specific rules]
```
What you get: Consistent addition spec that won't break system coherence

### AUDIT_MODE
Use when: You have existing UI that needs critique and improvement.
```
Skill: pattern-foundry [AUDIT_MODE]
Paste: [existing UI code or describe the page in detail]
Focus: [all | visual | UX | accessibility | conversion | performance]
```
What you get: 10-dimension score (1-10 each) + ranked issues + fix recommendations + upgraded spec

---

## How MASTER.md and Page Overrides Work Together

```
Reading example for a homepage:

Claude reads:
  1. MASTER.md → gets: color tokens, typography scale, motion system, CTA rules,
                         trust signal sequence, accessibility defaults, responsive rules

  2. pages/homepage.md → gets: specific section order, "gradient cards preferred",
                                "maximum trust density", "stats as 2×2 on mobile"

Claude applies:
  - All MASTER rules by default
  - Homepage.md overrides where specified
  - Any gap = fall back to MASTER

This keeps page files minimal (5-10 overrides max) rather than duplicating
the entire design system per page.
```

---

## Helper Scripts

Run these scripts to automate extraction and token generation:

```bash
# 1. Inspect a reference site
python3 scripts/inspect_site.py --url https://example.com --output ./inspection_output

# 2. Extract design tokens from live CSS
python3 scripts/extract_tokens.py --url https://example.com --output ./tokens_output

# 3. Build and validate the design system
python3 scripts/build_design_system.py \
  --tokens ./design-system/tokens.json \
  --master ./design-system/MASTER.md \
  --output ./design-system/

# 4. Generate a page override file
python3 scripts/generate_page_override.py --page homepage --output ./design-system/pages/
```

---

## Common Mistakes

❌ Invoking without specifying mode → gets generic output
✅ Always specify `[MODE]` or provide enough context for Claude to infer it

❌ Asking for a full site in one message
✅ Build page-by-page: homepage → pricing → dashboard → etc.

❌ Accepting output with `font-size: 48px` on hero
✅ Check for `clamp()` usage — reject fixed px on hero headings

❌ Forgetting to specify the stack
✅ Always include stack: `React + Tailwind` or `Vue + CSS` etc.

❌ Expecting Sample-specific output
✅ This skill generates ORIGINAL work inspired by the quality level, not the brand
