---
title: "Docs: players / users"
url: https://create.roblox.com/docs/players/users.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players / users

[Open](https://create.roblox.com/docs/players/users.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on users and scoped user IDs. Explains effective user IDs per domain (experience, group, OAuth app), pre- and post-rollout users, and how to use Datatype.User (Player.User, User.fromId, ToString/fromString) instead of raw numeric IDs for identity, data stores, and cross-domain references.

## Tips
- [page](https://create.roblox.com/docs/players/users) **[[data-persistence]]** Key data stores with player.User.Id within one game; numeric effective IDs are only unique per domain, so do not reuse them across games or apps.
- [page](https://create.roblox.com/docs/players/users) **[[data-persistence]]** When another domain (e.g. an OAuth moderation app) reads stored identity, store User:ToString() and restore with User.fromString(), not the bare integer, to avoid acting on the wrong user.
- [page](https://create.roblox.com/docs/players/users) **[[code-architecture-and-frameworks]]** Use Class.Player.User as the standard identifier in new code; Player.UserId and User.Id always match, so no branching is needed.
- [page](https://create.roblox.com/docs/players/users) **[[client-server-and-remotes]]** Use Class.Player for in-server actions (movement, GUI, teleport, chat, inventory) and Datatype.User for identity that outlives a session (data stores, Open Cloud, cross-game references).
- [page](https://create.roblox.com/docs/players/users) **[[matchmaking-and-teleport]]** Pass player.User (not UserId) to engine APIs like BadgeService:AwardBadge and Players:GetPlayerByUserId; both forms work but User is recommended.
- [page](https://create.roblox.com/docs/players/users) **[[analytics-metrics]]** Group in-game checks (IsInGroupAsync, GetRankInGroupAsync, GetRoleInGroupAsync, PromptJoinAsync) need no user ID handling; Open Cloud group APIs use the group's domain IDs.

## Numbers
- [page](https://create.roblox.com/docs/players/users) Scoped user ID example: **Pre-rollout user keeps global ID (e.g. 123); post-rollout users get different scoped IDs per game (500789, 302441)** (Same user gets different effective user IDs across games)

## Tools
Datatype.User, Class.Player.User, User.fromId, User:ToString, User.fromString, Open Cloud

## He points to
- Datatype.User reference
- Players service docs

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]] [[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
