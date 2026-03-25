# transferable-uiux-pattern-engine

> A Claude Code skill for generating original, premium UI/UX from extracted design intelligence. **Not a clone. A quality system.**

## What This Is

A user-adaptive, brand-neutral UI/UX generation engine based on extracted design intelligence. Marketplace usage is prompt-first and runs from bundled local references by default. It extracts the *quality system* — spacing discipline, component grammar, conversion architecture, interaction model — and applies that system to generate **original work** for entirely different brands and industries.

**The difference:** This skill makes you understand design principles, then generate something new at the same quality level — not copy the source.

## Engine Core
- **Semantic Tokens:** Located in `design-system/tokens.json`, these provide the "source of truth" for all design variables.
- **Documentation:** A comprehensive set of guidelines covering colors, motion, typography, layout, and component specifications.

## Key Design Principles
1. **Modern Authority:** A balance of "High-Trust Navy" (#193f68) and "Vibrant Action Orange" (#fe6724).
2. **Tactile Friendliness:** Use of extreme 32px radii and massive 60px ambient shadows to make academic content feel "approachable."
3. **Triple Font Strategy:** Lato (UI), Inter (Data), and Georgia (Content) to balance speed and reading stamina.
4. **Spatial Momentum:** Use of 0.45s cubic-bezier transitions to create a "premium, deliberate" feel for interactive elements.

## Directory Structure
```text
transferable-uiux-pattern-engine/
├── design-system/
│   └── tokens.json       # All verified design tokens
├── docs/
│   ├── color-system.md   # Palette, surfaces, and gradients
│   ├── motion-system.md  # Transitions, easing, and keyframes
│   ├── typography-system.md # Font families, scale, and hierarchy
│   ├── layout-system.md  # Containers, padding, and breakpoints
│   └── component-specs.md # Button, card, and nav specifications
```

## How to Use This Skill
This engine is designed to be **transferable**. You can use the `tokens.json` file to bootstrap a new project with high-performance design primitives, then adapt them to your own brand identity in any modern web framework (Tailwind, Framer Motion, etc.).

### Example: Tailwind Integration
The `docs/` folder contains specific implementation notes for Tailwind CSS, allowing you to quickly map these verified styles to a modern utility-first workflow.

---
**Verified Data Source:** Playwright Live Inspection (2026-03-24)
**Engine Version:** 0.2.1
