# Reference: Project Delivery & Handover

## Purpose

A successful project finishes with clean documentation, clear boundaries, and zero ambiguity regarding what was built, what was verified, and what the client or human developer must do next. This guide defines our project handoff methodology.

---

## 1. Defining Delivery Levels

Always establish and communicate the exact scope of the deliverable:

### Level 1: Visual & Conceptual Demo
- **Purpose**: Rapid stakeholder pitch, creative direction validation, mood board, or preliminary layout proposal.
- **Includes**: Static UI prototype, representative layout, placeholder or curated third-party imagery, preliminary copy.
- **Explicit Limitation**: Third-party images are strictly for evaluation and must not be published live.

### Level 2: Client-Ready Staging Site
- **Purpose**: Full client review, content audit, and interactive user-testing on staging URL (e.g. `*.vercel.app` or `*.pages.dev`).
- **Includes**: Fully responsive multi-section site, genuine client assets, verified pricing, working WhatsApp/inquiry flows, dynamic components, and SEO metadata.
- **Explicit Limitation**: Final DNS cutover pending final client sign-off.

### Level 3: Production Release
- **Purpose**: Public-facing commercial deployment on client's custom domain (e.g., `meghmachang.com`).
- **Includes**: Full image optimization, production CDN caching, domain SSL configuration, verified analytics (Google Analytics/Plausible), verified first-party image licensing, error monitoring, and completed handover report.

---

## 2. Standard Handover Package

Every completed project workspace must include a comprehensive `HANDOVER.md` (or `antigravity/handover-report.md`) generated from `templates/handover-report.md`:

1. **Executive Summary**: Property name, deliverables produced, live staging URL or local run command.
2. **Architecture & Stack**: Framework, package manager, key libraries, and font licensing notes.
3. **Local Development Guide**:
   ```bash
   cd /home/mashrafe/Documents/Default\ Project/<project-slug>
   npm install
   npm run dev
   ```
4. **Environment Variables**: Document any required keys (e.g., Google Maps API key, Formspree endpoint, Resend API key) with example values.
5. **Asset Provenance & Photography Shot List**: Explicitly list any temporary images needing final client photography.
6. **Outstanding Items & Next Steps**: Next actionable milestones for the client team.

---

## 3. Deployment Playbooks

### A. Vercel (Preferred for Next.js and React)
```bash
npx vercel deploy --prod
```
- Ensure environment variables are configured in project settings.
- Verify automatic image optimization headers and cache invalidation.

### B. Cloudflare Pages (Preferred for Astro and Static Sites)
```bash
cf pages deploy ./dist --project-name <project-slug>
```
- Fast edge distribution with zero server maintenance costs.
- Free SSL and custom domain routing.
