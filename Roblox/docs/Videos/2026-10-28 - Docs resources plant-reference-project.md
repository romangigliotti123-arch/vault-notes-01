---
title: "Docs: resources / plant-reference-project"
url: https://create.roblox.com/docs/resources/plant-reference-project.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / plant-reference-project

[Open](https://create.roblox.com/docs/resources/plant-reference-project.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page describing the Plant reference project: a plant/seed farming microgame showcasing project structure (single client/server entry points), singleton/class patterns, typed Luau, client-server communication preferences, and an imperative UI layer/view-handling approach.

## Tips
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[code-architecture-and-frameworks]]** Prefer a single client LocalScript and single server Script as entry points when you need deterministic control over system startup order; multiple entry points give isolation but non-deterministic order.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[code-architecture-and-frameworks]]** Use singleton ModuleScripts (no new(), called with dot syntax) for systems like Network, PlayerData, Market; requiring a ModuleScript caches it so all callers share one object.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[code-architecture-and-frameworks]]** Compose classes instead of inheriting: instantiate the child object inside new() and store it under self, as with CloseButton wrapping Button.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[code-architecture-and-frameworks]]** Give every class a destroy() method that destroys its instances, disconnects connections and destroys child objects; connected instances are not garbage collected otherwise.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[code-architecture-and-frameworks]]** Clone prefabricated instances from ReplicatedStorage/ServerStorage instead of building properties at runtime; it's easier to edit and generally faster.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[luau-language-and-types]]** Use --!strict in every script to catch type errors before runtime.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[luau-language-and-types]]** Declare class methods with a dot and type self explicitly (self: ClassType) so strict inference works; duplicate the self type in the constructor and let warnings catch drift.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[luau-language-and-types]]** After a nil guard, create a new local cast to the non-optional type (local p = optional :: number) since Luau does not narrow types after guards yet.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[luau-language-and-types]]** Wrap deep data model traversal in a generic getInstance helper that casts to any internally, rather than casting to any at every call site.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[client-server-and-remotes]]** Minimise RemoteEvent/RemoteFunction usage: prefer player data replication, then attributes, then tags, and only use direct Network calls for client-to-server requests.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[client-server-and-remotes]]** Set attributes on a new instance before parenting it to the data model so they replicate atomically with the instance, avoiding wait-for-remote code.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[client-server-and-remotes]]** Avoid a unified module that has both startServer and startClient logic; it exposes server code to the client unnecessarily, though it can be acceptable for a high-touch network module.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[client-server-and-remotes]]** Validate argument types received from the client at runtime in a central Network module.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[data-persistence]]** Store session player data in memory on the server, save via DataStoreService, and replicate mutations to the client with a setValue-style API rather than bespoke remotes.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[matchmaking-and-teleport]]** Disable Players.CharacterAutoLoads and spawn characters manually after player data has loaded, so spawning waits for persistent data.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[scripting-and-performance]]** Route WalkSpeed/JumpHeight changes through a multiplier-based manager to avoid conflicts when several systems modify the same humanoid value.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[ui-ux-design]]** Organise UI as Layers (top-level singletons) and Components (reusable clones of ReplicatedStorage templates); register layers with a central handler that controls visibility.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[ui-ux-design]]** Classify menus as HUD or Menu; show HUD only when no Menu is open and keep open Menus in a stack so closing a sub-menu returns to the previous one.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[ui-ux-design]]** Imperative UI is quick to build visually in Studio and simple to change, but state desync bugs grow with complexity; declarative libraries (Roact, Fusion) trade editing ease for easier debugging.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[core-loops-and-game-design]]** Keep the loading screen's ReplicatedFirst contents minimal; every instance there delays replication before code can run.
- [page](https://create.roblox.com/docs/resources/plant-reference-project) **[[building-and-level-design]]** Place static world models in Workspace and only store runtime-cloned player content under a Folder, keeping per-player objects out of static map geometry.

## Games
- **Plant**: Reference microgame: players plant and water seeds, then harvest and sell plants; demonstrates project architecture patterns.

## Tools
Roblox Studio, Roact, Fusion, DataStoreService, CollectionService

## He points to
- Client-Server Model guide
- Luau guide
- Remote Events and Callbacks guide
- UI guide

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[core-loops-and-game-design]] [[data-persistence]] [[luau-language-and-types]] [[matchmaking-and-teleport]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
