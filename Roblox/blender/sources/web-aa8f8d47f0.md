---
type: research-source
id: web-aa8f8d47f0
title: "DevForum thread 512059"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/512059"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0034
relevance: 2
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "creator-workflows", "roblox-import-pipeline", "roblox-mesh-limits", "texturing-baking-uv"]
---
# web-aa8f8d47f0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
2020 DevForum tutorial by ADbros: model a face-mask UGC hat in Blender 2.82. Workflow: export a character .obj via the Load Character plugin, import it to Blender with Split by Group, model over the head, decimate to the UGC triangle limit, Smart UV Project, paint the texture, then import via a MeshPart's MeshId and set TextureID. No blender-mcp, Claude, or bpy content. Thread replies are mostly praise.

## Claims
- c1: Character exported from Studio as .obj via AlreadyPro's Load Character plugin (right-click, Export Selection) to use as a head base in Blender. *(doc, high; roblox-import-pipeline)*
- c2: Blender 2.8+ OBJ import needs 'Split by Group' ticked, otherwise the whole character imports as one model with no separate limbs. *(experience, high; common-mistakes-fixes)*
- c3: Author states UGC hat triangle limit was 4k in April 2020; model was slightly over, reduced with Decimate modifier. *(doc, medium; roblox-mesh-limits)*
- c4: Author uses Smart UV Project, then paints colour directly on the UVs in Texture Paint; claims manual seams unnecessary because seams are not visible. *(opinion, medium; texturing-baking-uv)*
- c5: HoudiniDev advises manual seaming and unwrapping, plus compressing textures to 256px, for better results; author disagrees for this simple case. *(opinion, medium; texturing-baking-uv)*
- c6: Imported OBJ appears black or untextured in Roblox; fix is to set the MeshPart TextureID property to the saved texture. *(experience, medium; common-mistakes-fixes)*
- c7: Blender textures may not show in viewport; fix reported by a commenter is enabling Texture under Viewport Shading > Color. *(experience, low; common-mistakes-fixes)*
- c8: Import flow: insert MeshPart, set MeshId to the .obj via folder picker, dismiss the pop-up with No, then position manually. *(doc, medium; roblox-import-pipeline)*
- c9: Commenter claims Roblox accepts textures up to 1024x1024 and downscales larger ones; author's earlier claim of automatic 420x420 compression is disputed. *(opinion, low; roblox-mesh-limits)*
- c10: Commenters state that in 2020 only a small UGC-program beta group (around 20-30 people) could list hats in the catalog; submitting via support email was discouraged. *(opinion, low; creator-workflows)*

## Numbers
- n1: **UGC hat triangle limit (2020)**: 4k tris 
- n2: **Texture size claimed by author**: 420x420 (auto-compressed, disputed) 
- n3: **Texture size claimed by commenter**: max 1024x1024, larger downscaled 
- n4: **Texture size suggested by HoudiniDev**: 256 px 
- n5: **Blender version used**: 2.82 (commenter also 2.83) 
- n6: **UGC beta participants (commenter estimate)**: around 20-30 

## Techniques
- t1: **Smart UV Project + texture paint**: Edit mode, U > Smart UV Project. In UV editor create Image > New and save it. Add Image Texture to Base Colour, switch to Texture Paint, fill selected parts (L then M).
- t2: **Decimate modifier for tri budget**: Add Decimate, drag ratio slider while watching the tri count in the status bar, apply before texture painting.
- t3: **Split by Group OBJ import**: In Blender File > Import > OBJ, tick Split by Group so each body part loads as its own object.
- t4: **MeshPart MeshId import**: Insert MeshPart, click MeshId folder, select .obj, click No on the pop-up, then set TextureID to the saved image if texture is missing.

## Quotes (brief, for attribution)
> Unwrapping manually isn't needed in this case, as texture painting paints on the UVs, therefore seams won't be visible.  (devforum.roblox.com)
> When you import your obj file in Blender 2.8 and above, you need to tick "Split by Group" to import the character with limbs as separate models!  (devforum.roblox.com)
> No, only the few people who are in the UGC program can add hats to the catalog. It's not available publicly yet, it's still in beta.  (devforum.roblox.com)

## Contradictions flagged
- Roblox automatically compresses textures to 420x420. (vs Commenter Astreastela: Roblox accepts images up to 1024x1024 and only downscales larger ones.)
- Manual UV unwrapping is unnecessary when texture painting; seams won't show. (vs HoudiniDev: manually seam and unwrap for best texture results.)

## Points to
- https://www.roblox.com/library/752585459/Load-Character-Lite
- https://www.blender.org/
- https://twitter.com/ADbrosRBLX
