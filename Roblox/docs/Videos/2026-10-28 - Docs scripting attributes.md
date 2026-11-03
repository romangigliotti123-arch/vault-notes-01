---
title: "Docs: scripting / attributes"
url: https://create.roblox.com/docs/scripting/attributes.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / attributes

[Open](https://create.roblox.com/docs/scripting/attributes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on properties and attributes. Covers getting object references safely given non-guaranteed replication order, WaitForChild usage, ReplicatedFirst load order, creating/getting/setting/deleting attributes with SetAttribute/GetAttribute/GetAttributes, and listening for changes via Changed, AttributeChanged, GetPropertyChangedSignal and GetAttributeChangedSignal.

## Tips
- [page](https://create.roblox.com/docs/scripting/attributes) **[[client-server-and-remotes]]** Don't assume a server property change has replicated when FireAllClients is called; the client may see it before or after the RemoteEvent. Detect changes with events instead.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[client-server-and-remotes]]** Changes of the same type (e.g. two attribute changes) generally arrive in order, so sequencing within one type is safe.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[scripting-and-performance]]** In client scripts, use WaitForChild() to access Workspace objects; replication order is not guaranteed.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[scripting-and-performance]]** With StreamingEnabled, objects may not be in Workspace yet, so WaitForChild() is an even more important safety measure.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[scripting-and-performance]]** LocalScripts in ReplicatedFirst can safely read ReplicatedFirst objects without WaitForChild, but WaitForChild on other services negates that benefit.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[scripting-and-performance]]** Client scripts in ReplicatedStorage or PlayerScripts can safely read ReplicatedStorage objects without WaitForChild, since those load before the character spawns.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[code-architecture-and-frameworks]]** Create attributes with default values in Studio's UI when possible, then change them from scripts in response to player actions.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[code-architecture-and-frameworks]]** Use attributes as custom properties for tunable data, e.g. seed purchase price or max plant size, as the Plant reference project does.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[code-architecture-and-frameworks]]** Delete an attribute by setting it to nil; SetAttribute creates the attribute if it does not exist.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[scripting-and-performance]]** Use GetAttributeChangedSignal for one attribute and AttributeChanged for any attribute; use GetPropertyChangedSignal for one property. Changed fires for property and attribute changes alike.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[common-mistakes]]** Changed also fires when attributes change, with the property name 'Attributes'; filter that out if you only want real property changes.
- [page](https://create.roblox.com/docs/scripting/attributes) **[[physics-pathfinding-and-npc-ai]]** Anchor physics objects (e.g. Anchored on a thrown javelin or discus) at the moment they land to give players a clear visual of the result.

## Games
- **Plant (reference project)**: Uses attributes to store seed purchase price and maximum plant size per pot, showing attributes as tunable custom properties.

## Tools
Roblox Studio Explorer, Instance attributes (Studio UI), Luau scripts

## He points to
- Instance attributes docs
- Events docs
- Stream in / per-model streaming controls docs

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
