---
title: "Docs: cloud-services / data-stores"
url: https://create.roblox.com/docs/cloud-services/data-stores.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores

[Open](https://create.roblox.com/docs/cloud-services/data-stores.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on DataStoreService: enabling Studio access, getting stores, SetAsync/UpdateAsync/GetAsync/IncrementAsync/RemoveAsync, metadata and user IDs, ordered data stores with GetSortedAsync and BatchGetAsync, and read/write limit implications.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Wrap every DataStore call (SetAsync, GetAsync, UpdateAsync, etc.) in pcall; these are network calls that can occasionally fail.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Use UpdateAsync instead of SetAsync when multiple servers may write the same key; SetAsync can cause inconsistency but only counts against write limit.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Never yield inside UpdateAsync callbacks; returning nil cancels the write.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Access DataStores only from server Scripts; LocalScript access errors.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Do not enable Studio API access on live games; use a separate test version to avoid overwriting production data.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Always pass a metadata value when calling SetAsync, IncrementAsync or UpdateAsync, even if unchanged, or the current value is lost.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Use memory stores for temporary data that is accessed or updated frequently.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Use IncrementAsync for integer counters instead of manual UpdateAsync increments.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Use GetOrderedDataStore for sorted persistent leaderboard data; default stores do not sort.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** Confirm a key exists in BatchGetAsync results; missing keys are omitted. Each key counts as one read request.
- [page](https://create.roblox.com/docs/cloud-services/data-stores) **[[data-persistence]]** GetAsync values can be stale due to caching; see the disabling caching section if fresh reads are required.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores) BatchGetAsync read cost: **1 read request per key** (Each key in a batch call counts against ordered data store read limit)
- [page](https://create.roblox.com/docs/cloud-services/data-stores) UpdateAsync cost: **Counts against read and write limits** (Reads before writing, slower than SetAsync)
- [page](https://create.roblox.com/docs/cloud-services/data-stores) SetAsync cost: **Counts against write limit only** (Quick writes without read)
- [page](https://create.roblox.com/docs/cloud-services/data-stores) Pagination request limit: **Equal to ordered store page size** (AdvanceToNextPageAsync uses the page size set on the store)

## Tools
DataStoreService, Data Stores Manager (Creator Hub), Open Cloud APIs for data stores, Memory stores

## He points to
- Disabling caching (docs)
- Metadata limits (docs)
- Memory stores (docs)
- Open Cloud APIs for data stores (docs)

## Topics
[[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
