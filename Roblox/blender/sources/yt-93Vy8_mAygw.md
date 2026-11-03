---
type: research-source
id: yt-93Vy8_mAygw
title: "Blender Grease Pencil Tutorial: How to Create a Fantasy Map (/Gimp)"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=93Vy8_mAygw"
published: "2021-07-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 0
density: low
tags: ["research-source", "youtube", "other", "texturing-baking-uv"]
---
# yt-93Vy8_mAygw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Grease Pencil tutorial on hand-drawing a stylized fantasy map in 2D animation workspace, then rendering layers as transparent PNGs (Film > Transparent, PNG RGBA) and colouring them in an external image editor. Covers no Claude, blender-mcp, bpy, Roblox import or export material.

## Claims
- c1: Source is off-topic: a 2D Grease Pencil fantasy-map art tutorial; no mention of Claude, blender-mcp, bpy scripting, or Roblox export/import. *(doc, high; other)*
- c2: [9:52] Render transparency for overlay layers: enable Film > Transparent, output PNG with alpha (RGBA), 100% resolution, so layers composite without white background. *(demo, high; texturing-baking-uv)*

## Numbers
- n1: **Output resolution**: 100% Render resolution set to 100% before rendering layers as PNG with alpha

## Techniques
- t1: **Per-layer render separation**: Hide all but one element group (land, mountains, trees), render each to a separate transparent PNG, then import as layers in an image editor for colouring.
