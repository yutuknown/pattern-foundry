# Homepage — Page Override

> **Inherits from:** design-system/MASTER.md
> **Override only what differs from MASTER defaults**

## Page Goal
Convert visitors from awareness to free account creation. Zero financial friction. Maximum trust density near every CTA.

## Blueprint (Section Order)

```
01. NAVBAR (sticky)
    Height: 82px (confirmed). Container: 1296px. Logo left, nav center, Login+Signup right.
    Mobile: Logo + primary CTA only. No hamburger complexity — app-first approach.

02. HERO (above-fold complete at 1024px)
    Container: 1440px wide (background), 1296px inner.
    Layout: 55% text left / 45% visual right.
    Left: Trust badge → H1 (clamp 28-50px, weight 900) → Subheadline → Primary CTA → Social proof micro
    Right: App screenshot in device frame OR aspirational illustration
    Background: Dark navy gradient (linear-gradient 90deg dark navy family)
    Override: Hero uses dark background — text is white/inverse

03. TRUST SECTION
    Background: white (contrast with hero dark)
    Row 1: Scrolling marquee — awards, recognitions (scroll-left 40s linear)
    Row 2: 4-stat flex row — large bold number + small descriptor

04. CATEGORY BROWSER
    Background: color.surface.default (#e9f1fc equivalent)
    Two-column: [Category Type A] + [Category Type B]
    Each: section heading + pill tag grid (wrap, max 12 items, "See all" beyond)
    Tag style: pill radius, surface bg, blue-tinted border, hover bg shift

05. FEATURE GRID
    Background: white
    Section heading: centered, 42px weight 900
    Grid: 3-col (2 tablet, 1 mobile), gap 24px
    Cards: gradient background (warm #ff9a1f→#f97316 family), radius 20px
    Hover: translateY(-3px) + shadow.hover, 0.45s cubic-bezier

06. MID-PAGE CTA BLOCK
    Background: dark navy (contrast from white features section)
    Content: centered headline + social proof line + primary CTA (orange) + secondary (outline)
    Override: no surface bg here — needs strong contrast punch

07. APP DOWNLOAD BRIDGE
    Background: color.surface.default
    Layout: 2-col (text+QR+badges left, phone mockups right)
    Required: QR code SVG + Play Store + App Store badges
    Desktop-only: QR code. Mobile: App Store links prominent, QR hidden.

08. TESTIMONIALS (optional, insert between feature grid and CTA if available)
    Background: white
    Grid: 3-col (2 tablet, 1 mobile)
    Card: white, radius.lg, shadow.card

09. FOOTER
    Background: color.surface.default (#e9f1fc)
    Inner: max-width 1100px (confirmed: .ftr-new-inner)
    4-col: Brand | Company | Links | Categories
    Bottom bar: Copyright + Privacy + Terms
```

## Content Rhythm Override (Homepage-specific)

- H1 must be: outcome-first, ≤10 words, sentence case, font-size hero (clamp)
- Subheadline: platform + mechanism + audience in 1-2 sentences, ≤20 words
- Feature H2s: 2-3 words, bold label style ("Exam-Focused Smart Notes")
- Feature H3s: 1-2 sentence mechanism, active verb, ≤20 words
- Stats: exact number (never approximate) + specific context label

## CTA Override (Homepage-specific)

Primary CTA: "[Start/Begin/Join] [action] for Free" — never vague "Get Started"
3 CTA placements: hero section, mid-page CTA block, footer CTA or final section
Trust ABOVE every primary CTA: metric or badge, not below

## Trust Signal Density Override

Homepage needs maximum trust density (it's brand-unknown context):
- Hero: trust badge + social proof micro (rating + count)
- Trust section: full stats row + marquee
- Mid-page CTA: student/user count inline
- Footer: contact email visible

## Responsive Override

Stats section: on mobile, 2×2 grid (NOT flex row — too compressed at 390px)
Feature grid: 3→2→1 cols at lg/md/sm
Category tags: flex-wrap on all viewports (not grid)

## Component Emphasis

Feature cards: GRADIENT variant (warm) — not white cards on homepage
Course/category cards: radius.xl (32px), ambient shadow
Nav: always white bg, never transparent (non-sticky sites can do transparent, not here)
