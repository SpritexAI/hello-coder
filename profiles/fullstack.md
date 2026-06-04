---

# Fullstack Developer Profile

This profile activates ALL skills for any fullstack task:

- `skills/planning.md` — gather full context before starting
- `skills/ui.md` — professional colors, fonts, spacing, responsive design
- `skills/debug.md` — systematic debugging, no tunnel vision
- `skills/workflow.md` — break complex tasks into small steps
- `skills/review.md` — self-review all code before presenting
- `skills/decisions.md` — never assume, always ask before choosing
- `skills/testing.md` — real tests only, no fake results

---

## Additional Fullstack Rules

### Before Starting Any Fullstack Task:
1. Ask what frontend framework is being used
2. Ask what backend language and framework is being used
3. Ask what database is being used
4. Ask how the frontend and backend communicate — REST, GraphQL, WebSocket, SSE
5. Ask if there is an existing design system or component library
6. Ask about authentication — is it already implemented or needs to be built

### Frontend + Backend Connection Rules:
- Always agree on the API contract before building either side
- Define request and response structure first — then build
- Never build the frontend assuming an API shape that has not been confirmed
- Never build the backend returning a shape the frontend has not agreed on
- If the API changes mid-task, stop and update both sides together

### Separation of Concerns:
- Business logic belongs in the backend — never in the frontend
- The frontend only displays data and handles user interaction
- Never call the database directly from the frontend
- Never put secrets or API keys in frontend code — ever

### Fullstack Workflow Order:
Always follow this order for any new feature:
1. Plan the full feature — both frontend and backend
2. Define the API contract — endpoint, request, response
3. Build and test the backend endpoint first
4. Build the frontend to consume the confirmed backend
5. Test the full flow end to end

### Shared Rules:
- No hardcoded values anywhere — frontend or backend
- Consistent error handling on both sides
- Loading, empty, and error states on every frontend component
- Every backend endpoint validated, authenticated where needed, and tested

---

## Rule Summary

- Plan both sides together before building anything
- Define API contract first — then build frontend and backend
- Business logic in backend only — never in frontend
- No secrets in frontend code ever
- Test the full flow end to end after completing both sides
