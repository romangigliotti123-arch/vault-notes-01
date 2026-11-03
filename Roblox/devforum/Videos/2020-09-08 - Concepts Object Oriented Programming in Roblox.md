---
title: "Concepts: Object Oriented Programming in Roblox"
url: https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-09-08
views: 587
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Concepts: Object Oriented Programming in Roblox

[Open](https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267) | Roblox DevForum | 587 views | 2020-09-08

## Summary
Jonbyte's DevForum tutorial teaching object-oriented programming in Luau: objects as tables, colon syntax and self, constructors, ModuleScript classes, metatables with __index for prototype-based OOP, plus encapsulation, inheritance and polymorphism. Notes deep inheritance chains should be avoided.

## Tips
- [page](https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267) **[[luau-language-and-types]]** Use colon syntax (obj:Method()) for methods; it is sugar for obj.Method(obj), so self is passed automatically.
- [page](https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267) **[[code-architecture-and-frameworks]]** Build reusable objects with a ModuleScript constructor (Car.new) so each script doesn't redefine the constructor.
- [page](https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267) **[[scripting-and-performance]]** Put shared methods on a prototype table with Prototype.__index = Prototype and setmetatable on instances to avoid duplicating functions per object (DRY, less memory).
- [page](https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267) **[[scripting-and-performance]]** Set __index to a table, not a function, to keep Luau's fast method calls; avoid __index functions and deep __index chains.
- [page](https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267) **[[code-architecture-and-frameworks]]** Avoid deep inheritance chains; they increase complexity and a broken parent prototype breaks all its children. Prefer composition.
- [page](https://devforum.roblox.com/t/concepts-object-oriented-programming-in-roblox/761267) **[[luau-language-and-types]]** Prefix private fields and methods with an underscore (_secret) as a convention; Luau has no access modifiers.

## He points to
- https://luau-lang.org/
- https://developer.roblox.com/en-us/articles/Metatables
- https://devforum.roblox.com/t/all-about-object-oriented-programming/8585
- https://roblox.github.io/lua-style-guide/#metatables
- https://www.lua.org/pil/16.html

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
