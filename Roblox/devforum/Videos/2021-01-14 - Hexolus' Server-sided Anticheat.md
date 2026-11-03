---
title: "Hexolus' Server-sided Anticheat"
url: https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-01-14
views: 170
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Hexolus' Server-sided Anticheat

[Open](https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706) | Roblox DevForum | 170 views | 2021-01-14

## Summary
Hexcede's open-source server-sided anticheat for Roblox (CC0), originally built for Hexolus. Checks movement exploits via per-physics-tick prediction and corrects players server-side without client code. Notes project is discontinued and being replaced by "Polygon".

## Tips
- [page](https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706) **[[client-server-and-remotes]]** Server-authoritative checks need no client code: predict each player's position every physics tick and correct violations on the server, avoiding lag-back for other players.
- [page](https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706) **[[anti-exploit-and-security]]** Drop the anticheat into ServerScriptService; test it against incompatible features and disable or adjust checks/thresholds that conflict with custom physics.
- [page](https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706) **[[anti-exploit-and-security]]** Anticheat works best for simple games that don't heavily customize physics, such as minigames; expect compatibility issues with custom physics.
- [page](https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706) **[[anti-exploit-and-security]]** Use Changed events on CFrame/Position to detect server-side teleports and scripted velocity updates, rather than relying on the client.

## Numbers
- [page](https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706) Checks covered: **Speed, teleport (vertical/horizontal separately), noclip, tool deletion, invalid tool drop, FE godmode** (Stable server-side checks listed by the anticheat)
- [page](https://devforum.roblox.com/t/hexolus-server-sided-anticheat/983706) Validation frequency: **Every physics tick** (Prediction and measurement run each physics tick)

## Tools
Hexolus-Anticheat (GitHub, CC0), Hexolus-OpenSource hub repo

## He points to
- https://github.com/Hexcede/Hexolus-Anticheat
- https://github.com/Hexcede/Hexolus-OpenSource
- grilme99 (Changed event CFrame/Position explanation)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
