---
title: "Docs: luau / comments"
url: https://create.roblox.com/docs/luau/comments.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / comments

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/comments.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Luau documentation on comments: single-line (--) and block (--[[ ]], --[=[ ]=]) comments, TODO comments, hover tooltips from block comments placed before declarations, and comment directives (--!strict, --!nonstrict, --!nocheck, --!native, --!nolint, --!optimize 0|1|2) controlling type checking, native codegen, linting and optimization.

## Tips
- [page](https://create.roblox.com/docs/luau/comments) **[[titles-descriptions]]** Use block comments before functions or objects to describe intent; Script Editor shows them as on-hover tooltips, including inside typeof() type expressions.
- [page](https://create.roblox.com/docs/luau/comments) **[[code-architecture-and-frameworks]]** Put a block comment at the top of each file describing its purpose.
- [page](https://create.roblox.com/docs/luau/comments) **[[luau-language-and-types]]** Use --!strict at the top of scripts to enable strict type checking.
- [page](https://create.roblox.com/docs/luau/comments) **[[optimization-and-streaming]]** Keep --!optimize at default values unless you have a specific reason; level 1 is default in Studio testing, level 2 in live games.

## Numbers
- [page](https://create.roblox.com/docs/luau/comments) Optimization level default (Studio testing): **--!optimize 1** (Basic optimizations; default in Studio testing)
- [page](https://create.roblox.com/docs/luau/comments) Optimization level default (live games): **--!optimize 2** (Further optimizations; default in live games)
- [page](https://create.roblox.com/docs/luau/comments) Studio linter warning codes enabled: **1, 2, 3, 6, 10-15, 17-28** (Subset of Luau linter codes enabled by Roblox Studio)

## Tools
Roblox Studio Script Editor, Luau type checker, Luau linter, Luau compiler

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[optimization-and-streaming]] [[testing-debugging-and-qa]] [[titles-descriptions]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
