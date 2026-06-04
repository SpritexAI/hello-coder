import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

PLANNING_SKILL = open(os.path.join(os.path.dirname(__file__), "../skills/planning.md")).read()
DECISIONS_SKILL = open(os.path.join(os.path.dirname(__file__), "../skills/decisions.md")).read()
REVIEW_SKILL = open(os.path.join(os.path.dirname(__file__), "../skills/review.md")).read()

HELLO_CODER_CONTEXT = f"""
You are an AI coding agent. Before starting any task, follow these skills exactly:

{PLANNING_SKILL}

{DECISIONS_SKILL}

{REVIEW_SKILL}
"""

TEST_PROMPTS = [
    "Add a login page to my app",
    "Build a notification system",
    "Fix the bug in my payment service",
    "Create a pricing card component",
    "Write tests for the user service",
]

BEHAVIOR_CHECKS = [
    ("Asked clarifying questions", ["question", "before i start", "can you clarify", "i have a few", "could you tell me", "what framework", "which"]),
    ("Presented plan first", ["plan:", "step 1", "step 2", "here is my plan", "before i write", "do you approve"]),
    ("Avoided silent assumptions", ["i was about to assume", "i am assuming", "is that correct", "before i assume", "want to confirm"]),
    ("Self-reviewed code", ["self-review", "reviewed", "i have checked", "before presenting", "verified"]),
]

def check_behaviors(response_text):
    results = []
    for label, keywords in BEHAVIOR_CHECKS:
        found = any(kw.lower() in response_text.lower() for kw in keywords)
        results.append((label, found))
    return results

def run_test(prompt, use_hello_coder):
    system = HELLO_CODER_CONTEXT if use_hello_coder else "You are an AI coding agent. Help the user with their request."
    message = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def print_results(label, behaviors):
    print(f"\n  {label}:")
    score = 0
    for name, passed in behaviors:
        icon = "✓" if passed else "✗"
        status = "YES" if passed else "NO"
        print(f"    {icon} {name:<35} — {status}")
        if passed:
            score += 1
    print(f"    Score: {score}/{len(behaviors)}")
    return score

def main():
    print("\n👷 Hello Coder — Benchmark\n")
    print("=" * 55)

    total_without = 0
    total_with = 0

    for prompt in TEST_PROMPTS:
        print(f'\nPrompt: "{prompt}"')
        print("-" * 55)

        response_without = run_test(prompt, use_hello_coder=False)
        behaviors_without = check_behaviors(response_without)
        score_without = print_results("WITHOUT Hello Coder", behaviors_without)

        response_with = run_test(prompt, use_hello_coder=True)
        behaviors_with = check_behaviors(response_with)
        score_with = print_results("WITH Hello Coder", behaviors_with)

        improvement = score_with - score_without
        print(f"\n    Improvement: +{improvement} behaviors corrected")

        total_without += score_without
        total_with += score_with

    print("\n" + "=" * 55)
    print(f"\n👷 Final Results across {len(TEST_PROMPTS)} prompts:")
    print(f"   Without Hello Coder: {total_without}/{len(TEST_PROMPTS) * len(BEHAVIOR_CHECKS)}")
    print(f"   With Hello Coder:    {total_with}/{len(TEST_PROMPTS) * len(BEHAVIOR_CHECKS)}")
    print(f"   Total improvement:   +{total_with - total_without} behaviors corrected\n")

if __name__ == "__main__":
    main()
