---

# Review Skill

After writing any code, you MUST review your own work before presenting it to the user. Never hand over unreviewed code.

---

## Phase 1 — Immediate Self Review

Right after writing code, read through it completely and check:

1. Does this code actually do what was asked?
2. Are there any obvious bugs or logic errors?
3. Are there any unhandled edge cases?
4. Are there any null or undefined values that could crash the code?
5. Are there any hardcoded values that should be variables or configs?

If you find any issue — fix it before showing the user. Never say "this might have a bug" and hand it over anyway.

---

## Phase 2 — Consistency Check

Check that the new code matches the existing codebase:

1. Does it follow the same naming conventions?
2. Does it follow the same folder and file structure?
3. Does it use the same patterns already present in the project?
4. Does it import or use existing utilities instead of rewriting them?

Never introduce a new pattern when an existing one already works.

---

## Phase 3 — Security Check

Before finalizing, check for these common issues:

- No API keys, secrets, or passwords hardcoded in the code
- No user input used directly in database queries without sanitization
- No sensitive data being logged to console
- No endpoints left unprotected that should require authentication

---

## Phase 4 — Final Output Format

When presenting code to the user, always include:

1. A short summary of what was done
2. Which files were created or modified
3. Any assumptions that were made
4. Anything the user should manually check or test

Example format:
Done. Here is what was completed:
Created: handlers/auth.go — login and register handlers
Modified: routes/routes.go — added /login and /register routes
Assumption: JWT secret is read from environment variable JWT_SECRET
Please test: login with wrong password should return 401
---

## Hard Rules

- Never present code you have not read through yourself
- Never say "I think this should work" — verify it logically before handing over
- Never leave TODO comments in final code without flagging them explicitly to the user
- Never modify files that were not part of the task without asking first

---

## Rule Summary

- Always self-review before presenting code
- Check for bugs, edge cases, nulls, and hardcoded values
- Match existing codebase patterns and conventions
- Flag assumptions and things to manually test
- Never hand over code you are not confident in
