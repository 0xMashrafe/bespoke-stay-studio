# Reference: Asset Curation & Visual Provenance

## Purpose

Websites for hotels and stays live or die by imagery. Stock photography destroys credibility. This guide establishes our methodology for sourcing, auditing, categorizing, and optimizing authentic visual assets while preserving strict copyright and provenance standards.

---

## 1. The Primacy of Authentic Photography

> **Universal Rule:** Genuine property photography—even when imperfect—always beats polished, generic stock photography.

Guests want to know what they will see when they step through the door and walk out onto the terrace. Stock photos of anonymous luxury bedrooms or random palm trees signal deception and reduce booking trust.

### Sourcing Tiers (Priority Order):
1. **First-Party Client Assets**: Raw photos, camera originals, marketing archives provided directly by the property owner.
2. **High-Resolution Public Disclosures**: Uncompressed originals from official Facebook photo albums, Instagram feed masters, or verified press kits.
3. **Guest & Contributor Photographs (Reference/Demo Only)**: Google Maps photo uploads, public travel vlogs, YouTube drone sequences.
   - *Legal Constraint*: Third-party contributor photos may be used for internal concept demos, wireframes, and design proposals, but **must never be deployed to public production** without documented written permission or replacement by first-party shots.
4. **Curated Open Heritage & Archival Sources**: For regional landscapes, historical context, or architectural flora (via Wikimedia Commons, Openverse, Met Public Domain) with strict attribution.

---

## 2. Media Asset Categorization

Organize collected visual media into disciplined project subdirectories under `assets/`:

```
assets/
├── exteriors/           # Architecture, facades, approach pathways, outdoor lighting at dusk
├── cottages-or-rooms/   # Individual room types, bed arrangements, private balconies, en-suite baths
├── landscapes-views/    # Valley vistas, sea horizons, forest canopies, sunrise/sunset vantage points
├── interiors-details/   # Wall textures, bedding linen, wood joints, lamps, handcrafted fixtures
├── food-and-dining/     # Plated local meals, breakfast setups, dining pavilions, kitchen hearths
├── lifestyle-human/     # Guests reading on loungers, coffee on decks, quiet candid moments
├── identity-and-marks/  # Logos, carved wooden signage, stamps, letterheads, architectural blueprints
└── videos/              # Video loops, ambient background clips, aerial drone footage
```

---

## 3. Asset Audit & Inventory Ledger

Maintain an `asset-inventory.csv` or `references/asset-sources.md` tracking every asset:

| Column | Description |
| :--- | :--- |
| `asset_id` | Unique slug (e.g. `cottage-01-terrace-sunrise`). |
| `source_url` | Direct URL where original file was found. |
| `contributor` | Photographer name, handle, or "Official Property". |
| `license_status` | `First-Party Client`, `Creative Commons`, `Demo/Reference Only`, or `Public Domain`. |
| `original_res` | Pixel dimensions (e.g., `4032x3024`). |
| `web_suitability` | `Hero candidate`, `Gallery only`, `Texture/Background`, or `Discard (too blurry)`. |
| `subject_notes` | What is physically visible (e.g., "Bamboo Machang #3 overlooking East valley"). |

---

## 4. Digital Image Optimization Pipeline

Never serve multi-megabyte uncompressed camera files directly to end users.

### Specifications:
- **Formats**: Convert web deliverables to modern **AVIF** and **WebP** formats with responsive JPEG/PNG fallbacks.
- **Responsive Widths**: Generate stepped widths (`640w`, `960w`, `1280w`, `1920w`, and `2560w` for retina/ultrawide displays).
- **Compression Targets**:
  - Hero backgrounds: ≤ 250 KB (WebP/AVIF).
  - Editorial gallery images: ≤ 120 KB.
  - Detail thumbnails: ≤ 40 KB.
- **Ambient Video Optimization**:
  - Background video loops: H.264/MP4 or WebM, stripped of audio tracks, ≤ 4–6 MB total file size, muted, autoplaying, looping, with a paired static poster image for immediate paint.

---

## 5. Visual Provenance & Client Action Checklists

When preparing project delivery, compile an **Information Gaps & Asset Requirements** sheet (`information-gaps.md`):
- Explicitly list which temporary demo images need first-party replacements before public DNS cutover.
- Provide a clear shot list for the property owner/photographer (e.g., "Need 1 horizontal wide shot of Cottage 2 interior showing en-suite bathroom door, morning natural light").
