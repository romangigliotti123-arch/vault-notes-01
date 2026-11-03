---
title: "Docs: workspace / streaming / techniques"
url: https://create.roblox.com/docs/workspace/streaming/techniques.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / streaming / techniques

[Open](https://create.roblox.com/docs/workspace/streaming/techniques.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on converting games to in-game instance streaming. Covers recommended Workspace streaming properties, Model LevelOfDetail/SLIM and ModelStreamingMode usage, script patterns that break under streaming (indexing, remotes, property reads, collection iteration, spatial queries), proactive streaming, realistic testing, and the AI streaming conversion skill.

## Tips
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Enable StreamingEnabled, then set ModelStreamingBehavior=Improved, StreamingIntegrityMode=PauseOutsideLoadedArea, StreamOutBehavior=Opportunistic to reduce memory and OOM crashes.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Keep StreamingMinRadius at default 64 and StreamingTargetRadius at default 1024 for a good balance of visibility and memory.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Set LevelOfDetail to SLIM on models with static meshes/parts; not supported for models modified at runtime or playing animations.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[building-and-level-design]]** Keep each model's spatial extent under about 64 cubic studs; split large models into smaller modular ones so they stream in together.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[building-and-level-design]]** Decompose container models (many NPCs/props in one Model) into smaller models of physically or logically related parts.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Use ModelStreamingMode Atomic for models whose scripts need all child parts; use Persistent only when content must always be accessible, since it never streams out.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Flatten nested hierarchies: a persistent model inside an atomic model forces the atomic model to behave as persistent.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[scripting-and-performance]]** Avoid direct dot-indexing into Workspace descendants and character parts on client; use WaitForChild when progress requires it, or nil-check with FindFirstChild otherwise.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[client-server-and-remotes]]** Wait for or nil-check instances received via RemoteEvent; instances may not be replicated yet. Use WaitForChild with a timeout.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[client-server-and-remotes]]** Call Player:RequestStreamAroundAsync() on the server before teleporting a character to pre-fetch the destination and reduce pop-in.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Treat client-side desynchronization (local reparenting, Clone into Workspace, client Destroy) as an exception; those changes break replication and streaming.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[physics-pathfinding-and-npc-ai]]** Move distance checks and line-of-sight/position-sensitive logic to the server, since clients see stale property values for streamed-out instances.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[core-loops-and-game-design]]** Do not gate loading screen dismissal on a spatial map instance; signal readiness after the character spawns and nearby area streams in, or call AddReplicationFocus at spawn.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[common-mistakes]]** Don't assume ChildAdded, ChildRemoved or CollectionService added/removed signals mean real spawns; they also fire on stream in/out. Guard effects with an attribute like Spawned.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Use AddReplicationFocus sparingly for areas that must stay loaded; prefer RequestStreamAroundAsync for transient loading.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[optimization-and-streaming]]** Test with StreamingTargetRadius set to 64 and traverse, teleport and revisit areas; bugs appear at stream edges and transitions.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[testing-debugging-and-qa]]** Watch Output and Developer Console for 'attempt to index nil with' errors, which usually indicate a missing WaitForChild call.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[common-mistakes]]** Persistent models and Touched, ProximityPrompt, ClickDetector and DragDetector interactions don't work for players who don't have the part streamed in; use persistent models or another mechanism.
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) **[[ai-and-tools]]** Back up the game first (File > Publish to Roblox As) before running the rbx-convert-to-streaming AI skill; a typical conversion takes 20-30 minutes and about 200,000 tokens.

## Numbers
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) StreamingMinRadius default: **64** (Recommended default; lets engine scale down for low-end devices)
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) StreamingTargetRadius default: **1024** (Recommended default balancing high-end visibility and memory)
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) Model spatial extent guideline: **~64 cubic studs** (Keeps whole model likely to stream in together)
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) Test StreamingTargetRadius minimum: **64** (Used to expose streaming bugs during testing)
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) AI skill conversion time: **20-30 minutes** (Frontier model, typical conversion)
- [page](https://create.roblox.com/docs/workspace/streaming/techniques) AI skill token usage: **~200,000 tokens** (Typical conversion context usage)

## Tools
Roblox Studio, StreamingEnabled, ModelStreamingMode, LevelOfDetail (SLIM), CollectionService, rbx-convert-to-streaming AI skill, Streaming debug overlay

## He points to
- SLIM avatars docs
- Pathfinding - Strategies docs
- Proactive streaming docs

## Topics
[[ai-and-tools]] [[building-and-level-design]] [[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
