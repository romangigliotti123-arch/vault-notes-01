---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-CROSS_MCP_EXPORT_SYSTEM.md
title: "sandraschi/blender-mcp/docs/CROSS_MCP_EXPORT_SYSTEM.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/CROSS_MCP_EXPORT_SYSTEM.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0400
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-sandraschi-blender-mcp-f-docs-CROSS_MCP_EXPORT_SYSTEM.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Design spec (not implemented; planned Q1 2026) for a cross-MCP export system in sandraschi/blender-mcp, handing Blender assets to VRChat, Resonite, Unity, Unreal MCP servers. It has no Roblox content. Only generic ideas apply: per-platform optimization presets, FBX/GLTF export, polygon/material/texture limits, validation. Mostly aspirational pseudo-code with unverified targets.

## Claims
- c1: Doc is a specification only; implementation status is 'Specification Complete, Implementation Planned Q1 2026'. The code shown is design pseudo-code, not working tooling. *(doc, high; automation-and-creator-workflows)*
- c2: Proposes a single function export_for_mcp_handoff(asset_id, target_mcp, optimization_preset, quality_level) returning primary files, supporting files, integration commands, metadata, optimization report and validation results. *(doc, high; claude-blender-ai)*
- c3: Spec'd VRChat preset: 70k polygon avatar limit, 100k triangle scene limit, 8 materials, 2048 max texture, 256 bones, auto decimation, LOD generation, atlasing. These are VRChat values, not Roblox. *(doc, medium; mesh-texture-limits)*
- c4: Resonite preset: 100k polygons, 16 materials, collision mesh generation, GLTF/GLB export. *(doc, medium; mesh-texture-limits)*
- c5: No Roblox target is defined; supported targets are vrchat, resonite, unity, unreal. A Roblox engine would need a new PlatformExportEngine subclass. *(doc, high; blender-roblox-export-import)*
- c6: Claims targets such as <2 min chair-to-VRChat, 99.9% transfer success and <5% manual intervention; these are unmeasured goals, not results. *(opinion, low; automation-and-creator-workflows)*
- c7: Examples call construct_object(description, style_preset, complexity, rigging, export_target) for natural-language asset generation in Blender MCP, then hand off to another MCP. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **VRChat avatar polygon limit (spec)**: 70000 
- n2: **VRChat max texture size (spec)**: 2048 
- n3: **VRChat bone limit (spec)**: 256 
- n4: **Resonite polygon limit (spec)**: 100000 
- n5: **Target export time, simple/complex/scene**: <10s / <60s / <5min 

## Techniques
- t1: **Per-platform export engine abstraction**: Define abstract PlatformExportEngine with optimize, generate_files, generate_integration_commands, validate_compatibility; register per target in a dict; export returns files plus validation report. Pattern could be reused for a Roblox engine.

## Points to
- sandraschi/blender-mcp
- VRChat MCP
- Resonite ProtoFlux
- Unity MCP
