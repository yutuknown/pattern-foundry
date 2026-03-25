# Design System MASTER

> **Source:** Playwright-verified extraction from Sample.in
> **Status:** Authoritative — page files only override where necessary
> **Version:** 2.0

---

## Design Philosophy

**"Warm authority with breathing room."**

The system pairs warm action energy (orange family) against cool academic authority (navy family), grounded in a lightly tinted surface that prevents clinical whiteness. Interactions feel physical — elements lift, not just change color. Motion is present but never distracting. Content always precedes the ask.

**Four governing principles:**
1. **Value before gate** — deliver real content before requiring commitment
2. **Trust before CTA** — every action call is preceded by a proof signal
3. **Outcomes before features** — headlines describe transformation, not product
4. **Physical interaction** — hover = lift, not glow; state = texture, not color alone

---

## Semantic Token System

### Colors

```
ROLE                    SEMANTIC TOKEN              VALUE (reference source)
─────────────────────────────────────────────────────────────────────────────
Action (primary CTA)    color.action.primary        [warm orange ~ #fe6724]
Action hover            color.action.primary.hover  [deeper orange ~ #f97316]
Action warm start       color.action.gradient.from  [warm amber ~ #ff9a1f]
Action warm end         color.action.gradient.to    [orange ~ #f97316]

Authority               color.authority.primary     [dark navy ~ #193f68]
Authority deep          color.authority.deep        [deepest navy ~ #052b50]
Authority darkest       color.authority.darkest     [near-black ~ #010b24]

Surface default         color.surface.default       [light blue ~ #e9f1fc]
Surface pale            color.surface.pale          [very light ~ #eff4f7]
Surface hover           color.surface.hover         [lightest ~ #f6fcff]
Surface white           color.surface.white         #ffffff

Text primary            color.text.primary          [near-black ~ #111111]
Text authority          color.text.authority        [dark navy ~ #010b24]
Text muted              color.text.muted            [medium gray ~ #86949d]
Text secondary          color.text.secondary        [dark gray ~ #4b5661]
Text disabled           color.text.disabled         [light gray ~ #cacaca]
Text inverse            color.text.inverse          #ffffff

Border default          color.border.default        [blue-tinted ~ #a6d8fa]
Border subtle           color.border.subtle         [pale ~ #eff4f7]
Border emphasis         color.border.emphasis       [authority ~ #193f68]

Semantic error          color.semantic.error        [red ~ #e94e4d]
Semantic gold           color.semantic.gold         [gold ~ #f0b400]
Semantic success        color.semantic.success      [green ~ #22c55e] (estimated)
Semantic info           color.semantic.info         [blue ~ #a6d8fa]

Dark bg                 color.dark.bg               [dark ~ #191c27]
Dark surface            color.dark.surface          [dark card ~ #242836] (estimated)
```

### IMPORTANT: Brand Neutralization Rule
When adapting this system to a new brand:
- Replace `color.action.primary` with your brand's warm/energetic color
- Replace `color.authority.primary` with your brand's cool/trustworthy color
- Keep the **role assignments** identical — never use action color for text, never use authority color for primary CTA
- Adjust `color.surface.default` to a very lightly tinted version of your authority color (10% tint)

---

### Typography

```
FONT STACK:
  font.brand:    'Lato', sans-serif       → UI, marketing, headings (primary)
  font.ui:       'Inter', sans-serif      → Modern sections, data UI
  font.content:  'Georgia', 'Times New Roman', serif → Long-form reading (18px+)

SCALE (verified from Playwright computed styles):
  text.hero:     clamp(28px, 4vw, 50px)  → Hero H1 (fluid, never fixed)
  text.display:  42px / weight 900       → Section H2 (confirmed computed)
  text.2xl:      32px                    → Sub-section headings
  text.xl:       24px                    → Feature titles, card headings
  text.lg:       20px                    → Feature descriptions
  text.base:     18px                    → Body text, content pages
  text.ui:       16px                    → Standard UI labels
  text.sm:       14px                    → Secondary UI, nav, meta
  text.xs:       13px                    → Captions, fine print
  text.2xs:      12px                    → Timestamps, footnotes
  text.tiny:     11px                    → Legal, badges

LINE HEIGHTS:
  leading.hero:    1.1   → Hero heading (tight)
  leading.heading: 1.2   → Marketing headings
  leading.body:    1.5   → Standard body text
  leading.content: 1.6   → Long-form reading (confirmed: "line-height: 1.6em")
  leading.ui:      1.4   → UI labels, buttons

WEIGHTS:
  weight.regular:   400  → Body, descriptions, meta
  weight.medium:    500  → Secondary headings, emphasized labels
  weight.semibold:  600  → Subheadings, card headings
  weight.bold:      700  → Primary headings, h1
  weight.heavy:     900  → Section headings h2 (confirmed computed)

CASING:
  CTA buttons:     Sentence case ("Start learning for free")
  Nav links:       Title Case ("Entrance Exams")
  Section headers: Sentence case or Title Case
  Labels:          Sentence case
  NEVER:           ALL CAPS (aggressive), never in marketing CTAs
```

---

### Spacing System

**Base unit: 4px** (all spacing is multiples of 4)

```
SCALE:
  space.1:   4px    → Micro gaps, icon padding
  space.2:   8px    → Tight padding, small gaps
  space.3:   12px   → Input padding, small component gap
  space.4:   16px   → Standard gap (confirmed: gap:16px in feat-outer)
  space.5:   20px   → Medium padding
  space.6:   24px   → Card internal padding
  space.7:   28px   → Medium gap
  space.8:   32px   → Section breathing
  space.10:  40px   → Component group separation
  space.12:  48px   → Mobile section padding
  space.16:  64px   → Large padding, footer
  space.20:  80px   → Compact section vertical padding
  space.24:  96px   → Standard section padding (estimate)
  space.32:  128px  → Large section padding (confirmed: .er-crse-wrap)

SECTION VERTICAL PADDING:
  section.compact:  70-80px  → App download, smaller sections
  section.standard: 96px     → Standard sections
  section.large:    128px    → Hero, features, main content sections (confirmed)

  RULE: Use only 2 values per page (compact and large). Never introduce a 3rd.

COMPONENT GAPS:
  gap.tight:    16px  → Between inline elements (confirmed: gap:16px)
  gap.standard: 24px  → Between card grid items
  gap.wide:     30px  → Feature card grid (estimated from density)
  gap.section:  48px  → Between major sections within a page
```

---

### Container / Layout System

```
CONTAINERS (all verified from Playwright):
  container.wide:     1440px  → Full-width backgrounds, nav max-width
  container.standard: 1296px  → Primary content (.lp_nav_wrapper = 1296px)
  container.content:  1200px  → Alternate content container
  container.footer:   1100px  → Footer inner (.ftr-new-inner = 1100px)
  container.hero:     550px   → Hero left column (.hero-left-container)
  container.body:     800px   → Content/notes reading width
  container.narrow:   65ch    → Body text paragraph measure

HORIZONTAL PADDING (on containers):
  px.mobile:    16px
  px.tablet:    32px
  px.desktop:   48px (estimated)

GRID:
  columns.marketing: 12
  gutter.standard:   24px

BREAKPOINTS (confirmed from Playwright):
  All confirmed: 320px, 340px, 350px, 360px, 380px, 396px, 400px, 420px,
                 430px, 440px, 450px, 487px, 500px, 550px, 600px,
                 767px(min), 799px, 840px, 1005px, 1024px, 1036px,
                 1200px, 1240px, 1300px, 1440px

  PRIMARY BREAKPOINTS for new builds (simplified):
  sm:  640px   → Small mobile up
  md:  768px   → Tablet
  lg:  1024px  → Desktop
  xl:  1296px  → Wide
```

---

### Radius System

**Bimodal strategy — two distinct size ranges, never mixed:**

```
FUNCTIONAL (for interactive tools):
  radius.xs:   3-5px    → Inputs, form elements, small badges (confirmed: 4px, 5px)
  radius.sm:   6-8px    → Tags, dropdowns, small cards (confirmed: 8px auth modal)
  radius.md:   10-14px  → Standard buttons, tooltips (confirmed: 10px, 11px, 14px)

DISPLAY (for marketing/content containers):
  radius.lg:   20px     → Feature cards (confirmed: .feat-card border-radius 20px)
  radius.xl:   24-32px  → Course cards (confirmed: .crses border-radius 32px)
  radius.2xl:  60px     → Pill buttons, OAuth button (confirmed: radius 60px)
  radius.full: 50%/9999px → Circular elements, avatar, pill tags

RULE: radius.lg+ is ONLY for display/marketing containers.
      radius.sm and smaller is ONLY for functional UI.
      Never mix them (32px input = wrong; 5px feature card = wrong).
```

---

### Shadow / Elevation System

**All values confirmed from Playwright CSS extraction:**

```
shadow.none:     none
shadow.subtle:   rgba(0,0,0,0.07) 0px 2px 16px         → Very light lift
shadow.card:     rgba(0,0,0,0.08) 0px 4px 12px          → Card at rest
shadow.token:    rgba(0,0,0,0.11) 0px 1.76px 17.64px -1.76px → Token-precise
shadow.hover:    rgba(0,0,0,0.12) 0px 10px 30px          → Card on hover (confirmed)
shadow.ambient:  rgba(229,229,229,0.25) 1px 1px 60px 40px → Course card (confirmed)
shadow.glow:     rgba(255,255,255,0.3) 0px 0px 6px inset  → Inner glow (dark contexts)
shadow.bottom:   rgba(0,0,0,0.09) 0px -2px 50px 0px      → Bottom atmospheric
shadow.nav:      rgba(125,125,125,0.25) 1px 2px 4px 1px  → Nav bar on scroll

ELEVATION BEHAVIOR:
  At rest:  shadow.card (or none for flat surfaces)
  On hover: shadow.hover + translateY(-3px)  ← PHYSICAL LIFT (confirmed)
  Modal:    shadow.hover or stronger + overlay

RULE: Never apply shadow.hover persistently — it is earned through hover.
      Shadows should increase only on interaction, never as decoration.
```

---

### Border System

```
border.width.default:   1px
border.width.emphasis:  2px
border.width.thick:     3px

border.color.default:   color.border.default  (#a6d8fa — blue tinted)
border.color.subtle:    color.border.subtle   (#eff4f7 — near-white)
border.color.emphasis:  color.border.emphasis (#193f68 — authority)
border.color.action:    color.action.primary  (on focus/active states)

border.style:           solid (always)
border.none:            none (for display cards with gradients)

RULE: Blue-tinted borders (#a6d8fa family) on interactive/info elements.
      Near-white borders (#eff4f7 family) on card outlines.
      Never colored borders on gradient-background cards (use none).
```

---

### Motion System

**All timing values confirmed from Playwright CSS extraction:**

```
DURATION:
  duration.instant:  0ms    → State-only changes (color roles)
  duration.fast:     150ms  → Micro: opacity, color changes
  duration.base:     200ms  → Standard hover color/bg (confirmed: background 0.2s)
  duration.medium:   300ms  → Multi-prop transitions (confirmed: 0.3s ease-in-out)
  duration.slow:     450ms  → Spatial/transform changes (confirmed: 0.45s cubic-bezier)
  duration.shimmer:  4000ms → Loading skeleton loop
  duration.marquee:  40000ms → Trust banner scroll loop

EASING:
  ease.default:    cubic-bezier(0.4, 0, 0.2, 1)  → ALL spatial moves (confirmed exact)
  ease.in:         cubic-bezier(0.4, 0, 1, 1)    → Elements leaving screen
  ease.out:        cubic-bezier(0, 0, 0.2, 1)    → Elements entering screen
  ease.linear:     linear                         → Marquee/loop animations only

KEYFRAMES (confirmed from CSS):
  shimmer_lrn:           Skeleton loading sweep (left-right light pass), 4s infinite
  shimmer_lgou_floating: Floating element shimmer variant
  scroll-left:           Trust banner marquee, translateX 0 → -50%, 40s linear infinite

HOVER PHYSICS (confirmed from computed styles):
  transform: translateY(-3px)         → The lift distance
  box-shadow: shadow.hover            → Elevation increase
  transition: transform 0.45s + opacity 0.45s cubic-bezier(0.4,0,0.2,1)

  Combined hover rule (apply to all interactive cards):
  .card:hover {
    transform: translateY(-3px);
    box-shadow: rgba(0,0,0,0.12) 0px 10px 30px;
    transition: transform 0.45s cubic-bezier(0.4,0,0.2,1),
                box-shadow 0.45s cubic-bezier(0.4,0,0.2,1);
  }

COLOR TRANSITIONS (confirmed: background 0.2s, color 0.2s):
  Use 0.2s for all color/opacity property changes.

MULTI-PROP (confirmed: background 0.3s, transform 0.3s, width 0.3s, border-radius 0.3s):
  When animating multiple properties that aren't spatial, use 0.3s.

REDUCED MOTION (REQUIRED — not confirmed in source, add to all new builds):
  @media (prefers-reduced-motion: reduce) {
    .marquee { animation: none; overflow-x: auto; }
    .shimmer { animation: none; background: color.surface.default; }
    * { transition-duration: 0.01ms !important; }
    .card:hover { transform: none; }
  }
```

---

## Component Principles

### Bimodal Radius Rule
- `radius.xs–md` → Functional UI (inputs, dropdowns, badges, small buttons)
- `radius.lg–2xl` → Display UI (cards, feature containers, course cards, pill CTAs)
- Never mix. The radius signals purpose.

### Hover Physics Rule
Every interactive card (not just buttons) must have:
1. `translateY(-3px)` on hover
2. Shadow increase from `shadow.card` to `shadow.hover`
3. Both on the SAME transition (not separate)
4. Cursor: pointer appears BEFORE transform begins

### Button Hierarchy Rule
```
Primary:   action.primary fill + white text + medium/large radius
Secondary: authority.primary outline + authority text
Ghost:     transparent + authority text, opacity dim on hover
OAuth:     white fill + black text + large/pill radius (3rd party styling)
```

### State Completeness Rule
Every interactive component MUST have all states defined:
default → hover → focus → active → disabled → loading → error/success (where applicable)

### Flat-Then-Shadow Rule
Cards at rest: `shadow.card` or no shadow (never `shadow.hover`)
Cards on hover: `shadow.hover` (earned by interaction, not decoration)

---

## CTA / Trust Architecture

### Trust Signal Sequence (always in this order)
```
1. Volume proof    → "N+ users/students/customers"
2. Authority proof → "Backed by [trusted third party]" / award logos
3. Quality proof   → "4.7/5 rating · 150k+ reviews"
4. Risk reduction  → "No credit card" / "Cancel anytime" / "Free forever"
```

### CTA Placement Rhythm
```
Hero:      above-fold primary CTA (always "Free" in freemium)
Mid-page:  after value demonstration (features section)
End-page:  before footer (urgency or summary CTA)
```

### CTA Copy Formula (Freemium)
```
"[Verb] [specific action] for Free"
→ "Start learning for free" ✓
→ "Join Course for Free"   ✓
→ "Get Started"             ✗ (too generic, no "free")
→ "Sign Up"                 ✗ (no value signal)
```

### Trust Adjacent Rule
Every primary CTA cluster must have a trust signal within 2 visual units:
- Above: metric/rating/badge
- Below: "No credit card" / user count
- Adjacent: small star rating micro

---

## Content Rhythm Rules

### Headline Formula
```
Pattern: [Outcome verb] [stop/start contrast]
Good:    "Start scoring more, stop wasting time"
Good:    "[Action] for free — [benefit in numbers]"
Bad:     "Our comprehensive platform for [category]" (feature-led, not outcome-led)
Bad:     "The best [category] solution" (vague claim)
Max:     8-10 words
Case:    Sentence case always
```

### Feature Description Formula
```
[2-3 word label]
[Mechanism line: how it works in 1 sentence — active verbs]
[Benefit line: what outcome user gets — ≤40 words]
```

### Stats Display Formula
```
[LARGE BOLD NUMBER]
[small regular descriptor label]
→ Never reverse this hierarchy
→ Never put number inline with text
```

---

## Accessibility Defaults

Required on every output:
- `<a href="#main-content">Skip to main content</a>` — first element in body
- One `<h1>` per page — always matches primary page topic
- Heading levels sequential — never skip (H1 → H3 without H2)
- `<nav aria-label="...">` — labeled navigation landmarks
- All inputs: visible `<label>` element (not placeholder-only)
- All icon-only buttons: `aria-label` attribute
- All images: `alt=""` (decorative) or descriptive text (informative)
- `:focus-visible` — always styled, never suppressed without replacement
- Modals: `role="dialog"`, `aria-modal="true"`, focus trap, Escape close
- `@media (prefers-reduced-motion: reduce)` — all ambient animations wrapped

---

## Originality Guardrails

**DO NOT carry forward:**
- Source site's exact orange (#fe6724) — adapt the role, not the value
- Logo, branding, or product naming
- Exam category structure (NEET/UPSC/JEE) unless user is in EdTech
- Exact copy or taglines
- Y Combinator badge or specific third-party logos
- Exact student/user count statistics

**DO carry forward:**
- Warm action + cool authority color pairing *logic*
- Bimodal radius strategy
- `clamp()` fluid hero typography technique
- Trust signal stacking *sequence*
- Section background alternation *pattern*
- `translateY(-3px)` hover physics *principle*
- Value-before-gate *principle*
- Freemium CTA formula *structure*

---

## Responsive Rules (MASTER defaults)

```
GRID COLLAPSE:
  3-col → 2-col at md (768px) → 1-col at sm (640px)
  4-col → 2-col at md → 1-col at sm

HERO:
  Desktop: 2-col (text left 55-60%, visual right 40-45%)
  Mobile:  1-col stacked (text above, visual below)

STATS ROW:
  Desktop: flex row, justify-between (4 items)
  Mobile:  2×2 grid

SIDEBARS:
  Desktop: sticky sidebar (280px)
  Mobile:  collapsed (accessible alternative required — NOT just display:none)

SECTION PADDING:
  Desktop: 128px / 80px
  Mobile:  56px / 40px (half the desktop value)

TOUCH TARGETS:
  All interactive: minimum 44×44px on mobile (Apple HIG)
```

---

## Dark Mode

Dark mode is REQUIRED for all content-heavy pages (docs, notes, long reads).

```
css variables swap approach:
.dark {
  --color-bg:      #191c27;  (confirmed source dark bg)
  --color-surface: #242836;  (estimated dark card surface)
  --color-text:    #e2e8f0;
  --color-muted:   #94a3b8;
  --color-border:  #334155;
}

Toggle: class-based (.dark on <html>), persisted in localStorage
Also respect: prefers-color-scheme: dark (system preference)
```
