#!/usr/bin/env python3
"""
inspect_site.py (legacy)
------------------------
Phase 0 recon script: crawl and inventory a target website.
LEGACY — uses manual audit with manual audit tool; not required for typical skill usage.
Only run if you explicitly need to refresh the reference intelligence yourself.

Usage:
  python3 inspect_site.py --url https://example.com --output ./output

Output:
  - page_inventory.json   : All discovered pages with metadata
  - nav_structure.json    : Navigation hierarchy
  - cta_inventory.json    : All CTA buttons and copy
  - heading_map.json      : All headings by page
  - component_candidates.json : CSS classes suggesting components
"""

import asyncio
import json
import argparse
import os
from urllib.parse import urlparse, urljoin
from playwright.async_api import async_playwright


async def inspect_page(page, url, label):
    """Extract all recon-level information from a single page."""
    try:
        await page.goto(url, wait_until='domcontentloaded', timeout=30000)
        await page.wait_for_timeout(3000)

        result = {
            'url': url,
            'label': label,
            'title': await page.title(),
        }

        # Meta description
        result['meta_desc'] = await page.evaluate(
            "() => document.querySelector('meta[name=description]')?.content || ''"
        )

        # Headings
        result['headings'] = await page.evaluate('''() =>
            [...document.querySelectorAll('h1,h2,h3,h4')]
            .map(h => ({ tag: h.tagName, text: h.innerText.trim().slice(0, 120) }))
            .filter(h => h.text)
            .slice(0, 40)
        ''')

        # Navigation links
        result['nav_links'] = await page.evaluate('''() => {
            const nav = document.querySelector('nav, [role="navigation"], [class*="nav"]');
            if (!nav) return [];
            return [...nav.querySelectorAll('a')]
                .map(a => ({ text: a.innerText.trim(), href: a.href }))
                .filter(x => x.text && x.text.length < 60)
                .slice(0, 20);
        }''')

        # CTA buttons
        result['cta_buttons'] = await page.evaluate('''() => {
            const selectors = [
                'button', 'a[class*="btn"]', 'a[class*="cta"]',
                '[class*="btn-er"]', '[class*="start-learning"]',
                'input[type="submit"]'
            ];
            const buttons = [];
            selectors.forEach(sel => {
                document.querySelectorAll(sel).forEach(el => {
                    const text = el.innerText?.trim() || el.value || '';
                    const s = window.getComputedStyle(el);
                    if (text && text.length < 80) {
                        buttons.push({
                            text,
                            bg: s.backgroundColor,
                            color: s.color,
                            class: el.className?.slice(0, 60) || '',
                        });
                    }
                });
            });
            return [...new Map(buttons.map(b => [b.text, b])).values()];
        }''')

        # Key CSS classes (component candidates)
        result['component_classes'] = await page.evaluate('''() => {
            const classes = new Set();
            document.querySelectorAll('[class]').forEach(el => {
                el.className.split(' ').forEach(c => {
                    if (c.length > 3 && c.length < 40 && /^[a-z]/.test(c)) {
                        classes.add(c);
                    }
                });
            });
            return [...classes].slice(0, 100);
        }''')

        # Trust signals
        result['trust_signals'] = await page.evaluate('''() => {
            const text = document.body.innerText;
            const signals = [];
            // Numbers with + or Cr
            const numMatches = text.matchAll(/([\d.,]+)\s*(Crore|Cr|M|K|million|billion)?\+?\s*(students|users|ratings|reviews|downloads|companies)/gi);
            for (const m of numMatches) signals.push(m[0].trim().slice(0, 80));
            // Ratings
            const ratingMatches = text.matchAll(/([\d.]+)\s*\/\s*5|★\s*([\d.]+)/g);
            for (const m of ratingMatches) signals.push(m[0].trim().slice(0, 40));
            return [...new Set(signals)].slice(0, 10);
        }''')

        # Above fold screenshot
        result['sections_visible'] = await page.evaluate('''() => {
            const vh = window.innerHeight;
            const sections = [];
            document.querySelectorAll('section, [class*="section"], [class*="hero"], [class*="banner"]').forEach(el => {
                const rect = el.getBoundingClientRect();
                if (rect.top < vh) {
                    sections.push({
                        tag: el.tagName,
                        class: el.className?.slice(0, 60) || '',
                        inAboveFold: rect.top >= 0 && rect.bottom <= vh,
                    });
                }
            });
            return sections.slice(0, 10);
        }''')

        print(f"  ✓ {label}: {len(result['headings'])} headings, {len(result['cta_buttons'])} CTAs")
        return result

    except Exception as e:
        print(f"  ✗ {label}: {e}")
        return {'url': url, 'label': label, 'error': str(e)}


async def discover_pages(page, base_url):
    """Discover internal pages from nav and footer links."""
    await page.goto(base_url, wait_until='domcontentloaded', timeout=30000)
    await page.wait_for_timeout(2000)

    links = await page.evaluate('''(base) => {
        const all = [...document.querySelectorAll('a[href]')];
        return all
            .map(a => a.href)
            .filter(h => h.startsWith(base) && !h.includes('#'))
            .filter((v, i, arr) => arr.indexOf(v) === i)
            .slice(0, 30);
    }''', base_url)

    return links


async def main():
    parser = argparse.ArgumentParser(description='Inspect a website for UI/UX recon')
    parser.add_argument('--url', default='https://sample.in', help='Target URL')
    parser.add_argument('--output', default='./inspection_output', help='Output directory')
    parser.add_argument('--pages', nargs='*', help='Additional pages to inspect')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    base = args.url.rstrip('/')

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()

        print(f"Discovering pages at {base}...")
        discovered = await discover_pages(page, base)
        print(f"  Found {len(discovered)} internal links")

        # Build inspection list
        pages_to_inspect = [(base, 'homepage')]
        if args.pages:
            for p_url in args.pages:
                label = urlparse(p_url).path.strip('/').replace('/', '_') or 'page'
                pages_to_inspect.append((p_url, label))

        # Inspect all pages
        all_results = []
        for url, label in pages_to_inspect:
            result = await inspect_page(page, url, label)
            all_results.append(result)

        await browser.close()

    # Save outputs
    with open(f'{args.output}/page_inventory.json', 'w') as f:
        json.dump(all_results, f, indent=2)

    # Extract nav structure
    nav = next((r['nav_links'] for r in all_results if r.get('nav_links')), [])
    with open(f'{args.output}/nav_structure.json', 'w') as f:
        json.dump(nav, f, indent=2)

    # Extract CTAs
    all_ctas = []
    for r in all_results:
        for cta in r.get('cta_buttons', []):
            cta['page'] = r['label']
            all_ctas.append(cta)
    with open(f'{args.output}/cta_inventory.json', 'w') as f:
        json.dump(all_ctas, f, indent=2)

    # Heading map
    heading_map = {r['label']: r.get('headings', []) for r in all_results}
    with open(f'{args.output}/heading_map.json', 'w') as f:
        json.dump(heading_map, f, indent=2)

    # Component candidates
    all_classes = set()
    for r in all_results:
        all_classes.update(r.get('component_classes', []))
    with open(f'{args.output}/component_candidates.json', 'w') as f:
        json.dump(sorted(all_classes), f, indent=2)

    print(f'\n✓ Inspection complete. Output in {args.output}/')
    print(f'  Files: page_inventory.json, nav_structure.json, cta_inventory.json')
    print(f'         heading_map.json, component_candidates.json')


if __name__ == '__main__':
    asyncio.run(main())
