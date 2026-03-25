# Typography System

## Purpose
The Sample Typography System is built to balance academic readability with modern accessibility. It uses a triple-font strategy to differentiate between structural UI, content-heavy learning material, and high-impact marketing headings.

## Key Findings
- **Triple Font Strategy:**
  - **Lato (Sans-serif):** Primary UI and body font for modern, clean readability.
  - **Inter (Sans-serif):** Secondary UI font, likely used for denser data or specific components.
  - **Georgia (Serif):** Reserved for "content" (likely the smart notes or long-form reading) to improve reading stamina.
- **Hierarchy:**
  - **Visual Hero (H2):** 42px with a weight of 900 (Black). This is the true visual anchor.
  - **SEO H1:** 18px with weight 700. A unique pattern where the technical H1 is small and SEO-focused, while the visual H2s carry the design weight.
- **Body & Scale:** A highly granular scale ranging from 11px to 42px, allowing for precise information density.

## Evidence (cite specific Playwright data)
- **Computed H2:** 42px, Weight 900 ("We cover all Exams and Classes").
- **Computed H1:** 18px, Weight 700 ("Sample stands for Education Revolution").
- **Font Families:** Lato, Inter, Georgia (all confirmed in CSS).
- **Scale:** 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 24px, 25px, 26px, 42px.
- **Weights:** Body 400, H1 700, H2 900.

## Inference
The 42px/900 H2 is the "Signature" of the Sample brand. It suggests a "bold, confident, and revolutionary" voice. The inclusion of Georgia (Serif) indicates a deep respect for traditional learning formats within a digital context.

## Transferability
- The "Small SEO H1 / Massive Visual H2" pattern is a clever way to balance SEO requirements with bold marketing design.
- The use of a Serif font for specific content modules within a Sans-serif UI is a transferable best practice for any educational or documentation platform.

## Non-Copy Boundary
- Do NOT use Georgia for UI elements (buttons, nav).
- Do NOT use weight 900 for anything other than major section headings (H2).

## Reusable Rule
**The Content-Reading Rule:**
- **UI/Navigation:** Lato/Inter (Sans-serif)
- **Deep Reading:** Georgia (Serif)
- **Hero Statements:** 42px / Weight 900

## Implementation Note

### Tailwind CSS Font Config
```javascript
theme: {
  fontFamily: {
    sans: ['Lato', 'Inter', 'sans-serif'],
    serif: ['Georgia', 'serif'],
  },
  fontSize: {
    'xs': '11px',
    'sm': '13px',
    'base': '16px',
    'lg': '18px',
    'xl': '20px',
    '2xl': '24px',
    'hero': '42px',
  },
  fontWeight: {
    normal: 400,
    bold: 700,
    black: 900,
  }
}
```

## Typography Scale Table

| Level | Size | Weight | Role | Source Data |
|-------|------|--------|------|-------------|
| H2 | 42px | 900 | Hero/Section Heading | Computed |
| H1 | 18px | 700 | SEO Anchor | Computed |
| Lead | 24px | 700 | Feature Subheadings | Scale |
| UI | 16px | 400 | Standard Body/UI | Scale |
| Small | 13px | 400 | Labels/Secondary | Scale |
| X-Small | 11px | 400 | Meta/Captions | Scale |

## Confidence
**High.** All sizes and weights were extracted from live computed values. The "H1 vs H2" role distinction is a direct observation from the DOM structure.
