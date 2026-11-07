---
name: collaborator-permissions-setter
description: "Set who can edit, play, publish and see money for an experience with least privilege: permission levels, friend and age rules for Team Create, group roles, money-permission holders, two-step verification, and an access review through Activity History. Use when adding teammates, contractors or testers, and before launch."
category: publish
tags: collaborators, permissions, team create, roles, least privilege, group, access review, two-step verification, contractors
kb: Roblox/roblox-kb/team-and-budget.md, Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/development-process-and-speed.md
related: group-ownership-setup, roblox-group-setup, place-backup-planner, version-history-keeper, exploit-audit, secrets-leak-scanner
---

# collaborator-permissions-setter

One job: nobody has more access than the job needs, and you can show it. A rogue or compromised editor can publish, change prices or pull assets. This skill builds the access table (person, role, what they can do, expiry) and checks the money side with the pack's `marketing/roblox-group-setup/scripts/roles_check.py` (money-permission holders, two-step verification, ownership). Permission names, levels and age rules are `live-check`: the Creator Docs collaboration and group pages change, and the script's money list is mapped to the live names first.

## When to use
Adding a collaborator, contractor or tester; after a team change; before launch; after any unexpected change. Not for: transferring ownership (`group-ownership-setup`), designing the group's public page (`roblox-group-setup`), scanning code for leaked keys (`secrets-leak-scanner`).

## Inputs (max 2)
1. Who needs access and for what (default: owner only). 2. Is the game user-owned or group-owned (default: group if more than two people).

## Procedure
1. Open the live collaboration and groups pages (Evidence); copy the permission levels, the friends-only rule for Edit on user-owned games, the age-pairing rules and the money-permission rules with the date.
2. Build `roles.csv` with columns `person,role,permissions,twosv` where permissions is a semicolon list using the live permission names mapped onto the script's money words (payouts, revenue, ad_account, ad_invoices, analytics, ownership).
3. Run `python -I .rbx/claude-kit/skillpack/marketing/roblox-group-setup/scripts/roles_check.py roles.csv`. Fix every FAIL: too many money holders, a money role without two-step verification, ownership held by more than one person.
4. Least privilege by task: scripters get script edit, artists get asset and place edit only for the window they need it, testers get Play only (anyone can have Play; Edit needs a friend on user-owned games), contractors get time-boxed access with an end date in the table.
5. On group games prefer role-based Edit across all games for permanent staff (e.g. audio artist) and per-game Edit for temporary work.
6. Team Create age-check: collaborators and owners must complete the age check before joining; pairing by age group is limited, so confirm that a minor collaborator can join before promising it.
7. Script safety: use Drafts mode for script collaboration where you want a commit-like flow; never give edit access to a collaborator you would not give the code to.
8. Access review: monthly and after incidents, read Activity History filtered by collaborator and event type; remove stale members. Record the review date. Write `release/access.md` with the CSV, script output and review log.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> no MCP tool changes permissions: they are set in Creator Hub or the Studio collaboration panel by the owner. `execute_luau` (Edit) can list scripts changed recently by name for an informal review only.

## Fallback
The CSV, the script and the review log are plain files. Real permission state is read from the dashboard; until then every access row is `untested`.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs projects collaboration.md` (age check, Edit only for friends on user-owned games, role-based access on groups, Drafts mode, disable Team Create before reverting), `... Docs projects groups.md` (least privilege, two-step verification for money roles, audit logs), `... Docs projects group-guidelines.md`, `... Docs projects activity-history.md` (who changed prices, paid access and private servers). Pack: `Roblox/roblox-kb/team-and-budget.md`, `Roblox/roblox-kb/business-and-payouts.md`.

## Output
`roles.csv` and `release/access.md`.

## Acceptance checks
- [ ] `roles_check.py roles.csv` exits 0 (quote its summary line).
- [ ] Every person has a role, a purpose and an end date or "permanent" with a reason.
- [ ] The live permission names are mapped in the notes (date included).
- [ ] An access review date is recorded.
- [ ] `roles_check.py --selftest` prints `selftest ok`.

## Pitfalls
Giving money permissions to the person who built the shop. Leaving contractors in after the job. Assuming Edit can be given to any stranger on a user-owned game. Reverting a place while Team Create is on (auto-saves overwrite it).

## Related
`group-ownership-setup`, `roblox-group-setup`, `place-backup-planner`, `version-history-keeper`, `exploit-audit`.
