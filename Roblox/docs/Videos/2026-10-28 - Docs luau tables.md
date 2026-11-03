---
title: "Docs: luau / tables"
url: https://create.roblox.com/docs/luau/tables.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: luau / tables

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/luau/tables.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs reference on Luau tables: creating, reading, writing, iterating and removing items in arrays and dictionaries; reference semantics; shallow and deep cloning; freezing tables (shallow and deep) with table.freeze and table.isfrozen.

## Tips
- [page](https://create.roblox.com/docs/luau/tables) **[[luau-language-and-types]]** Luau arrays are 1-based; the first element is [1], not [0]. Remember this when indexing or looping.
- [page](https://create.roblox.com/docs/luau/tables) **[[luau-language-and-types]]** Use table.insert(array, value) or array[#array+1] to append; table.insert(array, pos, value) to insert mid-array (shifts following items up).
- [page](https://create.roblox.com/docs/luau/tables) **[[luau-language-and-types]]** Use table.remove(array, pos) to remove mid-array; following items shift back one index. Setting an element to nil in an array does not shift items.
- [page](https://create.roblox.com/docs/luau/tables) **[[luau-language-and-types]]** Assigning a table to a new variable creates a reference, not a copy; changes through either variable affect the original.

## Numbers
- [page](https://create.roblox.com/docs/luau/tables) array index base: **1** (Luau arrays start at index 1, not 0)

## Tools
Luau table library (table.insert, table.remove, table.clone, table.freeze, table.isfrozen)

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
