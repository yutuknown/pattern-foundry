# Visual DNA

## Purpose
One-page design fingerprint of the extracted quality system — the essence that makes new work feel at this quality level.

## Evidence
manually verified from live Sample.in CSS and DOM inspection.

---

## The DNA in One Block

```
PALETTE:
  Action: warm orange family (#fe6724 source — adapt hue, keep temperature)
  Authority: dark navy family (#193f68 source — adapt hue, keep gravitas)
  Surface: very light blue-tinted (#e9f1fc source — 10% tint of authority)
  Text primary: near-black (#111111)
  Gold: achievement/rating accent (#f0b400)

TYPOGRAPHY:
  Primary font: Lato (humanist sans-serif) — !important override on all UI
  Secondary font: Inter (geometric sans) — newer sections
  Content font: Georgia (serif) — long-form reading pages
  Hero: clamp(28px, 4vw, 50px) / weight 900 — FLUID, NEVER FIXED
  Section H2: 42px / weight 900 (confirmed from computed styles)
  Body: 18px / 1.6 line-height on content pages

SHAPE:
  Functional UI: 3-8px radius (inputs, badges, tags — confirmed 4px, 5px, 8px)
  Display UI: 20-32px radius (cards, containers — confirmed 20px, 32px)
  Pill elements: 60px or 50% (OAuth buttons, pill CTAs — confirmed 60px)

ELEVATION:
  At rest: shadow.card (rgba(0,0,0,0.08) 0px 4px 12px) OR no shadow
  On hover: translateY(-3px) + shadow.hover (rgba(0,0,0,0.12) 0px 10px 30px)
  Course card ambient: rgba(229,229,229,0.25) 1px 1px 60px 40px (soft glow)

MOTION:
  Spatial: 0.45s cubic-bezier(0.4, 0, 0.2, 1) — premium, unhurried
  Color/opacity: 0.2s — snappy, immediate
  Multi-prop: 0.3s ease-in-out — balanced
  Shimmer: 4s infinite — loading skeleton
  Marquee: 40s linear infinite — trust scroll

LAYOUT:
  Outer container: 1440px (backgrounds, nav max-width — confirmed)
  Content container: 1296px (main page content — confirmed .lp_nav_wrapper)
  Footer inner: 1100px (confirmed .ftr-new-inner)
  Hero left: max-width 550px (confirmed .hero-left-container)
  Section padding: 128px 0 (confirmed .er-crse-wrap)

GRADIENTS (confirmed from CSS):
  Warm feature card: linear-gradient(135deg, #ff9a1f 0px, #f97316 100%)
  Alt warm (courses): linear-gradient(155deg, #ff9a1f 0px, #f97316 100%)
  Dark hero: linear-gradient(90deg, navy → lighter navy)

FOOTER BACKGROUND: #e9f1fc (confirmed, same as surface)
```

---

## The Five Personality Traits

1. **Confident** — makes bold outcome claims, specific numbers, no hedging
2. **Approachable** — large radius on display elements, sentence case CTAs, "free" everywhere
3. **Academic** — Georgia serif for content, navy authority color, curriculum-aligned hierarchy
4. **Energetic** — orange primary action, gradient feature cards, physical hover physics
5. **Trustworthy** — Y Combinator-style authority badge, volume + rating + award stacking

---

## What Creates "Premium Feel"

| Element | Why It Feels Premium |
|---------|---------------------|
| `clamp()` hero heading | Fluid type on every viewport — no awkward break |
| `translateY(-3px)` hover | Physical metaphor — cards LIFT, they don't glow |
| `0.45s cubic-bezier(0.4,0,0.2,1)` | Material easing — grounded, not bouncy |
| Bimodal radius | Large radius signals consumer-friendly; tiny radius signals precision tool |
| Section padding 128px | Breathing room signals confidence, not timidness |
| Trust stacking sequence | Volume → Authority → Specificity → Risk-reduction feels orchestrated |
| Outcome-first headlines | "Start scoring more" beats "Our comprehensive platform" |
| Font.brand + Font.content split | Right font for right context — not one-size fits all |

---

## What Would Break the DNA

1. Fixed pixel hero heading (breaks at odd viewports)
2. Same radius on inputs and cards (no bimodal)
3. Color-only hover on cards (no physical lift)
4. Authority color (#193f68) as the CTA button (trust color ≠ action color)
5. Pure white page with no surface color variation
6. No trust signal adjacent to CTA
7. Generic "Get Started" CTA without "Free"
8. Heading hierarchy skipped (H1 → H3)
9. No `prefers-reduced-motion` on animations
10. Sidebar just hidden on mobile with `display:none`

## Confidence
**High** — all key values confirmed from live manual design audit and computed styles.
