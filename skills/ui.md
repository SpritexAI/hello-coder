---

# UI Design Skill

When building any UI — web, mobile, or desktop — you MUST follow these rules. No exceptions.

---

## Colors

### DO NOT use these:
- Bright, saturated colors as backgrounds (e.g. `#FF0000`, `#00FF00`, `#0000FF`)
- Random color combinations that are not tested for contrast
- More than 3 primary colors in a single UI
- Neon or glowing colors unless the design explicitly requires it
- Colors that look "AI-picked" — overly vibrant, mismatched, or childish

### DO use these:
- A maximum of 1 accent color + neutral base (dark or light)
- Dark backgrounds: `#0F0F0F`, `#111111`, `#1A1A1A`, `#18181B`
- Light backgrounds: `#FFFFFF`, `#F9F9F9`, `#F4F4F5`
- Accent colors that are desaturated and professional:
  - Blue: `#3B82F6` or `#2563EB`
  - Indigo: `#6366F1`
  - Zinc: `#71717A`
  - Neutral grays for borders: `#27272A`, `#3F3F46`
- Always check contrast ratio — body text must be minimum 4.5:1 against background

---

## Typography

### DO NOT use these:
- Decorative or display fonts for body text (e.g. Pacifico, Lobster, Satisfy)
- More than 2 font families in a single UI
- Random font sizes without a clear hierarchy
- All-caps for long paragraphs

### DO use these:
- System fonts or professional fonts only:
  - `Inter` — best for web UI
  - `Geist` — modern, clean
  - `JetBrains Mono` — for code blocks only
  - System default stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- Clear font size hierarchy:
  - Heading 1: 32px–48px
  - Heading 2: 24px–32px
  - Body: 14px–16px
  - Caption: 12px
- Font weight: 400 for body, 500–600 for labels, 700 for headings only

---

## Spacing & Layout

- Use consistent spacing units: 4px, 8px, 12px, 16px, 24px, 32px, 48px
- Never place elements randomly — always align to a grid
- Minimum touch target size on mobile: 44x44px
- Padding inside cards: minimum 16px
- Never crowd elements — when in doubt, add more whitespace

---

## Component Rules

- Buttons must have clear hover and active states
- Inputs must have visible focus rings
- Cards must have subtle borders or shadows — never floating without definition
- Icons must be consistent in size and style — do not mix icon sets
- Loading states must always be shown — never leave the user guessing

---

## Responsive Design

### DO NOT do these:
- Hardcode any width, height, padding, or font size in fixed px values for layout
- Use fixed widths like `width: 360px` or `height: 80px` for containers
- Build only for desktop and forget mobile
- Use `px` for layout spacing that needs to scale
- Assume the screen is a specific size

### DO these:
- Always build for both desktop and mobile from the start — not as an afterthought
- Use relative units for layout:
  - `%` or `vw/vh` for widths and heights
  - `rem` or `em` for font sizes and spacing
  - `min()`, `max()`, `clamp()` for fluid sizing
- Use CSS Flexbox or Grid — never float-based layouts
- For padding and spacing, use scalable tokens:
  - Instead of `padding: 16px` → use `padding: 1rem` or a CSS variable like `var(--space-4)`
- For font sizes, use fluid scaling:
  - Instead of `font-size: 32px` → use `clamp(20px, 4vw, 32px)`
- Test every component at these breakpoints:
  - Mobile: 375px
  - Tablet: 768px
  - Desktop: 1280px
- Use CSS media queries or framework breakpoints consistently — never one-off fixes

### Responsive Checklist (run before finishing any UI task):
- [ ] Does it look correct on 375px mobile width?
- [ ] Does it look correct on 1280px desktop width?
- [ ] Are all font sizes using relative units?
- [ ] Are all layout spacings using relative units or CSS variables?
- [ ] Are touch targets minimum 44x44px on mobile?

---

## Rule Summary

- Max 1 accent color + neutral base
- Professional fonts only — Inter or system font
- Consistent spacing scale
- No random combinations — every decision must have a reason
- If it looks "AI-made" at first glance, redo it
- Always build responsive — desktop AND mobile from the start
- No hardcoded px values for layout, spacing, or font sizes
