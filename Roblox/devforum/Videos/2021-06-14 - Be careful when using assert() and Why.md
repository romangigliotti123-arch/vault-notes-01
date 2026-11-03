---
title: "Be careful when using assert() and Why"
url: https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-06-14
views: 263
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# Be careful when using assert() and Why

[Open](https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175) | Roblox DevForum | 263 views | 2021-06-14

## Summary
DevForum post by EYYCHEEV arguing that assert() with a string-concatenated error message is costly because Lua evaluates arguments eagerly. Recommends if-else plus error() instead; a benchmark showed about 70% faster. Also suggests Luau type annotations to replace runtime type checks.

## Tips
- [page](https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175) **[[scripting-and-performance]]** Don't put string concatenation or tostring() in assert's message argument; Lua evaluates it on every call even when the condition passes.
- [page](https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175) **[[scripting-and-performance]]** Use an if-statement with error() for hot-path argument validation so the message is built only when the check fails.
- [page](https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175) **[[scripting-and-performance]]** Watch the Script Performance view in Studio; a sudden rise in script activity can come from costly assert message formatting.
- [page](https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175) **[[luau-language-and-types]]** Use Luau type annotations (e.g. number parameters) to move argument type checking to static analysis instead of runtime checks.
- [page](https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175) **[[common-mistakes]]** A custom assert wrapper that takes a message argument behaves the same as built-in assert and keeps the same eager-evaluation cost.

## Numbers
- [page](https://devforum.roblox.com/t/be-careful-when-using-assert-and-why/1289175) Benchmark speedup: **if-else + error() about 70% faster than assert() with concatenated message (6.9ms vs 22.9ms over 10,000 calls)** (Author's own test in Roblox Studio Play Solo)

## Tools
Script Performance view (Studio), assert(), error(), Luau type annotations

## He points to
- Programming in Lua (book, warns about assert message cost)
- LuaJIT wiki (warns about assert message cost)
- Defensive coding and failing fast (DevForum community tutorial)

## Topics
[[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
