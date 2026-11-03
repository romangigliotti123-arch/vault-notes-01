---
title: "Camera Animations for cutscenes and gameplay!"
url: https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-04-22
views: 480
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Camera Animations for cutscenes and gameplay!

[Open](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) | Roblox DevForum | 480 views | 2021-04-22

## Summary
Tutorial on camera animations in Roblox using Moon Animator. Covers building static-position cutscenes by keyframing a camera CFrame track, exporting per-frame CFrames, and playing them client-side with RenderStepped. Extends to gameplay cutscenes by multiplying the playback CFrame by a reference part (e.g. HumanoidRootPart) so the camera follows the character.

## Tips
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) **[[building-art-and-assets]]** Use Moon Animator to keyframe a camera's CFrame track; add a character with animation to sync camera shots to character animation.
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) **[[client-server-and-remotes]]** Run camera cutscene playback on the client (LocalScript), since the camera is client-owned; place exported frame folder where the client can access it.
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) **[[optimization-and-streaming]]** Moon Animator exports one CFrame per frame at its FPS (60 by default); consider lower FPS to reduce the number of stored frame values.
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) **[[combat-and-gameplay-systems]]** For attack cutscenes, animate the camera as normal, then in code set Camera.CFrame = reference part CFrame * frame CFrame, using HumanoidRootPart as the reference 99% of the time.
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) **[[player-psychology-and-game-feel]]** Camera animation can make attacks feel more powerful; use short camera moves on attacks and cinematic shots for cutscenes.
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) **[[core-loops-and-game-design]]** During cutscenes set Humanoid.AutoRotate to false and Camera.CameraType to Scriptable, then restore Custom and the saved CFrame when finished.

## Numbers
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) Default animation FPS in Moon Animator: **60** (Exported folder holds one CFrame per frame at this FPS)
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) Frame-time conversion in script: **FrameTime += DT * 60** (Converts RenderStepped delta seconds to frame index at 60 FPS)

## Tools
Moon Animator, RunService.RenderStepped, Camera.CameraType Scriptable

## He points to
- Moon Animator (Creator Hub Marketplace)

## Quotes
- [page](https://devforum.roblox.com/t/camera-animations-for-cutscenes-and-gameplay/1181691) "To be honest, there are barely any games that use camera animations. Even though a good camera can make an attack feel much more powerful."

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[optimization-and-streaming]] [[player-psychology-and-game-feel]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
