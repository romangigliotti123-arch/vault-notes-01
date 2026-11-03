---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-BLENDERKIT_GUIDE.md
title: "sandraschi/blender-mcp/docs/blender/BLENDERKIT_GUIDE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/BLENDERKIT_GUIDE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0394
relevance: 1
density: low
tags: ["research-source", "github", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-BLENDERKIT_GUIDE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
A BlenderKit add-on guide inside the sandraschi/blender-mcp repo. It covers installing BlenderKit and downloading assets, then shows one example of calling the repo's MCP tools (blender_transform, blender_materials, etc.) on an imported asset. It has nothing on Roblox, FBX export settings, or Roblox limits. It also contains questionable claims (e.g. BlenderKit "created by the Blender Foundation").

## Claims
- c1: The guide proposes a hybrid workflow: use the BlenderKit add-on to browse and import assets, then drive follow-up operations (transform, materials, lighting, camera, animation) through the repo's Blender MCP tools. *(doc, medium; claude-blender-ai)*
- c2: The repo's MCP tools are grouped by domain, called with an operation argument: blender_transform, blender_materials, blender_lighting, blender_camera, blender_animation. Example operations: move_object, scale_object, create_pbr_material, setup_three_point_lighting, create_camera, create_rotation_animation. *(doc, medium; claude-blender-ai)*
- c3: BlenderKit lists supported model formats .blend, .fbx, .obj, .dae, .abc. FBX is the one relevant to Roblox, but the guide gives no Roblox-specific export settings. *(doc, low; blender-roblox-export-import)*
- c4: The upload checklist for BlenderKit asks for no Ngons, complete non-overlapping UVs, PBR materials, and real-world scale. These are BlenderKit rules, not Roblox rules. *(doc, medium; mesh-texture-limits)*
- c5: The guide claims BlenderKit was created by the Blender Foundation. This is doubtful, since BlenderKit is a separate third-party service. It also uses the domain 'blendkit.com', which looks like a typo. Treat the document's accuracy with caution; it reads as auto-generated. *(opinion, low; other)*

## Numbers
- n1: **BlenderKit model file size**: <50MB preferred, <200MB max BlenderKit upload guidance, not Roblox limits
- n2: **BlenderKit texture size per material**: <20MB recommended BlenderKit guideline
- n3: **Blender version**: 3.0+ recommended, 2.8+ minimum BlenderKit add-on requirement

## Techniques
- t1: **BlenderKit import then MCP post-processing**: Install the BlenderKit add-on and log in. Search and download an asset, which imports with its materials. Then call the MCP tools to position, scale, re-material, light, camera and animate it.

### Code: MCP tool calls on an imported BlenderKit asset (repo's tool API)
```python
blender_transform(operation="move_object", name="Katana", location=[0, 0, 1])
blender_transform(operation="scale_object", name="Katana", scale=[1.2, 1.2, 1.2])
blender_materials(
    operation="create_pbr_material", name="DamascusSteel", base_color=[0.3, 0.3, 0.35], metallic=1.0, roughness=0.2
)
blender_lighting(operation="setup_three_point_lighting")
blender_camera(operation="create_camera", camera_name="HeroCam", location=[3, -3, 2], target_location=[0, 0, 1])
blender_animation(operation="create_rotation_animation", object_name="Katana", duration=120)
```

## Contradictions flagged
- The guide says BlenderKit was created by the Blender Foundation and is the 'official' library. (vs BlenderKit is a separate third-party service and add-on, not made by the Blender Foundation (my own knowledge, not from the source).)

## Points to
- https://github.com/sandraschi/blender-mcp
- BlenderKit add-on
