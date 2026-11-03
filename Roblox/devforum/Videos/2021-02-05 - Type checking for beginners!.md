---
title: "Type checking for beginners!"
url: https://devforum.roblox.com/t/type-checking-for-beginners/1027242
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-02-05
views: 514
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Type checking for beginners!

[Open](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) | Roblox DevForum | 514 views | 2021-02-05

## Summary
Beginner tutorial on Luau type checking: enabling --!strict, primitive and Roblox types, union/nullable/intersection/assertion operators, typed functions, loops and events, custom table types with generics, and organizing types via exported ModuleScripts.

## Tips
- [page](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) **[[code-architecture-and-frameworks]]** Put --!strict at the top of every script you want type checked.
- [page](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) **[[luau-language-and-types]]** Add types with 'local name: Type'; Luau then warns on any later assignment of a different type.
- [page](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) **[[luau-language-and-types]]** Use type assertions (value :: type) to silence warnings when you know a value's type, e.g. any values from tonumber input.
- [page](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) **[[luau-language-and-types]]** Avoid annotating variables assigned on the same line; type inference already handles it, except for table and complex types.
- [page](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) **[[code-architecture-and-frameworks]]** Define shared types in a ModuleScript using 'export type' and require them where needed to keep scripts organized.
- [page](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) **[[client-server-and-remotes]]** Type RemoteEvent handler parameters (e.g. player: Player, name: string) to catch bad client-sent data early.
- [page](https://devforum.roblox.com/t/type-checking-for-beginners/1027242) **[[luau-language-and-types]]** Use intersection (&) of small table types to build reusable types such as Vector2 or Vector3 shapes.

## Tools
Luau type checker (--!strict)

## He points to
- Official Luau type checking docs

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
