---
type: research-source
id: yt-m_4yqmzE2J0
title: "How To Make A Roblox Rig: EP10, Finalizing Your Rig (Blender) (FINAL EPISODE)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=m_4yqmzE2J0"
published: "2023-10-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 1
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "creator-workflows", "rigging-animation", "texturing-baking-uv"]
---
# yt-m_4yqmzE2J0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Final episode of a manual Blender rigging series for Roblox avatars. Covers parenting a settings bone to the head, moving the Armature modifier above Subdivision, a driver-based avatar detail switch, collection and workspace cleanup, color-coded bone groups, packing textures, a Child Of constraint for arm accessories, and a root bone. No Claude, blender-mcp, bpy or Roblox export content.

## Claims
- c1: [0:14] Parent the settings bone to the head with Shift-select then Ctrl+P, Keep Offset, so it moves when the head rotates. *(demo, high; rigging-animation)*
- c2: [0:50] Armature modifier must sit above Subdivision modifier in the stack; otherwise bends look broken when subdivision levels are raised to 2. *(demo, high; common-mistakes-fixes)*
- c3: [2:36] Avatar detail is an integer bone custom property: default 2, min 0 (so users can lower it when lagging), hard max 6, soft max 3. *(demo, high; rigging-animation)*
- c4: [3:17] Link the custom property to each mesh's viewport Subdivision levels by right-click Copy as New Driver, then Paste Driver on the levels field; skip accessories. *(demo, high; rigging-animation)*
- c5: [4:32] Put each rig in its own named collection so two rigs can coexist in one scene; hide-only eye icon for shape collections. *(demo, medium; rigging-animation)*
- c6: [6:18] Remove unneeded workspace tabs (modeling, sculpting, texture paint, geometry nodes), keep UV Editing and Scripting, and rename them for a clean default view when the rig file is opened. *(demo, medium; creator-workflows)*
- c7: [8:40] In the Scripting tab's text notes, every line must start with # or Python will try to run it as code. *(doc, high; common-mistakes-fixes)*
- c8: [10:25] Use five bone groups (settings, head, torso, left, right) with distinct colours to colour-code controllers in the viewport. *(demo, high; rigging-animation)*
- c9: [11:30] Pack textures into the .blend via File > External Data > Pack Resources so recipients without the texture files still see them. *(demo, high; texturing-baking-uv)*
- c10: [11:43] Attach arm accessories by adding a Child Of constraint targeting the armature, bone set to lower arm, then clicking Set Inverse to avoid jumping. *(demo, high; avatar-ugc-accessories)*
- c11: [14:18] Add a root bone (single bone, plane shape, bone group) and Ctrl+P Keep Offset the lower torso to it so the root drives the whole rig. *(demo, high; rigging-animation)*

## Numbers
- n1: **Avatar detail property limits**: default 2, min 0, max 6, soft max 3 
- n2: **Bone groups**: 5 (settings, head, torso, left, right) plus root added later 
- n3: **Video length**: 15:37, dated 2023-10-30, 8286 views 

## Techniques
- t1: **Custom property driver for subdivision levels**: Add integer custom property on settings bone with default/min/max/soft max. Right-click value, Copy as New Driver; on mesh modifier levels field, Paste Driver. Repeat per body mesh, skipping accessories.
- t2: **Child Of constraint for accessories**: Add Child Of constraint, target armature, pick bone, click Set Inverse so the object does not jump.
