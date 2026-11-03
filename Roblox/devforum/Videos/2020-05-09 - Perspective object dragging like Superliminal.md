---
title: "Perspective object dragging like Superliminal"
url: https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-05-09
views: 92
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Perspective object dragging like Superliminal

[Open](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) | Roblox DevForum | 92 views | 2020-05-09

## Summary
Tutorial on recreating Superliminal's perspective object dragging in Roblox: camera-relative CFrame holding, distance-based resizing, ray-cast clipping prevention, angle correction, RotatedRegion3 corner checks, and a tween to screen centre. Single-player first; multiplayer via network ownership is noted as a security risk.

## Tips
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) **[[scripting-and-performance]]** Anchor picked-up parts and zero Velocity/RotVelocity before dragging; an anchored part with velocity still acts as a conveyor.
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) **[[client-server-and-remotes]]** Transfer network ownership to the client via a RemoteEvent (SetNetworkOwner on server) so the client simulates physics; this approach is insecure in multiplayer.
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) **[[anti-exploit-and-security]]** Network ownership handed to clients can cause security issues in multiplayer; validate or find another ownership solution before shipping multiplayer.
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) **[[building-and-level-design]]** Use FindPartOnRayWithIgnoreList from the camera to find the furthest unobstructed position, ignoring the character and the held object.
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) **[[physics-pathfinding-and-npc-ai]]** Offset the part back by half its size along the ray to stop it clipping into nearby geometry.
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) **[[player-psychology-and-game-feel]]** Tween a picked-up object toward screen centre with Vector3:Lerp(…, 0.2) per frame instead of teleporting it, for smoother feel.
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) **[[development-process-and-speed]]** Prototype quickly: write the core idea in a simple first attempt, then iterate on the maths using trial and error; the whole build took about an hour.

## Numbers
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) Build time: **about 1 hour** (Full Superliminal-style mechanic, excluding writing the tutorial)
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) Final script length: **74 lines** (Complete drag-and-resize mechanic)
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) Ray length: **1000 studs** (Camera ray used to find furthest unobstructed position)
- [page](https://devforum.roblox.com/t/perspective-object-dragging-like-superliminal/566200) Lerp alpha for centring offset: **0.2** (Per-frame reduction of coolnessOffset for smooth tween)

## Tools
RotatedRegion3 (EgoMoose), Ray casting (FindPartOnRayWithIgnoreList), CFrame:ToObjectSpace / ToWorldSpace, RemoteEvent, SetNetworkOwner

## He points to
- Superliminal (game referenced as inspiration)
- EgoMoose rotated Region3 module
- Roblox Wiki on object space

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[client-server-and-remotes]] [[development-process-and-speed]] [[physics-pathfinding-and-npc-ai]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
