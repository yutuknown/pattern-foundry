# Anti-Copy Guardrails

## Purpose
Hard boundary document. Defines what must NOT be carried forward and what CAN be adapted. Enforces originality in every generation.

---

## DO NOT COPY (Hard Stops)

### Brand Identity
- ❌ Sample name, wordmark, logo
- ❌ "Education Revolution" tagline
- ❌ "Sample Infinity" subscription name
- ❌ Orange #fe6724 as-is (it's their brand color — adapt the role, not the value)
- ❌ Any mascots or proprietary character illustrations

### Third-Party Assets
- ❌ Y Combinator logo or badge
- ❌ Google Award badge imagery
- ❌ Specific award names or certification imagery
- ❌ Official App Store / Play Store badges (can use, must follow Apple/Google guidelines)

### Copyrighted Copy
- ❌ "Stop Wasted Effort Start Scoring More"
- ❌ "Flip. Recall. Repeat." (Sample's branded flashcard copy)
- ❌ "Exam-Focused Smart Notes" (branded feature name)
- ❌ "Test Insights" (branded feature name — use "Performance Analytics" or similar)
- ❌ Any other specific marketing copy from the site

### Brand-Specific Data
- ❌ "3.2 Crore+" student count
- ❌ "4.7 /5 Google Play" rating (their specific rating)
- ❌ "150k+ ratings" count
- ❌ "280 Crore+ MCQs" or any other Sample-specific metrics

### Domain-Specific Identity
- ❌ NEET, UPSC, JEE, CAT exam names (unless user is in Indian EdTech)
- ❌ Indian school curriculum structure (Class 1-12) unless explicitly requested
- ❌ NCERT-specific content structure

---

## ADAPT (Change Values, Keep Logic)

### Color
- ✅ DO use: warm action color + cool authority color + lightly tinted surface
- ✅ DO use: semantic color roles (error = red family, gold = achievement)
- ✅ DO use: the gradient strategy (warm gradient for feature cards)
- Adapt: Choose different hues that fit the new brand

### Typography
- ✅ DO use: `clamp()` for hero heading — fluid scaling is a technique, not a brand
- ✅ DO use: humanist sans for UI + serif for long-form reading
- ✅ DO use: weight 900 for section headings (bold is a system choice, not branded)
- Adapt: Choose different font families (Nunito, DM Sans, Plus Jakarta Sans, etc.)

### Spacing / Layout
- ✅ DO use: 128px section padding as the large value
- ✅ DO use: 1296px as standard content container
- ✅ DO use: the 4px base spacing unit and derived scale
- Adapt: These can be adjusted by brand density requirement

### Component Patterns
- ✅ DO use: bimodal radius strategy (functional vs display)
- ✅ DO use: `translateY(-3px)` hover lift — it's a physics principle
- ✅ DO use: flat-then-shadow elevation behavior
- ✅ DO use: skeleton shimmer loading pattern
- ✅ DO use: scrolling trust marquee pattern
- Adapt: Duration, exact shadow values, exact radius numbers can flex ±20%

### UX Patterns
- ✅ DO use: freemium CTA formula ("Start [action] for Free")
- ✅ DO use: trust signal stacking sequence (volume → authority → quality → risk)
- ✅ DO use: value-before-gate principle
- ✅ DO use: 3 CTA placements per long page (hero, mid, end)
- ✅ DO use: ToC sidebar + dark mode for content pages
- ✅ DO use: QR code + app badges for mobile-first products

---

## Transferability Test

Before any output, ask:
1. If the source brand saw this output, would they feel their brand was stolen? **→ NO (pass)**
2. Can the output serve a completely different industry with minor adjustments? **→ YES (pass)**
3. Does the output use exact source copy, exact source colors, or exact source logos? **→ NO (pass)**
4. Does the output still feel as high-quality as the source site? **→ YES (pass)**

If any test fails, revise before outputting.

---

## The Thin Line: Acceptable vs Unacceptable

| Element | Acceptable | Not Acceptable |
|---------|-----------|----------------|
| Orange action color | Any warm orange (coral, amber, rust) | Exact #fe6724 |
| Navy authority color | Any deep cool navy or slate | Exact #193f68 positioned identically |
| "Free" in CTA | Yes — "free" is a universal conversion word | "Start learning for Free" verbatim |
| Hover lift | translateY(-3px) is a standard CSS pattern | Claimed as unique to Sample |
| Trust badges | Your own stats, your own awards | Sample's specific awards |
| Card gradient | Any warm gradient (not necessarily orange) | exact `linear-gradient(135deg, #ff9a1f 0px, #f97316 100%)` |
| 128px section padding | Yes — derived from CSS, now a system default | Claimed as invented by this skill |
| Lato font | Use if you have a license / it fits | Required because "Sample uses it" |

---

## Confidence
**High** — guardrails derived from direct observation of what is brand-specific (logos, colors, exact copy, specific stats) vs what is universal (spacing systems, interaction patterns, conversion principles, accessibility rules).
