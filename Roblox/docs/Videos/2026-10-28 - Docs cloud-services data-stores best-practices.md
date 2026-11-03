---
title: "Docs: cloud-services / data-stores / best-practices"
url: https://create.roblox.com/docs/cloud-services/data-stores/best-practices.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores / best-practices

[Open](https://create.roblox.com/docs/cloud-services/data-stores/best-practices.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on data store best practices: keep few data stores, one key per player under 4 MB, static key patterns, buffer data in memory, staggered and jittered retries, prefer UpdateAsync, shard hot keys for read throttling, operational workflow, data versioning, and right-to-be-forgotten processing.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Create fewer data stores and organize records by key, e.g. one PlayerData store rather than one data store per player.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Store each player's persistent data under one key (e.g. User_123456) when it fits the 4 MB object size limit. Reduces requests and allows atomic updates.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Split a player's record into a small number of deterministic keys only when parts have different access patterns or hit per-key size/throughput limits. Keep atomically-changed data together.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Build keys from stable identifiers like User_{UserId}. Never use display names or changeable values, so keys stay predictable and RTBF can find them.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Use key prefixes (e.g. User_123456/Profile/Warrior) to group related keys and list them with ListKeysAsync.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Don't use DataStore2 for new experiences. If you use it, migrate with Roblox's official beta DataStore2 migration tool.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Load player data at session start, keep a server-local copy, and save periodically, on leave, on server shutdown, and at critical checkpoints like purchases. Periodic save interval example: 180 seconds.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Keep the periodic save interval within request limits and shorter than any session-lock expiration.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[optimization-and-streaming]]** Stagger recurring requests: assign a random initial offset before fixed-frequency loops and add bounded random jitter to polling intervals.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Wrap data store calls in pcall and retry transient failures with capped exponential backoff plus random jitter. Don't retry invalid-request errors.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Process retries in order per key; an older retry landing after a newer successful write can overwrite newer data. Account for writes with unknown outcomes after a failed call.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Prefer UpdateAsync over SetAsync when writes depend on the current value or multiple servers may write the same key. Use SetAsync only for new keys or values independent of prior state.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[scripting-and-performance]]** Shard hot read keys only for per-key read throttling: store copies under fixed keys (e.g. Weather_1..3) and assign each server a shard by hashing its JobId. Does not fix write throttling.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** When polling shared sharded keys, add a random initial delay and bounded jitter between reads; avoid all servers reading immediately after a shared event.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Don't shard data that needs atomic updates across all readers or that is already below its per-key read throughput limit.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[analytics-metrics]]** Monitor requests, response status, throughput and storage in the Data Stores Observability Dashboard and set custom alerts for sustained failures or unexpected growth.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[analytics-metrics]]** Use Data Stores Manager to inspect stores, keys, storage and estimated costs. With more than 100 data stores, use Open Cloud or the Data Stores Batch Processor for size and key counts.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[scripting-and-performance]]** Rate-limit operational Open Cloud scripts; Open Cloud and game servers share the experience-level request budget.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Use data store versions instead of new keys per revision. Only the latest version counts toward storage, and versions allow inspection or restore.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Use MemoryStore for temporary, rapidly changing data; it expires automatically and doesn't add to persistent storage.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[data-persistence]]** Delete test data and data for expired events or retired features. Marked data stores can be restored within a 30-day buffer before permanent deletion.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) **[[age-ratings-moderation-and-tos]]** Configure automated right-to-be-forgotten processing for player data following static key patterns; use the right-to-erasure webhook only if your schema isn't supported, and verify all matching data is removed.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) Object size limit per key: **4 MB** (Max size for one-key-per-player persistent data)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) Example periodic save interval: **180 seconds** (Player data and purchasing sample; must be shorter than session-lock expiration)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) Data store count before size metrics hidden: **100** (Above 100 data stores, Data Stores list omits size and key counts)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) Deleted data store restore window: **30 days** (Buffer after marking a data store for deletion)

## Tools
Data Stores Observability Dashboard, Data Stores Manager, Data Stores Batch Processor, Open Cloud data store APIs, Extended Services, DataStore2 migration tool (beta)

## He points to
- Data store error codes and limits
- Retries
- Set vs update
- Data Stores Manager
- Stagger recurring requests

## Topics
[[age-ratings-moderation-and-tos]] [[analytics-metrics]] [[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
