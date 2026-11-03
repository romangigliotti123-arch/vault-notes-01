---
title: "Docs: cloud-services / data-stores / error-codes-and-limits"
url: https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores / error-codes-and-limits

[Open](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on data store limits: request queues (30-request cap), data size (4 MB per key), metadata limits, per-key throughput (4 MB/min write, 25 MB/min read), experience-level and server-level request budgets, storage formula (500 MB + 1 MB per lifetime user), Open Cloud rate limiting approaches, and the error code reference.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[data-persistence]]** Wrap all data store calls in pcall; failed writes may still have succeeded on the backend, so verify with a fresh read before retrying.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[data-persistence]]** Store data uncompressed; data stores compress automatically, and pre-compression adds CPU overhead and reduces built-in compression effectiveness.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[data-persistence]]** Check serialized value size with HttpService:JSONEncode() before saving; each key is capped at 4,194,304 characters.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[data-persistence]]** Keep data store names, key names and scopes under 50 characters each; check with string.len().
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[optimization-and-streaming]]** Limit writes per key: per-key throughput caps at 4 MB per minute for writes and 25 MB per minute for reads, rounded up per request to the next KB.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[scripting-and-performance]]** Use UpdateAsync rather than blind SetAsync for shared data; it consumes both read and write budgets, so count it twice.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[scripting-and-performance]]** Call DataStoreService:GetRequestBudgetForRequestType() before issuing requests to confirm the current server's available budget.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[scripting-and-performance]]** Use SetRateLimitForRequestType() to cap each server's share of the shared experience budget when also using Open Cloud.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[anti-exploit-and-security]]** Open Cloud and in-experience requests share one budget; throttle Open Cloud scripts independently so they don't starve live players.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[data-persistence]]** Plan storage: limit is 500 MB + 1 MB per lifetime user (anyone who has joined once); only latest key versions count toward usage.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[common-mistakes]]** Don't test rate limits in Studio Run mode; it uses lower static limits. Use Studio Team Create instead.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[data-persistence]]** Handle throttle codes 301-306 (queue full, request dropped) and KeyThrottled/DatastoreThrottled by backing off and retrying.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[optimization-and-streaming]]** For Open Cloud loops, add a delay of 60 / (desired requests per minute) seconds, or use a leaky bucket limiter for bursts.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) **[[data-persistence]]** Limit metadata: 50-char key names, 250-char values, 300 characters total for key-value pairs.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Queue limit: **30 requests per queue (set, ordered set, get, ordered get)**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Max value size per key: **4,194,304 characters serialized**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Name/key/scope max length: **50 characters**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Per-key throughput: **Read 25 MB/min; write 4 MB/min**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Storage limit formula: **500 MB + 1 MB × lifetime users**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Standard read budget (experience): **300 + concurrentUsers × 40 per minute**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Standard write budget (experience): **300 + concurrentUsers × 20 per minute**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Standard list budget (experience): **300 + concurrentUsers × 2 per minute**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Ordered write budget (experience): **300 + concurrentUsers × 20 per minute**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Default server standard read/write: **60 + numPlayers × 40 per minute**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Default server ordered write: **30 + numPlayers × 5 per minute**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Metadata limits: **Key 50 chars; value 250 chars; total 300 chars**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Throughput rounding: **Rounded up to next KB per request**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Page size range (ordered): **1 to 100**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) GetVersionAtTimeAsync timestamp: **Positive and at most 10 minutes in future**
- [page](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) Deleted store storage retention: **30-day deletion processing period counts toward storage**

## Tools
DataStoreService, HttpService:JSONEncode, Open Cloud Data Store APIs

## He points to
- Control rate limits documentation
- Roblox Open Cloud API (apis.roblox.com/cloud/v2)

## Topics
[[anti-exploit-and-security]] [[common-mistakes]] [[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
