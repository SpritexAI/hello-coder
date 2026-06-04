---

# Frontend Developer Profile

This profile activates the following skills automatically for any frontend task:

- `skills/planning.md` — gather full context before starting
- `skills/ui.md` — professional colors, fonts, spacing, responsive design
- `skills/debug.md` — systematic debugging, no tunnel vision
- `skills/review.md` — self-review all code before presenting
- `skills/decisions.md` — never assume, always ask before choosing

---

## Additional Frontend Rules

### Before Starting Any Frontend Task:
1. Ask what framework is being used (React, Next.js, Vue, Jetpack Compose, SwiftUI etc.)
2. Ask if there is an existing design system or component library
3. Ask if there are existing components that should be reused
4. Ask for target devices — mobile only, desktop only, or both

### Component Rules:
- Never create a new component if a similar one already exists in the codebase
- Always check the existing component folder before writing anything new
- Every component must work on both mobile and desktop unless told otherwise
- Every component must handle loading state, empty state, and error state

### State Management Rules:
- Do not introduce a new state management library without asking
- Keep state as local as possible — do not put everything in global state
- Never store derived data in state — compute it instead

### Performance Rules:
- No unnecessary re-renders — think before adding state or props
- No importing an entire library for one function
- Images must always have defined width and height to prevent layout shift

---

## Rule Summary

- Always plan before building
- Always ask about existing design system and components
- Every component must be responsive and handle all states
- No new patterns without asking first
