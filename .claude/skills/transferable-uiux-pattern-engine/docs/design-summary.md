<!--
  ANALYSIS DOC — Reference Site Evidence
  ----------------------------------------
  This file documents patterns observed in the inspected reference site.
  It is intentionally named after the source site's patterns for accuracy.
  DO NOT use this as a generation template — use docs/extracted-style-dna.md,
  docs/visual-dna.md, and design-system/MASTER.md for generation instead.
-->

# Sample Design Patterns Summary

This document captures the essence of the Sample UI/UX, combining high-level strategy with granular tactical implementation based on curated manual audit notes.

## 1. Design Ethos
- **Tone:** Academic yet approachable.
- **Voice:** "Sample stands for Education Revolution."
- **Focus:** User trust, content clarity, and engagement.

## 2. Core Color Palette
| Category | Primary | Secondary | Backgrounds/Surfaces |
|----------|---------|-----------|----------------------|
| **Brand** | #fe6724 (Orange) | #193f68 (Navy) | #ffffff, #e9f1fc, #eff4f7 |
| **Accent** | #f0b400 (Gold) | - | - |
| **Functional** | #1a73e8 (Google Blue) | #86949d (Muted) | - |

## 3. Typography Hierarchy
- **Primary Font:** Lato (UI/Body)
- **Secondary Font:** Inter (Functional)
- **Content Font:** Georgia (Serif for reading)
- **Visual Anchor:** H2 @ 42px / Weight 900
- **SEO Anchor:** H1 @ 18px / Weight 700

## 4. Interaction Principles
- **Spatial Feedback:** 0.45s Cubic-Bezier transforms for depth and movement.
- **Color Feedback:** 0.2s fast transitions for immediate state changes.
- **Micro-interactions:** Subtle translateY(-3px) and box-shadow elevation on hover.

## 5. Layout & Containers
- **Max Container:** 1440px (Nav) / 1296px (Main) / 1100px (Footer).
- **Hero Constraint:** 550px max-width for primary text blocks.
- **Vertical Rhythm:** 128px section padding (top/bottom).
- **Responsive Granularity:** 25+ specific breakpoints for pixel-perfect adjustments.

## 6. Key UI Patterns
- **High-Trust Cards:** 32px radius + 60px ambient shadow.
- **Authority CTAs:** Navy background, white text, 5px radius.
- **Vibrant Highlights:** 135° - 155° linear gradients (Orange-Yellow).
- **Content Hierarchy:** "Small Tag H1" above "Massive Bold H2."

## 7. Verified Values Reference
- **Nav Height:** 82px.
- **Section Padding:** 128px.
- **Radii Range:** 3px to 60px (32px signature).
- **Shadows:** 6 specific levels (ambient, subtle, strong).
- **Motion:** 5 specific transition types + 3 keyframes.
