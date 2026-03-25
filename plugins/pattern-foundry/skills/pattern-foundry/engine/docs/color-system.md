# Color System

## Purpose
The Sample Color System is designed to project a balance between professional academic authority and vibrant, engaging learning experiences. It leverages a high-contrast primary orange against a deep navy foundation to create trust while maintaining energy.

## Key Findings
- **Primary Brand:** Orange (#fe6724) is the engine for conversion, used for all primary CTAs.
- **Authority Foundation:** Deep Navy (#193f68) provides the structural trust and professional grounding.
- **Surface Layering:** A sophisticated range of light blues and pale grays (#e9f1fc, #eff4f7, #f6fcff) is used to differentiate content sections without harsh borders.
- **Tertiary/Achievement:** Gold (#f0b400) is used for rewards, achievements, and "premium" features.

## Evidence (cite specific Playwright data)
- **Primary Brand Orange (#fe6724):** Found in 5 key CTA/highlight instances.
- **Authority Navy (#193f68):** Used in 3 core navigation and heading elements.
- **Footer Surface (#e9f1fc):** Confirmed as the background color for `.ftr-new-inner`.
- **Feature Card Gradients:** Linear gradients starting from #ff9a1f (warm start) to #f97316 (warm end).
- **Google Blue (#1a73e8):** Used 7 times, but exclusively for the Google OAuth login button, not as a brand element.

## Inference
The system uses "vibrancy for action" and "sobriety for content." The use of multiple light-blue surfaces suggests a focus on reducing visual fatigue while maintaining a cohesive brand identity that feels "lighter" than traditional academic platforms.

## Transferability
- The orange-navy contrast is highly transferable to any EdTech or professional service platform seeking a "modern authority" look.
- The use of very light blue surfaces instead of pure white/gray for sectioning is a reusable pattern for content-heavy sites.

## Non-Copy Boundary
- Do NOT use #1a73e8 as a brand color; it is reserved for third-party integrations (Google).
- Do NOT use #fe6724 for body text or large background areas; it is reserved for high-impact actions.

## Reusable Rule
**The 70-20-10 Rule for EdTech:**
- 70% Neutral Surfaces (#ffffff, #e9f1fc, #eff4f7)
- 20% Authority Colors (#193f68, #111111)
- 10% Action/Vibrancy (#fe6724, #f0b400)

## Implementation Note

### Tailwind CSS Configuration
```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          orange: '#fe6724',
          navy: '#193f68',
          gold: '#f0b400',
        },
        surface: {
          light: '#ffffff',
          alt: '#e9f1fc',
          pale: '#eff4f7',
          hover: '#f6fcff',
        },
        text: {
          primary: '#111111',
          secondary: '#4b5661',
          muted: '#86949d',
          dark: '#010b24',
        }
      },
      backgroundImage: {
        'feature-gradient': 'linear-gradient(135deg, #ff9a1f 0%, #f97316 100%)',
      }
    }
  }
}
```

## Color Palette Table

| Color | Hex | RGB | Role | Frequency | Semantic Token | Transferable As |
|-------|-----|-----|------|-----------|----------------|-----------------|
| White | #ffffff | (255,255,255) | Surface Primary | 27 | `surface.primary` | Base background |
| Black | #000000 | (0,0,0) | Text/Dark | 13 | `text.black` | Primary text |
| Orange | #fe6724 | (254,103,36) | Primary Brand | 5 | `color.brand.primary` | Primary CTA |
| Navy | #193f68 | (25,63,104) | Authority | 3 | `color.brand.secondary` | Headers/Trust |
| Gold | #f0b400 | (240,180,0) | Achievement | 5 | `color.brand.accent` | Highlights/Gold |
| L-Blue | #e9f1fc | (233,241,252) | Surface Alt | 4 | `surface.secondary` | Footer/Section |
| Pale | #eff4f7 | (239,244,247) | Surface Pale | 4 | `surface.tertiary` | Alt sections |
| Muted | #86949d | (134,148,157) | Muted Text | 6 | `text.muted` | Captions/Secondary |

## Confidence
**High.** All hex codes, roles, and frequencies were derived from live Playwright inspection data.
