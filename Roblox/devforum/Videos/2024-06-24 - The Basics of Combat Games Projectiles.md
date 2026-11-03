---
title: "The Basics of Combat Games: Projectiles"
url: https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332
creator: Roblox DevForum
official: false
advice_density: high
date: 2024-06-24
views: 50
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# The Basics of Combat Games: Projectiles

[Open](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) | Roblox DevForum | 50 views | 2024-06-24

## Summary
Tutorial on projectile systems for Roblox combat games: moving projectiles with RenderStepped/Heartbeat using a single shared loop, choosing client-sided vs server-sided vs client-origin creation, replicating cosmetic projectiles to other clients, and server-sided ghost projectiles for hit validation.

## Tips
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[genre-mechanics]]** Use Raycast for about 99% of projectiles; use GetPartsInBox only for large, mostly linear projectiles; avoid .Touched unless physics-heavy bouncing is needed.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[scripting-and-performance]]** Move non-physics projectiles in a client-side RenderStepped loop for smoothness; use one shared connection for all active projectiles instead of one per projectile.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[optimization-and-streaming]]** If projectile counts are very large, use RunService.Heartbeat instead of RenderStepped, since RenderStepped runs before render and expensive work there drops FPS.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[scripting-and-performance]]** Run hit detection on an interval (e.g. every 0.1s) rather than every frame to save cost.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[client-server-and-remotes]]** Create predictable projectiles on the client (client-sided) to save resources; use the server for complex projectiles that follow cursors or rely on physics, then hand network ownership to the client.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[client-server-and-remotes]]** Client-origin creation (no server wait) suits FPS-style rapid fire, but sanity-check ammo and similar state on the server when the client calls a hit.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[client-server-and-remotes]]** Replicate client-made projectiles to other clients by sending the attacker's projectile direction back to the server, then relaying it to all clients for cosmetic copies.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[client-server-and-remotes]]** Let clients simulate stopping for rapid or unimportant projectiles; send a remote event only for important projectiles (e.g. explosions) so stop time and location stay accurate.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[anti-exploit-and-security]]** Validate client hits with server-sided ghost projectiles and a magnitude check against the target; deny requests at outrageous distances to counter exploiters.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[client-server-and-remotes]]** Do not offset the server ghost projectile by one latency unit; it would end up ahead of the client's position. Keep it as-is, since it matches the client's position at hit time.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[optimization-and-streaming]]** Skip replicating half of rapid-fire bullets (e.g. minigun) and skip replicating projectiles far from a client that are not aimed toward them.
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) **[[optimization-and-streaming]]** If a projectile will hit near-instantly, use a raycast or spatial query instead of spawning a projectile; for ghost projectiles, estimate position from elapsed time to avoid creating them.

## Numbers
- [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) Projectile detection interval: **0.1 seconds** (Example DetectionInterval for projectile hit checks, not every frame)

## Tools
RunService.RenderStepped, RunService.Heartbeat, Raycast, GetPartsInBox, os.clock

## He points to
- TheCraftNCreator, The Basics of Combat Games: Hitboxes

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[genre-mechanics]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
