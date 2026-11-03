---
name: leaderboard-hooks-planner
description: "Plan how leaderboards build community instead of discouraging newcomers: friends-only and group boards, seasonal resets, leagues or tiers, hall-of-fame and clan boards, safe name display, and community hooks (Discord role for a top rank, season recap posts). Hands the build to leaderboard-builder. Use when a global top-100 is stale, unreachable for new players, or ignored."
category: community
tags: leaderboard, ranking, community, friends, seasons, leagues, social, recognition, retention, privacy
kb: Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/player-psychology-and-game-feel.md
related: leaderboard-builder, clan-system-planner, social-hook-designer, community-event-planner, streamer-kit-builder, ambassador-program-planner, event-planner
---

# leaderboard-hooks-planner

A global leaderboard rewards the top few and tells everyone else they are far behind. The vault's social advice: friends are a retention engine, new players need protection from veterans, and rewards for group play should not punish solo players. This decides which boards to show, who sees whom, and how rankings connect to the Discord and the group. It does not build the board (that is `leaderboard-builder`).

## When to use
A leaderboard exists but does not move behaviour, or you are designing one for a social game. Not for: the DataStore implementation (`leaderboard-builder`), clan mechanics (`clan-system-planner`), or invite hooks (`friend-invite-reward-builder`).

## Inputs (max 2)
1. The stat and how fast it grows (default: a score that grows without bound). 2. Typical audience size per server and overall (default: small, so avoid global-only boards).

## Procedure
1. Choose boards in layers, smallest first: Friends (people the player knows, from the platform friends list; the most motivating and safest), Server (this session), Clan or group (team pride), Season (resets so everyone restarts), Global hall of fame (permanent, top few). Ship two boards, not five.
2. Reachability: for a new player the visible target should be near them. Show "you are #214, 12 points from #200", a tiered league (bronze to gold) with promotion rather than one flat list, and weekly boards so a new account can reach the top ten.
3. Season rules: season length, reset time (fixed, announced), what carries over (cosmetics, titles; never the stat), end-of-season rewards for ranges rather than only rank one, and a recap post for the Discord and group.
4. Fairness and anti-cheat: rankings only from server-validated values; ban exploiters from boards with a visible procedure (see `exploit-audit`); allow appeal.
5. Privacy and safety: show display names the platform has already filtered; give a "hide me" option and use the streamer alias module (`streamer-kit-builder/scripts/StreamerAlias.luau`) for streamers; never show a player's exact location or join time; no public shaming boards (worst, most deaths).
6. Community hooks: a Discord role or group rank for a season top ten (via the owner's process, e.g. Open Cloud sync of in-game milestones to group roles; live-check), a monthly "top builders" post with consent, and friendly team vs team seasons.
7. Metrics: share of players who view a board, share of new players who reach the first league tier, retention of players in the top half vs bottom half, Discord joins after a season post.
8. Lint the player-facing copy (board titles, reward and recap posts): `python welcome-message-writer/scripts/text_lint.py leaderboard-copy.txt`.

## Studio MCP path
Planning only; when the user approves the build use `leaderboard-builder`: `list_roblox_studios` -> `get_studio_state` -> `multi_edit`, then `start_stop_play` and `get_console_output`. Friends data is read at runtime with the platform friends API (live-check availability).

## Fallback
The plan is text; the build skill has its own fallback.

## Evidence
`Roblox/roblox-kb/social-features-and-virality.md` (friends found in days 1-7 retain better; protect new players from veterans; scale rewards for group play without punishing solo players; do not isolate friends). `Roblox/roblox-kb/community-and-discord.md` (sync in-game milestones to community roles via Open Cloud; groups and notifications). `Roblox/roblox-kb/player-psychology-and-game-feel.md`.

## Output
`community/leaderboards.md`: board table (scope, stat, reset, who sees what, privacy), season rules, reward ladder, hooks, metrics, copy. Under 70 lines.

## Acceptance checks
- [ ] At most two boards at launch and at least one is a friends, clan or tiered board.
- [ ] A new player can see a reachable target (tier, weekly board or neighbours).
- [ ] Display uses platform-filtered names with a hide option; no shame boards.
- [ ] `text_lint.py` exits 0 on the copy.
- [ ] The build is handed to `leaderboard-builder` with server-validated values only.

## Pitfalls
Only a global top 100. Never resetting. Cheater-dominated boards. Revealing too much about a young player. Rewards only for rank one. Building five boards nobody opens.

## Related
`leaderboard-builder`, `clan-system-planner`, `social-hook-designer`, `streamer-kit-builder`, `community-event-planner`.
