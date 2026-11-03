---
title: "Docs: art / characters / validation-tool"
url: https://create.roblox.com/docs/art/characters/validation-tool.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / validation-tool

[Open](https://create.roblox.com/docs/art/characters/validation-tool.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page for the Avatar Validation Tool, a Blender add-on (Blender 3.5.1+) that checks character models against Roblox avatar specs and auto-fixes some issues. The tool is no longer in active development and is not a substitute for testing in Studio.

## Tips
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[building-art-and-assets]]** Install the Validation Tool add-on in Blender 3.5.1+; earlier versions may behave unexpectedly.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[building-art-and-assets]]** Set the Target Armature via eyedropper on the armature object (often named Joints or Armature) before running checks.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[building-art-and-assets]]** Freeze geometry location, rotation and scale to 0,0,0 before export; auto-fix may alter your rig, so back up first.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[building-art-and-assets]]** Keep body UVs within the 0-1 range; this must be fixed manually.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[building-art-and-assets]]** Avoid N-gons, non-manifold geometry and vertex color data; keep meshes watertight and within polycount budgets.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[3d-modeling-rigging-and-animation]]** Ensure Root and HumanoidRootNode bones exist, Root sits at world 0,0,0, and Left/Right bones are on correct axes.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[3d-modeling-rigging-and-animation]]** Corrective FACS poses must include existing base poses and use no more than 3 base poses; include a Neutral Pose mapping.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[3d-modeling-rigging-and-animation]]** Remove duplicate head bone names (.001, .002 suffixes) to avoid face joint errors.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[3d-modeling-rigging-and-animation]]** Remove keyframes on non-face objects, but never delete keyframes that also contain facial data.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[building-art-and-assets]]** Remove extra layers, orphan data and unused materials from the scene before export.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[building-art-and-assets]]** Check that cage meshes do not intersect character geometry; use a fresh template cage if cage UV auto-fix fails.
- [page](https://create.roblox.com/docs/art/characters/validation-tool) **[[testing-debugging-and-qa]]** Do not rely on the validation tool alone; always test characters in Studio and verify body specs manually.

## Numbers
- [page](https://create.roblox.com/docs/art/characters/validation-tool) Minimum Blender version: **3.5.1** (Validation Tool plugin compatibility requirement)
- [page](https://create.roblox.com/docs/art/characters/validation-tool) Max base poses per corrective FACS pose: **3** (FACS Data check; corrective poses must not use more than 3 base poses)
- [page](https://create.roblox.com/docs/art/characters/validation-tool) UV coordinate range: **0-1** (Body geometry UVs must fall within this range)

## Tools
Avatar Validation Tool (Blender add-on), Blender 3.5.1+, Roblox Studio

## He points to
- ValidationTool_Blender.zip

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
