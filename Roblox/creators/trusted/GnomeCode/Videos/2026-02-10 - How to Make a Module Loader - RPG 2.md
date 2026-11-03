---
title: "How to Make a Module Loader - RPG #2"
url: https://youtu.be/3D0l-WiEhLI
creator: GnomeCode
official: false
advice_density: medium
date: 2026-02-10
views: 33304
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Make a Module Loader - RPG #2

[Watch](https://youtu.be/3D0l-WiEhLI) | GnomeCode | 33,304 views | 2026-02-10

## Summary
Builds a class-based module loader for Roblox NPCs: CollectionService tags drive which ModuleScript runs per tagged model, with server and client versions, network ownership, and collision groups. Covers the structure used for scaling NPC logic without duplicating scripts.

## Tips
- [0:00](https://youtu.be/3D0l-WiEhLI?t=0) **[[code-architecture-and-frameworks]]** Replace duplicated per-NPC scripts with one ModuleScript per class; edit logic in one place instead of hundreds of scripts.
- [1:22](https://youtu.be/3D0l-WiEhLI?t=82) **[[code-architecture-and-frameworks]]** Use CollectionService tags to bind a ModuleScript's name to every instance that should use it (e.g. tag 'NPC').
- [3:50](https://youtu.be/3D0l-WiEhLI?t=230) **[[code-architecture-and-frameworks]]** Call CollectionService:GetInstanceAddedSignal for dynamically added objects, plus loop GetTagged for existing ones, so nothing is missed.
- [4:31](https://youtu.be/3D0l-WiEhLI?t=271) **[[code-architecture-and-frameworks]]** Connect the instance-added signal before the GetTagged loop so objects loading late (especially on client) aren't skipped.
- [6:37](https://youtu.be/3D0l-WiEhLI?t=397) **[[scripting-and-performance]]** Wrap per-object while-true loops in task.spawn so one infinite loop doesn't block the module loader from processing the rest.
- [7:19](https://youtu.be/3D0l-WiEhLI?t=439) **[[client-server-and-remotes]]** Run NPC movement on the server and set the root part's network owner to the server to avoid client ownership stutter and buffering.
- [7:57](https://youtu.be/3D0l-WiEhLI?t=477) **[[building-and-level-design]]** Set up collision groups (Window > 3D > Collision Groups) to stop NPCs colliding with each other and with players.
- [8:39](https://youtu.be/3D0l-WiEhLI?t=519) **[[building-and-level-design]]** When applying collision groups to characters, loop only BaseParts so accessories and tools don't error.
- [10:19](https://youtu.be/3D0l-WiEhLI?t=619) **[[code-architecture-and-frameworks]]** Keep the animation script in ReplicatedStorage disabled as the master copy and clone it onto each NPC on the client; keeps workspace clean.
- [11:41](https://youtu.be/3D0l-WiEhLI?t=701) **[[scripting-and-performance]]** Use WaitForChild for Humanoid, HumanoidRootPart and Animate on the client, since they may not have replicated yet.
- [12:24](https://youtu.be/3D0l-WiEhLI?t=744) **[[code-architecture-and-frameworks]]** Use a server/client suffix on module names and strip it with string.sub based on RunService:IsServer to derive the shared tag name.

## Numbers
- [0:00](https://youtu.be/3D0l-WiEhLI?t=0) NPC count in demo: **2 NPCs (Joe, Fred)**

## Tools
Roblox Studio, CollectionService, RunService, Luau require(), Collision Groups

## He points to
- gnomeode.com (academy files)
- gnomeode Discord

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[scripting-and-performance]]

Back to [[GnomeCode - How to make successful Roblox games]]
