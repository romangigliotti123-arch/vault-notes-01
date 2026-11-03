---
title: "These Weird Optimizations Made Our Game Run 10x FASTER!"
url: https://youtu.be/vBZMscweRDk
creator: Roox4
official: false
advice_density: medium
date: 2025-06-19
views: 541711
transcript: auto-captions
confidence: medium
tags: [roblox, roox4official, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# These Weird Optimizations Made Our Game Run 10x FASTER!

[Watch](https://youtu.be/vBZMscweRDk) | Roox4Official | 541,711 views | 2025-06-19

## Summary
A physics-based FPS dev explains how his team cut projectile lag: bullets become purely visual client effects while the server simulates them from start position, direction and velocity. Grenades use a ballistic equation for position over time. Turret rotation moved to server-side IK "Look At" constraints, removing the performance hit.

## Tips
- [0:42](https://youtu.be/vBZMscweRDk?t=42) **[[scripting-and-performance]]** Don't replicate every projectile as a physical part over the network; network bandwidth becomes the bottleneck. Simulate them with math instead.
- [2:46](https://youtu.be/vBZMscweRDk?t=166) **[[scripting-and-performance]]** Make bullets purely visual on clients and have the server simulate them from start position, direction and velocity; this reduces each object to a few numbers.
- [3:29](https://youtu.be/vBZMscweRDk?t=209) **[[scripting-and-performance]]** For non-linear projectiles like grenades, use a closed-form ballistic equation to compute position at any time instead of simulating physics objects.
- [5:34](https://youtu.be/vBZMscweRDk?t=334) **[[scripting-and-performance]]** Avoid rotating turrets with CFrame updates, animation rigs or mechanical constraints; they were too expensive at scale.
- [6:14](https://youtu.be/vBZMscweRDk?t=374) **[[client-server-and-remotes]]** Running turret logic on clients saves performance but makes server aim estimates inaccurate and desynced; avoid this trade-off if possible.
- [6:56](https://youtu.be/vBZMscweRDk?t=416) **[[physics-pathfinding-and-npc-ai]]** Use IK control in Look At mode to rotate a part toward a target on the server; the speaker reports it runs with no performance issues.

## Numbers
- [0:00](https://youtu.be/vBZMscweRDk?t=0) projectiles fired per second: **~1,400 at 60 FPS** (Physics-based FPS demo with networked, simulated bullets)
- [1:24](https://youtu.be/vBZMscweRDk?t=84) FPS before fix: **~15** (Original approach replicated each bullet as physical object)
- [4:11](https://youtu.be/vBZMscweRDk?t=251) Striderbot grenades thrown: **4 per second** (Enemy throws four grenades every second; 2-3 Striderbots at once)
- [5:34](https://youtu.be/vBZMscweRDk?t=334) Turret share of network bandwidth: **about half of available** (Turret rotation replication before IK fix)

## Tools
IK Control (Look At mode)

## Quotes
- [2:46](https://youtu.be/vBZMscweRDk?t=166) "Fake it if you can't make it. Only these bullets are purely visual. The server simulates them."
- [6:56](https://youtu.be/vBZMscweRDk?t=416) "One of the modes on IK control is called Look At, which rotates a part to face a target, and causes no performance issues."

## Topics
[[client-server-and-remotes]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roox4Official - How to make successful Roblox games]]
