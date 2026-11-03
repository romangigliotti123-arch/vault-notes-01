---
title: "Docs: tutorials / curriculums / gameplay-scripting / detect-hits"
url: https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / gameplay-scripting / detect-hits

[Open](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial on hit detection for a laser tag game. Covers choosing physical vs instantaneous hit checks, computing blast directions for spread blasters, raycasting with RaycastResult, server-side validation of ray data (angle, distance, obstruction), and reducing Humanoid health via TakeDamage to respect force fields.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[core-loops-and-game-design]]** Choose physically simulated hit checks for projectiles affected by gravity or wind (e.g. dodgeball); use instantaneous raycasts for near-infinite-speed beams (e.g. laser tag).
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[scripting-and-performance]]** Put shared logic like getDirectionsForBlast in ReplicatedStorage so the server can recompute expected values and compare them against client data.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[anti-exploit-and-security]]** Validate client blast data on the server: check ray result types, compare claimed angles to expected spread angles within a tolerance, and raycast from the shooter to confirm the target is not behind a wall.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[anti-exploit-and-security]]** Raycast() ignores CanCollide by default; decide how decorative parts should behave and set RaycastParams.RespectCanCollide if needed.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[player-psychology-and-game-feel]]** Apply damage with Humanoid:TakeDamage() rather than setting Health directly, so active ForceFields block damage.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[combat-and-gameplay-systems]]** Clamp damage to remaining health (math.min(damage, humanoid.Health)) because Health cannot go negative; apply damage per ray, so multi-beam blasts can hit several times.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[combat-and-gameplay-systems]]** Store damagePerHit as a blaster attribute so damage tuning is data-driven; e.g. 10 damage per hit means 10 hits to tag out a 100-health player.
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) **[[common-mistakes]]** Do not rely on client-reported hits without server checks; a malicious client can remove walls or fake tags unless the server verifies the raycast path.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) Default Humanoid Health: **100** (Built-in Humanoid.Health default used as tag-out pool)
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) Single-laser damagePerHit: **10** (Ten hits needed to tag out a default 100-health player)
- [page](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits) Example damage clamp: **10 health vs 15 damage beam inflicts 10** (Damage capped at remaining health)

## Games
- **Sample laser tag game (Roblox official tutorial)**: Reference project: single-beam and multi-beam spread blasters, server-validated raycasts, health-based tag-out.

## Tools
Roblox Studio, Workspace:Raycast, RaycastParams, RemoteEvent, Humanoid:TakeDamage

## He points to
- Raycasting documentation
- Implementing Blasters tutorial chapter
- Spawning and respawning tutorial chapter
- Gameplay Scripting Curriculum Q&A

## Topics
[[anti-exploit-and-security]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[core-loops-and-game-design]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
