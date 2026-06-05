# Evals

These tests verify that each Hello Coder skill produces the correct agent behavior.

---

## Difference from Benchmarks

- `benchmarks/` — measures how much better the agent performs with Hello Coder (score)
- `evals/` — verifies each skill is working correctly (pass/fail)

---

## Requirements

- Python 3.8+
- An Anthropic API key

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_api_key_here
```

---

## Run All Evals

```bash
python evals/run.py
```

## Run a Single Skill Eval

```bash
python evals/run.py --skill planning
python evals/run.py --skill ui
python evals/run.py --skill debug
python evals/run.py --skill decisions
python evals/run.py --skill workflow
python evals/run.py --skill review
python evals/run.py --skill testing
```

---

## Sample Output

```
👷 Hello Coder — Skill Evals
===============================================

planning.md
  ✓ asks clarifying questions before coding
  ✓ presents a plan before starting
  ✓ waits for user approval before writing code

ui.md
  ✓ avoids hardcoded px values in layout
  ✓ uses professional color palette
  ✓ builds responsive for mobile and desktop

debug.md
  ✓ lists multiple possible causes
  ✓ does not fix the first thing it sees
  ✓ verifies fix after applying

decisions.md
  ✓ asks before choosing a library
  ✓ provides options with tradeoffs
  ✓ does not silently assume

workflow.md
  ✓ breaks task into small steps
  ✓ shows progress after each step
  ✓ stops and re-plans when complexity grows

review.md
  ✓ self-reviews before presenting code
  ✓ flags assumptions to the user
  ✓ checks for hardcoded values

testing.md
  ✓ does not fake test results
  ✓ shows actual test output
  ✓ tests both success and failure cases

===============================================
21/21 evals passing
```
