---
type: research-source
id: gh-HoldMyBeer-gg-blenderwright-rel-v2.2.1
title: "HoldMyBeer-gg/blenderwright v2.2.1: v2.2.1"
source_type: "github"
creator: "HoldMyBeer-gg"
url: "https://github.com/HoldMyBeer-gg/blenderwright/releases/tag/v2.2.1"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0007
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-HoldMyBeer-gg-blenderwright-rel-v2.2.1

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for blenderwright v2.2.1, a Claude-to-Blender MCP server. Two changes: create_object now bakes its scale, and assign_material fills an empty material slot first. Only tangentially related to the Roblox pipeline; no Roblox-specific content.

## Claims
- c1: blenderwright v2.2.1 changes create_object to bake its scale into the object. *(doc, high; claude-blender-mcp)*
- c2: blenderwright v2.2.1 changes assign_material to fill an empty material slot first before adding a new one. *(doc, high; claude-blender-mcp)*
- c3: Baking object scale at creation time is relevant to Roblox scale issues, since unapplied scale causes wrong-size imports, though this release notes does not say so. *(opinion, low; common-mistakes-fixes)*

## Numbers
- n1: **release date**: 2026-10-08 

## Techniques
- t1: **Apply scale on object creation**: create_object bakes scale into mesh data so the object's scale is 1.0 after creation (per PR #70 title). Relevant to avoiding unapplied-scale issues when exporting.

## Quotes (brief, for attribution)
> fix: create_object bakes its scale; assign_material fills an empty slot first  (HoldMyBeer-gg)

## Points to
- https://github.com/HoldMyBeer-gg/blenderwright/pull/70
- https://github.com/HoldMyBeer-gg/blenderwright/pull/71
- https://github.com/HoldMyBeer-gg/blenderwright/compare/v2.2.0...v2.2.1
