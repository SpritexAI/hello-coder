---

<p align="center">
  <img src="https://spritexai.pro.bd/brand/hello-coder.png" alt="Hello Coder" width="120" height="120" />
</p>

<h1 align="center">Hello Coder 👷</h1>

<p align="center"><strong>why use smart agent when agent act like junior developer</strong></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/SpritexAI/hello-coder?style=flat" alt="License" /></a>
  <a href="https://github.com/SpritexAI/hello-coder/stargazers"><img src="https://img.shields.io/github/stars/SpritexAI/hello-coder?style=flat&color=yellow" alt="Stars" /></a>
  <a href="https://github.com/SpritexAI/hello-coder/commits/main"><img src="https://img.shields.io/github/last-commit/SpritexAI/hello-coder?style=flat" alt="Last Commit" /></a>
</p>

<p align="center">
  <a href="#why">Why</a> •
  <a href="#what-you-get">What You Get</a> •
  <a href="#install">Install</a> •
  <a href="#profiles">Profiles</a> •
  <a href="#skills">Skills</a>
</p>

---

AI coding agents are powerful. But out of the box, they:

- Pick random colors that look AI-generated
- Fix the first bug they see without investigating
- Make decisions without asking you
- Dump 500 lines of code at once
- Run fake tests and tell you everything passed
- Start coding before understanding what you actually want

Hello Coder fixes all of that. One setup. Every agent. Every project.

---

## Before / After

🤖 Normal Agent
> "Sure! I'll build the authentication system for you."
> *proceeds to create 12 files, picks a random UI color scheme, uses a library you've never heard of, and tells you tests passed without running them*

👷 Hello Coder Agent
> "Before I start, I have a few questions:
> 1. What framework are you using?
> 2. Do you have an existing auth pattern in this project?
> 3. Should this use JWT or sessions?
> 4. Which endpoints need to be protected?
>
> Once I understand the full picture, I'll present a plan for your approval before writing anything."

**Same agent. Completely different behavior.**

---

## What You Get

| Skill | What It Fixes |
|---|---|
| `skills/planning.md` | Agent starts coding without understanding the requirement |
| `skills/ui.md` | Vibe-coded colors, wrong fonts, broken mobile layout |
| `skills/debug.md` | Fixes the first thing it sees, ignores the real cause |
| `skills/decisions.md` | Silently picks libraries, structures, and patterns for you |
| `skills/workflow.md` | Dumps everything at once with no checkpoints |
| `skills/review.md` | Hands over unreviewed code with hidden bugs |
| `skills/testing.md` | Fakes test results and calls it done |

---

## Install

### Step 1 — Install Hello Coder

One command. Finds every agent on your machine. Installs for each automatically.

```bash
# macOS / Linux / WSL
curl -fsSL https://raw.githubusercontent.com/SpritexAI/hello-coder/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/SpritexAI/hello-coder/main/install.ps1 | iex
```

~30 seconds. Detects Claude Code, Cursor, Windsurf, Gemini CLI, Codex, and Cline automatically.

---

### Step 2 — Add to Your Project

Clone Hello Coder into the root of your project:

```bash
cd your-project
git clone https://github.com/SpritexAI/hello-coder.git
```

Then create an `AGENTS.md` file in your project root with this content:

```
Read and apply hello-coder/profiles/fullstack.md before starting any task.
```

For frontend projects use `frontend.md`, for backend use `backend.md`.

This file tells your agent to automatically load Hello Coder every time it opens your project. No need to say anything manually.

---

### Step 3 — Start Working

Open your project in your agent and start giving tasks normally. Hello Coder is now active.

Your agent will automatically:
- Ask full questions before starting any feature
- Present a plan and wait for your approval
- Follow professional UI standards
- Debug systematically
- Self-review all code before presenting
- Run real tests and show real results

---

### Manual — No Script

If you prefer not to use the installer, just copy any `.md` file from `skills/` directly into your project and tell your agent to read it. No setup needed.

---

## Profiles

Profiles combine multiple skills for your role. Load one profile and all relevant skills activate automatically.

| Profile | Best For | Skills Included |
|---|---|---|
| `profiles/frontend.md` | UI, components, web apps | planning, ui, debug, review, decisions |
| `profiles/backend.md` | APIs, databases, services | planning, debug, workflow, testing, review, decisions |
| `profiles/fullstack.md` | Full projects | All 7 skills |

---

## Skills

Load individual skills if you only need specific behavior fixed.

```
hello-coder/
└── skills/
    ├── planning.md    → gather full context, present plan, wait for approval
    ├── ui.md          → professional colors, fonts, spacing, responsive design
    ├── debug.md       → list all causes, find root cause, fix systematically
    ├── decisions.md   → never assume, always ask with options and tradeoffs
    ├── workflow.md    → small steps, one at a time, checkpoint after each
    ├── review.md      → self-review before presenting, flag assumptions
    └── testing.md     → real tests only, show actual output, no faking
```

---

## Works With

Claude Code · Codex · Gemini CLI · Cursor · Windsurf · Cline · Copilot · Anti Gravity · Any agent that reads markdown files

---

## Why This Exists

At **SpritEX AI** we build AI systems and research how to make them behave better in real development workflows. While building [RexiO](https://spritexai.pro.bd) — a production AI platform — we ran into every single problem this repo solves. We wrote these rules for ourselves first. Now we are sharing them.

SpritEX AI is an AI research company focused on improving how AI systems think, plan, and build. We study agent behavior, build production AI products, and publish tools that make AI more reliable for real developers.

→ [spritexai.pro.bd](https://spritexai.pro.bd)
→ [github.com/SpritexAI](https://github.com/SpritexAI)

---

## License

MIT — free to use, free to modify, free to share.

---

*Built by SpritEX AI — because good agents deserve good rules.*
