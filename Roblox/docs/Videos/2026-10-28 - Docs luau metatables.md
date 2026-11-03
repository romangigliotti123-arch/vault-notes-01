---
title: "Docs: luau / metatables"
url: https://create.roblox.com/docs/luau/metatables.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / metatables

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/metatables.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Luau documentation on metatables: setmetatable/getmetatable, the metamethod list (__index, __newindex, __call, arithmetic, __tostring, __metatable, __eq/__lt), operator overloading examples, rawset to avoid recursion, weak tables via __mode, and a Set datatype implementation.

## Tips
- [page](https://create.roblox.com/docs/luau/metatables) **[[luau-language-and-types]]** Use rawset inside __index when __newindex is also defined; otherwise t[i]=v re-triggers __newindex and can cause stack overflow.
- [page](https://create.roblox.com/docs/luau/metatables) **[[luau-language-and-types]]** __eq and __lt only fire when both operands share the same metamethod function and basic type; mixed table/userdata comparisons don't use them.
- [page](https://create.roblox.com/docs/luau/metatables) **[[luau-language-and-types]]** Arithmetic metamethods receive operands in either order; check types of both args, since scalar division is not commutative.
- [page](https://create.roblox.com/docs/luau/metatables) **[[luau-language-and-types]]** Set __mode to 'k', 'v', or 'kv' for weak tables; omitted modes stay strong. Don't rely on when GC removes entries.

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
