---
title: "Understanding When to Use Different Cases in Luau Scripting"
url: https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-08-11
views: 59
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Understanding When to Use Different Cases in Luau Scripting

[Open](https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987) | Roblox DevForum | 59 views | 2024-08-11

## Summary
Luau naming conventions guide from a DevForum post: when to use camelCase (locals, functions, member values, file names), PascalCase (classes, modules, types, services), LOUD_SNAKE_CASE (constants), and how to handle acronyms, plus consistency advice.

## Tips
- [page](https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987) **[[code-architecture-and-frameworks]]** Use PascalCase for class names, module scripts, constructors, exported types and Roblox service references like Players or DataStoreService.
- [page](https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987) **[[luau-language-and-types]]** Use camelCase for local variables, function names, member values and file names; use LOUD_SNAKE_CASE for constants that never change, e.g. MAX_HEALTH.
- [page](https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987) **[[luau-language-and-types]]** Write acronyms in mixed case within names (makeHttpRequest, JsonTable), but keep abbreviations fully capitalised (aRGBValue, XYZCoordinate).
- [page](https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987) **[[code-architecture-and-frameworks]]** Name each script after what it does, e.g. a script exporting a single function findPlayerLocation should be named findPlayerLocation.
- [page](https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987) **[[common-mistakes]]** Keep naming consistent across the whole project; if the team picks camelCase for variables, stick to it. In existing messy code, follow the existing style rather than refactoring it all.
- [page](https://devforum.roblox.com/t/understanding-when-to-use-different-cases-in-luau-scripting/3113987) **[[code-architecture-and-frameworks]]** Prioritise readability: names should clarify what a variable or function does, not obscure it.

## He points to
- Roblox Lua Style guide

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
