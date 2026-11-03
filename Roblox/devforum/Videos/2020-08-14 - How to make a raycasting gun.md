---
title: "How to make a raycasting gun"
url: https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-08-14
views: 542
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to make a raycasting gun

[Open](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) | Roblox DevForum | 542 views | 2020-08-14

## Summary
Tutorial for a server-authoritative raycasting gun in Luau: the client fires a RemoteEvent with the mouse hit position, the server raycasts from a Shoot part, draws a beam sized to the hit distance, and applies Humanoid damage. Updates a 2020 tutorial for the newer Raycast API and filtering enabled.

## Tips
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) **[[client-server-and-remotes]]** Fire a RemoteEvent from a LocalScript on tool.Activated with the mouse position; do all raycasting and damage on the server.
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) **[[scripting-and-performance]]** Use the new Workspace:Raycast API instead of outdated tutorial methods; old guides broke after filtering enabled was enforced.
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) **[[combat-and-gameplay-systems]]** When a raycast returns nil, use origin + direction as the hit position so misses still show a bullet.
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) **[[combat-and-gameplay-systems]]** Check the hit part's parent and grandparent for a Humanoid so hits on nested models still register damage.
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) **[[building-art-and-assets]]** Pre-build the bullet beam as an anchored, non-collidable neon part in ServerStorage and clone and resize it per shot.
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) **[[core-loops-and-game-design]]** Destroy visual bullet parts after about 0.25 seconds so they do not clutter Workspace.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) Raycast range: **300 studs** (Ray length used in tutorial; adjustable)
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) Damage per hit: **10** (Humanoid:TakeDamage(10) in example)
- [page](https://devforum.roblox.com/t/how-to-make-a-raycasting-gun/723716) Bullet visual lifetime: **0.25 seconds** (wait(0.25) before bullet_clone:Destroy())

## Tools
Roblox Studio, Luau, RemoteEvent, Workspace:Raycast

## He points to
- Roblox Developer Hub raycasting docs
- PlayerMouse2 custom mouse module by sjr04 (mentioned)

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
