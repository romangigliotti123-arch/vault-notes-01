---
title: "Docs: matchmaking / customize-matchmaking"
url: https://create.roblox.com/docs/matchmaking/customize-matchmaking.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: matchmaking / customize-matchmaking

[Open](https://create.roblox.com/docs/matchmaking/customize-matchmaking.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on customizing matchmaking: adjust weights of built-in Roblox signals, or create custom signals from custom player/server attributes (max 2 signals, 5 player + 5 server attributes per game), preview scores with mock servers, and apply configurations to places.

## Tips
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) **[[matchmaking-and-teleport]]** Start from the default Roblox signals and only adjust their weights before creating custom signals; this is the simplest matchmaking configuration.
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) **[[matchmaking-and-teleport]]** Create custom attributes before custom signals; custom signals read player and server data through attributes.
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) **[[matchmaking-and-teleport]]** Use Preview and Test to check which mock server wins and hover signal scores to inspect formulas before applying a configuration to live places.
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) **[[matchmaking-and-teleport]]** Use Average or Median aggregation to match a joining player to the server's typical player attribute; use Sum to target a total value across the server.
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) **[[matchmaking-and-teleport]]** Use Cluster for categorical attributes to group players with the same value (e.g. same mode preference); use Diversify to mix different values.
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) **[[data-persistence]]** Player attributes read from DataStores: set the data store, key template using {UserId}, value path into the JSON object, and scope (defaults to global).

## Numbers
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) Custom signals per game: **2** (Hard limit on custom signals per game)
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) Custom attributes per game: **5 server and 5 player** (Hard limit per game for custom attributes)
- [page](https://create.roblox.com/docs/matchmaking/customize-matchmaking) Mock servers in preview: **3** (Preview shows three mock servers and highlights the winner)

## Tools
Roblox Creator Dashboard, Custom Matchmaking configuration page

## He points to
- Existing signals
- Custom signals
- Custom attributes
- Scoring

## Topics
[[data-persistence]] [[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
