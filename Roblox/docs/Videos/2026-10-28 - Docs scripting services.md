---
title: "Docs: scripting / services"
url: https://create.roblox.com/docs/scripting/services.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / services

[Open](https://create.roblox.com/docs/scripting/services.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on services: the standard pattern (get services, require modules, add local functions, connect events), container vs scripting vs cloud services, and data model inspection methods. Emphasises caching services once per script and using WaitForChild for load-order safety.

## Tips
- [page](https://create.roblox.com/docs/scripting/services) **[[code-architecture-and-frameworks]]** Follow the core pattern: get services, require module scripts, add local functions, then connect the events that trigger them.
- [page](https://create.roblox.com/docs/scripting/services) **[[luau-language-and-types]]** Retrieve each service only once per script and name the variable after the service, e.g. local Players = game:GetService("Players"). Applies to module scripts too.
- [page](https://create.roblox.com/docs/scripting/services) **[[client-server-and-remotes]]** Use WaitForChild() on replicated content because Roblox does not guarantee load order and instance streaming changes what is loaded.
- [page](https://create.roblox.com/docs/scripting/services) **[[data-persistence]]** Use DataStoreService for persistent cross-session data, MemoryStoreService for frequent ephemeral data, and MessagingService for cross-server communication.
- [page](https://create.roblox.com/docs/scripting/services) **[[code-architecture-and-frameworks]]** Put shared logic in ReplicatedStorage and ReplicatedFirst, since these containers replicate content and logic between server and client.
- [page](https://create.roblox.com/docs/scripting/services) **[[physics-pathfinding-and-npc-ai]]** Use RunService for per-frame updates and to check whether code runs on server, client, or in Studio mode.
- [page](https://create.roblox.com/docs/scripting/services) **[[combat-and-gameplay-systems]]** Use CollectionService tags to group related instances; tags replicate from server to client, making batch assignment and lookup easier.

## Tools
game:GetService(), WaitForChild(), TweenService, MarketplaceService, RunService, SoundService, CollectionService, DataStoreService

## He points to
- Open Cloud
- Data model documentation

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[data-persistence]] [[luau-language-and-types]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
