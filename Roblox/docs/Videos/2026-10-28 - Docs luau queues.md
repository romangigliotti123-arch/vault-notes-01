---
title: "Docs: luau / queues"
url: https://create.roblox.com/docs/luau/queues.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / queues

[Open](https://create.roblox.com/docs/luau/queues.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on queues. Covers regular FIFO queues and priority queues, the built-in MemoryStoreService queue, and a Luau table-based regular queue implementation (new/enqueue/dequeue/isEmpty) to store in ReplicatedStorage as a ModuleScript.

## Tips
- [page](https://create.roblox.com/docs/luau/queues) **[[scripting-and-performance]]** Use a table-based queue (head/tail indices, nil out dequeued slots) for custom scheduling or request handling instead of table.remove from the front.
- [page](https://create.roblox.com/docs/luau/queues) **[[code-architecture-and-frameworks]]** Store a shared queue implementation as a ModuleScript in ReplicatedStorage so client and server use the same code.
- [page](https://create.roblox.com/docs/luau/queues) **[[matchmaking-and-teleport]]** Use priority queues for matchmaking and raise the priority of players who have waited longer so they are served first.
- [page](https://create.roblox.com/docs/luau/queues) **[[data-persistence]]** MemoryStoreService queues are non-persistent; use them for transient work, not for saving player data.
- [page](https://create.roblox.com/docs/luau/queues) **[[scripting-and-performance]]** Set priority above the current highest value to place an item at the front; equal priority items queue behind existing ones.

## Numbers
- [page](https://create.roblox.com/docs/luau/queues) Default priority: **0 for items at the back of a priority queue** (Priority queue back item default, per docs example)
- [page](https://create.roblox.com/docs/luau/queues) Example highest priority: **5 at front of queue** (Docs example queue; new item priority 3 goes behind items of 3 or more)
- [page](https://create.roblox.com/docs/luau/queues) Priority needed to jump to front: **6 or higher** (In docs example where current highest set priority is 5)

## Tools
MemoryStoreService, ModuleScript, ReplicatedStorage

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[matchmaking-and-teleport]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
