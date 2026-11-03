---
title: "Modules and Remotes - Roblox Beginners Scripting Tutorial #2"
url: https://youtu.be/645dTG0lR38
creator: VuukStudios
official: false
advice_density: medium
date: 2025-09-24
views: 1302
transcript: auto-captions
confidence: high
tags: [roblox, vuukstudios7635, youtube-learn]
creator_trust: MIXED
creator_score: 7.4
---

> [!note] Trust: MIXED (credibility audit score 7.4): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Modules and Remotes - Roblox Beginners Scripting Tutorial #2

[Watch](https://youtu.be/645dTG0lR38) | vuukstudios7635 | 1,302 views | 2025-09-24

## Summary
Beginner Roblox scripting episode 2. Covers organizing the Explorer with assets folders (animations, SFX, VFX, models, remotes) and a shared folder split into client/server/misc module folders. Shows a client/server init pattern that requires all ModuleScripts in a folder and calls their init functions, plus RemoteEvent FireServer/FireAllClients communication with examples.

## Tips
- [1:24](https://youtu.be/645dTG0lR38?t=84) **[[code-architecture-and-frameworks]]** Organize the project in one place: an assets folder in ReplicatedStorage (animations, SFX, VFX, models, remotes) and a shared folder with client, server, and misc module subfolders.
- [4:04](https://youtu.be/645dTG0lR38?t=244) **[[code-architecture-and-frameworks]]** Use one client init LocalScript in StarterPlayerScripts that requires all ModuleScripts in the client folder and calls each module's init via task.spawn.
- [9:47](https://youtu.be/645dTG0lR38?t=587) **[[code-architecture-and-frameworks]]** Mirror the client init on the server with a server Script, but skip the wait-for-game-loaded line since the server starts before clients.
- [7:44](https://youtu.be/645dTG0lR38?t=464) **[[code-architecture-and-frameworks]]** Keep all code inside each module's init function and avoid writing top-level code outside it, so every script has one consistent entry point.
- [12:45](https://youtu.be/645dTG0lR38?t=765) **[[client-server-and-remotes]]** Use RemoteEvents to communicate between client and server: FireServer sends client to server, FireAllClients sends server to clients, and OnServerEvent/OnClientEvent receive them.
- [16:10](https://youtu.be/645dTG0lR38?t=970) **[[client-server-and-remotes]]** Pass the player as the first argument when firing a RemoteEvent to the server, since the server receives the firing player first.
- [16:51](https://youtu.be/645dTG0lR38?t=1011) **[[client-server-and-remotes]]** Change visual properties like part colour on the server, not only on the client, or other players will not see the change.
- [19:33](https://youtu.be/645dTG0lR38?t=1173) **[[client-server-and-remotes]]** Use remotes to coordinate systems such as combat and abilities, so an ability cast can block M1 attacks between client and server.

## Tools
Roblox Studio, Explorer, ModuleScript, RemoteEvent, task.spawn, task.wait

## He points to
- Creator's academy (linked in description)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]]

Back to [[vuukstudios7635 - How to make successful Roblox games]]
