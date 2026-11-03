---
title: "What are Module Scripts? Roblox Scripting Explained"
url: https://youtu.be/HoLIx9tvT8w
creator: GnomeCode
official: false
advice_density: low
date: 2021-11-25
views: 205015
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# What are Module Scripts? Roblox Scripting Explained

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/HoLIx9tvT8w) | GnomeCode | 205,015 views | 2021-11-25

## Summary
Beginner tutorial on Roblox ModuleScripts: they can't run alone, must be required from another script; demonstrates storing data tables and functions in a module, requiring it, and accessing values/functions to keep code organized.

## Tips
- [0:00](https://youtu.be/HoLIx9tvT8w?t=0) **[[code-architecture-and-frameworks]]** Use ModuleScripts for reusable code; they only run when another script require()s them, so put shared data and functions there.
- [2:43](https://youtu.be/HoLIx9tvT8w?t=163) **[[code-architecture-and-frameworks]]** Store large data tables (items, prices, descriptions) in a ModuleScript instead of top of every script; require once and reuse across scripts.
- [4:05](https://youtu.be/HoLIx9tvT8w?t=245) **[[code-architecture-and-frameworks]]** Save a require() result to a local variable once at the top of a script, then access its fields or functions from that variable.
- [5:30](https://youtu.be/HoLIx9tvT8w?t=330) **[[code-architecture-and-frameworks]]** Keep main scripts as readable overviews that call module functions; move implementation details into the module for organization as projects grow.

## Tools
Roblox Studio

## Topics
[[code-architecture-and-frameworks]]

Back to [[GnomeCode - How to make successful Roblox games]]
