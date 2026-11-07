# Reference: Frontend Craft & Engineering Standards

## Purpose

A bespoke stay website demands engineering rigor equal to its visual artistry. Clunky load times, jarring layout shifts, or broken mobile navigation destroy luxury perception instantly. This reference establishes our frontend architecture, stack selection, and craftsmanship standards.

---

## 1. Stack Selection Matrix

Never force every client into a monolithic default framework. Select the right tool for the job:

| Project Needs | Recommended Stack | Rationale |
| :--- | :--- | :--- |
| **High Content, Editorial, Static Media Showcase, Ultimate Speed** | **Astro + Tailwind CSS / Vanilla CSS** | Zero JavaScript by default, phenomenal image optimization via Sharp, instantaneous SSG page loads, perfect Lighthouse scores. Ideal for boutique retreats and lodges. |
| **Dynamic Booking Engine, Client Portal, Complex Modals, Interactive Filtering** | **Next.js (App Router) + React 19 + Tailwind CSS** | Server Components, dynamic API routes, seamless client-side state for real-time room availability, interactive date pickers, multi-step booking wizards. |
| **Rapid Concept Demo, Lightweight Single-Page Presentation** | **Vite + React / HTML5 + Tailwind** | Lightning-fast development loop, portable single-bundle deployment, zero friction for immediate stakeholder reviews. |

---

## 2. Craftsmanship Checklist

### A. Typography & Rendering
- **Self-Host All Fonts**: Never rely on external Google Fonts CDN links that block render or flash unstyled text (FOUT). Store `.woff2` files locally in `/public/fonts/` with `font-display: swap`.
- **Text Wrapping & Balance**: Use `text-wrap: balance` on headlines and `text-wrap: pretty` on editorial body paragraphs to eliminate awkward orphan words.
- **Font Kerning & Ligatures**: Enable `font-feature-settings: "kern" 1, "liga" 1` for display serif typefaces.

### B. Image Pipeline & Responsive Art Direction
- Utilize modern HTML picture tags for art direction (e.g. vertical framing on mobile, cinematic horizontal framing on desktop):
  ```html
  <picture>
    <source media="(max-width: 768px)" srcset="/img/cottage-mobile.webp" type="image/webp" />
    <source media="(min-width: 769px)" srcset="/img/cottage-desktop.webp" type="image/webp" />
    <img src="/img/cottage-fallback.jpg" alt="Sunrise view over Sajek Valley from Cottage 3 private bamboo deck" width="1920" height="1080" loading="lazy" decoding="async" />
  </picture>
  ```
- Explicit `width` and `height` attributes on every `<img>` to enforce aspect-ratio and prevent Cumulative Layout Shift (CLS = 0).
- Hero above-the-fold image: `loading="eager"` with `fetchpriority="high"`. All subsequent gallery images: `loading="lazy"`.

### C. Interaction & Animation Refinement
- Animations must be hardware-accelerated: stick to `transform` and `opacity`. Avoid animating `height`, `width`, `top`, or `padding` which trigger browser reflows.
- Respect user system preferences:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```
- Interactive states: Hover transitions on buttons and room cards should feel buttery and weighted (`transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)`), never instant or jerky.

---

## 3. SEO & Structured Hospitality Metadata

Hotels and resorts win significant direct bookings when Google accurately indexes their property details.

### JSON-LD LodgingBusiness Schema
Always embed comprehensive Schema.org metadata in the `<head>` of the site:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LodgingBusiness",
  "name": "Megh Machang",
  "description": "Eco-retreat featuring elevated bamboo cottages above the clouds in Sajek Valley.",
  "image": ["https://meghmachang.com/og-hero.jpg"],
  "priceRange": "৳3500 - ৳5500",
  "telephone": "+8801XXXXXXXXX",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Ruilui Para",
    "addressLocality": "Sajek Valley",
    "addressRegion": "Rangamati",
    "addressCountry": "BD"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 23.3824,
    "longitude": 92.2938
  },
  "checkinTime": "12:00",
  "checkoutTime": "10:00",
  "petsAllowed": false,
  "starRating": {
    "@type": "Rating",
    "ratingValue": "4.5"
  }
}
</script>
```

### Essential Meta Tags
- Title format: `[Property Name] | [Bespoke Proposition] — [Location]` (e.g. `Megh Machang | Bamboo Cottages Above the Clouds — Sajek Valley`).
- Distinct OpenGraph image (`1200x630`) showcasing the most stunning hero visual.
- Canonical URL tag pointing to production domain.

---

## 4. Accessibility (WCAG 2.1 AA Compliance)

- **Contrast Ratios**: Body copy must maintain ≥ 4.5:1 contrast against background; large headlines ≥ 3:1.
- **Focus Rings**: Never remove `outline: none` without providing an elegant custom keyboard focus indicator.
- **Descriptive Alt Text**: Never use empty or generic alt text like "image.jpg" or "hotel photo". Describe the authentic architectural scene: `"Hand-woven bamboo balcony with rocking chairs overlooking the morning cloud sea in Ruilui Para"`.
- **Keyboard Navigation**: Modals, mobile drawer menus, and photo lightboxes must support keyboard `Escape` to close and focus trapping.
