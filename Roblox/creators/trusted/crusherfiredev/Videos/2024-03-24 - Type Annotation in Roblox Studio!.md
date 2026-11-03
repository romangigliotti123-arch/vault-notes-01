---
title: "Type Annotation in Roblox Studio!"
url: https://youtu.be/gowHu-r-zXg
creator: Crusherfire
official: false
advice_density: low
date: 2024-03-24
views: 26134
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Type Annotation in Roblox Studio!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/gowHu-r-zXg) | crusherfiredev | 26,134 views | 2024-03-24

## Summary
Tutorial on Luau type annotation in Roblox Studio: dynamic vs static typing, strict mode, parameter/return annotations, union and literal types, type refinement, custom types, intersection types, function types, variadic types, type casting, optional parameters, and generics (including a generic map function). Mostly language/tooling reference with no game-business advice.

## Tips
- [2:11](https://youtu.be/gowHu-r-zXg?t=131) **[[luau-language-and-types]]** Add the comment --!strict at the top of a script to make the type checker assert inferred and annotated types throughout the file.
- [3:56](https://youtu.be/gowHu-r-zXg?t=236) **[[luau-language-and-types]]** Annotate function parameters and return types (e.g. a: number) so Studio autofill and the linter catch wrong argument types before runtime.
- [8:00](https://youtu.be/gowHu-r-zXg?t=480) **[[luau-language-and-types]]** Annotate variables like Instance types (e.g. Humanoid) to get property autofill instead of typing properties from memory.
- [18:41](https://youtu.be/gowHu-r-zXg?t=1121) **[[luau-language-and-types]]** Use type casting (value :: Type) only when the inferred type is too generic, such as casting BasePart to MeshPart.

## Tools
Roblox Studio script analysis (strict mode, non-strict beta setting), Luau type checker / linter

## Topics
[[luau-language-and-types]]

Back to [[crusherfiredev - How to make successful Roblox games]]
