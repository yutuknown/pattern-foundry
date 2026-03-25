# Motion System

## Purpose
The Sample Motion System is designed to create a sense of responsiveness, depth, and momentum. It emphasizes "spatial feedback" for cards and "loading confidence" for data, ensuring that the interface feels alive and trustworthy during user interaction.

## Key Findings
- **Spatial/Card Transitions:** Uses a slow, intentional 0.45s `cubic-bezier(0.4, 0, 0.2, 1)` for movement and scaling.
- **Color Transitions:** Rapid 0.2s transitions for background-color changes (hover states).
- **Combined Hover Logic:** Cards often transition both `transform` and `box-shadow` simultaneously over 0.2s for tactile feedback.
- **Micro-interactions:** A generic 0.3s `ease-in-out` is used as a fallback for standard UI elements.
- **Visual Feedback:** Specialized shimmer keyframes (`shimmer_lrn`, `shimmer_lgou_floating`) for loading states and brand momentum.

## Evidence (cite specific manual audit data)
- **Cubic Bezier:** `0.45s cubic-bezier(0.4, 0, 0.2, 1)` — confirmed for spatial/card animations.
- **Background Fast:** `background 0.2s` — confirmed for quick color feedback.
- **Hover Shadow:** `transform 0.2s, box-shadow 0.2s` — confirmed for card interactions.
- **Multi-prop Transition:** `background 0.3s, transform 0.3s, width 0.3s, border-radius 0.3s` — confirmed for complex element shifts.
- **Keyframes:** `scroll-left`, `shimmer_lrn`, `shimmer_lgou_floating`.

## Inference
The 0.45s duration is relatively slow for modern UI but, when paired with the `cubic-bezier(0.4, 0, 0.2, 1)` easing, it creates a "premium/deliberate" feel rather than a "sluggish" one. This suggests a brand voice that values "considered" movement over "frantic" speed.

## Transferability
- The `cubic-bezier(0.4, 0, 0.2, 1)` curve is a classic "material-inspired" curve that is highly transferable for any platform emphasizing depth and physical layers.
- The use of 0.2s for color but 0.45s for spatial movement is a reusable principle: "Quick for color, graceful for physics."

## Non-Copy Boundary
- Avoid using durations longer than 0.45s for standard interactions, as this begins to feel sluggish.
- Ensure all `transform` transitions are GPU-accelerated to maintain 60fps, especially with the 0.45s slow curve.

## Reusable Rule
**The Sample 0.2s/0.45s Motion Rule:**
- **Action Feedback:** 0.2s (backgrounds, small shadows, text color).
- **Spatial Experience:** 0.45s (card expansion, page transitions, modal entry) with standard cubic-bezier.
- **Utility Motion:** 0.3s (tooltips, dropdowns) with ease-in-out.

## Implementation Note

### CSS Implementation
```css
/* Standard Card Hover */
.card-hover-effect {
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-hover-effect:hover {
  transform: translateY(-3px);
  box-shadow: 0px 10px 30px rgba(0,0,0,0.12);
}

/* Skeleton/Shimmer State */
@keyframes shimmer_lrn {
  0% { background-position: -468px 0; }
  100% { background-position: 468px 0; }
}

.shimmer-loading {
  animation: shimmer_lrn 1.2s linear infinite forwards;
  background: linear-gradient(to right, #eff4f7 8%, #e9f1fc 18%, #eff4f7 33%);
  background-size: 800px 104px;
}
```

### Framer Motion Implementation
```javascript
const cardTransition = {
  type: "tween",
  ease: [0.4, 0, 0.2, 1],
  duration: 0.45
};

<motion.div
  whileHover={{ y: -3, scale: 1.02 }}
  transition={cardTransition}
/>
```

## Easing Comparison
| Ease Type | Value | Use Case |
|-----------|-------|----------|
| Standard | `cubic-bezier(0.4, 0, 0.2, 1)` | Default spatial/movement |
| Rapid | `0.2s ease` | Immediate color/border feedback |
| Soft | `0.3s ease-in-out` | Subtle UI shifts/fades |

## Confidence
**Very High.** Transition values, durations, and keyframe names were extracted directly from the live computed CSS of the Sample landing page.
