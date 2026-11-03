---
type: research-source
id: web-c887d9b5a0
title: "DevForum thread 3844846"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/3844846"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.1137
relevance: 3
density: high
tags: ["research-source", "web", "common-mistakes-fixes", "creator-workflows", "roblox-import-pipeline", "roblox-mesh-limits", "texturing-baking-uv"]
---
# web-c887d9b5a0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum optimization guide for Roblox models (reviewed by Roblox rendering team input). Covers import limits, OBJ vs FBX, texture size and compression, SurfaceAppearance vs MaterialService, transparency, emissive tricks, RenderFidelity, CollisionFidelity, shadows, lights, draw calls, with an elevator consolidation example. No Claude, MCP or bpy content.

## Claims
- c1: Author states max import is 21k tris per mesh via 3D Importer and 10k via Asset Manager/other importers; later text says 10k per mesh, so the figures are inconsistent. *(doc, medium; roblox-mesh-limits)*
- c2: OBJ imports everything as one mesh and is usually more accurate to scale without changing Blender settings. FBX allows up to 200 objects per file, so 1,000 objects need 5 FBX files. *(experience, medium; roblox-import-pipeline)*
- c3: Max texture is 1024x1024; prefer 512 or 256. One 1024 is much more performant than four 512s because compression targets file size (512 may be ~80% of a 1024's size) and extra draw calls arise. *(experience, medium; texturing-baking-uv)*
- c4: Solid-colour metalness/roughness maps can be a single pixel. SurfaceAppearance uses Albedo, Metalness, Normal, Roughness; Substance Painter has an export preset. *(experience, medium; texturing-baking-uv)*
- c5: Merge meshes sharing a SurfaceAppearance into one mesh unless it harms collisions or function; keep moving parts separate. Use MaterialService tileable materials for non-hero assets: loaded once, fewer draw calls. *(experience, medium; creator-workflows)*
- c6: Set RenderFidelity to Performance in about 95% of cases; Precise only for things like mountain ranges. Workaround for distant objects: import as SpecialMesh and offset the mesh; allows objects larger than 2048 studs, but no SurfaceAppearance support. *(experience, medium; roblox-mesh-limits)*
- c7: Set CollisionFidelity as simple as possible (Box for most). Use Hull for wheels or bags, Default for handles, PreciseConvexDecomposition for walls, floors and ceilings the player interacts with. Disable collisions on buttons and bolts. Lower fidelity reduces memory and load time. *(experience, medium; roblox-mesh-limits)*
- c8: Disable CastShadow on parts whose shadow does not change the look; the gain at scale is significant. Point lights are costlier than surface or spot lights; moving lights add draw calls. *(experience, medium; roblox-mesh-limits)*
- c9: Budget about 500 draw calls for low-end devices. Reuse the same MeshIds and materials so they batch. UI also costs draw calls. Batching does not apply to transparent objects. *(experience, medium; roblox-mesh-limits)*
- c10: Transparency without alpha maps gives white haze at edges with mipmapping; use alpha channels in TGA for foliage. Transparency sorts per instance, back to front. Overlapping transparent objects hurt performance. *(experience, medium; texturing-baking-uv)*
- c11: Emissive: use Neon material on separated mesh parts. Trick: Color3/vertex colour values above 255 make surfaces glow, e.g. a SpecialMesh overlay with the emissive texture. *(experience, low; texturing-baking-uv)*
- c12: Remove hidden or interior faces in Blender via Select > Select All by Trait > Interior Faces > delete. Prefer clean joined geometry over intersecting cylinders. Keep detail in textures and preserve silhouette. *(experience, high; common-mistakes-fixes)*
- c13: Hero assets over 10k tris should be split into multiple meshes, each with its own 1024 texture set (e.g. rifle stock vs receiver/barrel). *(experience, medium; creator-workflows)*
- c14: Elevator example: 40 SurfaceAppearance objects x 4 maps (about 160 textures) and 42 meshes could drop to about 4 texture sets (16 textures) and about 8 meshes. Leave buttons untextured to script glow in engine. *(experience, medium; creator-workflows)*
- c15: Parts are slightly more optimized than meshes; replace meshes with parts where possible (author says difference is minimal but matters at scale). *(opinion, low; roblox-mesh-limits)*

## Numbers
- n1: **Max tris per mesh, 3D Importer**: 21k Author's stated limit
- n2: **Max tris per mesh, Asset Manager**: 10k Author's stated limit
- n3: **Max objects per FBX**: 200 Split larger scenes into multiple FBX files
- n4: **Max texture size**: 1024x1024 Prefer 512 or 256
- n5: **Draw call budget**: ~500 Target for low-end devices
- n6: **SpecialMesh size note**: more than 2048 studs cubed Typical size limit exceeded using SpecialMesh

## Techniques
- t1: **Delete interior faces**: In Blender: Select > Select All by Trait > Interior Faces, then delete. Enable Statistics overlay to count objects.
- t2: **Collision rebuild**: Set mesh to Box with CanCollide off and rebuild needed collisions with invisible parts. Visualize with the Mesh Optimization Tools plugin.
- t3: **Distant large mesh via SpecialMesh**: Import as SpecialMesh, place near players, set the inner Mesh object's Offset to the desired position. Keeps Performance fidelity and lighting interaction.

## Contradictions flagged
- Says 21k tris per mesh via 3D Importer and 10k elsewhere, but later says 'tri limit per mesh is 10k' and gives 20k combined OBJ figure (vs itself)

## Points to
- Mesh Optimization Tools plugin (create.roblox.com/store/asset/414923656)
- MrChickenRocket RDC 2024 talk: Using Roblox Tools to Improve Performance
- devforum.roblox.com/t/how-to-use-alpha-channels-for-transparent-textures/2312747
- Substance Painter
