# Do and Don't — Operational Guardrails

## Visual / Design

### Colors
✅ DO pair warm action color + cool authority color, each in their spatial domain
✅ DO use lightly tinted surface (10% tint of authority) — not pure white or gray
✅ DO use gradient cards (warm family) for feature/product sections
✅ DO verify white-on-action-color contrast ≥ 3:1 before shipping
✅ DO use gold (#f0b400 family) only for achievements/ratings, never decorative

❌ DON'T use action color for headings or body text
❌ DON'T use authority color as primary CTA fill
❌ DON'T use the exact Sample orange #fe6724 — adapt the role, change the value
❌ DON'T use pure white as the only surface — it reads as blank, not intentional
❌ DON'T mix warm and cool gradients in the same card grid

### Typography
✅ DO use `clamp(min, Nvw, max)` on hero headings (REQUIRED)
✅ DO use weight 900 for section h2 headings
✅ DO use ≥ 18px body text on content-heavy pages
✅ DO use Georgian/serif for any page with 500+ words of body text
✅ DO use sentence case for all CTAs

❌ DON'T use fixed `font-size: 48px` on hero headings
❌ DON'T use ALL CAPS in CTAs
❌ DON'T use more than 2 font families in UI contexts
❌ DON'T use `!important` on typography (code smell — fix specificity instead)

### Shape + Elevation
✅ DO use large radius (20-32px) for cards and marketing containers
✅ DO use small radius (5-8px) for inputs, tags, form elements
✅ DO keep cards flat at rest and elevated on hover
✅ DO add `translateY(-3px)` + shadow increase on hover

❌ DON'T use large radius (20px+) on form inputs or dropdowns
❌ DON'T use heavy persistent shadows (they're earned by hover, not decorative)
❌ DON'T use glassmorphism — flat + shadow is the correct approach
❌ DON'T animate `top`/`left`/`margin` — always use `transform` (GPU-accelerated)

---

## Layout

✅ DO use one primary container max-width (1296px standard)
✅ DO alternate section backgrounds (white → surface → dark → surface)
✅ DO ensure hero is above-fold-complete at 1024px (headline + CTA + trust)
✅ DO use only 2 section padding values per page (compact and large)
✅ DO use `gap` for grid/flex spacing — not margin on children

❌ DON'T use 3+ different container max-widths on the same page
❌ DON'T make adjacent sections the same background color
❌ DON'T use arbitrary padding values (`padding: 93px 0`)
❌ DON'T forget container horizontal padding on mobile (min 16px)

---

## Conversion / CTA

✅ DO include "Free" in all freemium primary CTAs
✅ DO place a trust signal within 2 visual units of every CTA
✅ DO have 3 CTA placements on any page taller than 600px
✅ DO use Google OAuth as the primary signup mechanism
✅ DO show 30%+ of content value before any login gate

❌ DON'T use "Get Started" alone — add the action + "for Free"
❌ DON'T put a CTA without adjacent social proof
❌ DON'T hide pricing only in modals — make it findable
❌ DON'T show login gate before delivering any value

---

## Content / Copy

✅ DO write headlines in outcome-first pattern
✅ DO use specific numbers (not "thousands" — use "12,000")
✅ DO follow trust sequence: volume → authority → quality → risk-reduction
✅ DO keep feature card descriptions under 40 words
✅ DO use sentence case for headings and CTAs

❌ DON'T use vague qualifiers ("amazing", "best-in-class", "revolutionary")
❌ DON'T use "millions of users" when you have a real number
❌ DON'T lead with features before benefits in feature descriptions
❌ DON'T copy Sample's exact taglines or copy patterns verbatim

---

## Accessibility

✅ DO add skip link: `<a href="#main-content">Skip to content</a>`
✅ DO use `<button>` for actions, `<a>` for navigation
✅ DO style `:focus-visible` visibly (never suppress without replacement)
✅ DO add `aria-label` to all icon-only buttons
✅ DO add `@media (prefers-reduced-motion: reduce)` to all ambient animations
✅ DO add descriptive `alt` text to informative images

❌ DON'T use `outline: none` without a custom ring/shadow replacement
❌ DON'T use `<div onClick>` for interactive elements
❌ DON'T use placeholder text as a substitute for a visible `<label>`
❌ DON'T suppress focus for "design reasons"
❌ DON'T deploy marquee or shimmer loops without `prefers-reduced-motion` handling

---

## Originality / Brand Safety

✅ DO adapt principles (warm+cool pairing, bimodal radius, CTA formula)
✅ DO change hues while keeping temperature and role
✅ DO produce work that could clearly belong to a different company
✅ DO run the transferability test before delivering

❌ DON'T use Sample logo, wordmark, mascot, or any brand asset
❌ DON'T use #fe6724 as output primary color
❌ DON'T use Indian exam names (NEET/UPSC/JEE) unless user requested EdTech
❌ DON'T copy specific statistics (3.2 Crore, 4.7/5, 150k+ ratings)
❌ DON'T use "Sample Infinity" or "Education Revolution" branding

---

## Implementation

✅ DO use semantic HTML (nav, main, header, footer, section, article)
✅ DO use Tailwind token classes (not magic px values)
✅ DO use `next/image` or equivalent for all images
✅ DO use `next/font` or `font-display: swap` for web fonts
✅ DO decompose into React components at organism-level minimum

❌ DON'T use `style={{ color: '#fe6724' }}` — use `className="text-action"`
❌ DON'T use `className="px-[37px]"` magic numbers
❌ DON'T put all JSX in one 500-line component file
❌ DON'T use `<div>` where `<button>`, `<a>`, `<nav>`, `<main>` is correct
