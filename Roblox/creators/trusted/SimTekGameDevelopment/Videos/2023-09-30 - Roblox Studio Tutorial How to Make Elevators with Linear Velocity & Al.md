---
title: "Roblox Studio Tutorial: How to Make Elevators with Linear Velocity & Align Orientation!"
url: https://youtu.be/6sgx1elbhwU
creator: SimTek Game Development
official: false
advice_density: medium
date: 2023-09-30
views: 1951
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Studio Tutorial: How to Make Elevators with Linear Velocity & Align Orientation!

[Watch](https://youtu.be/6sgx1elbhwU) | SimTekGameDevelopment | 1,951 views | 2023-09-30

## Summary
Tutorial on building a multi-floor elevator in Roblox Studio using LinearVelocity for movement and AlignOrientation to keep the platform level. Covers model setup, attachments, a move-elevator function that takes a destination floor, and calculating floors to travel.

## Tips
- [0:00](https://youtu.be/6sgx1elbhwU?t=0) **[[genre-mechanics]]** Use physics constraints (LinearVelocity) instead of tweening for moving platforms; forces are more realistic but can misbehave if parts are heavy or oriented oddly.
- [5:36](https://youtu.be/6sgx1elbhwU?t=336) **[[scripting-and-performance]]** Check each part's orientation indicator (Show Orientation Indicator) before using CFrame.UpVector; a rotated part will make the elevator move in the wrong direction.
- [9:10](https://youtu.be/6sgx1elbhwU?t=550) **[[physics-pathfinding-and-npc-ai]]** Add an AlignOrientation constraint between the moving floor and the base so heavy loads don't tip the platform.
- [11:27](https://youtu.be/6sgx1elbhwU?t=687) **[[building-and-level-design]]** Leave a small gap (about 0.2 studs) between the moving platform and static floors so the elevator never collides with anchored parts.
- [13:28](https://youtu.be/6sgx1elbhwU?t=808) **[[code-architecture-and-frameworks]]** Replace hardcoded numbers with variables (floor distance, current floor, destination floor) and wrap movement in a function that takes a target floor.
- [15:33](https://youtu.be/6sgx1elbhwU?t=933) **[[luau-language-and-types]]** Use math.abs on floor count for travel time and multiply distance by a direction of +1 or -1 so one function handles both up and down moves.
- [16:56](https://youtu.be/6sgx1elbhwU?t=1016) **[[physics-pathfinding-and-npc-ai]]** Track the current floor in a variable and compute floors to move as destination minus current, so any floor request works.

## Numbers
- [1:55](https://youtu.be/6sgx1elbhwU?t=115) Elevator speed: **10 studs per second; floor spacing 10 studs** (LinearVelocity set to 10 studs/s, each floor placed 10 studs apart)
- [4:53](https://youtu.be/6sgx1elbhwU?t=293) LinearVelocity MaxForce: **math.huge** (Used for the elevator floor's LinearVelocity constraint)

## Tools
Roblox Studio, LinearVelocity constraint, AlignOrientation constraint, Attachments

## Topics
[[building-and-level-design]] [[code-architecture-and-frameworks]] [[genre-mechanics]] [[luau-language-and-types]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
