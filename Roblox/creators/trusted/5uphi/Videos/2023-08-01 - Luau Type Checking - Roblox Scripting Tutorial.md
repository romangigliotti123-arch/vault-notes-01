---
title: "Luau Type Checking - Roblox Scripting Tutorial"
url: https://youtu.be/eRVDL7xlN8g
creator: Suphi Kaner
official: false
advice_density: medium
date: 2023-08-01
views: 24728
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Luau Type Checking - Roblox Scripting Tutorial

[Watch](https://youtu.be/eRVDL7xlN8g) | 5uphi | 24,728 views | 2023-08-01

## Summary
Tutorial on Luau type checking modes (none, non-strict, strict) in Roblox. Shows how strict mode infers types from values, while non-strict treats them as any. Walks through building Vector3 and Pet modules, adding type annotations, exporting types, and concludes strict mode is preferable because it infers types with less manual work.

## Tips
- [0:06](https://youtu.be/eRVDL7xlN8g?t=6) **[[luau-language-and-types]]** Enable the 'scripts are non-strict by default' beta feature, or add a mode comment at the top of each script, since the default is no-check.
- [2:11](https://youtu.be/eRVDL7xlN8g?t=131) **[[luau-language-and-types]]** Prefer strict mode: it infers variable types from values, whereas non-strict treats them as any and silently allows type mistakes.
- [3:37](https://youtu.be/eRVDL7xlN8g?t=217) **[[luau-language-and-types]]** Type checking has no runtime effect; it only catches mistakes at edit time, so it doesn't change game behaviour.
- [10:30](https://youtu.be/eRVDL7xlN8g?t=630) **[[luau-language-and-types]]** Annotate types on the variable declaration (e.g. local t: {x: number} = {...}); annotating only later does not enforce them.
- [11:53](https://youtu.be/eRVDL7xlN8g?t=713) **[[luau-language-and-types]]** Avoid optional '?' on fields you need always set; use it only when nil is valid, otherwise initialise every key in the table.
- [16:45](https://youtu.be/eRVDL7xlN8g?t=1005) **[[luau-language-and-types]]** Define reusable types with 'type Name = ...' and reference them by name instead of repeating the full table type.
- [17:28](https://youtu.be/eRVDL7xlN8g?t=1048) **[[luau-language-and-types]]** Use 'export type' to share types across modules so other scripts can require and annotate with them.
- [21:35](https://youtu.be/eRVDL7xlN8g?t=1295) **[[luau-language-and-types]]** In strict mode, function return types and export are inferred, so you can drop manual return annotations and export statements.

## Tools
Luau type checker

## Topics
[[luau-language-and-types]]

Back to [[5uphi - How to make successful Roblox games]]
