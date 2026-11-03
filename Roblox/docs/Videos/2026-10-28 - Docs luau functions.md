---
title: "Docs: luau / functions"
url: https://create.roblox.com/docs/luau/functions.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / functions

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/functions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Luau documentation on functions: basic function definition, parameters (extra args ignored, missing args become nil), multiple return values, methods using colon notation and self, callbacks (e.g. table.sort with anonymous function), and variadic functions with ... and unpack().

## Tips
- [page](https://create.roblox.com/docs/luau/functions) **[[luau-language-and-types]]** Use colon notation (:) to call methods so self is passed automatically; table:Method() is identical to table.Method(table).
- [page](https://create.roblox.com/docs/luau/functions) **[[luau-language-and-types]]** Remember Luau ignores extra arguments and passes nil for missing ones; missing args cause errors like arithmetic on nil.
- [page](https://create.roblox.com/docs/luau/functions) **[[luau-language-and-types]]** Do not place code between a return statement and its end keyword; Luau throws an error.
- [page](https://create.roblox.com/docs/luau/functions) **[[luau-language-and-types]]** Variadic token ... cannot be used inside nested functions defined within a variadic function; pack it into a table first.

## Topics
[[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
