---
name: team-roles-planner
description: "Decide who does what on a small Roblox team and how they collaborate: roles with owned folders and Roblox-side permissions, Team Create versus Rojo plus git versus Script Sync for this team, a backup for every critical role, and the written agreement. Use when a second person joins, when hiring one specialist, or when collaboration keeps colliding."
category: workflow
tags: team, roles, team create, rojo, collaboration, ownership, hiring, backup, permissions
kb: Roblox/roblox-kb/team-and-budget.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/version-control-and-tooling.md, Mentor/Combined-Brain.md, Manager/topic-managing-ai-agents-for-roblox-game-dev.md
related: collaborator-permissions-setter, roblox-group-setup, onboarding-new-dev, git-workflow-setter, folder-structure-planner, project-kickoff, sprint-planner
---

# team-roles-planner

Small teams fail on unclear ownership more than on skill. This skill writes the roles page and picks the collaboration mode. Group ranks and payouts are `roblox-group-setup` (marketing) and `group-management-planner` (community); setting actual Roblox permissions is `collaborator-permissions-setter` (publish) and the user's action. Workers (AI) count as team members with a folder and a fence.

## When to use
A second contributor is joining, you plan to hire for your weakest skill, or two people edited the same thing and lost work. Not for: recruiting copy, pay negotiation, or group rank design.

## Inputs (max 2)
1. Who is on the team now (people and AI workers) and their strengths. 2. Their working style: do they edit in Studio, in a code editor, or both (default: scripter in files, builder in Studio).

## Procedure
1. List the needed roles from the plan, not from a template: usually scripter, builder or map artist, UI, plus one owner for direction. Keep teams lean (2-4 is typical); one person may hold several roles.
2. Cover the weakest skill first: if an outside person is needed, make a small first hire with a paid sample task before a big commission; keep creative direction and core systems in-house.
3. Choose the collaboration mode with this table and write down why:

| Situation | Mode |
|---|---|
| Everyone builds and scripts live in Studio, small team | Team Create with Collaborative Editing, prompt commits; Team Create off when working solo |
| Code must be reviewed, AI workers write Luau | Rojo + git (file-first), Studio for map and instances only |
| Want code in git but the rest of the place in Studio | Script Sync (code-only version control) |
| Mixed team | Rojo owns `src/`; Team Create is used for builders on the same place; agree which tree each person may touch |

4. Write **Owns**: role -> folders in the repo and Explorer subtrees -> person. One owner per shared module; the `Remotes` module has one owner. Add the AI-worker rows (job id -> OWNS set).
5. Write **Collab** rules: commits or publishes how often, who may publish (the owner only), plugin and script hygiene rules for everyone (a bad plugin affects the whole Team Create place), and how conflicts are resolved (owner decides; Merge From Server flow in Team Create).
6. Write **Backup**: a named second person (or a documented module) for every critical role, because a stalled project when the one scripter leaves is a documented failure.
7. Save `docs/ROLES.md` (headings Roles, Owns, Collab, Backup; under 90 lines) and check it; confirm with the team, since it is a written agreement.

## Studio MCP path
None for planning. Studio-side permissions are set by the owner in Team Create settings and Creator Hub.

## Fallback
Markdown agreement only. Menu paths for Team Create change over time: live-check before instructing someone.

## Evidence
`Roblox/roblox-kb/team-and-budget.md` (cover your weakest skill first; start hiring small; keep creative direction in-house; lean teams of 2-4; vet by portfolio and paid sample; state pay in writing; same plugin and script hygiene for everyone; Team Create off for solo work), `Roblox/roblox-kb/development-process-and-speed.md` (split roles; do not depend on one scripter; Team Create with Collaborative Editing and prompt commits is 2021 guidance, live-check), `Roblox/roblox-kb/version-control-and-tooling.md` (Script Sync vs Rojo vs Drafts Mode), `Manager/topic-managing-ai-agents-for-roblox-game-dev.md` (one writer per file, ownership declared in the brief).

## Output
`docs/ROLES.md`.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/ROLES.md --kind roles` prints PASS.
- [ ] Every shared module and critical role has exactly one owner and one backup.
- [ ] The collaboration mode names which tree each person may edit.
- [ ] Menu-path claims are marked live-check.

## Pitfalls
Two collaboration modes editing the same scripts (Rojo would overwrite Studio edits). Hiring a big contractor before a paid sample. Roles by title without folders. No backup for the only scripter. Paying friends without written terms.

## Related
`collaborator-permissions-setter`, `onboarding-new-dev`, `git-workflow-setter`, `folder-structure-planner`, `roblox-group-setup`.
