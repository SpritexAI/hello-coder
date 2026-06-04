# Benchmarks

These scripts measure the difference in agent behavior with and without Hello Coder skills.

---

## What This Measures

- How many clarifying questions the agent asks before starting
- Whether the agent presents a plan before coding
- Whether the agent makes silent assumptions
- Whether the agent self-reviews before presenting code

---

## Requirements

- Python 3.8+
- An Anthropic API key

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_api_key_here
```

---

## Run

```bash
python benchmarks/benchmark.py
```

---

## How It Works

Each test sends the same prompt to Claude twice:

1. **Without Hello Coder** — raw prompt, no skills loaded
2. **With Hello Coder** — prompt with planning.md and decisions.md loaded

The script then compares:
- Did the agent ask clarifying questions?
- Did the agent present a plan before coding?
- Did the agent make silent assumptions?
- Did the agent self-review?

---

## Sample Output

```
Running benchmark: "Add a login page to my app"

WITHOUT Hello Coder:
  ✗ Asked clarifying questions   — NO
  ✗ Presented plan first         — NO
  ✗ Avoided silent assumptions   — NO
  ✗ Self-reviewed code           — NO
  Score: 0/4

WITH Hello Coder:
  ✓ Asked clarifying questions   — YES
  ✓ Presented plan first         — YES
  ✓ Avoided silent assumptions   — YES
  ✓ Self-reviewed code           — YES
  Score: 4/4

Improvement: +4 behaviors corrected
```
