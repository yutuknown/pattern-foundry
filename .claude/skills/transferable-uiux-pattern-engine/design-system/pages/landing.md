# Landing Page — Page Override

> **Inherits from:** design-system/MASTER.md

## Page Goal
Single conversion focus — one audience, one offer, one CTA. Minimal navigation distraction. Maximum value demonstration before the ask.

## Key Difference from Homepage
- **No global navigation** (or minimal: Logo + single CTA button only)
- **Single primary action** repeated 3+ times
- **Pre-segmented audience** (traffic is targeted — skip generic positioning)
- **Faster to the CTA** — less education needed
- **No footer navigation** (minimal footer: Logo + legal only)

## Blueprint (Section Order)

```
01. MINIMAL NAV
    Logo only + single CTA button (action color, right-aligned)
    Height: 60px, background white
    No navigation links (reduce exit opportunities)

02. HERO (center-aligned OR 2-col)
    Center-aligned variant (simpler, mobile-optimal):
    - Trust badge above headline
    - H1: single outcome promise (6-8 words, 50-64px)
    - Sub: one-line elaboration (18px, muted)
    - Primary CTA (large, action color, center)
    - Trust micro: rating + user count + "no credit card"
    - Hero visual: product screenshot below (auto-width, no device frame required)

    2-col variant (more visual context):
    - Same left content as above (60% width)
    - Right 40%: screenshot or illustration
    Background: white or very light surface (not dark navy — landing pages lighter)

03. PROBLEM → SOLUTION BRIDGE
    Background: white
    Show "Before" (pain) and "After" (benefit) contrast:
    Before: red/muted X icons + pain point text
    After:  green/action ✓ icons + benefit text
    Layout: 2-col side-by-side OR alternating rows

04. KEY FEATURE (1-2 only, not a full grid)
    Background: color.surface.default
    Alternating layout: text left + visual right, then visual left + text right
    Each feature: icon (40px) + heading (24-28px) + 40-word description + optional inline CTA

05. SOCIAL PROOF
    Background: white
    3 testimonial cards (2 tablet, 1 mobile)
    Each: quote + star rating + avatar + name + context (exam/role)

06. PRIMARY CTA BLOCK
    Background: dark authority (maximum contrast)
    Large headline + risk-reduction + big CTA button
    Risk: "No credit card · Cancel anytime · Works on all devices"

07. MINIMAL FOOTER
    Background: color.surface.pale (#eff4f7)
    Logo + Copyright + Privacy + Terms ONLY
    No navigation links (keep focus on conversion)
```

## CTA Override

**One and only one CTA label** used throughout the entire page:
```
"Start [Specific Action] for Free" — exact same copy at hero, mid-page, CTA block
```
Using different CTA copy in different sections = conversion confusion.

Secondary CTA only if needed: "Watch a demo" or "See how it works" (de-emphasized)

## Trust Override

Trust signals on landing pages:
- Hero: trust badge + micro proof (compact)
- Testimonials section: full user-voice trust
- CTA block: volume stats + guarantee
This is lighter trust density than homepage — users arrived pre-qualified from targeted traffic.

## Component Override

Modal: DO NOT use login modal on landing pages — send users to a dedicated signup page.
Nav: Minimal (logo + single CTA). Adding nav links kills conversion rate.
