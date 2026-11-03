---
title: "Docs: cloud / guides / data-stores"
url: https://create.roblox.com/docs/cloud/guides/data-stores.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / data-stores

[Open](https://create.roblox.com/docs/cloud/guides/data-stores.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud docs for data stores: how external tools (support portals, external leaderboards, schema migrations) access standard and ordered data stores via HTTP. Covers differences from the Engine API (universe ID, separate create/update permissions, manual JSON serialization), non-finite number tagging, required API key scopes, and Node.js/Python examples.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) **[[data-persistence]]** Open Cloud data store endpoints require you to serialize data to JSON yourself; the Engine API does this automatically.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) **[[anti-exploit-and-security]]** Create API keys with only the scopes needed and restrict by data store, IP address, and expiration date.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) **[[anti-exploit-and-security]]** Grant separate create and update scopes; a support tool may only need to edit existing entries, not create new ones.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) **[[data-persistence]]** Handle non-finite numbers (inf, -inf, nan) from Engine-written entries; they come back as tagged JSON objects, not plain numbers.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) **[[optimization-and-streaming]]** For large data stores, paginate list requests using maxPageSize and pageToken query parameters rather than fetching all entries at once.
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) **[[client-server-and-remotes]]** Keep Open Cloud data-writing scripts out of client code; API keys must stay server-side, read from environment variables.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) Example page size: **first 10 entries** (Support portal example processes only the first 10 entries before pagination)
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) Example increment: **+10 currency per entry** (Inventory increment example adds 10 to currency field)
- [page](https://create.roblox.com/docs/cloud/guides/data-stores) Sample random score range: **1 to 50** (Leaderboard example random values for sample ordered entries)

## Tools
Open Cloud APIs (apis.roblox.com/cloud/v2), Node.js, Python requests

## He points to
- Manage API keys (Roblox docs)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[data-persistence]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
