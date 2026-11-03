---
type: research-source
id: gh-elithril-blender-kiln-rel-v2.0.0
title: "elithril/blender-kiln v2.0.0: blender-kiln 2.0 — from a photo to a measured asset"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v2.0.0"
published: "2026-10-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-export-settings", "roblox-mesh-limits", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-rel-v2.0.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for blender-kiln v2.0.0, a Claude plugin that rebuilds Blender objects from photos. It works through two Blender MCP servers (official Blender Lab and ahujasid's mcp-for-blender), uses CC0 Poly Haven textures, and benchmarks shape fidelity. Nothing Roblox-specific; output is GLB with Draco/WebP, which Roblox import does not cover.

## Claims
- c1: kiln 2.0 runs on both the official Blender Lab MCP (behind Claude's Blender connector) and ahujasid's mcp-for-blender. *(doc, high; claude-blender-mcp)*
- c2: Poly Haven is accessed via its public API when an MCP server has no Poly Haven integration. *(doc, high; claude-blender-mcp)*
- c3: Rebuild-from-photo pipeline: inventory parts from enlarged crops, settle real size and camera before modeling, measure silhouette/materials against photo via tools/fidelity_check.py, render and inspect each joint, re-measure shipped GLB. *(doc, high; procedural-generation)*
- c4: Optional 3D template: proportions read from a TRELLIS.2 mesh generated from the same photo (run locally on Apple Silicon) via tools/template_profile.py; measured, never shipped. *(doc, high; procedural-generation)*
- c5: Textures come from Poly Haven CC0 scan sets chosen against the photo, tinted to its palette, worn by form, and baked to UVs. *(doc, high; texturing-baking-uv)*
- c6: Brass has no scanned set in Poly Haven and gained less than rust and wood. *(data, medium; texturing-baking-uv)*
- c7: Fixed a float colour bake that exported black and a headless Blender crash that exited 0. *(doc, high; common-mistakes-fixes)*
- c8: Triangle range in a brief is a guide, not a cap: up to twice a tier's top is kept and reported; reduction is proposed beyond that. Thin parts are rebuilt as curves, not decimated. *(doc, high; roblox-mesh-limits)*
- c9: _final.glb ships Draco (KHR_draco_mesh_compression) and WebP (EXT_texture_webp) by default; loaders need a Draco decoder and WebP support. _original.glb is still written. Roblox import support for these extensions is not stated in the source. *(doc, medium; roblox-export-settings)*
- c10: Author-reported size assumption: when a brief gives no object size, it is assumed and atypical objects get it wrong. *(doc, high; creator-workflows)*
- c11: Author-reported benchmark: 3 photo references, one run each, Blender 5.2.2 and Opus 5.5; shape scores 0.750-0.950 against real asset; not a broad test. *(data, medium; creator-workflows)*
- c12: Plugin upgrade from 1.x via Claude Code /plugin menu or reinstall; commands, brief format and output layout unchanged. *(doc, medium; claude-blender-mcp)*

## Numbers
- n1: **Shape score (silhouette overlap, 5 sides)**: lantern 0.897, ammo box 0.950, gothic chair 0.750 kiln 2.0 scores vs real asset; before-photo-method 0.830, 0.854, 0.445
- n2: **Shipped GLB size**: 229 KB, 187 KB, 239 KB three photo-based assets in v2.0.0 benchmark
- n3: **Text brief total size**: 32.9 MB to 0.96 MB five text briefs, GLB compression on both MCP servers
- n4: **Skill trigger tests**: 12 prompts, all fire, no false positive 4 held out while skill was written

## Techniques
- t1: **Photo-to-asset rebuild**: Inventory parts from enlarged crops; fix real size and camera first; model; measure silhouette and materials vs photo with fidelity_check.py; render each joint; re-measure shipped GLB.
- t2: **Template-driven proportions**: Generate mesh from same photo with TRELLIS.2 locally; read proportions via template_profile.py; use only for measurement, not shipping.
- t3: **Scan-based texture selection and tint**: Pick CC0 Poly Haven sets matching photo; tint to photo palette; add wear from form; bake to UVs.

## Points to
- https://github.com/elithril/blender-kiln/releases/tag/v2.0.0
- https://github.com/elithril/blender-kiln/blob/v2.0.0/docs/benchmarks.md
- https://github.com/elithril/blender-kiln/blob/v2.0.0/CHANGELOG.md
- ahujasid/mcp-for-blender
- Blender Lab official MCP
- Poly Haven
- TRELLIS.2
