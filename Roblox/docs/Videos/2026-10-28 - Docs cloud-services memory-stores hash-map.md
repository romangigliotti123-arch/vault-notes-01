---
title: "Docs: cloud-services / memory-stores / hash-map"
url: https://create.roblox.com/docs/cloud-services/memory-stores/hash-map.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / memory-stores / hash-map

[Open](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs for Memory Store hash maps: key-value storage for cached, shared, fast-access data. Covers limits, SetAsync/GetAsync/ListItemsAsync/UpdateAsync/RemoveAsync usage, concurrent-safe updates via UpdateAsync, and deleting all data via paginated listing.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) **[[scripting-and-performance]]** Wrap all MemoryStore calls in pcall; they are async network calls that can occasionally fail.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) **[[data-persistence]]** Use hash maps for simple caching and shared state (e.g. shared inventories, auction houses) when you have more than 1,000 keys; use sorted maps for smaller key spaces.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) **[[data-persistence]]** Use UpdateAsync rather than GetAsync+SetAsync for shared values modified by multiple servers; it reads the latest value before writing, so concurrent contributions aren't lost.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) **[[data-persistence]]** Always set an expiration time on SetAsync/UpdateAsync so memory is cleaned up automatically; the maximum is 3,888,000 seconds (45 days).
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) **[[scripting-and-performance]]** Return nil from an UpdateAsync callback to abort the update; contention triggers automatic retries until success, nil, or max retries (then a conflict is returned).
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) **[[data-persistence]]** To wipe a hash map, page through ListItemsAsync and call RemoveAsync per key; there is no single bulk delete call.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) Key size limit: **128 characters** (Hash map key size limit)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) Value size limit: **32 KB** (Hash map value size limit)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) Max expiration time: **3,888,000 seconds (45 days)** (Maximum SetAsync/UpdateAsync expiration)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/hash-map) Recommended threshold for hash maps: **More than 1,000 keys** (Below this, docs recommend sorted maps instead)

## Tools
MemoryStoreService, MemoryStoreHashMap

## He points to
- Class.MemoryStoreHashMap
- Class.MemoryStoreService

## Topics
[[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
