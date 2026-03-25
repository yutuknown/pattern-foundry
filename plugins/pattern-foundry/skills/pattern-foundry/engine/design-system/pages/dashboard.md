# Dashboard — Page Override

> **Inherits from:** design-system/MASTER.md

## Page Goal
Primary workspace — orientation, progress tracking, quick access to key actions. Logged-in users only. Retention-focused, not acquisition-focused.

## Layout Architecture

```
┌─────────────────────────────────────────────────┐
│ TOP BAR (sticky, 64px)                          │
│ Logo | Search | Notifications | User avatar ↓   │
├──────────────┬──────────────────────────────────┤
│ SIDEBAR      │ MAIN CONTENT                      │
│ 240px fixed  │ (remaining width, scrollable)     │
│              │                                   │
│ Nav items    │ Stats row                         │
│              │                                   │
│ ─────────    │ Primary content grid 8/4          │
│ Settings     │                                   │
│ Help         │ Secondary widgets                 │
│              │                                   │
│ User info    │                                   │
└──────────────┴──────────────────────────────────┘
```

## Component Emphasis

**Stats cards:**
- radius.lg (20px) — large enough to feel "display" not "form"
- shadow.card at rest, shadow.hover on hover
- translateY(-3px) on hover (physical even in dashboard)
- Icon: 32px, colored (action.primary or semantic category color)
- Number: 36-40px, bold, action.primary color
- Delta: 13px, semantic.success green for positive, semantic.error red for negative

**Sidebar:**
- Background: slightly darker than main canvas (authority.deep family)
- Nav items: 48px height minimum (touch-safe)
- Active: action.primary background (low opacity ~15%) + action.primary text
- Hover: slightly lighter background shift (0.2s transition)
- Icons: 20px, consistent stroke weight

**Top bar:**
- Background: white (or dark surface in dark mode)
- Height: 64px (comfortable, not cramped)
- shadow.nav appears on scroll

## Responsive Override

Mobile: sidebar collapses to bottom nav bar (not hamburger menu):
```
Bottom nav: 5 icon items max + user avatar
Each item: icon + label (13px), 44px min height
Active: action.primary icon + label color
```

Stats row: 2×2 grid on mobile

**Dark mode is REQUIRED for dashboards** — developers and power users demand it.
Toggle in top bar right side OR user preferences.

## CTA Override

No conversion CTAs on dashboard — user is already signed in.
Only action CTAs: "Continue", "Start", "View all", "Add new"
Upgrade prompt (if freemium): subtle inline banner, not modal interruption.

## Content Rhythm Override

Dashboard headings: 20-24px (smaller than marketing pages — space is precious)
Labels: 12-13px, all UPPERCASE with letter-spacing (dashboard convention)
Numbers: large and prominent — data is the primary content
Empty states: always include a clear next action CTA
