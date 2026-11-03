---
type: research-source
id: yt-VWdcKJCJ5Fk
title: "🎩 Beginner’s Guide to Roblox UGC (2025-2026) | What It Is + How to Get Started"
source_type: "youtube"
creator: "Zander"
url: "https://www.youtube.com/watch?v=VWdcKJCJ5Fk"
published: "2025-07-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 2
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "other"]
---
# yt-VWdcKJCJ5Fk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner UGC walkthrough: model accessory in Blender (mirror, seams, UVs), export OBJ/FBX, texture in Substance Painter, export 2D or PBR maps, import to Studio, build via UGC Makers Kit (SpecialMesh for 2D, MeshPart+SurfaceAppearance for PBR). Covers 4,000-tri limit, 750 Robux upload fee, publish costs. No blender-mcp or bpy content.

## Claims
- c1: [0:36] Creator requirements: ID verified and a Premium 1000 or Premium 2200 subscription kept active for as long as UGC items stay published and on sale. *(doc, medium; avatar-ugc-accessories)*
- c2: [1:20] Accessory mesh must be a single mesh, max 4,000 triangles, and fit within size bounds. *(doc, medium; mesh-texture-limits)*
- c3: [3:38] Fill faces to keep mesh watertight (UGC requirement); also prevents seeing inside when a user is headless. *(opinion, medium; avatar-ugc-accessories)*
- c4: [4:20] Marking seams in Blender splits faces when unwrapping, giving separate UV islands for texturing. *(demo, high; mesh-texture-limits)*
- c5: [5:10] Mirrored halves share one UV side, so texture density doubles, but shadows look less realistic. *(opinion, low; mesh-texture-limits)*
- c6: [5:51] Export as OBJ or FBX from Blender before texturing in Substance Painter; presenter prefers OBJ. *(demo, medium; other)*
- c7: [6:46] Substance Painter new-project document resolution set to 1024; bake output at 4K with 16x anti-aliasing (not exported). *(demo, medium; mesh-texture-limits)*
- c8: [12:00] For PBR, export surface appearance maps at 256x256; base color map may be 1024x1024; other PBR maps locked at 256x256. *(doc, medium; mesh-texture-limits)*
- c9: [13:06] Color maps 1024x1024 while other PBR textures are locked at 256x256 for performance, per Roblox announcement. *(doc, medium; mesh-texture-limits)*
- c10: [14:09] Node Wrangler add-on (built into Blender, enabled in Preferences > Add-ons) used to auto-load PBR maps into Principled BSDF via Ctrl+Shift+T. *(demo, medium; blender-roblox-export-import)*
- c11: [14:50] Custom scratch/normal detail on PBR loses quality; workaround is baking everything into one 2D texture for base color and disabling height/normal maps. *(opinion, low; mesh-texture-limits)*
- c12: [16:25] Import 3D in Studio home tab; if using rig, set item position to 0,0,0 to auto-align to avatar. *(demo, medium; blender-roblox-export-import)*
- c13: [16:51] UGC Makers Kit plugin used to create accessory and thumbnails; Roblox built-in accessory creator is the free alternative. *(demo, medium; avatar-ugc-accessories)*
- c14: [17:33] Normal (2D) accessories use SpecialMesh; PBR accessories use MeshPart. Thumbnail FOV set to 70. *(demo, medium; avatar-ugc-accessories)*
- c15: [18:35] For PBR MeshPart: remove TextureID from the handle mesh and add a SurfaceAppearance with the maps. *(demo, medium; avatar-ugc-accessories)*
- c16: [19:56] As of video, UGC thumbnails do not render PBR; they show plain renders. *(experience, medium; avatar-ugc-accessories)*
- c17: [20:09] Upload fee is 750 Robux per item submission and is non-refundable even if declined. *(doc, medium; avatar-ugc-accessories)*
- c18: [20:50] Publishing cost: 600-1,500 Robux for non-limited accessories/layered clothing; 5,000-15,000 for limiteds. *(doc, medium; avatar-ugc-accessories)*
- c19: [21:31] Presenter advises pricing at the price floor because the UGC market is flooded (opinion). *(opinion, medium; avatar-ugc-accessories)*
- c20: [21:57] Check triangle count via overlays dropdown > Statistics, then select the item. *(demo, high; mesh-texture-limits)*
- c21: [22:26] Presenter describes UGC as a flooded, gamble-like market; not a reliable income path for beginners (opinion). *(opinion, low; avatar-ugc-accessories)*

## Numbers
- n1: **max triangles per accessory mesh**: 4,000 
- n2: **Substance Painter document resolution**: 1024 
- n3: **bake output size / anti-aliasing**: 4K / 16x 
- n4: **PBR non-color map size**: 256x256 
- n5: **PBR base color map size**: 1024x1024 
- n6: **thumbnail camera FOV**: 70 
- n7: **upload fee per submission**: 750 Robux 
- n8: **non-limited publish cost**: 600-1,500 Robux 
- n9: **limited publish cost**: 5,000-15,000 Robux 

## Techniques
- t1: **Seam-based UV unwrap before texturing**: Mark seams on edges (right-click Mark Seam), unwrap in UV editor, arrange islands with UV Packmaster; scale to fit bounds.
- t2: **Baked-AO dirt mask in Substance Painter**: Add black mask, add Ambient Occlusion generator, invert, set layer to soft light, blur, tune opacity; similar with curvature for edges.
- t3: **PBR preview in Blender via Node Wrangler**: Duplicate material, select Principled BSDF, Ctrl+Shift+T, pick color map, load other maps automatically.
- t4: **PBR MeshPart accessory setup**: Create MeshPart accessory in UGC Makers Kit, delete TextureID on Handle, add SurfaceAppearance and assign maps.

## Quotes (brief, for attribution)
> it must be a single mesh with a maximum of 4,000 triangles  (at 1:20, Zander)
> there is a upload fee of 750 Robux per item submission  (at 20:09, Zander)

## Points to
- UGC Makers Kit (Roblox plugin)
- Substance Painter
- Node Wrangler (Blender add-on)
- UV Packmaster
- SoftGB starter rigs
