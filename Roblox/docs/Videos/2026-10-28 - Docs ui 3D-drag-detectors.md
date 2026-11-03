---
title: "Docs: ui / 3D-drag-detectors"
url: https://create.roblox.com/docs/ui/3D-drag-detectors.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / 3D-drag-detectors

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/ui/3D-drag-detectors.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on DragDetector: making parts/models draggable without code, drag styles, drag direction via ReferenceInstance/Axis, response styles (Geometric/Physical/Custom), limits, permissions, physics tuning, modifier keys, replication, and script hooks (events, scriptable style, constraint functions, 3D UI examples).

## Tips
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) **[[building-and-level-design]]** Always set DragDetector.ReferenceInstance to a dedicated reference part when using axis or movement limits; otherwise each drag resets limits to the object's current world position.
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) **[[building-and-level-design]]** When making children of models draggable, set ReferenceInstance to a surface inside the model (e.g. desk top) so drag direction stays consistent if the model rotates.
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) **[[scripting-and-performance]]** Set PermissionPolicy to Scriptable and register a function; if the function is missing or returns an invalid result, all players are blocked from dragging.
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) **[[client-server-and-remotes]]** With RunLocally false (default), custom events and registered functions must live in server Scripts; with RunLocally true, put them in client scripts and use RemoteEvents to update the server.

## Numbers
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) DragDetector.MaxForce default: **10000000** (max force applied to reach drag goal under Physical response)
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) DragDetector.MaxTorque default: **10000** (max torque applied under Physical response)
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) DragDetector.Responsiveness default: **10** (higher values reach goal more rapidly)
- [page](https://create.roblox.com/docs/ui/3D-drag-detectors) Default Axis: **(0, 1, 0)** (primary drag axis, world Y by default)

## Tools
Roblox Studio, DragDetector, Luau

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[client-server-and-remotes]] [[core-loops-and-game-design]] [[cross-platform-and-console]] [[development-process-and-speed]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
