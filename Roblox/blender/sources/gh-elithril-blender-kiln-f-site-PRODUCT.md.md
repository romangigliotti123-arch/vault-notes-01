---
type: research-source
id: gh-elithril-blender-kiln-f-site-PRODUCT.md
title: "elithril/blender-kiln/site/PRODUCT.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/site/PRODUCT.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-mcp", "creator-workflows", "other", "roblox-export-settings"]
---
# gh-elithril-blender-kiln-f-site-PRODUCT.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Product doc for blender-kiln, a Claude Code plugin that turns a text brief or photo into a GLB (Draco/WebP), FBX or USDZ by driving Blender through an MCP server (ahujasid's or Blender Lab's). Requires Blender 4.4+ with an MCP server running. No Roblox-specific content: no Roblox export settings, import steps or limits.

## Claims
- c1: blender-kiln drives Blender through an MCP server, either ahujasid's Blender MCP or the official Blender Lab MCP, to build assets from a text brief or photo. *(doc, high; claude-blender-mcp)*
- c2: Requires Blender 4.4+; the author reports verification on Blender 5.0 and 5.2, with a Blender MCP server running. *(doc, high; claude-blender-mcp)*
- c3: Outputs include GLB optimized with Draco/WebP, FBX and USDZ. No Roblox-specific export settings are given. *(doc, high; roblox-export-settings)*
- c4: Text-brief GLB size fell from 32.9 MB to 0.96 MB with the ahujasid MCP, and from 3.9 MB to 0.75 MB with the Blender Lab MCP, per the author's benchmarks. *(data, medium; claude-blender-mcp)*
- c5: The 15-prop gallery and animation showcase were produced by scripts written to the skill's rules, not by an interactive session of the skill. *(doc, high; other)*
- c6: Bench scores each photo rebuild against the real 3D object it was photographed from. Lantern 0.830 to 0.897, ammo box 0.854 to 0.950, gothic chair 0.445 to 0.750; one run per brief. *(data, medium; other)*
- c7: Size is an assumption when a brief gives none. No paid image or 3D cloud service is used without explicit consent and a cost estimate. *(doc, high; creator-workflows)*
- c8: Animation: since 2.1 the plugin animates what it rigs, routed by subject; 2.2 adds a /kiln animate command. *(doc, high; other)*
- c9: UniMate model weights are CC BY-NC 4.0, which means non-commercial use only. *(doc, high; other)*

## Numbers
- n1: **Blender version requirement**: 4.4+ (verified 5.0 / 5.2) 
- n2: **Text-brief GLB size, ahujasid MCP**: 32.9 MB -> 0.96 MB 
- n3: **Text-brief GLB size, Blender Lab MCP**: 3.9 MB -> 0.75 MB 
- n4: **Bench score, lantern**: 0.830 -> 0.897 
- n5: **Bench score, ammo box**: 0.854 -> 0.950 
- n6: **Bench score, gothic chair**: 0.445 -> 0.750 
- n7: **Shipped GLB size**: lantern 229 KB; ammo box 187 KB; chair 239 KB 

## Techniques
- t1: **Install as Claude Code plugin**: Run /plugin marketplace add elithril/blender-kiln, then /plugin install blender-kiln@blender-kiln, then /kiln setup. Start a Blender MCP server first.

### Code: Install blender-kiln plugin in Claude Code
```text
/plugin marketplace add elithril/blender-kiln
/plugin install blender-kiln@blender-kiln
/kiln setup
```

## Quotes (brief, for attribution)
> Requires Blender 4.4+ (verified 5.0 / 5.2) with a Blender MCP server running.  (elithril)

## Points to
- https://github.com/elithril/blender-kiln
- ahujasid Blender MCP
- Blender Lab MCP (official)
- arXiv 2606.01057 (3DCodeBench)
