---
title: "Docs: tutorials / use-case-tutorials / input-and-camera / control-the-users-camera"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / input-and-camera / control-the-users-camera

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on controlling the user's camera: switching to first-person via StarterPlayer.CameraMode, building a side-scrolling camera with a LocalScript bound to RunService render step, and adapting it into an isometric/top-down camera by changing the offset and FieldOfView.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) **[[client-server-and-remotes]]** Camera code must run in a LocalScript; only a user can see their own camera configuration, so it is always controlled from the client.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) **[[scripting-and-performance]]** Bind camera updates with RunService:BindToRenderStep at Enum.RenderPriority.Camera.Value + 1 so your function runs after Roblox's default camera update.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) **[[building-and-level-design]]** Use StarterPlayer.CameraMode = LockFirstPerson for a first-person view that stays locked to the character's head.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) **[[code-architecture-and-frameworks]]** Separate individual numbers into named constants (e.g. CAMERA_DEPTH, HEIGHT_OFFSET) so they are easy to tweak later.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) **[[genre-mechanics]]** HumanoidRootPart sits about 2 studs below the head, so add a height offset when aiming the camera at the character.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) **[[building-and-level-design]]** For an isometric look, offset the camera equally on X, Y and Z from the root and lower FieldOfView (e.g. 20) while increasing distance to compensate.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) HumanoidRootPart height offset: **2 studs below head** (Offset needed to aim camera at the head)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) Example FieldOfView for isometric: **20** (Zooms in for a flatter isometric look; increase distance to compensate)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) Example camera depth (side-scroller): **24 studs** (CAMERA_DEPTH on Z axis in the tutorial sample)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) Example camera depth (isometric): **64 studs** (CAMERA_DEPTH used in the FieldOfView=20 isometric sample)

## Tools
Roblox Studio, RunService:BindToRenderStep, CFrame.lookAt, StarterPlayer.CameraMode

## He points to
- Roblox Creator Docs: Control the user's camera

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[genre-mechanics]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
