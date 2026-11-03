---
type: research-source
id: yt-t2oo2j88Qt8
title: "How to create layered clothing for Roblox | Roblox UGC Tutorial 2026"
source_type: "youtube"
creator: "Zander"
url: "https://www.youtube.com/watch?v=t2oo2j88Qt8"
published: "2026-09-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 2
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-t2oo2j88Qt8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Manual Blender workflow for Roblox layered clothing (shirt and pants) using the RBX Tools Blender add-on. Covers offset shell, seams and face-set sculpting, UV unwrap, watertight caps, inner and outer cages named {item}_InnerCage and {item}_OuterCage, weight painting with limit 4, export, and Studio accessory setup. No blender-mcp, bpy, or Claude content.

## Claims
- c1: [0:00] Creator recommends the RBX Tools Blender add-on for its file export, layered clothing pages and armature, which they say speeds the workflow. *(experience, medium; avatar-ugc-accessories)*
- c2: [2:41] Offsetting the cloth shell outward by about 0.015 (Alt+S) is used to create clearance over the body before sculpting. *(demo, medium; avatar-ugc-accessories)*
- c3: [8:29] Pants were already under 4,000 triangles, so no retopology was needed before applying the multires modifier. *(demo, medium; mesh-texture-limits)*
- c4: [3:26] Sculpting workflow: mark seams, initialize face sets by UV seams, then use Planar/Grab brushes with auto-masking set to face sets to shape folds. *(demo, medium; other)*
- c5: [17:01] Cap open ends (merge/extrude then scale to zero) so the mesh is watertight and the one-way invisible faces Roblox adds are not visible. *(experience, medium; avatar-ugc-accessories)*
- c6: [18:51] Cages must be named {itemName}_InnerCage and {itemName}_OuterCage; creator is unsure whether names are case sensitive and recommends matching exactly. *(experience, medium; avatar-ugc-accessories)*
- c7: [19:32] Outer cage must cover the entire mesh and tells other clothing how to deform over this item; inner cage tells this item how to deform over the avatar or other clothes. Creator says both are required for layered clothing. *(experience, high; avatar-ugc-accessories)*
- c8: [24:02] When edge-sliding cage geometry, turn off Correct UVs; cages must keep their original UVs or the layered clothing breaks. *(experience, high; avatar-ugc-accessories)*
- c9: [26:51] Armpit area of the outer cage often needs manual fixing: select vertices, enable proportional editing, and move slightly with mirroring on. *(demo, low; avatar-ugc-accessories)*
- c10: [30:54] Weight paint via Ctrl+P with automatic weights, then in weight paint mode use Weights > Limit Total set to 4 per vertex. *(demo, high; rigging-animation)*
- c11: [32:17] Test weights by posing the armature in pose mode; collar and lower body often need less influence and should be painted out with strength around 0.5. *(demo, medium; rigging-animation)*
- c12: [36:45] Export by selecting the armature and the item, then the item's pages (via RBX Tools), and export as FBX. *(demo, medium; blender-roblox-export-import)*
- c13: [37:46] In Studio, import the FBX via Import, then Avatar tab > accessory > clothing type, Next, preview, then Generate MeshPart Accessory and Confirm; delete the old mesh. *(demo, high; blender-roblox-export-import)*
- c14: [39:21] Upload via Save to Roblox as an avatar item of the chosen accessory type; the t-shirt validated even with no texture applied. *(experience, medium; avatar-ugc-accessories)*
- c15: [40:03] Test by placing the item in StarterPlayer > StarterCharacterScripts, or by pasting it onto a mannequin in the character rig to check deformation. *(demo, medium; avatar-ugc-accessories)*

## Numbers
- n1: **Shell offset**: 0.015 
- n2: **Triangle count (pants) before retopo skipped**: under 4,000 
- n3: **Limit Total max influences per vertex**: 4 
- n4: **Weight paint strength suggested**: 0.5 

## Techniques
- t1: **Offset shell and multires sculpt**: Select all, Alt+S offset ~0.015, subdivide or add multires, then sculpt folds in face sets. Apply multires when done.
- t2: **Seam-based face sets**: Mark seams where folds should split, Initialize Face Sets by UV Seams, then auto-mask by face sets to sculpt one panel at a time.
- t3: **Inner and outer cage pair**: Duplicate cage, Alt+P clear parent keep transform, rename to item_InnerCage and item_OuterCage, loop select and Alt+S outer cage to cover mesh.
- t4: **Auto-weights then limit-and-paint**: Parent item to armature with automatic weights, then Limit Total 4, paint zero weights on unneeded areas, smooth or blur.

## Quotes (brief, for attribution)
> your goal with an outer cage is to cover the entire mesh  (at 19:32, Zander)
> make sure to turn off correct UVs. The cages must stay with their original UVs, or else it will break.  (at 24:02, Zander)
> click on limit total. Make sure the limit is four.  (at 30:54, Zander)

## Contradictions flagged
- For avatars only the inner cage matters, but layered clothing requires both cages. (vs Creator's own statement in the same segment (19:32-20:56); not a true contradiction, noted for context)

## Points to
- RBX Tools Blender add-on
- UV Pack Master
