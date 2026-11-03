---
title: "Object Oriented Programming in Roblox Studio"
url: https://youtu.be/PByZNBuob4g
creator: SimTek Game Development
official: false
advice_density: medium
date: 2025-05-25
views: 25374
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Object Oriented Programming in Roblox Studio

[Watch](https://youtu.be/PByZNBuob4g) | SimTekGameDevelopment | 25,374 views | 2025-05-25

## Summary
Beginner tutorial on object-oriented programming in Luau for Roblox: tables as classes, metatables with __index for inheritance, constructors via setmetatable, the colon/self convention, and building Dog, GuardDog and Puppy module-script classes used by a manager script. Mostly technical, no monetisation or growth content.

## Tips
- [0:00](https://youtu.be/PByZNBuob4g?t=0) **[[code-architecture-and-frameworks]]** Organise NPC or game logic as classes: a base module with shared behaviour, and subclasses that inherit it via metatables so you write less code.
- [6:28](https://youtu.be/PByZNBuob4g?t=388) **[[luau-language-and-types]]** Pattern for inheritance: set Subclass.__index = Subclass, setmetatable(Subclass, {__index = Base}), and create objects with setmetatable(obj, Subclass).
- [10:38](https://youtu.be/PByZNBuob4g?t=638) **[[luau-language-and-types]]** Use colon syntax (obj:method()) so self is passed implicitly; obj.method(obj) is the equivalent explicit call and works when colon calls would fail.
- [4:28](https://youtu.be/PByZNBuob4g?t=268) **[[luau-language-and-types]]** Print tables to the output with Log mode turned off in the output window to inspect their contents.
- [12:42](https://youtu.be/PByZNBuob4g?t=762) **[[testing-debugging-and-qa]]** Test incrementally after each small change; forgetting to return the object from a constructor is an easy-to-miss bug.
- [16:08](https://youtu.be/PByZNBuob4g?t=968) **[[code-architecture-and-frameworks]]** Put shared class modules in ReplicatedStorage and require them from server scripts such as a manager script that creates instances.

## Tools
Roblox Studio, Luau, Output window

## He points to
- Lua documentation on metatables and metamethods (linked in video description)

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[testing-debugging-and-qa]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
