---
title: "Docs: tutorials / fundamentals / coding-6 / create-with-module-scripts"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-6 / create-with-module-scripts

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on module scripts. Builds a TreasureManager ModuleScript in ServerStorage that handles key pickups, chest opening and leaderstat updates, and is required from the key and chest scripts.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts) **[[code-architecture-and-frameworks]]** Put shared game logic in a ModuleScript in ServerStorage and require it from other scripts. Keep all module code between `local X = {}` and `return X`; return must be the last line.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts) **[[code-architecture-and-frameworks]]** Split module code into Local Functions and Module Functions sections so private helpers stay separate from the exposed API.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts) **[[scripting-and-performance]]** Use WaitForChild() when requiring a module from a script that may load first. For ServerScriptService or ServerStorage paths, dot access is safe.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts) **[[client-server-and-remotes]]** Keep leaderstat currency changes (keys, treasure) in a server-side module so only server code modifies player values.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts) Keys granted per key pickup: **1** (keyDrop variable in TreasureManager tutorial)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts) Keys cost per chest open: **1** (chestPickCost variable in TreasureManager tutorial)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/create-with-module-scripts) Gold reward per chest: **100** (chestReward variable in TreasureManager tutorial)

## Tools
Roblox Studio, ModuleScript, Luau

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
