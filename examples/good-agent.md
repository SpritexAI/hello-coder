# Good Agent — With Hello Coder

These are the same examples showing how the agent behaves after loading Hello Coder skills.

---

## Example 1 — New Feature Request

**User said:**
> "Add a login page to my app"

**Agent responded:**
> "Before I start, I have a few questions:
> 1. What framework and styling system is this project using?
> 2. Is there an existing authentication system I should connect to?
> 3. What should happen after a successful login — redirect to dashboard?
> 4. Should this match the existing dark theme I can see in the codebase?
> 5. Is there an existing button or input component I should reuse?
>
> Once I have these answers I will present a full plan before writing anything."

**After user answered:**
> "Here is my plan:
> - Create `pages/login.jsx` using existing `Button` and `Input` components
> - Connect to existing `/auth/login` endpoint already in `services/api.js`
> - Match dark theme using existing color variables from `globals.css`
> - Redirect to `/dashboard` on success, show inline error on failure
> - No new libraries needed
>
> Do you approve this plan? I will not write any code until you confirm."

**Result:** Exactly what the user wanted. First try.

---

## Example 2 — Bug Report

**User said:**
> "The submit button is not working on the contact form"

**Agent responded:**
> "Let me investigate before touching anything. Possible causes:
> 1. Button onClick handler missing or incorrectly bound
> 2. Form validation silently blocking submission
> 3. API call failing with no visible error shown to user
> 4. State not updating correctly before submission
>
> Tracing the code now... The most likely cause is #2 — the validation function returns false but there is no error message shown to the user, so the form appears frozen. The onClick handler is actually fine.
>
> Fix: Show validation errors inline so the user knows what to fix. Shall I proceed?"

**Result:** Real root cause found and fixed in one pass.

---

## Example 3 — UI Component

**User said:**
> "Build me a pricing card component"

**Agent responded:**
> "Before building, I want to confirm a few things:
> 1. I can see the project uses Inter font and a dark theme with `#111111` background — should this card match that?
> 2. Should this work on mobile as well as desktop?
> 3. Is there an existing Card component I should extend?
>
> I will use `clamp()` for font sizes and `rem` units for spacing so it scales correctly on all screen sizes. No hardcoded pixel values for layout."

**Result:**
- Matches existing design system perfectly
- Works on all screen sizes
- No new fonts or libraries added
- Looks like it belongs in the app

---

## Example 4 — Testing

**User said:**
> "Write tests for the payment service"

**Agent responded:**
> "I will write integration tests that test the real payment logic. I will only mock the external payment gateway API — not the internal service itself.
>
> Here is the actual test output:
> ```
> Running payment service tests...
> ✓ successful payment returns order confirmation (234ms)
> ✓ declined card returns 402 with clear error message (187ms)
> ✗ duplicate transaction detection FAILED
>   Expected: 409 Conflict
>   Received: 200 OK — duplicate was processed
>
> 2 passed, 1 failed
> ```
>
> Found a real bug — duplicate transactions are not being caught. Shall I fix this?"

**Result:** Real bug found before it reached production.

---

## Example 5 — Planning

**User said:**
> "Build a notification system"

**Agent responded:**
> "Notification systems can mean very different things. Before I plan anything:
> 1. Do you need in-app UI notifications only, or also email or push notifications?
> 2. Do notifications need to persist — should users see old ones after refresh?
> 3. Is this for real-time events or just UI feedback like success and error toasts?
> 4. How many users will this serve — does scale matter now?
>
> This will completely change the approach. A simple toast system takes 20 minutes. A real-time persistent system takes days."

**User answered:** Just UI toast feedback for now.

**Agent responded:**
> "Plan:
> 1. Create `components/Toast.jsx` — simple overlay notification
> 2. Create `context/ToastContext.jsx` — global trigger from anywhere
> 3. Add ToastProvider to root layout
>
> Do you approve? I will start with Step 1 and show you before continuing."

**Result:** 25 minutes. Exactly what was needed. Nothing more.

---

*This is what every agent should do. This is Hello Coder.*
