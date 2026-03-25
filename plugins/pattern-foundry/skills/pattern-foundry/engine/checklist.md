# Pre-Output Checklist

## Purpose
Run this before finalizing any generated output. Every item must pass.

---

## Phase 1: Originality Check

- [ ] No Sample logo, wordmark, or "Education Revolution" branding present
- [ ] Primary action color is NOT exact #fe6724 (unless user explicitly chose it)
- [ ] No "Sample Infinity", "Sample App", "Test Insights" feature names
- [ ] No Indian exam names (NEET/UPSC/JEE/CAT) unless user requested EdTech
- [ ] No specific student/user count stats from Sample (3.2 Crore, 150k+ ratings)
- [ ] Y Combinator badge or logo not included
- [ ] Exact source copy not reproduced ("Stop Wasted Effort Start Scoring More" etc.)
- [ ] Output would clearly work for a different company in a different industry
- [ ] PASS? If no → revise before proceeding

---

## Phase 2: Visual Hierarchy

- [ ] Single H1 per page
- [ ] Heading levels sequential (H1 → H2 → H3, no skips)
- [ ] Hero heading uses `clamp()` — NOT fixed px size
- [ ] Hero heading weight ≥ 700 (preferably 900)
- [ ] Stats: large number (≥ 40px) above small label (≤ 14px), never inline
- [ ] Primary CTA is visually distinct from secondary CTA
- [ ] Each section has one dominant element (not multiple competing elements)

---

## Phase 3: Spacing Rhythm

- [ ] Section vertical padding uses only 2 values (compact ~80px, large ~128px)
- [ ] No arbitrary padding values (px-[93px]) — use scale tokens
- [ ] Grid uses `gap` not `margin` on children
- [ ] Container has horizontal padding on all viewports
- [ ] Cards have adequate internal padding (≥ 20px)

---

## Phase 4: Color Application

- [ ] Action color (warm) used ONLY for CTAs and primary highlights
- [ ] Authority color (cool) used ONLY for headings, text, trust elements
- [ ] Surface color is lightly tinted (not pure white, not gray)
- [ ] White text on action color: verify ≥ 3:1 contrast ratio
- [ ] Error color (#e94e4d equivalent) used ONLY for errors, never decorative

---

## Phase 5: Component Correctness

- [ ] Display cards: radius ≥ 20px
- [ ] Form inputs: radius ≤ 8px
- [ ] Primary button: action color fill + white text
- [ ] Secondary button: outline or ghost — clearly weaker than primary
- [ ] Cards have hover state (translateY(-3px) + shadow increase)
- [ ] Cards: shadow.card at rest (not shadow.hover which is too heavy)

---

## Phase 6: CTA Architecture

- [ ] Primary CTA copy contains "Free" (if freemium context)
- [ ] CTA appears: above fold (hero) + mid-page + near-footer (3 minimum)
- [ ] Trust signal is adjacent to every primary CTA (within 200px)
- [ ] Trust signal sequence: volume → authority → quality → risk-reduction
- [ ] Risk-reduction copy present ("No credit card" / "Cancel anytime")
- [ ] Primary and secondary CTAs are clearly visually differentiated

---

## Phase 7: Accessibility

- [ ] Skip link: `<a href="#main-content">Skip to main content</a>` as first body element
- [ ] `<nav aria-label="Primary navigation">` on main nav
- [ ] All icon-only buttons: `aria-label` attribute
- [ ] All images: `alt=""` (decorative) or descriptive text (informative)
- [ ] All form inputs: visible `<label>` element (not placeholder-only)
- [ ] `:focus-visible` styles present — never `outline: none` without replacement
- [ ] Modals: `role="dialog"`, `aria-modal="true"`, focus trap, Escape close
- [ ] `@media (prefers-reduced-motion: reduce)` wraps all ambient animations

---

## Phase 8: Motion Quality

- [ ] Interactive cards have `transform: translateY(-3px)` on hover
- [ ] Shadow increases on card hover (from shadow.card to shadow.card_hover)
- [ ] Spatial transitions use `0.45s cubic-bezier(0.4, 0, 0.2, 1)`
- [ ] Color/opacity transitions use `0.2s`
- [ ] No distracting motion for non-interactive elements
- [ ] Marquee/shimmer animations have `prefers-reduced-motion` override

---

## Phase 9: Responsiveness

- [ ] Hero: 2-col desktop → 1-col mobile (visual below text)
- [ ] Feature grid: 3 → 2 → 1 column at lg/md/sm breakpoints
- [ ] Stats row: flex row → 2×2 grid on mobile
- [ ] Sidebar: NOT just `display:none` — accessible mobile alternative
- [ ] No horizontal scroll at 375px viewport width
- [ ] Touch targets: all interactive elements ≥ 44×44px on mobile
- [ ] Text remains readable on mobile (no overflow, no tiny text)

---

## Phase 10: Implementation Cleanliness

- [ ] `<nav>`, `<main>`, `<header>`, `<footer>`, `<section>` used correctly
- [ ] `<button>` for actions (never `<div onClick>`)
- [ ] `<a>` for navigation (never `<button>` for page navigation)
- [ ] No inline `style={{ color: '#xxx' }}` for design values — use tokens
- [ ] No magic numbers in class names (`px-[37px]`) — use scale tokens
- [ ] Images: `width` + `height` set to prevent layout shift (CLS)

---

## Final Score

Count passes: ___ / 40

- 38-40: Ship immediately
- 34-37: Ship with minor fixes (< 30 min)
- 28-33: Needs revision before shipping
- < 28: Major issues — rework required

**Never ship with a Phase 7 (Accessibility) score below 5/7.**
