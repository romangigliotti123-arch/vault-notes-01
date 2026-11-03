---
title: "Designing an FPS Framework: Beginner’s guide [PART 2]"
url: https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-05-04
views: 616
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Designing an FPS Framework: Beginner’s guide [PART 2]

[Open](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) | Roblox DevForum | 616 views | 2021-05-04

## Summary
Part 2 of a beginner FPS framework tutorial for Roblox. Covers spring-based recoil and camera shake, muzzle flash and sounds via particle Emit, bobble and sway springs, raycast hit detection with a Damage remote, bullet replication through a Fire remote relayed to all clients, aiming with a tweened AimAlpha and a custom mouse raycast, and ammo-based reload.

## Tips
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[scripting-and-performance]]** Do not pass damage as a client parameter in production; validate hits server-side with a second raycast, since this tutorial simplifies for beginners.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[client-server-and-remotes]]** Replicate bullets via client Fire remote to server, then server FireAllClients to every other client, skipping the shooter to avoid double bullets.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[client-server-and-remotes]]** Pass the origin Vector3 and end position to remotes instead of the gun model to keep bullet replication lightweight.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[vfx-and-particles]]** Keep muzzle flash emitters disabled and call :Emit() on fire; enable LockedToPart so particles stick to the barrel.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[sound-and-music]]** Clone gun sounds and parent them to workspace on fire so the sound has a world origin, and set PlayOnRemove true so clones clean up.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[player-psychology-and-game-feel]]** Use a spring module to shove recoil on each shot, then decay it back down, with random sideways offset and screen shake for feel.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[ui-ux-design]]** Use a spring for bobble driven by player velocity and sway driven by mouse delta, applied to the viewmodel and HumanoidRootPart.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[combat-and-gameplay-systems]]** Raycast toward the bullet's predicted future position each frame; on hit, destroy the bullet and disconnect its loop. Skip this step if using FastCast.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[combat-and-gameplay-systems]]** Track ammo in a variable, reject shots at 0, decrement per shot, and refill only when the reload animation ends.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[ui-ux-design]]** Tween an AimAlpha NumberValue (not IntegerValue) to 1 or 0 and lerp the sight toward the viewmodel camera for smooth aiming.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) **[[ui-ux-design]]** Scopes block the default mouse raycast; use a custom GetMouse raycast from the camera with RaycastParams to aim through scoped guns.

## Numbers
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) Tutorial length: **1-2 days to complete** (Author's estimate for following the full FPS tutorial)
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) Raycast lookahead multiplier: **1.5** (Raycast to bullet future position times 1.5 for safety)
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) Likes on post: **616** (Post engagement reported on DevForum)

## Tools
SpringModule (rbxm), FastCast, Roblox Studio, RemoteEvents, RaycastParams, TweenService, ParticleEmitter

## He points to
- Part 1 of the FPS Framework tutorial by EXM_0
- Author's Discord server

## Quotes
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) "DISCLAIMER: please DO NOT pass the damage as a parameter for server side damage, im doing this to keep it simple for beginners."
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginner%E2%80%99s-guide-part-2/1203507) "We're raycasting to the bullet's future position. If it hits something we destroy the bullet, disconnect the loop and do something about it."

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[sound-and-music]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
