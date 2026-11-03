---
title: "METATABLES - What are they and how can we use them?"
url: https://youtu.be/mtjCgqyZ5wk
creator: Crusherfire
official: false
advice_density: low
date: 2024-01-29
views: 86095
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# METATABLES - What are they and how can we use them?

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/mtjCgqyZ5wk) | crusherfiredev | 86,095 views | 2024-01-29

## Summary
Explains Luau metatables: attaching with setmetatable, defining metamethods (__add, __sub, __tostring, __unm) as helper functions, returning new tables to preserve immutability (const correctness), and re-attaching metatables to returned results.

## Tips
- [5:53](https://youtu.be/mtjCgqyZ5wk?t=353) **[[luau-language-and-types]]** Metamethods like __add must return a new table; mutating the input causes shared-reference bugs where two variables point to the same table.
- [13:26](https://youtu.be/mtjCgqyZ5wk?t=806) **[[luau-language-and-types]]** Re-attach the metatable with setmetatable on every returned result, otherwise chained operations fail with 'attempt to perform arithmetic on table'.
- [14:07](https://youtu.be/mtjCgqyZ5wk?t=847) **[[luau-language-and-types]]** Declare the metatable variable before the functions that reference it, then assign it afterward, to avoid unknown global errors.
- [15:29](https://youtu.be/mtjCgqyZ5wk?t=929) **[[luau-language-and-types]]** Use __tostring to define custom print output for tables, which makes debugging data structures much easier.

## Tools
Roblox Studio, Luau

## Topics
[[luau-language-and-types]]

Back to [[crusherfiredev - How to make successful Roblox games]]
