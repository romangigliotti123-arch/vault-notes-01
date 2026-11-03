---
title: "Docs: cloud-services / memory-stores / queue"
url: https://create.roblox.com/docs/cloud-services/memory-stores/queue.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / memory-stores / queue

[Open](https://create.roblox.com/docs/cloud-services/memory-stores/queue.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on MemoryStoreQueue: creating queues with GetQueue, adding items with expiration and priority, reading with invisibility timeout, removing processed items, and checking queue size. Covers FIFO and priority queues and their use for matchmaking and cross-server user ordering.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) **[[data-persistence]]** Wrap all MemoryStore calls (AddAsync, ReadAsync, RemoveAsync, GetSizeAsync) in pcall, since they are async network calls that can fail.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) **[[matchmaking-and-teleport]]** Use memory store queues as a centralized, cross-server store for matchmaking order, then teleport matched users to the main place.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) **[[scripting-and-performance]]** Call RemoveAsync immediately after finishing processing read items so the same item is never processed twice.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) **[[scripting-and-performance]]** Set the invisibility timeout longer than your expected read-and-remove duration; items reappear for processing after it elapses if not removed.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) **[[scripting-and-performance]]** In processing loops, add task.wait(1) after a failed ReadAsync to avoid hammering the service on errors.
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) **[[matchmaking-and-teleport]]** Use a lobby place as the start place, storing user info in queues accessible by multiple servers before teleporting to the main place.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) Default invisibility timeout: **30 seconds** (Applied to GetQueue when no timeout is passed)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) Default GetSizeAsync excludeInvisible: **false** (Invisible items are counted unless set to true)
- [page](https://create.roblox.com/docs/cloud-services/memory-stores/queue) Default AddAsync priority: **0 (FIFO)** (Leaving priority empty or 0 keeps FIFO order)

## Tools
MemoryStoreService, MemoryStoreQueue

## He points to
- Roblox docs: MemoryStoreService:GetQueue
- Roblox docs: MemoryStoreQueue:AddAsync / ReadAsync / RemoveAsync / GetSizeAsync

## Topics
[[data-persistence]] [[matchmaking-and-teleport]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
