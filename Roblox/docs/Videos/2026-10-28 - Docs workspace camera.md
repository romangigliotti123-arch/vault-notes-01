---
title: "Docs: workspace / camera"
url: https://create.roblox.com/docs/workspace/camera.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: workspace / camera

[Open](https://create.roblox.com/docs/workspace/camera.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs on customizing the camera. Covers StarterPlayer camera properties (zoom distance, CameraMode, occlusion modes, movement modes) for default third/first-person behavior, and scripting a Scriptable camera via Workspace.CurrentCamera (CFrame, FieldOfView, CameraType, Focus).

## Tips
- [page](https://create.roblox.com/docs/workspace/camera) **[[building-and-level-design]]** Set CameraMinZoomDistance and CameraMaxZoomDistance to the same value to lock the camera at a fixed distance and prevent zooming.
- [page](https://create.roblox.com/docs/workspace/camera) **[[ui-ux-design]]** Choose a DevCameraOcclusionMode: Zoom pulls the camera in when the character is hidden; Invisicam fades the occluding object instead, keeping the camera still.
- [page](https://create.roblox.com/docs/workspace/camera) **[[ui-ux-design]]** Pick movement modes per platform: DevComputerCameraMovementMode for PC and DevTouchCameraMovementMode for phone/tablet, since they are set independently.
- [page](https://create.roblox.com/docs/workspace/camera) **[[scripting-and-performance]]** For a Scriptable camera, update Camera.Focus every frame, because nearby visuals get more detail based on distance to the focus point.
- [page](https://create.roblox.com/docs/workspace/camera) **[[ui-ux-design]]** Use CameraType = Scriptable to fully override the default camera for over-the-shoulder, isometric, or scoped views instead of building a custom follow camera.

## Numbers
- [page](https://create.roblox.com/docs/workspace/camera) Camera.FieldOfView range: **1–120 degrees, default 70**
- [page](https://create.roblox.com/docs/workspace/camera) Zoom occlusion threshold: **Transparency below 0.25 triggers Zoom mode**
- [page](https://create.roblox.com/docs/workspace/camera) Invisicam occlusion threshold: **Transparency below 0.75 triggers Invisicam**
- [page](https://create.roblox.com/docs/workspace/camera) Example max zoom for far zoom-out: **500 studs (docs example)**

## Tools
Roblox Studio Explorer/Properties, StarterPlayer properties, Workspace.CurrentCamera

## He points to
- Class.StarterPlayer
- Class.Camera
- Enum.CameraType

## Topics
[[building-and-level-design]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
