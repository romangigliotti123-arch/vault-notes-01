---
title: "Luau's New Type Solver: How to utilize type functions!"
url: https://devforum.roblox.com/t/luaus-new-type-solver-how-to-utilize-type-functions/3637378
creator: Roblox DevForum
official: false
advice_density: low
date: 2025-05-04
views: 173
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Luau's New Type Solver: How to utilize type functions!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/luaus-new-type-solver-how-to-utilize-type-functions/3637378) | Roblox DevForum | 173 views | 2025-05-04

## Summary
Web tutorial on Luau's New Type Solver: built-in type functions (keyof, rawkeyof, index, rawget, setmetatable, getmetatable), custom user-defined type functions using the types library and type instance methods (properties, readproperty, setproperty, setindexer, setparameters, setreturns, generics), read/write property modifiers, negation, union, and intersection types, plus examples from TypeForge and Class++.

## Tips
- [page](https://devforum.roblox.com/t/luaus-new-type-solver-how-to-utilize-type-functions/3637378) **[[luau-language-and-types]]** Use keyof<T> to derive a union of a table's keys instead of hand-writing key unions; use index<T, U> to get value types from key unions.
- [page](https://devforum.roblox.com/t/luaus-new-type-solver-how-to-utilize-type-functions/3637378) **[[luau-language-and-types]]** Use rawkeyof and rawget when you want to ignore metatables and only inspect a table's own properties.
- [page](https://devforum.roblox.com/t/luaus-new-type-solver-how-to-utilize-type-functions/3637378) **[[luau-language-and-types]]** Use the read and write keywords on table type properties to make them read-only or write-only; type errors are raised on violating access.
- [page](https://devforum.roblox.com/t/luaus-new-type-solver-how-to-utilize-type-functions/3637378) **[[luau-language-and-types]]** Custom type functions must return a type when called outside type functions, otherwise a type error is emitted.

## Tools
Luau New Type Solver, Luau types library, TypeForge (module of utility type functions), Class++ (class system module by TenebrisNoctua)

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
