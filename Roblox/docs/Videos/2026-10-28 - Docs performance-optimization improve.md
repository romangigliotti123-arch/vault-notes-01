---
title: "Docs: performance-optimization / improve"
url: https://create.roblox.com/docs/performance-optimization/improve.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / improve

[Open](https://create.roblox.com/docs/performance-optimization/improve.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on improving performance: script computation, memory leaks, physics cost and collision fidelity, Humanoid overhead, rendering draw calls and instancing, networking/replication traffic, and asset memory via instance streaming. Gives MicroProfiler scopes and specific mitigation steps.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[scripting-and-performance]]** Limit code on RunService PreRender/PreSimulation/PostSimulation/Heartbeat to what truly needs per-frame updates (e.g. camera); run other work in other events or on a throttled loop.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Break large expensive tasks with task.wait() across frames; use multithreading (parallel Luau) for compute-heavy work that doesn't touch the DataModel.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[scripting-and-performance]]** Avoid recursive or large-table serialization, deserialization and deep cloning per frame; they scale badly with table size.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Use native code generation for compute-heavy server scripts; reserve more CPU with Extended Services for Compute if servers still run out after optimizing.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[common-mistakes]]** Don't assume Player objects are destroyed on leave; connections to Player and CharacterAdded keep leaking on servers. Enable PlayerCharacterDestroyBehavior or destroy manually on PlayerRemoving.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[scripting-and-performance]]** Remove entries from per-player tables on PlayerRemoving; tables that only grow slow iteration and consume memory over long server sessions.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Anchor all parts that don't need physics simulation, such as static NPCs.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[physics-pathfinding-and-npc-ai]]** Keep adaptive physics stepping (60/120/240 Hz); fixed 240 Hz mode forces four steps per frame and costs significantly more.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[physics-pathfinding-and-npc-ai]]** Minimize constraints and joints per assembly, and disable self-collision in ragdoll limbs with limits or no-collision constraints.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[building-art-and-assets]]** Set MeshPart CollisionFidelity to Box for small or non-interactable parts, box/hull for small-medium, and build custom collision from invisible parts for large complex meshes.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[genre-mechanics]]** Disable unused HumanoidStateTypes on NPCs with SetStateEnabled (e.g. Climbing unless NPCs climb ladders).
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[scripting-and-performance]]** Don't use Humanoids on static NPCs; use an AnimationController for animation-only NPCs and a custom movement controller for moving ones.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Pool frequently respawned NPCs and characters instead of destroying and re-instantiating them; only spawn NPCs when players are nearby.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[client-server-and-remotes]]** Play NPC animations on the client by creating the Animator locally, reducing server load and replication; animations can also be culled by distance.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[building-art-and-assets]]** Upload each mesh once and duplicate it in Studio rather than importing whole maps, so identical meshes share asset IDs and instance into single draw calls.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Reduce draw calls: limit object density, decals, textures and ParticleEmitter property changes, which batch poorly. Check Render Stats with Shift+F2.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Set MeshPart RenderFidelity to Automatic or Performance and Model LevelOfDetail to SLIM with instance streaming to reduce polygons at distance.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Disable CastShadow on small or distant parts, disable Light.Shadows where unneeded, limit light range and angle, and cull lights room by room.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[client-server-and-remotes]]** Send only necessary data at lower frequency and only the changed item rather than whole inventories; throttle input-triggered remote calls.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[client-server-and-remotes]]** Don't tween objects server-side; the tweened property replicates every frame causing jitter and traffic. Tween on the client, and let clients create VFX locally from server-sent location data.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Chunk large instance trees like maps and load them across frames; clean animation metadata from rigs after import, since clones replicate it.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[optimization-and-streaming]]** Enable instance streaming, the highest-impact way to reduce client memory; lower StreamingMinRadius and StreamingTargetRadius and reduce Persistent streaming mode if needed.
- [page](https://create.roblox.com/docs/performance-optimization/improve) **[[building-art-and-assets]]** Load audio only when needed for the part of the game being played, since audio files can be a surprising source of client memory use.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/improve) Physics step rates (adaptive): **60 Hz, 120 Hz or 240 Hz; fixed mode = 240 Hz (4x per frame)**
- [page](https://create.roblox.com/docs/performance-optimization/improve) Avatar invalidation warning threshold: **updateInvalidatedFastClusters over 4 ms**
- [page](https://create.roblox.com/docs/performance-optimization/improve) Shadow quality cutoff: **Shadows disabled entirely at graphics quality level below 4**

## Tools
Developer Console, MicroProfiler, Render Stats (Shift+F2), PlaceScriptMemory, Visualization Options (collision fidelity), Explorer filter CollisionFidelity=PreciseConvexDecomposition

## He points to
- Set physics and rendering parameters
- Delete layered transparencies
- Humanoid performance tips
- streaming properties
- Load time

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[genre-mechanics]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
