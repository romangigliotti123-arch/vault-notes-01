---
title: "Full Beginner Guide To Metatables - What are they and every metamethod explained!"
url: https://devforum.roblox.com/t/full-beginner-guide-to-metatables-what-are-they-and-every-metamethod-explained/2505946
creator: Roblox DevForum
official: false
advice_density: low
date: 2023-08-04
views: 317
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Full Beginner Guide To Metatables - What are they and every metamethod explained!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/full-beginner-guide-to-metatables-what-are-they-and-every-metamethod-explained/2505946) | Roblox DevForum | 317 views | 2023-08-04

## Summary
Beginner tutorial on Luau metatables: setmetatable usage and an explanation of each metamethod (__index, __newindex, __tostring, __call, arithmetic ops, __unm, __eq, __lt, __le, __metatable, __len, __mode, __iter), with code examples. Mostly reference material, not game-design advice.

## Tips
- [page](https://devforum.roblox.com/t/full-beginner-guide-to-metatables-what-are-they-and-every-metamethod-explained/2505946) **[[luau-language-and-types]]** Use __index for default values or inheritance-like behaviour; it must return a value when a key is missing.
- [page](https://devforum.roblox.com/t/full-beginner-guide-to-metatables-what-are-they-and-every-metamethod-explained/2505946) **[[luau-language-and-types]]** Use __newindex to block or validate unwanted new keys on a table, enforcing rules on assignments.
- [page](https://devforum.roblox.com/t/full-beginner-guide-to-metatables-what-are-they-and-every-metamethod-explained/2505946) **[[code-architecture-and-frameworks]]** Use metatables judiciously to keep code readable; avoid unnecessary complexity.
- [page](https://devforum.roblox.com/t/full-beginner-guide-to-metatables-what-are-they-and-every-metamethod-explained/2505946) **[[luau-language-and-types]]** Both operands of __eq, __lt and __le should share the same metatable, otherwise the comparison fails.

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
