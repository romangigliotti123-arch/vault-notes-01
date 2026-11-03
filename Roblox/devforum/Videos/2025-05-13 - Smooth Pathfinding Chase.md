---
title: "Smooth Pathfinding Chase"
url: https://devforum.roblox.com/t/smooth-pathfinding-chase/3648450
creator: Roblox DevForum
official: false
advice_density: low
date: 2025-05-13
views: 61
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Smooth Pathfinding Chase

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/smooth-pathfinding-chase/3648450) | Roblox DevForum | 61 views | 2025-05-13

## Summary
Introduces SmoothChase, a lightweight open-source PathfindingService-based NPC chase module for Roblox. Covers features (distance-based update rates, Vector3/Part/CFrame targets, async jump handling, data-oriented design for many NPCs) and suggested use cases. Mostly a promotional project page.

## Tips
- [page](https://devforum.roblox.com/t/smooth-pathfinding-chase/3648450) **[[ai-and-tools]]** Drop the SmoothChase module into ServerScriptService to use it; full docs are in the project's GitHub README.
- [page](https://devforum.roblox.com/t/smooth-pathfinding-chase/3648450) **[[physics-pathfinding-and-npc-ai]]** Use distance-based update rates for pathfinding NPCs so distant chasers recompute paths less often, saving performance.
- [page](https://devforum.roblox.com/t/smooth-pathfinding-chase/3648450) **[[physics-pathfinding-and-npc-ai]]** Use a data-oriented design so one system can drive many NPCs simultaneously instead of per-NPC heavy logic.
- [page](https://devforum.roblox.com/t/smooth-pathfinding-chase/3648450) **[[physics-pathfinding-and-npc-ai]]** Handle jumps explicitly in async pathfinding movement; the module's jump handling is a known requirement for natural chase movement.

## Tools
SmoothChase (Luau module), PathfindingService

## Topics
[[ai-and-tools]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
