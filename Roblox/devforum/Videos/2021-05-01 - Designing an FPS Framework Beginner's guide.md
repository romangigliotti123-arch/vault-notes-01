---
title: "Designing an FPS Framework: Beginner's guide"
url: https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-05-01
views: 774
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Designing an FPS Framework: Beginner's guide

[Open](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) | Roblox DevForum | 774 views | 2021-05-01

## Summary
Beginner tutorial on building a basic Roblox FPS framework without OOP, using module scripts. Covers viewmodel setup with Motor6Ds and CameraBone, positioning the viewmodel to the camera each frame, welding and equipping a gun, playing hold animations via Moon Animator, a simple projectile module, and mouse-held firing. Part 2 (recoil, sway, hit detection, replication) is linked but not covered.

## Tips
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) **[[building-art-and-assets]]** Keep the gun to as few parts as possible; name the functional parts (barrel, handle, sight) in a GunComponents folder for scripts to reference.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) **[[3d-modeling-rigging-and-animation]]** Build viewmodel bones with Motor6Ds: HumanoidRootPart to arms, CameraBone to HRP, and a 'Handle' Motor6D for welding the gun. Delete the viewmodel's Humanoid and use AnimationController instead.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) **[[ui-ux-design]]** Position the viewmodel to the camera CFrame every frame inside RenderStepped so the arms track the view without lag.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) **[[3d-modeling-rigging-and-animation]]** Zero the viewmodel HumanoidRootPart position and rotation before animating in Moon Animator, and set hold animations to loop.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) **[[common-mistakes]]** When animating with Moon Animator, guard the weld function with 'if v ~= Main then' or the plugin crashes.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) **[[vfx-and-particles]]** Multiply bullet velocity by dt when moving projectiles per frame so speed stays consistent across frame-rate changes.
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) **[[scripting-and-performance]]** Destroy projectiles once they exceed a max travel distance to avoid leaking instances.

## Numbers
- [page](https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208) Community request threshold: **20 hearts** (Author required 20 likes before committing to part 2)

## Tools
Moon Animator, Roblox Animator, Blender, AnimationController, RenderStepped, Motor6D, WeldConstraint

## He points to
- Designing an FPS Framework: Beginner's guide [PART 2] (Community Tutorials, by EXM_0)
- EXM_0 Discord server

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[common-mistakes]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
