---
title: "Docs: luau / scope"
url: https://create.roblox.com/docs/luau/scope.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / scope

[Open](https://create.roblox.com/docs/luau/scope.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Luau docs on scope: global vs local variables and functions, local-scope performance benefits, capture (upvalues) and shadowing, and why ModuleScripts are needed to share values between scripts.

## Tips
- [page](https://create.roblox.com/docs/luau/scope) **[[luau-language-and-types]]** Declare variables and functions with local by default; globals are slower and use more memory than locals.
- [page](https://create.roblox.com/docs/luau/scope) **[[luau-language-and-types]]** Global access in a time-critical loop can make code more than 10% slower than using a local in the same loop.
- [page](https://create.roblox.com/docs/luau/scope) **[[code-architecture-and-frameworks]]** Use ModuleScripts to share values and functions between scripts; globals and locals are not accessible across scripts.
- [page](https://create.roblox.com/docs/luau/scope) **[[luau-language-and-types]]** Redeclaring a local without assigning a value sets it to nil; be aware this creates a new shadow variable rather than overwriting the outer one.

## Numbers
- [page](https://create.roblox.com/docs/luau/scope) Performance penalty of global variable in time-critical loop: **>10% slower vs local** (Luau uses hash lookup for globals in the same loop)

## He points to
- Const variables documentation
- ModuleScript documentation

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
