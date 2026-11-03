---
title: "All about Object Oriented Programming"
url: https://devforum.roblox.com/t/all-about-object-oriented-programming/8585
creator: Roblox DevForum
official: false
advice_density: medium
date: 2014-09-03
views: 2666
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# All about Object Oriented Programming

[Open](https://devforum.roblox.com/t/all-about-object-oriented-programming/8585) | Roblox DevForum | 2,666 views | 2014-09-03

## Summary
Tutorial on object-oriented programming in Luau for Roblox: explains objects as tables, constructors (Car.new), methods via colon syntax, __index metatables for method lookup, returning classes from ModuleScripts, and inheritance by setting a metatable on the child class to the parent.

## Tips
- [page](https://devforum.roblox.com/t/all-about-object-oriented-programming/8585) **[[code-architecture-and-frameworks]]** Define a class as a table with Class.__index = Class, a Class.new constructor, and methods on the same table; use setmetatable(obj, Class) so instances find methods.
- [page](https://devforum.roblox.com/t/all-about-object-oriented-programming/8585) **[[code-architecture-and-frameworks]]** Put functions in the class table, not in each instance table; copying functions into every object is inefficient and messy.
- [page](https://devforum.roblox.com/t/all-about-object-oriented-programming/8585) **[[code-architecture-and-frameworks]]** Split large scripts into ModuleScripts that end with 'return Class' so each class is small and easy to change.
- [page](https://devforum.roblox.com/t/all-about-object-oriented-programming/8585) **[[code-architecture-and-frameworks]]** For inheritance, have the child constructor call Parent.new, then setmetatable(Child, Parent) so inherited methods resolve; child methods override parent methods of the same name.
- [page](https://devforum.roblox.com/t/all-about-object-oriented-programming/8585) **[[luau-language-and-types]]** Use colon syntax (obj:Method()) for methods that act on an instance; it passes self automatically, equivalent to obj.Method(obj).

## He points to
- Wikipedia definition of object (OOP)

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
