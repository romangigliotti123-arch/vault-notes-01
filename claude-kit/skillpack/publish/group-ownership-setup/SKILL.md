---
name: group-ownership-setup
description: "Move an experience under a group (or receive one) without breaking it: prerequisites, private assets and packages, API keys, place copying, roles and payout splits, title continuity, and a gate list judged by the same go/no-go script as the launch gate. Use before any ownership transfer or when starting a game under a group."
category: publish
tags: group, ownership transfer, roles, payouts, API keys, packages, place copying, team, publish, revenue split
kb: Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/team-and-budget.md, Roblox/roblox-kb/studio-business-funding-and-publishing.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: collaborator-permissions-setter, roblox-group-setup, place-backup-planner, publish-readiness-gate, audio-permission-checker, asset-license-checker
---

# group-ownership-setup

One job: a transfer that loses nothing. A game under a group unlocks group permissions and revenue management; a careless transfer breaks private scripts, assets and API keys, hides the game, or moves money differently than agreed. `scripts/transfer_gates.py` emits a gate list in the format of `publish-readiness-gate/scripts/gate.py`, so the same arithmetic gives GO or NO-GO with evidence. Requests expire, cooldowns apply and payment details are removed: every number and rule below is `live-check`, because the Creator Docs change. The transfer itself is the owner's action in Creator Hub.

## When to use
Before transferring a game to a group, before accepting one, and when starting a project under a group. Not for: marketing the group page (`roblox-group-setup`), role design in detail (`collaborator-permissions-setter`), backups (`place-backup-planner`).

## Inputs (max 2)
1. Sending and receiving owner (user or group). 2. Agreed revenue split, in writing (default: not agreed yet; this blocks the gate).

## Procedure
1. Open the live ownership-transfer and groups pages (Evidence); copy the prerequisites, request expiry, re-transfer cooldown and discovery notes with the date.
2. Back up first: run `place-backup-planner` and keep the verified manifest.
3. Make the gate file: `python -I ~/.claude/claude-kit/skillpack/publish/group-ownership-setup/scripts/transfer_gates.py --template > release/transfer.json`.
4. Work each gate with a real check and paste evidence: sender email verified; private ModuleScripts and InsertService assets moved to the group; user-owned packages recreated or replaced with group-owned ones (`list_assets.luau` helps); Open Cloud API keys reviewed (keys follow the access of the user who generated them, so regenerate under an account that keeps access); Place Copying disabled before private assets go in; roles least-privilege (run `collaborator-permissions-setter`).
5. Money: agree splits in writing; Roblox does not arbitrate group disputes. Model the split math with the group payout rules (per-game and group-wide percentages, remainder to the group balance); subscription split percentages for private servers are fixed at purchase time.
6. Run `python -I .../publish-readiness-gate/scripts/gate.py release/transfer.json`. NO-GO lists each blocker; fix, re-collect evidence, re-run.
7. Transfer (owner action): keep the title unchanged, make no edits while the request is pending (changes are not carried over), and finish before the request expires.
8. After acceptance: the receiver sets payment details (they are removed in transfer), sets permissions, releases the game again (it stays hidden otherwise) and watches discovery for the first day. Record in `release/transfer-after.md`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) running `build/asset-license-checker/scripts/list_assets.luau` and a search for `require(` of non-local assets to find private dependencies -> `get_console_output`. The transfer, roles and keys are web actions; no MCP tool performs them.

## Fallback
The gate list and script work offline. Everything about the real dashboard (transfer button, expiry, cooldown) is `untested` until the owner runs it.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs projects game-ownership-transfer.md` (prerequisites, API keys, 7-day request expiry, 30-day re-transfer wait, credit card removal, discovery window, no edits during transfer), `... Docs projects groups.md` (roles least privilege, two-step verification for money roles, payout splits, place copying, audit logs, no arbitration), `... Docs projects group-guidelines.md` (owners must moderate), `... Docs projects activity-history.md`. Pack: `Roblox/roblox-kb/business-and-payouts.md`, `Roblox/roblox-kb/team-and-budget.md`.

## Output
`release/transfer.json` (with evidence), the printed verdict, `release/transfer-after.md`.

## Acceptance checks
- [ ] `gate.py release/transfer.json` printed `VERDICT: GO` (quote it) before the transfer.
- [ ] A verified backup manifest is attached.
- [ ] The revenue split is written and linked.
- [ ] The live page date is recorded.
- [ ] `transfer_gates.py --selftest` prints `selftest ok`.

## Pitfalls
Forgetting that a private ModuleScript stops loading for the new owner. API keys that silently lose access. Editing the place during the pending request. Changing the title and losing search. Treating a verbal split as an agreement.

## Related
`collaborator-permissions-setter`, `roblox-group-setup`, `place-backup-planner`, `publish-readiness-gate`, `asset-license-checker`.
