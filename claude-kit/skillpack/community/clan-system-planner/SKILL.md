---
name: clan-system-planner
description: "Design clans, guilds or teams inside a Roblox game: create, join, ranks, kick, leave, size caps, name rules, clan perks and boards, abuse and safety rules. Ships ClanRules.luau (pure permission and validation rules with Lune tests) the server wires to storage and remotes. Use when the game needs durable social groups beyond one server session."
category: community
tags: clan, guild, team, social, ranks, permissions, in-game, retention, moderation, luau
kb: Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: group-management-planner, leaderboard-hooks-planner, friend-invite-reward-builder, remote-guard-builder, datastore-schema-builder, chat-filter-tester, moderation-rules-writer
---

# clan-system-planner

The vault lists guilds, trading, gifting and collaborative building among the systems that drive retention in social games, and notes that structure should match design: flat fan groups for simple games, ranked hierarchies where rank unlocks gameplay. This plans the in-game clan (not the Roblox group; see `group-management-planner`) and ships the tested rules module.

## When to use
Players want teams that persist across sessions, or you want group play perks and boards. Not for: managing the Roblox group (`group-management-planner`), invite rewards (`friend-invite-reward-builder`), or pure server-session parties.

## Inputs (max 2)
1. What clans do in this game (default: shared perks, a clan board, a clan chat channel). 2. Max size and ranks (default: 30 members; member, officer, leader).

## Procedure
1. Define the purpose and the cost of joining: what a clan gives (a small shared bonus that scales with online members, a board, a tag), never a bonus that makes solo play unviable (vault: scale group rewards without punishing solo players).
2. Ranks and rules from `scripts/ClanRules.luau`: `canJoin` (member, banned, full), `canKick` (strictly higher rank, never yourself or the leader), `canSetRank` (leader only), `canLeave` (the leader must transfer first unless alone), `validName` (3-20 characters, letters, digits and single spaces) and `validate` (exactly one leader, within size). Add rules the module lacks only with tests.
3. Wiring (server only): remotes for create/join/leave/kick/setRank, each going through kit `RemoteGuard` rate limits and argument validation (`remote-guard-builder`); the server reads the actor's rank from the clan record, never from the client; clan records saved with `UpdateAsync` so two officers cannot both take the last slot (`datastore-schema-builder`).
4. Safety: every clan name, tag and message is passed through `TextService:FilterStringAsync` (or TextChat) on the server before it is stored or shown; names are re-filtered for each viewer where the API requires it (live-check); clan chat uses TextChannels so messages stay reportable and respect parental settings; a report button exists; moderators can rename or disband a clan; no external links or contact details in names.
5. Anti-abuse: cap clans created per account per day, require some playtime before creating, throttle invites, and lock clan perks against alt-farming (one claim per account).
6. Boards and community hooks: a clan board from `leaderboard-hooks-planner`, a clan announcement, optional sync to a Discord role by the owner; keep clan features optional for players who prefer solo play.
7. Run `cd systems && lune run ../skillpack/community/clan-system-planner/scripts/tests/ClanRules.test.luau` (6 tests); the whole pack with `bash skillpack/check-scripts.sh skillpack/community`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `ClanRules.luau` under ServerScriptService and the service wiring -> `start_stop_play` -> `execute_luau` (Server datamodel) to call the rules with junk and valid input -> `get_console_output`. Real DataStore round trips and filtering need a published place and two accounts: `untested`.

## Fallback
`ClanRules.luau` and its Lune tests work without Studio; wiring is hand steps. Filter behaviour and persistence are `untested` until run in a published place.

## Evidence
`Roblox/roblox-kb/social-features-and-virality.md` (guilds, trading, gifting drive retention; scale group rewards without punishing solo players; do not isolate friends into separate instances). `Roblox/roblox-kb/community-and-discord.md` (structure should match design; sync in-game milestones to roles). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (filter all user text; use TextChannels; moderate groups actively).

## Output
`community/clans.md` (feature spec, rank table, safety list), `ClanRules.luau` placed in the game, and the Lune output pasted.

## Acceptance checks
- [ ] The ClanRules Lune test runs green; the output is quoted ("6 passed, 0 failed").
- [ ] All clan text is server-filtered in the spec and the code.
- [ ] Every rank decision happens on the server from the stored record.
- [ ] Abuse limits (creation cap, invite throttle, one claim per account) are listed.
- [ ] Solo players are not locked out of core progression.

## Pitfalls
Letting the client send its rank. Unfiltered clan names. Leaderless clans. Mandatory clans. Perks so large that solo play is worse. Clan chat outside the platform chat system.

## Related
`group-management-planner`, `leaderboard-hooks-planner`, `friend-invite-reward-builder`, `remote-guard-builder`, `datastore-schema-builder`.
