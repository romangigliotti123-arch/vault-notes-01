---
name: folder-structure-planner
description: "Design the repo layout and the matching Explorer tree for a Rojo-based Roblox project: server, client and shared folders, system folders with one owner each, where tests, docs and assets live, checked against default.project.json with foldercheck.py. Use when starting a project or when files have no obvious home."
category: workflow
tags: folders, structure, layout, rojo, explorer, repo, modules, ownership, architecture
kb: Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/development-process-and-speed.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md, Mentor/Combined-Brain.md
related: rbx-rojo, project-kickoff, git-workflow-setter, team-roles-planner, asset-pipeline-planner, code-style-guide-writer, dependency-pinner
---

# folder-structure-planner

`rbx-rojo` and `games.py init --rojo` create the basic `src/server`, `src/shared`, `src/client` layout. This skill decides how the inside is organised by system, so each system (and each worker) owns a folder, and checks that the tree matches `default.project.json`. It does not install tools (`dependency-pinner`) or place assets (`asset-pipeline-planner`).

## When to use
A new project, a project that has grown a `Utils` junk drawer, or before running parallel workers who need disjoint write sets. Not for: moving instances inside Studio only (that is Explorer hygiene, not repo layout).

## Inputs (max 2)
1. The project folder and its systems list (default: the systems named in `docs/kickoff.md`). 2. Team size (default: solo; more people means stricter ownership).

## Procedure
1. List systems from the plan: data, shop, combat, UI, map, services. One folder per system under each side that needs it, e.g. `src/server/Shop`, `src/shared/Shop` (types and config only), `src/client/Shop`.
2. Keep to the kit mapping: `src/server` to ServerScriptService, `src/shared` to `ReplicatedStorage.Shared`, `src/client` to `StarterPlayer.StarterPlayerScripts`, `Packages` to `ReplicatedStorage.Packages`. Map a dedicated child folder, never the repo root or a whole service by accident.
3. Put server-only secrets and logic only under `src/server`; `src/shared` holds ModuleScripts only (no Script/LocalScript there).
4. Set the file naming: `*.server.luau` (Script), `*.client.luau` (LocalScript), `*.luau` (ModuleScript), `init.luau` for folder modules, `*.spec.luau` for Lune tests, one extension (`.luau`) across the project.
5. Write the **Ownership** table: system -> folder -> owner (person or worker id). Shared modules such as `Remotes` have exactly one owner.
6. Place non-code: `docs/` (kickoff, decisions, handoff), `briefs/`, `reports/`, `assets/` (source files, not uploaded ids; see `asset-pipeline-planner`), `tests/`.
7. Apply it with file moves (not Explorer edits), then run `python folder-structure-planner/scripts/foldercheck.py <project>`; fix every FAIL (missing `$path`, misplaced scripts, space or case-only duplicates).
8. Save `docs/FOLDERS.md` (headings Repo, Explorer, Ownership; under 90 lines) and check it.

## Studio MCP path
After `rojo serve` is connected, optionally `search_game_tree` to confirm the Explorer tree matches the plan; never move instances through MCP if Rojo owns them (Rojo would overwrite).

## Fallback
File moves and `rojo build -o build.rbxl` as the proof the mapping resolves. Explorer layout is `untested` without Studio.

## Evidence
`Roblox/roblox-kb/version-control-and-tooling.md` (map `$path` to a dedicated child folder, not a service; Rojo for file-first projects; verify the build before live sync), `Roblox/roblox-kb/code-architecture-and-frameworks.md`, `Roblox/roblox-kb/development-process-and-speed.md` (split roles and parallelise team work), `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (decompose by file ownership; one shared Remotes module is one owner).

## Output
`docs/FOLDERS.md` and the moved files; foldercheck output.

## Acceptance checks
- [ ] Executed: `python folder-structure-planner/scripts/foldercheck.py --selftest` prints `selftest ok`; the project run prints PASS.
- [ ] Executed: `rojo build -o build.rbxl` succeeds (or `untested: rojo missing`).
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/FOLDERS.md --kind folders` prints PASS.
- [ ] Every folder has one owner in the table; no file name differs only by case.

## Pitfalls
A `Utils` folder that every system imports. Server code in `shared` because it was convenient. Case-only name clashes on Windows. Moving files while a worker holds them (finish or pause jobs first).

## Related
`rbx-rojo`, `project-kickoff`, `git-workflow-setter`, `team-roles-planner`, `asset-pipeline-planner`, `dependency-pinner`.
