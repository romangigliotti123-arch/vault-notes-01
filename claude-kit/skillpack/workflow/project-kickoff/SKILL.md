---
name: project-kickoff
description: "Start a Roblox project with the day-one files an AI worker and a human both need: goal, scope fence, toolchain check, milestones with acceptance tests and the first three tasks, written to docs/kickoff.md. Use right after /game-dev-workflow has a plan (or when a folder has code but no written plan) and before the first build job."
category: workflow
tags: kickoff, start, setup, project, rojo, milestones, first tasks, scope, repo
kb: Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/mindset-and-strategy.md, Mentor/Combined-Brain.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md, Manager/topic-long-running-always-on-agents.md
related: game-dev-workflow, roblox-rojo-project-setup, mvp-definer, task-breaker, folder-structure-planner, dependency-pinner, git-workflow-setter, session-handoff
---

# project-kickoff

`game-dev-workflow` decides WHAT to build and keeps the stage state in `Games/<slug>/`. This skill writes the small, checkable project record that lives in the repo itself so any later session (or a worker that sees only the repo) starts from files, not chat. It does not scaffold folders (`roblox-rojo-project-setup`, `folder-structure-planner`), define the playable minimum (`mvp-definer`) or split tasks (`task-breaker`); it ties their outputs together.

## When to use
A project folder is about to get its first worker brief, or exists without a written goal, scope and milestones. Not for: an idea still being rated (stay in `game-dev-workflow`), a mid-project pause (`session-handoff`).

## Inputs (max 2)
1. The project folder (default: the current directory; the plan is `game-plan.md` or `docs/GDD.md` if present). 2. Time box in working days (default 14 for a first playable, 6 productive hours per day).

## Procedure
1. Read the plan files that exist (`game-plan.md`, `docs/GDD.md`, `docs/idea.md`). If none exist, stop and send the user to `/game-dev-workflow`; do not invent a design here.
2. Write the **Goal** as one sentence naming the one core loop and the player, and the **Scope** as three lists: in (the MVP set), out (deferred), frozen-until (the playtest that unlocks more). Stop condition: the in-list fits the time box at 2x solo estimates (`sprint-planner` has the factor).
3. Record the **Toolchain** with real output: `rojo --version`, `stylua --version`, `selene --version`, `lune --version` (a missing tool is written as `missing`, never assumed), whether `default.project.json` exists, whether `mcp__Roblox_Studio__` tools are listed (mode 1/2/3 of `roblox-studio-connect`).
4. Write 3-5 **Milestones**, each with one pass/fail acceptance test a stranger can run ("a new player can buy item 1 within 90 seconds on mobile"). Milestone 1 is always "the loop runs with no errors".
5. List the **First tasks** (three at most), each with a verify command; hand the full split to `task-breaker`.
6. Add the rules every worker inherits: file ownership by folder, ids are `0` until set in Creator Hub, nothing is published or spent by a worker.
7. Save `docs/kickoff.md` (under 90 lines) and run the check below. Append one line to `docs/PROGRESS.md` (create it if missing) with the date and "kickoff written".

## Studio MCP path
Optional evidence only: `list_roblox_studios` then `get_studio_state` to record which place is open; do not write the kickoff through MCP.

## Fallback
Pure Markdown plus the toolchain commands run in a shell. Anything needing Studio (mode check) is written `untested`.

## Evidence
`Roblox/roblox-kb/development-process-and-speed.md` (barebones MVP around one loop; plan the full player loop before building; solo takes about twice as long), `Roblox/roblox-kb/version-control-and-tooling.md` (pin tools, keep the place binary out of git), `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (repo is the memory: plan, ledger, progress file; workers see only the brief and the repo), `Manager/topic-long-running-always-on-agents.md` (state lives in files, not in one chat), `Mentor/Combined-Brain.md` job "running a game project".

## Output
`docs/kickoff.md` with headings Goal, Scope, Toolchain, Milestones, First tasks; one `docs/PROGRESS.md` line.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py --selftest` prints `selftest ok`; `python project-kickoff/scripts/wfdoc.py docs/kickoff.md --kind kickoff` prints PASS.
- [ ] Every milestone has a pass/fail test, not an adjective.
- [ ] Toolchain lines are pasted tool output or the word `missing`.
- [ ] Scope in-list total is within the time box.

## Pitfalls
Writing milestones as feature lists ("add shop") instead of tests. Copying the GDD wholesale (the kickoff points to it). Declaring a tool present because the template lists it. Skipping the frozen-until rule, which is what stops scope creep later (`scope-creep-guard`).

## Related
`game-dev-workflow`, `roblox-rojo-project-setup`, `mvp-definer`, `task-breaker`, `folder-structure-planner`, `session-handoff`.
