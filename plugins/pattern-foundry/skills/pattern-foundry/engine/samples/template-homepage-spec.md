# Sample: Generic Template — SaaS Freemium Homepage

> **Mode:** TEMPLATE
> **Template type:** SaaS/EdTech/B2C freemium marketing homepage
> **Industry range:** Any B2C or prosumer B2B product with a free tier
> **Audience:** Generic (fill in)
> **Density:** Medium
> **Complexity:** Standard (8 sections)
> **Stack:** React + Tailwind CSS

---

## How to Use This Template

1. Replace all `[PLACEHOLDER]` values with your brand
2. Adapt `[COLOR_ACTION]` and `[COLOR_AUTHORITY]` to your brand palette
3. Swap font to your brand font (keep humanist sans family)
4. Replace stats with your own metrics
5. Replace feature names and descriptions with your own
6. The structure, spacing, and interaction rules stay the same

---

## Token Slots

```css
:root {
  /* FILL THESE IN */
  --color-action:      [COLOR_ACTION];        /* warm/energetic CTA color */
  --color-action-hover: [COLOR_ACTION_DARK];  /* slightly darker hover */
  --color-authority:   [COLOR_AUTHORITY];     /* cool/trustworthy authority */
  --color-surface:     [COLOR_SURFACE];       /* very lightly tinted background */

  /* KEEP THESE — system tokens */
  --color-text:        #111111;
  --color-muted:       #86949d;
  --color-border:      [10% tint of authority]; /* derive from authority */

  /* KEEP THESE — space tokens */
  --section-lg:        128px;
  --section-sm:        80px;
  --container-main:    1296px;
  --container-wide:    1440px;
  --container-footer:  1100px;
}
```

---

## Section Templates

### [SECTION 1: NAVBAR]
```
Component: Navbar
Height: 82px
Max-width: var(--container-wide)
Inner: var(--container-main)

Left:   [YOUR_LOGO]
Center: [NAV_LINK_1] | [NAV_LINK_2] | [NAV_LINK_3]
Right:  [Login] [PRIMARY_CTA_BUTTON]

Primary CTA: action color, radius 8px, "Start [action] for free"
Background: white
On scroll: subtle bottom shadow appears (0.2s transition)
Mobile: Logo + CTA only (no nav links)
```

### [SECTION 2: HERO]
```
Component: HeroSection
Background: dark gradient (authority color family)
Padding: var(--section-lg) 0
Container: var(--container-main)
Layout: 55/45 split (text left / visual right)

TEXT COLUMN (max-width: 550px):
  [TRUST_BADGE]: small badge above headline
    - "Backed by [Authority]" or "[N]+ [users] trust us" or "[Award]"
    - Component: TrustBadge — small, pill shape, surface bg

  [H1_HEADLINE]: primary outcome promise
    - font-size: clamp(28px, 4vw, 50px)
    - font-weight: 900
    - color: white
    - Content: "[Outcome verb] [benefit]. [Stop/start contrast]."
    - Max: 10 words
    - Case: Sentence case

  [SUBHEADLINE]: platform + mechanism + audience
    - 18px, white/80%, max-width 44ch
    - 1-2 sentences maximum

  [PRIMARY_CTA]:
    - Background: var(--color-action)
    - Color: white
    - font-weight: 700
    - radius: 8px
    - padding: 14px 28px
    - text: "[Verb] [action] for Free"
    - hover: var(--color-action-hover) + transition 0.2s

  [SOCIAL_PROOF_MICRO]:
    - 13px, white/60%
    - "⭐ [X.X] rating · [N]+ [users]"
    - Placed directly below CTA

VISUAL COLUMN:
  [PRODUCT_VISUAL]: App screenshot, illustration, or mockup
  - No complex device frames required
  - Max-width: 100% of column
  - On mobile: moves below text column

Mobile adaptation:
  - Text column: full width, text-center
  - Visual: hidden or below (with reduced height)
  - CTA: full width
```

### [SECTION 3: TRUST SIGNALS]
```
Component: TrustSection
Background: white
Padding: var(--section-sm) 0

ROW 1: Logo/Award Marquee
  - Component: ScrollingMarquee
  - [LOGO_1] [LOGO_2] [LOGO_3] [LOGO_4] [LOGO_5]
  - All logos: grayscale, 50% opacity
  - animation: scroll-left 40s linear infinite
  - prefers-reduced-motion: pause or hide

ROW 2: Stats Row
  - Layout: flex, justify-between (desktop) / 2×2 grid (mobile)
  - 4 stats maximum:

  [STAT_1]:
    Number: [YOUR_NUMBER] — 48px, weight 900, var(--color-action)
    Label:  [YOUR_LABEL]  — 13px, weight 400, muted
  [STAT_2]: same pattern
  [STAT_3]: same pattern
  [STAT_4]: same pattern

  RULE: Always use exact numbers (not "thousands"). Label immediately below.
```

### [SECTION 4: CATEGORY/FEATURE BROWSER]
```
Component: CategoryBrowser (optional — use for multi-category products)
Background: var(--color-surface)
Padding: var(--section-lg) 0

Or replace with: FeatureList, ProductCategories, UseCases, etc.

Pattern: 2-column (or 1-column) with pill/tag navigation
Tags: pill radius (9999px), surface bg, border, hover bg shift
```

### [SECTION 5: FEATURE GRID]
```
Component: FeatureGrid
Background: white
Padding: var(--section-lg) 0

[SECTION_HEADING]: "[How you help] [who with what]"
  - 42px, weight 900, centered
  - Sentence case

[SECTION_SUBHEADING]: 1 line, 18px, muted, centered

GRID: 3 columns (2 tablet, 1 mobile)
Gap: 24px

FEATURE CARD (×3):
  Background: linear-gradient(135deg, [WARM_START], [WARM_END])
  Radius: 20px  ← display radius
  Padding: 28px 24px
  Hover: translateY(-3px) + shadow rgba(0,0,0,0.12) 0px 10px 30px
  Transition: 0.45s cubic-bezier(0.4, 0, 0.2, 1)

  [FEATURE_ICON]: 48px SVG, white
  [FEATURE_NAME]: bold, 20px, white, margin-top 16px
  [FEATURE_DESC]: 14-16px, white/80%, margin-top 8px, max-width 38ch

  Content formula:
    Name: "[2-3 word benefit label]"
    Desc: "[Mechanism (how it works)] + [outcome (what user gets)]"
```

### [SECTION 6: MID-PAGE CTA]
```
Component: CTASection
Background: dark authority (var(--color-authority) or darker variant)
Padding: var(--section-sm) 0

Content: centered

[HEADLINE]: "Ready to [specific outcome]?"
  - 32-36px, white, weight 700

[PROOF_LINE]: "[N]+ [users] already [doing the thing]"
  - 16px, white/70%

[PRIMARY_CTA]: action color, large, radius 8px
[SECONDARY_CTA]: white outline, ghost (optional — for alt path like "Watch demo")

[RISK_REDUCTION]: "No credit card · Cancel anytime · [Other risk reducer]"
  - 13px, white/60%, below CTA
```

### [SECTION 7: APP DOWNLOAD / SECONDARY CONVERSION] (if mobile app)
```
Component: AppBridge
Background: var(--color-surface)
Layout: 2-col (text+QR left, mockups right)

Left:
  Headline: "Available everywhere you work"
  [QR_CODE_SVG]: 120px, visible on desktop only
  [PLAY_STORE_BADGE]: official SVG
  [APP_STORE_BADGE]: official SVG

Right:
  [PHONE_MOCKUPS]: 2-3 screenshots in device frames

Mobile: Show app store links only (hide QR, center layout)
```

### [SECTION 8: FOOTER]
```
Component: Footer
Background: var(--color-surface)  ← same as main surface (lightly tinted)
Inner max-width: 1100px

4 columns:
  [Brand: Logo + tagline + social icons]
  [Company: About | Blog | Careers | Press]
  [Product: Features | Pricing | Changelog | Roadmap]
  [Legal: Privacy | Terms | Security | Cookies]

Bottom bar:
  © [YEAR] [BRAND]. All rights reserved.
  Color: muted (--color-muted)

Mobile: 1-column stacked, brand at top
```

---

## Full Page Component Tree

```tsx
<Layout>
  <Navbar logo={Logo} links={navLinks} cta="Start [action] for free" />

  <HeroSection
    trustBadge="[TRUST_BADGE_TEXT]"
    headline="[H1_HEADLINE]"
    subheadline="[SUBHEADLINE]"
    primaryCta="[Verb] [action] for Free"
    socialProof="⭐ [X.X] · [N]+ [users]"
    visual={<YourVisual />}
  />

  <TrustSection logos={logos} stats={stats} />

  <FeatureGrid
    heading="[SECTION_HEADING]"
    subheading="[SECTION_SUBHEADING]"
    features={[feature1, feature2, feature3]}
  />

  <CTASection
    headline="Ready to [outcome]?"
    proofLine="[N]+ [users] already..."
    primaryCta="[Verb] [action] for Free"
    riskReduction="No credit card · Cancel anytime"
  />

  {hasApp && <AppBridge qrCode={qr} />}

  <Footer />
</Layout>
```

---

## Tailwind Config Slots

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        action: '[YOUR_ACTION_COLOR]',
        'action-hover': '[YOUR_ACTION_HOVER]',
        authority: '[YOUR_AUTHORITY_COLOR]',
        surface: '[YOUR_SURFACE_COLOR]',
        'text-muted': '#86949d',
        'border-default': '[YOUR_BORDER_COLOR]',
      },
      fontFamily: {
        brand: ['[YOUR_FONT]', 'sans-serif'],
        content: ['Georgia', 'serif'],  // if you have content pages
      },
      borderRadius: {
        display: '20px',   // for cards, feature containers
        'display-xl': '32px',  // for course/product cards
        pill: '9999px',  // for tags, pill buttons
      },
      boxShadow: {
        card: '0 4px 12px rgba(0,0,0,0.08)',
        'card-hover': '0 10px 30px rgba(0,0,0,0.12)',
      },
      maxWidth: {
        container: '1296px',
        wide: '1440px',
        footer: '1100px',
        hero: '550px',
      },
    },
  },
}
```

---

## Accessibility Checklist (All Templates)

- [ ] Skip link: `<a href="#main-content" className="sr-only focus:not-sr-only">Skip to content</a>`
- [ ] Single `<h1>` — the hero headline
- [ ] Heading hierarchy: H1 → H2 → H3 (no skips)
- [ ] Nav: `<nav aria-label="Primary navigation">`
- [ ] Logo: `<img alt="[Brand name]" />`
- [ ] Trust logos: `<img alt="[Company] logo" />`
- [ ] Icon-only buttons: `aria-label` required
- [ ] All CTAs: descriptive text (not "Click here")
- [ ] Marquee: `@media (prefers-reduced-motion)` pause
- [ ] Feature cards: `role="article"` if standalone content
- [ ] Footer: `<nav aria-label="Footer navigation">`
