---
title: "Docs: luau / variables"
url: https://create.roblox.com/docs/luau/variables.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / variables

[Open](https://create.roblox.com/docs/luau/variables.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Luau official docs page on variables: valid naming rules, case sensitivity, naming conventions (PascalCase for APIs/classes, camelCase locals, LOUD_SNAKE_CASE constants), reserved keywords, local vs global scope, multiple assignment, and const semantics including table contents and contextual keyword behaviour.

## Tips
- [page](https://create.roblox.com/docs/luau/variables) **[[luau-language-and-types]]** Declare variables with local rather than global scope; Luau accesses local variables faster than global ones.
- [page](https://create.roblox.com/docs/luau/variables) **[[luau-language-and-types]]** Use PascalCase for classes, enum-like objects and all Roblox APIs; camelCase for locals, member values and functions.
- [page](https://create.roblox.com/docs/luau/variables) **[[luau-language-and-types]]** Use LOUD_SNAKE_CASE for constants and values not expected to change.
- [page](https://create.roblox.com/docs/luau/variables) **[[luau-language-and-types]]** Spell out words fully in names; abbreviations make code harder to read.
- [page](https://create.roblox.com/docs/luau/variables) **[[luau-language-and-types]]** Avoid names like _VERSION (underscore plus all uppercase), which Luau may reserve for internal globals.
- [page](https://create.roblox.com/docs/luau/variables) **[[luau-language-and-types]]** Don't capitalise whole acronyms in names; write aJsonVariable or MakeHttpCall.
- [page](https://create.roblox.com/docs/luau/variables) **[[luau-language-and-types]]** Use const to prevent reassignment; it makes the binding immutable, not the table contents. Use Library.table.freeze() to freeze contents too.
- [page](https://create.roblox.com/docs/luau/variables) **[[common-mistakes]]** Extra values in a multiple assignment are silently dropped; missing values become nil.

## He points to
- Luau documentation on Scope

## Topics
[[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
