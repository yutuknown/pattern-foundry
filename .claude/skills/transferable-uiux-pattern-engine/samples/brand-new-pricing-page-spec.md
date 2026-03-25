# Sample: Brand-New Pricing Page — Clearflow (Finance SaaS)

> **Mode:** NEW_BRAND
> **Brand:** Clearflow — cash flow management for small businesses
> **Industry:** Fintech / SMB SaaS
> **Audience:** Small business owners, finance managers, 30–55
> **Tone:** Trustworthy, clear, no-BS. Financial credibility.
> **CTA Style:** Free trial (14 days)
> **Visual Personality:** Deep emerald authority + warm gold action + warm cream surface
> **Stack:** React + Tailwind CSS

---

## Originality Notes

Different from Sample:
- Industry: fintech (not EdTech)
- Audience: business owners (not students)
- Colors: emerald + gold (not orange + navy)
- Trust: SOC 2, bank integrations, accountant endorsements (not student count)
- CTA: "Start free trial" (not "for Free" — financial tools can charge from day 1)
- No app download bridge (web-first product)
- No dark mode required (SMB finance is desktop-professional)

DNA applied: bimodal radius, physical hover, trust sequence, section alternation, CTA adjacent trust.

---

## Page Goal
Convert comparison-shopping SMB owners to 14-day free trial. Primary objections: security, switching cost, complexity.

## Token Adaptation

```css
:root {
  --color-action: #d4a017;        /* warm gold — financial credibility + action */
  --color-action-hover: #b8860b;
  --color-authority: #064e3b;     /* deep emerald — trust, stability, growth */
  --color-surface: #f0fdf4;       /* very light green-tinted cream */
  --color-surface-warm: #fefce8;  /* warm cream alternate */
  --color-text: #111827;
  --color-muted: #6b7280;
  --color-border: #a7f3d0;        /* emerald-tinted border */
}
```

---

## Section Structure

### Section 1: Navbar (minimal — user is on pricing, high intent)
```
[Clearflow Logo] — left
[Features | Integrations | Security — center]
[Log in | Start free trial — right]
```

### Section 2: Pricing Header
```
Background: white
Content: centered, py-20

  [Trust compact row above heading:]
  [SOC 2 badge] [Bank-grade encryption] [QuickBooks certified] — icons + labels, 14px

  [H1: "Transparent pricing. No surprises."]
    36px, weight 700, color #111827

  [Sub: "Every plan includes bank-grade security, real-time sync, and 14-day free trial."]
    18px, muted, center, max-width 55ch

  [Annual/Monthly toggle]
    Pill switch: selected=authority bg + white text; unselected=muted
    "Save 2 months" badge next to annual
```

### Section 3: Pricing Cards
```
Background: color.surface (#f0fdf4 — lightly tinted)
Layout: 3-col (2 tablet, 1 mobile)
Gap: 24px

STARTER CARD (white, subtle border, radius 20px):
  [Badge: "For solo founders"]
  [$29] /mo — [or $23/mo billed annually]
  "Everything to get your cash flow under control."
  Features (7 items with ✓):
    - Bank account sync (up to 3)
    - Cash flow forecast (30 days)
    - Invoice tracking
    - Basic P&L report
    - CSV export
    - Email support
    - 1 user
  [CTA: "Start 14-day trial" — authority outline button]

PRO CARD (white, 4px top border in action/gold, radius 20px, shadow.card):
  [Badge: "Most popular" — gold bg, white text, pill]
  [$79] /mo — [or $63/mo annually]
  "For growing teams that need complete visibility."
  Features (includes all Starter plus):
    - Unlimited bank accounts
    - 90-day forecast
    - Accounts payable tracking
    - Custom reporting
    - QuickBooks sync
    - Priority support
    - 5 users
  [CTA: "Start free trial" — action fill button (gold), radius 8px]

ENTERPRISE CARD (deep emerald bg, white text, radius 20px):
  [Badge: "Enterprise"]
  [Custom pricing]
  "For finance teams with complex needs."
  Features (all Pro plus):
    - Multi-entity support
    - API access
    - SSO / SAML
    - Dedicated CSM
    - SLA guarantee
    - Unlimited users
  [CTA: "Talk to sales" — white outline]

All cards: hover translateY(-3px) + shadow increase (0.45s cubic-bezier)
Highlighted Pro: very slight scale(1.02) on desktop
```

### Section 4: Trust Before Signing Up
```
Background: white
Compact row (not full section):
  "Your data is protected by:"
  [SOC 2 Type II] [256-bit AES encryption] [99.9% uptime SLA] [Bank-level security]
  Each: icon + label, centered, muted
```

### Section 5: Feature Comparison Table
```
Background: color.surface-warm (#fefce8)
Sticky header row: Starter | Pro | Enterprise
Row groups:
  [Cash Flow Features]: 5 rows
  [Reporting]: 4 rows
  [Integrations]: 3 rows
  [Team & Access]: 3 rows
  [Support]: 3 rows
Each row: feature name | ✓/—/custom for each tier
Mobile: horizontal scroll with sticky first column
```

### Section 6: FAQ
```
Background: white
Section heading: "Common questions" — 32px, weight 700, left-aligned
5 questions (target financial objections):
  Q: "How does the free trial work?"
  Q: "Can I import my existing QuickBooks/Xero data?"
  Q: "Is my financial data secure?"
  Q: "Can I change plans or cancel anytime?"
  Q: "Do you offer discounts for accountants/bookkeepers?"
Component: accordion, aria-expanded, 0.3s slide
```

### Section 7: Final CTA Block
```
Background: #064e3b (deep emerald — authority, not just action)
Content: centered

  [Stats in gold:]
  2,800+ businesses | $4.2B cash flow managed | 99.9% uptime

  [Headline: "Join 2,800+ businesses who stopped guessing."]
    36px, white, weight 700

  [Sub: "14-day free trial. No credit card. Cancel anytime."]
    18px, white/80%

  [Primary CTA: "Start free trial" — gold fill, large, radius 8px]
  [Secondary: "Talk to sales →" — white ghost]
```

---

## Trust Signal Audit (Fintech-specific)

| Signal | Role | Placement |
|--------|------|-----------|
| SOC 2 badge | Security authority | Header trust row + footer |
| QuickBooks certified | Integration authority | Header trust row |
| 2,800+ businesses | Volume proof | Final CTA block |
| $4.2B managed | Scale proof | Final CTA block |
| 99.9% uptime | Reliability proof | Trust row + final CTA |
| 14-day trial, no card | Risk reduction | Sub in every section |
| FAQ: data security | Objection handling | FAQ section |

---

## Component Breakdown

```tsx
<PricingPage>
  <Navbar minimal />
  <PricingHeader
    h1="Transparent pricing. No surprises."
    trustRow={[SOC2, Encryption, QuickBooks]}
    toggle={annualMonthly}
  />
  <PricingCards
    cards={[Starter, Pro, Enterprise]}
    highlighted="Pro"
  />
  <SecurityTrustRow badges={[...]} />
  <ComparisonTable rows={features} tiers={3} />
  <FAQSection questions={financialFAQs} />
  <FinalCTA
    stats={[...]}
    headline="Join 2,800+ businesses..."
    cta="Start free trial"
    riskReduction="14-day free trial · No credit card · Cancel anytime"
    bg="emerald-950"
  />
  <Footer />
</PricingPage>
```

## Responsive Notes
- Pricing cards: 3 → 2 → 1 col
- Comparison table: horizontal scroll on mobile
- Trust row: 2×2 grid on mobile
- FAQ: accordion on all viewports

## Accessibility Checks
- [ ] Pricing cards: `aria-label="[Plan] pricing plan"`
- [ ] FAQ: `aria-expanded`, `aria-controls`
- [ ] Toggle: `role="switch"`, `aria-checked`
- [ ] Checkmark icons: `aria-hidden="true"` (text is present)
- [ ] Focus visible: gold ring on authority bg, emerald ring on light bg
