---
title: "Docs: cloud-services / data-stores-vs-memory-stores"
url: https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores-vs-memory-stores

[Open](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs comparing cloud storage options: data stores (permanent, cross-server, NoSQL-style key-value and ordered), memory stores (up to 45 days, high-throughput temporary data like matchmaking and leaderboards), configs (read-only feature flags, ~5 min deploy), secrets stores (API keys), and in-memory Luau storage (single-server session).

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[data-persistence]]** Use DataStoreService for long-term data like user progress and inventory; it is consistent across all servers and places in the game.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[data-persistence]]** Use ordered data stores only for numeric permanent leaderboards; standard data stores store numbers, strings, booleans and tables but cannot be ranked.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[data-persistence]]** Standard data stores automatically keep previous versions of data for 30 days; ordered data stores do not keep version backups.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[data-persistence]]** Use MemoryStoreService for frequently updated temporary data such as matchmaking queues and daily/monthly leaderboards, not permanent progress.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[matchmaking-and-teleport]]** Use memory stores for skill-based matchmaking queues and match state in multiplayer games.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[ab-testing-and-experiments]]** Use configs for feature flags and tunable values (enemy health, weapon damage, item prices, event toggles) so you can change them live without restarting servers.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[updates-live-ops]]** Use configs to enable a new dungeon, disable a limited-time mode, or start a holiday event without a server restart; config changes take about five minutes to deploy.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[anti-exploit-and-security]]** Store API keys, passwords and access tokens in the secrets store, never in a data store, to avoid unnecessary security risk.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[scripting-and-performance]]** Use in-memory Luau tables for session-only values that change often (timers, counters, enemy health, status effects) to avoid external service call cost and latency.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[client-server-and-remotes]]** Cloud services are only accessible from server scripts; call data, memory, config and secrets APIs on the server, not the client.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[common-mistakes]]** Do not use memory stores for data that must persist beyond 45 days; their maximum lifetime is 45 days.
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) **[[common-mistakes]]** Do not use memory stores to frequently read a single key or partition; configs are more performant for that read-only case.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) Data store persistence: **Permanent** (DataStoreService data kept between sessions)
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) Standard data store version backup: **30 days** (Automatically manages previous versions)
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) Memory store maximum persistence: **45 days** (Data expires after this period)
- [page](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) Config deploy time: **5 minutes** (Changes to configs deploy over this period)

## Tools
DataStoreService, MemoryStoreService, Configs, Secrets store, Open Cloud APIs for data stores, Creator Hub, Roblox Studio

## He points to
- Data stores docs
- Ordered data stores docs
- Open Cloud APIs for data stores

## Topics
[[ab-testing-and-experiments]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[matchmaking-and-teleport]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
