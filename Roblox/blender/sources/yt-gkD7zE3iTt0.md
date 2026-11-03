---
type: research-source
id: yt-gkD7zE3iTt0
title: "Roblox UGC | How to create ANIMATED ITEMS"
source_type: "youtube"
creator: "Zander"
url: "https://www.youtube.com/watch?v=gkD7zE3iTt0"
published: "2026-10-27"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# yt-gkD7zE3iTt0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Roblox UGC tutorial (10 min) on making animated transformation accessories (horns morphing to halo) in Blender: a rig as position reference, bevel/curve horns, torus halo, plane slices with Array modifier, Bool Tool boolean cut with Exact solver, flipped normals for two-sided visibility, a 256x256 split-color texture, then OBJ/FBX export and import into Roblox Studio as an accessory. No bpy, blender-mcp, or Open Cloud content.

## Claims
- c1: [0:35] Animated transformation effect is built by slicing a horn/halo mesh with planes (Array modifier) and Boolean-cutting it, so only the revealed portion shows over time. *(demo, high; avatar-ugc-accessories)*
- c2: [4:25] Boolean solver set to Exact produced the slices; resulting mesh was about 900 triangles for the horns pair; author estimates ~2,000 triangles per item alone. *(demo, medium; mesh-texture-limits)*
- c3: [5:06] Array distance 0.05 gives more slices but is heavy and laggy; 0.1 with count 125 was used, yielding ~1,800 triangles for the cutter plane. *(demo, medium; mesh-texture-limits)*
- c4: [6:06] Red face normals are invisible in Roblox Studio; blue side is visible, so normals must face outward for the visible side. *(demo, medium; avatar-ugc-accessories)*
- c5: [6:35] Halo slices are flipped with Alt+N in edit mode so the effect is visible from both sides. *(demo, medium; avatar-ugc-accessories)*
- c6: [7:40] Texture sheet of 256x256 is enough for a solid-color effect; one half one color, other half another, projected from view per side. *(demo, medium; mesh-texture-limits)*
- c7: [8:20] Apply texture by assigning image texture to a material in Blender and checking in material preview; overlapping horns moved apart. *(demo, low; mesh-texture-limits)*
- c8: [9:02] Export as OBJ or FBX, import via Studio's import tool, then make it an accessory as usual. *(demo, medium; blender-roblox-export-import)*
- c9: [1:44] Horns made from a path under the Curve menu, shaped by hand; halo is a torus shaded smooth. *(demo, medium; other)*
- c10: [0:14] Source does not use Claude, blender-mcp, or bpy scripting; all steps are manual Blender GUI. *(demo, high; claude-blender-ai)*

## Numbers
- n1: **triangles**: 900 combined boolean horns after Exact solver
- n2: **Array distance / count**: 0.1 / 125 halo/cutter plane slicing; 0.05 called laggy
- n3: **triangles**: 1800 cutter plane alone, author says seems good
- n4: **plane Z rotation**: -5 degrees rotation of slicing plane
- n5: **plane rotation**: 90 degrees from front view
- n6: **texture size**: 256x256 solid-color split texture sheet

## Techniques
- t1: **Array + Boolean slice cut**: Add Array modifier to plane, Ctrl+numpad +/- for Boolean (Bool Tool add-on), set solver Exact, tune Array distance and count, apply modifiers.
- t2: **Flip normals for two-sided visibility**: Edit mode on halo slices, select, Alt+N flip so both sides render in Studio.
- t3: **Project-from-view split texture**: Project each side from view, paint each half a different solid color on a 256px sheet, assign as image texture.

## Quotes (brief, for attribution)
> change that to exact, and that'll make it into the slices for us  (at 4:25, Zander)
> what's red wouldn't be visible, so this side is not visible in Roblox Studio  (at 6:06, Zander)

## Points to
- Bool Tool add-on (Blender)
- Roblox Studio import tool
- Affinity (texture painting)
