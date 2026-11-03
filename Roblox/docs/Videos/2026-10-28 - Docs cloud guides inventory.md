---
title: "Docs: cloud / guides / inventory"
url: https://create.roblox.com/docs/cloud/guides/inventory.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / inventory

[Open](https://create.roblox.com/docs/cloud/guides/inventory.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Cloud Inventory API docs: checking whether a user owns specific asset IDs, filtering inventory results (collectibles, asset types, badges, passes, private servers), and paginating correctly when nextPageToken is non-empty but the page is empty.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/inventory) **[[scripting-and-performance]]** Use the filter parameter with comma-separated assetIds to check ownership of several items in one request instead of one call per item.
- [page](https://create.roblox.com/docs/cloud/guides/inventory) **[[scripting-and-performance]]** Combine filters with semicolons (e.g. onlyCollectibles=true;inventoryItemAssetTypes=HAT) to narrow results server-side.
- [page](https://create.roblox.com/docs/cloud/guides/inventory) **[[scripting-and-performance]]** When paginating, check both a non-empty nextPageToken and a non-empty inventoryItems array; a divisible result count can yield an empty final page with a token.
- [page](https://create.roblox.com/docs/cloud/guides/inventory) **[[client-server-and-remotes]]** Inventory API calls need an API key (x-api-key header) or OAuth 2 configured before use; most calls need no special permissions, but some filters require Inventory read permissions.

## Tools
Roblox Open Cloud Inventory API

## He points to
- Roblox Open Cloud docs: Filtering
- Roblox Open Cloud docs: Pagination

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
