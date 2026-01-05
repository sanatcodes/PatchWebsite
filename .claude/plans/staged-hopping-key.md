# Plan: Port Static HTML/CSS to Astro Components

## Overview
Port `zed.dev-fun/index2.html` and `index2.css` into the Astro project at `PatchWebsiteCode/`, decomposing into modular, reusable components while maintaining visual parity.

---

## File Structure

```
PatchWebsiteCode/src/
├── styles/
│   └── global.css              # CSS variables, reset, base styles
├── components/
│   ├── ui/                     # Atomic components
│   │   ├── Button.astro        # Primary/secondary variants
│   │   ├── Avatar.astro        # User avatar with gradient
│   │   ├── Divider.astro       # Line with corner diamonds
│   │   └── SectionHeader.astro # Title + subtitle pattern
│   ├── cards/
│   │   ├── CardAlt.astro       # Blog/media card (sh-alt shadow)
│   │   ├── SmallCard.astro     # Compact feature card
│   │   └── TestimonialCard.astro # Quote with author
│   └── sections/
│       ├── Header.astro        # Sticky nav
│       ├── Hero.astro          # Hero with grid background
│       ├── MainCard.astro      # Feature card overlapping hero
│       ├── CardGridSection.astro
│       ├── SquareGradientSection.astro
│       ├── SmallCardsSection.astro
│       ├── FeaturedTestimonial.astro
│       ├── TestimonialsGrid.astro
│       ├── LetterSection.astro # With spinning badge
│       └── Footer.astro
├── layouts/
│   └── Layout.astro            # Update to import global.css
└── pages/
    └── index.astro             # Assemble all sections
```

**Assets to move:**
- `zed.dev-fun/PatchLogoBlue.svg` → `public/PatchLogoBlue.svg`
- `zed.dev-fun/PatchLogoBlue_Padded.svg` → `public/PatchLogoBlue_Padded.svg`

---

## Component Specifications

### UI Components

| Component | Props | Slots | Notes |
|-----------|-------|-------|-------|
| `Button.astro` | `variant: 'primary'\|'secondary'`, `href?: string` | default (content) | Renders `<a>` if href provided |
| `Avatar.astro` | `initials: string`, `size?: 'sm'\|'md'` | - | 32px/36px with gradient background |
| `Divider.astro` | - | - | Full-width line + corner diamonds |
| `SectionHeader.astro` | `title: string`, `subtitle?: string` | - | Centered section title pattern |

### Card Components

| Component | Props | Slots | Notes |
|-----------|-------|-------|-------|
| `CardAlt.astro` | `title: string`, `description: string` | `image` | sh-alt shadow, hover effect |
| `SmallCard.astro` | `title: string`, `subtitle: string` | - | Inset→offset shadow on hover |
| `TestimonialCard.astro` | `quote`, `authorName`, `authorTitle`, `initials` | - | Quote with author info |

### Section Components

| Component | Props | Slots | Notes |
|-----------|-------|-------|-------|
| `Header.astro` | `logoText?: string` | - | Sticky nav with corner diamonds |
| `Hero.astro` | `headline`, `description` | `actions` | Inline SVG grid pattern |
| `MainCard.astro` | - | `features`, `content` | -128px margin overlap |
| `CardGridSection.astro` | `title`, `subtitle?` | default (cards) | 3-column responsive grid |
| `SquareGradientSection.astro` | `title`, `description` | `actions` | Blue gradient border |
| `SmallCardsSection.astro` | `title`, `subtitle?` | default (cards) | auto-fill grid |
| `FeaturedTestimonial.astro` | `quote`, `authorName`, `authorTitle`, `initials` | `logo` | Grid background, highlights |
| `TestimonialsGrid.astro` | - | default (4 cards) | 2x2 grid with borders |
| `LetterSection.astro` | `label`, `title`, `signature` | default (body) | Logo background + spinning badge |
| `Footer.astro` | - | default | Simple footer |

---

## Implementation Order

### Phase 1: Foundation
1. **Create `src/styles/global.css`**
   - CSS variables (colors, shadows, borders)
   - Reset and base styles
   - Typography utilities
   - Main container with side borders
   - Noise texture (commented with TODO)

2. **Update `src/layouts/Layout.astro`**
   - Import global.css
   - Add main-container div wrapper

3. **Copy SVG assets to `public/`**

### Phase 2: Atomic Components
4. `Button.astro` - Primary/secondary with inset shadows
5. `Avatar.astro` - Gradient background avatar
6. `Divider.astro` - Line with diamond corners
7. `SectionHeader.astro` - Title + subtitle

### Phase 3: Card Components
8. `SmallCard.astro` - Compact card
9. `CardAlt.astro` - Blog-style card
10. `TestimonialCard.astro` - Quote card

### Phase 4: Section Components
11. `Header.astro` - Sticky nav
12. `Hero.astro` - With inline SVG grid
13. `MainCard.astro` - Feature row + content area
14. `CardGridSection.astro`
15. `SquareGradientSection.astro`
16. `SmallCardsSection.astro`
17. `FeaturedTestimonial.astro`
18. `TestimonialsGrid.astro`
19. `LetterSection.astro` - With spinning badge animation
20. `Footer.astro`

### Phase 5: Page Assembly
21. **Update `src/pages/index.astro`**
    - Import all section components
    - Assemble in correct order with dividers

### Phase 6: Verification
22. Run `npm run dev` and compare with original

---

## Key Implementation Details

### CSS Variables (global.css)
```css
:root {
  --color-cream-50: #f5f4ef;
  --color-blue-200: #bedbff;
  --color-accent-blue: #0751cf;
  --sh-default: 6px 6px 0 rgba(7,77,207,0.06), -6px -6px 0 rgba(7,77,207,0.06);
  --sh-alt: 6px 6px 0 rgba(7,77,207,0.06);
  --grid-border-color: rgba(190, 219, 255, 0.5);
  /* ... full list from index2.css lines 7-44 */
}
```

### Noise Texture Handling
The noise texture is available at `PatchWebsiteCode/public/noise.png`. Use:
```css
body::before {
  background-image: url('/noise.png');
  background-size: 180px;
  background-repeat: repeat;
  opacity: 0.035;
  /* ... */
}
```

### SVG Grid Pattern (inline in Hero/FeaturedTestimonial)
Must be inline for `mask-image` to work. Use unique pattern IDs:
- Hero: `id="hero-grid-pattern"`
- Testimonial: `id="testimonial-grid-pattern"`

### Spinning Badge Animation
```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.letter-badge { animation: spin 20s linear infinite; }
```

### Responsive Breakpoints
- 1024px: Stack feature row
- 768px: Single-column cards
- 640px: Letter section stacks
- 480px: Minimal margins

---

## Critical Source Files

| File | Purpose |
|------|---------|
| `zed.dev-fun/index2.html` | HTML structure, inline SVGs, content |
| `zed.dev-fun/index2.css` | All styles, CSS variables, shadows |
| `PatchWebsiteCode/src/layouts/Layout.astro` | Existing layout to enhance |
| `PatchWebsiteCode/src/pages/index.astro` | Target page file |

---

## Verification Checklist
- [ ] All sections render at desktop (1200px+)
- [ ] Responsive at 768px and 480px
- [ ] Grid patterns fade correctly with mask
- [ ] Hover effects work on cards/buttons
- [ ] Badge spins continuously
- [ ] Sticky header works
- [ ] MainCard overlaps hero
- [ ] Corner diamonds positioned correctly
- [ ] Typography matches (Georgia serif for headlines)
- [ ] Shadow system matches (sh-default, sh-alt)
