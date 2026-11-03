---
title: "Docs: tutorials / fundamentals / coding-5 / make-changes-to-arrays"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-5/make-changes-to-arrays.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-5 / make-changes-to-arrays

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/make-changes-to-arrays.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial on Luau table functions for arrays: adding with table.insert, removing last or by index with table.remove, searching with table.find or custom for-loop search, and safely removing all duplicates by looping backward.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/make-changes-to-arrays) **[[code-architecture-and-frameworks]]** Use table.insert(array, value) to add values to an array rather than manual index assignment.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/make-changes-to-arrays) **[[luau-language-and-types]]** table.remove(array, index) only accepts a numeric index; passing a string value like "Potion" causes an error.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/make-changes-to-arrays) **[[luau-language-and-types]]** Removing items shifts later indexes down; when removing multiple matches, loop backward from #array to 1 to avoid skipping values.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/make-changes-to-arrays) **[[luau-language-and-types]]** Use return inside a for loop to stop searching at the first match and send the index back.

## Tools
Luau table library (table.insert, table.remove, table.find), Roblox Studio Output window

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
