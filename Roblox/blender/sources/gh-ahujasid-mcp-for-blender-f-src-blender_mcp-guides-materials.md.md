---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-materials.md
title: "ahujasid/mcp-for-blender/src/blender_mcp/guides/materials.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/src/blender_mcp/guides/materials.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "procedural-generation", "texturing-baking-uv"]
---
# gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-materials.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Guide from the blender-mcp project on materials and texturing via bpy and MCP tools: node-based Principled BSDF setup, believable PBR value ranges, Poly Haven import, UV-based tiling math, Non-Color maps, procedural noise looks, and checking materials in Material Preview. Not Roblox-specific; useful for the texturing step before export.

## Claims
- c1: Tiling rule: Mapping node Scale = surface size in metres / texture size in metres, for 0-1 UVs across a surface. *(doc, high; texturing-baking-uv)*
- c2: Image textures for roughness, metallic and normal maps must be set to Non-Color colourspace. *(doc, high; texturing-baking-uv)*
- c3: Scripted meshes without UVs need smart_project or box projection (Texture Coordinate > Object into Mapping, Image Texture projection BOX). *(doc, high; texturing-baking-uv)*
- c4: import_asset(source='polyhaven', id=..., apply_to=[...]) builds and applies a full PBR material in one call. *(doc, high; claude-blender-mcp)*
- c5: Material colours only display in Material Preview or Rendered shading; use look(mode='camera', shading='material') or shading='rendered'. Solid shows only viewport display colour. *(doc, high; claude-blender-mcp)*
- c6: mat.use_nodes = True is a no-op in Blender 5.0+ where node trees are always on. *(doc, high; bpy-scripting-headless)*
- c7: Principled BSDF socket names changed in 4.0, so inputs should be resolved defensively, e.g. inputs.get('Emission Color') or inputs.get('Emission'). *(doc, high; bpy-scripting-headless)*
- c8: Base colours should stay roughly between 0.02 and 0.9 linear; pure black or white is unrealistic. *(doc, medium; common-mistakes-fixes)*
- c9: Recommended PBR starting values: polished metal base 0.9, metallic 1, roughness 0.05-0.2; rubber base 0.02-0.05, roughness 0.8; painted wall roughness 0.8-0.9. *(doc, medium; texturing-baking-uv)*
- c10: Glass: metallic 0, roughness 0, Transmission 1, IOR 1.45. *(doc, medium; texturing-baking-uv)*
- c11: Prefer large-coverage textures (min_size_m search filter) for walls and floors; small textures repeat visibly. *(doc, medium; texturing-baking-uv)*
- c12: Noise, Voronoi and Wave textures through a Color Ramp add variation without images; mixing noise into roughness reduces flat CG look. *(opinion, medium; procedural-generation)*
- c13: Material assignment pattern: obj.data.materials.clear() then obj.data.materials.append(mat). *(doc, high; bpy-scripting-headless)*
- c14: Look up each node before indexing its sockets to avoid errors from missing or renamed nodes. *(doc, low; common-mistakes-fixes)*

## Numbers
- n1: **Polished metal base colour / metallic / roughness**: 0.9 / 1 / 0.05-0.2 Believable PBR starting values table
- n2: **Glass IOR**: 1.45 Transmission 1, roughness 0
- n3: **Base colour range**: ~0.02 to ~0.9 linear Nothing in nature is pure 0 or 1
- n4: **Painted wall base / roughness**: 0.5-0.7 grey / 0.8-0.9 Metallic 0
- n5: **Rubber base / roughness**: 0.02-0.05 / 0.8 Metallic 0
- n6: **Socket rename version**: Blender 4.0 Principled BSDF inputs renamed
- n7: **use_nodes behaviour**: no-op in 5.0+ Node trees always on

## Techniques
- t1: **Principled BSDF material setup**: Create bpy.data.materials.new, set use_nodes, find BSDF_PRINCIPLED node by type, set Base Color, Metallic, Roughness defaults, clear and append to obj.data.materials.
- t2: **Box projection for UV-less meshes**: Add Texture Coordinate > Object into Mapping node; set Image Texture projection to BOX.
- t3: **Real-world tiling scale**: Mapping Scale = surface size (m) / texture size (m) for 0-1 UVs.
- t4: **Procedural variation**: Noise, Voronoi or Wave texture through Color Ramp for grunge, stains, wood rings; blend noise into roughness.

### Code: Create Principled BSDF material and assign to object
```python
mat = bpy.data.materials.new("Brushed Steel")
mat.use_nodes = True   # no-op in 5.0+, where it's always on
bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
bsdf.inputs["Base Color"].default_value = (0.6, 0.6, 0.62, 1)
bsdf.inputs["Metallic"].default_value = 1.0
bsdf.inputs["Roughness"].default_value = 0.35
obj.data.materials.clear(); obj.data.materials.append(mat)
```

### Code: Defensive socket lookup across Blender versions
```python
inputs.get("Emission Color") or inputs.get("Emission")
```

## Quotes (brief, for attribution)
> Image textures for roughness, metallic and normal maps must be Non-Color  (ahujasid)
> Material colours only show in Material Preview or Rendered shading  (ahujasid)

## Points to
- Poly Haven (import_asset source='polyhaven')
- get_guide('bpy')
- look() tool with mode='camera' and shading options
