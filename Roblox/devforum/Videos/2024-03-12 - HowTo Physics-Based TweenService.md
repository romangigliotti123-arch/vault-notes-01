---
title: "HowTo: Physics-Based TweenService"
url: https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-03-12
views: 189
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# HowTo: Physics-Based TweenService

[Open](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) | Roblox DevForum | 189 views | 2024-03-12

## Summary
Shows a technique to make TweenService-driven platforms carry physics-based occupants: step the tween on RenderStepped via TweenService:GetValue(), PivotTo the model, and set AssemblyLinearVelocity/AngularVelocity on touching parts each frame (conveyor-belt method), so the native PGS solver moves players with the platform.

## Tips
- [page](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) **[[core-loops-and-game-design]]** Plain TweenService on moving platforms makes players slide off; drive the movement per frame and feed velocity to touching parts instead.
- [page](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) **[[client-server-and-remotes]]** Run the moving-platform animation on the client, and set network ownership of touching assemblies to the client for smooth performance.
- [page](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) **[[scripting-and-performance]]** Step the platform on RunService:BindToRenderStep at priority 99 (RenderStepped), not Heartbeat, so physics solves with the new velocities that frame.
- [page](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) **[[physics-pathfinding-and-npc-ai]]** Set AssemblyLinearVelocity = (newPos - oldPos) / deltaTime and AssemblyAngularVelocity from the rotation delta on each part of the moving model.
- [page](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) **[[luau-language-and-types]]** Use TweenService:GetValue(alpha, style, direction) as a pure easing function, with your own alpha accumulator, to get per-frame control instead of Tween:Play().

## Numbers
- [page](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) Tween duration in example: **10 seconds** (Example tween duration in the GetValue loop script)

## Tools
TweenService, RunService, AssemblyLinearVelocity, AssemblyAngularVelocity, PivotTo

## He points to
- Sawhorse Interactive
- Supersocial
- Red Manta
- @SigmaTechRBLX

## Quotes
- [page](https://devforum.roblox.com/t/howto-physics-based-tweenservice/2873727) "Heartbeat is done after physics is calculated. At that point, it'd be too late."

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[luau-language-and-types]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
