---
title: "Docs: tutorials / fundamentals / coding-3 / multiple-conditions"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-3 / multiple-conditions

[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial on Luau multiple conditions. Covers if/elseif/else chains, then builds a parkour finish-line script that awards gold, silver or bronze medals based on a race timer incremented once per second in a while loop.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) **[[luau-language-and-types]]** Use if with multiple elseif branches instead of a separate if per case. Only the first true condition runs; later conditions are not checked.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) **[[luau-language-and-types]]** Always end an if chain with an else as a fallback, and keep else as the last check before end.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) **[[scripting-and-performance]]** Place the timer while loop at the bottom of the script so earlier event connections and functions are set up before the loop runs.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) **[[core-loops-and-game-design]]** Use a raceActive flag to stop the timer and the finish handler from repeating once the race has ended.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) **[[scripting-and-performance]]** Use task.wait(1) for a once-per-second timer loop rather than tight loops.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) Gold medal threshold: **<= 10 seconds finish time** (Parkour finish-line tutorial example medal tiers)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) Silver medal threshold: **<= 20 seconds finish time** (Parkour finish-line tutorial example medal tiers)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) Bronze medal threshold: **<= 30 seconds finish time** (Parkour finish-line tutorial example medal tiers)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/multiple-conditions) Timer tick interval: **1 second (task.wait(1))** (Race timer increments timePassed once per loop iteration)

## Tools
Roblox Studio, Output window

## He points to
- Create a Timed Bridge tutorial (Surface GUI for displaying time)

## Topics
[[core-loops-and-game-design]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
