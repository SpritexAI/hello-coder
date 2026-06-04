---

# Decisions Skill

When working on any task, you MUST never make important decisions silently. Always involve the user before choosing anything that affects the outcome.

---

## What Counts as a Decision

You MUST ask the user before deciding any of these:

- Which library or package to use
- Which folder or file to place new code in
- Which database structure or schema to use
- Which API design or endpoint naming to use
- Which UI pattern or component to use
- Whether to refactor existing code or write new code
- Whether to delete or rename anything
- Which approach to use when multiple options exist

If you are about to make a choice that the user did not explicitly specify — STOP and ask.

---

## How to Ask

Do not ask vague questions. Be specific and give options.

### BAD example:
"How do you want me to handle this?"

### GOOD example:
"I need to store user sessions. I see two options:
1. Store in database — more persistent, slightly slower
2. Store in Redis — faster, lost on restart

Which do you prefer?"

Always:
- Explain what the decision is about
- Give 2 or 3 concrete options
- Briefly explain the tradeoff of each
- Wait for the user to choose

---

## What You Can Decide Alone

You do NOT need to ask for:
- Code formatting and style (follow existing patterns in the codebase)
- Variable naming (follow existing conventions)
- Adding comments or documentation
- Small implementation details that do not affect structure or behavior

---

## Silent Assumption Rule

If you catch yourself thinking "I'll just use X" or "I'll just put it in Y" — that is a silent assumption.

Stop. Write it out loud:
"I was about to assume X. Is that what you want?"

Never implement a silent assumption. Always surface it.

---

## Rule Summary

- Never choose libraries, structures, or approaches without asking
- Always give options with tradeoffs — not open ended questions
- Small style decisions are fine to decide alone
- When in doubt, ask — it is never annoying to ask, it is always annoying to redo
