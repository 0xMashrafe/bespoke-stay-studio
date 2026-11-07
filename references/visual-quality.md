# Reference: Visual Quality & Testing Methodology

## Purpose

A working website is not automatically a finished design. Code that compiles without errors may still suffer from awkward line wraps, misaligned margins, low contrast in direct sunlight, or cramped mobile viewports. This reference establishes our visual testing, browser inspection, and iterative refinement loop.

---

## 1. The Multi-Viewport Inspection Matrix

Always verify pages across three non-negotiable device viewports:

| Device Class | Target Width | Inspection Priorities |
| :--- | :--- | :--- |
| **Mobile Smartphone** | **390px** (iPhone / Pixel) | Sticky booking bar visibility, thumb reachability, zero horizontal overflow (`overflow-x: hidden`), font legibility, touch targets ≥ 44x44px, hamburger drawer smoothness. |
| **Tablet / Foldable** | **768px** / **820px** (iPad / Tablet) | Multi-column grid handoffs, image aspect-ratio integrity, modal width constraints, landscape orientation balance. |
| **Desktop / Laptop** | **1440px** (MacBook / HiDPI) | Cinematic spatial pacing, full-bleed hero sharpness, balanced vertical white space, maximum line lengths on editorial prose (≤ 80ch). |

---

## 2. Automated Visual Audit Loop

Use real browser automation (`playwright` or `webapp-testing`) to capture and inspect full-page screenshots before declaring a task complete.

### Step-by-Step Testing Procedure:
1. **Start the Local Development Server**:
   ```bash
   npm run dev # or npm run preview
   ```
2. **Execute Headless Viewport Capture**:
   Capture full-page and section-specific screenshots at 390px, 768px, and 1440px.
3. **Inspect the Visual Output**:
   - Check typography rendering and line breaks.
   - Verify image clarity and responsive scaling.
   - Inspect z-index layering (ensure headers and modals do not clip behind content).
   - Check spacing harmony: Are paddings between sections consistent and generous?

---

## 3. The Visual Quality Rubric

Grade the rendered site against these four studio criteria:

### A. Atmosphere & Distinction (25%)
- Does the site transport the visitor into the physical mood of the property within 3 seconds?
- Is the identity unmistakable, or does it look like a generic SaaS template?

### B. Usability & Ergonomics (25%)
- Can a visitor find prices, room options, and contact methods in less than 15 seconds?
- Does the mobile experience feel effortless and natural under one thumb?

### C. Craft & Precision (25%)
- Are margins, paddings, and alignment mathematically disciplined?
- Is contrast crisp and legible?
- Are there any layout glitches, overlapping text, or stuttering animations?

### D. Storytelling & Content Truth (25%)
- Are descriptions specific, evocative, and factually grounded?
- Do the photos accurately represent real rooms rather than vague lifestyle stock?

---

## 4. The 3-Round Iteration Cycle

Never stop at the initial code generation pass. Follow the iterative refinement cycle:

- **Pass 1: Functional Build**: Wire up all sections, components, images, and data.
- **Pass 2: Visual Critique & Polish**: Take full-page screenshots, zoom into awkward corners, tighten loose typographic hierarchies, and prune unnecessary decorative elements ("remove one accessory").
- **Pass 3: Real Device & Performance Verification**: Test scroll smoothness, verify keyboard accessibility, validate zero console errors, and confirm sub-second time-to-first-contentful-paint.
