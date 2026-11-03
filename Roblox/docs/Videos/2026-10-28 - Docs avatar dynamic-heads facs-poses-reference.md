---
title: "Docs: avatar / dynamic-heads / facs-poses-reference"
url: https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / dynamic-heads / facs-poses-reference

[Open](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox documentation listing the 50 FACS facial base poses used by avatar heads (dynamic heads). Explains how poses are stored in a head model from Blender/Maya, combined per frame, and which 17 poses are required for Marketplace publishing. Covers corrective handling for collisions (ChinRaiser/ChinRaiserUpperLip, LipsTogether with JawDrop).

## Tips
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) **[[ugc-and-avatar-economy]]** Avatar heads published to the Marketplace must include the 17 required FACS base poses; validation rejects assets missing any of them.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) **[[3d-modeling-rigging-and-animation]]** Store FACS poses inside the head model in Blender or Maya before importing to Studio; the pose order doesn't matter except for the neutral pose, which must be first.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) **[[3d-modeling-rigging-and-animation]]** Combine multiple FACS poses in one animation frame for complex expressions, but add a corrective where poses collide at full default values.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) **[[3d-modeling-rigging-and-animation]]** To raise the chin with the mouth closed, set ChinRaiser and ChinRaiserUpperLip to the same value so lips move together and do not collide.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) **[[3d-modeling-rigging-and-animation]]** To keep lips together while the jaw drops, set JawDrop and LipsTogether to 100% of default; ease LipsTogether to make the mouth open and close.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) **[[3d-modeling-rigging-and-animation]]** Use MouthLeft/MouthRight to move only the mouth, and JawLeft/JawRight to move the jaw, teeth, tongue and lower lip together.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) **[[3d-modeling-rigging-and-animation]]** TongueUp and TongueDown are only visible when combined with TongueOut; otherwise the tongue bends inside the mouth.

## Numbers
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) Required base poses for Marketplace avatar head: **17** (Marketplace validation rejects heads missing these; 50 base poses total)
- [page](https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference) Total FACS base poses listed: **50** (Documented list of facial base poses for dynamic heads)

## Tools
Blender, Maya, Roblox Studio

## Topics
[[3d-modeling-rigging-and-animation]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
