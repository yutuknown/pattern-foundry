# Sample: Brand-New Homepage — LearnPath (Engineering Career Training)

> **Mode:** NEW_BRAND
> **Brand:** LearnPath — AI-powered skill training for software engineers
> **Industry:** B2B/B2C EdTech + Career Development
> **Audience:** Mid-career software engineers, 25–40, looking to level up
> **Tone:** Technical but approachable. Confidence without arrogance.
> **CTA Style:** Freemium trial
> **Visual Personality:** Deep indigo authority + warm amber action + light steel-blue surface
> **Stack:** Next.js + Tailwind CSS

---

## Originality Notes

This is NOT Sample. Different:
- Industry: software engineering careers (not academic exams)
- Audience: professionals (not students)
- Colors: indigo + amber (not orange + navy)
- Font: Plus Jakarta Sans + Fira Code (not Lato + Georgia)
- Icons: mono-outline tech style (not colorful exam icons)
- Trust signals: GitHub stars, company logos, LinkedIn endorsements (not student count)

The DNA applied: bimodal radius, physical hover, fluid hero, trust sequence, section alternation.

---

## Page Goal
Convert visiting engineers to free account creation. Primary: skill assessment trial signup.

## Token Adaptation

```css
:root {
  --color-action: #d97706;        /* warm amber — adapted action color */
  --color-action-hover: #b45309;
  --color-authority: #312e81;     /* deep indigo — adapted authority */
  --color-surface: #eef0f8;       /* lightly indigo-tinted surface */
  --color-text: #0f172a;          /* near-black */
  --color-muted: #64748b;
  --color-border: #c7d2fe;        /* indigo-tinted border */

  /* Gradient: amber family */
  --gradient-warm: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);

  /* Confirmed spacing ratios applied */
  --section-lg: 128px;
  --section-sm: 80px;
}
```

## Section Structure

### Section 1: Navbar (sticky, 82px height)
```
[LearnPath Logo — left]
[Skills | Tracks | For Teams | Pricing — center]
[Log in | Start Free — right]
Background: white
Shadow: appears on scroll
Container: max-w-[1296px]
```

### Section 2: Hero (above-fold, 1024px complete)
```
Background: linear-gradient(90deg, #1e1b4b 0%, #312e81 100%)  [dark indigo]
Layout: 55% text left / 45% visual right

LEFT COLUMN (max-width: 550px):
  [Trust badge: "Trusted by engineers at Stripe, Vercel, Shopify"]
  [H1: "Level up faster. Ship better code."]
    font-size: clamp(28px, 4vw, 50px), weight 900, color white
  [Sub: "LearnPath creates a personalized skill path from your codebase — and closes your gaps."]
    18px, white/80%, max-width 44ch
  [Primary CTA: "Analyze my skills for free"]
    bg: #d97706 (amber), color white, radius 8px, py-3 px-6, weight 700
  [Social proof micro: "⭐ 4.8 · 12,000+ engineers improved their P/E skills"]
    13px, white/60%

RIGHT COLUMN:
  [Screenshot: LearnPath skill radar chart in dark terminal-style UI]
  [Device: No frame needed — data visualization is self-contextualizing]
```

### Section 3: Trust Signals
```
Background: white
Row 1: Logo strip [Stripe | Vercel | Shopify | Linear | Notion] — grayscale, 50% opacity
         Scrolling marquee: 40s linear infinite  ← same pattern, different logos
Row 2: Stats flex row (desktop) / 2×2 grid (mobile):
  [12k+]            [4.8/5]           [94%]               [2h avg]
  [engineers]       [rating]          [pass job screen]   [to see skill gap]
  weight 900, 48px  weight 900, 48px  weight 900, 48px    weight 900, 48px
  amber color       amber color       amber color         amber color
```

### Section 4: How It Works (not category browser — different product)
```
Background: color.surface (#eef0f8)
Section heading: "From confused to confident in 3 steps" — 42px, weight 900, center
3-col grid:
  [Step 1 Card: gradient amber]
    Icon: code bracket SVG (40px, white)
    "Connect Your Repo"
    "LearnPath reads your commits and PRs — zero manual input."
  [Step 2 Card: gradient amber-darker]
    Icon: chart SVG
    "Get Your Skill Radar"
    "AI maps your strengths, gaps, and growth opportunities."
  [Step 3 Card: white on indigo bg]
    Icon: checkmark-star SVG
    "Follow Your Path"
    "Daily micro-lessons that close your specific gaps."
All cards: radius 20px, hover translateY(-3px) + shadow increase
```

### Section 5: Feature Grid
```
Background: white
Features (alternating 2-col layout):

Feature 1: [Left: text | Right: screenshot]
  "Skill gap detection that's actually specific"
  "Not generic videos. LearnPath identifies which React hooks you use wrong — then fixes exactly that."

Feature 2: [Left: screenshot | Right: text]
  "Learning that fits your stack"
  "If you write TypeScript + Postgres, you don't get Python lessons. Ever."
```

### Section 6: Social Proof (Testimonials)
```
Background: color.surface
3-col cards:
  [Card 1]
    "Went from L3 to L4 in 8 months. LearnPath showed me my blind spots before my manager did."
    ⭐⭐⭐⭐⭐
    [Avatar: 40px] Jake R., Senior SWE at Linear
  [Card 2]
    "No other platform reads your actual code. This is the only tool that learns what you need."
    ⭐⭐⭐⭐⭐
    [Avatar] Priya M., Staff Engineer at Shopify
  [Card 3]
    "Used it for 6 weeks before my Google loop. Passed all 5 rounds."
    ⭐⭐⭐⭐⭐
    [Avatar] Carlos D., SWE at Google
Cards: white, radius 20px, shadow.card, hover lift
```

### Section 7: Mid-Page CTA
```
Background: #1e1b4b (dark indigo — high contrast)
Content: centered
  "12,000 engineers already know their gaps. Do you?"
  [Analyze my skills for free] — amber CTA, large, radius 8px
  "No credit card · Connects with GitHub · Results in 2 minutes"
```

### Section 8: Footer
```
Background: #eef0f8 (surface — mirrors Sample footer pattern)
Inner: max-width 1100px
4-col: LearnPath + tagline | Product | Company | Legal
Bottom: © 2025 LearnPath · Privacy · Terms
Color: #64748b (muted)
```

---

## Component Breakdown (React)

```tsx
// Page structure
<Navbar />
<HeroSection
  headline="Level up faster. Ship better code."
  sub="LearnPath creates a personalized skill path..."
  cta="Analyze my skills for free"
  trustBadge="Trusted by engineers at Stripe, Vercel, Shopify"
  socialProof="⭐ 4.8 · 12,000+ engineers"
  visual={<SkillRadarScreenshot />}
  bgGradient="from-[#1e1b4b] to-[#312e81]"
/>
<TrustSection
  logos={[Stripe, Vercel, Shopify, Linear, Notion]}
  stats={[...]}
/>
<HowItWorksSection steps={[...]} />
<FeatureSection features={[...]} alternating />
<TestimonialsSection testimonials={[...]} />
<CtaSection
  headline="12,000 engineers already know their gaps."
  cta="Analyze my skills for free"
  riskReduction="No credit card · Connects with GitHub · 2 minutes"
  bg="indigo-950"
/>
<Footer />
```

## Responsive Notes
- Hero: 2-col desktop → 1-col mobile (screenshot moves below text)
- Stats: flex → 2×2 mobile grid
- How it works: 3-col → 1-col mobile
- Features: alternating 2-col → 1-col mobile (always text above visual)

## Accessibility Checks
- [ ] Skip link to `#main-content`
- [ ] H1 one per page (hero headline)
- [ ] Logo strip: all logos have aria-label
- [ ] CTA buttons: focus ring in amber
- [ ] Marquee: prefers-reduced-motion stops animation
- [ ] Stats: each stat card has aria-label (not just visual number)
- [ ] testimonial: `<blockquote>` + `<cite>`

## Implementation Notes
```bash
# Fonts: next/font/google
import { 'Plus_Jakarta_Sans' } from 'next/font/google'
import localFont from 'next/font/local'  # Fira Code for any code examples

# Tailwind config extensions:
colors.action: '#d97706'
colors.authority: '#312e81'
colors.surface: '#eef0f8'
borderRadius.display: '20px'
borderRadius.display-xl: '32px'
```
