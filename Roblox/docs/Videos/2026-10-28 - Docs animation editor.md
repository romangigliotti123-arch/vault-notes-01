---
title: "Docs: animation / editor"
url: https://create.roblox.com/docs/animation/editor.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / editor

[Open](https://create.roblox.com/docs/animation/editor.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the Animation Editor (Avatar tab). Covers creating rigs and poses, keyframe operations, easing style and direction, automatic and on-demand keyframe optimization, looping, animation priority levels, saving to ServerStorage, and publishing/exporting animations, including the required "End" keyframe rename for default animation replacement.

## Tips
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** For custom rigs with Motor6D joints, set AssemblyRootPart to the part that should stay stationary; PrimaryPart does not set the assembly root.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** Keyframes insert at the position closest to where you right-clicked, not at the scrubber position. Check placement before adding.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** Use Constant easing to snap between keyframes; use CubicV2 for natural motion, since Linear looks stiff and robotic on turns.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** Looping animations do not interpolate from last to first keyframe. Duplicate the first keyframe as the final keyframe for a seamless loop.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** Set animation priority so overlapping animations resolve correctly, e.g. Jump above Idle so a character does not play both.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** To replace default jump or run animations, rename the final keyframe to exactly 'End' (case-sensitive) before publishing.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** Export (Publish to Roblox) animations before referencing them in your game; saved local animations stay in ServerStorage and do not replicate to clients.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** If clients need local animation data, move the KeyframeSequence or CurveAnimation objects to ReplicatedStorage.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** Use Optimize Keyframes and the automatic removal of repeated keyframes to reduce keyframe count and keep the timeline manageable.
- [page](https://create.roblox.com/docs/animation/editor) **[[3d-modeling-rigging-and-animation]]** Set the group in the Creator field when publishing animations used in a group-owned game.

## Numbers
- [page](https://create.roblox.com/docs/animation/editor) Default animation frame rate: **30 fps (0:15 = 0.5 s)**
- [page](https://create.roblox.com/docs/animation/editor) Default timeline duration: **1 second (1:00)**
- [page](https://create.roblox.com/docs/animation/editor) Automatic keyframe removal threshold: **3 or more consecutive identical-value keyframes reduced to first and last**
- [page](https://create.roblox.com/docs/animation/editor) Animation priority levels: **7 (Action4 highest to Core lowest)**

## Tools
Animation Editor, Rig Generator, Explorer, Toolbox

## He points to
- Use animations (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
