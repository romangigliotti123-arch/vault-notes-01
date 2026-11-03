---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-scene.md
title: "ahujasid/mcp-for-blender/src/blender_mcp/guides/scene.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/src/blender_mcp/guides/scene.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 3
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation"]
---
# gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-scene.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Scene-design guide from the blender-mcp repo for Claude-driven Blender work. Covers blockout-first workflow, which asset source to use (generate_3d, Poly Haven, Sketchfab, Poly Pizza, scripted geometry), fixing scale/ground/facing after import, composition, HDRI-plus-key lighting, and camera focal lengths. Little on Roblox export specifically.

## Claims
- c1: Recommended agent workflow: get_scene_info first, block out with primitives at real-world size, check with look(mode="camera") or look(mode="angles") before spending on assets, then replace blockout pieces biggest-first. *(doc, high; claude-blender-mcp)*
- c2: generate_3d should be used for one hero object per call, never whole scenes, ground, or parts to assemble; duplicate generated objects with obj.copy() for repeats. *(doc, high; claude-blender-mcp)*
- c3: search_assets(source="polyhaven") supplies HDRIs and PBR textures for large surfaces plus generic props, CC0 licensed. *(doc, high; claude-blender-mcp)*
- c4: Sketchfab for specific real-world objects; check licence and face count. Poly Pizza for stylised low-poly props; credit CC-BY creators. Do not mix low-poly and photoreal assets in one frame. *(doc, high; claude-blender-mcp)*
- c5: Script geometry only for simple or procedural pieces (walls, floors, shelves, stairs, fences, arrays, scattering). *(doc, high; procedural-generation)*
- c6: Imported and generated models arrive at arbitrary scale, rotation and origin; scale from world_bounding_box rather than by eye, then drop to ground with obj.location.z -= min_z. *(doc, high; common-mistakes-fixes)*
- c7: Generators usually face -Y or +Y; rotate to correct facing and check with look(mode="angles", target=[name]); check for intersections with neighbours. *(doc, medium; common-mistakes-fixes)*
- c8: Camera focal length guidance: 35–50 mm natural views, 85 mm+ product shots, 24 mm or wider for interiors. *(doc, high; creator-workflows)*
- c9: Lighting: HDRI from Poly Haven for ambient light and reflections with strength 0.5–1.5, then add sun or area key light; three-point for products; interiors use area lights in windows (portals in Cycles) plus emissive practicals. *(doc, high; creator-workflows)*
- c10: Blown-out white or pure black areas indicate light power is off; fix light power before changing exposure. Verify with look(mode="camera", shading="rendered"). *(doc, high; common-mistakes-fixes)*
- c11: Render settings: read the current engine first (get_guide("bpy")); keep samples low for previews and raise only for final render. *(doc, medium; creator-workflows)*
- c12: Composition: vary scale and rotation of repeated props slightly since perfect grids look fake; props should sit on surfaces; leave negative space; rule of thirds. *(doc, medium; creator-workflows)*

## Numbers
- n1: **HDRI strength**: 0.5–1.5 Poly Haven HDRI ambient light strength before adding key light
- n2: **focal length**: 35–50 mm natural; 85 mm+ product; 24 mm or wider interiors camera guidance for scene composition

## Techniques
- t1: **Blockout then replace**: Place primitives at real-world size, check with look() views, then swap in generated or library assets biggest-first; light, material, then small props.
- t2: **Bounding-box fit**: Read world_bounding_box from import result, scale to real size, subtract min z from location.z to ground, rotate to face, check neighbour intersections.

### Code: Ground an imported model using its bounding box min z
```python
obj.location.z -= min_z
```

### Code: Duplicate a generated object instead of regenerating
```python
obj.copy()
```

## Quotes (brief, for attribution)
> One object per generation — never a whole scene, the ground, or parts to assemble.  (ahujasid)
> Blown-out white or pure black areas mean exposure or light power is off; fix light power before touching exposure.  (ahujasid)

## Points to
- get_guide("bpy")
- Poly Haven
- Sketchfab
- Poly Pizza
