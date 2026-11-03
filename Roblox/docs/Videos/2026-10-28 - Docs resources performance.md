---
title: "Docs: resources / performance"
url: https://create.roblox.com/docs/resources/performance.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: medium
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / performance

[Open](https://create.roblox.com/docs/resources/performance.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Overview page for Peter "MrChickenRocket" McNeill's Cardboard Box Simulator performance case study (2024 project). Covers rendering budgets, reusable art, visibility, distance culling, coins, pets, and effects, with practical tasks and reference appendixes. The page itself gives no concrete figures; it points to the full article for measurements.

## Tips
- [page](https://create.roblox.com/docs/resources/performance) **[[optimization-and-streaming]]** Set a rendering budget and measure your game against it, using the author's example figures as a starting reference rather than fixed targets.
- [page](https://create.roblox.com/docs/resources/performance) **[[building-art-and-assets]]** Reuse art assets across the game instead of creating unique meshes for every object, to reduce rendering cost.
- [page](https://create.roblox.com/docs/resources/performance) **[[optimization-and-streaming]]** Cull distant or non-visible objects so they are not rendered, using visibility checks and distance culling.
- [page](https://create.roblox.com/docs/resources/performance) **[[vfx-and-particles]]** Budget effects carefully, since particles and visual effects add to frame cost on top of geometry.

## Games
- **Cardboard Box Simulator**: Case study for frame-time budgeting: reusable art, visibility and distance culling, and managing coins, pets and effects for performance.

## He points to
- Peter "MrChickenRocket" McNeill's original Cardboard Box Simulator performance article
- Cardboard Box Simulator experience

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
