# Pricing Page — Page Override

> **Inherits from:** design-system/MASTER.md

## Page Goal
Convert free users to paid subscribers. Zero confusion about tiers. Maximum clarity on value difference. Trust density near the buy button.

## Blueprint (Section Order)

```
01. NAVBAR (inherit from MASTER)

02. PRICING HEADER
    Background: white
    Content: centered
    - H1: "Simple, [qualifier] pricing" (32-40px)
    - Subheadline: "Start free. Upgrade when ready."
    - Annual/Monthly toggle (if applicable) — pill switch with subtle animation
    - Social proof micro: "[N]+ customers on [Plan]"

03. PRICING CARDS
    Background: color.surface.default (lightly tinted)
    Layout: 3-col (2 tablet, 1 mobile) OR 2-col if only Free+Pro
    Card anatomy:
      - Free: white bg, subtle border, radius.xl
      - Pro (highlighted): white bg, 4px top border (action color), radius.xl, shadow.card
      - Enterprise: dark navy bg, white text, radius.xl
    Badge: "Most Popular" on highlighted tier (action color, white text, pill)
    Price: 48-56px, bold → /month 16px muted → annual note 13px
    Feature list: checkmark (action color) + text, max 8 visible, "See all" expand
    CTA: Primary on Pro, Secondary on Free, Outline-white on Enterprise

04. COMPARISON TABLE (if 3+ tiers)
    Background: white
    Sticky header row with plan names
    Feature rows with ✓ / — / custom text
    Grouped by feature category
    Horizontal scroll on mobile (not reformatted)

05. FAQ ACCORDION
    Background: color.surface.default
    5-8 questions addressing conversion objections
    Component: click-to-expand, 0.3s slide-down, aria-expanded

06. TRUST + FINAL CTA
    Background: dark authority (navy family)
    Content: centered
    - Stats (volume + rating)
    - Headline: "Join [N] [users] on [Pro/Premium]"
    - Primary CTA: large, action color
    - Risk-reduction: "No credit card · Cancel anytime"

07. FOOTER (inherit from MASTER)
```

## Content Rhythm Override

Tier names: NOT vague ("Plus", "Max") — use functional names ("Free", "Pro", "Enterprise")
Price: always show the number prominently — never hide it
Risk-reduction copy: must appear immediately below every pay CTA
FAQ: answer the 3 biggest objections (cancel?, data security?, upgrade/downgrade?)

## CTA Override

Primary CTA on pricing: "Start [Plan] for Free" or "Start free trial" (NEVER "Buy Now")
Enterprise CTA: "Talk to Sales" or "Contact us" (never "Buy")
Free tier CTA: "Get started free" — de-emphasized style vs Pro CTA

## Trust Signal Override

Trust must appear ABOVE pricing cards (not just in the final CTA section).
Format: compact trust row — logo strip (grayscale) + rating + user count

## Component Emphasis

Pricing cards: radius.xl (32px) — large radius signals "friendly/consumer"
Highlighted card: extra visual weight via top border + very slight scale (103%)
FAQ: accordion, NOT static expanded — saves vertical space
