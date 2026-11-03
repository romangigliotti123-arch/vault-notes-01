---
type: research-source
id: web-9462f5d8ee
title: "Roblox docs: avatar/character-bodies/test-blender"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/character-bodies/test-blender.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "rigging-animation"]
---
# web-9462f5d8ee

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on verifying avatar character bodies in Blender before Studio import. Covers checking facial animation data (timeline 0–330, neutral pose on frame 0, Head_Geo RootFaceJoint attribute, FACS pose names) and skinning tests (Pose mode bone rotation, hiding face bones, Calisthenics Tool preview with save-conflict warning). Says nothing about blender-mcp, bpy, or the Blender-to-Roblox export pipeline.

## Claims
- c1: Facial animation timeline typically spans frames 0–330; neutral pose must be on frame 0 and keyframe gaps between posed frames should be removed. *(doc, high; rigging-animation)*
- c2: Head_Geo Custom Properties must include RootFaceJoint set to the first facial bone (often named DynamicHead), which must be a child of the Head bone. *(doc, high; rigging-animation)*
- c3: Each unique facial animation frame needs its own mapped custom property, with pose names matching the FACS pose reference spelling and capitalization. *(doc, high; rigging-animation)*
- c4: Avatar armature must contain 15 required bones, including Head. *(doc, medium; avatar-ugc-accessories)*
- c5: Skinning test: enable Show In Front on Armature, enter Pose mode, hide face bones with H, rotate body bones with R and verify mesh deformation; Alt+R clears rotation. *(doc, high; rigging-animation)*
- c6: Roblox's Calisthenics Tool adds preview animations to the timeline and may conflict with saved facial animation on the same frames; be careful when saving or exporting. *(doc, high; rigging-animation)*
- c7: If facial or skinning data is broken in a template, reskinning/remapping may be required, or it may be quicker to restart from the original template file. *(doc, medium; rigging-animation)*
- c8: Pre-import checklist covers body scale, triangle budgets, body part naming and visibility, rigging/skinning data, attachment naming and positioning, and outer cage naming and positioning. *(doc, high; avatar-ugc-accessories)*

## Numbers
- n1: **timeline frame range**: 0–330 typical facial animation timeline range in templates
- n2: **required rig bones**: 15 required bones in avatar armature, per specifications page

## Techniques
- t1: **Facial data integrity check**: Select Armature, review timeline frames, confirm neutral on frame 0, remove gaps. Check Head_Geo custom properties: RootFaceJoint, one per pose, FACS-matching names.
- t2: **Bone deformation test**: Armature > Object Properties > Viewport Display > Show In Front. Pose mode, hide face bones (H), select body bone, press R, click to confirm or right-click to cancel, Alt+R to reset.

## Quotes (brief, for attribution)
> perform the following Blender tests regularly and review any areas of concern.  (create.roblox.com)
> Be careful when saving or exporting your character when using this tool, as it may conflict with saved facial animation data that uses the same timeline.  (create.roblox.com)

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/character-bodies/specifications.md
- Calisthenics Tool (art/modeling/calisthenics-tool.md)
- Rigging and skinning (art/modeling/rigging.md)
- FACS poses reference (dynamic-heads/facs-poses-reference.md)
- Creating heads (art/characters/facial-animation/create-basic-heads.md)
