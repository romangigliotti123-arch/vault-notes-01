---
name: onboarding-new-dev
description: "Onboard a new teammate (scripter, builder, artist or an AI worker) to a Roblox project in one day: access, setup commands that were actually run, the first small task with a verify step, and the house rules. Use when someone new joins or a worker starts a repo it has never seen."
category: workflow
tags: onboarding, new developer, teammate, setup, first task, access, rules, collaborator
kb: Roblox/roblox-kb/team-and-budget.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/version-control-and-tooling.md, Manager/topic-context-engineering.md, Mentor/Combined-Brain.md
related: team-roles-planner, project-kickoff, folder-structure-planner, docs-writer-roblox, collaborator-permissions-setter, git-workflow-setter, code-style-guide-writer
---

# onboarding-new-dev

A new person (or a fresh AI session) needs the same four things: access, a working setup, a first success, and the rules. The skill produces one page, `docs/ONBOARDING.md`, built from the project's own files and from commands run on a clean checkout. Roles and permissions are `team-roles-planner` and `collaborator-permissions-setter`; hiring and vetting is in the vault KB, not here.

## When to use
Someone joins within a week, or a worker is starting a project it has not seen. Not for: recruiting and vetting, or granting Roblox permissions (the owner does that).

## Inputs (max 2)
1. Who and what role (scripter, builder, UI, artist, AI worker). 2. How they work (Rojo files, Team Create in Studio, or both; default: read from `docs/ROLES.md` if it exists).

## Procedure
1. **Day one**: write the order of the day in four lines: read `docs/kickoff.md`, set up, do the first task, post the result for review.
2. **Setup**: list exact commands for their path: clone, `rokit install`, `rojo build -o build.rbxl`, `luau-check.sh src`, `rojo serve` and the Studio plugin connect, or "open the Team Create place from the owner's invite". Run these yourself on a clean clone (or a temp folder copy) and paste the last line of each; mark any you could not run `untested`.
3. **Access**: list what the owner must grant (Team Create invite, repo access, Discord role, asset permissions) by name and who grants it. Never include tokens, keys or passwords in the page.
4. **First task**: pick a real, small, low-risk task (fix a typo'd constant, add a unit test, rename a variable behind a Lune test) with a verify command; assign a folder they own. Hand the full task through `ai-brief-writer` if the newcomer is a worker.
5. **Rules**: link `docs/STYLE.md`, `docs/GIT.md`, the ownership table in `docs/FOLDERS.md`; add three house rules in plain words (ask before touching others' folders, no publishing or spending, report in the standard format).
6. **Buddy**: name the human who reviews the first change; define "done" as reviewed and merged, not pushed.
7. Save `docs/ONBOARDING.md` (headings Day one, Setup, First task, Rules; under 100 lines) and check it.

## Studio MCP path
For an AI worker: `list_roblox_studios` and `get_studio_state` to learn which place is open, and say whether Studio jobs are serial. Do not open or focus Studio.

## Fallback
All steps are commands and text; the Team Create path is steps in Studio the owner performs (`untested` until a second account joins).

## Evidence
`Roblox/roblox-kb/team-and-budget.md` (define roles in writing; vet by a paid sample task; hold every collaborator to the same plugin and script hygiene; keep a stable core plus flexible contractors), `Roblox/roblox-kb/development-process-and-speed.md` (clear specs and backup scripters so work survives people leaving; Team Create with Collaborative Editing and prompt commits, 2021 guidance so live-check menu paths), `Roblox/roblox-kb/version-control-and-tooling.md`, `Manager/topic-context-engineering.md` (what a context-free reader needs).

## Output
`docs/ONBOARDING.md`.

## Acceptance checks
- [ ] Executed: the setup commands were run on a clean copy and last lines pasted, or marked `untested`.
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/ONBOARDING.md --kind onboarding` prints PASS.
- [ ] First task has a verify command and an owner folder.
- [ ] No secrets or personal data in the page.

## Pitfalls
A setup page written from memory that no longer works. A first task that touches shared modules. Granting write access to everything on day one. Forgetting the Roblox-side access (Team Create, group roles) that files cannot carry.

## Related
`team-roles-planner`, `project-kickoff`, `folder-structure-planner`, `docs-writer-roblox`, `collaborator-permissions-setter`, `git-workflow-setter`.
