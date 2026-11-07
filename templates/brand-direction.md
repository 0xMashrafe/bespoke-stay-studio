# Brand Direction & Visual Identity: [Property Name]

## 1. Creative Thesis & Atmospheric Anchor

- **The Core Thesis**:
  > *"[One vivid sentence defining the soul of the digital experience—e.g. 'A dark, quiet film of a small bamboo house sitting inside a cloud...']"*
- **The Visual Anchor**: [e.g. The dark timber window frame looking out into glowing morning mist]
- **Atmospheric Keywords**: [e.g. Weathered, Elevated, Quiet, Luminous, Handcrafted]

---

## 2. Color System Derived from Physical Reality

*Sampled directly from authentic site photography, local stone, wood, and geography:*

| Token Name | Hex Code | Role & Physical Reference |
| :--- | :--- | :--- |
| `--stay-canvas` | `#E8EDF1` | Background canvas; morning cloud and valley mist |
| `--stay-ground` | `#1E2318` | Dark typography & framing; monsoon forest pine |
| `--stay-timber` | `#B3904C` | Warm architectural accent; sunlit bamboo stalks |
| `--stay-stone` | `#5B625E` | Structural lines & secondary text; river rock |
| `--stay-accent` | `#4EB3C5` | Signature accent; painted cottage shutters |

---

## 3. Typography Architecture

### A. Display / Title Typeface
- **Family**: [e.g. *Fraunces* or *Cormorant Garamond*]
- **Role**: Headlines, section titles, property wordmark.
- **Stylistic Qualities**: [e.g. High-contrast optical sizes, editorial warmth, soft serifs]

### B. Body & Reading Typeface
- **Family**: [e.g. *Instrument Sans* or *Inter*]
- **Role**: Narrative paragraphs, room specs, logistics, UI labels.
- **Stylistic Qualities**: [e.g. Clean geometric clarity, tall x-height, neutral readability]

### C. Vernacular / Script Pairing (if applicable)
- **Primary Script**: [e.g. Bengali]
- **Typeface**: [e.g. *Noto Serif Bengali* for headings + *Hind Siliguri* for body copy]
- **Line-Height Adjustment**: `+15%` to prevent diacritic collision.

---

## 4. Composition & Spatial Rhythm

- **Grid System**: [e.g. Asymmetric 12-column editorial grid with full-bleed breaks]
- **Vertical Silence**: Section padding set to `clamp(5rem, 10vw, 10rem)` to avoid crowded SaaS feels.
- **Corner Radii**: Strictly disciplined (`0px` to `4px` maximum; no bubbly rounded cards).
- **Surface Elevation**: Rely on spatial layering and subtle tonal shifts; no heavy black drop-shadows.

---

## 5. Motion & Interaction Language

- **Pacing**: [e.g. Slow, weather-like ambient drift on hero visuals (25s scale transition)]
- **Transitions**: Smooth, low-friction opacity fades (`350ms cubic-bezier(0.16, 1, 0.3, 1)`).
- **Reduced Motion**: Instant static fallbacks for accessibility.
