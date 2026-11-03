---
title: "Roblox OOP (Object Oriented Programming)"
url: https://devforum.roblox.com/t/roblox-oop-object-oriented-programming/1639499
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-01-22
views: 429
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Roblox OOP (Object Oriented Programming)

[Open](https://devforum.roblox.com/t/roblox-oop-object-oriented-programming/1639499) | Roblox DevForum | 429 views | 2022-01-22

## Summary
Dev_Simphony's web tutorial on Roblox OOP in Luau. Builds a Gun module with Gun.New constructor, metatables (__index, setmetatable) so objects get methods, then a Rocket module that inherits from Gun via setmetatable(Rocket, Gun) and adds a special move.

## Tips
- [page](https://devforum.roblox.com/t/roblox-oop-object-oriented-programming/1639499) **[[code-architecture-and-frameworks]]** Put shared modules in ReplicatedStorage/Shared, server-only modules in ServerStorage, and keep a single client LocalScript and a single server Script as entry points.
- [page](https://devforum.roblox.com/t/roblox-oop-object-oriented-programming/1639499) **[[code-architecture-and-frameworks]]** Use a module table with Module.__index = Module and a constructor that calls setmetatable(obj, Module) and returns obj; methods then work via colon syntax.
- [page](https://devforum.roblox.com/t/roblox-oop-object-oriented-programming/1639499) **[[code-architecture-and-frameworks]]** Forgetting to return the constructed object from the constructor makes method calls fail; always return the new table.
- [page](https://devforum.roblox.com/t/roblox-oop-object-oriented-programming/1639499) **[[code-architecture-and-frameworks]]** Use inheritance by requiring the base module and calling setmetatable(Child, Base) so child objects reuse base methods like Shoot while adding their own.

## Tools
Luau metatables (setmetatable, __index)

## Topics
[[code-architecture-and-frameworks]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
