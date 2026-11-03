---
title: "Advanced Roblox Studio Tutorial: Memory Stores (MemoryStoreService)"
url: https://youtu.be/EpF5oWNS-Pk
creator: XTB7
official: false
advice_density: medium
date: 2023-10-31
views: 8433
transcript: auto-captions
confidence: medium
tags: [roblox, xtb7-dev, youtube-learn]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Advanced Roblox Studio Tutorial: Memory Stores (MemoryStoreService)

[Watch](https://youtu.be/EpF5oWNS-Pk) | xtb7-dev | 8,433 views | 2023-10-31

## Summary
Tutorial on MemoryStoreService in Roblox Studio, covering its two real data structures: queues (ordered arrays with priority, read via ReadAsync-style calls with an identifier for removal) and sorted/hash maps (key-value stores with expirations and UpdateAsync). Explains memory stores are faster than DataStores but have a 45-day max expiration, suited to rapidly changing data like matchmaking queues. Server-only access.

## Tips
- [0:00](https://youtu.be/EpF5oWNS-Pk?t=0) **[[data-persistence]]** Use MemoryStore for rapidly changing data like matchmaking queues; it is faster than DataStore but data expires (max 45 days).
- [0:00](https://youtu.be/EpF5oWNS-Pk?t=0) **[[client-server-and-remotes]]** MemoryStoreService can only be accessed from the server, so call it from a server Script only.
- [1:15](https://youtu.be/EpF5oWNS-Pk?t=75) **[[data-persistence]]** Set an expiration on every queue item and map entry; maximum is 3,888,000 seconds (45 days).
- [2:38](https://youtu.be/EpF5oWNS-Pk?t=158) **[[data-persistence]]** Publish the place before testing MemoryStore calls; unpublished places return errors.
- [2:38](https://youtu.be/EpF5oWNS-Pk?t=158) **[[data-persistence]]** Use a higher numeric priority to place items later in a queue; equal priority returns in insertion order.
- [1:56](https://youtu.be/EpF5oWNS-Pk?t=116) **[[data-persistence]]** Set AllOrNothing to true when you need an exact count from a queue; default false returns fewer items if fewer exist.
- [3:40](https://youtu.be/EpF5oWNS-Pk?t=220) **[[data-persistence]]** Use UpdateAsync with a transform function when the new value depends on the current value, to avoid overwriting concurrent changes.
- [8:26](https://youtu.be/EpF5oWNS-Pk?t=506) **[[scripting-and-performance]]** Wrap all MemoryStore async calls in pcall in production; they fail more often than DataStore calls.

## Numbers
- [0:00](https://youtu.be/EpF5oWNS-Pk?t=0) Max expiration: **3,888,000 seconds (45 days)** (Maximum time an item can persist in a MemoryStore structure)
- [1:15](https://youtu.be/EpF5oWNS-Pk?t=75) Expiration unit: **seconds** (Expiration argument for queue add and map set calls)

## Tools
Roblox Studio, MemoryStoreService

## He points to
- Roblox creator documentation (MemoryStore)

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[xtb7-dev - How to make successful Roblox games]]
