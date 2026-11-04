---
name: studio-mcp-session-planner
description: "Plan a Roblox Studio MCP working session before touching the place: which studio, which mode (MCP, Rojo files or hand code), the serial order of calls, checkpoints with rollback, and what stays untested. Use before any worker or session edits a live Studio place through MCP tools."
category: workflow
tags: studio, mcp, session, plan, checkpoint, rollback, serial, place, connection
kb: Roblox/roblox-kb/ai-and-tools.md, Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md, Manager/topic-tool-and-mcp-design.md, Mentor/Combined-Brain.md
related: rbx-studio, rbx-rojo, git-workflow-setter, playtest-evidence-logger, task-breaker, release-checklist-builder, worker-verifier
---

# studio-mcp-session-planner

`rbx-studio` explains the three modes and the tool names; this skill is the pre-flight plan for one session so a worker with write access to a real place cannot lose work or fight Rojo. It writes a plan and does not start Studio (never launch or focus GUI apps).

## When to use
A session or worker will change scripts or instances in an open place, run playtests, or read the console through `mcp__Roblox_Studio__` tools. Not for: pure file work in a Rojo project with no Studio open.

## Inputs (max 2)
1. The goal of the session in one sentence. 2. The place (default: whichever `list_roblox_studios` returns; if two are open, the user picks).

## Procedure
1. **Connection**: check that tools named `mcp__Roblox_Studio__` exist in your tool list. If absent, say "Studio MCP not connected" and plan mode 2 (Rojo files) or 3 (hand code) instead; the session plan is then a file plan with `untested` Studio steps.
2. If present: `list_roblox_studios`, then `get_studio_state`; confirm the place name matches the game. Record the studio id for every later call.
3. **Who owns what**: if a Rojo session is connected, edit the project files and let Rojo sync; do not also edit the same scripts through MCP (Rojo overwrites). Reserve MCP for instances Rojo cannot hold (models, terrain, UI trees) and for running and reading.
4. **Serial**: one writer through MCP at a time; mark the session's jobs `serial` in `jobs.md`. Reads (`script_read`, `script_search`, `get_console_output`) may be interleaved by the same session only.
5. **Checkpoints**: before the first write take a restore point (git tag of the Rojo project; for MCP-only edits ask the user to publish/save a version or save a copy of the place; creating it is the user's action). After each logical change run `get_console_output` and note new errors. Define the rollback: `git restore`/tag for files, the saved version for the place.
6. Plan the **verification**: the playtest (`start_stop_play`, read Output, stop) and the exact acceptance lines; the 3-minute no-red-lines run is the usual bar. Use `playtest-evidence-logger` for the record.
7. **Do-not list**: no publishing, no spending, no changes to other places, no `execute_luau` that writes DataStores or calls external services, no secrets.
8. Save `docs/mcp-session-<date>.md` (headings Connection, Checkpoint, Serial, Rollback; under 90 lines) and check it.

## Studio MCP path
This is the MCP path: `list_roblox_studios` -> `get_studio_state` -> reads (`script_search`, `script_read`, `get_console_output`) -> writes (`multi_edit`, `execute_luau` in Edit datamodel) -> `start_stop_play` -> `get_console_output` -> stop. Tool names are taken from `rbx-studio`; confirm against the live tool list.

## Fallback
Rojo files plus `luau-check.sh` and `rojo build`; the plan marks every step that needs a running place `untested`.

## Evidence
`Roblox/roblox-kb/ai-and-tools.md` and the Studio MCP notes it points to (list_roblox_studios disambiguates by place id), `Roblox/roblox-kb/version-control-and-tooling.md` (commit or publish a backup before risky changes; Rojo sync is file-first), `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (the Studio MCP session is one shared writer, so MCP jobs stay serial; verification must be a run), `Manager/topic-tool-and-mcp-design.md`.

## Output
`docs/mcp-session-<date>.md`.

## Acceptance checks
- [ ] Executed: the tool list was inspected for `mcp__Roblox_Studio__` and the result (present/absent) is written down.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/mcp-session-<date>.md --kind mcpsession` prints PASS.
- [ ] A restore point step exists before the first write, or the plan says no writes will happen.
- [ ] Rojo-owned scripts are not in the MCP write list.

## Pitfalls
Editing a script through MCP while Rojo is connected. Two workers with Studio write access. No restore point before a bulk change. Reporting a static check as a playtest.

## Related
`rbx-studio`, `rbx-rojo`, `git-workflow-setter`, `playtest-evidence-logger`, `task-breaker`.
