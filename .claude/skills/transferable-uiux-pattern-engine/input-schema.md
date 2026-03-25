# Input Schema

## Purpose
Complete reference for all inputs the skill accepts across all modes.

---

## Universal Inputs (All Modes)

| Input | Type | Values | Default | Description |
|-------|------|--------|---------|-------------|
| `mode` | enum | NEW_BRAND, TEMPLATE, PAGE_GEN, EXPAND, AUDIT | inferred | Skill execution mode |
| `stack` | string | "React + Tailwind", "Vue + CSS", "HTML + CSS" | React + Tailwind | Target implementation stack |
| `a11y_target` | enum | WCAG_AA, WCAG_AAA | WCAG_AA | Accessibility compliance level |

---

## NEW_BRAND_MODE Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `brand` | string | YES | — | Brand/product name |
| `industry` | string | YES | — | Industry sector |
| `page_type` | enum | YES | homepage | Page to generate |
| `audience` | string | YES | — | Target user description |
| `tone` | enum | NO | confident | confident, technical, warm, playful, minimal |
| `trust_level` | enum | NO | established | startup, established, enterprise |
| `density` | enum | NO | medium | airy, medium, dense |
| `cta_style` | enum | NO | freemium | freemium, trial, demo, contact, buy |
| `palette_hint` | string | NO | adapted | e.g., "deep teal + warm amber" |
| `dark_mode` | boolean | NO | false | Whether dark mode is required |
| `trust_signals` | array | NO | generic | Your specific trust signals |
| `features` | array | NO | 3 placeholders | Feature names/descriptions |

### Tone Guide
```
confident:   Bold claims, strong CTAs, outcome-forward copy
technical:   Precise language, feature detail, less marketing gloss
warm:        Empathetic, first-person, human-centered
playful:     Light, emoji-friendly, shorter sentences
minimal:     Sparse copy, visual-heavy, implicit over explicit
```

### Trust Level Guide
```
startup:     "Join early" framing, founding team credibility, early adopter language
established: Rating + volume proof, media logos, case studies
enterprise:  Compliance badges (SOC2, HIPAA), named company case studies, SLA guarantees
```

### CTA Style Guide
```
freemium: Primary CTA always includes "Free". No payment upfront.
trial:    "Start free trial" (14/30 days), credit card may be required
demo:     "Book a demo" / "Request demo" — sales-led
contact:  "Contact us" / "Talk to sales" — enterprise
buy:      "Buy now" / "Get [product]" — direct commerce
```

---

## TEMPLATE_MODE Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `template_type` | enum | YES | homepage | Page type |
| `industry_range` | string | NO | "Any" | Industry flexibility |
| `sections_needed` | array or "standard" | NO | standard | List of sections |
| `complexity` | enum | NO | standard | minimal, standard, full |

### Sections Available
```
hero, trust, category-browser, feature-grid, cta-block,
app-download, testimonials, pricing-cards, comparison-table,
faq, stats-row, marquee, footer, navbar
```

---

## PAGE_GEN_MODE Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `product` | string | YES | — | 1-sentence product description |
| `page` | string | YES | — | Which page to build |
| `goal` | string | YES | — | What the page must achieve |
| `audience` | string | YES | — | Who sees this page |
| `existing_system` | string | NO | — | Current design system (if any) |
| `constraints` | array | NO | none | "must use X", "can't use Y" |

---

## SYSTEM_EXPAND_MODE Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `existing_system` | string | YES | — | Description or paste of current system |
| `new_addition` | string | YES | — | What page/feature to add |
| `consistency_target` | enum | NO | strict | strict (full match), flexible (adapt) |

---

## AUDIT_MODE Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `ui_code` or `ui_description` | string | YES | — | Current UI to audit |
| `focus` | enum | NO | all | all, visual, UX, accessibility, conversion, mobile |
| `priority` | enum | NO | comprehensive | ship-fast, comprehensive, accessibility-first |
| `output_format` | enum | NO | full | full, summary, issues-only |

---

## Token Adaptation Inputs (All Modes)

When `palette_hint` is provided, Claude derives:

```
palette_hint: "deep teal + warm amber"
→ color.authority.primary: derived deep teal (cool, trustworthy)
→ color.action.primary: derived warm amber (warm, energetic)
→ color.surface.default: 10% tint of teal
→ color.border.default: 30% tint of teal
```

If no `palette_hint`, Claude chooses appropriate colors based on `industry` and `tone`:
- Healthcare → teal authority, calm blue action
- Finance → charcoal authority, gold action
- Developer tools → zinc authority, purple action
- Wellness → warm earth authority, coral action
- EdTech → slate authority, amber action (different from Sample to avoid similarity)

---

## Defaults Table

| Context | Default Action | Default Authority | Default Surface |
|---------|---------------|------------------|----------------|
| Generic | Amber #d97706 | Slate #334155 | Light gray-blue |
| B2B SaaS | Indigo #6366f1 | Slate #1e293b | Light gray |
| EdTech | Amber #f59e0b | Blue-gray #1e3a5f | Light blue |
| Healthcare | Teal #0d9488 | Dark slate #1e293b | Mint |
| Finance | Emerald #10b981 | Dark charcoal #111827 | Warm cream |
| Dev Tools | Purple #8b5cf6 | Zinc #3f3f46 | Near-white |
| Consumer | Coral #f97316 | Dark green #14532d | Warm peach |
