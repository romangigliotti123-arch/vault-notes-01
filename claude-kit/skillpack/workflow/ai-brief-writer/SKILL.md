---
name: ai-brief-writer
description: "Write the brief an AI worker (a subagent or a headless claude session) can execute alone: goal and why, paths to read, a write fence, DONE WHEN items that each name a check, an honest exit, budget, stop rule and report format; linted with briefcheck.py. Use before launching any worker for a Roblox job."
category: workflow
tags: brief, prompt, worker, delegate, subagent, done when, scope, report format, instructions
kb: Manager/topic-brief-prompt-engineering.md, Manager/topic-report-formats-and-verification.md, Manager/topic-anthropic-agent-guidance.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md, Mentor/Combined-Brain.md, Roblox/roblox-kb/ai-and-tools.md
related: task-breaker, worker-verifier, usage-budgeter, rbx-clarify, rbx-workflow, session-handoff
---

# ai-brief-writer

`rbx-workflow` ships `templates/brief.md`; this skill is how to fill it well and prove it is well formed before spending a worker run. It writes the brief only; splitting the job is `task-breaker`, checking the answer is `worker-verifier`, choosing the model is `usage-budgeter`, and asking the user clarifying questions is `rbx-clarify`.

## When to use
Any time you delegate Roblox work to a subagent, a headless `claude -p` run or a future session. Not for: a one-line lookup you will do yourself, or prompts for Roblox's own Assistant.

## Inputs (max 2)
1. The task row (default: the next READY row of `jobs.md` / `docs/tasks.csv`). 2. Worker model and turn cap if known (default: sonnet-class, about 30 tool calls).

## Procedure
1. Pass the colleague test: a smart stranger with no chat history could do this from the brief alone. If you cannot state the goal in one sentence you do not understand the task yet; stop and read more instead of delegating the understanding.
2. Write **GOAL** (the observable end state) and one clause on why and who it is for, so the worker can calibrate depth.
3. **CONTEXT**: paths to read (not pasted), what is already known and what was ruled out. Do not hand a diagnostic worker your hypothesis as fact.
4. **OWNS**: the only paths it may write. Everything else is read-only. This is the single-writer fence.
5. **DONE WHEN**: numbered, each with the exact command or observable that proves it (`luau-check.sh <path>` ends with no errors; `lune run X.spec.luau` prints PASS). Lookups get the exact command; investigations get the question, not the steps.
6. **VERIFY YOURSELF**, **PRE-REPORT CHECK**, **BUDGET** and **STOP RULE** as in the template: one retry per failing step, then PARTIAL with the exact blocker; an honest exit: "if a check cannot run, write `untested: <why>`; do not simulate or guess".
7. **REPORT FORMAT**: the RESULT / CRITERIA / CHANGES / NOT_CHECKED / PROBLEMS block with a word cap (about 250), full details to a file.
8. Replace capitals and "NEVER" with a plain reason; if a rule is a real prohibition (publish, spend, delete) say it once, and enforce it with permissions or hooks where possible.
9. Save as `briefs/<job-id>.md` and run `python ai-brief-writer/scripts/briefcheck.py briefs/<job-id>.md`. Fix every FAIL line.

## Studio MCP path
Say in the brief whether Studio MCP tools exist and that Studio jobs are serial. Do not tell a worker to launch or focus Studio.

## Fallback
Fill the template by hand; briefcheck.py runs without any tool. Without a way to start workers, the brief doubles as the checklist you follow yourself.

## Evidence
`Manager/topic-brief-prompt-engineering.md` (the brief is the worker's entire world; dense not terse; never delegate understanding; one core objective per worker; observable done criteria plus the check; give an honest exit; replace shouting with reasons; calibrate to the worker model), `Manager/topic-report-formats-and-verification.md` (claims need evidence; mandatory not-checked field; lead with failure), `Manager/topic-anthropic-agent-guidance.md`, `Manager/topic-managing-ai-agents-for-roblox-game-dev.md`. Word-count and shout thresholds in the script are the skill's own.

## Output
`briefs/<job-id>.md` ready to send, plus the briefcheck PASS line.

## Acceptance checks
- [ ] Executed: `python ai-brief-writer/scripts/briefcheck.py --selftest` prints `selftest ok`; the real brief prints PASS.
- [ ] Every DONE WHEN item names a command or observable.
- [ ] OWNS is a concrete path list, disjoint from any parallel worker.
- [ ] The brief contains an honest-exit sentence and a stop rule.

## Pitfalls
"Based on your findings, fix it" (understanding delegated). A strict output format with no way to say "could not". Briefs that paste whole files instead of paths. Long prompts for small models, which stop early. Copying one brief across model tiers without re-testing.

## Related
`task-breaker`, `worker-verifier`, `usage-budgeter`, `rbx-clarify`, `rbx-workflow`.
