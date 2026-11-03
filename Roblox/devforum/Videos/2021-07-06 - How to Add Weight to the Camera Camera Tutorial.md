---
title: "How to Add 'Weight' to the Camera [Camera Tutorial]"
url: https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-07-06
views: 196
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Add "Weight" to the Camera [Camera Tutorial]

[Open](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) | Roblox DevForum | 196 views | 2021-07-06

## Summary
Tutorial on adding camera "weight" in Roblox so the camera drags behind the character. A anchored invisible Subject part is lerped toward the head each render step and set as CameraSubject. Covers separate XZ/Y weights, shift-lock compatibility, and disabling weight in first person.

## Tips
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) **[[building-and-level-design]]** Anchor the invisible Subject part and make it non-colliding/transparent so it doesn't interfere with the workspace; it must stay where you set it.
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) **[[ui-ux-design]]** Use different weights for horizontal and vertical camera motion (e.g. WEIGHT_XZ=20, WEIGHT_Y=5) since screens are wider than tall.
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) **[[ui-ux-design]]** Disable camera weight in first person by switching CameraSubject back to the Humanoid when the camera is within 1 stud of the head; weight otherwise blocks the screen.
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) **[[client-server-and-remotes]]** Run camera weight logic in a LocalScript and bind to RunService render step at Enum.RenderPriority.Camera.Value so it updates before the camera renders.
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) **[[common-mistakes]]** Setting CameraSubject to a non-humanoid part breaks shift lock rotation; manually rotate the root part toward the camera's XZ LookVector when MouseBehavior is LockCenter.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) WEIGHT value (lerp divisor): **20 (1 = no weight)** (Example camera weight; each tick moves subject 1/WEIGHT of remaining distance)
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) Vertical WEIGHT_Y example: **5** (Lower vertical weight than horizontal WEIGHT_XZ=20 for wider screens)
- [page](https://devforum.roblox.com/t/how-to-add-weight-to-the-camera-camera-tutorial/1331996) First-person threshold: **1 stud** (Camera-to-head distance below which first-person mode is assumed)

## Tools
Roblox Studio, Luau LocalScript, RunService:BindToRenderStep

## He points to
- xXSanrioSlayer99 DevForum tutorial post

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[common-mistakes]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
