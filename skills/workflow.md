---

# Workflow Skill

When working on any task — especially complex ones — you MUST break it into small, controlled steps. Never attempt everything at once.

---

## Phase 1 — Break the Task Down

Before starting any work, split the task into the smallest possible steps.

Example format:
Task: Add user authentication
Steps:
Create user table in database
Build register endpoint
Build login endpoint
Implement JWT token generation
Add auth middleware to protected routes
Test each endpoint individually

No step should do more than one thing. If a step feels too big, break it down further.

---

## Phase 2 — One Step at a Time

- Complete one step fully before moving to the next
- After each step, show the user what was done
- Ask for confirmation before moving to the next step if the step was significant

### Confirmation checkpoint example:
"Step 1 complete — user table created with columns: id, email, password_hash, created_at. Ready to move to Step 2?"

---

## Phase 3 — Do Not Jump Ahead

### NEVER do these:
- Write 10 files at once without showing progress
- Skip steps because they "seem obvious"
- Combine multiple steps silently to "save time"
- Start the next step before the current one is verified working

### ALWAYS do these:
- Finish what you started before moving on
- If a step reveals new complexity, stop and re-plan
- Keep the user informed at every stage

---

## Phase 4 — Handle Complexity Mid-Task

If during implementation you discover the task is more complex than planned:

1. Stop immediately — do not continue with the original plan
2. Explain what new complexity was found
3. Present a revised plan
4. Get user approval before continuing

Never silently expand the scope of a task.

---

## Phase 5 — End of Task Checklist

After completing all steps:
- [ ] Every step from the plan was completed
- [ ] No unplanned files were created or modified
- [ ] No scope was silently added
- [ ] User was informed at each major checkpoint
- [ ] Everything works as described in the original plan

---

## Rule Summary

- Always break tasks into small single-purpose steps
- One step at a time — never rush ahead
- Show progress after each step
- If complexity grows mid-task, stop and re-plan
- Never silently expand scope
