---
type: research-source
id: off-art_modeling_surface-appearance
title: "Roblox Creator Docs: art_modeling_surface-appearance"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/surface-appearance"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0044
relevance: 2
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "mesh-texture-limits", "other"]
---
# off-art_modeling_surface-appearance

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on PBR textures. Explains adding a SurfaceAppearance under a MeshPart, the five supported maps (color, normal, roughness, metalness, emissive mask), AlphaMode behavior, color tinting, and emissive rules. Mentions Blender/Maya texture settings only via a link. Does not cover blender-mcp, bpy, or the Blender-to-Roblox export pipeline.

## Claims
- c1: Studio supports 5 PBR map types: ColorMap, NormalMap, RoughnessMap, MetalnessMap, EmissiveMaskContent. Maps change appearance only, not MeshPart geometry. *(doc, high; mesh-texture-limits)*
- c2: PBR is applied by inserting a SurfaceAppearance object under a MeshPart, which overrides the original texture; each map property takes an uploaded image asset ID. *(doc, high; mesh-texture-limits)*
- c3: SurfaceAppearance properties generally cannot be modified by scripts during a game because the engine needs pre-processing. *(doc, high; mesh-texture-limits)*
- c4: Normal maps must be OpenGL format, tangent space; a flat normal map is uniform RGB [127,127,255]. R,G,B map to X,Y,Z. *(doc, high; mesh-texture-limits)*
- c5: AlphaMode options are Opaque, Overlay (default), Transparency, and TintMask. Opaque ignores alpha; Overlay reveals MeshPart.Color where alpha is transparent. *(doc, high; mesh-texture-limits)*
- c6: Transparency AlphaMode: set MeshPart.Transparency to 0 for hard-edged cutouts (foliage, lace); use at least 0.02 for soft semi-transparent detail. Values like 0.01 may still count as opaque. *(doc, high; mesh-texture-limits)*
- c7: Color tint via SurfaceAppearance.Color is a multiplier on texel color, so near-white grayscale color maps give the strongest tint. Tinting does not affect MeshPart.Color and costs no extra performance. *(doc, high; mesh-texture-limits)*
- c8: Roughness: 0% is sharp glossy reflection, 100% is matte. Doc suggests adding about 0.1 roughness to compensate for unexpected specular at some angles. *(doc, medium; mesh-texture-limits)*
- c9: Studio uses only the metalness workflow. Metalness should usually be 0 or 100%; partial values fake satin or silk. *(doc, high; mesh-texture-limits)*
- c10: Marketplace avatar items (3D accessories, layered clothing, bodies) may use emissive masks; EmissiveStrength must be between 0 and 40 to pass validation. 2D clothing and makeup do not support emissive yet; IEC emissive is not supported at launch. *(doc, high; avatar-ugc-accessories)*
- c11: Doc warns against tuning material values to look right in one lighting setup; base values on physical properties. *(opinion, medium; mesh-texture-limits)*
- c12: Blender and Maya texture connection settings for Studio import are on a separate page (assign-textures.md), not covered here. *(doc, high; other)*

## Numbers
- n1: **Supported PBR map types**: 5 color, normal, roughness, metalness, emissive mask
- n2: **MeshPart.Transparency for soft transparency**: at least 0.02 Transparency AlphaMode with semi-transparent detail
- n3: **MeshPart.Transparency for hard cutouts**: 0 foliage, lace, netting in Transparency AlphaMode
- n4: **Flat normal map RGB**: [127,127,255] uniform color equals completely flat normal
- n5: **Roughness compensation**: +0.1 suggested increase when unexpected specular appears at angles
- n6: **EmissiveStrength marketplace range**: 0 to 40 required to pass Marketplace validation
- n7: **Emissive tint example**: [255,0,255] magenta EmissiveTint example

## Techniques
- t1: **Hard-edged alpha cutout**: Use Transparency AlphaMode with an alpha-channel color map and set MeshPart.Transparency to 0 so depth occlusion works, instead of sculpting extra geometry.
- t2: **Tint mask for selective color**: Set AlphaMode to TintMask. Keep color in transparent areas and turn off premultiplied alpha. Tinting applies where alpha is opaque, not in grout-like transparent areas.
- t3: **Custom skin tone via Overlay**: Make transparent regions of the color map in Overlay mode so the MeshPart.Color shows through, letting one map serve several skin tones.
- t4: **Emissive mask glow**: Use a grayscale EmissiveMaskContent to control glow per area, then tune EmissiveStrength and EmissiveTint instead of the all-or-nothing Neon material.

## Quotes (brief, for attribution)
> In general, you can't modify SurfaceAppearance properties by scripts during a game because the engine requires some pre-processing to display these graphics.  (create.roblox.com)
> Roblox only supports OpenGL format - Tangent Space normal maps.  (create.roblox.com)
> Studio only uses the metalness workflow which determines whether a material is a nonmetal or a metal.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/modeling/assign-textures
- https://create.roblox.com/docs/art/modeling/material-reference
- https://create.roblox.com/docs/art/modeling/texture-specifications
- https://create.roblox.com/docs/avatar/character-bodies/specifications
