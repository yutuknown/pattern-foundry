<!--
  ANALYSIS DOC — Extracted Pattern Evidence
  ------------------------------------------
  This file names patterns by their observed source-site characteristics for
  precise reference. The patterns themselves are transferable; the naming
  is descriptive. Brand-specific names (e.g., "Sample") are used as
  shorthand for the inspected site — not as branding for your output.
  For use in generation, apply the abstracted rules in design-system/MASTER.md.
-->

# Transferable UI/UX Patterns: Education Revolution (Sample)

This section documents the high-level reusable patterns extracted from the Sample UI/UX audit. These patterns represent the "secret sauce" that makes the platform feel modern, authoritative, and friendly.

## 1. The "Approachable Authority" Pattern
- **Combination:** #193f68 (Deep Navy) + 32px Border Radius + 60px Ambient Shadow.
- **Why it works:** The navy provides professional academic trust, while the extreme roundness and soft shadow remove the "intimidating" nature of exams.
- **Usage:** Use for major course categories, featured content cards, and main product offerings.

## 2. The "SEO-First Visual Hierarchy"
- **Combination:** H1 (18px/700) + H2 (42px/900).
- **Why it works:** Allows for long, keyword-rich technical H1s for crawlers while using bold, punchy H2s for human visual engagement.
- **Usage:** Place the technical H1 above the hero title, styled as a "tag" or "overline," and use the H2 as the main visual headline.

## 3. The "Hybrid Reading" Typography
- **Combination:** Sans-serif UI (Lato/Inter) + Serif Content (Georgia).
- **Why it works:** Sans-serif ensures the interface feels like a modern app, while Serif ensures that when the student settles in to read a "Smart Note," their eyes encounter the familiar rhythm of traditional academic books.
- **Usage:** Switch to Georgia specifically for the `article` or `note-content` containers.

## 4. The "Physics-First" Interaction Model
- **Combination:** 0.45s Cubic-Bezier Spatial Movement + 0.2s Background Fast-Fade.
- **Why it works:** Spatial changes (scaling, moving) feel "physical" and high-end when they have a slow, accelerating curve. Color changes feel "responsive" when they happen nearly instantly.
- **Usage:** Apply the 0.45s curve to `:hover` transforms and the 0.2s ease to `:hover` background colors.

## 5. The "Layered Surface" Sectioning
- **Combination:** #ffffff → #e9f1fc → #eff4f7.
- **Why it works:** Instead of using hard lines or borders (which create visual noise), sectioning is achieved through subtle shifts in "coolness" and "brightness."
- **Usage:**
  - Section 1: White
  - Section 2: Pale Surface (#eff4f7)
  - Section 3: Light Blue Surface (#e9f1fc)
  - Footer: Deepest surface or Light Blue.

## 6. The "Action-Glow" Button Strategy
- **Combination:** #fe6724 Primary + #f0b400 Accent.
- **Why it works:** The primary orange is the "Engine" (Start Learning). The gold is the "Reward" (Achievements/Premium).
- **Usage:** Reserve the orange strictly for the primary path to conversion. Use gold for value-add features or gamification elements.
