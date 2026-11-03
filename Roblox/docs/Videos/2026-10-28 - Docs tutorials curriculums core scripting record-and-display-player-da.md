---
title: "Docs: tutorials / curriculums / core / scripting / record-and-display-player-data"
url: https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / scripting / record-and-display-player-data

[Open](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial: builds a PlayerData ModuleScript in ServerStorage to store per-player coin counts keyed by UserId, a Leaderboard module that creates a leaderstats folder with IntValue stats, and wires both into CoinService so collected coins update the on-screen leaderboard.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) **[[code-architecture-and-frameworks]]** Put shared data and leaderboard logic in ModuleScripts in ServerStorage so multiple server scripts require the same table instead of duplicating state.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) **[[code-architecture-and-frameworks]]** Expose simple public functions (getValue, updateValue) and keep the heavy lifting in local helper functions.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) **[[scripting-and-performance]]** Use FindFirstChild to check whether an object exists before using it; it returns nil instead of erroring.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) **[[analytics-metrics]]** Create leaderstats as a Folder under each Player with IntValue/NumberValue/StringValue children so Roblox automatically renders the default leaderboard UI.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) **[[data-persistence]]** The sample stores data only in a Lua table in memory, so values reset when the server stops; use DataStores for persistence.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) **[[client-server-and-remotes]]** Keep coin data and leaderboard updates on the server; the CoinService touch handler runs server-side and validates the player from the character.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) Coin cooldown: **10 seconds before a coin re-enables** (Tutorial CoinService COOLDOWN constant)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data) Coins added per pickup: **1** (Tutorial COIN_AMOUNT_TO_ADD constant)

## Tools
Roblox Studio, ModuleScript, Folder/IntValue leaderstats, Explorer

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
