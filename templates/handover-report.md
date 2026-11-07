# Project Handover Report: [Property Name]

**Date**: [YYYY-MM-DD]  
**Delivery Level**: [Level 1: Visual Demo / Level 2: Staging Site / Level 3: Production]  
**Lead Agent**: Bespoke Stay Studio  

---

## 1. Executive Summary

- **Client / Property**: [Property Name]
- **Deliverable Produced**: [e.g. Fully responsive bilingual Astro website with high-res responsive media]
- **Staging / Preview URL**: [URL or local preview instructions]
- **Codebase Location**: `/home/mashrafe/Documents/Default Project/[project-slug]`

---

## 2. Technical Stack & Architecture

- **Core Framework**: [e.g. Astro v5 / Next.js 16 / Vite]
- **Styling**: [e.g. Tailwind CSS + custom CSS custom properties]
- **Language**: TypeScript
- **Fonts**: Self-hosted local WOFF2 files in `/public/fonts/` (Zero external CDN calls)
- **Image Pipeline**: Automated WebP/AVIF generation with responsive srcset widths

---

## 3. Local Run & Build Instructions

```bash
cd "/home/mashrafe/Documents/Default Project/[project-slug]"

# Install dependencies
npm install

# Start local preview server
npm run dev

# Build production bundle
npm run build
```

---

## 4. Asset Provenance & Photography Audit

- **Total Assets Included**: [e.g. 32 photos, 1 ambient video loop]
- **First-Party Confirmed Assets**: [e.g. 18 photos]
- **Reference / Demo Assets (Require Client Action Before Production)**:
  - `hero-cloud-dawn.jpg`: Needs high-resolution replacement from owner.
  - `cottage-interior-bath.jpg`: Temporary placeholder from guest review upload.

---

## 5. Outstanding Client Actions & Next Milestones

1. **Review Room Pricing**: Confirm high-season rates in `src/data/rooms.json`.
2. **Phone & WhatsApp Numbers**: Verify direct contact digits in `src/components/Contact.astro`.
3. **Domain & DNS**: Provide Cloudflare / domain registrar access for production cutover.
