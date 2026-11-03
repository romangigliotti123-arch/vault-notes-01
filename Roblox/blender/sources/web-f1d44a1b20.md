---
type: research-source
id: web-f1d44a1b20
title: "Managing 32-bit floating point precision with relative camera offsets"
source_type: "web"
creator: "hydroxide.dev"
url: "https://hydroxide.dev/articles/32-bit-floating-point-precision-relative-camera-offsets/"
published: "2025-12-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 0
density: medium
tags: ["research-source", "web", "other"]
---
# web-f1d44a1b20

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Filament renderer deep-dive on float32 precision: getWorldFromModelMatrix() yields camera-relative "camera offset space" because camera_at_origin moves the camera to origin. Recover true world position via getUserWorldFromWorldMatrix(). Not about Blender, bpy, MCP, or Roblox export.

## Claims
- c1: Source covers Filament game-engine shader internals, not Blender, bpy, blender-mcp, or Roblox asset pipeline. *(doc, high; other)*
- c2: Float32 cannot represent 10,000,000.5; adding 0.5 to 10,000,000 in float32 returns 10,000,000.0, collapsing a small triangle. *(demo, high; other)*

## Numbers
- n1: **float32 precision example**: 10,000,000 + 0.5 rounds to 10,000,000 

## Techniques
- t1: **Camera-relative coordinates for float precision**: Offset model transforms relative to camera position so values stay near zero, where float32 precision is highest. Filament does this via camera_at_origin.

## Points to
- https://hydroxide.dev/articles/32-bit-floating-point-precision-relative-camera-offsets/
