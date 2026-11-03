---
title: "The Basics Of Basic Optimization"
url: https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756
creator: Roblox DevForum
official: false
advice_density: medium
date: 2016-07-05
views: 443
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# The Basics Of Basic Optimization

[Open](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) | Roblox DevForum | 443 views | 2016-07-05

## Summary
Old (2016) basic Luau optimization tutorial: localize globals/functions, cache repeated math and CFrame results, cache method lookups to cut __index calls, and time code with tick(). Author notes the 2019 Lua VM update made some of these tricks (table.index, global-caching) unnecessary; profile before assuming gains.

## Tips
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) **[[scripting-and-performance]]** Profile before and after optimizing; the author warns some changes may have no effect, since the newer Luau VM already handles some optimizations.
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) **[[luau-language-and-types]]** Declare frequently used globals and functions as locals (e.g. local sqrt = math.sqrt) so lookups skip the global table.
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) **[[scripting-and-performance]]** Precompute constant values like CFrame.new(0,1,0) outside loops instead of recreating them every iteration.
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) **[[scripting-and-performance]]** Cache indexed methods and constructors (e.g. Workspace.FindPartOnRay, Vector3.new) in locals to reduce repeated __index calls inside loops.
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) **[[analytics-metrics]]** Time code by storing tick() before a loop of repeated calls and printing tick() minus start afterward, to compare versions.
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) **[[common-mistakes]]** Do not sacrifice readability for micro-optimizations; apply basic optimizations that keep code easy to read.

## Numbers
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) CameraScript script performance after optimization: **reduced from 3%-5% to 0.5%-2%**
- [page](https://devforum.roblox.com/t/the-basics-of-basic-optimization/26756) Wait interval in loop example: **1/30 second per wait()**

## Tools
tick()

## He points to
- AxisAngle (advanced optimization)

## Topics
[[analytics-metrics]] [[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
