---
name: tech-debt-lister
description: "List a Roblox project's technical debt with impact, risk and fix hours, rank it by pain per hour with debt.py, and decide what to fix now, next, later or accept. Use before a milestone, after a rushed prototype, or when the code feels slow to change."
category: workflow
tags: tech debt, refactor, cleanup, rank, risk, maintenance, backlog, code health
kb: Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/common-mistakes.md, Manager/topic-multi-agent-failure-modes.md, Mentor/Combined-Brain.md
related: code-style-guide-writer, rbx-luau, game-optimizer, script-profiler, scope-creep-guard, sprint-planner, post-mortem-writer
---

# tech-debt-lister

Turns "the code is a mess" into a ranked list with hours. Bug lists are `output-error-triager` and `bug-intake-builder`; performance hunting is `lag-hunter` / `script-profiler`; style rules are `code-style-guide-writer`. This one covers structural debt: duplicated remotes, missing data migrations, god scripts, untested pure logic, hard-coded ids.

## When to use
A milestone is ending, a prototype is becoming the real game, or a change that should take an hour takes a day. Not for: a single known bug, or optimisation without a measured problem.

## Inputs (max 2)
1. The project folder (default: current). 2. Hours available for debt this sprint (default: 20% of a sprint's capacity).

## Procedure
1. Gather evidence, do not guess: `luau-check.sh src` output (warnings count), `git log --since="30 days" --name-only --pretty=format: | sort | uniq -c | sort -rn | head` for hot files, line counts of the largest scripts, a grep for `wait(` / `spawn(` / `loadstring` / hard-coded numeric ids. Quote the numbers in the list.
2. Write one row per debt item: `item,impact,risk,fix_h,blocks`. Impact (1-5) = how often it slows or breaks work; risk (1-5) = chance and cost of data loss, exploit or player-visible failure; fix_h includes writing a test; blocks = the milestone it blocks, if any.
3. Run `python tech-debt-lister/scripts/debt.py debt.csv --budget-h 4`. Read NOW / NEXT / LATER / ACCEPT and the budget column.
4. Challenge the top three as a sceptic: is each real (evidence line) or taste? Remove taste items; mark them ACCEPT.
5. For each NOW item write the acceptance check that proves it fixed (a Lune test, a `luau-check.sh` clean run, a grep returning zero).
6. Hand the NOW items to `task-breaker`; record accepted debt in `docs/decisions.md` via `decision-log-writer` so it is a choice, not a surprise.
7. Save `docs/debt.md` (headings Item, Fix, Rank; under 100 lines) and check it.

## Studio MCP path
Optional: `script_search` / `script_grep` for banned patterns across the place, and `get_console_output` for repeating warnings; each result is quoted, not summarised.

## Fallback
Rojo project files plus shell commands (`grep`, `git log`); anything needing the live place is `untested`.

## Evidence
`Roblox/roblox-kb/code-architecture-and-frameworks.md` (module structure and frameworks as the main debt sources), `Roblox/roblox-kb/development-process-and-speed.md` (do not over-engineer one-time content; ship the MVP before perfecting), `Roblox/roblox-kb/common-mistakes.md`, `Manager/topic-multi-agent-failure-modes.md` (AI-written code drifts when specs are loose; add structural checks). The scoring formula is this skill's own, a ranking aid and not a measurement.

## Output
`docs/debt.md` with the ranked table, the debt.py output, and the NOW list with acceptance checks.

## Acceptance checks
- [ ] Executed: `python tech-debt-lister/scripts/debt.py --selftest` prints `selftest ok`; the project run lists every item with a verdict.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/debt.md --kind debt` prints PASS.
- [ ] Each of the top three has a cited command output or file path as evidence.
- [ ] NOW total hours fit the stated budget, or the overflow is named.

## Pitfalls
Listing every style nit (it buries the data-loss risk). Scoring fix_h without test time. A refactor sprint with no feature progress; keep debt to a fixed share of each sprint. Fixing debt in a file a worker is editing right now (ownership clash).

## Related
`code-style-guide-writer`, `rbx-luau`, `script-profiler`, `scope-creep-guard`, `sprint-planner`, `post-mortem-writer`.
