---
name: milestone-reviewer
description: "Review a project milestone against its pass/fail acceptance tests: a table of criterion, result and evidence, a PASS, HOLD or FAIL verdict from milestone.py, and the gaps to close before the next milestone starts. Use at the end of each milestone, before unfreezing scope, or before the critic gate in rbx-workflow."
category: workflow
tags: milestone, review, acceptance, gate, verdict, evidence, sign-off, progress
kb: Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/playtesting-and-feedback.md, Manager/topic-report-formats-and-verification.md, Manager/topic-llm-judge-and-adversarial-verification.md, Mentor/Combined-Brain.md
related: project-kickoff, worker-verifier, playtest-evidence-logger, scope-creep-guard, rbx-critic, sprint-planner, mvp-definer
---

# milestone-reviewer

`rbx-workflow` advances stages only after an independent critic says GOOD (`rbx-critic`). This skill is the project-level, evidence-table review that feeds that gate and every smaller milestone in between. It decides nothing about game quality; it decides whether the stated tests were actually run and passed.

## When to use
A milestone from `docs/kickoff.md` is declared done, before work on the next one starts, or before unfreezing scope. Not for: judging fun or design (`rbx-critic`), checking one worker report (`worker-verifier`).

## Inputs (max 2)
1. The milestone and its acceptance tests (default: the first unfinished milestone in `docs/kickoff.md`). 2. The evidence folder (default: `reports/`, `Games/<slug>/playtests/`, `docs/PLAYTEST.md`).

## Procedure
1. Copy each acceptance test verbatim into a table with columns `criterion | result | evidence`. Do not rephrase the test to match what was built.
2. For each row decide `met`, `unmet` or `untested`, with evidence: a command and its output excerpt, a playtest file path with date, or a hash. `Untested` means the test could not be run here (no Studio, no mobile device); say what is needed.
3. Re-run at least one check per load-bearing row yourself (`luau-check.sh`, `lune run`, `rojo build`, the playtest if Studio MCP exists) instead of copying the worker's line; use `worker-verifier` for the reports behind the rows.
4. Run `python milestone-reviewer/scripts/milestone.py docs/milestone-<n>.md`. PASS needs every row met with real evidence; HOLD means untested rows remain; FAIL means an unmet row or a met row without evidence.
5. List the **Gaps** from the script and assign each to a task (`task-breaker`) with a verify; or accept an `untested` row in writing with the owner's name, which stays visible in the next review.
6. If PASS: append to `docs/PROGRESS.md`, tell `rbx-workflow` the stage evidence is ready for the critic, and release the scope freeze only if the rule says so (`scope-creep-guard`). If not PASS: do not start the next milestone's build tasks.
7. Save `docs/milestone-<n>.md` (headings Criteria, Verdict, Gaps; under 80 lines; evidence marks required) and check it.

## Studio MCP path
`list_roblox_studios`, `start_stop_play`, `get_console_output` for the "runs with no errors" rows; quote the Output lines. Serial use only.

## Fallback
Static checks (`luau-check.sh`, `rojo build`) give "checked, not run" evidence; Studio-run rows stay `untested`.

## Evidence
`Roblox/roblox-kb/development-process-and-speed.md` (barebones MVP first; plan the full player loop including edge cases), `Roblox/roblox-kb/playtesting-and-feedback.md` (playtest early with a rough build; watch new players), `Manager/topic-report-formats-and-verification.md` (every done line carries evidence; untested is a first-class value), `Manager/topic-llm-judge-and-adversarial-verification.md` (verify state, binary criteria, scope the review to correctness gaps and allow "no issues found").

## Output
`docs/milestone-<n>.md` with the table, verdict line and gap list.

## Acceptance checks
- [ ] Executed: `python milestone-reviewer/scripts/milestone.py --selftest` prints `selftest ok`; the project file run prints a VERDICT.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/milestone-<n>.md --kind milestone` prints PASS.
- [ ] At least one row's evidence command was re-run by the reviewer this session.
- [ ] No criterion text was rewritten from the kickoff.

## Pitfalls
Rewording tests after the fact. Counting a lint pass as a playtest. Treating HOLD as a pass because the date is close. Letting the builder review its own milestone without re-running anything.

## Related
`project-kickoff`, `worker-verifier`, `playtest-evidence-logger`, `scope-creep-guard`, `rbx-critic`, `mvp-definer`.
