---
title: "Docs: tutorials / curriculums / core / scripting / script-game-behavior"
url: https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / scripting / script-game-behavior

[Open](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial: builds a coin collection mechanic. Creates a Coins folder of gold cylinder Parts (anchored, non-collidable), then a server Script in ServerScriptService that connects Touched handlers, uses an Enabled attribute, hides coins for a 10-second cooldown, and explains services, GetChildren, and task.wait.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior) **[[scripting-and-performance]]** Put gameplay logic scripts in ServerScriptService so they run on the server and clients cannot access them.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior) **[[luau-language-and-types]]** Use task.wait() instead of wait() for delays; it does not pause all code execution and lets other threads run concurrently.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior) **[[building-and-level-design]]** Group related objects (e.g. all coins) in a single folder so scripts can find and manage them easily.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior) **[[client-server-and-remotes]]** Track state like collectability with instance attributes (e.g. Enabled) and check them server-side before applying effects.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior) **[[development-process-and-speed]]** Build placeholder objects (simple Parts) first to prototype mechanics before final art.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior) Coin respawn cooldown: **10 seconds** (COOLDOWN constant in the tutorial coin script)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-game-behavior) Coin part size: **0.6, 8, 4 (cylinder, Orientation 90,0,0)** (Lays the coin flat like a disc)

## Tools
Roblox Studio, Explorer, Properties window, Output window, Assistant

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[development-process-and-speed]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
