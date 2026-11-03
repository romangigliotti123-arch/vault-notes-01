---
title: "Docs: scripting / module"
url: https://create.roblox.com/docs/scripting/module.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / module

[Open](https://create.roblox.com/docs/scripting/module.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on ModuleScripts: anatomy, require() caching behaviour, and patterns for data sharing, custom events via BindableEvents, and encapsulating RemoteEvents in a shared module.

## Tips
- [page](https://create.roblox.com/docs/scripting/module) **[[code-architecture-and-frameworks]]** Store ModuleScripts in ReplicatedStorage to share code between server and clients; they can go anywhere scripts can.
- [page](https://create.roblox.com/docs/scripting/module) **[[code-architecture-and-frameworks]]** Return a table of functions from a ModuleScript rather than a bare function; it's easier to read at call sites and to extend later.
- [page](https://create.roblox.com/docs/scripting/module) **[[common-mistakes]]** Avoid ModuleScripts requiring each other in a circle; this causes a 'Requested module was required recursively' error.
- [page](https://create.roblox.com/docs/scripting/module) **[[client-server-and-remotes]]** Use WaitForChild when requiring modules or remotes from client scripts to avoid replication-order race conditions.
- [page](https://create.roblox.com/docs/scripting/module) **[[code-architecture-and-frameworks]]** Keep shared tuning values (e.g. gun damage, magazine size, fire rate) in a config ModuleScript instead of attributes or value objects, which get unwieldy for many objects.
- [page](https://create.roblox.com/docs/scripting/module) **[[code-architecture-and-frameworks]]** Wrap a single RemoteEvent in a ModuleScript that takes an id argument so one remote can carry many message types, and expose named helpers instead of raw remotes.
- [page](https://create.roblox.com/docs/scripting/module) **[[code-architecture-and-frameworks]]** Wrap DataStoreService calls in a ModuleScript to centralise error handling around sensitive services.
- [page](https://create.roblox.com/docs/scripting/module) **[[data-persistence]]** Note that require() runs a module once and caches it; modifying a returned table persists for all later requires on that side.

## Numbers
- [page](https://create.roblox.com/docs/scripting/module) example output: **print(bonus) → 125 (legendary 100 × default multiplier 1.25)**

## Tools
Roblox Studio, ModuleScript, RemoteEvent, BindableEvent, DataStoreService

## He points to
- Replication order (Roblox docs)
- Events (Roblox docs)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
