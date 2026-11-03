---
title: "Writing an FPS framework, part 2 (2020)"
url: https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-05-18
views: 441
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Writing an FPS framework, part 2 (2020)

[Open](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) | Roblox DevForum | 441 views | 2020-05-18

## Summary
Part 2 of a DevForum tutorial on building a Roblox FPS framework: smooth-value module, FastCast projectile setup, Motor6D holster/equip welds, server-side equip/aim/fire remotes, client replication of gunfire and damage. Mostly code walkthrough with a few setup tips.

## Tips
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[client-server-and-remotes]]** Validate equip requests on the server and have the client refuse to equip if the server returns false; spawn the server request so the client doesn't block.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[anti-exploit-and-security]]** Don't trust client-sent hit results; the author's damage-by-client remote is a shortcut, and real games should verify hits server-side.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[client-server-and-remotes]]** Replicate weapon fire by sending origin and direction to the server, which relays to other clients; re-simulate the bullet locally on each client.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[scripting-and-performance]]** Keep projectiles client-side for responsiveness and replicate them, rather than server-only bullets which freeze and cost more to create.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[building-art-and-assets]]** Scale weapon models to real player height; oversized guns broke the author's animations and needed rework.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[ai-and-tools]]** Use FastCast Redux for raycast-based bullets with bullet drop; gravity values of -100 to -500 work well.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[3d-modeling-rigging-and-animation]]** Export looping animations for poses; use lower priority for idle; use Out easing for quick shooting animations.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) **[[ui-ux-design]]** Don't store animations inside the script output path only; put animation references in a settings module so missing animations don't throw errors.

## Numbers
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) RPM: **700 rpm, magCapacity 30, velocity 1500, range 5000** (example firing settings in the tutorial)
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) Magazine count: **5 spare magazines per weapon** (magazineCount used to compute spare ammo)
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) Damage values: **damage 50, headshot 100** (example firing settings; headshot used as multiplier in code)
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) Holster/equip tween: **0.6 seconds** (TweenInfo duration for lowering the gun on unequip)
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) Gravity for bullet drop: **-100 to -500** (FastCast gravity range the author found works well)

## Games
- **Untitled FPS**: Author's own FPS demo; the framework is extracted from it, with some parts removed before open-sourcing.

## Tools
FastCast Redux, Moon Animator (moon animation suite), Blender, Roblox Studio

## He points to
- FastCast Redux by EtiTheSpirit (Roblox library 4453855787)

## Topics
[[3d-modeling-rigging-and-animation]] [[ai-and-tools]] [[anti-exploit-and-security]] [[building-art-and-assets]] [[client-server-and-remotes]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
