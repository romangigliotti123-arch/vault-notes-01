---
title: "Efficient Object Oriented Programming Tutorial"
url: https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-02-21
views: 228
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Efficient Object Oriented Programming Tutorial

[Open](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) | Roblox DevForum | 228 views | 2021-02-21

## Summary
Tutorial on building an efficient, memory-friendly OOP system in Roblox Luau. Covers __index metatable classes, a custom Rcade class/__call/__init system, single-inheritance via __super, metamethod inheritance, event listener helpers, and default values via class tables.

## Tips
- [page](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) **[[scripting-and-performance]]** Put methods on the class table and use __index metatables, not per-object closures; each object otherwise allocates duplicate functions, wasting memory.
- [page](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) **[[code-architecture-and-frameworks]]** Use a base Rcade.class wrapper with __call and __init so classes are created via Class(...) and share one constructor pattern across the project.
- [page](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) **[[code-architecture-and-frameworks]]** Implement inheritance with a __super field and an Rcade __index that falls back to the superclass; call super __init explicitly from the subclass __init.
- [page](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) **[[code-architecture-and-frameworks]]** Copy metamethods (keys starting with __, excluding __super and __init) from the superclass onto subclasses so __tostring etc. are inherited; note this slightly increases memory.
- [page](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) **[[client-server-and-remotes]]** Wrap event connections in a helper that forwards to a named method on self (eventListener/remoteListener/bindToClose) to keep class methods as the event handlers.
- [page](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) **[[data-persistence]]** Set references to Roblox instances (e.g. Player) to nil on object cleanup, and add a destroy method, to avoid memory leaks from objects holding instances.
- [page](https://devforum.roblox.com/t/efficient-object-oriented-programming-tutorial/1061153) **[[scripting-and-performance]]** Declare default property values in the class table (Rcade.class{name='NO NAME'}) rather than using 'or' in __init, so setting a field to nil still falls back to the default.

## Tools
Roblox Studio, Luau metatables, ModuleScripts

## He points to
- All about Object Oriented Programming (Roblox DevForum community tutorial, 2014, edited 2020)
- Rcade Example Kit (Roblox model by SuperSpeedy101)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
