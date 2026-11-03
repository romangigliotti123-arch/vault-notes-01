---
title: "Docs: tutorials / fundamentals / coding-4 / glow-lights-with-for-loops"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-4 / glow-lights-with-for-loops

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial: create a glowing lamp by scripting the brightness of a SpotLight/PointLight with two for loops (count up, count down) nested in a while true loop, using task.wait for timing.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops) **[[scripting-and-performance]]** Use task.wait(timeChange) inside loops to spread changes over time; without it the whole loop runs instantly.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops) **[[luau-language-and-types]]** For loop syntax: for var = start, end, step do ... end; use a negative step (-brightnessChange) to count down.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops) **[[code-architecture-and-frameworks]]** Store lookups in variables (lightPart = script.Parent; light = lightPart.SpotLight) and verify paths in Explorer, since model structure varies.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops) **[[common-mistakes]]** Keep loop body statements between do and end, and use exactly two commas in the for-loop header, or the effect won't show.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops) ClockTime: **0** (Night time setting used to make the light visible)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops) Brightness range: **0 to 5, step 1** (Lamp brightness loop values in the tutorial)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-4/glow-lights-with-for-loops) timeChange: **1 second (min suggested); 0.2 in final script** (Wait between brightness steps)

## Tools
Roblox Studio, Luau, Explorer, PointLight

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
