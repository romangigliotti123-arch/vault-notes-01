---
title: "Functional Programming in Roblox Studio!"
url: https://youtu.be/p4AgsDML0hU
creator: Crusherfire
official: false
advice_density: low
date: 2024-03-09
views: 8179
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Functional Programming in Roblox Studio!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/p4AgsDML0hU) | crusherfiredev | 8,179 views | 2024-03-09

## Summary
Introduces functional programming in Luau. Covers pure vs impure functions, building filter, map and iterate helpers as generic functions, moving them into ModuleScripts for reuse, and using recursion instead of for loops. Ends with a note that OOP and FP can be mixed.

## Tips
- [1:22](https://youtu.be/p4AgsDML0hU?t=82) **[[code-architecture-and-frameworks]]** Write helper functions as pure functions: same inputs give same outputs, no reads of external variables. Pure functions can be safely moved into ModuleScripts and reused.
- [8:06](https://youtu.be/p4AgsDML0hU?t=486) **[[code-architecture-and-frameworks]]** Put shared utility functions (filter, map, iterate) in ModuleScripts and require them via game:GetService('ServerScriptService') from any script.
- [9:28](https://youtu.be/p4AgsDML0hU?t=568) **[[luau-language-and-types]]** Make utility functions generic (type T) with typed parameters so the Luau linter can autofill fields like animal.name instead of showing error type.
- [18:59](https://youtu.be/p4AgsDML0hU?t=1139) **[[luau-language-and-types]]** For recursive iteration, always include a bounds check (index < #array) as the stopping condition, or the function loops forever and indexes nil.

## Tools
Roblox Studio, Luau, ModuleScript

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[crusherfiredev - How to make successful Roblox games]]
