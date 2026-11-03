---
title: "Metatables - Roblox Scripting Tutorial"
url: https://youtu.be/bk8UVm-gxBs
creator: Suphi Kaner
official: false
advice_density: low
date: 2021-12-10
views: 35368
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Metatables - Roblox Scripting Tutorial

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/bk8UVm-gxBs) | 5uphi | 35,368 views | 2021-12-10

## Summary
Tutorial on Luau metatables: __index (default values and lookup fallback), __call, __add, __eq, and __tostring. Builds a Vector2-like data type, shows sharing methods via a metatable __index table to save memory, and explains colon method syntax and returning new objects from __add.

## Tips
- [4:15](https://youtu.be/bk8UVm-gxBs?t=255) **[[luau-language-and-types]]** Put shared methods in a metatable's __index table, not inside each instance, so every object reuses one function instead of allocating a new closure per object.
- [15:52](https://youtu.be/bk8UVm-gxBs?t=952) **[[scripting-and-performance]]** Roblox now makes identical functions raw-equal; avoid capturing per-instance variables in methods so closures stay identical and shared in memory.
- [13:48](https://youtu.be/bk8UVm-gxBs?t=828) **[[luau-language-and-types]]** Define methods with colon syntax (function obj:method()) so self is passed automatically, matching Roblox built-in types like Vector2.
- [19:55](https://youtu.be/bk8UVm-gxBs?t=1195) **[[luau-language-and-types]]** In __add, return a new object instead of mutating the operands, matching Roblox's Vector2 behaviour and keeping original values unchanged.

## Numbers
- [9:53](https://youtu.be/bk8UVm-gxBs?t=593) Vector2 magnitude example result: **42 for (23,36) using sqrt(x*x+y*y) as written** (Example calculation in tutorial, not a benchmark)

## Tools
Roblox Studio, Luau

## Topics
[[luau-language-and-types]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
