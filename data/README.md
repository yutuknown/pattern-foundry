# data/

Raw extraction artifacts from the manual audit-based site inspection.
These files are the **source evidence** for the design tokens and patterns
in `.claude/skills/transferable-uiux-pattern-engine/design-system/`.

## Structure

```
data/
  raw/
    all_css.txt           ← Full CSS dump (87,614 chars) from homepage
    playwright_data.json  ← CSS tokens, fonts, classes from 4 pages
    deep_extract.json     ← Computed styles, CTA colors, card styles
    colors_deep.json      ← RGB color frequency from all DOM elements
  screenshots/
    homepage_desktop.png  ← 1440px viewport
    homepage_mobile.png   ← 390px viewport
    neet_hub.png          ← Exam hub page
    notes_page.png        ← Content/notes page
```

## How to regenerate

```bash
# Regenerate all_css.txt and playwright_data.json:
python3 .claude/skills/transferable-uiux-pattern-engine/scripts/extract_tokens.py \
  --url https://[reference-site] --output data/raw/

# Regenerate screenshots:
python3 .claude/skills/transferable-uiux-pattern-engine/scripts/inspect_site.py \
  --url https://[reference-site] --output data/
```

## gitignore status

Raw JSON files (large, re-generatable) are gitignored.
Screenshots are committed (small, useful visual evidence).
