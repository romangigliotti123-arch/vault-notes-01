---
type: research-source
id: gh-ifBars-schedule-one-blender-f-docs-ARCHITECTURE.md
title: "ifBars/schedule-one-blender/docs/ARCHITECTURE.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender/blob/HEAD/docs/ARCHITECTURE.md"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: medium
tags: ["research-source", "github", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# gh-ifBars-schedule-one-blender-f-docs-ARCHITECTURE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Architecture doc for ifBars/schedule-one-blender, a tool that extracts a Unity game (Schedule One) into Blender scenes using UnityPy and Blender's Python. It covers Unity asset decoding, terrain and texture reduction, material translation, and a native expansion loader. It does not cover Roblox, blender-mcp, or the Roblox export pipeline.

## Claims
- c1: Tool targets Unity game extraction (UnityPy, BuildSettings, Mono/IL2CPP layouts) into Blender, not Roblox Studio export. *(doc, high; other)*
- c2: Document contains no Roblox-specific FBX/glTF settings, MeshPart import, or Studio importer guidance. *(doc, high; blender-roblox-export-import)*
- c3: Document does not mention blender-mcp, MCP servers, or LLM-driven Blender control; Blender side uses its own Python for scene creation. *(doc, high; claude-blender-ai)*
- c4: Ordinary color textures are bounded to 512px proxies and reduced with Pillow LANCZOS; terrain controls use independent-channel BOX reduction. *(doc, high; mesh-texture-limits)*
- c5: Reference meshes are batched into 64m chunks with source-ID provenance; forest meshes are shared while terrain tiles stay separate. *(doc, high; mesh-texture-limits)*
- c6: Packed Unity normal maps are decoded into tangent-space RGB; alpha is not treated as normal data because it may mean transparency or a fourth terrain material. *(doc, medium; mesh-texture-limits)*
- c7: Compiled custom shaders cannot run in Blender; dynamic water, foam, vegetation motion, weather and volumetrics are approximated or not exact. *(doc, high; other)*
- c8: Serialized skinned meshes are exported frozen; runtime-spawned entities and gameplay state are absent. *(doc, high; rigging-animation)*
- c9: Offline extraction does not execute game code; CI cannot include the user's game assets and needs a local game for full completeness checks. *(doc, high; other)*

## Numbers
- n1: **texture proxy max size**: 512px 
- n2: **mesh batch chunk size**: 64m 

## Points to
- https://docs.unity3d.com/2022.3/Documentation/ScriptReference/Renderer-localToWorldMatrix.html
- EXPANSIONS.md
