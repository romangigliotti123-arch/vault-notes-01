---
name: git-workflow-setter
description: "Set up the git side of a Rojo project: .gitignore for Roblox, one-branch-per-feature naming, conventional commit subjects, a snapshot rule before risky changes and a rollback recipe, all checked with gitcheck.py. Use when a Roblox project is not under git yet or its history is unreadable."
category: workflow
tags: git, branch, commit, gitignore, rojo, snapshot, rollback, version control, merge
kb: Roblox/roblox-kb/version-control-and-tooling.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/team-and-budget.md, Manager/topic-multi-agent-failure-modes.md, Mentor/Combined-Brain.md
related: rbx-rojo, folder-structure-planner, ci-check-setter, changelog-writer, version-history-keeper, place-backup-planner, team-roles-planner
---

# git-workflow-setter

`rbx-rojo` (and `games.py init --rojo`) lays out the project and a basic `.gitignore`. This skill sets the habits on top: how branches and commits are named so history, changelog and rollback work. Place-level restore points and Creator Hub version history are `version-history-keeper` and `place-backup-planner` in the publish category; this is about the source repo.

## When to use
`git init` has not been run, the ignore file is missing entries, commits read "stuff", or a worker is about to edit files and you want a snapshot first. Not for: whether to use Team Create or Rojo (`team-roles-planner`), CI hooks (`ci-check-setter`).

## Inputs (max 2)
1. The project folder. 2. Solo or team (default: solo, branches `main` plus short-lived `feat/...`; team adds a protected `main` and pull requests).

## Procedure
1. `git rev-parse --is-inside-work-tree`; if it fails run `git init -b main`. Stop condition: never run it inside a folder that already sits in another repo; report instead.
2. Write `.gitignore` from the kit template (`tools/roblox-project-template/.gitignore`) and make sure it has `Packages/`, `sourcemap.json`, `*.rbxl`, `*.rbxlx`, `.env`, `*.key`, `build/`. Run `python git-workflow-setter/scripts/gitcheck.py ignore .gitignore`; fix until PASS.
3. Branch rule: `<type>/<kebab-slug>` with type feat, fix, chore, docs or exp; one branch per feature, rebased on `main` often, merged when its acceptance test passes. Check a name with `python git-workflow-setter/scripts/gitcheck.py branch feat/shop-limit`.
4. Commit rule: `type(scope): what changed`, subject at most 72 characters, no trailing full stop; check with `gitcheck.py msg "<subject>"`. Small commits per verified step so a worker's work can be diffed.
5. Snapshot rule: before a refactor, a terrain or bulk edit, or a worker job with write access, commit (or `git tag snap-<date>`) so rollback is one command. Rollback recipe: `git switch -c rescue` then `git revert <sha>` for shared history; `git restore <path>` for one file. Never rewrite pushed history without the owner's say.
6. Remote: a private repo per game. Pushing to a remote is the user's action; prepare, do not push.
7. Write `docs/GIT.md` (Branch, Commit, Ignore, Rollback; under 90 lines) and check it.

## Studio MCP path
None. If Rojo is connected, git sees only the files Rojo owns; edits made inside Studio are not in the repo until the user syncs them (Script Sync or a published version), so say so in GIT.md.

## Fallback
All steps are plain git commands. GitHub Desktop is a valid GUI for the same rules.

## Evidence
`Roblox/roblox-kb/version-control-and-tooling.md` (keep the place binary out of git and version the sources; commit a snapshot before risky changes; one branch per feature and rebase main in often; Script Sync vs Rojo vs Drafts Mode), `Roblox/roblox-kb/development-process-and-speed.md` (duplicate or back up before destructive edits), `Manager/topic-multi-agent-failure-modes.md` (parallel writers conflict; use a single writer per path and a clean diff to review).

## Output
`.gitignore`, `docs/GIT.md`, an initial commit made by the user or on their go-ahead.

## Acceptance checks
- [ ] Executed: `python git-workflow-setter/scripts/gitcheck.py --selftest` prints `selftest ok`; `gitcheck.py ignore .gitignore` prints PASS.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/GIT.md --kind gitflow` prints PASS.
- [ ] `git status --short` shows no place binaries or Packages tracked.
- [ ] Rollback recipe tried once on a throwaway branch, or marked `untested`.

## Pitfalls
Committing `.rbxl` files (huge, unmergeable). Long-lived branches that diverge from `main`. Force-pushing shared history. Assuming Studio-side edits reach git by themselves. The kit template's own `.gitignore` is minimal (lock files, Packages, sourcemap, .DS_Store): it lacks `*.rbxl`, `*.rbxlx`, `.env`, `*.key` and `build/`, so step 2 adds them and gitcheck proves it.

## Related
`rbx-rojo`, `folder-structure-planner`, `ci-check-setter`, `changelog-writer`, `version-history-keeper`, `place-backup-planner`.
