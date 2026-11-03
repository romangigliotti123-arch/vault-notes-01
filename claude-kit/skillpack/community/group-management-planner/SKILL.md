---
name: group-management-planner
description: "Run a Roblox group as a living community, not just a name: ranks and permissions per role, who may touch money, wall moderation, audit-log habit, announcements and the group-versus-experience ownership question, plus a payout split calculator. Reuses the roles linter from roblox-group-setup. Use after the group exists and has members, a team or more than one person with rights."
category: community
tags: group, roles, ranks, permissions, payouts, moderation, audit-log, two-step, community, wall
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/social-features-and-virality.md
related: roblox-group-setup, ambassador-program-planner, moderation-rules-writer, clan-system-planner, discord-server-setup, devex-planner
---

# group-management-planner

`roblox-group-setup` creates a group with sensible first roles. This is the running side: who gets which rank as the team and community grow, how to keep damaging permissions with the creator, how to moderate the wall, and how to split revenue fairly. Roblox expects group owners to moderate actively and use the audit logs; the vault says to keep damaging permissions with the creator.

## When to use
The group has members and more than one person with rights, a collaborator asks for payouts, or the wall is unmoderated. Not for: first-time group creation (`roblox-group-setup`), in-game clans (`clan-system-planner`), or cash-out rules (`devex-planner`).

## Inputs (max 2)
1. People and their jobs (default: owner + 1-3 collaborators + volunteers). 2. Revenue arrangement, if any (default: none yet; a written agreement before anyone is promised a share).

## Procedure
1. List every person with: role, what they need to do, and the minimum permissions for that. Put it in `community/roles.csv` with columns `person,role,permissions,twosv` using the money words `payouts, revenue, ad_account, ad_invoices, analytics, ownership` for anything sensitive (map them to the live Roblox permission names first: they change).
2. Run `python skillpack/marketing/roblox-group-setup/scripts/roles_check.py community/roles.csv` (run from the kit root). Fix every FAIL (too many money holders, missing two-step verification, more than one owner, a tester or member role with money rights) and rerun to exit 0.
3. Define ranks for the community side: Owner, Developer, Moderator, Trusted (volunteers), Member. Volunteers get wall and moderation tools only, never funds, ownership or group settings.
4. Wall moderation: a written rule set (`moderation-rules-writer`), who deletes and bans, a weekly look at the audit log, and no promotion of violating content (the vault: group owners must make a reasonable effort to address harmful behavior).
5. Revenue split (only if agreed in writing): decide percentages that add to 100 and run `python scripts/payout_split.py --amount <robux> --split ann=50,bob=30,cy=20`; the amount comes from the live group funds page, never a guess. Payout approval stays with the owner; live-check Creator Hub for payout types and limits.
6. Branding and links: name the group after the studio, not one game; keep announcements (polls on the community page) to a regular rhythm; observe the limits on social links on game pages (verified-age requirements: live-check).
7. Leaving process: when someone leaves, remove rights the same day and rotate anything shared.

## Studio MCP path
Not applicable: group settings are not reachable from Studio. Optional: `script_grep` for `IsInGroup` / `GetRankInGroup` to see which rank gates in-game perks (use rank names, not hardcoded numbers).

## Fallback
Text, one CSV and the payout calculator. All group actions are the owner's; nothing is changed by the skill.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (keep damaging permissions with the creator; delegate moderation with escalation paths; name the group after the studio; use groups and notifications; sync in-game milestones to community roles via Open Cloud). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (groups: moderate actively, use audit logs, do not promote violative content). Payout mechanics are live-check items.

## Output
`community/group-plan.md`: roles table, `roles.csv`, linter output, wall moderation routine, split table (if any), leaving checklist. Under 80 lines.

## Acceptance checks
- [ ] `roles_check.py` exit 0 on `roles.csv`; output quoted.
- [ ] `payout_split.py --selftest` passes and the split run totals exactly the stated amount.
- [ ] Percentages add to 100 and are written down and agreed before use.
- [ ] No volunteer role holds money, ownership or group settings.
- [ ] Nothing in the plan changes the real group.

## Pitfalls
Giving broad roles for convenience. Verbal revenue promises. Payout rights without two-step verification. A group named after one game you later outgrow. No audit log habit. Hardcoding rank numbers in scripts.

## Related
`roblox-group-setup`, `ambassador-program-planner`, `moderation-rules-writer`, `clan-system-planner`, `devex-planner`.
