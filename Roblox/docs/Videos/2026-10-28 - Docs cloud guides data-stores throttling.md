---
title: "Docs: cloud / guides / data-stores / throttling"
url: https://create.roblox.com/docs/cloud/guides/data-stores/throttling.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / data-stores / throttling

[Open](https://create.roblox.com/docs/cloud/guides/data-stores/throttling.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on Data Store throttling for Open Cloud v1 endpoints. Explains two limit types (requests per minute and throughput per universe, not scaled by user count) and lists per-minute limits for legacy standard and ordered data store read/write/delete operations. Exceeding either returns 429.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) **[[data-persistence]]** Data Store limits are per universe, shared across all API keys; using more keys does not raise the limit.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) **[[scripting-and-performance]]** Exceeding requests/minute or throughput returns HTTP 429 Too Many Requests; batch or reduce writes and reads to stay under limits.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) **[[data-persistence]]** Data store limits do not scale with player count, unlike Engine API limits; plan save frequency with fixed per-minute budgets.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) **[[data-persistence]]** Legacy v1 limits apply only to /datastores/v1 and /ordered-data-stores/v1 endpoints; check Open Cloud v2 docs for v2 limits.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) Standard data store write throughput: **10 MB/minute/universe** (Legacy /datastores/v1 write operations)
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) Standard data store read throughput: **20 MB/minute/universe** (Legacy /datastores/v1 read operations)
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) Standard data store requests: **300 requests/minute/universe** (Write, read and delete operations, legacy v1)
- [page](https://create.roblox.com/docs/cloud/guides/data-stores/throttling) Ordered data store requests: **300 requests/minute/universe** (Write and read operations, legacy ordered v1)

## Tools
Open Cloud Data Stores API v1

## He points to
- Data store error codes and limits (Open Cloud v2 rate limits)

## Topics
[[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
