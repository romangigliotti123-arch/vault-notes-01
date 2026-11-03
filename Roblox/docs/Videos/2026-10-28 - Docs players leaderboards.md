---
title: "Docs: players / leaderboards"
url: https://create.roblox.com/docs/players/leaderboards.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players / leaderboards

[Open](https://create.roblox.com/docs/players/leaderboards.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on leaderboards: the PlayerList "Here" view uses leaderstats folders with value objects (IntValue etc.) for session stats, with ordering via IsPrimary/Priority; hiding via SetCoreGuiEnabled. Persistent "Friends"/"Global" views (beta) read from a registered OrderedDataStore with one numeric score per user ID, written server-side.

## Tips
- [page](https://create.roblox.com/docs/players/leaderboards) **[[scripting-and-performance]]** Name the folder exactly "leaderstats" in lowercase; Roblox silently skips the player from the leaderboard otherwise.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[analytics-metrics]]** Set stat values through .Value (e.g. gold.Value), not by assigning the object directly; stats must be IntValue/NumberValue/StringValue children of leaderstats.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[ui-ux-design]]** Use IsPrimary BoolValue (true) to put a stat first; if several are primary, Priority decides order. Non-prioritised stats default to priority 0.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[ui-ux-design]]** Hide the PlayerList with StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.PlayerList, false) from a client script during menus or cutscenes.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[client-server-and-remotes]]** Write leaderboard scores only from the server; the platform reads ordered data store scores but never writes them.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[data-persistence]]** Store one numeric score per player in the OrderedDataStore, keyed by user ID (or a consistent format containing it), before registering it in Creator Hub.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[data-persistence]]** Wrap SetAsync score writes in pcall and warn on failure so failed saves are visible during testing.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[anti-exploit-and-security]]** Validate score writes server-side and review suspicious or impossible values before they affect global rankings.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[data-persistence]]** Migrate scores from other backends into an ordered data store and update the scoring flow so new changes keep reaching it.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[updates-live-ops]]** Deactivating a leaderboard in Creator Hub hides it from players without deleting its data store or scores, so it can be reactivated later.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[testing-debugging-and-qa]]** If a player or score is missing from Friends/Global, check the data store name, numeric value, key format, and that the leaderboard configuration is active.
- [page](https://create.roblox.com/docs/players/leaderboards) **[[testing-debugging-and-qa]]** Test Friends and Global with accounts that already have saved scores, then update a score server-side and confirm the board reflects it.

## Numbers
- [page](https://create.roblox.com/docs/players/leaderboards) Persistent leaderboard limit: **1 active persistent leaderboard per experience (beta)** (Only one registered, active leaderboard shows in Friends/Global)
- [page](https://create.roblox.com/docs/players/leaderboards) Default stat priority: **0** (Stats without a Priority child; higher Priority appears earlier)

## Tools
Creator Hub, PlayerList, leaderstats, OrderedDataStore, DataStoreService

## He points to
- Ordered data stores documentation

## Topics
[[analytics-metrics]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[data-persistence]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[ui-ux-design]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
