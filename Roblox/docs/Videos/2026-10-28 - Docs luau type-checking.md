---
title: "Docs: luau / type-checking"
url: https://create.roblox.com/docs/luau/type-checking.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / type-checking

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/type-checking.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page on Luau type checking: gradual typing via annotations and inference, the three mode directives (--!nocheck, --!nonstrict, --!strict), primitive/Roblox/literal types, casts, function, table, variadic, union/intersection, typeof, generic and exported types.

## Tips
- [page](https://create.roblox.com/docs/luau/type-checking) **[[luau-language-and-types]]** Add --!strict as the first line of scripts to assert all inferred and annotated types and surface mismatches as warnings in Script Analysis.
- [page](https://create.roblox.com/docs/luau/type-checking) **[[luau-language-and-types]]** Set a default type-check mode for all scripts via Workspace.LuauTypeCheckMode, then override per script as needed.
- [page](https://create.roblox.com/docs/luau/type-checking) **[[luau-language-and-types]]** Annotate function parameters and return types so Luau warns on wrong argument types instead of erroring at runtime.
- [page](https://create.roblox.com/docs/luau/type-checking) **[[luau-language-and-types]]** Use the ...type syntax (e.g. (...number) -> number) for variadic functional types; (...: number) only works in function definitions.

## Numbers
- [page](https://create.roblox.com/docs/luau/type-checking) Inference modes: **3 (nocheck, nonstrict, strict)** (set on first line of script; nonstrict is the default-typed mode)
- [page](https://create.roblox.com/docs/luau/type-checking) Primitive annotation types: **4 (nil, boolean, number, string)** (plus Roblox classes, data types and enums as types)

## Tools
Luau type checker, Script Editor, Script Analysis window

## Topics
[[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
