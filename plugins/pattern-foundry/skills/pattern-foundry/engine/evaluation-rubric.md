# Evaluation Rubric

## Purpose
Score any UI output against the extracted quality bar. Use before finalizing any generation.

---

## Scoring System
1–10 per dimension. **Ship threshold: all dimensions ≥ 7.**

---

## Dimension 1: Originality (1-10)

**10:** No brand-specific elements from source. A competitor of Sample would not recognize their DNA. Output works for a completely different industry.
**7:** One or two shared visual elements that could be coincidental (similar radius, similar warm color). No branded copy or logos.
**4:** Clearly influenced by source brand — similar color, similar feature names, similar stats format.
**1:** Direct clone. Same copy, same colors, same logo style.

**Check:**
- [ ] No exact #fe6724 used as primary
- [ ] No "Sample", "Infinity", "Education Revolution"
- [ ] No exam names (NEET/UPSC/JEE) unless user requested EdTech
- [ ] No source site's exact stat counts
- [ ] Output works for a different industry without changes

---

## Dimension 2: Visual Hierarchy (1-10)

**10:** Clear dominant element per section. Heading levels H1→H2→H3, never skipped. User eye path is unambiguous.
**7:** Mostly clear. One or two sections have competing elements.
**4:** Multiple elements competing for attention. Heading levels inconsistent.
**1:** No visual hierarchy. Everything feels the same weight.

**Check:**
- [ ] One H1 per page
- [ ] Hero heading is the largest element above fold
- [ ] Stats: number dominates (48px+), label subordinate (13px)
- [ ] CTA button visually distinct from surrounding text

---

## Dimension 3: Spacing Rhythm (1-10)

**10:** Section padding is one of two values (compact ~80px or large ~128px). All component gaps from token scale. Zero arbitrary pixel values.
**7:** Mostly consistent. 1-2 sections feel off.
**4:** Multiple different section padding values. Arbitrary numbers appear.
**1:** Random spacing throughout.

**Check:**
- [ ] Section vertical padding: only 2 values used
- [ ] Grid gap from token (16px, 24px, or 30px)
- [ ] No `px-[37px]` style magic numbers in Tailwind
- [ ] Container has correct horizontal padding per breakpoint

---

## Dimension 4: CTA Logic (1-10)

**10:** 3 CTA placements on long pages. Trust signal adjacent to every primary CTA. Copy follows "[Verb] [action] for Free" formula. Primary clearly differentiated from secondary.
**7:** 2 CTAs. Trust usually adjacent. Copy mostly good.
**4:** 1 CTA only. "Get Started" as copy. Trust not adjacent.
**1:** No CTA or unclear what to do.

**Check:**
- [ ] CTA in hero (above fold)
- [ ] CTA in mid-page (after value demonstration)
- [ ] CTA at end (before footer)
- [ ] "Free" in primary CTA (if freemium)
- [ ] Trust signal within 2 visual units of each CTA

---

## Dimension 5: Trust Placement (1-10)

**10:** Volume → Authority → Quality → Risk-reduction in correct sequence. Trust appears before every primary CTA cluster.
**7:** Trust present and adjacent to CTAs. Sequence slightly off.
**4:** Trust exists but appears randomly or after CTAs.
**1:** No trust signals.

**Check:**
- [ ] Volume proof (N+ users) appears before authority proof
- [ ] Risk-reduction ("No credit card") appears last
- [ ] Trust visible in hero without scrolling
- [ ] Specific numbers (not vague "millions")

---

## Dimension 6: Accessibility (1-10)

**10:** Skip link, labeled nav, single H1, sequential headings, visible focus, all images have alt, all forms have labels, modals have focus trap, `prefers-reduced-motion` on animations.
**7:** Focus visible, alt text on key images, forms have labels. Missing skip link or reduced-motion.
**4:** Focus not visible. Some missing labels. No `prefers-reduced-motion`.
**1:** No accessibility consideration.

**Check:**
- [ ] `<a href="#main-content">Skip to content</a>` at top
- [ ] `<nav aria-label="...">` on all navs
- [ ] All inputs: visible `<label>`, not placeholder-only
- [ ] All icon buttons: `aria-label`
- [ ] `:focus-visible` styled, not suppressed
- [ ] `@media (prefers-reduced-motion: reduce)` on marquee + shimmer

---

## Dimension 7: Motion Quality (1-10)

**10:** Cards lift `translateY(-3px)` on hover. Color changes 0.2s. Spatial changes 0.45s cubic-bezier(0.4,0,0.2,1). No distracting loops. All loops reduced-motion safe.
**7:** Card hover present. Transitions reasonable. One timing issue.
**4:** No hover states or only color change (no physical lift). No reduced-motion.
**1:** No motion or excessive/distracting motion.

**Check:**
- [ ] Interactive cards: `transform: translateY(-3px)` on hover
- [ ] Cards: shadow increases on hover
- [ ] Spatial easing: `cubic-bezier(0.4, 0, 0.2, 1)` (not `linear`)
- [ ] Color changes: 0.2s (not 0.45s)
- [ ] Ambient animations have `prefers-reduced-motion` override

---

## Dimension 8: Responsiveness (1-10)

**10:** 3→2→1 column grid collapse at correct breakpoints. Hero stacks on mobile. Sidebars have accessible mobile alternative (not just display:none). No horizontal scroll at 375px. Touch targets ≥ 44px.
**7:** Grid collapses. Hero mostly works. Minor mobile issues.
**4:** Grid doesn't fully collapse. Mobile hero broken.
**1:** Not responsive.

**Check:**
- [ ] 3-col → 2-col at md (768px) → 1-col at sm (640px)
- [ ] Hero: 2-col → 1-col stacked on mobile
- [ ] Stats: flex row → 2×2 grid on mobile
- [ ] Sidebar: accessible mobile alternative (not display:none)
- [ ] No horizontal scroll at 375px viewport width
- [ ] All interactive elements: min 44×44px on touch

---

## Dimension 9: Component Coherence (1-10)

**10:** Bimodal radius applied correctly (functional 3-8px, display 20-32px). Button hierarchy clear (primary → secondary → ghost). Card variants consistent. Shadow earned (hover only).
**7:** Mostly coherent. 1-2 component issues.
**4:** Radius mixed without logic. Button hierarchy unclear. Heavy shadows always-on.
**1:** No component system evident.

**Check:**
- [ ] Display cards: `radius-lg` (20px) or `radius-xl` (32px)
- [ ] Form inputs: `radius-sm` or `radius-md` (5-8px)
- [ ] Primary button: action color fill, white text
- [ ] Secondary: outline or ghost, never same visual weight as primary
- [ ] Cards: no heavy shadow at rest; shadow earned on hover

---

## Dimension 10: Implementation Cleanliness (1-10)

**10:** Semantic HTML. Tailwind tokens (not magic numbers). Components properly decomposed. No inline styles for design values. Accessible elements use correct HTML semantics.
**7:** Mostly clean. Some inline styles or magic numbers.
**4:** Inline styles common. No token consistency. Random class names.
**1:** Pure inline styles. No component structure.

**Check:**
- [ ] `<h1>`, `<h2>` (not `<div className="text-4xl">`)
- [ ] `<nav>` for navigation (not `<div>`)
- [ ] `<button>` for actions, `<a>` for navigation
- [ ] No `style={{ color: '#fe6724' }}` — use Tailwind `text-action`
- [ ] No `px-[37px]` — use `px-9` or custom token

---

## Total Score + Verdict

| Total | Verdict |
|-------|---------|
| 90-100 | Ship immediately |
| 80-89 | Ship with minor polish (30min) |
| 70-79 | Needs fixes before shipping |
| 60-69 | Requires significant revision |
| <60 | Major rework needed |

**Never ship a dimension that scores below 5 — even if total score is acceptable.**
An accessibility score of 3 fails the user, regardless of how the hero looks.
