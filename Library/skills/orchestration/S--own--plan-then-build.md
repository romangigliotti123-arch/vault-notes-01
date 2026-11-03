---
id: "plan-then-build"
type: skill
category: "orchestration"
source: "own"
license: "first-party"
repo_path: "skills/orchestration/plan-then-build/SKILL.md"
description: "Gate and procedure for big builds: use plan mode for setup and large work (skip it for simple fixes), ask clarifying questions, write a spec file, break it into small tasks each with a check, get approval, then build task by task with per-task verification and stop after failed checks. Use when starting a new project or large feature, or when the user says plan first, spec this out, plan mode, write a spec then build it, break this into tasks, or build this app."
orig_name: "plan-then-build"
orig_argument_hint: "<project idea or feature>"
tags: [lib/skill, cat/orchestration, src/own]
---

# plan-then-build

> Gate and procedure for big builds: use plan mode for setup and large work (skip it for simple fixes), ask clarifying questions, write a spec file, break it into small tasks each with a check, get approval, then build task by task with per-task verification and stop after failed checks. Use when starting a new project or large feature, or when the user says plan first, spec this out, plan mode, write a spec then build it, break this into tasks, or build this app.

Type: skill | Category: [[categories/cat-orchestration|orchestration]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/orchestration/plan-then-build/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--phased-build-orchestrator]], [[S--own--clarify-before-build]]

Creator videos (notes are in the AI Library Vault, Creators/videos): 2026-01-16-build-anything-with-claude-code-n8n-beginner-s-guide, 2026-04-12-this-one-plugin-just-10x-d-claude-code, 2026-10-02-how-to-actually-build-sell-software-with-ai-as-a-non-techie, 2026-10-11-i-tried-100-github-repos-for-claude-these-6-are-the-best

---
# plan-then-build

## Gate: plan or just do it?
Plan when: new project or setup, more than ~3 files, unclear requirements, anything hard to undo. Do NOT plan for: typo, rename, one-file fix, a clear bug with a known cause. Say which you chose in one line.

## Steps
1. **Plan mode**: read-only exploration of the repo; no edits.
2. **Clarify**: run clarify-before-build (3-7 questions with defaults).
3. **Spec**: write `SPEC.md`: goal, users, scope in/out, requirements as testable statements, stack choices with reasons, risks.
4. **Tasks**: `TASKS.md`, each task small (under ~1 hour or one commit), with id, goal, files, acceptance check (command or observable), dependencies. Order so each task leaves the project runnable.
5. **Approval gate**: show spec and task list; wait for yes. Changes loop back to step 3.
6. **Build**: leave plan mode (auto-accept edits is fine now). For each task in order: implement, run its check, record result in TASKS.md (`done` with evidence or `blocked`). Commit per task if in git.
7. **Stop rule**: if a check fails twice, stop and report instead of piling on changes; update the spec if the plan was wrong.
8. **Finish**: run the full test/build, list unfinished tasks, summarise what to verify by hand.

## Checks
Spec items map to tasks; every task has a check that can fail; TASKS.md reflects reality.

## Failure modes
- Over-planning small work.
- Plans that drift from code: update SPEC.md when a decision changes.
- Giant tasks that hide failures: split them.

## Related
clarify-before-build, spec-test-review-workflow (tests-first and two-stage review), phased-build-orchestrator (parallel workers), the library's planner/requirements skills.

## Sources
Idea from AI-creator research (catalogue ideas idea-0037). Credit and where it appears:
- Nate Herk, "Build ANYTHING with Claude Code & n8n (Beginner's Guide)" (2026-01-16) @ 7:50-22:26, https://www.youtube.com/watch?v=OCO3aq3G0mk&t=470s. Seen there as: Plan-mode-first pattern
- Nate Herk, "This One Plugin Just 10x’d Claude Code" (2026-04-12) @ 3:25, https://www.youtube.com/watch?v=4XqVR6xI6Kw&t=205s. Seen there as: Executing plans skill
- Nate Herk, "How to Actually Build & Sell Software with AI as a Non-Techie" (2026-10-02) @ 21:06, https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=1266s. Seen there as: Spec-driven development planning (legacy pattern)
- Nate Herk, "I Tried 100+ Github Repos for Claude. These 6 Are the Best" (2026-10-11) @ 4:57, https://www.youtube.com/watch?v=HhZdNYI4pJs&t=297s. Seen there as: Agent Skills (/spec, /plan, /build)
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.
