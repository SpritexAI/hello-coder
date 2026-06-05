import anthropic
import os
import argparse

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SKILLS_DIR = os.path.join(os.path.dirname(__file__), "../skills")

def load_skill(name):
    path = os.path.join(SKILLS_DIR, f"{name}.md")
    with open(path) as f:
        return f.read()

EVALS = {
    "planning": [
        {
            "name": "asks clarifying questions before coding",
            "prompt": "Build me a user authentication system",
            "keywords": ["question", "before i start", "i have a few", "could you tell me", "what framework", "which database", "clarify"],
        },
        {
            "name": "presents a plan before starting",
            "prompt": "Add a payment page to my app",
            "keywords": ["plan:", "step 1", "here is my plan", "before i write", "proposed plan"],
        },
        {
            "name": "waits for user approval before writing code",
            "prompt": "Create a REST API for my blog",
            "keywords": ["do you approve", "shall i proceed", "before i start coding", "confirm", "your approval"],
        },
    ],
    "ui": [
        {
            "name": "avoids hardcoded px values in layout",
            "prompt": "Build me a pricing card component",
            "keywords": ["rem", "clamp", "em", "vw", "vh", "relative", "responsive units", "css variable"],
        },
        {
            "name": "uses professional color palette",
            "prompt": "Design a landing page hero section",
            "keywords": ["#111", "#0f0f0f", "#3b82f6", "#6366f1", "neutral", "contrast", "professional", "inter"],
        },
        {
            "name": "builds responsive for mobile and desktop",
            "prompt": "Create a navigation bar component",
            "keywords": ["mobile", "responsive", "breakpoint", "375px", "desktop", "media query", "both"],
        },
    ],
    "debug": [
        {
            "name": "lists multiple possible causes",
            "prompt": "My login button is not working",
            "keywords": ["possible cause", "could be", "another possibility", "might also", "several reasons", "cause 1", "cause 2"],
        },
        {
            "name": "does not fix the first thing it sees",
            "prompt": "The form is not submitting on my app",
            "keywords": ["investigate", "before fixing", "possible causes", "root cause", "let me check", "first let me"],
        },
        {
            "name": "verifies fix after applying",
            "prompt": "Fix the null pointer error in my code",
            "keywords": ["verify", "confirm", "check if", "make sure", "after the fix", "this solves"],
        },
    ],
    "decisions": [
        {
            "name": "asks before choosing a library",
            "prompt": "Add form validation to my React app",
            "keywords": ["which library", "do you prefer", "option 1", "option 2", "would you like", "i see two", "before i choose"],
        },
        {
            "name": "provides options with tradeoffs",
            "prompt": "I need to store user sessions",
            "keywords": ["tradeoff", "option 1", "option 2", "pros", "cons", "faster", "slower", "persistent", "which do you prefer"],
        },
        {
            "name": "does not silently assume",
            "prompt": "Add a database to my project",
            "keywords": ["before i assume", "i want to confirm", "which database", "do you already have", "what are you using"],
        },
    ],
    "workflow": [
        {
            "name": "breaks task into small steps",
            "prompt": "Build a complete e-commerce checkout flow",
            "keywords": ["step 1", "step 2", "step 3", "first", "then", "after that", "break", "small steps"],
        },
        {
            "name": "shows progress after each step",
            "prompt": "Create a full user profile system",
            "keywords": ["step 1 complete", "ready to move", "before continuing", "checkpoint", "done with", "next step"],
        },
        {
            "name": "stops and re-plans when complexity grows",
            "prompt": "Add real-time notifications to my app",
            "keywords": ["more complex", "re-plan", "revised plan", "stop", "update the plan", "new complexity", "discovered"],
        },
    ],
    "review": [
        {
            "name": "self-reviews before presenting code",
            "prompt": "Write a function to handle file uploads",
            "keywords": ["reviewed", "self-review", "checked", "i have verified", "before presenting", "i went through"],
        },
        {
            "name": "flags assumptions to the user",
            "prompt": "Create an API endpoint for user registration",
            "keywords": ["assumption", "i assumed", "assuming", "please note", "i used", "you may want to check"],
        },
        {
            "name": "checks for hardcoded values",
            "prompt": "Build a function that sends emails",
            "keywords": ["environment variable", "env", "config", "no hardcoded", "hardcoded", "secret", "api key"],
        },
    ],
    "testing": [
        {
            "name": "does not fake test results",
            "prompt": "Write tests for my payment service",
            "keywords": ["real", "actual output", "run the test", "not mock", "genuine", "real behavior", "integration"],
        },
        {
            "name": "shows actual test output",
            "prompt": "Test my user authentication module",
            "keywords": ["output:", "result:", "passing", "failing", "✓", "✗", "test output", "ran"],
        },
        {
            "name": "tests both success and failure cases",
            "prompt": "Write tests for the login endpoint",
            "keywords": ["failure case", "error case", "edge case", "invalid", "wrong password", "missing", "both"],
        },
    ],
}

def run_eval(skill_name, eval_case):
    skill_content = load_skill(skill_name)
    system = f"""You are an AI coding agent. Follow these rules exactly:\n\n{skill_content}"""
    message = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": eval_case["prompt"]}]
    )
    response = message.content[0].text.lower()
    passed = any(kw.lower() in response for kw in eval_case["keywords"])
    return passed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", type=str, default=None, help="Run evals for a specific skill only")
    args = parser.parse_args()

    print("\n👷 Hello Coder — Skill Evals")
    print("=" * 47)

    skills_to_run = [args.skill] if args.skill else list(EVALS.keys())
    total = 0
    passed_total = 0

    for skill_name in skills_to_run:
        if skill_name not in EVALS:
            print(f"\n✗ Unknown skill: {skill_name}")
            continue

        print(f"\n{skill_name}.md")
        cases = EVALS[skill_name]

        for case in cases:
            passed = run_eval(skill_name, case)
            icon = "✓" if passed else "✗"
            print(f"  {icon} {case['name']}")
            total += 1
            if passed:
                passed_total += 1

    print("\n" + "=" * 47)
    print(f"{passed_total}/{total} evals passing\n")

if __name__ == "__main__":
    main()
