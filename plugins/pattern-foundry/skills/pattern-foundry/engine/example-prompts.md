# Example Prompts — 15+ Real Examples

## Purpose
Ready-to-paste prompts that activate the skill correctly.

---

### 1. New SaaS Homepage (New Brand Mode)
```
Using pattern-foundry [NEW_BRAND_MODE]:

Brand: Synthflow — AI-powered customer interview platform
Industry: B2B SaaS / UX Research
Audience: Product managers and UX researchers at tech companies
Tone: Professional but approachable. Data-confident.
CTA: Freemium ("Start free")
Palette: Deep purple authority + warm coral action + light lavender surface
Dark mode: No (marketing page)
Stack: Next.js 14 + Tailwind CSS

Generate:
- Complete homepage spec (all sections with content hierarchy)
- Adapted token set (don't use Sample colors)
- React component breakdown
- Tailwind class plan
- Accessibility checklist
```

---

### 2. Generic SaaS Pricing Template (Template Mode)
```
Using pattern-foundry [TEMPLATE_MODE]:

Template: SaaS freemium pricing page
Industry range: Any B2C/B2B SaaS with 3 tiers
Sections: Header, 3 pricing cards, comparison table, FAQ, final CTA
Complexity: Standard
Stack: React + Tailwind CSS

Generate a fill-in-the-blank template. All content as [PLACEHOLDER].
All structure and interaction rules from the extracted quality system.
Include: component tree, Tailwind class map, accessibility requirements.
```

---

### 3. EdTech Homepage (Different Stack, Different Audience)
```
Using pattern-foundry [NEW_BRAND_MODE]:

Brand: Skillvault — professional certification training for accountants
Industry: Professional EdTech / Finance Education
Audience: CPAs and accounting students, 25-45
Tone: Credible, professional, clear. Not playful.
CTA: "Start free trial" (not "for Free" — B2B EdTech)
Palette: Slate authority + amber action + warm cream surface
Stack: React + Tailwind CSS

Apply: freemium conversion structure, trust signal stacking, section alternation.
Do NOT use: any Sample-specific branding, colors, or exam content.
Generate complete homepage spec + JSX components.
```

---

### 4. Developer Tool Landing Page (Landing Mode)
```
Using pattern-foundry [PAGE_GEN_MODE]:

Product: Lognow — structured logging SDK for Node.js
Page: Feature landing page (single feature focus)
Goal: Drive npm install + docs read
Audience: Node.js developers, pragmatic, impatient
Tone: Minimal, technical, zero fluff
CTA: "npm install lognow" (primary) + "Read the docs" (secondary)
Stack: Next.js + Tailwind

Override: No warm gradient cards — use flat dark cards (developer aesthetic)
Override: Smaller radius (8px for cards) — precision over friendliness
No QR code / no app badges
Generate: minimal landing page spec. Sections: hero, feature demo, code snippet, social proof (npm downloads + GitHub stars), CTA.
```

---

### 5. Healthcare Service Homepage (High-Trust)
```
Using pattern-foundry [NEW_BRAND_MODE]:

Brand: Healpath — telehealth platform for chronic disease management
Industry: Digital Health / Telehealth
Audience: Adults 40-65 managing chronic conditions
Tone: Warm, reassuring, clinical authority. Not overly tech.
Trust level: Maximum — medical context, skeptical audience
CTA: "Talk to a doctor today" (NOT "free" — medical context)
Palette: Calm teal authority + soft rose action + mint surface
Stack: React + Tailwind
Accessibility target: WCAG AAA (patients may have disabilities)
Dark mode: No

Trust signals to include: board-certified doctors, HIPAA compliant, insurance accepted
Avoid: overly energetic motion, aggressive CTAs, excessive statistics
Generate: homepage spec with healthcare-appropriate trust architecture
```

---

### 6. UI Audit (Audit Mode)
```
Using pattern-foundry [AUDIT_MODE]:

Here is the current homepage implementation: [paste code]

Audit against the extracted quality system. I want:
1. Score on all 10 dimensions (1-10)
2. Total score and verdict
3. Top 5 issues ordered by user impact
4. For each issue: current state → recommended fix → code example
5. Quick wins (changes taking <1 hour)

Focus: CTA placement, trust signals, spacing rhythm, and mobile responsiveness.
```

---

### 7. Upgrade Weak UI (Audit + Redesign)
```
Using pattern-foundry [AUDIT_MODE] then [SYSTEM_EXPAND_MODE]:

Current state: Generic Bootstrap homepage with:
- H1: "Welcome to Our Platform"
- CTA: "Sign Up" (no free signal, no value prop)
- No trust signals
- Flat layout, no section rhythm
- All buttons same size
- No hover states

Apply the extracted quality system to redesign this page.
Give me: critique, then upgraded spec, then React/Tailwind code plan.
Keep the same product (replace all copy with new copy following content rhythm rules).
```

---

### 8. Multi-Page SaaS Site
```
Using pattern-foundry:

I'm building a complete 5-page SaaS site for:
Brand: Mosaic — content analytics for media companies
Industry: B2B SaaS / Media Tech
Audience: Content strategy teams at publishers

Generate specs for all 5 pages in order:
1. Homepage [NEW_BRAND_MODE]
2. Pricing [PAGE_GEN_MODE]
3. Features [PAGE_GEN_MODE]
4. Docs index [PAGE_GEN_MODE]
5. Blog post [PAGE_GEN_MODE]

Palette: Charcoal authority + warm amber action + soft cream surface
Stack: Next.js + Tailwind
Dark mode: Yes for docs

Ensure visual consistency across all pages (same tokens, same component variants).
```

---

### 9. Dashboard Shell
```
Using pattern-foundry [PAGE_GEN_MODE]:

Product: TrackPulse — social media analytics dashboard
Page: Main dashboard shell (logged-in, primary workspace)
Goal: Show key metrics, enable quick content review
Audience: Social media managers
Density: High (lots of data to show)
Dark mode: Yes (power users prefer it)
Stack: React + Tailwind
Mobile: Sidebar collapses to bottom nav

Components needed:
- Sticky top bar with search + notifications + avatar
- Sidebar with 6 nav items + settings + help
- Stats row (4 cards with trend indicators)
- Content performance table (sortable)
- Quick-post sidebar widget

Apply: physical hover on stat cards, action color for active/positive indicators,
dark mode fully supported via Tailwind dark: variants.
```

---

### 10. Content/Notes Template (Template Mode)
```
Using pattern-foundry [TEMPLATE_MODE]:

Template: Long-form content / knowledge base article page
Industry range: EdTech, SaaS docs, any product with deep content
Complexity: Full (ToC sidebar, dark mode, breadcrumbs, embedded CTAs)
Stack: React + Tailwind
Dark mode: Required
Accessibility: WCAG AA (screen reader + keyboard users)

Generate: complete content page template with all [PLACEHOLDER] slots.
Must include: 4-level breadcrumb, sticky ToC sidebar, body text at 18px/1.6lh,
4 callout box variants (info/warning/error/tip), code blocks with copy button,
mobile ToC replacement (accessible, not just display:none).
```

---

### 11. Adapted Color System
```
Using pattern-foundry [SYSTEM_EXPAND_MODE]:

I have a fitness app brand:
  Brand color: Vibrant coral #ef4444
  Industry: Fitness / Wellness
  Personality: Energetic, motivational, aspirational

Using the extracted quality system, build the full token set:
- Adapt action color (coral family — not Sample orange)
- Derive authority color (complementary cool)
- Derive surface color (10% tint)
- Verify contrast ratios for accessibility
- Output: complete tokens.json + tailwind.config.js
```

---

### 12. Redesign Request
```
Using pattern-foundry [AUDIT_MODE]:

Redesign brief: The current [ProductName] homepage feels generic and dated.
It was built with a Bootstrap template, has no hover states, uses "Get Started"
as the only CTA, and has no trust signals.

Apply the extracted quality system to produce:
1. A critique identifying the 8 worst violations
2. A new section structure (keeping the same product)
3. New CTA copy following the formula
4. Component upgrade plan (hero, feature cards, CTA block)
5. Tailwind code for the new hero section as a starting point
```

---

### 13. Mobile-First App Landing Page
```
Using pattern-foundry [NEW_BRAND_MODE]:

Brand: Moodloop — daily mental wellness journal app
Industry: Consumer wellness / Mobile app
Audience: Adults 18-35, anxious or burned-out
Tone: Calming, supportive, personal. Not clinical.
CTA: "Download free" (primary) + QR code on desktop
Palette: Soft lavender authority + warm amber action + very light sand surface
Stack: React + Tailwind
Mobile viewport: primary design target

Include: desktop-to-mobile bridge (QR + store badges + phone mockups)
Apply: prefers-reduced-motion (users with anxiety may be sensitive)
Avoid: aggressive countdown timers, fear-based copy, excessive statistics
```

---

### 14. Pricing Page for Enterprise
```
Using pattern-foundry [PAGE_GEN_MODE]:

Product: Vaultify — enterprise document security platform
Page: Pricing page
Tiers: Starter ($0, up to 5 users) | Business ($299/mo) | Enterprise (custom)
Audience: IT directors and procurement teams at Fortune 500
Tone: Professional, security-focused, compliance-aware
Trust signals: SOC 2 Type II, ISO 27001, GDPR compliant
CTA style: "Request demo" (enterprise doesn't buy self-serve)

Generate: complete pricing page with security trust signals woven throughout.
```

---

### 15. Brand Neutrality Check
```
Using pattern-foundry:

Review this page spec I've generated: [paste spec]

Run the anti-copy guardrail check:
1. Identify any elements that are too close to the Sample source brand
2. Identify any elements that need adaptation
3. Confirm: could this pass as a completely different company's website?
4. List any remaining [FILL:] placeholders that need values
```
