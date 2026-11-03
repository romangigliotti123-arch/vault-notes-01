---
title: "All about optimization"
url: https://devforum.roblox.com/t/all-about-optimization/2586333
creator: Roblox DevForum
official: false
advice_density: high
date: 2023-09-09
views: 179
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# All about optimization

[Open](https://devforum.roblox.com/t/all-about-optimization/2586333) | Roblox DevForum | 179 views | 2023-09-09

## Summary
Beginner DevForum tutorial on Roblox optimization: plan before optimizing, disable unnecessary shadows/collisions, avoid unanchored parts and heavy materials, use task library and RunService, split client/server work, avoid Humanoids for many NPCs, use bindable events over remotes, and use streaming.

## Tips
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[common-mistakes]]** Don't build features before planning; unused systems (e.g. a shop for weapons not yet designed) get deleted later and waste work.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[building-art-and-assets]]** Disable CanCollide, CanTouch and CanQuery on small, unreachable, or decorative parts (plants, windows, tools) to reduce physics cost.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[building-art-and-assets]]** Disable CastShadow on small or hard-to-see parts such as flowers and windows.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[building-art-and-assets]]** Use fewer semi-transparent, Glass, and Neon parts since they need more rendering calculations than opaque plastic.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[building-art-and-assets]]** Keep parts anchored unless physics is needed; unanchor only for the action, then re-anchor afterward.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[building-art-and-assets]]** Avoid unnecessary gradients, many open frames and glitter effects, which can reduce performance on low-end devices.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[ui-ux-design]]** Offer graphics presets (High/Medium/Low/Very low) that remove shadows, fog, clouds and effects for weaker devices.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[scripting-and-performance]]** Replace deprecated wait() with task.wait(); the author says it is more stable and about 2x faster.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[scripting-and-performance]]** Use RunService.Heartbeat instead of while wait() loops for per-frame code.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[scripting-and-performance]]** Connect functions to events once at startup rather than creating connections repeatedly at runtime.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[luau-language-and-types]]** Cache services and required modules in local variables at the top of scripts for better performance.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[scripting-and-performance]]** Set all properties on an Instance before parenting it to the game, so the engine does not process changes repeatedly.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[building-art-and-assets]]** Clone pre-built template parts instead of calling Instance.new for each object when possible.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[client-server-and-remotes]]** Run cosmetic effects, animations and audio on clients via remotes, while server handles hit detection and cooldowns to stay exploit-safe.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[scripting-and-performance]]** Use modules to store functions and tables so one require serves many calls instead of repeated lookups.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[physics-pathfinding-and-npc-ai]]** Use hitboxes that only run when players enter or leave an area, rather than constant per-frame player detection.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[physics-pathfinding-and-npc-ai]]** Delete the Humanoid from NPCs that do not move; for many NPCs, move them with constraints or CFrame instead of MoveTo and use BillboardGui health bars.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[client-server-and-remotes]]** Avoid spamming RemoteEvents; use BindableEvents for communication between scripts on the same side.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[optimization-and-streaming]]** If your game can handle it, enable instance streaming, since parts outside player range are unloaded.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[mindset-and-strategy]]** Think from the player's perspective and skip features players will not use.
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) **[[development-process-and-speed]]** Split work with teammates and review each other's code to catch mistakes.

## Numbers
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) task.wait vs wait: **about 2x faster (author's claim)**
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) server work offloaded: **about 50% of arrow-hit effects handled on client (author's example)**

## Games
- **Tower defense series by GnomeCode**: Referenced as an example of splitting client effects and server calculations.

## Tools
Roblox Studio, task library, RunService, BindableEvent, RemoteEvent, BillboardGui

## He points to
- GnomeCode tower defense series

## Quotes
- [page](https://devforum.roblox.com/t/all-about-optimization/2586333) "Think about what player/object can do, and how it can destroy code."

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[development-process-and-speed]] [[luau-language-and-types]] [[mindset-and-strategy]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
