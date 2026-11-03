---
title: "Docs: luau / stacks"
url: https://create.roblox.com/docs/luau/stacks.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / stacks

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/stacks.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs page on stacks (LIFO) in Luau. Shows a generic Stack ModuleScript class (new, isEmpty, push, pop) built on a table with table.insert/table.remove, stored in ReplicatedStorage, plus a usage example. Warns not to pop from an empty stack.

## Tips
- [page](https://create.roblox.com/docs/luau/stacks) **[[luau-language-and-types]]** Implement a stack in Luau with a plain table: table.insert to push, table.remove(t, #t) to pop. Luau has no built-in stack type.
- [page](https://create.roblox.com/docs/luau/stacks) **[[code-architecture-and-frameworks]]** Put reusable data-structure modules in ReplicatedStorage as ModuleScripts so both client and server can require them.
- [page](https://create.roblox.com/docs/luau/stacks) **[[common-mistakes]]** Guard pop() with an isEmpty() check; popping an empty stack returns nil and can cause errors downstream.

## Tools
ModuleScript, table.insert, table.remove, setmetatable

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
