---
title: "Docs: studio / optimization / memory-usage"
url: https://create.roblox.com/docs/studio/optimization/memory-usage.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / optimization / memory-usage

[Open](https://create.roblox.com/docs/studio/optimization/memory-usage.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on monitoring memory usage in the Developer Console. Covers the Memory tool (CoreMemory, PlaceMemory, PlaceScriptMemory categories) for real-time usage, and the Luau heap tool for snapshots, views (Graph, Object Tags, Memory Categories, Object Classes, Unique References/Unparented Instances) and finding leaked instances.

## Tips
- [page](https://create.roblox.com/docs/studio/optimization/memory-usage) **[[scripting-and-performance]]** Monitor memory in the Developer Console (F9) during testing and live sessions; memory limits can crash user devices or servers.
- [page](https://create.roblox.com/docs/studio/optimization/memory-usage) **[[optimization-and-streaming]]** Focus on PlaceMemory and PlaceScriptMemory in the Memory tool; they show how your building and scripting choices affect memory use.
- [page](https://create.roblox.com/docs/studio/optimization/memory-usage) **[[testing-debugging-and-qa]]** Take multiple Luau heap snapshots over time and compare them to find memory growth.
- [page](https://create.roblox.com/docs/studio/optimization/memory-usage) **[[scripting-and-performance]]** Use debug.setmemorycategory to assign custom memory category names so script memory is easier to attribute.
- [page](https://create.roblox.com/docs/studio/optimization/memory-usage) **[[common-mistakes]]** Disconnect and destroy instances you no longer need; check Unique References and Unparented Instances views for leaked, unparented instances still pinned by scripts.
- [page](https://create.roblox.com/docs/studio/optimization/memory-usage) **[[scripting-and-performance]]** Check Graph view paths (registry, upvalue, env, array) to see what is holding references keeping objects alive.

## Numbers
- [page](https://create.roblox.com/docs/studio/optimization/memory-usage) Graph view node threshold: **Elements under 2 KB shown as a single '…' node** (Luau heap Graph view aggregation)

## Tools
Developer Console (F9 / /console), Memory tool, Luau heap tool, debug.setmemorycategory

## He points to
- Performance Optimization (Roblox docs)

## Topics
[[common-mistakes]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
