---
title: "LinearVelocity vs. VectorForce vs. AssemblyLinearVelocity in Roblox"
url: https://youtu.be/ArNJwChSU8Q
creator: SimTek Game Development
official: false
advice_density: medium
date: 2023-09-22
views: 62326
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# LinearVelocity vs. VectorForce vs. AssemblyLinearVelocity in Roblox

[Watch](https://youtu.be/ArNJwChSU8Q) | SimTekGameDevelopment | 62,326 views | 2023-09-22

## Summary
Technical Roblox tutorial comparing three physics movers for projectiles: LinearVelocity constraint (holds constant speed, needs MaxForce), VectorForce (continuous acceleration, speeds up unbounded), and AssemblyLinearVelocity (one-shot initial velocity, decays with friction). Builds a ball-thrower demo in a rig script using all three.

## Tips
- [0:00](https://youtu.be/ArNJwChSU8Q?t=0) **[[physics-pathfinding-and-npc-ai]]** Use LinearVelocity constraint to hold a constant speed (e.g. rolling ball); it applies whatever force is needed, so set MaxForce to math.huge.
- [0:00](https://youtu.be/ArNJwChSU8Q?t=0) **[[physics-pathfinding-and-npc-ai]]** Use VectorForce for continuous acceleration; the object keeps speeding up until opposed by gravity or other forces.
- [0:00](https://youtu.be/ArNJwChSU8Q?t=0) **[[physics-pathfinding-and-npc-ai]]** Use AssemblyLinearVelocity for one-shot impulses like knockback or pool shots; velocity decays over time from friction.
- [0:00](https://youtu.be/ArNJwChSU8Q?t=0) **[[physics-pathfinding-and-npc-ai]]** Set LinearVelocity RelativeTo to World when direction should be world-space rather than attachment-relative.
- [6:12](https://youtu.be/ArNJwChSU8Q?t=372) **[[physics-pathfinding-and-npc-ai]]** Multiply a spawn CFrame by CFrame.new(x,y,z) relative to the HumanoidRootPart so spawned objects stay in front of the rig when it rotates.
- [8:58](https://youtu.be/ArNJwChSU8Q?t=538) **[[data-persistence]]** Use Debris:AddItem(obj, TTL) to clean up spawned projectiles automatically instead of manual destroy code.
- [10:23](https://youtu.be/ArNJwChSU8Q?t=623) **[[physics-pathfinding-and-npc-ai]]** Keep spawn templates in ServerStorage and clone them into Workspace when needed.
- [13:09](https://youtu.be/ArNJwChSU8Q?t=789) **[[physics-pathfinding-and-npc-ai]]** For VectorForce, compute force as mass times a chosen factor (e.g. Mass*20) and tune by trial; force and velocity are not directly equivalent.

## Numbers
- [8:58](https://youtu.be/ArNJwChSU8Q?t=538) Debris time to live: **10 seconds** (Cleanup TTL used for all spawned balls in demo)
- [8:58](https://youtu.be/ArNJwChSU8Q?t=538) Spawn count: **5 balls per type** (Loop spawns five balls with one-second waits)
- [8:17](https://youtu.be/ArNJwChSU8Q?t=497) Default LinearVelocity speed in demo: **1 stud/s before speed increase** (Unscaled look vector magnitude is one)

## Tools
Roblox Studio, Luau, LinearVelocity constraint, VectorForce constraint, AssemblyLinearVelocity property, Debris service

## Quotes
- [14:31](https://youtu.be/ArNJwChSU8Q?t=871) "For knockback with VectorForce, the force keeps applying, so for that you really shouldn't be using VectorForce; use assembly linear velocity."

## Topics
[[data-persistence]] [[physics-pathfinding-and-npc-ai]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
