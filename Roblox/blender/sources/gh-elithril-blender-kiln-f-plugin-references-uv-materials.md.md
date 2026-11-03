---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-uv-materials.md
title: "elithril/blender-kiln/plugin/references/uv-materials.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/uv-materials.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 2
density: high
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-uv-materials.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Reference for UV unwrapping, texel density, PBR metallic/roughness setup and texture resolution, written for a glTF-focused Blender plugin (blender-kiln). Includes a bpy smart_project unwrap and a Principled BSDF material helper. Roblox is not mentioned, so Roblox-specific limits must come from other sources.

## Claims
- c1: Texel density targets: Mobile/Web 5.12-10.24 px/cm at 1K-2K; Console/PC 10.24-20.48 px/cm at 2K-4K; Cinematic 20.48+ px/cm at 4K+. *(doc, medium; mesh-texture-limits)*
- c2: UV packing: island margin 4-8 px for 2K textures, 8-16 px for 4K; target UV utilization above 85%; textures should be power of 2. *(doc, medium; mesh-texture-limits)*
- c3: Single UV (0-1) is the default for real-time; UDIM is not supported by glTF and is only for film/hero assets. *(doc, medium; mesh-texture-limits)*
- c4: Seams should go in hidden areas (under arms, inner legs, behind ears) and never mid visible flat surfaces; for hard surfaces, seams should coincide with sharp edges. *(opinion, medium; mesh-texture-limits)*
- c5: Metallic/Roughness is the standard workflow, not Specular/Glossiness; Base Color carries no baked lighting; Normal maps are tangent space and set to Non-Color. *(doc, medium; mesh-texture-limits)*
- c6: ORM packing puts AO in R, Roughness in G, Metallic in B in one texture; described as standard for glTF and Unreal Engine. *(doc, medium; mesh-texture-limits)*
- c7: Emissive values above 1.0 trigger bloom in glTF. *(doc, medium; mesh-texture-limits)*
- c8: Suggested texture sizes: Web Base Color/Normal 512-1024, ORM 512; Mobile 1024 base/normal; Console/PC base/normal 2048-4096, ORM 1024-2048; Film 4096-8192. *(doc, medium; mesh-texture-limits)*
- c9: Web format advice: JPEG for Base Color (lossy OK), PNG for Normal maps (lossless), KTX2/Basis for everything, WebP as intermediate. *(opinion, low; mesh-texture-limits)*
- c10: Common material presets, e.g. oak wood base (0.45,0.28,0.14) metallic 0 roughness 0.6-0.8; steel (0.55,0.55,0.55) metallic 1.0 roughness 0.3-0.5; glass roughness 0.0-0.1. *(doc, medium; mesh-texture-limits)*
- c11: Auto unwrap via bpy.ops.uv.smart_project with angle_limit=66.0, island_margin=0.02, area_weight=0.0, correct_aspect and scale_to_bounds enabled, run from edit mode. *(doc, medium; automation-and-creator-workflows)*
- c12: Helper create_pbr_material(name, ...) builds a Principled BSDF node tree from albedo, normal, and roughness image paths using bpy.data.images.load and ShaderNodeNormalMap. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **Texel density (Mobile/Web)**: 5.12-10.24 px/cm Textures 1K-2K
- n2: **Texel density (Console/PC)**: 10.24-20.48 px/cm Textures 2K-4K
- n3: **Texel density (Cinematic)**: 20.48+ px/cm Textures 4K+
- n4: **UV island margin**: 4-8 px (2K), 8-16 px (4K) Padding between UV islands
- n5: **UV space utilization target**: >85% Packing goal
- n6: **Smart project angle_limit**: 66.0 degrees bpy.ops.uv.smart_project default in snippet
- n7: **Smart project island_margin**: 0.02 Normalized UV margin in snippet
- n8: **Console/PC base color/normal size**: 2048-4096 Per-use-case table
- n9: **Web base color/normal size**: 512-1024 Per-use-case table
- n10: **Film base color/normal size**: 4096-8192 Per-use-case table

## Techniques
- t1: **ORM channel packing**: Store AO in R, Roughness in G, Metallic in B of one texture to cut texture count; standard for glTF and Unreal per source.
- t2: **Uniform texel density**: Pick a platform density band (px/cm), derive texture size per asset, and keep density consistent across all UV islands.
- t3: **Seam placement in hidden areas**: Cut seams at clothing junctions, material changes or hard-surface sharp edges; avoid visible flat faces.
- t4: **Scripted smart UV project**: In object mode, set active object, enter edit mode, select all, call uv.smart_project with listed params, return to object mode.

### Code: Quick automatic UV unwrap via smart projection in Blender bpy
```python
import bpy

obj = bpy.context.active_object
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.smart_project(
    angle_limit=66.0,      # degrees
    island_margin=0.02,    # margin between islands
    area_weight=0.0,
    correct_aspect=True,
    scale_to_bounds=True,
)
bpy.ops.object.mode_set(mode='OBJECT')
```

### Code: Build a Principled BSDF material with optional base color, normal and roughness textures
```python
def create_pbr_material(name, albedo_path=None, normal_path=None, 
                         roughness_path=None, metallic=0.0, roughness=0.5,
                         base_color=(0.8, 0.8, 0.8, 1.0)):
    mat = bpy.data.materials.new(name=name)
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    bsdf = nodes.get("Principled BSDF")
    
    if albedo_path:
        tex = nodes.new("ShaderNodeTexImage")
        tex.image = bpy.data.images.load(albedo_path)
        links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
```

## Quotes (brief, for attribution)
> Single UV (0-1) default for blender-kiln; UDIM only if single UV insufficient.  (elithril)
> Emissive values > 1.0 trigger bloom in glTF.  (elithril)

## Contradictions flagged
- ORM packing (R=AO, G=Roughness, B=Metallic) is standard for glTF and Unreal Engine. (vs Roblox SurfaceAppearance takes separate PBR maps; source does not address Roblox, so Roblox packing is unverified here.)

## Points to
- https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/uv-materials.md
