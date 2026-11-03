---
title: "Object-Oriented Programming in Roblox Studio!"
url: https://youtu.be/9VHThbipoFs
creator: Crusherfire
official: false
advice_density: medium
date: 2024-02-21
views: 35750
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Object-Oriented Programming in Roblox Studio!

[Watch](https://youtu.be/9VHThbipoFs) | crusherfiredev | 35,750 views | 2024-02-21

## Summary
Tutorial on imitating object-oriented programming in Luau using tables and metatables. Builds a custom Vector2 class via a ModuleScript: constructor with new(), colon-method self passing, __index metamethod, __div for scalar division, and const-correct methods returning new objects. Ends with a dot-product demo.

## Tips
- [2:06](https://youtu.be/9VHThbipoFs?t=126) **[[code-architecture-and-frameworks]]** Put each class in a ModuleScript that returns a table; expose a new() constructor and require it from other scripts to create objects.
- [2:47](https://youtu.be/9VHThbipoFs?t=167) **[[luau-language-and-types]]** Store class methods in a separate metatable and set it on each instance; add a __index metamethod pointing to that table, or method lookups on objects will fail.
- [5:56](https://youtu.be/9VHThbipoFs?t=356) **[[luau-language-and-types]]** Tag instances with a hidden type key (e.g. _type = 'Vector2') and check it in methods, throwing an error on wrong argument types.
- [7:48](https://youtu.be/9VHThbipoFs?t=468) **[[luau-language-and-types]]** Call methods with colon syntax so the object is passed automatically as self; dot calls silently ignore the object.
- [17:48](https://youtu.be/9VHThbipoFs?t=1068) **[[common-mistakes]]** Don't mutate self inside methods that return values; return a new object instead (const correctness) to avoid aliasing bugs where two variables share one table.
- [12:00](https://youtu.be/9VHThbipoFs?t=720) **[[testing-debugging-and-qa]]** The Studio command bar can show spurious errors with ModuleScripts; run the game to verify the real behaviour.

## Tools
Roblox Studio, ModuleScript, Luau metatables

## He points to
- Creator's earlier video on metatables (linked in description)

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]] [[testing-debugging-and-qa]]

Back to [[crusherfiredev - How to make successful Roblox games]]
