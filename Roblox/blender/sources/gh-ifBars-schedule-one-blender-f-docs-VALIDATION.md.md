---
type: research-source
id: gh-ifBars-schedule-one-blender-f-docs-VALIDATION.md
title: "ifBars/schedule-one-blender/docs/VALIDATION.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender/blob/HEAD/docs/VALIDATION.md"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: medium
tags: ["research-source", "github", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# gh-ifBars-schedule-one-blender-f-docs-VALIDATION.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Validation record for ifBars/schedule-one-blender, a tool that extracts a Unity game scene (Schedule I, IL2CPP/Mono) into Blender files. Not about Roblox, blender-mcp, or bpy-driven Claude workflows. Useful only as a loose reference for Blender packing and relative-path pitfalls: Windows handling of Blender "//" relative texture paths broke an editor phase, and packed textures were capped at 512px.

## Claims
- c1: Source is a Unity-to-Blender extraction tool validation for game 0.4.7f9; it does not cover Roblox export or blender-mcp. *(doc, high; other)*
- c2: Windows handling of Blender '//' relative texture paths caused a failure; fixed before the editor phase passed validation. *(doc, high; blender-roblox-export-import)*
- c3: Editor validation packed 1,296 images, all at most 512px, as the texture budget. *(data, high; mesh-texture-limits)*
- c4: Terrain control textures used Channel Packed mode with weight-sum error below 0.008. *(data, medium; mesh-texture-limits)*
- c5: Validated against Blender 5.2.2 LTS on Windows with Python 3.13.11; the source does not mention MCP or Claude. *(data, high; claude-blender-ai)*
- c6: Raising camera near clip from 0.01m to 0.5m removed depth artifacts in a bridge without changing geometry. *(demo, medium; mesh-texture-limits)*
- c7: A NumPy shaped inverse-index output broke submesh slicing in Unity import; flattening the array before slicing fixed the geometry. *(demo, medium; other)*
- c8: Smoothness and wetness outliers in materials were normalized to the median dry peer for preview only; this is an opinionated approximation, not game-runtime parity. *(doc, medium; mesh-texture-limits)*

## Numbers
- n1: **max packed image size**: 512px (1,296 images) Blender editor validation texture budget
- n2: **Blender version**: 5.2.2 LTS Validation environment, Windows
- n3: **near clip change**: 0.01m to 0.5m Viewport and reference cameras fix for bridge depth artifacts
- n4: **viewport peak memory**: 5,118 MiB working set, 11,442 MiB committed 960x640 Material Preview check, one scene and machine
- n5: **editor objects**: 2,907 Validated editor scene object count

## Techniques
- t1: **Packing textures for budget**: Cap texture size at 512px, pack images into the .blend, then verify packed count and sizes in a fresh-process validation pass.
- t2: **Channel-packed terrain controls**: Store terrain weight controls in Channel Packed textures; check that channel weight sums stay within a tolerance (0.008 reported).

## Quotes (brief, for attribution)
> Windows handling of Blender's `//` relative texture paths.  (ifBars)

## Points to
- https://github.com/ifBars/schedule-one-blender
