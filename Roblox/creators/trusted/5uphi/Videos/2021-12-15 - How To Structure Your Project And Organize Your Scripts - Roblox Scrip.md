---
title: "How To Structure Your Project And Organize Your Scripts - Roblox Scripting Tutorial"
url: https://youtu.be/YsXijBUUmmM
creator: Suphi Kaner
official: false
advice_density: medium
date: 2021-12-15
views: 55863
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How To Structure Your Project And Organize Your Scripts - Roblox Scripting Tutorial

[Watch](https://youtu.be/YsXijBUUmmM) | 5uphi | 55,863 views | 2021-12-15

## Summary
Shows how to structure a Roblox project with a global module loader in ServerScriptService: auto-require all ModuleScripts into a global table, then call initialize/initiate in order to avoid load-order errors. Also demonstrates a simple OOP class using metatables and a client-side equivalent in ReplicatedFirst with a loading screen.

## Tips
- [1:07](https://youtu.be/YsXijBUUmmM?t=67) **[[code-architecture-and-frameworks]]** Auto-require every ModuleScript under a folder into one global table keyed by script name; module names must be unique or they overwrite each other.
- [4:22](https://youtu.be/YsXijBUUmmM?t=262) **[[code-architecture-and-frameworks]]** Fix load-order errors by calling an initialize pass on all modules after all are required, then an initiate pass, so modules can safely use each other.
- [6:29](https://youtu.be/YsXijBUUmmM?t=389) **[[code-architecture-and-frameworks]]** Split module setup into two phases (initialize for setup, initiate for cross-module calls) so dependencies exist before use.
- [7:36](https://youtu.be/YsXijBUUmmM?t=456) **[[code-architecture-and-frameworks]]** Build classes with a metatable: set module.__index = module, put shared methods on the module table and per-object data on the self table to save memory.
- [14:55](https://youtu.be/YsXijBUUmmM?t=895) **[[code-architecture-and-frameworks]]** On the client, use a LocalScript in ReplicatedFirst that waits for game.Loaded, runs the same loader, then destroys a custom loading screen after initiation.

## Tools
Roblox Studio

## Topics
[[code-architecture-and-frameworks]]

Back to [[5uphi - How to make successful Roblox games]]
