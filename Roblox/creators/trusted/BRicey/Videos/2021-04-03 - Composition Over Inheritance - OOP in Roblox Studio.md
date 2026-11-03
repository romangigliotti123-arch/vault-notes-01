---
title: "Composition Over Inheritance - OOP in Roblox Studio"
url: https://youtu.be/KNT-vjqB_qI
creator: B Ricey
official: false
advice_density: medium
date: 2021-04-03
views: 35218
transcript: manual-subs
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Composition Over Inheritance - OOP in Roblox Studio

[Watch](https://youtu.be/KNT-vjqB_qI) | BRicey | 35,218 views | 2021-04-03

## Summary
Tutorial on composition vs inheritance in Roblox Luau OOP. Uses a vehicle simulator example (Car, Plane, Boat) to show why has-a components (Engine, Wheel as mixins) scale better than an is-a inheritance hierarchy. Walks through module setup, constructors, and testing in Studio.

## Tips
- [1:15](https://youtu.be/KNT-vjqB_qI?t=75) **[[code-architecture-and-frameworks]]** Avoid deep is-a inheritance trees for varied game objects; a Plane sharing Car code gets messy. Prefer composition for scalable class design.
- [3:25](https://youtu.be/KNT-vjqB_qI?t=205) **[[code-architecture-and-frameworks]]** Model entities as has-a: build reusable components (Engine, Wheel) and assemble each class from them, so a boat-car is just a combination of existing parts.
- [6:18](https://youtu.be/KNT-vjqB_qI?t=378) **[[code-architecture-and-frameworks]]** Don't inherit from Roblox Instances in Luau; hold a reference to the model inside your class table (composition) since models are C++-backed.
- [7:36](https://youtu.be/KNT-vjqB_qI?t=456) **[[code-architecture-and-frameworks]]** Keep hard references to Workspace models out of component modules; pass the model into Car.new() so one class can drive multiple models.
- [9:01](https://youtu.be/KNT-vjqB_qI?t=541) **[[code-architecture-and-frameworks]]** Use the standard Roblox pattern: module with Class.__index = Class, Class.new() returning setmetatable({...}, Class), and methods defined with colon syntax.
- [14:28](https://youtu.be/KNT-vjqB_qI?t=868) **[[code-architecture-and-frameworks]]** Avoid copying all component methods onto the main class table; it hides where methods live and makes code harder to read. Call through components like self.Engine:TurnOn().
- [15:29](https://youtu.be/KNT-vjqB_qI?t=929) **[[code-architecture-and-frameworks]]** Search for 'mixins' when learning composition; the term is used across Lua class libraries and JavaScript.

## Tools
Roblox Studio, Luau

## He points to
- Creator's own OOP series (metatables and modules)
- Multiple inheritance video linked in description

## Quotes
- [15:29](https://youtu.be/KNT-vjqB_qI?t=929) "I haven't really found a use to use inheritance when composition wouldn't work, so I've just been using that all the time."

## Topics
[[code-architecture-and-frameworks]]

Back to [[BRicey - How to make successful Roblox games]]
