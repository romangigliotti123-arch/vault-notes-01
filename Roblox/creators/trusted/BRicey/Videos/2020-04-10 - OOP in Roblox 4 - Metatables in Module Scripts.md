---
title: "OOP in Roblox #4 - Metatables in Module Scripts"
url: https://youtu.be/CyWDg0T5ilg
creator: B Ricey
official: false
advice_density: medium
date: 2020-04-10
views: 22406
transcript: manual-subs
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# OOP in Roblox #4 - Metatables in Module Scripts

[Watch](https://youtu.be/CyWDg0T5ilg) | BRicey | 22,406 views | 2020-04-10

## Summary
Tutorial on combining module scripts with metatables for OOP in Roblox. Shows a Base class with a New constructor that sets __index to itself, a Child module inheriting from Base via require, and a normal script reading an inherited value. Explains abstraction benefits for team code organisation.

## Tips
- [0:50](https://youtu.be/CyWDg0T5ilg?t=50) **[[code-architecture-and-frameworks]]** Put base class in a ModuleScript that sets __index to itself, and a New() constructor using self so child classes inherit correctly without skipping a generation.
- [4:34](https://youtu.be/CyWDg0T5ilg?t=274) **[[code-architecture-and-frameworks]]** Create child classes by requiring the base and calling base:New(); child metatable points to base, giving inheritance through module scripts.
- [5:59](https://youtu.be/CyWDg0T5ilg?t=359) **[[code-architecture-and-frameworks]]** Use only dot indexing inside module scripts for OOP code; it is cleaner and reads like other OOP languages.
- [7:48](https://youtu.be/CyWDg0T5ilg?t=468) **[[code-architecture-and-frameworks]]** Combine metatables with module scripts so normal scripts can share OOP classes without bindables or bindable events passing metatables around.
- [8:33](https://youtu.be/CyWDg0T5ilg?t=513) **[[code-architecture-and-frameworks]]** Encapsulate logic in module-script classes so main scripts stay simple and teammates only need to know the public functions.

## Tools
Roblox Studio

## He points to
- OOP in Roblox #3 (previous video in series)

## Topics
[[code-architecture-and-frameworks]]

Back to [[BRicey - How to make successful Roblox games]]
