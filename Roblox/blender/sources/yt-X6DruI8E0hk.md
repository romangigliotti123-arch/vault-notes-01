---
type: research-source
id: yt-X6DruI8E0hk
title: "NEW FREE ROBLOX RIG ADDON (Roblox Rigs Suite) | Blender"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=X6DruI8E0hk"
published: "2025-03-22"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0640
relevance: 1
density: low
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "creator-workflows", "rigging-animation"]
---
# yt-X6DruI8E0hk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Showcase of a third-party paid/pay-what-you-want Blender add-on (Roblox Rigs Suite v1.0.0) for posing/animating Roblox-style R6/R15 rigs for GFX/renders. Covers rig types, quality settings, IK, accessory/layered-clothing/face-rig attach tools. Not about Claude, MCP, bpy scripting or exporting to Roblox Studio; relevant only tangentially to rigging/accessory workflows in Blender.

## Claims
- c1: [1:10] Add-on imports Blocky, Roblox 2.0, man, woman, boy, girl and superhero rigs, each in R6 and R15 (except blocky sharp variant, which has no R15). *(demo, high; rigging-animation)*
- c2: [3:29] Rig quality levels: compatibility = 0 subdivisions, balanced (default) = 1, high = 2, ultra = render default. Separate viewport and render quality; lower viewport quality improves performance. *(demo, high; rigging-animation)*
- c3: [4:51] R15 rigs have no rig-quality setting because they keep original Roblox geometry unedited. R15 versions lack finger controls. *(demo, high; rigging-animation)*
- c4: [5:31] IK/fancy feet switches are sliders rather than checkboxes/integers, making it easier for animators to blend in and out. IK limbs follow their limbs when fancy feet/wrists are off. *(demo, medium; rigging-animation)*
- c5: [7:46] 3D/layered clothing auto-rig tool offers three binding methods: surface deform (best, works best for blocky rigs), data transfer, and Blender automatic weights. Author calls it the most unreliable tool, especially for non-blocky rigs. *(demo, medium; avatar-ugc-accessories)*
- c6: [8:26] Manual prep before binding clothing: edit mode, select all, Alt+J / M merge by distance, fix normals (add-on does this), then separate arm parts via Ctrl+L and P by selection. *(demo, medium; common-mistakes-fixes)*
- c7: [9:08] Bind clothing at the same quality as the render quality (bind on ultra sets viewport to ultra), otherwise it looks dysfunctional when rendered at ultra. *(demo, medium; avatar-ugc-accessories)*
- c8: [10:26] Accessory attach tool: choose accessory type (head, shoulder, gear with hand choice etc.), pick accessory object, attach. 'Link materials' copies the rig material; avoid for accessories using different textures. *(demo, medium; avatar-ugc-accessories)*
- c9: [7:26] Custom head/face rig tool: delete existing head, select the armature, choose face rig, click bind. *(demo, medium; rigging-animation)*
- c10: [11:18] Animation linker transfers animation between rigs; both rigs need the same IK settings or it likely fails. *(demo, medium; rigging-animation)*
- c11: [15:00] Finger autocurl curls fingers when rotating upper finger controls; thumb autocurl and fingertip-hide options exist, per-hand settings. R6 rigs only. *(demo, medium; rigging-animation)*
- c12: [1:10] Install: Edit > Preferences > Add-ons > Install from Disk using the unextracted zip. Distributed via Gumroad pay-what-you-want. Targets posing/GFX, not Studio export. *(demo, high; creator-workflows)*

## Numbers
- n1: **subdivisions: compatibility/balanced/high**: 0/1/2 rig quality levels; ultra is render default
- n2: **rig types**: 7 packages, R6 and R15 Blocky, Roblox 2.0, man, woman, boy, girl, superhero
- n3: **tools in v1.0.0**: 4 custom head/face rig, layered clothing, accessory attach, animation linker

## Techniques
- t1: **Bind 3D clothing to rig**: Edit mode, select all, merge by distance, split clothing per limb with Ctrl+L then P by selection, select rig, set clothing part to body part object, choose binding method, bind (match render quality).
- t2: **Author's GFX rig setup routine**: Shift+A add R6 boy rig, set own texture in material settings, import hair OBJ, split by group, delete non-hair, attach as head accessory with link materials, enable finger autocurl, pose.

## Points to
- Roblox Rigs Suite (Gumroad, ComixProd)
- Fluid Rig
- Cloud Face face rig
- Comix Productions Discord

## Visual notes
Contact sheet shows Gumroad product page (Roblox Rigs Suite, Action Lightrooms, ViRig) and Blender UI with the Importer/rig panel and blocky rigs; no export settings shown.
