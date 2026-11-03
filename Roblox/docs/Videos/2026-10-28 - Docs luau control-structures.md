---
title: "Docs: luau / control-structures"
url: https://create.roblox.com/docs/luau/control-structures.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / control-structures

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/control-structures.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Luau docs page on control structures: if/elseif/else, while, repeat-until, numeric and generic for loops, generalized iteration with __iter, break and continue. Includes warning about infinite loops needing a wait.

## Tips
- [page](https://create.roblox.com/docs/luau/control-structures) **[[common-mistakes]]** Always include a delay such as task.wait() inside infinite while loops; omitting it freezes the game and crashes Studio.
- [page](https://create.roblox.com/docs/luau/control-structures) **[[luau-language-and-types]]** In Luau, 0 and the empty string are truthy; only false and nil are falsy. Don't copy checks from other languages that treat 0 as false.
- [page](https://create.roblox.com/docs/luau/control-structures) **[[luau-language-and-types]]** Use ipairs() for arrays and pairs() for dictionaries; pairs() traversal order is arbitrary.
- [page](https://create.roblox.com/docs/luau/control-structures) **[[luau-language-and-types]]** Iterate tables directly with 'for i, v in t do' (generalized iteration) instead of ipairs() when appropriate.

## Topics
[[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
