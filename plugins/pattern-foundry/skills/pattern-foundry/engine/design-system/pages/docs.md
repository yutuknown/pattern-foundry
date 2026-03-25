# Docs / Content Page — Page Override

> **Inherits from:** design-system/MASTER.md

## Page Goal
Deliver reference content efficiently. Support deep reading, quick navigation, and serendipitous discovery. Dark mode is critical here.

## Layout

```
┌──────────────────────────────────────────────────────┐
│ HEADER (sticky) — Logo | Search | Dark Mode Toggle    │
├──────────────────────────────────────────────────────┤
│ BREADCRUMB (4 levels: Category > Sub > Chapter > Page)│
├────────────────────┬─────────────────────────────────┤
│ LEFT SIDEBAR       │ MAIN CONTENT                     │
│ 280px, sticky      │ max-width 800px                  │
│ top: 72px          │                                  │
│                    │ H1: Page title (36-40px)          │
│ Table of Contents  │ Meta: Author · Date · Read time  │
│ - H2 links         │                                  │
│ - H3 links (indent)│ Body (18px, line-height 1.6)     │
│                    │ H2 sections (26-30px)            │
│ ──────────         │ H3 subsections (20-24px)         │
│ Join CTA (small)   │ Bullet lists, callouts           │
│ Related links      │ Embedded interactive blocks      │
│                    │ Download/Join CTAs (inline)      │
├────────────────────┴─────────────────────────────────┤
│ RELATED CONTENT GRID (3-col)                          │
├──────────────────────────────────────────────────────┤
│ FOOTER DEEP LINKS                                     │
└──────────────────────────────────────────────────────┘
```

## Typography Override (Content-specific)

**Body font must be font.content (Georgia/serif) OR Lato at 18px+ with 1.6 line-height**
```
content.h1:    36-40px, weight 700, font.brand
content.h2:    26-30px, weight 700, authority color
content.h3:    20-24px, weight 600
content.body:  18px, weight 400, font.content, line-height 1.6
content.meta:  14px, weight 400, text.muted
content.code:  15px, monospace, dark bg, border-radius.sm
content.caption: 13px, italic, text.muted
```

Paragraph max-width: 65ch (readability limit — NEVER full container width)
Paragraph margin-bottom: space.5 (20px)
Between H2 sections: space.12 (48px) minimum

## Component Override (Content-specific)

**Callout boxes** (required variant for docs):
```
Info:    border-left 4px action.primary, bg tinted action (5% opacity)
Warning: border-left 4px semantic.gold, bg tinted gold
Error:   border-left 4px semantic.error, bg tinted error
Tip:     border-left 4px semantic.success, bg tinted success
Padding: 16px 20px, margin: 24px 0, radius.sm on right corners
```

**Code blocks:**
```
Background: #1e1e2e (dark in both modes)
Font: monospace, 14-15px
Border-radius: radius.md (10-12px)
Copy button: top-right corner, small ghost button
```

**MCQ/Quiz blocks** (if content has interactive recall):
```
Question: bold, 16-18px, left-aligned
Options: radio or clickable cards, hover state
Reveal: "Show Answer" button, action color
Answer: expandable, green border-left
```

## Dark Mode Override

Dark mode is **REQUIRED** (not optional) for content pages.
Toggle: top-right in sticky header
Persist: localStorage
System preference: respect prefers-color-scheme

## Sidebar Override (Mobile)

On mobile: sidebar is NOT hidden with display:none (accessibility gap).
Mobile replacement:
- "Contents" button at top of content area (sticky, below breadcrumb)
- Expands to anchor link list (slide-down, 0.3s)
- OR: Bottom sheet that slides up from bottom of screen

## CTA Override

Content pages have soft CTAs only:
- "Join [Course] for Free" — inline, at natural stopping points (after major sections)
- "Download as PDF" — prominent but secondary
- "Start [topic] test" — engagement CTA after long sections
NO modal interruption mid-read. Gate only at explicit action.

## SEO Structure (Required for docs pages)

- Structured data: Article JSON-LD or BreadcrumbList JSON-LD
- Open Graph: title, description, image
- Canonical URL
- H1 matches title in URL
