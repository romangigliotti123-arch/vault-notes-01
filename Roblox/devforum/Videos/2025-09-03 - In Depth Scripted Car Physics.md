---
title: "In Depth Scripted Car Physics"
url: https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-09-03
views: 207
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# In Depth Scripted Car Physics

[Open](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) | Roblox DevForum | 207 views | 2025-09-03

## Summary
Tutorial on building scripted car physics in Roblox without SpringConstraints. Covers suspension theory (Hooke's law, damped spring equation), rig setup, VectorForce-based springs, and raycast-based ground detection. Assumes no Server Authority; later sections cover advanced traction and throttle curves.

## Tips
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[physics-pathfinding-and-npc-ai]]** Use VectorForce with RelativeTo World and raycast-based springs instead of SpringConstraints for more control over suspension behaviour.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[physics-pathfinding-and-npc-ai]]** Set wheel parts Anchored=false, CanCollide=false, CanQuery=false, CanTouch=false so visual wheels don't bounce the car.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[physics-pathfinding-and-npc-ai]]** Set damping roughly 10x lower than stiffness as a starting point (example: STIFFNESS 10, DAMPING 1), then tune by testing.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[physics-pathfinding-and-npc-ai]]** Raycast down only to rest length plus wheel radius, not infinity, so the car isn't flung when driving off ramps.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[physics-pathfinding-and-npc-ai]]** Exclude the whole car model in RaycastParams and set RespectCanCollide=true so wheels don't snap to the car body or walls.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[physics-pathfinding-and-npc-ai]]** Reset each VectorForce to zero when the wheel has no ground hit, otherwise the car keeps floating away.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[scripting-and-performance]]** Set Instance parent last after configuring properties, especially for Attachments whose WorldPosition changes when parented.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[scripting-and-performance]]** Compute point velocity as AssemblyLinearVelocity + AssemblyAngularVelocity:Cross(point - part.Position) since built-in GetVelocityAtPosition reportedly doesn't work reliably.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[common-mistakes]]** Don't use infinite raycast length for suspension; it applies huge forces when airborne and launches the car.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[common-mistakes]]** Don't keep wheels collidable if they are only visual; they will hit the floor and make the car bounce incorrectly.
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) **[[scripting-and-performance]]** The tutorial's code is not production-ready and omits optimisation; modify before shipping.

## Numbers
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) STIFFNESS: **10** (Example starting spring stiffness in tutorial)
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) DAMPING: **1** (Example starting damping; rule of thumb 10x less than stiffness)
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) REST_LENGTH: **2 studs** (Example spring rest length from body centre)
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) WHEEL_RADIUS: **1.5 studs** (Example wheel radius (largest Size axis / 2))
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) Car body size: **7x1x13.5** (Example rig base part dimensions)
- [page](https://devforum.roblox.com/t/in-depth-scripted-car-physics/3915628) Wheel size: **0.5x3x3 rotated (90,0,0)** (Example wheel dimensions; minimum advised about half a stud)

## Tools
Roblox Studio, Luau, VectorForce, Attachment, RaycastParams, workspace:Raycast

## He points to
- Understanding Raycasting - DevForum Community Tutorials
- Comprehensive Beginner's Guide to CFrames - DevForum Community Tutorials

## Topics
[[common-mistakes]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
