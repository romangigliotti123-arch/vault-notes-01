---
title: "Docs: luau / native-code-gen"
url: https://create.roblox.com/docs/luau/native-code-gen.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / native-code-gen

[Open](https://create.roblox.com/docs/luau/native-code-gen.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on native code generation for Luau. Explains enabling --!native per script or @native per function, best practices (use on numeric/buffer-heavy server code, measure with Script Profiler), code patterns that deoptimize, type annotations (Vector3), Studio tooling (debugging, profiler, heap, debug.dumpcodesize), and compile limits and error fixes.

## Tips
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[luau-language-and-types]]** Enable native code generation only on server scripts doing heavy numeric work on tables or buffers; top-level code runs once and gains little.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[luau-language-and-types]]** Prefer @native on specific hot functions instead of --!native everywhere; native compilation adds server startup time, memory use, and a total code limit.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[optimization-and-streaming]]** Measure each function with and without native compilation using the Script Profiler before keeping it enabled.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[luau-language-and-types]]** Annotate function arguments with types, especially Vector3, so native code is specialized instead of checking for tables.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[luau-language-and-types]]** Avoid getfenv/setfenv, math functions called with non-numeric arguments, and mismatched argument types, since these deoptimize native code.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[testing-debugging-and-qa]]** Placing breakpoints disables native execution for those functions; remove breakpoints before profiling native performance.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[optimization-and-streaming]]** Run debug.dumpcodesize() in Server view to check native code size against the limit and find large compiled functions.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[optimization-and-streaming]]** If a function exceeds instruction limits, split it into smaller functions or move large ones into a separate non-native script.
- [page](https://create.roblox.com/docs/luau/native-code-gen) **[[optimization-and-streaming]]** If memory allocation limit is hit, remove --!native from memory-heavy scripts or move rarely called functions to non-native modules.

## Numbers
- [page](https://create.roblox.com/docs/luau/native-code-gen) single code block instruction limit: **64K instructions per block** (Exceeding this errors; split the function)
- [page](https://create.roblox.com/docs/luau/native-code-gen) function code block limit: **32K internal blocks** (Per function; simplify control flow or split)
- [page](https://create.roblox.com/docs/luau/native-code-gen) module instruction limit: **1 million instructions** (Total for entire script with native code)

## Tools
Script Profiler, Luau heap profiler, Roblox Studio Command Bar, debug.dumpcodesize()

## Topics
[[luau-language-and-types]] [[optimization-and-streaming]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
