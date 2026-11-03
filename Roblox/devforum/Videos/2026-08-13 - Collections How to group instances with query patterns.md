---
title: "Collections: How to group instances with query patterns"
url: https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-08-13
views: 125
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Collections: How to group instances with query patterns

[Open](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) | Roblox DevForum | 125 views | 2026-08-13

## Summary
Announcement of Collections, a CollectionService extension where a query string (engine QueryDescendants syntax) defines a live set of instances. Callbacks (OnAdded/OnRemoved, On{Event}, OnHeartbeat, OnAttributeChanged) are bulk-bound with automatic connection management and streaming-safe membership. Includes query performance guidance and an experimental in-radius selector.

## Tips
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[scripting-and-performance]]** Scope collections to a small root instance via CreateCollection's rootInstance argument; workspace-wide queries force tracking of many instances and cost more.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[scripting-and-performance]]** Include a class specifier (Part#Killbrick, not #Killbrick) so the engine ignores non-matching classes and only monitors relevant instances for name changes.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[scripting-and-performance]]** Avoid combinators (>, >>, has, in-radius) where possible; they add significant tracking overhead, with has() and in-radius() called out as expensive.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[scripting-and-performance]]** Tag and attribute selectors do not speed up queries and slightly slow them, since extra listeners are needed to detect tag and attribute changes.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[code-architecture-and-frameworks]]** Replace per-instance signal connections and maid/cleanup code with collection callbacks; connections are attached on enter and removed on exit automatically.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[client-server-and-remotes]]** Write one collection and instantiate it on both client and server to keep predicted and authoritative behaviour aligned for server-authority designs.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[data-persistence]]** Use Atomic Streaming Modes with collections so callbacks only run on streamed-in instances, avoiding WaitForChild.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[luau-language-and-types]]** Use has() child queries (e.g. Part:has(> Part#SomePart)) so the typed callback argument lets you access the child without WaitForChild.
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) **[[luau-language-and-types]]** Bind callbacks to class-specific events (OnTouched) so the argument is typed to that class instead of generic Instance.

## Numbers
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) Query cost tiers: **Cheap: RootContext, Class, Tag, Property, Name, Attribute, not(); High: >, >>, has(), in-radius()** (Approximate performance chart from the release notes)
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) in-radius syntax: **Part#Killbrick:in-radius(10, Part#HumanoidRootPart)** (Experimental; radius measured from selected Part center to nearest edge of selector Part)

## Games
- **CollectionObby**: Official demo obby (5 levels plus museum) showcasing Collection examples; downloadable .rbxl for reference.

## Tools
CollectionService:CreateCollection, Collection:ForEach, Collection:Destroy, Studio Explorer query: search filter, QueryDescendants selector syntax, RunService signals via OnHeartbeat/OnSimulate

## He points to
- Instance:QueryDescendants documentation
- CSS selectors / Blink (performance design inspiration)
- flecs (ECS reference for planned query extensions)
- CollectionObby.rbxl demo place

## Quotes
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) "Collections automatically manage connections so their callbacks are leak-free."
- [page](https://devforum.roblox.com/t/collections-how-to-group-instances-with-query-patterns/4809143) "Using a rootContext with a small subtree of your place is the best way to maximize Collection query performance."

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
