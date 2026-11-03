---
title: "Docs: scripting / transparent-batching"
url: https://create.roblox.com/docs/scripting/transparent-batching.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / transparent-batching

[Open](https://create.roblox.com/docs/scripting/transparent-batching.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox scripting doc on transparent batching: the engine merges concurrent calls to supported APIs (MarketplaceService, AvatarEditorService, AssetService) into fewer HTTP requests. Explains serial vs concurrent calling patterns, supported methods, and best practices.

## Tips
- [page](https://create.roblox.com/docs/scripting/transparent-batching) **[[scripting-and-performance]]** Start calls to the same supported API concurrently (task.spawn per item) rather than awaiting one at a time; the engine batches them into fewer HTTP requests.
- [page](https://create.roblox.com/docs/scripting/transparent-batching) **[[scripting-and-performance]]** Start batched calls close together in time; calls started much later fall into a separate batch.
- [page](https://create.roblox.com/docs/scripting/transparent-batching) **[[anti-exploit-and-security]]** Wrap network-bound API calls in pcall() so one failed request does not abort the whole operation.
- [page](https://create.roblox.com/docs/scripting/transparent-batching) **[[scripting-and-performance]]** Do not manually group requests or tune batch sizes; the engine picks the batching strategy automatically.
- [page](https://create.roblox.com/docs/scripting/transparent-batching) **[[scripting-and-performance]]** Rely on built-in caching: repeated requests for the same data return from cache instead of making a new network call.
- [page](https://create.roblox.com/docs/scripting/transparent-batching) **[[scripting-and-performance]]** Batching only applies when the same supported method is called concurrently; serial waiting on each call sends one HTTP request per call and risks rate limits.

## Numbers
- [page](https://create.roblox.com/docs/scripting/transparent-batching) Example batching reduction: **20 concurrent product lookups can batch into 1-2 HTTP requests instead of 20** (Doc example of transparent batching effect on MarketplaceService calls)

## Tools
MarketplaceService:GetProductInfoAsync, MarketplaceService:UserOwnsGamePassAsync, AvatarEditorService:GetItemDetailsAsync, AssetService:GetBundleDetailsAsync, task.spawn, pcall

## Topics
[[anti-exploit-and-security]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
