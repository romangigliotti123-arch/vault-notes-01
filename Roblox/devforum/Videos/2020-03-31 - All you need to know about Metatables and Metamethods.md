---
title: "All you need to know about Metatables and Metamethods"
url: https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-03-31
views: 720
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# All you need to know about Metatables and Metamethods

[Open](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) | Roblox DevForum | 720 views | 2020-03-31

## Summary
Tutorial on Luau metatables and metamethods: setmetatable/getmetatable, __index (function and table), __newindex, operator overloading (__add, __concat, __lt, __eq, __unm), proxy tables, weak tables via __mode, rawget/rawset/rawequal, string and userdata metatables, and why Roblox locks metatables and how exploiters bypass them with getrawmetatable.

## Tips
- [page](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) **[[anti-exploit-and-security]]** Never rely on client-side property checks like WalkSpeed > 16 to catch speed exploits; exploiters can spoof reads via getrawmetatable __index hooks. Validate on the server.
- [page](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) **[[luau-language-and-types]]** Use rawget/rawset/rawequal inside metamethods to avoid re-triggering __index/__newindex/__eq and causing infinite recursion or C-stack overflow.
- [page](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) **[[luau-language-and-types]]** Metamethods only fire when a key is missing (__index) or new (__newindex); __newindex does not fire on updating existing keys.
- [page](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) **[[data-persistence]]** Use __mode weak tables ("k", "v", "kv") for caches so entries are collected when nothing else references them; note Roblox disables collectgarbage() and __gc.
- [page](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) **[[code-architecture-and-frameworks]]** Use __index pointing to a backup table for default values or class-style lookups, sharing keys between a table and its fallback.
- [page](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) **[[luau-language-and-types]]** For operator overloading, metamethods must be set on both operands for __eq; order matters for __add/__concat, so check operand types inside the function.
- [page](https://devforum.roblox.com/t/all-you-need-to-know-about-metatables-and-metamethods/503259) **[[luau-language-and-types]]** Roblox does not support __gc and forced garbage collection; do not depend on collectgarbage() to free memory.

## Tools
setmetatable, getmetatable, rawget, rawset, rawequal, newproxy, getrawmetatable, collectgarbage

## He points to
- Roblox Dev wiki metamethods page
- Lua 5.1 manual

## Topics
[[anti-exploit-and-security]] [[code-architecture-and-frameworks]] [[data-persistence]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
