# Bespoke Stay Studio

**Every property deserves a digital identity that could belong to nobody else.**

Bespoke Stay Studio is a reusable creative and technical methodology for building extraordinary, highly personalized websites for hotels, resorts, boutique stays, eco-retreats, lodges, villas and other hospitality businesses.

This is not a template generator. It is a structured creative workflow that AI agents follow to discover a property's identity and translate it into an exceptional digital experience.

## What It Does

The skill coordinates the complete journey:

1. **Property Discovery** — Research the actual business from public sources before making design decisions.
2. **Asset Curation** — Find and organize the strongest available visual assets.
3. **Creative Direction** — Develop an original digital identity grounded in what makes the property special.
4. **Experience Strategy** — Design around real customers and business objectives.
5. **Frontend Development** — Build with exceptional craftsmanship, selecting technologies appropriate to the project.
6. **Visual Testing** — Inspect at multiple screen sizes, identify weaknesses, iterate.
7. **Delivery** — Produce clean documentation and a working local preview.

The methodology is consistent. The resulting websites are not.

## Philosophy

- Exceptionally personalized. Never generic.
- Premium, clean and visually sophisticated.
- Alive, immersive and thoughtfully interactive.
- Distinctive in composition and storytelling.
- Grounded in the actual identity of the business.
- Professionally engineered and genuinely useful.
- Absolutely no AI slop.

## Installation

### Using the Skills CLI

```bash
npx skills add 0xMashrafe/bespoke-stay-studio -g -y
```

### Manual Installation

Clone the repository into your global skills directory:

```bash
git clone https://github.com/0xMashrafe/bespoke-stay-studio.git ~/.agents/skills/bespoke-stay-studio
```

Then symlink to your agent's skill directory:

```bash
# Antigravity
ln -s ~/.agents/skills/bespoke-stay-studio ~/.gemini/config/skills/bespoke-stay-studio

# Codex
ln -s ~/.agents/skills/bespoke-stay-studio ~/.codex/skills/bespoke-stay-studio

# Claude Code
ln -s ~/.agents/skills/bespoke-stay-studio ~/.claude/skills/bespoke-stay-studio
```

### Verify Installation

```bash
python3 scripts/validate-skill.py
```

## Quick Start

Once installed, start a project by telling your agent:

> "Start a new website project for [Resort Name]. Here's their Facebook page and Google Maps listing. Research the business, prepare its project workspace and build a personalized website demo."

Or use the project initialization script:

```bash
python3 scripts/create-project.py "Resort Name"
```

The skill adapts to different scopes: research only, design concept, demo, or full production website.

## Project Workspace

Each client gets an independent directory inside your default project workspace:

```
/path/to/default-project/<project-slug>/
├── research/           # Business intelligence
├── references/         # Source links, asset inventory
├── brand/              # Creative direction, typography, color
├── assets/             # Photographs, videos, logos
├── planning/           # Content strategy, opportunities
└── src/                # Website source code
```

Client assets and information are never mixed between projects.

## Recommended Companion Skills

Bespoke Stay Studio works well with:

- **[design-taste-frontend](https://github.com/Leonxlnx/taste-skill)** — Anti-slop frontend art direction (preferred creative starting point).
- **frontend-design** — Distinctive visual design guidance.
- **frontend-ui-engineering** — Production-quality accessible UI.
- **webapp-testing** / **playwright** — Browser-based visual testing.
- **unslop** — Identifying and removing AI-generated visual patterns.

## Repository Structure

```
bespoke-stay-studio/
├── SKILL.md              # Main instruction file (concise, procedural)
├── README.md             # This file
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # Contribution guidelines
├── CHANGELOG.md          # Version history
├── references/           # Detailed guidance (progressive disclosure)
│   ├── property-discovery.md
│   ├── asset-curation.md
│   ├── creative-direction.md
│   ├── hospitality-experience.md
│   ├── frontend-craft.md
│   ├── visual-quality.md
│   └── project-delivery.md
├── templates/            # Reusable project templates
│   ├── project-brief.md
│   ├── research-report.md
│   ├── brand-direction.md
│   └── handover-report.md
├── scripts/              # Automation helpers
│   ├── create-project.py
│   └── validate-skill.py
└── evals/                # Creative quality evaluation
    └── creative-quality-scenarios.md
```

## Quality Standards

Universal standards that protect the work without restricting creative direction:

- **Factual integrity** — Every claim must be verifiable.
- **Asset provenance** — Every photograph must have a documented source.
- **Accessibility** — Semantic HTML, keyboard navigation, sufficient contrast.
- **Performance** — Optimized images, minimal JavaScript, fast initial load.
- **Security** — No exposed credentials or client-private information.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[MIT](LICENSE)

## Author

Built by [@0xMashrafe](https://github.com/0xMashrafe).
