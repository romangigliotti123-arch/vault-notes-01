---
name: ambassador-program-planner
description: "Design a small, safe program that rewards helpful community members (ambassadors, helpers, moderators-in-training): selection, tiers, perks that are not pay-to-win, duties, adult oversight for young volunteers, how to say thanks and how to part ways. Reuses the roles linter so helpers never hold money or admin. Use once a community has regular helpers or before delegating moderation."
category: community
tags: ambassador, helpers, volunteers, rewards, moderation, roles, community, recognition, safety
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: group-management-planner, moderation-rules-writer, discord-server-setup, creator-collab-planner, welcome-message-writer, community-event-planner
---

# ambassador-program-planner

The vault: treat testers, bug reporters and Discord mods as an extension of the team, let them self-organise and thank them regularly; reward engaged members with visible status. Done carelessly, volunteer programs create unpaid labour, drama and safety risk with young helpers. This keeps it small and safe.

## When to use
Three or more people already answer questions or report bugs unprompted, or you are about to hand out moderation rights. Not for: paid creator deals (`creator-collab-planner`), group permissions and payouts (`group-management-planner`), or the rule ladder (`moderation-rules-writer`).

## Inputs (max 2)
1. Community size and who already helps (default: a few regulars, no formal roles). 2. Helper ages (default: assume some are under 18; staff with moderation power are adults).

## Procedure
1. Define 2-3 tiers only: Helper (answers FAQ questions, reports problems, can warn), Ambassador (hosts events, welcomes members, trusted voice), Moderator (adult, timeouts and bans per the ladder). Each tier lists duties, hours expected (small), rights, and what is never allowed (money, ownership, DMs with minors, speaking officially for the game).
2. Selection: invite based on observed helpfulness over weeks, not requests or flattery; two staff agree; no minors in moderation roles with enforcement power (platform policies differ: live-check Discord and Roblox rules for volunteer minors).
3. Perks, none pay-to-win: a role colour, credit in a patch note (with consent), early access to a test build, a say in cosmetic votes, a cosmetic item, a monthly thank-you. Avoid paying young volunteers in Robux unless the owner has checked the platform's rules; if any payment exists, it goes through the group payout process with the owner approving, never from a personal account.
4. Permissions: build `community/ambassadors.csv` (`person,role,permissions,twosv`) for any group or Discord rights and run `python skillpack/marketing/roblox-group-setup/scripts/roles_check.py community/ambassadors.csv` (run from the kit root); exit 0 required: no helper holds payouts, revenue, ads or ownership.
5. Onboarding and conduct: a one-page code of conduct (same standards as members, plus confidentiality about unreleased content, no favoritism); a trial period of two weeks; a named staff mentor.
6. Care and exit: monthly check-in, rotate heavy duties, no guilt about quitting; removal is a private conversation with the reason, rights revoked the same day.
7. Lint the invitation and thank-you texts: `python welcome-message-writer/scripts/text_lint.py ambassador-texts.txt`.

## Studio MCP path
Not needed. Optional for in-game recognition: `list_roblox_studios` -> `get_studio_state` -> `script_grep` for existing group-rank perks before proposing a badge or title.

## Fallback
Text and one CSV. Creating roles and inviting people is the owner's action.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (treat engaged members as team extension and thank them; delegate moderation with escalation paths; keep damaging permissions with the creator; sync in-game milestones to roles). `Roblox/roblox-kb/influencer-and-creator-marketing.md` (credit and reward creators; recognition builds loyalty). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`.

## Output
`community/ambassadors.md`: tiers table, selection rules, perks, conduct page, exit process, plus `ambassadors.csv` and the linter output. Under 80 lines.

## Acceptance checks
- [ ] `roles_check.py` exit 0 on the CSV; output quoted.
- [ ] No perk requires payment or can be sold; no helper holds money or ownership.
- [ ] Moderation with enforcement power is adults-only in the plan.
- [ ] Every duty has a stated time expectation; an exit process exists.
- [ ] `text_lint.py` exits 0 on the invitation and thank-you texts.

## Pitfalls
Unpaid labour with no recognition. Handing admin to the friendliest person. Young volunteers doing enforcement alone. Favoritism. Perks that become status for sale. No way to leave gracefully.

## Related
`group-management-planner`, `moderation-rules-writer`, `creator-collab-planner`, `community-event-planner`.
