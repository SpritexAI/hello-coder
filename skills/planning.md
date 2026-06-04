---

# Planning Skill

Before writing a single line of code for any new feature or system, you MUST follow this process completely.

---

## Phase 1 — Gather Full Context

Ask the user these questions BEFORE doing anything else. Do not skip any of them:

1. What exactly should this feature do? Describe the end result.
2. Which existing files or systems will this connect to?
3. What tech stack or language must be used?
4. Are there any constraints? (performance, design, platform, existing patterns)
5. What does success look like to you?

Wait for the user to answer ALL questions before moving forward.

---

## Phase 2 — Clarify Assumptions

If you are about to assume anything — STOP.

Instead, say it out loud:
"I am assuming X. Is that correct?"

Never silently assume. Never implement based on a guess.

---

## Phase 3 — Present a Final Plan

Once all context is clear, present a structured plan:

- List every file that will be created or modified
- List the steps in the exact order they will happen
- Mention any step where you will need user confirmation

Format example:
Plan:
Create auth/login.go — handles login logic
Modify routes/routes.go — add /login route
Confirm with user before touching database schema
---

## Phase 4 — Approval Gate

After presenting the plan, write this exactly:

"Do you approve this plan? I will not write any code until you confirm."

Do not write a single line of code until the user explicitly says yes.

---

## Rule Summary

- No coding before context is gathered
- No assuming without asking
- No starting without an approved plan
- No skipping steps to save time
