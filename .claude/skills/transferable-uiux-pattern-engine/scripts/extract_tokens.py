#!/usr/bin/env python3
"""
extract_tokens.py (legacy)
-------------------------
Phase 1 extraction: Derive design tokens from live CSS inspection via manual audit tooling.
LEGACY — not required for typical skill usage. Run only if you need to regenerate the reference intelligence yourself.

Usage:
  python3 extract_tokens.py --url https://example.com --output ./tokens_output

Output:
  - raw_css.txt          : All CSS rules concatenated
  - color_frequency.json : Colors sorted by usage frequency
  - typography.json      : Font families, sizes, weights
  - radii.json           : Border radius values
  - shadows.json         : Box shadow values
  - motion.json          : Transitions, animations, keyframes
  - layout.json          : Max-widths, containers, breakpoints
  - tokens.json          : Proposed semantic token mapping (fill in [FILL:] slots)
"""

import asyncio
import json
import re
import argparse
import os
from collections import Counter
from playwright.async_api import async_playwright


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))


def parse_rgb(rgb_str):
    m = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', rgb_str)
    if m:
        return rgb_to_hex(*m.groups())
    return None


async def extract_all_css(page):
    return await page.evaluate("""() => {
        let css = '';
        [...document.styleSheets].forEach(sheet => {
            try {
                [...sheet.cssRules].forEach(rule => { css += rule.cssText + '\\n'; });
            } catch(e) {}
        });
        return css;
    }""")


async def extract_computed_colors(page):
    return await page.evaluate("""() => {
        const freq = {};
        [...document.querySelectorAll('*')].slice(0, 800).forEach(el => {
            const s = window.getComputedStyle(el);
            ['backgroundColor', 'color', 'borderColor'].forEach(prop => {
                const v = s[prop];
                if (v && v.startsWith('rgb') && v !== 'rgba(0, 0, 0, 0)') {
                    freq[v] = (freq[v] || 0) + 1;
                }
            });
            const bg = s.backgroundImage;
            if (bg && bg.includes('gradient')) {
                const matches = [...bg.matchAll(/#([0-9a-fA-F]{3,6})/g)];
                matches.forEach(m => {
                    const hex = '#' + m[1].toLowerCase();
                    freq[hex] = (freq[hex] || 0) + 1;
                });
            }
        });
        return freq;
    }""")


def analyze_css(css_text):
    result = {}
    rgb_matches = re.findall(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', css_text)
    hex_freq = Counter()
    for r, g, b in rgb_matches:
        hex_freq[rgb_to_hex(r, g, b)] += 1
    result['hex_from_css'] = dict(hex_freq.most_common(50))
    result['font_sizes'] = sorted(set(
        s.strip() for s in re.findall(r'font-size:\s*([^;}{!]+?)(?:!important)?(?:;|})', css_text) if s.strip()
    ))
    result['font_families'] = list(set(
        f.strip() for f in re.findall(r'font-family:\s*([^;}{!]+?)(?:!important)?;', css_text) if f.strip()
    ))
    result['font_weights'] = sorted(set(
        w.strip() for w in re.findall(r'font-weight:\s*([^;}{!]+?)(?:!important)?(?:;|})', css_text) if w.strip()
    ))
    result['radii'] = sorted(set(
        r.strip() for r in re.findall(r'border-radius:\s*([^;}{!]+?)(?:!important)?(?:;|})', css_text) if r.strip()
    ))
    result['shadows'] = list(set(
        s.strip() for s in re.findall(r'box-shadow:\s*([^;}{!]+?)(?:!important)?(?:;|})', css_text)
        if s.strip() and s.strip() != 'none'
    ))
    result['transitions'] = list(set(
        t.strip() for t in re.findall(r'(?<!transform-)transition:\s*([^;}{!]+?)(?:!important)?(?:;|})', css_text) if t.strip()
    ))
    result['keyframes'] = list(set(re.findall(r'@keyframes\s+([\w-]+)', css_text)))
    result['gradients'] = list(set(re.findall(r'(?:linear|radial)-gradient\([^)]+\)', css_text)))
    result['max_widths'] = sorted(set(int(m) for m in re.findall(r'max-width:\s*(\d+)px', css_text)))
    result['paddings'] = sorted(set(
        p.strip() for p in re.findall(r'padding:\s*([^;}{!]+?)(?:!important)?(?:;|})', css_text) if p.strip()
    ))
    result['z_indexes'] = sorted(set(int(z) for z in re.findall(r'z-index:\s*(\d+)', css_text)))
    result['media_queries'] = sorted(set(
        m.strip() for m in re.findall(r'@media\s*([^{]+)\{', css_text)
    ))
    return result


def build_semantic_tokens(analysis, computed_colors):
    hex_colors = {}
    for rgb_str, count in sorted(computed_colors.items(), key=lambda x: -x[1]):
        if rgb_str.startswith('rgb('):
            h = parse_rgb(rgb_str)
            if h:
                hex_colors[h] = count
        elif rgb_str.startswith('#'):
            hex_colors[rgb_str.lower()] = count

    return {
        "_meta": {
            "note": "Semantic token proposal. Adapt roles to your brand.",
            "source": "manual audit tool live CSS extraction",
            "instructions": "Fill in [FILL:...] slots with your brand values"
        },
        "color": {
            "action": {
                "primary": "[FILL: warm/energetic CTA color]",
                "hover": "[FILL: slightly darker action]",
                "gradient_from": "[FILL: warm gradient start]",
                "gradient_to": "[FILL: warm gradient end]"
            },
            "authority": {
                "primary": "[FILL: cool/trustworthy color]",
                "deep": "[FILL: darker authority]",
                "darkest": "[FILL: near-black heading]"
            },
            "surface": {
                "default": "[FILL: 10% tint of authority]",
                "pale": "[FILL: lighter surface]",
                "hover": "[FILL: lightest hover]",
                "white": "#ffffff"
            },
            "text": {
                "primary": "#111111",
                "muted": "#86949d",
                "disabled": "#cacaca",
                "inverse": "#ffffff"
            },
            "border": {
                "default": "[FILL: tinted border]",
                "subtle": "[FILL: near-white border]"
            },
            "semantic": {
                "error": "#e94e4d",
                "gold": "#f0b400",
                "success": "#22c55e"
            }
        },
        "typography": {
            "font_family": {
                "brand": "[YOUR_FONT], sans-serif",
                "content": "Georgia, serif"
            },
            "font_size": {
                "hero": "clamp(28px, 4vw, 50px)",
                "display": "42px", "2xl": "32px", "xl": "24px",
                "lg": "20px", "base": "18px", "ui": "16px",
                "sm": "14px", "xs": "13px", "2xs": "12px"
            },
            "font_weight": {
                "regular": 400, "medium": 500, "semibold": 600,
                "bold": 700, "heavy": 900
            },
            "line_height": {
                "hero": "1.1", "heading": "1.2", "body": "1.5",
                "content": "1.6", "ui": "1.4"
            }
        },
        "spacing": {
            "1": "4px", "2": "8px", "3": "12px", "4": "16px",
            "5": "20px", "6": "24px", "8": "32px", "10": "40px",
            "12": "48px", "16": "64px", "20": "80px", "32": "128px",
            "_section_lg": "128px", "_section_sm": "80px"
        },
        "radius": {
            "xs": "3px", "sm": "5px", "md": "8px",
            "lg": "20px", "xl": "32px", "pill": "60px", "full": "9999px",
            "_rule": "xs-md for functional UI; lg-xl for display cards; pill for CTAs"
        },
        "shadows": {
            "none": "none",
            "subtle": "rgba(0,0,0,0.07) 0px 2px 16px",
            "card": "rgba(0,0,0,0.08) 0px 4px 12px",
            "card_hover": "rgba(0,0,0,0.12) 0px 10px 30px",
            "ambient": "rgba(229,229,229,0.25) 1px 1px 60px 40px"
        },
        "motion": {
            "duration": {
                "fast": "150ms", "base": "200ms", "medium": "300ms",
                "slow": "450ms", "shimmer": "4000ms", "marquee": "40000ms"
            },
            "easing": {
                "default": "cubic-bezier(0.4, 0, 0.2, 1)",
                "linear": "linear"
            },
            "hover_transform": "translateY(-3px)"
        },
        "layout": {
            "container_wide": "1440px", "container_standard": "1296px",
            "container_footer": "1100px", "hero_column": "550px",
            "content_max": "800px", "body_measure": "65ch"
        },
        "z_index": {
            "base": 0, "raised": 1, "nav": 10,
            "overlay": 1000, "modal": 1023, "tooltip": 2000
        },
        "breakpoints": {
            "sm": "640px", "md": "768px", "lg": "1024px",
            "xl": "1200px", "2xl": "1296px", "3xl": "1440px"
        },
        "_raw": {
            "top_colors": dict(list(hex_colors.items())[:20]),
            "font_sizes_found": analysis.get('font_sizes', [])[:15],
            "radii_found": analysis.get('radii', [])[:12],
            "shadows_found": analysis.get('shadows', [])[:8],
            "transitions_found": analysis.get('transitions', [])[:8],
            "keyframes_found": analysis.get('keyframes', []),
            "max_widths_found": analysis.get('max_widths', []),
        }
    }


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default='https://sample.in')
    parser.add_argument('--output', default='./tokens_output')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    print(f"Extracting from {args.url}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()
        await page.goto(args.url, wait_until='domcontentloaded', timeout=30000)
        await page.wait_for_timeout(4000)
        css = await extract_all_css(page)
        computed = await extract_computed_colors(page)
        await browser.close()

    analysis = analyze_css(css)

    with open(f'{args.output}/raw_css.txt', 'w') as f:
        f.write(css)

    for key, data in analysis.items():
        with open(f'{args.output}/{key}.json', 'w') as f:
            json.dump(data if isinstance(data, (list, dict)) else list(data), f, indent=2)

    tokens = build_semantic_tokens(analysis, computed)
    with open(f'{args.output}/tokens.json', 'w') as f:
        json.dump(tokens, f, indent=2)

    print(f'Done. Key output: {args.output}/tokens.json')
    print('Fill in [FILL:...] placeholders with your brand values.')


if __name__ == '__main__':
    asyncio.run(main())
