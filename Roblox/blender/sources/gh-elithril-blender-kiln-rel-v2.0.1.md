---
type: research-source
id: gh-elithril-blender-kiln-rel-v2.0.1
title: "elithril/blender-kiln v2.0.1: blender-kiln 2.0.1"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v2.0.1"
published: "2026-10-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-export-settings", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-rel-v2.0.1

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Patch release v2.0.1 of elithril/blender-kiln, a Claude Code plugin. It only fixes the /plugin menu description, which still described 1.x (text brief to optimized GLB, Hunyuan3D only). The description now lists 2.0 features: rebuilding from a photo, CC0 scan textures, local TRELLIS.2 templates, and both Blender MCP servers. No change to skill, tools or output. Roblox is not mentioned.

## Claims
- c1: blender-kiln 2.0 description says it works with both Blender MCP servers (names not given in source). *(doc, high; claude-blender-mcp)*
- c2: blender-kiln 1.x was text-brief-to-GLB via Hunyuan3D only; 2.0 adds local TRELLIS.2 templates and rebuilding from a photo. *(doc, high; procedural-generation)*
- c3: blender-kiln 2.0 applies textures from CC0 scans. *(doc, high; texturing-baking-uv)*
- c4: v2.0.1 changed only the plugin description text; skill, tools and output are unchanged from 2.0.0. *(doc, high; creator-workflows)*
- c5: The description bug was found by installing 2.0.0 from GitHub into a clean Claude Code profile. *(experience, medium; common-mistakes-fixes)*
- c6: Source says nothing about Roblox import, scale, or mesh/texture limits; output format stated is GLB only. *(doc, high; roblox-export-settings)*

## Quotes (brief, for attribution)
> from text brief to optimized GLB  (elithril)

## Points to
- https://github.com/elithril/blender-kiln/releases/tag/v2.0.0
- https://github.com/elithril/blender-kiln/compare/v2.0.0...v2.0.1
