---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-SKILL.md
title: "elithril/blender-kiln/plugin/SKILL.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/SKILL.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.1276
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "rigging-animation", "roblox-export-settings"]
---
# gh-elithril-blender-kiln-f-plugin-SKILL.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
A Claude skill (blender-kiln) that drives Blender through blender-mcp (ahujasid 2.0.0 or the official Blender Lab MCP) with a 26-rule pipeline. It covers the MCP tool surface, how disabled integrations fail, geometry-nodes export, glTF/FBX export rules, cleanup and merge order, rig density, and headless fallback. It targets glTF, web and AR, not Roblox, so Roblox-specific content is absent.

## Claims
- c1: blender-mcp 2.0.0 (bundled addon 1.7) exposes 36 tools, including execute_blender_code, get_object_info, get_viewport_screenshot, export_scene, bpy_api_lookup and describe_node_type. The raw addon socket uses different names (execute_code). *(doc, high; claude-blender-mcp)*
- c2: A disabled integration (PolyHaven, Sketchfab, etc.) unregisters its commands, so calling one returns 'Unknown command type', which looks like a version bug. Call the always-registered get_*_status tools first; they carry the remediation text. *(experience, high; claude-blender-mcp)*
- c3: Ticking an integration checkbox takes effect immediately, because the flags are scene properties read at dispatch time. The addon's 'restart the connection' advice is unnecessary. *(experience, medium; claude-blender-mcp)*
- c4: get_scene_info returns object names and counts only, with no dimensions. Use get_object_info(name) for world_bounding_box to verify 1 unit = 1 m. *(doc, high; claude-blender-mcp)*
- c5: An outdated addon is missing commands such as get_addon_info. Fix it with `uvx blender-mcp install-addon` and re-enable the addon. addon_utils.enable() leaves property groups incomplete. *(doc, medium; claude-blender-mcp)*
- c6: The official Blender Lab MCP uses different tool names (get_objects_summary, get_object_detail_summary, get_screenshot_of_area_as_image, jump_to_view3d_object_by_name, search_api_docs). It has no marketplace or generation tools. Its add-on needs Blender 5.1+ and online access enabled. *(doc, high; claude-blender-mcp)*
- c7: Its package is also named blender-mcp, so `uvx blender-mcp` starts ahujasid's server. Run the Lab one from git and register it under the MCP name 'blender'. The bench measured the same 7 GLBs for 10% less cost on the Lab server. *(data, medium; claude-blender-mcp)*
- c8: Sessions tend to under-screenshot: on the Lab server, one screenshot per session on 4 of 5 briefs. Frame the viewport on the subject first, or a small prop renders as a few pixels and looks deleted. *(data, medium; claude-blender-mcp)*
- c9: If MCP export times out, fall back to `blender --background scene.blend --python-exit-code 1 --python-expr ...`. Without --python-exit-code 1 a failed export still exits 0. *(experience, high; bpy-scripting-headless)*
- c10: Look bpy APIs and node sockets up in the running Blender (bpy_api_lookup, describe_node_type) rather than recalling them, because the API changes every release. The animation paths need Blender 4.4+ (layered actions, channelbag()). *(doc, medium; bpy-scripting-headless)*
- c11: Geometry nodes output exists only as a modifier result. Exporting with export_apply=False wrote 2 tris instead of 2,688. Apply the modifier (modifier_apply) before export, with Realize Instances at the end of the tree. Keep the .blend with the live modifier. *(data, high; procedural-generation)*
- c12: Simulation Zone gotchas: Group Input values do not propagate into sim zones, geometry freezes after frame 1, and a Set Position is required after the sim zone output. *(experience, medium; procedural-generation)*
- c13: AI 3D generation is optional. TRELLIS.2 (MIT) Space is first choice, then TRELLIS, then TripoSR. Hunyuan3D's licence excludes the EU, UK and South Korea. Rodin and Tripo native are paid. Scripting is recommended for low-poly or geometric forms, AI for organic ones. *(doc, medium; procedural-generation)*
- c14: Merge-by-distance order: apply transforms, merge doubles keeping each corner's normal, then recalc normals. A plain merge on a faceted mesh bent 94.5% of corners over 5° (from 26.7%). Merging before applying a scale of 100 deleted 108 of 928 faces. *(data, high; common-mistakes-fixes)*
- c15: Procedural shader nodes (Noise, Voronoi, Color Ramp) are silently lost in glTF export. Audit materials before export and bake or warn. *(experience, high; common-mistakes-fixes)*
- c16: FBX export rules: Apply Transform, scale 1.0, version 7.4. Blender -Y/Z converts to glTF +Z/Y automatically. Never use export_apply=True for glTF, since Array/Mirror modifiers balloon file size. *(doc, medium; roblox-export-settings)*
- c17: Never use `gltf-transform optimize`, because its simplify step destroys geometry. Use individual steps: resize, webp, draco. Default web texture cap is 1024, and Draco needs a client decoder. *(experience, medium; creator-workflows)*
- c18: Count vertices per deform bone after welding and aim for 20 or more. A Rigify human (160 bones) on a 370-vertex mesh left 107 bones influencing nothing and detached the head. Tiers: under 700 verts hand-built 12-20 bones; 700-3000 basic human (35 bones); over 3000 full human. *(data, high; rigging-animation)*
- c19: Rigify limbs ship in IK, so FK controls do nothing until switched, with no error. Marketplace characters rarely arrive in T-pose: three free models measured A-pose at -27° and -28° and I-pose at -71°. Measure shoulder-to-hand angle, not a horizontal slice. *(data, medium; rigging-animation)*
- c20: Thin parts (wires, loops) break under decimation, so rebuild them as beveled curves and decimate only the body. After decimating, compare open and non-manifold edge counts and view close renders. *(experience, medium; common-mistakes-fixes)*
- c21: Rename imported assets to a convention such as SM_PascalCase (with the mesh data-block renamed too) in the import step, whatever the source. Keep the .blend as the recovery point. *(opinion, low; creator-workflows)*

## Numbers
- n1: **blender-mcp tool count**: 36 (server 2.0.0, addon 1.7) extracted 2026-09-29
- n2: **GN scatter export triangles**: 2 tris (export_apply=False) vs 2,688 (modifier applied) 208.7 kB when applied first
- n3: **corners bent >5° after plain merge**: 26.7% to 94.5% faceted low-poly mesh
- n4: **min verts per deform bone**: ~20 370-vertex figure on Rigify gave 2.3
- n5: **Rigify deform bones**: 35 basic human, 160 full human, 46 quadruped Blender 5.0.1
- n6: **Blender Lab MCP minimum Blender**: 5.1.0 kiln's own floor is 4.4
- n7: **default glTF texture cap**: 1024 px 2048 only for close-ups or PC/console
- n8: **faces lost by merging before applying scale 100**: 108 of 928 merge-order bug

## Techniques
- t1: **Preflight integration status**: Call get_addon_status (check up_to_date), then get_polyhaven_status, get_sketchfab_status or get_polypizza_status before any search or generation. Show the message field instead of the raw 'Unknown command type'.
- t2: **Frame then screenshot**: Select the object, then view3d.view_selected inside temp_override(area, region), then get_viewport_screenshot. Take two opposite angles after texturing.
- t3: **Apply geometry nodes before glTF export**: Add Realize Instances at the end of the tree. Save the .blend, then bpy.ops.object.modifier_apply(modifier='GN'), then export with export_apply=False.
- t4: **Headless export fallback**: Run blender --background scene.blend --python-exit-code 1 --python-expr '...' so failures return a nonzero exit code.
- t5: **Safe cleanup order**: Apply transforms, merge by distance while keeping corner normals, recalc normals, then rig and export. Verify dimensions via get_object_info world_bounding_box.
- t6: **Detect dead deform bones**: After skinning, count vertex groups where no vertex has weight above 0.01. Any dead bone means the rig is too dense for the mesh, so go down a tier.
- t7: **Measure T-pose**: Compute atan2 from the shoulder to the farthest hand vertex. Within ±15° is T-pose, -15 to -45° is A-pose, below -45° is I-pose. Wingspan roughly equals height in a T-pose.
- t8: **Texture compress chain**: Resize textures, convert to WebP, then Draco, as separate gltf-transform steps. Never use the combined optimize command.

### Code: Frame the viewport on the selected object before a screenshot
```python
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for region in area.regions:
            if region.type == 'WINDOW':
                with bpy.context.temp_override(area=area, region=region):
                    bpy.ops.view3d.view_selected()
```

### Code: Apply geometry nodes modifier before export
```python
bpy.ops.object.modifier_apply(modifier="GN")   # procedural becomes geometry
```

### Code: Count dead deform bones after skinning
```python
dead = sum(1 for vg in mesh.vertex_groups
           if not any(g.group == vg.index and g.weight > 0.01
                      for v in mesh.data.vertices for g in v.groups))
```

## Contradictions flagged
- Enabling an integration checkbox needs no reconnect. (vs The addon's own remediation text says to restart the connection to Claude.)
- Geometry nodes assets must have the modifier applied before export. (vs Its own rule 18, which forbids baking modifiers on export, so the rule carries an exception.)

## Points to
- ahujasid/blender-mcp
- projects.blender.org/lab/blender_mcp
- gltf-transform
- gltfpack
- Poly Haven
- Sketchfab
- microsoft/TRELLIS.2
- Hunyuan3D
