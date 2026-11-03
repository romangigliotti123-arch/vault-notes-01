---
title: "Docs: luau / strings"
url: https://create.roblox.com/docs/luau/strings.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / strings

[Open](https://create.roblox.com/docs/luau/strings.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Luau docs page on strings: declaration (quotes, multi-line brackets), concatenation, tonumber conversion, escape sequences, backtick string interpolation, automatic string-to-number arithmetic, lexicographic comparison pitfalls, and the full Lua pattern reference (character classes, magic characters, anchors, modifiers, sets, captures, position captures).

## Tips
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Compare numeric strings with tonumber() first; string comparison is lexicographic by ASCII, so "100" < "20" is true.
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Use tonumber() to convert strings; it returns nil when no numeric representation exists, so check for nil before using the result.
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Concatenation with .. adds no spaces; include spaces explicitly, or pass multiple arguments to print() which separates them with spaces.
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Prefer backtick interpolation (`Hello {name}`) over concatenation to embed variables and expressions in strings.
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Escape magic characters ($ % ^ * ( ) . [ ] + - ?) with % in patterns when matching them literally, e.g. "roblox%.com".
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Anchor patterns with ^ and $ together ("^Roblox$") to match the entire string rather than a substring.
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Wrap character classes in a set ([%l%p]+) when one quantifier must apply to multiple classes; without brackets the quantifier binds only to the last class.
- [page](https://create.roblox.com/docs/luau/strings) **[[luau-language-and-types]]** Use %1-%9 in gsub replacements; captures beyond nine can't be referenced with this syntax even though up to 32 captures are allowed.

## Numbers
- [page](https://create.roblox.com/docs/luau/strings) Max capture groups per pattern: **32** (Luau limit; only first nine referenceable in gsub replacements)
- [page](https://create.roblox.com/docs/luau/strings) Magic characters: **12** (Reserved in patterns; escape with % to match literally)

## He points to
- Lua 5.1 Manual (ranges in sets)

## Topics
[[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
