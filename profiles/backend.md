---

# Backend Developer Profile

This profile activates the following skills automatically for any backend task:

- `skills/planning.md` — gather full context before starting
- `skills/debug.md` — systematic debugging, no tunnel vision
- `skills/workflow.md` — break complex tasks into small steps
- `skills/testing.md` — real tests only, no fake results
- `skills/review.md` — self-review all code before presenting
- `skills/decisions.md` — never assume, always ask before choosing

---

## Additional Backend Rules

### Before Starting Any Backend Task:
1. Ask what language and framework is being used
2. Ask what database is being used and how it is connected
3. Ask if there are existing patterns for routes, handlers, and responses
4. Ask if authentication is required for the new endpoint
5. Ask about rate limiting or any access restrictions

### API Design Rules:
- Follow existing endpoint naming conventions in the codebase
- Always validate incoming request data before processing
- Always return consistent response structures — success and error
- Never expose internal error messages or stack traces to the client
- Every endpoint that modifies data must require authentication unless explicitly told otherwise

### Database Rules:
- Never run raw queries with unsanitized user input
- Always use transactions when multiple writes depend on each other
- Never drop or alter a table without explicit user confirmation
- Always add indexes for columns that will be used in WHERE or JOIN clauses
- Never use SELECT * in production queries — always specify columns

### Security Rules:
- No secrets, API keys, or passwords hardcoded anywhere
- All sensitive config must come from environment variables
- Passwords must always be hashed — never stored as plain text
- Log errors for debugging but never log sensitive user data

### Error Handling Rules:
- Every endpoint must have proper error handling
- Never let an unhandled error crash the server
- Return meaningful HTTP status codes:
  - 200 for success
  - 201 for created
  - 400 for bad request
  - 401 for unauthorized
  - 403 for forbidden
  - 404 for not found
  - 500 for server error

---

## Rule Summary

- Always plan and ask about existing patterns before building
- Validate all input, sanitize all queries
- Consistent response structure for every endpoint
- No hardcoded secrets — environment variables only
- Real tests only — show actual results
