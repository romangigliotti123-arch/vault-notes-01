---
type: research-source
id: gh-elithril-blender-kiln-rel-v1.0.0
title: "elithril/blender-kiln v1.0.0: v1.0.0 — The 3D Asset Forge"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v1.0.0"
published: "2026-08-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "open-cloud-automation", "other", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-rel-v1.0.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for blender-kiln v1.0.0, a Claude Code plugin pipeline that drives Blender over blender-mcp for AI/scripted/marketplace 3D asset creation, with batch mode and post-export validation. Roblox is not mentioned; relevance to Roblox-specific pipeline is low. Covers install, pipeline stages, Blender 4.x+ and MCP port 9876 requirements, and two install bugs fixed.

## Claims
- c1: Pipeline drives Blender over MCP; requires Blender 4.x+ with the Blender MCP addon (ahujasid/blender-mcp) listening on port 9876. *(doc, high; claude-blender-mcp)*
- c2: Installed as a Claude Code plugin via /plugin marketplace add elithril/blender-kiln then /plugin install; /kiln setup detects environment and installs missing pieces. *(doc, high; claude-blender-mcp)*
- c3: Creation methods: Hunyuan3D 2.x (local or cloud), scripted modeling, geometry nodes, or marketplace sourcing from PolyHaven and Sketchfab. *(doc, high; procedural-generation)*
- c4: Local Hunyuan3D-2 Mini: full shape+texture pipeline on NVIDIA; shape-only generation on Apple Silicon via MPS. *(doc, high; procedural-generation)*
- c5: Batch mode: wizard collects scene, theme, palette and reference images, emits a YAML manifest, and a runner executes it autonomously. *(doc, high; bpy-scripting-headless)*
- c6: Material export audit detects procedural nodes that GLTF export would silently drop and proposes a bake workflow. *(doc, high; texturing-baking-uv)*
- c7: Post-export validation is an 8-point checklist including Babylon.js sandbox and Three.js console checks; it is not Roblox-specific. *(doc, medium; common-mistakes-fixes)*
- c8: Character support includes T-pose enforcement, rigging patterns, bone validation, and Blender 5.x bone collections. *(doc, medium; rigging-animation)*
- c9: Plugin marketplace.json source pointed to a nonexistent directory path; spec requires a directory starting with ./ — fixed in v1.0.0. *(doc, high; common-mistakes-fixes)*
- c10: Documented /kiln:<sub> colon commands did not resolve because kiln is a single skill with no commands/ directory; working form is /kiln <sub>. *(doc, high; open-cloud-automation)*
- c11: Pipeline stages: CONFIG → BRIEF → SOURCE → IMPORT → CLEANUP → TEXTURING → OPTIMIZE → EXPORT. *(doc, high; creator-workflows)*
- c12: Design rules: 26 iron rules, including never hard-capping poly count, never silently destroying geometry, always keeping the .blend as recovery point. *(doc, medium; creator-workflows)*
- c13: Pipeline was developed April 2026 but first released as v1.0.0 on 2026-08-26; MIT license declared, LICENSE file added in this release. *(doc, high; other)*

## Numbers
- n1: **MCP port**: 9876 
- n2: **Blender version required**: 4.x+ 
- n3: **Post-export validation checks**: 8-point checklist 
- n4: **Iron rules**: 26 
- n5: **Documented /kiln sub-commands**: 12 
- n6: **Release date**: 2026-08-26 (pipeline started April 2026) 

## Techniques
- t1: **Install and setup**: Add marketplace elithril/blender-kiln, install blender-kiln@blender-kiln, run /kiln setup to detect environment and install missing optional tools. Requires Blender MCP addon on port 9876.
- t2: **Batch manifest runner**: Run wizard to collect scene, theme, palette, reference images; it writes a YAML manifest; runner executes autonomously overnight.
- t3: **Material export audit**: Scan for procedural nodes GLTF export would drop; propose bake workflow before export.

## Quotes (brief, for attribution)
> Blender 4.x+ with the Blender MCP addon on port 9876. Everything else is optional and detected by /kiln setup.  (elithril)
> never hard-cap poly count, never silently destroy geometry, always keep the .blend as the recovery point.  (elithril)

## Points to
- https://github.com/ahujasid/blender-mcp
- https://github.com/elithril/blender-kiln/blob/main/CHANGELOG.md
- https://github.com/elithril/blender-kiln
