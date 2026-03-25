# Brand Adaptation Model

## Purpose
Define how to transform the extracted design intelligence into original work for any brand, industry, or audience — while maintaining the same quality level.

---

## The 3-Layer Adaptation Framework

```
Layer 1: KEEP AS-IS (Universal Structural Rules)
  These don't change regardless of brand:
  - Value before gate
  - Trust before CTA
  - Outcome-first headlines
  - Bimodal radius (functional vs display)
  - Physical hover (translateY-3px + shadow)
  - Fluid hero typography (clamp)
  - Section background alternation
  - Trust signal sequence (volume → authority → specificity → risk)
  - Heading hierarchy (H1 → H2 → H3, never skip)
  - Accessibility defaults (skip link, focus states, labels, reduced-motion)

Layer 2: ADAPT THE ROLE (Keep logic, change values)
  The role assignment stays the same, values change per brand:
  - Action color: must be warm/energetic → find the right hue for brand
  - Authority color: must be cool/trustworthy → find the right hue for brand
  - Surface: must be lightly tinted authority (10%) → derive from authority color
  - Font: must be readable humanist sans → find equivalent (Nunito, DM Sans, Plus Jakarta...)
  - Spacing scale: keep the 4px base unit, adjust section padding by content density

Layer 3: BRAND-SPECIFIC (Entirely new per brand)
  - Exact color hues
  - Specific font family
  - Icon style and illustration treatment
  - Copy tone and voice
  - Logo and wordmark
  - Specific content and product names
  - Industry-specific section types (e.g., "exams" → "courses" → "templates")
```

---

## Industry Adaptation Presets

### B2B SaaS (e.g., project management, analytics, CRM)

```
Visual Tone: Professional, data-dense, feature-complete
Action color: Indigo or deep blue-violet (#6366f1 family)
Authority color: Slate or charcoal (#334155 family)
Surface: Very light gray-blue (#f1f5f9)
Font: Inter (UI everywhere), no Georgia (no long-form content)
Radius: Smaller overall — radius.sm for most cards (10-14px)
Density: Higher — more features visible above fold
Trust: Case studies + customer logos + G2/Capterra rating
CTA: "Start free trial" or "Book a demo" (not "for Free")
Dark mode: Yes, common in developer/analyst tools
Motion: Faster (0.3s spatial), more minimal — no marquee
```

### Healthcare / Medical

```
Visual Tone: Clinical confidence, accessible, trustworthy above all
Action color: Medical teal (#0d9488 family) or calming blue
Authority color: Deep clinical navy or dark slate
Surface: Soft mint or clinical white (very low saturation)
Font: Source Serif (for credibility) + Inter (UI)
Radius: Medium (10-16px) — not too playful (32px), not harsh (0px)
Density: Medium-low — patients need breathing room
Trust: Medical credentials, certifications, HIPAA badge, doctor endorsements
CTA: "Start [action]" (remove "for Free" — may undermine medical credibility)
Accessibility: WCAG AAA target (patients may have disabilities)
Motion: Minimal — avoid anxiety-inducing animations
```

### Finance / Fintech

```
Visual Tone: Security-forward, premium, precise
Action color: Emerald green (#10b981) or deep amber
Authority color: Midnight blue or dark charcoal
Surface: Warm cream or pale blue-gray
Font: Inter + DM Serif Display (for premium headlines)
Radius: Medium-small (6-12px) — precision over friendliness
Density: Medium-high — financial data needs to be visible
Trust: Security certifications (SOC2, PCI DSS), bank logos, audit reports
CTA: "Open your account" or "Get started" (free is implied or not relevant)
Dark mode: Often yes — financial dashboards used in professional settings
Motion: Subtle — numbers animate with CountUp, not spatial motion
```

### Developer Tools / DevOps

```
Visual Tone: Minimal, efficient, code-native, no marketing fluff
Action color: Purple (#8b5cf6) or green (#22c55e) — developer colors
Authority color: Zinc or slate (#52525b)
Surface: Near-white or GitHub-like off-white (#f6f8fa)
Font: Inter (UI) + Fira Code/JetBrains Mono (code)
Radius: Minimal-medium (4-8px) — tools feel precise
Density: High — developers don't mind dense information
Trust: GitHub star count, npm downloads, open source, company logos using it
CTA: "npm install [pkg]" or "Read the docs" or "Try the playground"
Dark mode: Required — most developers prefer it
Motion: Almost none — performance and clarity > aesthetics
```

### Consumer Lifestyle / Fitness / Wellness

```
Visual Tone: Motivational, energy, aspiration, personal
Action color: Coral, vivid orange, or energetic yellow-green
Authority color: Dark green or warm charcoal
Surface: Warm off-white or warm light beige
Font: Nunito or Poppins (friendly round edges) + DM Serif for hero
Radius: Large (20-40px) — max friendliness
Density: Low — emotional pages need breathing room
Trust: Before/after stories, transformation testimonials, influencer endorsements
CTA: "Start your journey" or "Join [N] [people]"
Dark mode: Optional — wellness is often light
Motion: More expressive — celebration animations for milestones
```

### Education / EdTech (Adapted — not cloned)

```
Visual Tone: Supportive, credible, goal-oriented
Action color: Warm amber or soft orange (NOT Sample's specific #fe6724)
Authority color: Dark blue-gray or slate-navy (NOT #193f68 exactly)
Surface: Soft lavender or warm cream (NOT #e9f1fc exactly)
Font: Nunito (friendly) + Georgia (content) OR DM Sans + Source Serif
Radius: Same bimodal strategy (adapt to slightly more playful if K-12)
Density: Medium — students need focus but also engagement
Trust: Test score improvements, certifications, institution partnerships
CTA: "Start learning for free" (keep the "free" — same principle)
Dark mode: Required for content pages
Motion: Same physical hover principle, same shimmer loading
```

---

## Adaptation Checklist

When adapting to a new brand, verify each of these:

**Colors:**
- [ ] Action color is warm/energetic (not cool or muted)
- [ ] Authority color is cool/trustworthy (not warm or bright)
- [ ] Surface color is ≤10% saturation (not too dark, not pure white)
- [ ] White text on action color passes 3:1 contrast (large text)
- [ ] Dark text on surface color passes 4.5:1 (body text)
- [ ] Error color is distinct from action and authority colors

**Typography:**
- [ ] Hero heading uses `clamp()` — not fixed px
- [ ] Body text ≥ 16px (≥ 18px for content-heavy pages)
- [ ] Maximum 2 font families in a single UI context
- [ ] Long-form content uses a different (more readable) font than marketing

**Structure:**
- [ ] Warm-cool role assignment is maintained
- [ ] Bimodal radius applied (functional vs display)
- [ ] Physical hover on interactive cards
- [ ] Trust signal sequence follows volume → authority → quality → risk

**Content:**
- [ ] Headline is outcome-first (not feature-first)
- [ ] Primary CTA includes risk-reduction language
- [ ] Stats show specific number + context label
- [ ] No vague adjectives ("amazing", "revolutionary") in headlines

**No Sample Brand Carried Forward:**
- [ ] No exact orange #fe6724 used
- [ ] No "Sample", "Infinity", "Education Revolution" naming
- [ ] No Indian exam names unless the user is in EdTech
- [ ] No exact stat claims (3.2 Crore etc.)
- [ ] No exact headlines or taglines

## Confidence
**High** — adaptation model derived from structural analysis of what is brand-specific vs universal across multiple comparable platforms.
