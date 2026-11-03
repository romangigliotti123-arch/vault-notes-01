---
title: "Docs: cloud-services / memory-stores"
url: https://create.roblox.com/docs/cloud-services/memory-stores.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / memory-stores

[Open](https://create.roblox.com/docs/cloud-services/memory-stores.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on MemoryStoreService: three data structures (sorted map, queue, hash map), their use cases, memory/request/size quotas, per-partition and per-key throttling, quota recovery (Open Cloud flush, Extended Services), best practices, status codes, and Studio testing behaviour.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[scripting-and-performance]]** Use a hash map when you need key-based access; use a sorted map for ordering; use a queue for ordered FIFO processing.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[data-persistence]]** Use memory stores only for ephemeral, rapidly changing data; use data stores for anything that must persist across sessions.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Cache values on the server and recheck after an interval (e.g. 30 s) to reduce request volume.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Shard sorted maps/queues by prefix or user ID digits, and shard hot hash map keys with multiple copies, to spread load across partitions.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Batch requests where possible and apply exponential backoff on throttling or DataUpdateConflict responses.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Remove processed items explicitly with RemoveAsync; treat expiration as a safety net, not the primary cleanup.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Set expiration to the shortest practical time when adding data; the default is 45 days, which can exhaust memory quota.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Store only necessary values, e.g. keep just the highest bid in one key instead of all bids.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Compress stored values (e.g. LZW) and keep values under the 32 KB item size limit by splitting across keys.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[common-mistakes]]** Do not design against per-partition limits as fixed numbers; they are estimates set on the backend and may change.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[common-mistakes]]** Flushing memory stores with Open Cloud clears all queues, sorted maps and hash maps in the scope, including live matchmaking or trading data. Flush only if the game can run without it.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[testing-debugging-and-qa]]** Test memory stores in Studio before production; Studio data is isolated, but Studio has the same limits and slightly higher latency.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[optimization-and-streaming]]** Monitor the Observability dashboard (Memory Usage chart, Request Count by Status) and confirm Success responses outnumber NoItemFound responses.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) **[[monetisation-other]]** If you must retain more data than the default quota allows, enable Extended Services for memory stores and set monthly budgets; usage beyond budget is throttled.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Memory size quota: **64 KB + 1.2 KB × number of users** (Game-level quota; grows with users immediately, shrinks only after 8-day traceback)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Request unit quota: **1000 + 120 × concurrent users per minute** (Game-level, applies to all MemoryStoreService calls)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Per-partition throttling: **~30,000 request units/min (estimate)** (Sorted maps and queues sit on one partition; hash maps spread across partitions)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Hash map per-key limits: **~5,000 write RU/min; ~15,000 read RU/min** (Applies on top of per-partition limit to single-key operations)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Data structure item limit: **1,000,000 items** (Per sorted map or queue)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Data structure size limit: **100 MB** (Per sorted map or queue, including keys for sorted maps)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Max item value size: **32 KB** (ItemValueSizeTooLarge above this)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Default expiration: **45 days** (For queue AddAsync and sorted map SetAsync; set shorter)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Data structure request limit (status doc): **100,000 request units/min** (DataStructureRequestsOverLimit threshold per observability table)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Queue ReadAsync cost: **+1 unit every 2 seconds while reading** (Plus one unit per returned item)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) HashMap UpdateAsync cost: **minimum 2 request units** (Counts against both read and write per-key limits)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Max expiration time (client validation): **0 to 3,888,000 seconds** (InvalidExpirationTime range (45 days))
- [page](https://create.roblox.com/docs/cloud-services/memory-stores) Suggested cache recheck interval: **30 seconds** (Example local cache interval in troubleshooting)

## Tools
MemoryStoreService, Open Cloud Flush Memory Store endpoint, Observability Dashboard, Developer Console, Creator Dashboard Extended Services

## He points to
- Recover from memory quota exhaustion
- Troubleshooting
- Enable a service
- Service pricing
- Developer Forum

## Topics
[[common-mistakes]] [[data-persistence]] [[monetisation-other]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
