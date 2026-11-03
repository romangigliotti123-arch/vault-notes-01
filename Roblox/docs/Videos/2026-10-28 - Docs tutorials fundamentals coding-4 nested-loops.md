---
title: "Docs: tutorials / fundamentals / coding-4 / nested-loops"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-4 / nested-loops

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on nested loops in Luau. Covers how nested loops execute (inner loop completes before outer advances), a PartMaker demo, and building a 3D cube tower with three nested for loops for height, length and width. Ends with optional challenges (fading transparency, rain-down cupcakes).

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops) **[[luau-language-and-types]]** Parent new instances to workspace last, after setting their properties. Changes made before parenting are cheaper than changes to a physical object already in the world.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops) **[[luau-language-and-types]]** Use CAPITALISED_UNDERSCORE names for constants (e.g. TOWER_SIZE, CUBE_SIZE) that never change, to separate them from mutable variables.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops) **[[code-architecture-and-frameworks]]** Indent nested loops consistently; deep nesting becomes unreadable otherwise.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops) **[[scripting-and-performance]]** Delete or disable an old test script before running a new one, otherwise two scripts spawn parts at the same place at the same time.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops) Example tower size: **TOWER_SIZE = 4 (changed to 6 in fade challenge)** (Cube tower tutorial constant values)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops) Wait between cube spawns: **0.25 seconds** (task.wait inside innermost loop of tower build)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/nested-loops) Wait between batches in PartMaker: **2 seconds** (Outer loop pause in nested loop example)

## Tools
Roblox Studio, Luau

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
