---
type: research-source
id: gh-elithril-blender-kiln-readme
title: "elithril/blender-kiln README: Claude Code plugin that turns a text brief or a photo into a production-ready 3D asset through Blender: rebuil"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0969
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "rigging-animation", "roblox-export-settings", "roblox-mesh-limits", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README of blender-kiln, a Claude Code plugin/skill driving Blender via MCP (ahujasid blender-mcp or official Blender Lab MCP) to produce optimized GLBs from briefs or photos. Targets web/GLB, not Roblox, but covers MCP setup gotchas, headless bpy scripting, cleanup/poly rules, texturing, optimization, rigging checks, and Blender 4.4+/5.x API drift relevant to Claude+Blender workflows.

## Claims
- c1: Blender MCP addon integrations (PolyHaven, Sketchfab, Hunyuan3D, Hyper3D) ship off; while off, commands aren't registered, so calls return 'Unknown command type: search_polyhaven_assets', which looks like a version mismatch. *(doc, high; claude-blender-mcp)*
- c2: get_*_status commands (polyhaven, sketchfab, hunyuan3d, hyper3d) are always registered and return fix steps; check them before searching. Enable boxes in BlenderMCP sidebar panel (N key), then reconnect. *(doc, high; claude-blender-mcp)*
- c3: Skill works with both ahujasid's mcp-for-blender (addon on port 9876, installed via `uvx blender-mcp install-addon`) and the Blender Foundation's official Blender Lab MCP, which backs Claude's Blender connector. *(doc, high; claude-blender-mcp)*
- c4: MCP-driven and headless scripted passes produced byte-identical results: 111.9 kB GLB, 2,202 triangles, three materials. *(data, medium; claude-blender-mcp)*
- c5: Core loop rules: get_scene_info() before each phase, get_viewport_screenshot() after geometry/material changes (two angles after texturing), frame viewport before screenshot or scene looks empty, confirm before destructive actions. *(doc, high; claude-blender-mcp)*
- c6: Blender 4.4 is a hard floor: layered actions arrived in 4.4, animation code uses action.layers[].strips[].channelbag(), absent on 4.0-4.3. Verified on 5.0 locally and 5.2 LTS in CI; 4.4-4.5 untested. *(doc, high; bpy-scripting-headless)*
- c7: A weekly CI check found Material.use_nodes deprecated, slated for removal in Blender 6.0; CI fails on any DeprecationWarning reached by docs, guarding against API drift in Claude-written bpy. *(doc, high; bpy-scripting-headless)*
- c8: Gallery of 15 props was built headless with `blender --background --python` scripts; this exercises scripted modelling only, not the interactive MCP loop. *(doc, high; bpy-scripting-headless)*
- c9: Geometry nodes modifiers must be applied before export, and rule 18 says never use export_apply=True for glTF because modifiers balloon file size (as reported by the README). *(doc, medium; bpy-scripting-headless)*
- c10: Cleanup phase: merge doubles, recalc normals, apply transforms, check poly budget, verify scale 1 unit = 1 m, centre origin; object sits on Z=0. Welding must preserve faceted shading, otherwise split-edge meshes tear at first pose. *(doc, medium; common-mistakes-fixes)*
- c11: Procedural shader nodes are lost on glTF export; a material export audit detects them and bakes procedural to textures before export (rule 19). *(doc, high; common-mistakes-fixes)*
- c12: Size is assumed when a brief gives none: a generated chair came out 29% short of ordinary chair height, so state real size explicitly. *(data, medium; common-mistakes-fixes)*
- c13: Scripted modelling in Blender Python is the default; AI generation optional. HF Space status Oct 2026: TRELLIS.2 and trellis-community running, TripoSR RUNTIME_ERROR, Hunyuan3D-2 Space shape works but texture fails server-side. *(doc, medium; procedural-generation)*
- c14: Free HF ZeroGPU quota is 2 min without account, 3.5 min with a free one; a generation needs 60-120 s, so roughly 1-2 generations a day. Hunyuan3D licence excludes EU, UK, South Korea. *(doc, high; procedural-generation)*
- c15: Generated meshes were used only as measured proportion templates (template_profile.py), never shipped; photo rebuilds textured from Poly Haven CC0 scans and scored against real asset silhouettes. *(doc, medium; procedural-generation)*
- c16: Texturing strategy: Poly Haven CC0 PBR sets chosen against reference, tinted to palette, baked to UVs; procedural only when no scan fits. *(doc, medium; texturing-baking-uv)*
- c17: Rule 26: do not choose a Rigify rig without measuring vertices divided by deform bones; a Rigify human needs about 3,200 vertices to be worth it. Poly count alerts but is never hard-capped. *(doc, medium; roblox-mesh-limits)*
- c18: Character rigging: T-pose, skeleton sized to mesh with joints at bends, weights checked on a bent pose, Blender 5.x bone collections. UniMate text-to-motion measured unusable for quadruped walking; its checkpoints are CC BY-NC 4.0. *(doc, medium; rigging-animation)*
- c19: Optimisation via gltf-transform (resize, WebP, Draco) and gltfpack (simplify, LOD) cut five text-brief outputs from 32.9 MB to 0.96 MB (ahujasid MCP) and 3.9 MB to 0.75 MB (Lab MCP). Do not use `gltf-transform optimize`; run individual steps (rule 20). *(data, medium; creator-workflows)*
- c20: Photo-to-asset method: inventory parts from enlarged crops, texture from scans, render model at photo camera to measure silhouette gaps, render every joint, re-measure the shipped GLB. Shape scores improved lantern 0.830 to 0.897, ammo box 0.854 to 0.950, chair 0.445 to 0.750. *(data, medium; creator-workflows)*
- c21: Batch mode: wizard builds YAML manifest, runner executes autonomously; between assets clear scene by removing datablocks, not read_homefile() (rule 30). *(doc, medium; creator-workflows)*
- c22: Exports GLB/FBX/USDZ with 8-point validation checklist; Blender exports USDZ natively. No Roblox-specific settings are given; output is aimed at web (Three.js/Babylon.js). *(doc, medium; roblox-export-settings)*

## Numbers
- n1: **MCP addon port**: 9876 Blender MCP addon listening port
- n2: **Minimum Blender version**: 4.4 (verified 5.0, 5.2 LTS) Layered actions API required
- n3: **Cost per photo rebuild**: $3.80-$6.13 Opus 5.5, one run each
- n4: **Shipped GLB sizes (photo rebuilds)**: 187-239 KB After Draco/WebP
- n5: **Final GLBs compressed**: 7 of 7 from 0 of 7 Both MCP servers
- n6: **FLUX.1-schnell concept art speed**: 5.6 s per image HF Space, Apache-2.0
- n7: **Barrel test triangles**: 2,202 SM_Barrel, 111.9 kB GLB
- n8: **Rigify human worthwhile vertex count**: ~3,200 Rule 26

## Techniques
- t1: **Check MCP integration status first**: Call get_polyhaven_status / get_sketchfab_status / get_hunyuan3d_status / get_hyper3d_status; enable integrations in the BlenderMCP sidebar panel, add the Sketchfab API key, reconnect, then search.
- t2: **Install ahujasid addon**: Run `uvx blender-mcp install-addon`, enable in Blender, start server on port 9876, then run /kiln setup to detect Blender, MCP and optional tools.
- t3: **Photo-to-asset fidelity loop**: Inventory parts from crops, state size and camera, texture from CC0 scans, render at the photo camera with fidelity_check.py for silhouette gaps, render each joint, re-measure the final GLB.
- t4: **Optimize GLB with individual steps**: Use gltf-transform resize, WebP and Draco separately, optionally gltfpack for simplify/LOD, then run Khronos validator; keep the uncompressed _original.glb and .blend.
- t5: **Verify bpy API weekly in CI**: Scheduled CI runs Blender headless, checks documented bpy API and Principled sockets still exist, and fails on DeprecationWarning.

## Quotes (brief, for attribution)
> Blender MCP servers give an agent hands in Blender; kiln gives it the production method on top.  (elithril)

## Contradictions flagged
- Blender MCP's 'Unknown command type' error is caused by disabled integrations, not a version mismatch. (vs common assumption that the error indicates addon/version mismatch)

## Points to
- https://github.com/ahujasid/mcp-for-blender
- https://projects.blender.org/lab/blender_mcp
- https://github.com/img2threejs/img2threejs
- https://github.com/Friedrich-M/UniMate
- https://huggingface.co/spaces/microsoft/TRELLIS.2
- https://arxiv.org/abs/2606.01057
- Poly Haven
- gltf-transform
- gltfpack
