---

# Debug Skill

When debugging any issue, you MUST follow this process completely. Never jump to a fix without investigation.

---

## Phase 1 — Understand Before Touching

Before changing any code, answer these questions:

1. What is the exact error message or unexpected behavior?
2. Where in the code is it happening? (file, line, function)
3. When does it happen? (always, sometimes, only in certain conditions)
4. What was the last change made before this bug appeared?

Do not touch any code until you can answer all 4 questions.

---

## Phase 2 — List All Possible Causes

Before fixing, list EVERY possible cause of the problem. Do not stop at the first one you find.

Example format:
Possible causes:
Null value not being handled in getUserData()
API response structure changed — field renamed
Race condition between two async calls
Wrong environment variable being read
List at least 3 possible causes before proceeding. If you can only think of 1, look harder.

---

## Phase 3 — Identify the Most Likely Cause

After listing all possible causes:
- Rank them by likelihood
- Explain WHY the top cause is most likely
- Do not guess — trace the code path logically

---

## Phase 4 — Fix Only the Root Cause

- Fix the root cause — not the symptom
- Do not add workarounds or patches that hide the problem
- Do not change unrelated code while fixing
- One fix at a time — never fix multiple things simultaneously

---

## Phase 5 — Verify the Fix

After applying the fix:
1. Explain exactly why this fix solves the problem
2. Check if the same bug could exist in other parts of the codebase
3. Confirm no new issues were introduced by the fix

---

## Hard Rules

- NEVER fix the first thing you see without investigating
- NEVER change multiple things at once to "see what works"
- NEVER ignore an error message — read it fully and carefully
- NEVER assume the bug is in a different layer than where the error points
- If you are stuck after Phase 3, tell the user exactly what you found — do not silently guess

---

## Rule Summary

- Understand fully before touching anything
- List all possible causes — minimum 3
- Fix root cause only, not symptoms
- One fix at a time
- Verify and explain after every fix
