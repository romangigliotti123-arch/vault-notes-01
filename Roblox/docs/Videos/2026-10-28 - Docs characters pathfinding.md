---
title: "Docs: characters / pathfinding"
url: https://create.roblox.com/docs/characters/pathfinding.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / pathfinding

[Open](https://create.roblox.com/docs/characters/pathfinding.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on pathfinding: PathfindingService setup, path creation parameters, computing and moving along waypoints with Humanoid:Move, blocked-path handling, material costs, PathfindingModifier regions and pass-through, PathfindingLink for custom traversal, streaming compatibility, and failure limits (3,000 studs, 20,000 nodes).

## Tips
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[physics-pathfinding-and-npc-ai]]** Use Humanoid:Move() waypoint-to-waypoint with a Heartbeat check for arrival rather than moving the character directly.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[physics-pathfinding-and-npc-ai]]** Connect Path.Blocked and recompute, but only when the blocked waypoint index is ahead of the current waypoint; ignore blocks behind the agent.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[physics-pathfinding-and-npc-ai]]** Wait until the humanoid is grounded before calling ComputeAsync; paths computed mid-fall start from an inferred position.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[physics-pathfinding-and-npc-ai]]** Set costs to a high finite value (100 or 1000) instead of math.huge for materials to use only as a last resort; math.huge makes them non-traversable.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[physics-pathfinding-and-npc-ai]]** Create a non-collidable anchored part with a PathfindingModifier and matching Costs key to make the agent avoid a region regardless of floor material.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[physics-pathfinding-and-npc-ai]]** Use PathfindingModifier.PassThrough on doors or obstacles so the path extends through them; the NPC can then react as if it heard the player behind.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[physics-pathfinding-and-npc-ai]]** For custom traversal (e.g. boats), use a PathfindingLink with a label and give its Costs entry a lower value than Water so the agent prefers it.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[optimization-and-streaming]]** In streaming-enabled games, recompute blocked paths as parts stream in and out; use persistent models for client-side path destinations.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[scripting-and-performance]]** For client-side pathfinding targets, use a BasePart in a persistent model and wait for Workspace.PersistentLoaded, since streamed-out objects cannot be resolved by clients.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[common-mistakes]]** Do not rely on default shortest paths: they route through swamp water when it is geometrically shorter; set material costs to avoid this.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[common-mistakes]]** Keep path requests under 3,000 studs straight-line distance and expect failures in large open worlds or mazes that exceed 20,000 nodes.
- [page](https://create.roblox.com/docs/characters/pathfinding) **[[common-mistakes]]** Set AgentHeight and AgentCanJump to match the agent; computations fail if the only route needs jumping while AgentCanJump is false.

## Numbers
- [page](https://create.roblox.com/docs/characters/pathfinding) Path request max straight-line distance: **3,000 studs** (ComputeAsync fails if start-to-finish line-of-sight exceeds this)
- [page](https://create.roblox.com/docs/characters/pathfinding) Node budget: **20,000 nodes** (Computation may exhaust nodes before reaching distance cap)
- [page](https://create.roblox.com/docs/characters/pathfinding) Default AgentRadius: **2 studs** (CreatePath parameter default)
- [page](https://create.roblox.com/docs/characters/pathfinding) Default AgentHeight: **5 studs** (CreatePath parameter default; smaller gaps are non-traversable)
- [page](https://create.roblox.com/docs/characters/pathfinding) Default WaypointSpacing: **4 studs** (Spacing between intermediate waypoints)
- [page](https://create.roblox.com/docs/characters/pathfinding) Default material cost: **1** (All materials; math.huge makes non-traversable)
- [page](https://create.roblox.com/docs/characters/pathfinding) Vertical waypoint limit: **-65,536 to 65,536 studs Y** (Waypoints outside this Y range are ignored)

## Tools
PathfindingService, Path, Humanoid:Move, PathfindingModifier, PathfindingLink, Studio Visualization Options

## He points to
- Roblox docs: Pathfinding (creating paths, costs, modifiers, links, streaming)

## Topics
[[common-mistakes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
