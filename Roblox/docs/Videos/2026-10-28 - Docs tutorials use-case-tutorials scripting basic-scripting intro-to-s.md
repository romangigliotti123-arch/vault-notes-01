---
title: "Docs: tutorials / use-case-tutorials / scripting / basic-scripting / intro-to-scripting"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / scripting / basic-scripting / intro-to-scripting

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on basic scripting: makes a part-based platform that disappears and reappears on a timer using a Script inside the Part, with variables, functions, properties (Transparency, CanCollide), and a while loop with task.wait().

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting) **[[scripting-and-performance]]** Always include a task.wait() inside a while true loop; without it the game freezes because Studio never gets to run other code.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting) **[[scripting-and-performance]]** Use local variables and camelCase names; local scopes the variable to the block where it is declared.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting) **[[code-architecture-and-frameworks]]** Group code for one action into a named function (e.g. disappear/appear) so it can be reused and kept readable.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting) **[[building-and-level-design]]** Anchor platforms (Anchored = true) so they stay in place; unanchored parts fall.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting) Platform wait interval: **3 seconds between disappear and appear (task.wait(3)), described as a sensible starting point** (Timed platform toggle in basic scripting tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/intro-to-scripting) Transparency range: **0 to 1, where 1 is fully invisible** (BasePart.Transparency property used to hide platform)

## Tools
Roblox Studio, Luau, Explorer, Properties window

## Topics
[[building-and-level-design]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
