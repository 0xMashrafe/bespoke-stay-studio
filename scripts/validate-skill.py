#!/usr/bin/env python3
"""
Bespoke Stay Studio: Skill Integrity & Schema Validator
Checks YAML frontmatter, markdown reference links, and ensures no private leaks exist.
"""

import sys
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent

def validate_skill():
    errors = []
    warnings = []
    print(f"🔍 Validating Bespoke Stay Studio skill at: {SKILL_ROOT}")

    skill_file = SKILL_ROOT / "SKILL.md"
    if not skill_file.exists():
        errors.append("Missing SKILL.md in root directory.")
        return False, errors, warnings

    content = skill_file.read_text(encoding="utf-8")

    # 1. Frontmatter Validation
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not frontmatter_match:
        errors.append("SKILL.md is missing YAML frontmatter enclosed in '---'.")
    else:
        fm = frontmatter_match.group(1)
        name_match = re.search(r"^name:\s*([a-zA-Z0-9_-]+)", fm, re.MULTILINE)
        if not name_match:
            errors.append("Frontmatter missing valid 'name' field.")
        else:
            skill_name = name_match.group(1)
            if skill_name != "bespoke-stay-studio":
                warnings.append(f"Frontmatter name '{skill_name}' does not match expected 'bespoke-stay-studio'.")

        desc_match = re.search(r"^description:\s*(.+)", fm, re.MULTILINE)
        if not desc_match:
            errors.append("Frontmatter missing 'description' field.")

    # 2. Relative Link Verification
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for link_text, link_target in links:
        if link_target.startswith("http://") or link_target.startswith("https://") or link_target.startswith("#"):
            continue
        # Clean relative target (remove leading ./ and anchor tags)
        cleaned_target = link_target.split("#")[0].lstrip("./")
        target_path = SKILL_ROOT / cleaned_target
        if not target_path.exists():
            errors.append(f"Broken relative link in SKILL.md: '{link_target}' (resolved to {target_path})")

    # 3. Privacy & Sanitization Check
    suspicious_patterns = [
        (r'ghp_[a-zA-Z0-9]{36}', "GitHub personal access token"),
        (r'sk-[a-zA-Z0-9]{32,}', "OpenAI secret key"),
        (r'/home/(?!mashrafe)[a-zA-Z0-9_]+/', "Unsanitized foreign home directory"),
    ]

    for py_or_md in SKILL_ROOT.rglob("*"):
        if py_or_md.is_file() and not py_or_md.name.startswith("."):
            try:
                f_text = py_or_md.read_text(encoding="utf-8", errors="ignore")
                for pat, desc in suspicious_patterns:
                    if re.search(pat, f_text):
                        errors.append(f"Potential secret or private pattern ({desc}) in {py_or_md.relative_to(SKILL_ROOT)}")
            except Exception:
                pass

    # 4. Mandatory Files Check
    mandatory_files = [
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "references/property-discovery.md",
        "references/asset-curation.md",
        "references/creative-direction.md",
        "references/hospitality-experience.md",
        "references/frontend-craft.md",
        "references/visual-quality.md",
        "references/project-delivery.md",
        "templates/project-brief.md",
        "templates/research-report.md",
        "templates/brand-direction.md",
        "templates/handover-report.md",
        "scripts/create-project.py",
        "evals/creative-quality-scenarios.md",
    ]

    for m in mandatory_files:
        if not (SKILL_ROOT / m).exists():
            errors.append(f"Missing mandatory file: {m}")

    return len(errors) == 0, errors, warnings

def main():
    success, errors, warnings = validate_skill()
    if warnings:
        print("\n⚠️  Warnings:")
        for w in warnings:
            print(f"  - {w}")

    if not success:
        print("\n❌ Validation Failed with errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\n✅ Skill validation PASSED! All files, schemas, and links are intact.")
    sys.exit(0)

if __name__ == "__main__":
    main()
