#!/usr/bin/env python3
"""
build_design_system.py
----------------------
Merge extracted docs into MASTER.md and validate tokens.json.

Usage:
  python3 build_design_system.py --tokens ./tokens_output/tokens.json \
    --docs ./docs/ --output ./design-system/

Output:
  - design-system/MASTER.md (regenerated or validated)
  - design-system/tokens.json (validated + merged)
  - build_report.json (validation issues list)
"""

import json
import argparse
import os
import re
from pathlib import Path


REQUIRED_TOKEN_KEYS = [
    'color.action.primary',
    'color.authority.primary',
    'color.surface.default',
    'color.text.primary',
    'typography.font_family.brand',
    'typography.font_size.hero',
    'spacing._section_lg',
    'radius.lg',
    'shadows.card',
    'shadows.card_hover',
    'motion.duration.slow',
    'motion.easing.default',
    'motion.hover_transform',
    'layout.container_standard',
]

FILL_PATTERN = re.compile(r'\[FILL:')


def get_nested(d, path):
    """Get a nested dict value by dot-separated path."""
    keys = path.split('.')
    for k in keys:
        if isinstance(d, dict) and k in d:
            d = d[k]
        else:
            return None
    return d


def validate_tokens(tokens):
    """Validate token completeness and flag [FILL:] placeholders."""
    issues = []

    for key in REQUIRED_TOKEN_KEYS:
        val = get_nested(tokens, key)
        if val is None:
            issues.append({'level': 'ERROR', 'key': key, 'msg': 'Required token missing'})
        elif isinstance(val, str) and FILL_PATTERN.search(val):
            issues.append({'level': 'WARNING', 'key': key, 'msg': f'Unfilled placeholder: {val}'})

    # Check for unfilled placeholders anywhere
    tokens_str = json.dumps(tokens)
    fill_count = len(re.findall(r'\[FILL:', tokens_str))
    if fill_count > 0:
        issues.append({
            'level': 'WARNING',
            'key': 'tokens',
            'msg': f'{fill_count} unfilled [FILL:] placeholders found — replace before using in production'
        })

    return issues


def validate_master_md(master_path):
    """Check that MASTER.md contains required sections."""
    required_sections = [
        'Design Philosophy',
        'Semantic Token System',
        'Typography',
        'Spacing System',
        'Container',
        'Radius System',
        'Shadow',
        'Motion System',
        'CTA',
        'Trust',
        'Accessibility',
        'Originality',
    ]

    issues = []
    if not os.path.exists(master_path):
        return [{'level': 'ERROR', 'key': 'MASTER.md', 'msg': 'File not found'}]

    with open(master_path) as f:
        content = f.read()

    for section in required_sections:
        if section.lower() not in content.lower():
            issues.append({
                'level': 'WARNING',
                'key': 'MASTER.md',
                'msg': f'Missing section: {section}'
            })

    return issues


def build_tailwind_config(tokens):
    """Generate a Tailwind config snippet from tokens."""
    action = get_nested(tokens, 'color.action.primary') or '[YOUR_ACTION_COLOR]'
    authority = get_nested(tokens, 'color.authority.primary') or '[YOUR_AUTHORITY_COLOR]'
    surface = get_nested(tokens, 'color.surface.default') or '[YOUR_SURFACE_COLOR]'

    return f"""// tailwind.config.js — generated from design-system/tokens.json
module.exports = {{
  darkMode: 'class',
  theme: {{
    extend: {{
      colors: {{
        'action':        '{action}',
        'action-hover':  '{get_nested(tokens, "color.action.hover") or "[YOUR_ACTION_HOVER]"}',
        'authority':     '{authority}',
        'surface':       '{surface}',
        'text-muted':    '{get_nested(tokens, "color.text.muted") or "#86949d"}',
        'border-default': '{get_nested(tokens, "color.border.default") or "[YOUR_BORDER]"}',
        'semantic-error': '#e94e4d',
        'semantic-gold':  '#f0b400',
        'dark-bg':        '{get_nested(tokens, "color.dark.bg") or "#191c27"}',
      }},
      fontFamily: {{
        brand:   ['{get_nested(tokens, "typography.font_family.brand") or "Inter"}', 'sans-serif'],
        content: ['Georgia', 'serif'],
      }},
      fontSize: {{
        hero: ['clamp(28px, 4vw, 50px)', {{ lineHeight: '1.1' }}],
        display: ['42px', {{ lineHeight: '1.2' }}],
      }},
      borderRadius: {{
        display:    '20px',
        'display-xl': '32px',
        pill:       '60px',
      }},
      boxShadow: {{
        card:       'rgba(0,0,0,0.08) 0px 4px 12px',
        'card-hover': 'rgba(0,0,0,0.12) 0px 10px 30px',
        ambient:    'rgba(229,229,229,0.25) 1px 1px 60px 40px',
      }},
      maxWidth: {{
        container: '1296px',
        wide:      '1440px',
        footer:    '1100px',
        hero:      '550px',
        content:   '800px',
      }},
    }},
  }},
}};
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tokens', default='./design-system/tokens.json')
    parser.add_argument('--master', default='./design-system/MASTER.md')
    parser.add_argument('--output', default='./design-system/')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    report = {'issues': [], 'status': 'ok'}

    # Validate tokens
    if os.path.exists(args.tokens):
        with open(args.tokens) as f:
            tokens = json.load(f)
        token_issues = validate_tokens(tokens)
        report['issues'].extend(token_issues)

        # Generate Tailwind config
        tailwind = build_tailwind_config(tokens)
        with open(os.path.join(args.output, 'tailwind.config.js'), 'w') as f:
            f.write(tailwind)
        print(f"✓ Generated tailwind.config.js")
    else:
        report['issues'].append({
            'level': 'ERROR', 'key': 'tokens.json',
            'msg': f'Not found at {args.tokens}'
        })

    # Validate MASTER.md
    master_issues = validate_master_md(args.master)
    report['issues'].extend(master_issues)

    # Determine overall status
    errors = [i for i in report['issues'] if i['level'] == 'ERROR']
    warnings = [i for i in report['issues'] if i['level'] == 'WARNING']

    if errors:
        report['status'] = 'error'
    elif warnings:
        report['status'] = 'warnings'

    # Save report
    report_path = os.path.join(args.output, 'build_report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    # Print summary
    print(f"\n=== Build Report ===")
    print(f"Status: {report['status'].upper()}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  ✗ [{e['key']}] {e['msg']}")
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ [{w['key']}] {w['msg']}")
    if not report['issues']:
        print("  ✓ All checks passed")

    print(f"\nReport saved to {report_path}")


if __name__ == '__main__':
    main()
