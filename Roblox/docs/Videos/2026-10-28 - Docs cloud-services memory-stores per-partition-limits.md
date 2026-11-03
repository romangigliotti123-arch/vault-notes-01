---
title: "Docs: cloud-services / memory-stores / per-partition-limits"
url: https://create.roblox.com/docs/cloud-services/memory-stores/per-partition-limits.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / memory-stores / per-partition-limits

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud-services/memory-stores/per-partition-limits.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on MemoryStores partitions. Sorted maps and queues each live on a single partition; hash maps are spread automatically across many partitions. Points to Per-partition limits and best practices for spreading load.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/per-partition-limits) **[[data-persistence]]** Sorted maps and queues each occupy a single partition, so heavy traffic on one of them shares that partition's limits. Use hash maps when you need throughput spread across partitions.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/per-partition-limits) **[[data-persistence]]** Hash map items are distributed across partitions automatically, so spreading load across many keys helps. Check Per-partition limits and best practices before designing high-volume memory stores.

## Topics
[[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
