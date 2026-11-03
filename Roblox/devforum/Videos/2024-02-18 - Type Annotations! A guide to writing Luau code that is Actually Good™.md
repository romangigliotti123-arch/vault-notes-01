---
title: "Type Annotations! A guide to writing Luau code that is Actually Good™"
url: https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-02-18
views: 341
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Type Annotations! A guide to writing Luau code that is Actually Good™

[Open](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) | Roblox DevForum | 341 views | 2024-02-18

## Summary
DevForum tutorial on Luau type annotations for writing clearer, reusable code: --!strict, explicit types, nullable refinement, typeof/IsA, function and table types, prototype-based classes with exported Class types, typecasting, and any-casts for dynamic access.

## Tips
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Put --!strict at the top of every script so variables get inferred types instead of falling back to any.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Avoid any unless there is no alternative; it silences the type system entirely.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Refine nullable values with if-checks, and/or inline, early return, or assert before indexing them to avoid warnings.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Use typeof() for top-level concrete types and IsA() to downcast Instances to subclasses like BasePart or Terrain.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Use unknown for untyped external input and narrow it with type() or typeof() before use.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[code-architecture-and-frameworks]]** Build prototype-based classes: set Class.__index = Class, export typeof(setmetatable({} :: {...}, Class)) as the instance type, and annotate methods with self: Class.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Define reusable shapes with type aliases; use {T} for arrays and {[K]: V} for dictionaries keyed by any type, such as Player.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Use typecasts like {} :: {[Player]: number} to inline complex types compactly instead of multi-line annotations.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Write nullable function types as ((A) -> B)? because (A) -> B? means a function returning a nullable value.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Use (obj :: any) only for deliberate dynamic property access on concrete types, such as setting BodyColors properties by name.
- [page](https://devforum.roblox.com/t/type-annotations-a-guide-to-writing-luau-code-that-is-actually-good%E2%84%A2/2843221) **[[luau-language-and-types]]** Annotate typeof(template) as a type alias to type cloned template objects; if Parent warns, cast the new parent to any.

## Tools
Luau type checker, --!strict

## He points to
- Roblox Lua Style guide
- Roblox typechecking documentation (/types)

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
