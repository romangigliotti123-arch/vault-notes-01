---
title: "All About Tables (the first of two tutorials on the subject)"
url: https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-12-07
views: 111
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# All About Tables (the first of two tutorials on the subject)

[Open](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) | Roblox DevForum | 111 views | 2019-12-07

## Summary
Phlegethon5778's comprehensive Lua tables tutorial (part 1). Covers arrays vs dictionaries, mixed tables, table key identity (tables index by reference), insert/remove, concat, pack/unpack, ipairs/pairs/next ordering, and the pitfalls of removing during iteration and the # operator. Explicitly not Roblox-specific.

## Tips
- [page](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) **[[luau-language-and-types]]** Use numeric or ipairs loops for arrays to guarantee order; on Roblox ipairs is now as fast or faster than numeric for loops.
- [page](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) **[[luau-language-and-types]]** Use pairs for dictionaries since order is not guaranteed; stick with one iterator consistently in a codebase.
- [page](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) **[[common-mistakes]]** Don't call table.remove while looping with ipairs; the iterator doesn't account for length changes and skips elements.
- [page](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) **[[common-mistakes]]** Table keys match by reference, not contents: x[{"a"}] will not find a value set with a different table literal. Store the table in a variable and reuse it.
- [page](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) **[[common-mistakes]]** The # operator only counts the array part; use a pairs-based counter to get the full size of a dictionary-containing table.
- [page](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) **[[common-mistakes]]** Avoid table.insert/table.remove at arbitrary positions in large tables; shifting elements is inefficient.
- [page](https://devforum.roblox.com/t/all-about-tables-the-first-of-two-tutorials-on-the-subject/402930) **[[luau-language-and-types]]** Use table.pack and table.unpack to copy array parts; table.concat joins array elements with an optional delimiter.

## Tools
Luau, table library (insert, remove, concat, pack, unpack)

## He points to
- Associative array (general concept, linked in article)
- ScriptGuider DevForum answer on table.concat
- HaxHelper (Luau ipairs performance info)

## Topics
[[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
