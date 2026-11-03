---
title: "Docs: scripting / security / defensive-design"
url: https://create.roblox.com/docs/scripting/security/defensive-design.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / defensive-design

[Open](https://create.roblox.com/docs/scripting/security/defensive-design.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on defensive design against exploiters. Core principle: design systems where cheating is impossible or pointless rather than detecting it after the fact. Gives obby, combat, and economy examples contrasting reactive detection with defensive design.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/defensive-design) **[[common-mistakes]]** Don't rely on complex detection code to catch exploiters; they will find a way around it. Change the design so the abuse yields no advantage.
- [page](https://create.roblox.com/docs/scripting/security/defensive-design) **[[anti-exploit-and-security]]** Remove or reduce point gains for kills on newly spawned players to stop bot farming and discourage spawn camping.
- [page](https://create.roblox.com/docs/scripting/security/defensive-design) **[[anti-exploit-and-security]]** In obbies, use mandatory sequential checkpoints and have the server verify each was activated in order before granting rewards.
- [page](https://create.roblox.com/docs/scripting/security/defensive-design) **[[anti-exploit-and-security]]** Optionally flag players who finish stages faster than humanly possible, as an extra layer on top of checkpoint validation.
- [page](https://create.roblox.com/docs/scripting/security/defensive-design) **[[anti-exploit-and-security]]** Calculate all combat damage on the server from server-side weapon stats and validate hits with server-side raycasting.
- [page](https://create.roblox.com/docs/scripting/security/defensive-design) **[[anti-exploit-and-security]]** Prevent item duplication with server-side cooldowns and validate every transaction against current server-side inventory state.
- [page](https://create.roblox.com/docs/scripting/security/defensive-design) **[[anti-exploit-and-security]]** When designing any feature, ask how an exploiter would abuse it and change the design so abuse is impossible or worthless.

## Topics
[[anti-exploit-and-security]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
