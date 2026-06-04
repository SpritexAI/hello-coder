# Bad Agent — Without Hello Coder

These are real examples of how AI coding agents behave without any skill guidance.

---

## Example 1 — New Feature Request

**User said:**
> "Add a login page to my app"

**Agent did:**
- Immediately created 8 files without asking anything
- Picked a bright blue and white color scheme that clashes with the existing dark theme
- Used a library called `react-hook-form` that was never in the project
- Hardcoded the API endpoint as `http://localhost:3000/auth/login`
- Wrote zero error handling
- Said "Done! Your login page is ready" without testing anything

**Problems:**
- Wrong colors — looks completely different from the rest of the app
- New library added without asking — now there is an unexpected dependency
- Hardcoded localhost URL — breaks in production immediately
- No error handling — blank screen if login fails
- Never asked what the existing auth system looks like

---

## Example 2 — Bug Report

**User said:**
> "The submit button is not working on the contact form"

**Agent did:**
- Looked at the button component
- Found that `onClick` was missing a function reference
- Fixed only that one thing
- Said "Fixed! The button was missing its onClick handler"

**What actually happened:**
- The real bug was that the form validation was blocking submission silently
- The missing onClick was a separate unrelated issue
- After the fix, the button fired but the form still did not submit
- User had to come back and report the same problem again
- Agent wasted time fixing the wrong thing

**Problems:**
- Did not investigate all possible causes
- Fixed the first thing it saw
- Never verified the fix actually solved the original problem

---

## Example 3 — UI Component

**User said:**
> "Build me a pricing card component"

**Agent did:**
- Built the card with `width: 380px` hardcoded
- Used `font-size: 24px` hardcoded for the title
- Used `padding: 20px` hardcoded everywhere
- Only tested on desktop — completely broken on mobile
- Picked purple and orange as the color scheme
- Used the font `Raleway` which was never in the project

**Problems:**
- Hardcoded sizes break on every screen size except one
- Colors look random and unprofessional
- New font added without asking — inconsistent with the rest of the app
- Mobile layout completely broken

---

## Example 4 — Testing

**User said:**
> "Write tests for the payment service"

**Agent did:**
- Wrote tests that mocked the entire payment service
- Every test passed immediately
- Said "All 8 tests passing!"

**What actually happened:**
- The mock replaced the real payment logic entirely
- The tests were testing the mock, not the actual code
- Real bugs in the payment service were completely undetected
- False confidence — user thought the service was tested and safe

**Problems:**
- Mocked the subject of the test — which makes the test meaningless
- Reported passing tests that proved nothing
- Real bugs shipped to production

---

## Example 5 — Planning

**User said:**
> "Build a notification system"

**Agent did:**
- Immediately started building
- Created a WebSocket system from scratch
- Built a full notifications database table
- Added a background job queue
- After 2 hours of work, presented everything to the user

**What the user actually wanted:**
- Just a simple in-app toast notification for UI feedback
- No persistence needed
- No WebSocket needed
- A 20 minute job became a 2 hour mess

**Problems:**
- Never asked what kind of notification system
- Assumed the most complex interpretation
- Built the wrong thing completely
- All work had to be thrown away

---

*All of these problems are solved by Hello Coder.*
