---
title: "Docs: animation / curve-editor"
url: https://create.roblox.com/docs/animation/curve-editor.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / curve-editor

[Open](https://create.roblox.com/docs/animation/curve-editor.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Animation Editor's Curve Editor: converting KeyframeSequence to CurveAnimation, Euler vs quaternion rotation types, interpolation modes (linear/constant/cubic), tangents, generating bounce/elastic interpolation curves, and Euler angle order behavior.

## Tips
- [page](https://create.roblox.com/docs/animation/curve-editor) **[[building-art-and-assets]]** Set Default Rotation Type to Quaternions before opening the Curve Editor; quaternion-to-Euler conversion is irreversible and can alter animation near gimbal lock.
- [page](https://create.roblox.com/docs/animation/curve-editor) **[[building-art-and-assets]]** Converting a KeyframeSequence to a CurveAnimation is one-way for the rotation track; verify rotation type first.
- [page](https://create.roblox.com/docs/animation/curve-editor) **[[building-art-and-assets]]** Use Cubic interpolation mode when you need eased in/out motion; it is the only mode that allows tangent editing.
- [page](https://create.roblox.com/docs/animation/curve-editor) **[[building-art-and-assets]]** Use Generate Curve > Bounce or Elastic on selected keyframes to mimic easing styles unavailable for curve animations.
- [page](https://create.roblox.com/docs/animation/curve-editor) **[[building-art-and-assets]]** Right-click an unset or set tangent and choose Set Tangent to Zero to reset it to default interpolation.
- [page](https://create.roblox.com/docs/animation/curve-editor) **[[building-art-and-assets]]** Changing Euler order on an existing Euler track can change the animation because keyframe values are preserved; set order before authoring keys.

## Numbers
- [page](https://create.roblox.com/docs/animation/curve-editor) Euler angle orders available: **6 (XYZ, XZY, YXZ, YZX, ZXY, ZYX)**
- [page](https://create.roblox.com/docs/animation/curve-editor) Interpolation modes for curve animations: **3 (Linear default, Constant, Cubic)**
- [page](https://create.roblox.com/docs/animation/curve-editor) Quaternion segment range: **Each segment interpolates from 0 to 1**

## Tools
Roblox Studio Animation Editor, Curve Editor

## He points to
- Roblox Creator Docs: Curve Editor

## Topics
[[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
