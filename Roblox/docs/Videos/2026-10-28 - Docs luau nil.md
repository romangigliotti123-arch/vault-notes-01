---
title: "Docs: luau / nil"
url: https://create.roblox.com/docs/luau/nil.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / nil

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/nil.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Luau docs page on nil: nil removes variables and table keys, unparents instances, and marks values for garbage collection once no longer referenced. Only false and nil are falsy.

## Tips
- [page](https://create.roblox.com/docs/luau/nil) **[[scripting-and-performance]]** In long-running scripts, set large variables to nil once no longer needed so the garbage collector can reclaim them.
- [page](https://create.roblox.com/docs/luau/nil) **[[scripting-and-performance]]** Setting an instance's Parent to nil removes it from the game without destroying it; reassign Parent to return it.
- [page](https://create.roblox.com/docs/luau/nil) **[[common-mistakes]]** Clearing an instance's Parent to nil does not free memory while a variable still references it; also set the variable to nil.

## Tools
Luau garbage collector

## Topics
[[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
