---
type: research-source
id: yt-Cl6OZ8V1r6E
title: "FIXED R15, NEW TOOL, AND MORE! - Roblox Rigs Suite (Update)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=Cl6OZ8V1r6E"
published: "2026-02-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0030
relevance: 2
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "creator-workflows", "rigging-animation", "roblox-import-pipeline"]
---
# yt-Cl6OZ8V1r6E

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Update walkthrough for "Roblox Rig Suite" (a Blender add-on, not blender-mcp or bpy-scripting). Covers R15 texture-compatibility fix via a rig variant setting, new rig types, IK pole placement, a "remove compatibility" tool that bakes IK and strips drivers for export, custom face toggling, and bug fixes. Only tangentially relevant to Claude-driven Blender or the Roblox import pipeline.

## Claims
- c1: [0:56] Creator says Roblox's 2025 new R15 rigs broke textures saved from new R15 models; add-on now offers a rig variant setting (2025 default or legacy) to fix texture fit. *(demo, medium; roblox-import-pipeline)*
- c2: [1:36] Creator states legacy-rig textures fail on new R15 rigs and vice versa; switching variant to default makes the texture apply correctly in the demo. *(demo, medium; rigging-animation)*
- c3: [2:18] Add-on now provides a blocky-legged woman rig in both legacy and R15 variants; IK pole targets moved to the front of the limb instead of the side. *(demo, medium; rigging-animation)*
- c4: [4:23] Render rig quality gained a maximum-detail option at four subdivisions, above ultra-level three, for close-up production renders. *(demo, medium; rigging-animation)*
- c5: [5:51] Add-on preference 'unlink rigs' fully removes a deleted rig from the Blender file (not just the scene) but keeps imported textures. *(demo, medium; creator-workflows)*
- c6: [7:11] Remove compatibility tool (presets default/custom/light/full) strips drivers, edge splits, bone shapes and extra nodes, and can bake all keyframes plus IK into FK for software without IK support. *(demo, medium; rigging-animation)*
- c7: [9:54] Custom faces are now toggled live with a button in the material settings panel instead of requiring a reimport with a 'use custom faces' option. *(demo, medium; avatar-ugc-accessories)*
- c8: [10:36] Custom face textures can be an image sequence for animated 2D faces, and the edit-mapping panel adjusts texture size and rotation. *(demo, medium; avatar-ugc-accessories)*
- c9: [12:40] Restore defaults in the rig manager resets rig settings but intentionally keeps the imported texture; glossy or bump settings are reset by it. *(demo, medium; rigging-animation)*
- c10: [13:20] A show-in-front option makes thin controllers on rigged 3D clothing visible while posing; creator notes it is the same property as the Blender bone setting, now exposed in the add-on. *(demo, medium; avatar-ugc-accessories)*
- c11: [14:42] Add-on can set rotation mode (for example WXYZ or XYZ Euler) on every bone at once; render smooth fix is an option some packages turn off by default. *(demo, medium; rigging-animation)*
- c12: [15:55] Fixed bug where binding 3D clothing on ultra did not set viewport quality to ultra, causing mesh explosion artifacts when the quality was changed. *(demo, medium; common-mistakes-fixes)*
- c13: [17:18] Fixed the 3D clothing attachment tool, which failed in Blender versions above 4.5; creator says it now works in 5.0. *(demo, medium; common-mistakes-fixes)*
- c14: [17:56] Fixed arm IK flipping because the IK constraint pole angle on the control had been inverted; the same issue existed on the girl rig. *(demo, medium; rigging-animation)*
- c15: [18:47] Creator says the remove compatibility tool took most of the development time and will need updates if Blender changes break it. *(opinion, medium; creator-workflows)*

## Numbers
- n1: **render rig quality subdivisions**: 4 (new 'maximum detail', above ultra at 3) 
- n2: **testers for update**: 3 
- n3: **rig vault size**: up to 50 unusual rigs (free and paid versions) 
- n4: **version**: Roblox Rig Suite 1.2, released 2026-02-07 

## Techniques
- t1: **Rig variant switch for texture fit**: Set generation to R15, open Advanced, choose rig variant 2025 default or legacy to match the texture source rig before applying the texture.
- t2: **Bake-and-strip before export**: Run remove compatibility on custom preset with driver cleanup, bone shapes, material compatibility, extra nodes and bake animations enabled to make an add-on-free universal rig.
- t3: **Live custom face toggle**: In material settings, use the toggle custom faces button instead of reimporting with a use-custom-faces option.

## Quotes (brief, for attribution)
> a lot of what took the time out of everything was that remove compatibility tool  (at 18:47, Comix Productions)

## Points to
- Roblox Rig Suite Discord
- Gumroad (Roblox rig vault)
