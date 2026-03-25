<div align="center">
  <img src="assets/readme/banner.svg" alt="Pattern Foundry Banner" width="100%" />

  <br />

  <h1>Pattern Foundry</h1>

  <p>
    <strong>A Claude Code skill for extracting transferable UI/UX design DNA from a reference site and reusing it for original brands and templates.</strong>
  </p>

  <p>
    <a href="https://github.com/yutuknown/pattern-foundry/stargazers"><img src="https://img.shields.io/github/stars/yutuknown/pattern-foundry?style=for-the-badge&color=eab308" alt="Stars" /></a>
    <a href="https://github.com/yutuknown/pattern-foundry/network/members"><img src="https://img.shields.io/github/forks/yutuknown/pattern-foundry?style=for-the-badge&color=3b82f6" alt="Forks" /></a>
    <a href="https://github.com/yutuknown/pattern-foundry/releases"><img src="https://img.shields.io/github/v/release/yutuknown/pattern-foundry?style=for-the-badge&color=22c55e" alt="Release" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/github/license/yutuknown/pattern-foundry?style=for-the-badge" alt="License" /></a>
  </p>
</div>

---

## Why this exists

Generative UI tools often produce generic "design mush" or clone reference sites too directly, leading to copyright and brand-safety issues. 

**Pattern Foundry solves this by separating brand identity from design quality.**

Instead of copying colors and logos, this skill extracts the *quality system*—spacing discipline, interaction physics, typography scaling, component grammar, and conversion architecture—and applies those structural rules to generate **original work** for entirely different brands, industries, and contexts.

## What it does

- **Extracts Visual DNA:** Reverses CSS rules into semantic design tokens.
- **Separates Identity from System:** Distinguishes between what is proprietary (logos, exact copy) and what is transferable (fluid typography, bimodal radii, trust signal sequencing).
- **Generates Reusable Systems:** Packages findings into a persisted `MASTER.md` design system.
- **Supports Original Generation:** Builds fresh, premium sites for new brands using the extracted intelligence.
- **Builds Reusable Templates:** Creates generic, blank-fill templates with premium structure built-in.

## Core features

<div align="center">
  <img src="assets/readme/architecture.svg" alt="Architecture Diagram" width="80%" />
</div>

- **Single-site deep inspection workflow:** Live CSS and DOM analysis via Playwright.
- **Design-system persistence:** Leverages `MASTER.md` for global rules and `pages/*.md` for precise, minimal overrides.
- **Brand adaptation rules:** Shifts temperature, density, and tone to fit new industries (B2B, Healthcare, Fintech, etc.).
- **Anti-copy guardrails:** Strictly enforces originality to prevent source-brand leakage.
- **Sample outputs:** React and Tailwind CSS scaffolding ready for production.
- **Helper scripts:** Python automation for extraction, design-system builds, and validations.

## Repo structure

```text
pattern-foundry/
├── .claude/skills/transferable-uiux-pattern-engine/
│   ├── design-system/   # MASTER.md and page-specific overrides
│   ├── docs/            # Deep analysis documents (UX, UI, Accessibility)
│   ├── samples/         # React components & generated page specs
│   ├── scripts/         # Python automation for token extraction
│   └── templates/       # Tailwind, PostCSS, and Framer Motion defaults
├── data/
│   ├── raw/             # Raw Playwright extraction JSONs (gitignored)
│   └── screenshots/     # Reference site visual captures
└── assets/              # README visuals
```

## Installation

### Prerequisites
- [Claude Code](https://docs.anthropic.com/claude/docs/claude-code) installed and authenticated.
- Python 3.9+ (if running extraction scripts).
- Playwright (if running extraction scripts: `pip install playwright && playwright install`).

### Local setup

```bash
git clone https://github.com/yutuknown/pattern-foundry.git
cd pattern-foundry

# (Optional) If you want to run extraction scripts:
pip install -r requirements.txt
playwright install chromium
```

### How to use the skill in Claude Code

Open your terminal in the repository root (or copy the `.claude/skills` folder to your project) and start Claude Code:

```bash
claude
```

## Quick start

You can invoke the skill inside Claude Code by explicitly naming it and selecting a mode.

**Example 1: Generate a new site for a different brand**
```text
Using pattern-foundry [NEW_BRAND_MODE]:
Brand: Synthflow — AI-powered customer interview platform
Industry: B2B SaaS
Audience: Product managers
Tone: Professional but approachable
Palette: Deep purple authority + warm coral action
Stack: Next.js + Tailwind CSS
Generate: Complete homepage spec + React component breakdown
```

**Example 2: Audit existing UI**
```text
Using pattern-foundry [AUDIT_MODE]:
[Paste your existing UI code here]
Score it on all 10 dimensions. List top 5 issues by impact. Provide upgraded spec.
```

## How it works

<div align="center">
  <img src="assets/readme/workflow.svg" alt="Workflow Diagram" width="100%" />
</div>

1. **Inspect:** Playwright scripts crawl the reference site, capturing computed styles, responsive behavior, and DOM hierarchy.
2. **Extract:** Raw CSS is parsed into token frequency maps, grouping values by their semantic roles.
3. **Abstract:** The system defines transferable rules (e.g., "Hover states must lift physically using `translateY(-3px)`" instead of "Use orange buttons").
4. **Generate:** Claude utilizes `SKILL.md` and the `MASTER.md` memory system to enforce the extracted rules on fresh prompts.

## Use cases

- **Build a new homepage:** Get a fully structured spec, React components, and a Tailwind config tailored to your brand.
- **Create a template:** Generate reusable, industry-agnostic scaffolding for agencies or themes.
- **Audit weak UI:** Score a generic Bootstrap or MUI page against a premium 10-dimension rubric and get refactor instructions.
- **Expand a design system:** Add a new feature (like a pricing page or dashboard) to an existing app without breaking visual consistency.

## Design system memory model

The skill relies on a strict persistence hierarchy to avoid context bloat:
1. **`MASTER.md`**: The global source of truth. Contains semantic tokens, universal spacing, and accessibility rules.
2. **`pages/*.md`**: Minimal overrides. Contains *only* what makes a specific page (e.g., `dashboard.md`) deviate from the global rules (like enforcing dark mode or altering CTA logic).

Claude is instructed to read `MASTER.md` first, then the specific page override, and never duplicate global rules into page files.

## Example prompts

### Dashboard Shell
```text
Using pattern-foundry [PAGE_GEN_MODE]:
Page: Dashboard shell
Product: Analytics platform for marketing teams
Tone: Professional, data-dense
Dark mode: yes
Stack: React + Tailwind
Generate: Full dashboard shell spec with sidebar, top bar, stats cards
```

### Brand Adaptation
```text
Using pattern-foundry [SYSTEM_EXPAND_MODE]:
I have a fitness app brand:
  Brand color: Vibrant coral #ef4444
  Industry: Fitness / Wellness

Using the extracted quality system, build the full token set:
- Adapt action color
- Derive authority color
- Derive surface color
- Output: complete tokens.json + tailwind.config.js
```

## Contributors

We welcome contributions! 

<a href="https://github.com/yutuknown/pattern-foundry/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yutuknown/pattern-foundry" />
</a>

*Looking to get involved? Read our [CONTRIBUTING.md](CONTRIBUTING.md).*

## Star History

<a href="https://star-history.com/#yutuknown/pattern-foundry&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=yutuknown/pattern-foundry&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=yutuknown/pattern-foundry&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=yutuknown/pattern-foundry&type=Date" />
  </picture>
</a>

## Roadmap

- [ ] Support for Vue/Nuxt and SvelteKit outputs in template mode.
- [ ] Automated accessibility auditing scripts inside the extraction pipeline.
- [ ] Multi-site fusion (extracting tokens from 3+ sites and finding the median premium rules).
- [ ] Export tokens directly to Figma Tokens Studio format.

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, development process, and pull request guidelines.

## License

[MIT License](LICENSE) - See the LICENSE file for details.

## Acknowledgements

- Built with [Claude Code](https://docs.anthropic.com/claude/docs/claude-code).
- Extraction layer powered by [Playwright](https://playwright.dev/).
