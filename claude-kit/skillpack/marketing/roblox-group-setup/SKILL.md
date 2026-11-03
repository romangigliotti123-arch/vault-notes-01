---
name: roblox-group-setup
description: "Set up a Roblox group (community) for a game or studio: name, description, social links, roles and permissions kept least-privilege, announcement and wall rules, in-game group perks, and the security steps before anyone gets payout rights. Use when creating or tidying a group; Discord is discord-server-setup."
category: marketing
tags: roblox group, community, roles, permissions, announcements, group wall, payouts, audit log, group perks, brand
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/business-and-payouts.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/influencer-and-creator-marketing.md
related: discord-server-setup, social-post-calendar, brand-kit-builder, community-showcase-planner, roblox-monetization-audit, press-kit-builder
---

# roblox-group-setup

A group is the in-platform home of a game's audience and, for co-owned games, the owner of the game and its money. Vault: name it after the studio, link socials on the community page, use announcements with polls, promote it in-game with a perk, and protect payout permissions. Group creation costs Robux and permission changes affect money, so the owner performs every step; this skill prepares the plan.

## When to use
Creating a studio group, converting a personal game to a group-owned one, or cleaning up roles. Not for: the Discord (`discord-server-setup`), Robux or payout strategy (`roblox-monetization-audit`).

## Inputs (max 3)
1. Studio or game name and number of collaborators. 2. Is the game group-owned or personal (default: personal, moving to group if co-owned). 3. Roles needed (default: Owner, Admin, Developer, Moderator, Tester, Member).

## Procedure
1. Decide the type: flat fan group for a simple game; deeper ranked roles only when rank unlocks something (vault: structure should match design depth). Co-owned games and shared profit belong in a group, with the split documented in writing.
2. Name and brand: name after the studio, not a single hit; icon from the brand kit (`brand-kit-builder`); description: what you make, where to play, how to report problems, community rules in three lines. All-ages language. Live-check current group rules and costs on Creator Docs and the Roblox help pages; record with date.
3. Social links: the community page takes YouTube, Discord and X links (vault); add them.
4. Roles by least privilege. Draft a table: role, who, what it can do. Keep payouts, revenue, ad accounts and analytics for the smallest trusted set; sensitive permissions require two-step verification, turn it on for every holder first (vault). Never give a collaborator ownership. Write the plan as `marketing/roles.csv` (`person,role,permissions,twosv`, money permissions named payouts, revenue, ad_account, ad_invoices, analytics, ownership) and run `python -I ~/.claude/claude-kit/skillpack/marketing/roblox-group-setup/scripts/roles_check.py marketing/roles.csv`; fix every FAIL (too many money holders, missing 2SV, shared ownership, low roles with money rights).
5. Content rules: announcements and polls for updates (members are notified), wall rules written in the description, a moderator on duty, a plan for spam. Use the audit log / activity history to watch collaborator actions; repeated inaction on violations can restrict future ownership (vault).
6. In-game perks that reward joining without a paywall: a group-only item, a member tag via `Player:IsInGroup`, rank-based tags; check behaviour live. Optional: sync milestones to group roles via Open Cloud (vault, single source) if the owner wants it.
7. Funnel: link the group from the game description and Discord (`discord-server-setup`), and use it as the channel for update posts (`update-announcement-writer`).
8. Hand the owner the step list; they create the group, set roles and turn on 2SV themselves.

## Studio MCP path
Only for the in-game perk. `list_roblox_studios` -> `get_studio_state`, then `multi_edit` to add a server-side `IsInGroup` check (group id placeholder `0`); verify with `start_stop_play` and `get_console_output`. Group settings are not reachable via Studio.

## Fallback
The plan as a document and a Luau snippet using `Player:IsInGroup(groupId)`, group id `0` = SET BY OWNER; the check is `untested` without a published place and a test account.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (name the group after your studio; social links on the community page; promote the group in-game; announcements with polls; flat vs ranked structure; audit logs; group-member tags with IsInGroup, low-advice), `Roblox/roblox-kb/business-and-payouts.md` (use a group for co-owned games and document the split; restrict analytics, payouts and ad invoices to trusted roles; two-step verification before payout permissions), `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`, `Roblox/roblox-kb/influencer-and-creator-marketing.md` (creator programmes with Talent Hub profiles). Costs and permission names change: live-check.

## Output
`marketing/group-plan.md`: type decision, name and description text, links, role table with permissions, 2SV checklist, moderation rules, perk design, owner step list.

## Acceptance checks
- [ ] `roles_check.py` exit 0 on `marketing/roles.csv` (output quoted); payout rights are limited to named people.
- [ ] 2SV is listed as done for each holder before payout rights.
- [ ] Costs and rules cite a source and date from this run.
- [ ] Group id in code is `0` until the owner supplies it.
- [ ] Nothing was created, joined or changed by the skill.

## Pitfalls
Giving broad roles for convenience. A group named after one game that you later outgrow. No moderation on the wall. Paywalling the group perk. Skipping the written profit split.

## Related
`discord-server-setup`, `brand-kit-builder`, `social-post-calendar`, `community-showcase-planner`, `roblox-monetization-audit`.
