---
title: "Docs: luau / operators"
url: https://create.roblox.com/docs/luau/operators.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / operators

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/operators.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Luau reference page for operators: logical (and, or, not), comparison, arithmetic (including floor division and exponentiation), compound assignment (+=, ..=, etc.), and miscellaneous concatenation and length operators, with truthiness rules and metamethod mappings.

## Tips
- [page](https://create.roblox.com/docs/luau/operators) **[[luau-language-and-types]]** In Luau, zero and the empty string are truthy, unlike many languages. Don't use 0 or "" as falsy sentinels; check for nil or false explicitly.
- [page](https://create.roblox.com/docs/luau/operators) **[[luau-language-and-types]]** Use 'x or default' to supply fallback values when x may be nil or false, e.g. local y = x or 1.
- [page](https://create.roblox.com/docs/luau/operators) **[[luau-language-and-types]]** Use 'not variable' to branch when a variable is nil or false; it also works for negating multi-condition expressions.
- [page](https://create.roblox.com/docs/luau/operators) **[[luau-language-and-types]]** Compound assignment (+=, -=, ..=, etc.) evaluates the operation once, so an expression with side effects such as a random index is only computed one time.

## Topics
[[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
