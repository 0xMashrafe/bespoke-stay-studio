#!/usr/bin/env python3
"""
Bespoke Stay Studio: Project Workspace Initializer
Creates an independent client project workspace inside the default projects directory.
"""

import sys
import os
import re
import argparse
from pathlib import Path

DEFAULT_WORKSPACE_ROOT = Path("/home/mashrafe/Documents/Default Project")

def slugify(name: str) -> str:
    """Converts a property name into a clean, filesystem-safe lowercase slug."""
    s = name.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

def init_project(name: str, base_dir: Path = DEFAULT_WORKSPACE_ROOT) -> Path:
    slug = slugify(name)
    if not slug:
        raise ValueError("Invalid property name resulting in empty slug.")

    project_dir = base_dir / slug
    if project_dir.exists():
        print(f"⚠️  Directory already exists: {project_dir}")
        print("    Preserving existing project files. Did not overwrite.")
        return project_dir

    print(f"🚀 Initializing new bespoke hospitality workspace for '{name}'...")
    print(f"📁 Destination: {project_dir}")

    # Standard workspace subdirectories
    subdirs = [
        "antigravity",
        "assets/originals",
        "assets/processed",
        "assets/logo",
        "brand",
        "planning",
        "references",
        "research",
        "src",
    ]

    for d in subdirs:
        (project_dir / d).mkdir(parents=True, exist_ok=True)

    # 1. Initialize README.md
    readme_content = f"""# {name}

Hospitality digital experience and bespoke website workspace.

- **Client / Property**: {name}
- **Workspace Slug**: `{slug}`
- **Created**: {os.popen('date -I').read().strip() if hasattr(os, 'popen') else '2026-11-07'}
- **Methodology**: Bespoke Stay Studio (`bespoke-stay-studio`)

## Directory Layout

- `antigravity/` — Central research, design direction, and agent coordination
- `assets/originals/` — Raw property photography, drone footage, logos
- `assets/processed/` — Web-optimized AVIF/WebP assets
- `brand/` — Color palette, typography, visual identity thesis
- `planning/` — Content inventory, section breakdown, opportunities
- `references/` — Source links, asset inventory, review archives
- `research/` — Business intelligence, customer insights, competitor audit
- `src/` — Website source code (Astro / Next.js / Vite)

## Next Steps

1. Fill out initial details in `antigravity/project-brief.md`
2. Gather initial links and photos into `references/source-links.md`
3. Execute Property Discovery and summarize in `research/business-overview.md`
"""
    (project_dir / "README.md").write_text(readme_content, encoding="utf-8")

    # 2. Initialize project-brief.md
    brief_content = f"""# Project Brief: {name}

- **Property Name**: {name}
- **Location**: [Village / Valley / City, Region]
- **Property Type**: [Eco-retreat / Boutique Stay / Heritage Villa / Resort]
- **Target Outcome**: [Level 1: Visual Demo / Level 2: Staging Site / Level 3: Production]

## Source Links
- Official Website: 
- Facebook: 
- Instagram: 
- Google Maps: 

## Project Notes
"""
    (project_dir / "antigravity" / "project-brief.md").write_text(brief_content, encoding="utf-8")

    # 3. Initialize source-links.md
    source_links_content = f"""# Source Links & References: {name}

## Primary Channels
- Google Maps Listing: 
- Facebook Page: 
- Instagram: 

## Photo & Media Collections
- Google Maps Review Photos:
- Facebook Photo Albums:
"""
    (project_dir / "references" / "source-links.md").write_text(source_links_content, encoding="utf-8")

    # 4. Create convenient symlink for antigravity workspace marker if useful
    try:
        (project_dir / "antigravity" / "_agy_workspace").touch()
    except Exception:
        pass

    print("✅ Project workspace successfully initialized.")
    print(f"\nNext Steps for Agent:\n  cd \"{project_dir}\"\n  Inspect 'antigravity/project-brief.md' and begin Property Discovery.")
    return project_dir

def main():
    parser = argparse.ArgumentParser(description="Initialize a new Bespoke Stay Studio project workspace.")
    parser.add_argument("name", help="Name of the hospitality property (e.g. 'Silent Peak Eco Retreat')")
    parser.add_argument("--dir", default=str(DEFAULT_WORKSPACE_ROOT), help="Base directory for project workspaces")
    args = parser.parse_args()

    try:
        init_project(args.name, Path(args.dir))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
