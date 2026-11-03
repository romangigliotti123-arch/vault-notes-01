---
title: "Docs: tutorials / use-case-tutorials / data-storage / create-leaderboard"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / data-storage / create-leaderboard

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on building a custom global leaderboard with OrderedDataStores: saving gold scores via SetAsync, fetching sorted top scores with GetSortedAsync in a shared module, bridging to the client via RemoteFunction, and polling the UI every 3 seconds. Includes Studio API access setup.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[development-process-and-speed]]** Enable Studio Access to API Services (File > Experience Settings > Security) after publishing, or data store calls from Studio will fail.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[anti-exploit-and-security]]** Call DataStoreService only from server Scripts; data store access from the client is blocked and client-side access would let exploiters overwrite player data.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[data-persistence]]** Give each data store a unique name (e.g. GlobalLeaderboard) so stores don't overlap or conflict.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[data-persistence]]** Ordered data stores only accept string keys and numeric values; convert userIds with tostring() and read them back with tonumber().
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[data-persistence]]** Use GetOrderedDataStore for ranked numeric data; GetSortedAsync(false, limit) returns highest-first results across all servers.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[client-server-and-remotes]]** Put leaderboard fetch logic in a ModuleScript and expose it through a RemoteFunction so the client never touches the data store directly.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[code-architecture-and-frameworks]]** Store shared logic in a ModuleScript that returns its table so updates to sorting or name lookup apply to every caller from one place.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[client-server-and-remotes]]** Wrap InvokeServer and data store calls in pcall and return an empty table on failure so the UI loop does not crash.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[ui-ux-design]]** Clone a hidden template label for each row and use UIListLayout with LayoutOrder to keep leaderboard rows in order.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[optimization-and-streaming]]** Poll the leaderboard on a fixed interval (the tutorial uses 3 seconds) rather than on every frame to limit server requests.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[data-persistence]]** Expect a few seconds of delay on ordered data store leaderboards due to backend caching; use MemoryStore if you need real-time cross-server updates.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) **[[data-persistence]]** Save to the leaderboard store on player leave and on a periodic autosave (tutorial uses 30 seconds) so scores survive crashes.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) Leaderboard refresh interval: **3 seconds** (Client InvokeServer polling loop in LeaderboardGuiScript)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) Autosave interval: **30 seconds** (GoldManager autosave coroutine in the Gold Rush example)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) Displayed top scores: **3** (GetTopScores(3) limit used by the tutorial's leaderboard)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/create-leaderboard) Gold chunk value: **10 gold** (GOLD_VALUE constant in the Gold Rush example)

## Games
- **Gold Rush (tutorial sample game)**: Example game used to demonstrate gold collection feeding a global ordered-data-store leaderboard.

## Tools
Roblox Studio, DataStoreService, OrderedDataStore (GetSortedAsync, SetAsync), RemoteFunction, ModuleScript, MemoryStore (suggested for real-time updates)

## He points to
- Roblox Creator Docs: Create a custom leaderboard with ordered data stores

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]] [[development-process-and-speed]] [[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
