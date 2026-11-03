---
title: "Writing an FPS framework (2020)"
url: https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-03-31
views: 1289
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Writing an FPS framework (2020)

[Open](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) | Roblox DevForum | 1,289 views | 2020-03-31

## Summary
Beginner tutorial (2020) building a first-person shooter gun framework in Roblox: folder setup, gun model structure, viewmodel with Motor6Ds, a metatable-based weapon handler, offsets and CFrame lerping, spring-based sway/walk bob, RMB aim tweening, muzzle flash, auto-fire loop with RPM, and recoil. Notes that projectiles and server security are out of scope.

## Tips
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[scripting-and-performance]]** Multiply procedural movement by deltaTime (e.g. *deltaTime*60) so FPS-unlocked clients (100-300 FPS) don't run animations faster.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[building-art-and-assets]]** Keep the viewmodel separate from the gun model; merge them only when equipped. Don't put the viewmodel in workspace.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[client-server-and-remotes]]** Replicate gun sound/effects to other clients via remotes instead of disabling filtering enabled (SoundService.RespectFilteringEnabled = false).
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[data-persistence]]** Keep ammo variables and damage, equipped states and similar economy-relevant logic server-side.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[anti-exploit-and-security]]** Have the server manage damage, ammo and equipped state rather than trusting the client.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[building-art-and-assets]]** Rig animation parts to weaponRootPart rather than the receiver; Blender did not recognise parts rigged to the receiver, so reload mag movement failed.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[ui-ux-design]]** Add a center-screen dot during testing; aim offset can look correct yet be visually misaligned.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[scripting-and-performance]]** Use TweenService for aim in/out transitions and lerp between idle and aim CFrame offsets via a NumberValue.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[development-process-and-speed]]** Tune offsets live via the command bar, then copy the resulting values into the Offsets folder rather than hand-editing numbers repeatedly.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[building-art-and-assets]]** Use a Rojo + VS Code workflow instead of the default Studio script editor; the author found it much more productive.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[combat-and-gameplay-systems]]** Use a fire loop with wait(60/rpm) and a canFire cooldown; shove recoil springs on fire and reverse after ~0.15s.
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) **[[combat-and-gameplay-systems]]** Use FastCast for projectiles; the author noted it as the projectile library of choice.

## Numbers
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) FPS unlocker example: **100-300 FPS** (Frame rates where unscaled animation breaks; deltaTime scaling needed)
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) Example fire rate: **800 RPM** (Example rpm setting in firing table; fire delay = 60/rpm seconds)
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) Recoil reset delay: **0.15 s** (Wait before reversing the recoil spring shove)
- [page](https://devforum.roblox.com/t/writing-an-fps-framework-2020/503318) Aim tween times: **1 s in, 0.5 s out** (TweenInfo durations with Quart Out easing for aim lerp value)

## Tools
Rojo, FastCast, Velocity framework (ReturnedTrue), Spring module (x_o), Old Moon Animation Studio plugin, Blender rig exporter/animation importer, ACS gun model

## He points to
- Writing an FPS framework, part 2 (2020) DevForum tutorial
- rojo.space

## Topics
[[anti-exploit-and-security]] [[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[data-persistence]] [[development-process-and-speed]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
