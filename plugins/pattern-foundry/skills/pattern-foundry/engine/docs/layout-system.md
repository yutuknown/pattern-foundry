# Layout & Grid System

## Purpose
The Sample Layout System is designed for a desktop-first, highly responsive experience. It uses a series of nested containers with specific max-widths to maintain optimal reading lengths and visual balance across a wide array of device sizes.

## Key Findings
- **Container Strategy:**
  - **Navigation:** 1440px max-width (`.lp_ed_navbar`) with a 1296px inner wrapper (`.lp_nav_wrapper`).
  - **Footer:** 1100px max-width (`.ftr-new-inner`), creating a more intimate, content-dense feel than the main navigation.
  - **Hero Content:** The left side is constrained to 550px max-width to ensure headline readability and prevent text overflow on wide screens.
- **Section Rhythm:** A consistent vertical rhythm is maintained with 128px of top and bottom padding for major sections (`.er-crse-wrap`).
- **Responsive Granularity:** An unusually high density of 25+ specific breakpoints, allowing for precise design adjustments at every possible device width.

## Evidence (cite specific manual audit data)
- **Nav Width:** Max-width 1440px, Height 82px.
- **Nav Inner:** Width 1296px.
- **Footer Inner:** Max-width 1100px.
- **Hero Left:** Max-width 550px.
- **Section Padding:** 128px 0px.
- **Breakpoints (all confirmed):** 320px, 340px, 350px, 360px, 380px, 396px, 400px, 420px, 430px, 440px, 450px, 487px, 500px, 550px, 600px, 767px (min), 799px, 840px, 1005px, 1024px, 1036px, 1200px, 1240px, 1300px, 1440px.

## Inference
The 128px section padding is a "luxury" spacing choice, suggesting a brand that values white space and avoids a "cluttered" educational feel. The high number of breakpoints indicates a mature platform that has been meticulously tuned for the mobile-heavy Indian EdTech market.

## Transferability
- The "Nested Container" strategy (1440px for chrome, 1296px for content, 1100px for footer) is a highly transferable model for modern B2C landing pages.
- The 128px vertical rhythm is a great "rule of thumb" for high-end landing pages that need to feel "breathable."

## Non-Copy Boundary
- Do NOT exceed 1440px for main content containers to avoid excessive eye-scanning.
- Do NOT use the full 25+ breakpoints for a new project; stick to the core "turning points" (320, 767, 1024, 1440).

## Reusable Rule
**The Sample Container Hierarchy:**
- **Chrome (Nav):** 1440px
- **Main Content:** 1296px
- **Utility/Footer Content:** 1100px
- **Hero Content Constraint:** 550px

## Implementation Note

### Tailwind CSS Container Config
```javascript
theme: {
  container: {
    center: true,
    padding: '1rem',
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1296px', // Main content width
      '2xl': '1440px', // Nav max width
    },
  },
  extend: {
    spacing: {
      'section': '128px', // Standard vertical rhythm
    },
    maxWidth: {
      'hero': '550px',
      'footer': '1100px',
    }
  }
}
```

## Responsive Strategy Table

| Breakpoint | Role | Verified Data |
|------------|------|---------------|
| 320px | Mobile (Min) | Confirmed |
| 767px | Tablet Transition | Confirmed |
| 1024px | Desktop Transition | Confirmed |
| 1296px | Content Max-Width | Confirmed |
| 1440px | Shell Max-Width | Confirmed |

## Confidence
**High.** All widths and padding values were directly measured via CSS inspection. The breakpoint list is exhaustive and verified across the platform's stylesheets.
