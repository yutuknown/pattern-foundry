#!/usr/bin/env python3
"""
generate_page_override.py
-------------------------
Generate a page-specific override markdown file from a set of page rules.
Outputs a minimal page override that works with MASTER.md.

Usage:
  python3 generate_page_override.py --page homepage --output ./design-system/pages/
"""

import argparse
import os
from datetime import datetime

PAGE_BLUEPRINTS = {
    "homepage": {
        "goal": "Convert visitors to free account creation",
        "sections": [
            "NAVBAR (sticky, 82px, max-w-[1440px] outer / 1296px inner)",
            "HERO (dark gradient bg, 55/45 split, clamp hero type, trust badge above H1)",
            "TRUST (white bg, scrolling marquee + 4-stat row)",
            "CATEGORY BROWSER (surface bg, pill tag grid)",
            "FEATURE GRID (white bg, gradient cards, radius 20px, hover lift)",
            "MID-PAGE CTA (dark authority bg, centered headline + CTA + risk-reduction)",
            "APP DOWNLOAD (surface bg, QR + badges + phone mockups, 2-col)",
            "FOOTER (surface bg, max-w-[1100px], 4-col)"
        ],
        "cta_override": "Start [action] for Free — ALL CTAs include 'Free'",
        "trust_override": "Maximum trust density — hero badge + stats row + marquee",
        "density": "medium",
        "dark_mode": False,
        "component_emphasis": "Gradient cards (warm), pill CTAs (60px radius)"
    },
    "pricing": {
        "goal": "Convert free users to paid tier",
        "sections": [
            "NAVBAR (inherit MASTER)",
            "PRICING HEADER (white, centered, annual/monthly toggle)",
            "PRICING CARDS (surface bg, 3-col, Free/Pro/Enterprise)",
            "COMPARISON TABLE (white, sticky header, grouped features)",
            "FAQ ACCORDION (surface bg, 5-8 objection questions)",
            "FINAL CTA (dark authority bg, stats + headline + risk-reduction)"
        ],
        "cta_override": "Start [Plan] for Free (NOT 'Buy Now'). Enterprise: 'Talk to Sales'",
        "trust_override": "Trust ABOVE pricing cards (logo strip + rating compact)",
        "density": "medium-high",
        "dark_mode": False,
        "component_emphasis": "Pricing cards radius.xl (32px), highlighted tier with action-color top border"
    },
    "dashboard": {
        "goal": "Orient logged-in users, show progress, enable quick actions",
        "sections": [
            "TOP BAR (sticky, 64px, Logo + Search + Notifications + Avatar)",
            "SIDEBAR (240px, darker bg, sticky nav items)",
            "STATS ROW (4 cards, radius.lg, hover lift)",
            "MAIN CONTENT (8/4 grid split, primary + widgets)",
            "FOOTER (minimal or none)"
        ],
        "cta_override": "Action CTAs only ('Continue', 'Start', 'View all') — no conversion CTAs",
        "trust_override": "No trust signals — user is already converted",
        "density": "high",
        "dark_mode": True,
        "component_emphasis": "Stats cards (radius.lg, action primary color numbers), sidebar nav (active: action bg 15%)"
    },
    "docs": {
        "goal": "Deliver reference content, support deep reading",
        "sections": [
            "HEADER (sticky, Logo + Search + Dark Mode Toggle)",
            "BREADCRUMB (4-level trail, authority color links)",
            "CONTENT GRID (ToC sidebar 280px + main 800px)",
            "RELATED CONTENT (3-col card grid below content)",
            "FOOTER DEEP LINKS"
        ],
        "cta_override": "Soft CTAs only: 'Join for Free', 'Download as PDF', 'Start Test'",
        "trust_override": "No prominent trust signals — content IS the proof",
        "density": "high",
        "dark_mode": True,
        "component_emphasis": "ToC sidebar (sticky), callout boxes (4 types), code blocks (dark bg always)"
    },
    "landing": {
        "goal": "Single conversion focus — targeted traffic, one CTA",
        "sections": [
            "MINIMAL NAV (Logo + single CTA only — no navigation links)",
            "HERO (center-aligned OR 2-col, lighter bg than homepage)",
            "PROBLEM→SOLUTION BRIDGE (before/after contrast)",
            "KEY FEATURES (1-2 only, alternating layout)",
            "TESTIMONIALS (3 cards)",
            "PRIMARY CTA BLOCK (dark bg, large CTA, risk-reduction)",
            "MINIMAL FOOTER (Logo + legal only)"
        ],
        "cta_override": "IDENTICAL CTA copy throughout entire page. One label only.",
        "trust_override": "Lighter trust (pre-segmented traffic) — hero badge + testimonials",
        "density": "low-medium",
        "dark_mode": False,
        "component_emphasis": "Minimal nav (no links), center-aligned hero, no complex category browser"
    }
}


def generate_override(page_name, output_dir):
    blueprint = PAGE_BLUEPRINTS.get(page_name)
    if not blueprint:
        print(f"Unknown page type: {page_name}. Supported: {list(PAGE_BLUEPRINTS.keys())}")
        return None

    content = f"""# {page_name.title()} Page — Override

> **Generated:** {datetime.now().strftime('%Y-%m-%d')}
> **Inherits from:** design-system/MASTER.md
> **Override only what differs from MASTER defaults**

## Page Goal
{blueprint['goal']}

## Section Blueprint

"""
    for i, section in enumerate(blueprint['sections'], 1):
        content += f"```\n{i:02d}. {section}\n```\n\n"

    content += f"""## CTA Override

{blueprint['cta_override']}

## Trust Signal Override

{blueprint['trust_override']}

## Component Emphasis

{blueprint['component_emphasis']}

## Density
{blueprint['density']}

## Dark Mode
{'Required' if blueprint['dark_mode'] else 'Not required (optional for content-heavy variant)'}

---

*Overrides are minimal by design. All base rules from MASTER.md apply unless listed here.*
"""

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{page_name}.md")
    with open(out_path, 'w') as f:
        f.write(content)

    print(f"✓ Generated {out_path}")
    return out_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--page', choices=list(PAGE_BLUEPRINTS.keys()) + ['all'],
                        default='all', help='Page type to generate override for')
    parser.add_argument('--output', default='./design-system/pages/',
                        help='Output directory for page override files')
    args = parser.parse_args()

    if args.page == 'all':
        for page in PAGE_BLUEPRINTS:
            generate_override(page, args.output)
        print(f'\nAll {len(PAGE_BLUEPRINTS)} page overrides generated in {args.output}')
    else:
        generate_override(args.page, args.output)


if __name__ == '__main__':
    main()
