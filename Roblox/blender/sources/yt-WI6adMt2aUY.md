---
type: research-source
id: yt-WI6adMt2aUY
title: "How to Animate Roblox Characters in Blender (2026 Tutorial)"
source_type: "youtube"
creator: "Rool-Studio"
url: "https://www.youtube.com/watch?v=WI6adMt2aUY"
published: "2026-04-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: low
tags: ["research-source", "youtube", "avatar-ugc-accessories", "blender-roblox-export-import", "other", "rigging-animation"]
---
# yt-WI6adMt2aUY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender-for-Roblox tutorial (5:38). Covers installing a Blender add-on from a zip, exporting an animation as a script copied to clipboard and importing it into Roblox Studio via a free plugin, and exporting an avatar as OBJ from Studio to build a textured R6 render rig with UGC accessories parented to bones. No Claude, MCP, or bpy content. Thin on pipeline specifics.

## Claims
- c1: [0:32] Roblox animation Blender add-on is installed from a downloaded zip via Edit > Preferences > Add-ons > Install from Disk; the zip must be extracted first. *(demo, medium; blender-roblox-export-import)*
- c2: [1:14] Add-on success is checked by seeing an 'RBLX animation' entry in the sidebar (N-panel) drop-down. *(demo, medium; blender-roblox-export-import)*
- c3: [1:24] Creator says the smooth-looking R6 rig will not work in Roblox Studio for animation; it is only for high-quality renders. *(opinion, medium; rigging-animation)*
- c4: [1:55] Animation export: plugin's 'export animation' copies a script to clipboard; Studio free toolbox plugin 'import animation from clipboard' converts it to Roblox format on the selected rig, then export animation again. *(demo, medium; rigging-animation)*
- c5: [3:15] Avatar is brought into Blender by right-clicking the avatar in Studio Explorer > Export Selection, saved as OBJ. *(demo, medium; blender-roblox-export-import)*
- c6: [3:55] Creator states the render rig texture only works with R6 textures; R15 textures will break it. *(opinion, low; rigging-animation)*
- c7: [4:15] When importing OBJ (File > Import > Wavefront OBJ), enable 'Split by Group' before importing so parts separate. *(demo, medium; blender-roblox-export-import)*
- c8: [4:36] If imported model is far off-origin, use Set Origin > Geometry to Origin to center it. *(demo, medium; blender-roblox-export-import)*
- c9: [4:50] Delete the blocky default body parts from the imported OBJ, keeping only the UGC accessory meshes. *(demo, medium; avatar-ugc-accessories)*
- c10: [4:50] Attach accessories: in Pose Mode, select accessory, shift-select target bone, Ctrl+P > Bone to parent it. *(demo, medium; avatar-ugc-accessories)*
- c11: [5:17] Render setup: add camera (Shift+A) since Blender needs one; set output folder in Output Properties or output is lost; render via Render menu. *(demo, medium; other)*

## Numbers
- n1: **video length**: 5:38 

## Techniques
- t1: **Clipboard animation transfer**: Blender plugin 'export animation' copies script to clipboard; in Studio select rig, run plugin, 'import animation from clipboard', then export animation.
- t2: **Studio OBJ round-trip for render rig**: Studio Export Selection to OBJ; Blender import with Split by Group; set origin to geometry; delete body parts; keep accessories.
- t3: **Bone parenting accessories**: Pose mode; select mesh then bone; Ctrl+P > Bone to weld accessory to rig bone (e.g., head).

## Quotes (brief, for attribution)
> that smooth-looking R6 rig won't actually work in Roblox Studio for this. It's strictly for rendering high-quality images and videos  (at 1:24, Rool-Studio)

## Points to
- Creator Discord server (source of Blender add-on zip, starter rig zip, and face textures)
- Roblox Studio free toolbox plugin for animation import
