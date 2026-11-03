---
title: "I built my own Module Loader! (it's epic)"
url: https://youtu.be/dJjZ7ml9bSo
creator: Crusherfire
official: false
advice_density: medium
date: 2025-08-10
views: 31874
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# I built my own Module Loader! (it's epic)

[Watch](https://youtu.be/dJjZ7ml9bSo) | crusherfiredev | 31,874 views | 2025-08-10

## Summary
Walkthrough of a free single-script-architecture Module Loader (Marketplace model) for Roblox: setup, module lifecycle (require, initialize, start), attributes like client-only, server-only relocation, parallel actors, loader priority, ignore loader, and error/yield warnings. Shows a real use in Clothing Factory Tycoon 2.

## Tips
- [0:32](https://youtu.be/dJjZ7ml9bSo?t=32) **[[code-architecture-and-frameworks]]** Use a single server script and single local script that require a Module Loader, then load modules from containers or CollectionService tags, treating modules like custom services.
- [3:07](https://youtu.be/dJjZ7ml9bSo?t=187) **[[code-architecture-and-frameworks]]** Put event connections and setup in initialize; put long-running loops in start. Handle already-present players with task.defer when listening to PlayerAdded.
- [9:18](https://youtu.be/dJjZ7ml9bSo?t=558) **[[scripting-and-performance]]** Never yield inside initialize or start; yielding stalls the loader for every other module. Loader warns after a yield threshold is exceeded.
- [12:13](https://youtu.be/dJjZ7ml9bSo?t=733) **[[anti-exploit-and-security]]** Mark server-only code as server-only and relocate it to ServerScriptService so exploiters cannot decompile it from ReplicatedStorage.
- [14:42](https://youtu.be/dJjZ7ml9bSo?t=882) **[[anti-exploit-and-security]]** After relocating a module, use normal require paths for shared modules; require-by-string parent lookups break because the parent changes.
- [17:23](https://youtu.be/dJjZ7ml9bSo?t=1043) **[[testing-debugging-and-qa]]** Rely on the loader's error handling: a failing initialize or start logs a warning with stack trace without halting other modules. Enable verbose loading while debugging.
- [27:55](https://youtu.be/dJjZ7ml9bSo?t=1675) **[[code-architecture-and-frameworks]]** Set a loader priority attribute with a high number on critical modules like data service to guarantee they load first.
- [28:51](https://youtu.be/dJjZ7ml9bSo?t=1731) **[[testing-debugging-and-qa]]** Use an ignore-loader boolean attribute to temporarily disable a module without deleting it.
- [21:14](https://youtu.be/dJjZ7ml9bSo?t=1274) **[[scripting-and-performance]]** Parallel modules run in separate actors with separate Luau VMs, so require caching is not shared; do not expect shared state across them.
- [22:59](https://youtu.be/dJjZ7ml9bSo?t=1379) **[[code-architecture-and-frameworks]]** Organise shared code into universal and game-specific folders, and keep reusable services as packages to reuse across multiple games.

## Numbers
- [9:59](https://youtu.be/dJjZ7ml9bSo?t=599) Yield warning interval: **loader warns after 10s yield threshold, repeats every 5s** (Module loader yield warning behaviour in demo)
- [31874](https://youtu.be/dJjZ7ml9bSo?t=31874) Video views: **31874** (Video view count at upload (2025-08-10))

## Games
- **Clothing Factory Tycoon 2** [22:18](https://youtu.be/dJjZ7ml9bSo?t=1338): Uses module loader with universal and game-specific module folders, relocates server checkout logic to ServerScriptService, and keeps most setup in initialize.

## Tools
Module Loader (Roblox Marketplace, single-script architecture), CollectionService, Actors (parallel Luau), Roblox Studio Output

## He points to
- Module Loader on Roblox Marketplace (linked in video description)
- Creator's video on task.defer

## Quotes
- [22:18](https://youtu.be/dJjZ7ml9bSo?t=1338) "Do you need to use a module loader? Absolutely not. You can structure the scripts in your game however you want."
- [12:13](https://youtu.be/dJjZ7ml9bSo?t=733) "If your server code is inside of replicated storage inside of a module script, that means any exploiter can steal your code."

## Topics
[[anti-exploit-and-security]] [[code-architecture-and-frameworks]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[crusherfiredev - How to make successful Roblox games]]
