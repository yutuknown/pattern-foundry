# Transferable Principles

## Purpose
Abstract, brand-neutral principles extracted from Sample — usable for ANY industry, ANY product, ANY visual style.

## Evidence
Derived from 4-page Playwright inspection + live CSS extraction.

---

## P1: Value Before Commitment
**The principle:** Deliver genuine value before asking for anything.
**Evidence:** Sample content pages are fully readable without signup. Free tier is actually useful.
**Application:** Any product with a freemium or trial model.
**Anti-pattern:** Gating the first 3 lines of content with a login wall.
**Rule:** Show 30%+ of real value before presenting any conversion gate.

---

## P2: Outcome-First Messaging
**The principle:** Headlines describe what the user achieves, not what the product does.
**Evidence:** "Start Scoring More" — focuses on user outcome. H2s name benefits ("Exam-Focused Smart Notes"), not features ("Note-taking Module").
**Application:** Every page headline in every industry.
**Anti-pattern:** "The most comprehensive [category] platform with 200+ features."
**Rule:** Test every headline: can the user complete "After using this, I will ___"?

---

## P3: Layered Trust Architecture
**The principle:** Trust signals must appear in a specific escalating sequence.
**Evidence:** Scrolling awards (recognition) → student count (volume) → 4.7 rating (quality) → "free" CTA (risk-free).
**Sequence:**
1. Volume proof (social proof at scale)
2. Authority proof (3rd party recognition/backer/award)
3. Quality proof (rating + review count)
4. Risk reduction (free/no card/cancel anytime)
**Application:** Every product where trust must be earned (most consumer products).
**Rule:** Never put risk-reduction before volume proof — establish scale first, then remove fear.

---

## P4: Warm-Cool Color Role Assignment
**The principle:** Pair a warm energetic color (action) with a cool authoritative color (trust). Assign each a spatial domain.
**Evidence:** Orange (#fe6724) = CTAs, highlights. Navy (#193f68) = headings, text, secondary UI. They never compete.
**Application:** Any consumer B2C or B2B product needing both credibility and energy.
**Role rule:** Warm color → spatial domain of "doing" (buttons, CTAs, active states). Cool color → spatial domain of "knowing" (text, headings, trust elements). NEVER swap.

---

## P5: Bimodal Border Radius
**The principle:** Use two radius scales: small for functional UI, large for display UI. The shape signals intent.
**Evidence (Playwright):** Functional: 4px (.crses_tag), 5px (badges), 8px (auth modal). Display: 20px (feature cards), 32px (course cards), 60px (pill CTAs).
**Application:** Any product interface. This principle works regardless of industry or brand.
**Rule:** If it's a tool the user operates (input, dropdown, tag), use small radius. If it's a container the user looks at (card, feature block, course), use large radius.

---

## P6: Physical Hover — Not Chromatic
**The principle:** Interactive elements must move spatially on hover, not just change color.
**Evidence (Playwright):** `transform: translateY(-3px)` + `box-shadow` increase on cards. Transition: 0.45s cubic-bezier(0.4,0,0.2,1).
**Application:** Every card-based UI where cards are destinations.
**Why physical:** Physical metaphor (lifting) is more universally understood than color shift. It works even for users with color vision deficiencies.
**Rule:** Cards that are links must lift. The lift amount is 3px — enough to signal interactivity, subtle enough to not distract.

---

## P7: Fluid Hero Typography
**The principle:** The hero heading must scale fluidly with viewport using `clamp()`.
**Evidence:** Direct CSS extraction: `clamp(28px, 4vw, 50px)` on hero heading. Weight 900 (confirmed computed).
**Application:** Every marketing page with a hero section.
**Rule:** `font-size: clamp(min, [2-5]vw, max)`. Never fixed px for the most important text on the page.
**Why:** Fixed px headings break at unusual viewports (large monitors, portrait tablets). `clamp()` is always correct.

---

## P8: Section Background Alternation
**The principle:** Adjacent sections must never share the same background color.
**Evidence:** Homepage: dark (hero) → white (trust) → surface (categories) → white (features) → dark (CTA) → surface (app download) → surface (footer).
**Application:** Any multi-section marketing page.
**Pattern:** Dark → White → Surface → Dark → White/Surface → Surface (footer)
**Rule:** At minimum, alternate between white and surface (lightly tinted). Use dark backgrounds for maximum contrast CTA sections.

---

## P9: Stats Anatomy — Number Dominates Label
**The principle:** In any metric display, the number is the dominant element and the label is subordinate.
**Evidence:** "3.2 Crore+" at 48-64px bold, "Students on Sample" at 13-14px muted, immediately below.
**Application:** Any trust/stats section, dashboard metrics, KPI displays.
**Rule:** Number must be 3-4x the size of its label. Never put them inline. Never label above number.

---

## P10: Progressive Freemium Gate
**The principle:** Design the upgrade path as a staircase, not a wall.
**Evidence:** View free content → Create free account → Join free course → Install app → Upgrade to premium. Each step is smaller than the last.
**Application:** Any freemium SaaS, content platform, EdTech product.
**Rule:** Never gate with payment as the first decision. The first gate is always free (email/OAuth). Payment comes after the user has experienced real value at least twice.

---

## P11: Content Page Reading Discipline
**The principle:** Long-form content pages must support reading (ToC, dark mode) without interrupting it (no intrusive modals).
**Evidence:** Sample notes pages: sticky ToC sidebar, dark mode toggle in header, breadcrumbs, embedded MCQs — all supporting, none interrupting.
**Application:** Documentation, knowledge bases, blog posts, study materials.
**Rule:** ToC for any content >800 words. Dark mode toggle on any content page used for extended reading. CTAs are inline at natural stopping points, not overlay interruptions.

---

## P12: App-Web Bridge Design
**The principle:** For mobile-first products, the web's job is to be a great acquisition channel for the mobile app.
**Evidence:** QR code + App Store badges + phone mockups in the "Get the App" section. All optimized for desktop-to-mobile conversion.
**Application:** Any consumer product where the mobile app is the primary experience.
**Rule:** Desktop users get: QR code + store badges. Mobile users get: direct app store deep links (no QR). Never show QR code on mobile — it's useless there.

---

## Brand Adaptation Model

This system can be adapted to any industry by changing the **surface values** while keeping the **role assignments**:

| Role | Source Value | Healthcare | Finance | Developer Tools | Luxury |
|------|-------------|-----------|---------|-----------------|--------|
| Action | warm orange | teal | emerald | purple | champagne |
| Authority | dark navy | dark slate | charcoal | midnight | near-black |
| Surface | light blue | soft mint | warm cream | cool gray | ivory |
| Gold | #f0b400 | bronze | gold | amber | gold |
| Text | #111111 | same | same | same | same |

**What never changes across adaptations:**
- Role assignment (warm=action, cool=authority)
- Bimodal radius strategy
- Trust signal sequence
- Physical hover principle
- Fluid hero typography
- Value-before-gate principle

## Confidence
**High** for all principles — derived from directly confirmed CSS values and observed behavior patterns.
