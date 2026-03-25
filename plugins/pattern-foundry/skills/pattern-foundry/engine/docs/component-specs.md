<!--
  ANALYSIS DOC — Component Evidence from Reference Site
  -------------------------------------------------------
  This file documents component measurements observed in the reference site
  via manual audit. Values are used as source-of-truth for the token system.
  Do not copy branded component names or branded copy into new implementations.
  Use samples/react/ for neutral component implementations.
-->

# Component Library & Specifications

## Purpose
The Sample Component Library is built for high-trust conversions. It balances friendly, rounded shapes (32px radius) with professional authority (navy buttons). Every element is designed to feel tactile, responsive, and trustworthy.

## Key Findings
- **High-Tactile Cards:** The "Sample signature" is the extreme 32px border radius on course cards, paired with a massive 60px ambient shadow.
- **Action Buttons:** A clear hierarchy exists between the "High-Trust Navy" (Authority) buttons and "Low-Friction Ghost" (Secondary) buttons.
- **Google Integration:** A dedicated button style for Google login that maintains the brand's rounded aesthetic while adhering to Google's branding.
- **Feature Cards:** Use a 20px radius and vibrant 135deg linear gradients to differentiate specific learning modes (Notes, Tests, etc.).

## Evidence (cite specific manual audit data)
- **Course Card (.crses):** Radius 32px, Shadow `rgba(229,229,229,0.25) 1px 1px 60px 40px`.
- **Feature Card:** Radius 20px, Gradient `linear-gradient(135deg, #ff9a1f 0px, #f97316 100%)`.
- **Action Button (Submit):** BG #193f68, White text, Radius 5px, Padding 6px 12px.
- **Ghost Button (Login):** BG #eff4f7, Color #86949d, Radius 5px, Padding 6px 12px.
- **Google Button:** BG white, Black text, Radius 8px/60px, Padding 6px 12px.
- **Nav Links:** Entrance Exams, School Exams, Sample App, Features, Login, Signup.

## Inference
The extreme roundness (32px) and massive soft shadow (60px) on course cards suggest a "friendly, non-intimidating" approach to complex academic material. This is a deliberate contrast to traditional, "boxed-in" educational tools.

## Transferability
- The 32px radius + massive ambient shadow is a highly transferable pattern for any brand that wants to feel "warm, friendly, and premium."
- The 135deg warm-to-hot gradient is a reusable pattern for high-energy feature callouts.

## Non-Copy Boundary
- Do NOT use the 32px radius for small UI elements (buttons, inputs) as it creates "pill" shapes that may clash with the more structural 5px radius buttons.
- Do NOT use the #193f68 navy for "Success" or "Warning" actions; it is reserved for "Authority" and "Standard" actions.

## Reusable Rule
**The Sample Radius-Shadow Scale:**
- **Primary Content (Course Cards):** 32px Radius + 60px Ambient Shadow.
- **Feature Modules:** 20px Radius + Gradient.
- **Interactive UI (Buttons):** 5px Radius (Standard) or 60px (Google/Pill).

## Component Spec Table

| Component | Selector | Key Styles | Intent |
|-----------|----------|------------|--------|
| Primary Button | `.btn-primary` | BG #193f68, Radius 5px | High-trust conversion |
| Ghost Button | `.btn-login` | BG #eff4f7, Color #86949d | Secondary action |
| Course Card | `.crses` | Radius 32px, Shadow (Ambient) | Premium content |
| Feature Card | `.feat-card` | Radius 20px, Gradient (135deg) | Mode callout |
| Nav Link | `.nav-link` | Lato, 16px, Weight 400 | Structural navigation |

## Confidence
**Very High.** All styles, selectors, and dimensions were extracted from live computed values. Selectors like `.lp_ed_navbar`, `.lp_nav_wrapper`, and `.crses` are verified.
