---
name: task-breaker
description: "Break a goal or milestone into small verifiable tasks an AI worker can finish alone: each with owned files, a dependency list, a check that proves it and an hours estimate, then group them into parallel waves with tasks.py. Use when a plan item is bigger than about four hours or before writing several worker briefs."
category: workflow
tags: tasks, breakdown, decompose, waves, dependencies, ownership, verify, parallel, ledger
kb: Roblox/roblox-kb/development-process-and-speed.md, Manager/topic-orchestration-patterns.md, Manager/topic-multi-agent-failure-modes.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md, Mentor/Combined-Brain.md
related: project-kickoff, ai-brief-writer, worker-verifier, sprint-planner, scope-creep-guard, usage-budgeter, game-dev-workflow
---

# task-breaker

The head manager in `game-dev-workflow` keeps a job ledger (`jobs.md`, template `templates/jobs.md`). This skill produces the rows that go into it: the decomposition itself. It does not write the briefs (`ai-brief-writer`), choose models (`usage-budgeter`) or fit tasks into a week (`sprint-planner`).

## When to use
A milestone or feature has no task list, or a task is over four hours, or two planned tasks might edit the same file. Not for: design questions (`mvp-definer`), triage of existing bugs (`output-error-triager` and `bug-intake-builder`).

## Inputs (max 2)
1. The goal or milestone with its acceptance test (default: the next unfinished milestone in `docs/kickoff.md`). 2. Max task size in hours (default 4).

## Procedure
1. Restate the acceptance test; every task must move toward it. Stop if the test is vague and ask for one pass/fail sentence.
2. Split by file ownership and system (data, shop, UI, map), not by role titles. One task, one owner folder or file set. Shared modules (a `Remotes` module, the data module) belong to exactly one task.
3. For each task fill `id,title,deps,owns,verify,est_h` in `tasks.csv`. The `verify` is a command or observable ("`lune run ShopRate.spec.luau` prints PASS", "Output has no red lines in a 3-minute playtest"), never "works".
4. Add the tests as their own early tasks when pure logic is involved (a Lune suite for the logic, then the wiring).
5. Run `python task-breaker/scripts/tasks.py tasks.csv`. Fix every ERROR: split tasks over the cap, give vague verifies a command, serialise tasks that own the same path, break cycles.
6. Read the waves. A wave of independent tasks is the maximum parallelism, not the plan: the default is one worker at a time (small caps beat wide fan-out), parallel only for disjoint owns.
7. Mark Studio-touching tasks `serial` (one shared Studio session) in the ledger. Copy the rows into `jobs.md`; save `docs/tasks.csv`.

## Studio MCP path
None to split. For tasks that need a place, note `get_studio_state` as the first step of the task and mark it serial.

## Fallback
Spreadsheet or Markdown table with the same six columns; the script reads CSV only, so export first.

## Evidence
`Manager/topic-orchestration-patterns.md` (read-parallel is safe, write-parallel is not; keep one writer per artifact; a task ledger beats memory), `Manager/topic-multi-agent-failure-modes.md` (failures are mostly specification and verification; parallel writers conflict), `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (decompose by file ownership; one shared Remotes module is one job), `Roblox/roblox-kb/development-process-and-speed.md` (plan the full loop including edge cases before building).

## Output
`docs/tasks.csv` plus the script's wave listing and critical path (hours), and the rows added to `jobs.md`.

## Acceptance checks
- [ ] Executed: `python task-breaker/scripts/tasks.py --selftest` prints `selftest ok`, and the project run ends `PASS`.
- [ ] No task over the size cap, none without a verify command, none without owns.
- [ ] No two tasks in one wave own overlapping paths (script enforces).
- [ ] Every task traces to the milestone's acceptance test.

## Pitfalls
Tasks named by activity ("work on shop") with no end state. A "polish" task with no check. Hiding a shared file inside two tasks. Treating wave width as a target for how many workers to launch (cost grows about 15x with fan-out per the Manager KB).

## Related
`project-kickoff`, `ai-brief-writer`, `worker-verifier`, `sprint-planner`, `usage-budgeter`, `scope-creep-guard`.
