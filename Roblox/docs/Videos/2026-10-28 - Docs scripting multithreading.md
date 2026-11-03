---
title: "Docs: scripting / multithreading"
url: https://create.roblox.com/docs/scripting/multithreading.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / multithreading

[Open](https://create.roblox.com/docs/scripting/multithreading.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on Parallel Luau: running code across multiple threads via Actors, task.desynchronize/synchronize, ConnectParallel, thread safety levels, cross-thread communication (actor messaging, SharedTable, data model), and two examples (server-side raycast validation, procedural terrain generation), plus best practices.

## Tips
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Scripts run serially by default; put logic under Actors and call task.desynchronize() to get real parallel execution, since actors alone don't speed anything up.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Combine serial and parallel phases: compute in parallel, then call task.synchronize() before modifying instances or global state.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Scripts in the same actor run sequentially; use multiple actors for logic units that should run on separate threads.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Use more actors (e.g. 64+) split by logic unit rather than few large ones; finer granularity gives better load balancing across cores, but don't overdo it.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Avoid long unyielding computations in parallel phases; they block other scripts and cause lag.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Don't call require() inside a desynchronized phase; require modules in a serial context first.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Use RBXScriptSignal:ConnectParallel() for signals like Heartbeat when the callback's work is mostly computation; it avoids calling desynchronize inside the callback.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[client-server-and-remotes]]** For per-player hit validation, give each character its own RemoteEvent and actor so validations run in parallel instead of funneling through one centralized script.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[common-mistakes]]** Don't assume API members are parallel-safe; members without a stated thread safety level are Unsafe and can't be read or written in parallel.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[scripting-and-performance]]** Use actor messaging (SendMessage / BindToMessageParallel) or SharedTable for cross-thread communication; writing to the data model from parallel code is restricted and forces frequent synchronization.
- [page](https://create.roblox.com/docs/scripting/multithreading) **[[data-persistence]]** Use SharedTable for large shared state across actors; updates are atomic and visible to all actors, and cloning uses structural sharing rather than copying.

## Numbers
- [page](https://create.roblox.com/docs/scripting/multithreading) Example actor count: **32 actors (procedural terrain); 64+ suggested for raycast validation** (Docs sample and best-practice guidance on actor counts)
- [page](https://create.roblox.com/docs/scripting/multithreading) Thread safety levels: **Unsafe, Read Parallel, Local Safe, Safe** (Access tiers for API properties and functions in parallel code)
- [page](https://create.roblox.com/docs/scripting/multithreading) Default thread safety: **Unsafe** (Applies to API members with no stated safety level)

## Tools
Actor, task.desynchronize / task.synchronize, RunService:ConnectParallel, Actor:SendMessage / BindToMessageParallel, SharedTable, Workspace:Raycast, Terrain:WriteVoxels

## He points to
- Roblox API reference thread safety tags
- Best practices section of Parallel Luau docs

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
