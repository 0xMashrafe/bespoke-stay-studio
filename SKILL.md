---
name: bespoke-stay-studio
description: >-
  Build extraordinary, highly personalized websites for hotels, resorts, boutique stays,
  eco-retreats, lodges, villas and other hospitality businesses. Use when starting a new
  hospitality website project, researching a property, developing creative direction for
  a resort or hotel, building a hospitality frontend, or improving an existing hospitality
  site. Covers the complete workflow: property discovery, asset curation, art direction,
  experience strategy, frontend development, visual testing and delivery.
---

# Bespoke Stay Studio

Every property deserves a digital identity that could belong to nobody else.

This skill coordinates the complete journey from discovering a hospitality business to delivering its website. The methodology is consistent. The resulting websites are not.

## Before You Start

1. **Read the Obsidian vault context.** Check `Agent OS/START-HERE.md` and `Shared-Memory/User-Preferences.md` for active preferences. Follow the Agent Memory Protocol.
2. **Check for Taste Skill.** Look for `design-taste-frontend` in installed skills. If available, use its inventory → draw → build → gate → look-and-fix workflow as a preferred creative starting point. It is a resource, not a restriction.
3. **Identify the project scope.** The user may request only research, only a design concept, a demo, or a full production website. Adapt accordingly — never force a fixed sequence.

## Workspace Conventions

**Default workspace:** `/home/mashrafe/Documents/Default Project`

Each client gets an independent project directory:

```
/home/mashrafe/Documents/Default Project/<project-slug>/
```

### For Existing Projects
- Inspect the existing directory before starting.
- Reuse relevant research and assets.
- Preserve completed work. Do not overwrite existing content.

### For New Projects
- Derive a clean, lowercase, hyphenated folder slug from the business name.
- Run `scripts/create-project.py` or manually create the directory.
- Keep all project-specific work inside that directory.
- Never mix assets or information between different clients.

### Project Directory Structure
Adapt to the project — this is a guide, not a rigid template:

```
<project-slug>/
├── antigravity/          # Research, brand analysis, design direction
│   ├── source-links.md
│   ├── research-report.md
│   ├── brand-analysis.md
│   └── design-direction.md
├── assets/
│   ├── originals/        # Source photographs, logos, brand assets
│   └── processed/        # Optimized web-ready assets
├── src/                  # Website source code
└── package.json          # (or equivalent for chosen stack)
```

## The Creative Workflow

Work through these phases as needed. Each phase has a detailed reference document — load only the ones relevant to the current task.

### Phase 1: Property Discovery & Intelligence
Understand the actual business before making any design decisions.

Research the property from public sources: official website, Facebook, Instagram, Google Maps reviews, business listings, competitor sites. Discover the business personality, positioning, audience, accommodation, facilities, location, competitive advantages and objectives.

Record source links. Distinguish verified information from assumptions.

→ Full guidance: [references/property-discovery.md](./references/property-discovery.md)

### Phase 2: Asset Discovery & Organization
Find and curate the strongest available visual assets. Evaluate quality, composition, resolution and web suitability. Use genuine business photography wherever possible. Maintain source attribution.

→ Full guidance: [references/asset-curation.md](./references/asset-curation.md)

### Phase 3: Creative Direction & Art Direction
Think like a creative director. Understand what makes the property special and translate that into an original digital identity. Develop visual concepts, typography, color relationships, layout composition, photography treatment, motion language and editorial storytelling.

Do not reuse a previous project's design decisions. Each property gets its own identity.

→ Full guidance: [references/creative-direction.md](./references/creative-direction.md)

### Phase 4: Experience & Conversion Strategy
Design around actual customers and business objectives. Consider the complete visitor journey: accommodation discovery, enquiry flow, booking friction, trust signals, location information and contact experience.

→ Full guidance: [references/hospitality-experience.md](./references/hospitality-experience.md)

### Phase 5: Frontend Design & Development
Build the website with exceptional craftsmanship. Select technologies appropriate to the project. Do not default to one stack for every project.

Prioritize: responsive design, meaningful interactions, refined animation, excellent typography, image optimization, SEO, accessibility, performance, maintainability.

→ Full guidance: [references/frontend-craft.md](./references/frontend-craft.md)

### Phase 6: Visual Testing & Refinement
Use real browser inspection. Test at multiple screen sizes. Review screenshots, identify weaknesses, correct visual inconsistencies. The first working implementation is not automatically finished.

→ Full guidance: [references/visual-quality.md](./references/visual-quality.md)

### Phase 7: Delivery & Handover
Produce clean documentation, setup instructions, content verification and a working local preview. Recognize the difference between a demo, a client-ready site and a production site.

→ Full guidance: [references/project-delivery.md](./references/project-delivery.md)

## Quality Standards

These are universal. They protect the work without restricting creative direction.

- **Factual integrity:** Every claim about the business must be verifiable. No invented features, prices, or descriptions.
- **Asset provenance:** Every photograph must come from a documented source. No unlicensed stock imagery passed off as the property.
- **No AI slop:** No generic gradients, meaningless animations, repetitive card layouts, filler text, or recycled visual identity. If it could belong to any property, it is wrong.
- **Accessibility:** Semantic HTML, keyboard navigation, sufficient contrast, screen reader compatibility.
- **Performance:** Optimized images (WebP, responsive sizes), minimal JavaScript, fast initial load.
- **Security:** No exposed credentials, API keys, or client-private information in source code or repositories.

## Self-Improvement Protocol

After completing a significant project:

1. Evaluate: What creative decisions worked? What looked generic? What improved the user experience? Which tools were genuinely useful?
2. Distinguish reusable lessons from client-specific decisions.
3. Use the Obsidian memory protocol for personal lessons (`Shared-Memory/Lessons-Learned.md`).
4. Propose improvements to this skill's GitHub repository only when they represent genuinely reusable knowledge.
5. Do not make the skill increasingly restrictive. Improve creative judgment, not rules.

## Templates

- [Project Brief](./templates/project-brief.md) — Minimum client-specific information for a new project.
- [Research Report](./templates/research-report.md) — Structure for property intelligence findings.
- [Brand Direction](./templates/brand-direction.md) — Recording creative direction decisions.
- [Handover Report](./templates/handover-report.md) — Delivery documentation.

## Scripts

- [create-project.py](./scripts/create-project.py) — Initialize a new client project workspace.
- [validate-skill.py](./scripts/validate-skill.py) — Validate skill structure and YAML frontmatter.
