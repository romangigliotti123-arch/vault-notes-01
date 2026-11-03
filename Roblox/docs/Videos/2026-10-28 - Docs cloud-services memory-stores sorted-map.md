---
title: "Docs: cloud-services / memory-stores / sorted-map"
url: https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / memory-stores / sorted-map

[Open](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox MemoryStoreService sorted map reference: creating maps, SetAsync/GetAsync/GetRangeAsync/UpdateAsync/RemoveAsync/GetSizeAsync, sort-key ordering rules, size limits, sharding, and bulk-deletion pattern.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) **[[scripting-and-performance]]** Wrap every MemoryStoreSortedMap call in pcall; these are async network calls that can fail occasionally.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) **[[combat-and-gameplay-systems]]** Use UpdateAsync rather than GetAsync+SetAsync for shared values written by multiple servers, so the callback reads the latest value and avoids lost updates.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) **[[data-persistence]]** Use sharding via key prefixes to split data that exceeds the 128-char key, 32 KB value, or sort-key limits, and to improve scalability.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) **[[data-persistence]]** Set expiration on every SetAsync/UpdateAsync; data auto-cleans after expiry, with a maximum of 3,888,000 seconds (45 days).
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) **[[scripting-and-performance]]** Delete a sorted map by paging GetRangeAsync in batches of 100 and calling RemoveAsync per key, using the last key as the exclusive lower bound.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) **[[scripting-and-performance]]** Remember sort order: numeric sort keys first, then string sort keys, then keys without sort key; ties break by key alphabetically.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) Key size limit: **128 characters**
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) Value size limit: **32 KB**
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) Sort key size limit: **128 characters**
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) Maximum expiration time: **3,888,000 seconds (45 days)**
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/sorted-map) Batch size used in bulk delete example: **100 items per GetRangeAsync**

## Tools
MemoryStoreService, MemoryStoreSortedMap

## He points to
- Roblox docs: Memory store sorted map

## Topics
[[combat-and-gameplay-systems]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
