---
title: "Docs: avatar / character-bodies / test-blender"
url: https://create.roblox.com/docs/avatar/character-bodies/test-blender.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / character-bodies / test-blender

[Open](https://create.roblox.com/docs/avatar/character-bodies/test-blender.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on testing character bodies in Blender before importing into Studio. Covers checking technical specs (body scale, triangle budgets, naming, rigging/skinning, attachments, outer cage), validating facial animation data (timeline frames, RootFaceJoint, custom properties, FACS names), and verifying skinning via Pose mode and the Calisthenics Tool.

## Tips
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[building-art-and-assets]]** Periodically test character bodies in Blender to catch issues before importing into Studio; use templates and non-destructive modeling to avoid breaking components.
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[3d-modeling-rigging-and-animation]]** Keep the neutral facial pose on frame 0 of the Armature timeline and remove keyframe gaps between facial animation frames.
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[3d-modeling-rigging-and-animation]]** Verify Head_Geo's RootFaceJoint attribute names the first facial animation bone, which must be a child of the Head bone (commonly DynamicHead).
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[3d-modeling-rigging-and-animation]]** Ensure one custom property per unique facial animation frame, with pose names matching the FACS pose reference spelling and capitalization.
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[3d-modeling-rigging-and-animation]]** Enable Show In Front and hide face bones in Pose mode when testing body skinning, so body bones are easy to select and rotate.
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[3d-modeling-rigging-and-animation]]** Reset pose (Alt+R) after each skinning test, and cancel with right-click to restore a bone's original position.
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[3d-modeling-rigging-and-animation]]** Be careful saving or exporting after using the Calisthenics Tool, since its added animations can conflict with saved facial animation data on the same timeline.
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) **[[common-mistakes]]** Destructive modeling changes or overridden saved animations can corrupt facial or skinning data; reapplying steps or restarting from the original template may be faster than repairing.

## Numbers
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) Facial animation timeline range: **0–330 frames (not all templates use full range)**
- [page](https://create.roblox.com/docs/avatar/character-bodies/test-blender) Required avatar rig bones: **15 bones in the Head/rig armature**

## Tools
Blender, Roblox Studio, Calisthenics Tool (Blender add-on)

## He points to
- Creating heads (Roblox docs)
- Rigging and skinning (Roblox docs)
- Character body specifications (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
