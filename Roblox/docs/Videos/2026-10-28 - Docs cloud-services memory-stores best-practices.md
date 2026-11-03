---
title: "Docs: cloud-services / memory-stores / best-practices"
url: https://create.roblox.com/docs/cloud-services/memory-stores/best-practices.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / memory-stores / best-practices

[Open](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs best practices for MemoryStoreService: key/structure design, expiration, UpdateAsync, staggering, monitoring quotas, managing sorted map/queue limits, and sharding sorted maps, queues, and hash maps to avoid throttling.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[scripting-and-performance]]** Apply static key patterns and prefixes to both keys and data structure names so every server routes the same logical data to the same location.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[data-persistence]]** Choose expiration times matching how long data stays useful. Don't use memory stores for persistent player records or data that must survive expiration.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[client-server-and-remotes]]** Prefer UpdateAsync over SetAsync (MemoryStoreHashMap/SortedMap:UpdateAsync) to avoid overwriting concurrent changes.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[optimization-and-streaming]]** Stagger recurring requests and retry transient failures to reduce throttling.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[analytics-metrics]]** Monitor quota usage, request volume and response statuses in the Memory Store Observability Dashboard; set custom alerts and use the Error Report.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[optimization-and-streaming]]** Reduce requests, item sizes and expiration times before increasing capacity; evaluate Extended Services only if legitimate usage exceeds default quotas.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[optimization-and-streaming]]** When sorted map or queue hits item or memory limits, remove items manually or add expiration; if only memory is throttling, shrink keys and values.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[optimization-and-streaming]]** Sorted maps and queues live on a single partition; if throughput throttles, sharding is the only solution.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[scripting-and-performance]]** Shard sorted maps by assigning each user Id to one of N maps via modulo (userId % N + 1) using a helper function.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[scripting-and-performance]]** Shard queues with a revolving pattern: multiple queues, rotate read and add pointers; adds, reads and removes only occur at queue front/back.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[optimization-and-streaming]]** Hash maps auto-shard but a single nested metadata key concentrates load on one partition; store each independently accessed field as its own key with a prefix.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) **[[optimization-and-streaming]]** If many servers read one hash map key, copy the value to multiple keys and route each server to a stable shard to avoid partition throttling.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) Sharded sorted map example: **4 maps, routed by userId % 4** (Example shard count for player records in sorted maps)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices) Example expiration in sorted map SetAsync: **600 seconds** (Example TTL used when initializing player values)

## Tools
MemoryStoreService, Memory Store Observability Dashboard, Error Report, Extended Services

## He points to
- Best practices for data stores
- Data stores versus memory stores

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
