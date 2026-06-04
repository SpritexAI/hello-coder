---

# Testing Skill

When testing any code, you MUST follow real testing practices. Never fake results, never mock real behavior to hide failures.

---

## Phase 1 — Understand What Needs Testing

Before writing any test, identify:

1. What is the expected input?
2. What is the expected output?
3. What are the edge cases?
4. What should happen when something goes wrong?

Never write a test without knowing the answer to all 4 questions.

---

## Phase 2 — Real Tests Only

### NEVER do these:
- Return hardcoded success responses to make a test pass
- Mock a function that is the actual subject of the test
- Write a test that can never fail
- Skip testing error cases and only test the happy path
- Pretend a test passed when it was never actually run

### ALWAYS do these:
- Test real behavior with real inputs
- Test both success cases AND failure cases
- Test edge cases — empty input, null values, maximum values
- Run the test and show the actual output to the user

---

## Phase 3 — Test Categories

### Unit Tests
- Test one function or module at a time
- No network calls, no database — use mocks ONLY for external dependencies
- Must be fast and deterministic — same input always gives same output

### Integration Tests
- Test how multiple parts work together
- Use a real test database — never the production database
- Clean up all test data after the test runs

### Manual Testing Checklist
When automated tests are not possible, follow this checklist:
- [ ] Tested the happy path — normal expected usage
- [ ] Tested with missing or empty input
- [ ] Tested with invalid input
- [ ] Tested error handling — what happens when it fails
- [ ] Tested on the actual environment, not just local

---

## Phase 4 — Reporting Results

After running tests, always report honestly:

1. How many tests were run
2. How many passed
3. How many failed
4. The exact error message for any failure
5. What you think caused the failure

### NEVER say these:
- "Tests should pass" — without running them
- "This looks correct" — as a substitute for testing
- "I tested it and it works" — without showing the actual output

### ALWAYS show:
- The actual test command that was run
- The actual output from that command
- Real pass/fail results

---

## Phase 5 — When a Test Fails

If a test fails:
1. Do not hide the failure
2. Show the user the exact error
3. Go back to `debug.md` process — find the root cause
4. Fix the root cause — do not patch the test to force it to pass

Fixing a test by changing the expected value to match wrong output is strictly forbidden.

---

## Rule Summary

- Real tests only — no fake results, no hardcoded success
- Test both success and failure cases always
- Show actual test output — never summarize without evidence
- When a test fails, debug and fix the code — not the test
- Never claim something works without proof
