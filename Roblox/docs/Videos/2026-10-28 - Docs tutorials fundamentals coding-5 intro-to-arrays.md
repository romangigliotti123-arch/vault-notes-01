---
title: "Docs: tutorials / fundamentals / coding-5 / intro-to-arrays"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-5/intro-to-arrays.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-5 / intro-to-arrays

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/intro-to-arrays.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on arrays in Luau. Builds a talking NPC that cycles through a dialogue array using indexes, dialogueIndex counter, and #array size to wrap back to index 1. Covers index basics, out-of-range nil errors, and random selection via Random.new().

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/intro-to-arrays) **[[luau-language-and-types]]** Arrays are 1-indexed in Luau; the first value is index 1, unlike 0-indexed languages like Java. Indexing past the end (e.g. arr[4] on a 3-item array) throws a nil error.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/intro-to-arrays) **[[luau-language-and-types]]** Use #array (no space after #) to get array length; use it to wrap an index counter back to 1 instead of erroring at the end.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/intro-to-arrays) **[[luau-language-and-types]]** Use Random.new():NextInteger(1, #array) to pick a random array element by index.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/intro-to-arrays) **[[scripting-and-performance]]** The legacy Chat API shown is for demonstration only; in real games use TextChatService.

## Tools
Roblox Studio, Luau, Explorer, ProximityPrompt

## Topics
[[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
