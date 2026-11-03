---
title: "Scripts vs Local Scripts vs Module Scripts, When should you use them?"
url: https://youtu.be/48XmvyD2F5o
creator: PineappleDev
official: false
advice_density: low
date: 2023-11-07
views: 2399
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Scripts vs Local Scripts vs Module Scripts, When should you use them?

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/48XmvyD2F5o) | pineappledevv | 2,399 views | 2023-11-07

## Summary
Explains the three Roblox script types: Script (server-side, ServerScriptService, saves data and shared state), LocalScript (client-only, StarterPlayerScripts/StarterGui for UI), and ModuleScript (reusable code, typically in ReplicatedStorage, loaded with require).

## Tips
- [0:20](https://youtu.be/48XmvyD2F5o?t=20) **[[client-server-and-remotes]]** Put server-authoritative logic (saving data, shared game state visible to all players) in regular Scripts in ServerScriptService; LocalScripts only affect the local player.
- [1:01](https://youtu.be/48XmvyD2F5o?t=61) **[[client-server-and-remotes]]** Use LocalScripts for single-player visuals and UI like menus, placed in StarterPlayerScripts or StarterGui; the server does not know about these changes.
- [1:50](https://youtu.be/48XmvyD2F5o?t=110) **[[code-architecture-and-frameworks]]** Store reusable functions and tables in ModuleScripts in ReplicatedStorage so both server and client scripts can require them instead of rewriting code.
- [3:51](https://youtu.be/48XmvyD2F5o?t=231) **[[data-persistence]]** Save player data only through server Scripts; DataStore saving cannot be done from a LocalScript.

## Tools
Roblox Studio

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]]

Back to [[pineappledevv - How to make successful Roblox games]]
