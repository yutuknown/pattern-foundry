# Extracted Style DNA

## Purpose
Single-page design fingerprint — the minimum required reading to understand what makes this system work. Paste this into any prompt to anchor Claude to the quality system.

---

## The DNA (Copy-Paste Block for Prompts)

```
DESIGN DNA — transferable-uiux-pattern-engine v2.0
Source: Live Playwright extraction from high-quality consumer EdTech product

COLOR ROLES (adapt hues, keep roles):
  color.action.primary:    warm orange family — CTAs and primary highlights ONLY
  color.authority.primary: dark navy family   — headings, text, trust elements ONLY
  color.surface.default:   lightly tinted (10% authority tint) — section backgrounds
  color.text.primary:      near-black (#111)
  color.semantic.gold:     achievement/rating accent
  RULE: Never use authority color as CTA. Never use action color as text.

TYPOGRAPHY (confirmed live values):
  font.brand:    Lato (or equivalent humanist sans) — all UI
  font.content:  Georgia (serif) — long-form reading only
  text.hero:     clamp(28px, 4vw, 50px), weight 900 — FLUID, NEVER FIXED
  text.display:  42px, weight 900 — section headings
  text.body:     18px, line-height 1.6 — content pages
  Casing: Sentence case for CTAs. Never ALL CAPS.

SHAPE (bimodal — confirmed):
  Functional UI: 3-8px radius (inputs, tags, small buttons)
  Display UI:    20-32px radius (cards, feature blocks)
  Pill CTAs:     60px or 50%
  RULE: Never apply display radius to functional elements or vice versa.

ELEVATION (confirmed):
  At rest:  rgba(0,0,0,0.08) 0px 4px 12px
  On hover: translateY(-3px) + rgba(0,0,0,0.12) 0px 10px 30px
  RULE: Shadow is earned on hover, not decorative at rest.

MOTION (confirmed cubic-bezier):
  Spatial:  0.45s cubic-bezier(0.4, 0, 0.2, 1)
  Color:    0.2s
  Multi:    0.3s ease-in-out
  Shimmer:  4s infinite
  Marquee:  40s linear infinite
  RULE: All ambient animations need prefers-reduced-motion override.

LAYOUT (confirmed containers):
  Nav outer: 1440px | Content: 1296px | Footer: 1100px
  Section padding: 128px 0 (large) / 80px 0 (compact) — ONLY 2 values
  Hero left column: max-width 550px
  Body text measure: max-width 65ch

TRUST SEQUENCE:
  1. Volume proof → 2. Authority proof → 3. Quality proof → 4. Risk reduction
  RULE: Trust must appear adjacent to every primary CTA.

CTA FORMULA (freemium):
  "[Verb] [specific action] for Free"
  Placement: hero + mid-page + end-of-page (3 minimum)

ACCESSIBILITY:
  Skip link, sequential headings, visible :focus-visible, labeled inputs,
  prefers-reduced-motion, aria on interactive elements.

ORIGINALITY:
  Use these PRINCIPLES. Do NOT use: exact #fe6724, Sample branding, exam names,
  specific stats, or any exact copy from the source site.
```

---

## Quick Reference

| Rule | Value |
|------|-------|
| Hero font-size | `clamp(28px, 4vw, 50px)` |
| Hero font-weight | `900` |
| Section H2 size | `42px, weight 900` |
| Body text | `18px, line-height 1.6` |
| Card hover transform | `translateY(-3px)` |
| Card hover shadow | `rgba(0,0,0,0.12) 0px 10px 30px` |
| Transition spatial | `0.45s cubic-bezier(0.4, 0, 0.2, 1)` |
| Transition color | `0.2s` |
| Feature card radius | `20px` |
| Course/display card radius | `32px` |
| Functional element radius | `4-8px` |
| Nav container width | `1440px` |
| Content container | `1296px` |
| Footer inner | `1100px` |
| Large section padding | `128px 0` |
| Footer bg | `#e9f1fc equivalent` |
| Feature card gradient | `135deg, #ff9a1f → #f97316` |
| Nav height | `82px` |
| Marquee duration | `40s linear` |

---

## The 5 Non-Negotiable Rules

1. **Fluid hero heading** — `clamp()` always. No exceptions.
2. **Physical hover on cards** — lift + shadow, not color-only
3. **Trust before CTA** — proof signal adjacent to every action
4. **Bimodal radius** — functional=small, display=large, never mixed
5. **Value before gate** — show 30%+ content before any signup prompt
