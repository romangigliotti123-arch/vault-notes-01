---
type: research-source
id: web-72fcac2436
title: "how to use blenders new ultimate shader principled bsdf"
source_type: "web"
creator: "www.blenderguru.com"
url: "https://www.blenderguru.com/posts/2017/6/21/how-to-use-blenders-new-ultimate-shader-principled-bsdf"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 1
density: low
tags: ["research-source", "web", "mesh-texture-limits", "other"]
---
# web-72fcac2436

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Andrew Price's 2017 BlenderGuru post introduces the Principled BSDF in Blender 2.79 as a single slider-based shader covering multiple shader types, with auto-realistic roughness/fresnel. It shows connecting it to a texture set (Poliigon or Substance export). Text is thin; diagrams and advanced section are images. Little relevance to Claude, bpy, or Roblox pipeline.

## Claims
- c1: Source is a 2017 Blender 2.79 shader tutorial on the Principled BSDF; it does not mention Claude, blender-mcp, bpy scripting, Roblox, or FBX/glTF export. *(doc, high; other)*
- c2: Author claims the Principled BSDF replaces multiple shader types with simple sliders and gives consistent results across apps like Substance to Blender; this is opinion/marketing-tinged. *(opinion, medium; other)*
- c3: Principled BSDF is connected to a texture set (e.g., Poliigon or Substance Painter export) for PBR-style material setup; the connection diagram is image-only, so exact socket mapping is not in the text. *(doc, medium; mesh-texture-limits)*

## Numbers
- n1: **Blender version**: 2.79 
- n2: **Publication date**: 2017-06-21 (listed Jun 22) 

## Techniques
- t1: **Principled BSDF with texture set**: Add Principled BSDF node; connect texture maps (e.g., from Poliigon or Substance Painter export) to its inputs. Exact connections shown only in images.

## Quotes (brief, for attribution)
> In fact, it's likely that 95% of all your future materials will be made using the Principled BSDF, because it's so powerful!  (www.blenderguru.com)

## Points to
- https://www.blenderguru.com/posts/2017/6/21/how-to-use-blenders-new-ultimate-shader-principled-bsdf
- Poliigon
- Substance Painter
