---
title: "Zombie AI and Finite State Machines with Transition Hooks"
url: https://youtu.be/9rzgsXFPTjY
creator: SimTek Game Development
official: false
advice_density: medium
date: 2025-07-28
views: 18428
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Zombie AI and Finite State Machines with Transition Hooks

[Watch](https://youtu.be/9rzgsXFPTjY) | SimTekGameDevelopment | 18,428 views | 2025-07-28

## Summary
Builds a zombie NPC in Roblox Luau using a finite state machine (FSM): wander, investigate, chase states. Covers R15 rig setup, CollectionService tagging, Animation Editor keyframe animations published to Roblox, a StateManager base class with on-enter/on-exit transition hooks, ray-cast line-of-sight, and a config module for speeds, animation IDs and sight range.

## Tips
- [1:20](https://youtu.be/9rzgsXFPTjY?t=80) **[[scripting-and-performance]]** Put literals like walk speeds, animation IDs, detection radius and sight distance in a config ModuleScript instead of hardcoding them across scripts.
- [15:07](https://youtu.be/9rzgsXFPTjY?t=907) **[[code-architecture-and-frameworks]]** Structure AI as a reusable FSM: a state manager core, one ModuleScript per state, and an NPC class that inherits via setmetatable so states can be shared across NPCs.
- [27:28](https://youtu.be/9rzgsXFPTjY?t=1648) **[[code-architecture-and-frameworks]]** Guard optional transition hooks with a nil check before calling them so states without on-enter/on-exit functions do not error.
- [36:27](https://youtu.be/9rzgsXFPTjY?t=2187) **[[scripting-and-performance]]** Use a RaycastParams exclusion list containing the NPC's own model so line-of-sight rays don't hit the zombie itself.
- [40:35](https://youtu.be/9rzgsXFPTjY?t=2435) **[[scripting-and-performance]]** Use a random wander delay (min to max seconds) and a task.wait loop of about 0.5s for AI decisions to keep state changes varied and cheap.
- [53:36](https://youtu.be/9rzgsXFPTjY?t=3216) **[[scripting-and-performance]]** Check that HumanoidRootPart and target character exist before using them; WaitForChild on the Animator avoids nil errors when spawning NPCs.
- [1:17:39](https://youtu.be/9rzgsXFPTjY?t=4659) **[[building-art-and-assets]]** Keep animation priority set to Movement and tighten keyframe spacing to speed up an animation rather than changing speed in code.
- [4:09](https://youtu.be/9rzgsXFPTjY?t=249) **[[building-art-and-assets]]** Make the first and last keyframes identical so looping animations transition smoothly.
- [2:03](https://youtu.be/9rzgsXFPTjY?t=123) **[[building-art-and-assets]]** Remove default body colors from rigs and add new ones so the NPC is not moderated for having no clothing.

## Numbers
- [1:20](https://youtu.be/9rzgsXFPTjY?t=80) Walk speed wander / investigate / chase: **3 / 6 / fastest studs per second (chase value not stated)** (Config walk speeds for zombie states)
- [1:10:46](https://youtu.be/9rzgsXFPTjY?t=4246) Investigate sight-based distance: **30 studs** (Distance before investigate reverts to wander)
- [1:18:20](https://youtu.be/9rzgsXFPTjY?t=4700) Max sight ray cast distance: **45 studs** (Config vision max sight used by can-see raycast)
- [43:59](https://youtu.be/9rzgsXFPTjY?t=2639) Ray cast distance in code: **50 studs** (Initial ray cast length before config change)
- [32:17](https://youtu.be/9rzgsXFPTjY?t=1937) Decision loop wait: **0.5 seconds** (task.wait interval for NPC decide-action loop)
- [32:17](https://youtu.be/9rzgsXFPTjY?t=1937) Respawn delay after death: **5 seconds** (task.delay before cloning zombie again)
- [49:27](https://youtu.be/9rzgsXFPTjY?t=2967) Wander delay range: **2 to 6 seconds** (Random min and max delay between wander moves)
- [4:09](https://youtu.be/9rzgsXFPTjY?t=249) Animation keyframe timing: **30 frames per second, 15-frame walk cycle** (Animation Editor default frame rate for wander animation)

## Tools
Roblox Studio, Animation Editor, Tag Editor, CollectionService, RaycastParams, Luau ModuleScript, PathfindingService (mentioned, not used)

## He points to
- Earlier finite state machine and NPC videos by the same creator

## Topics
[[building-art-and-assets]] [[code-architecture-and-frameworks]] [[scripting-and-performance]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
