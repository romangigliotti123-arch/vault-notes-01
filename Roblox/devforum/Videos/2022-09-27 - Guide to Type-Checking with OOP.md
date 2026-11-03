---
title: "Guide to Type-Checking with OOP"
url: https://devforum.roblox.com/t/guide-to-type-checking-with-oop/1997394
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-09-27
views: 196
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Guide to Type-Checking with OOP

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/guide-to-type-checking-with-oop/1997394) | Roblox DevForum | 196 views | 2022-09-27

## Summary
Developer tutorial on typing Luau OOP classes with typeof(setmetatable(...)) and export types, covering single classes and inheritance via & intersection and metatable chaining. Purely technical; no Roblox business or growth advice.

## Tips
- [page](https://devforum.roblox.com/t/guide-to-type-checking-with-oop/1997394) **[[code-architecture-and-frameworks]]** Define class structure as a type 'self', then export Car = typeof(setmetatable({} :: self, Car)) so other scripts can require and reuse the type.
- [page](https://devforum.roblox.com/t/guide-to-type-checking-with-oop/1997394) **[[luau-language-and-types]]** Annotate methods with dot syntax and an explicit self: Car.Boost(self: Car) so Luau types self and still allows colon-call syntax.
- [page](https://devforum.roblox.com/t/guide-to-type-checking-with-oop/1997394) **[[luau-language-and-types]]** For inheritance, define Truck type as typeof(setmetatable({} :: self, Truck)) & Car.Car to combine child fields with parent type.
- [page](https://devforum.roblox.com/t/guide-to-type-checking-with-oop/1997394) **[[luau-language-and-types]]** In subclass constructors, wrap the parent constructor result as setmetatable(Car.new() :: Truck, Truck) to avoid type errors.

## Tools
Luau type checker

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
