---

# Accessibility Skill

When building any UI — web, mobile, or desktop — you MUST follow these accessibility rules. Every user deserves to use what you build, regardless of how they interact with it.

---

## Phase 1 — Semantic HTML

### NEVER do these:
- Use `<div>` or `<span>` for interactive elements instead of proper semantic tags
- Use `<div onClick>` as a substitute for `<button>`
- Use `<a href="#">` for actions that are not navigation
- Skip heading levels (e.g. jump from `<h1>` to `<h4>`)
- Use `<br>` for spacing between paragraphs

### ALWAYS do these:
- Use semantic HTML elements: `<nav>`, `<main>`, `<section>`, `<article>`, `<header>`, `<footer>`, `<aside>`
- Use `<button>` for actions, `<a>` for navigation — never mix them
- Maintain proper heading hierarchy: `<h1>` → `<h2>` → `<h3>` — never skip levels
- Use `<label>` for every form input — connect with `for`/`id` attributes
- Use `<table>` with `<thead>`, `<tbody>`, `<th>` for tabular data — never for layout

### BAD example:
```html
<div class="nav">
  <div onClick="goHome()">Home</div>
  <div onClick="openMenu()">Menu</div>
</div>
<div class="big-title">Subtitle</div>
<input type="email" placeholder="Email">
```

### GOOD example:
```html
<nav aria-label="Main navigation">
  <a href="/">Home</a>
  <button aria-expanded="false" aria-controls="menu">Menu</button>
</nav>
<h2>Subtitle</h2>
<label for="email">Email</label>
<input type="email" id="email" name="email">
```

---

## Phase 2 — Images and Media

### NEVER do these:
- Leave images without `alt` attributes
- Use descriptive `alt` text for decorative images (e.g. `alt="decorative line"`)
- Use images of text instead of actual text
- Embed videos without captions or transcripts
- Use autoplay for audio or video content

### ALWAYS do these:
- Every `<img>` must have an `alt` attribute
- Informative images: write concise, meaningful `alt` text that describes the content
- Decorative images: use `alt=""` (empty) so screen readers skip them
- Complex images (charts, diagrams): provide a text description nearby or use `aria-describedby`
- Videos must have captions, transcripts, or audio descriptions

### BAD example:
```html
<img src="chart.png">
<img src="divider.png" alt="decorative divider line">
```

### GOOD example:
```html
<img src="chart.png" alt="Revenue grew 40% from January to June 2026">
<img src="divider.png" alt="">
```

---

## Phase 3 — ARIA (Accessible Rich Internet Applications)

### NEVER do these:
- Use ARIA when a native HTML element does the job
- Add `role="button"` to a `<button>` — it already has that role
- Use `aria-label` to replace visible text when a `<label>` would work
- Create custom interactive components without ARIA roles and states
- Use `aria-hidden="true"` on elements that contain focusable content

### ALWAYS do these:
- Prefer native HTML elements over ARIA — `<button>` over `role="button"`
- Use ARIA only when native HTML cannot express the semantics
- Use `aria-label` or `aria-labelledby` for elements that need an accessible name but have no visible text
- Use `aria-expanded`, `aria-haspopup`, `aria-controls` for dropdowns, menus, and toggles
- Use `aria-live="polite"` for dynamic content that updates without page reload (notifications, chat messages, search results)
- Use `aria-live="assertive"` only for critical alerts that need immediate attention
- Use `aria-describedby` to link an element to its description

### BAD example:
```html
<div role="button" tabindex="0" class="dropdown">
  Settings
</div>
<div class="notification" role="alert">
  <!-- No aria-live, screen reader won't announce updates -->
</div>
```

### GOOD example:
```html
<button aria-expanded="false" aria-haspopup="true" aria-controls="settings-menu">
  Settings
</button>
<ul id="settings-menu" role="menu" hidden>
  <li role="menuitem">Profile</li>
  <li role="menuitem">Logout</li>
</ul>
<div aria-live="polite" class="notification">
  <!-- Screen reader will announce when content changes -->
</div>
```

---

## Phase 4 — Keyboard Navigation

### NEVER do these:
- Make any interactive element unreachable by keyboard
- Remove visible focus indicators without providing an alternative
- Trap keyboard focus without a way to escape (e.g. no Escape key handler)
- Rely on hover-only interactions — they are not keyboard accessible
- Use `tabindex` values greater than 0 (they break natural tab order)

### ALWAYS do these:
- Every interactive element must be reachable using Tab key
- Every interactive element must be activatable using Enter or Space
- Provide visible focus indicators — outline, border, or background change
- Modals and dialogs must trap focus inside and close on Escape
- Provide a "Skip to main content" link on pages with repetitive navigation
- Custom components (dropdowns, tabs, dialogs) must support full keyboard interaction:
  - Arrow keys for navigation within the component
  - Enter/Space to activate
  - Escape to close or go back
  - Tab to move out of the component

### BAD example:
```html
<!-- Mouse-only dropdown -->
<div class="dropdown" onMouseEnter="open()" onMouseLeave="close()">
  <div class="option">Option 1</div>
  <div class="option">Option 2</div>
</div>
```

### GOOD example:
```html
<button aria-expanded="false" aria-haspopup="listbox" aria-controls="options">
  Select option
</button>
<ul id="options" role="listbox" hidden>
  <li role="option" tabindex="-1" aria-selected="false">Option 1</li>
  <li role="option" tabindex="-1" aria-selected="false">Option 2</li>
</ul>
```

---

## Phase 5 — Color and Contrast

### NEVER do these:
- Use color as the ONLY way to convey information (e.g. red = error, green = success)
- Use light gray text on white backgrounds
- Use text smaller than 12px for body content
- Animate content without respecting `prefers-reduced-motion`

### ALWAYS do these:
- Maintain minimum contrast ratio of 4.5:1 for normal text (WCAG AA)
- Maintain minimum contrast ratio of 3:1 for large text (18px+ or 14px bold)
- Aim for 7:1 contrast ratio for WCAG AAA compliance
- Pair color with icons, text labels, or patterns to convey meaning
- Respect `prefers-reduced-motion` media query — disable or reduce animations for users who prefer it
- Ensure focus indicators have sufficient contrast (minimum 3:1 against adjacent colors)

### BAD example:
```css
/* Error shown only by color */
.error { color: red; }

/* Low contrast */
.body-text { color: #999; background: #fff; }

/* Ignores motion preference */
.modal { animation: slideIn 0.3s ease; }
```

### GOOD example:
```css
/* Error with icon and text */
.error { color: #DC2626; }
.error::before { content: "⚠ "; }

/* Good contrast */
.body-text { color: #374151; background: #fff; }

/* Respects motion preference */
@media (prefers-reduced-motion: no-preference) {
  .modal { animation: slideIn 0.3s ease; }
}
```

---

## Phase 6 — Forms and Input

### NEVER do these:
- Submit forms without validating input first
- Show errors only after form submission — not inline
- Use placeholder text as a substitute for labels
- Make required fields only indicated by color or asterisk without `aria-required`
- Disable form inputs without explaining why

### ALWAYS do these:
- Validate input inline — show errors as the user types or on blur
- Every input must have a visible `<label>` — placeholder is not a label
- Use `aria-required="true"` for required fields
- Use `aria-invalid="true"` on inputs with errors
- Link error messages to inputs using `aria-describedby`
- Group related fields with `<fieldset>` and `<legend>`
- Provide clear, specific error messages — not just "Invalid input"

### BAD example:
```html
<input type="email" placeholder="Email *">
<!-- Error appears only after submit -->
<div class="error" style="display:none">Invalid email</div>
```

### GOOD example:
```html
<label for="email">Email <span aria-hidden="true">*</span></label>
<input
  type="email"
  id="email"
  name="email"
  aria-required="true"
  aria-invalid="true"
  aria-describedby="email-error"
>
<div id="email-error" role="alert">
  Please enter a valid email address (e.g. user@example.com)
</div>
```

---

## Phase 7 — Accessibility Checklist

Run this checklist before finishing any UI task:

- [ ] All images have appropriate `alt` text (meaningful or empty for decorative)
- [ ] All form inputs have associated `<label>` elements
- [ ] Page has a single `<h1>` and proper heading hierarchy
- [ ] All interactive elements are keyboard accessible (Tab, Enter, Space, Escape)
- [ ] Focus indicators are visible on all interactive elements
- [ ] Color is not the only way to convey information
- [ ] Text contrast meets minimum 4.5:1 ratio
- [ ] Dynamic content updates use `aria-live` regions
- [ ] Custom components have proper ARIA roles and states
- [ ] Modals trap focus and close on Escape
- [ ] `prefers-reduced-motion` is respected for animations
- [ ] Touch targets are minimum 44x44px on mobile
- [ ] Page works at 200% zoom without horizontal scrolling
- [ ] Error messages are specific and linked to the relevant input

---

## Rule Summary

- Use semantic HTML first — ARIA only when native HTML is not enough
- Every image must have an `alt` attribute
- Every form input must have a visible `<label>`
- All interactive elements must be keyboard accessible
- Never use color alone to convey information
- Minimum 4.5:1 contrast ratio for all text
- Respect `prefers-reduced-motion` for animations
- Run the accessibility checklist before finishing any UI task
