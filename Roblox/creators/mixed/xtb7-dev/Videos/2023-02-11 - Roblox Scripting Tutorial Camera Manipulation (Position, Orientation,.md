---
title: "Roblox Scripting Tutorial: Camera Manipulation (Position, Orientation, Rotation) - *2025*"
url: https://youtu.be/0TpwPpULXxU
creator: XTB7
official: false
advice_density: medium
date: 2023-02-11
views: 27986
transcript: manual-subs
confidence: high
tags: [roblox, xtb7-dev, youtube-learn]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Roblox Scripting Tutorial: Camera Manipulation (Position, Orientation, Rotation) - *2025*

[Watch](https://youtu.be/0TpwPpULXxU) | xtb7-dev | 27,986 views | 2023-02-11

## Summary
Roblox scripting tutorial on camera manipulation with a LocalScript: binding to RunService.RenderStepped-style BindToRenderStep at priority after Camera, setting camera type to Scriptable, positioning via CFrame offsets relative to HumanoidRootPart, orienting with math.rad and CFrame.Angles (X/Y/Z mapping quirks), and adjusting FieldOfView (70 default).

## Tips
- [1:23](https://youtu.be/0TpwPpULXxU?t=83) **[[scripting-and-performance]]** Use RunService:BindToRenderStep with Enum.RenderPriority.Camera.Value + 1 (or 201) so your camera changes aren't overridden by Roblox.
- [2:50](https://youtu.be/0TpwPpULXxU?t=170) **[[scripting-and-performance]]** Set camera.CameraType to Scriptable, otherwise custom camera changes won't take effect.
- [3:31](https://youtu.be/0TpwPpULXxU?t=211) **[[scripting-and-performance]]** Combine CFrames with multiplication (*), not addition; adding offsets every frame with + causes runaway drift.
- [4:32](https://youtu.be/0TpwPpULXxU?t=272) **[[scripting-and-performance]]** Put the camera LocalScript in StarterCharacterScripts so it doesn't error when the character dies and no character exists.
- [5:56](https://youtu.be/0TpwPpULXxU?t=356) **[[building-and-level-design]]** Offset the camera along Z (e.g. 0,2,8 backwards and sideways) so it doesn't sit inside the character; tune values per game.
- [8:01](https://youtu.be/0TpwPpULXxU?t=481) **[[scripting-and-performance]]** CFrame.Angles axes are not intuitive: X tilts up/down, Y turns left/right, Z tilts/rolls; use math.rad to convert degrees.
- [9:27](https://youtu.be/0TpwPpULXxU?t=567) **[[ui-ux-design]]** Keep pitch angles small (clamp around ±45 or less); large pitch values look odd.
- [10:41](https://youtu.be/0TpwPpULXxU?t=641) **[[ui-ux-design]]** Zoom via camera.FieldOfView: default 70; lower values zoom in (60), higher zoom out (80).

## Numbers
- [10:41](https://youtu.be/0TpwPpULXxU?t=641) Default camera FieldOfView: **70** (Roblox default; decrease to zoom in, increase to zoom out)
- [9:27](https://youtu.be/0TpwPpULXxU?t=567) Radians per degree conversion: **~57 degrees per radian** (Use math.rad to convert degrees automatically)

## Tools
RunService, Enum.RenderPriority, CFrame, math.rad, Roblox Creator Documentation

## He points to
- Roblox Creator Documentation

## Topics
[[building-and-level-design]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[xtb7-dev - How to make successful Roblox games]]
