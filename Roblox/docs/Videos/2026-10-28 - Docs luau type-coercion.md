---
title: "Docs: luau / type-coercion"
url: https://create.roblox.com/docs/luau/type-coercion.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / type-coercion

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/type-coercion.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Luau type coercion. Explains that Luau implicitly converts values for arithmetic (strings to numbers), concatenation (numbers to strings), and property assignment (numbers/strings to enum values, numbers to Lighting.TimeOfDay strings). Recommends explicit enum names and string.format for number-to-string conversion.

## Tips
- [page](https://create.roblox.com/docs/luau/type-coercion) **[[luau-language-and-types]]** Use string.format() instead of concatenation coercion when converting numbers to strings, e.g. string.format("%.3f", x) for fixed decimals.
- [page](https://create.roblox.com/docs/luau/type-coercion) **[[luau-language-and-types]]** Assign full enum names (Enum.Material.Concrete) rather than numbers or strings; it is best practice and most explicit.
- [page](https://create.roblox.com/docs/luau/type-coercion) **[[common-mistakes]]** Arithmetic on a non-numeric string ("hello" + 234) throws a runtime error and stops the rest of the script; validate input types first.
- [page](https://create.roblox.com/docs/luau/type-coercion) **[[luau-language-and-types]]** Coercion happens at run time per operation and does not change the stored variable's value.

## Topics
[[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
