---
name: playtest-evidence-logger
description: "Record a playtest or test run in one standard evidence format: build, mode (Studio MCP, Rojo static, or hand), the exact result lines from Output, what was and was not exercised, and a verdict. Use after every playtest so milestone reviews, critics and handoffs can rely on files instead of memory."
category: workflow
tags: playtest, evidence, log, output, console, test run, record, result, mode
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/playtesting-and-feedback.md, Manager/topic-report-formats-and-verification.md, Manager/topic-observability.md, Roblox/roblox-kb/development-process-and-speed.md, Mentor/Combined-Brain.md
related: game-dev-playtest, milestone-reviewer, worker-verifier, studio-mcp-session-planner, regression-checklist-builder, bug-report-template, roblox-playtest-checklist
---

# playtest-evidence-logger

`game-dev-playtest` runs the playtest and writes `docs/PLAYTEST.md`; `roblox-playtest-checklist` lists what to test; `bug-report-template` records a single bug. This skill defines the evidence record that `game-dev-workflow` stage detection and `milestone-reviewer` read: `Games/<slug>/playtests/<date>.md`. It adds no testing of its own.

## When to use
Right after any playtest, static check run or human test session. Not for: deciding what to test, or logging individual bugs.

## Inputs (max 2)
1. The run you just did (or the human tester's notes). 2. The build id (git short hash, or `unknown` if there is no git).

## Procedure
1. Name the **Build**: `git rev-parse --short HEAD` output, the place version if known, device and platform (PC, phone, tablet; `unknown` if not stated).
2. Name the **Mode**, one of: `studio-mcp` (a real run read through the tools), `static` (`luau-check.sh` and `rojo build` only: "checked, not run"), `human` (a person played; give their experience level), `code-walk` (read only). Say what the mode cannot show.
3. Record **Result** lines exactly: for a Studio run, the Output lines from `get_console_output` quoted verbatim with the first error first; the run length (about 3 minutes is the usual bar); whether the loop was completed. For a human test, silent-watch notes (where they stalled) before their spoken feedback.
4. Record **Evidence**: the commands and output excerpts, screenshots by path, and what was NOT exercised (mobile touch, purchases, multi-player). Anything not exercised is `untested`.
5. Give the **Verdict**: `clean` (no errors, loop completed), `issues` (list with severity), or `blocked` (could not run, with the reason). Never write `clean` for a static run; write `static-clean`.
6. Link new bugs to `bug-report-template` entries and the next action to the ledger.
7. Save `Games/<slug>/playtests/YYYY-MM-DD.md` (or `docs/playtests/` outside the games folder), under 80 lines, and check it; one file per run, never overwrite.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `start_stop_play` (let it run) -> `get_console_output` (quote) -> stop -> optionally `screen_capture`. Record `Studio MCP: yes`.

## Fallback
Static mode: `luau-check.sh src` and `rojo build -o build.rbxl` output lines, labelled `static`. A human tester's notes pasted as given.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`, `Roblox/roblox-kb/playtesting-and-feedback.md` (watch new players silently; test on mobile; playtest early), `Manager/topic-report-formats-and-verification.md` (report what actually happened; untested is a value; evidence from this session), `Manager/topic-observability.md`, `Roblox/roblox-kb/development-process-and-speed.md`. The stage rule that a playtest report enables the playtest stage lives in `game-dev-workflow` `references/stages.md`.

## Output
One dated evidence file with headings Build, Mode, Result, Evidence.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py Games/<slug>/playtests/<date>.md --kind playtestlog` prints PASS (evidence marks required).
- [ ] Result lines are verbatim output, not paraphrase.
- [ ] The mode is stated and its limits named.
- [ ] Not-exercised areas are listed as `untested`.

## Pitfalls
Calling a lint pass a playtest. Paraphrasing an error. One shared log file that hides when each run happened. Logging only successes.

## Related
`game-dev-playtest`, `milestone-reviewer`, `worker-verifier`, `studio-mcp-session-planner`, `bug-report-template`, `roblox-playtest-checklist`.
