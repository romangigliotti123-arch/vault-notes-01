---
type: research-source
id: gh-Roblox-roblox-blender-plugin-rel-v1.0.1
title: "Roblox/roblox-blender-plugin v1.0.1: Release v1.0.1"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/releases/tag/v1.0.1"
published: "2023-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# gh-Roblox-roblox-blender-plugin-rel-v1.0.1

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Changelog for Roblox's blender plugin v1.0.1 (2023-10-31) listing five fixes: less common port to avoid conflicts, Display Name instead of Username, https required with secure Roblox issuer, upload timeout set to server timeout plus 5s, and clearer upload-timeout error. Thin for the topic: no Claude/blender-mcp, bpy, FBX/glTF settings, or mesh/rig/accessory specs.

## Claims
- c1: v1.0.1 (2023-10-31) of Roblox blender plugin changed the local server to a less common port to avoid port conflicts (PR #16). *(doc, high; blender-roblox-export-import)*
- c2: v1.0.1 uses Display Name instead of Username in the plugin (PR #23). *(doc, high; blender-roblox-export-import)*
- c3: v1.0.1 requires https and expects the Roblox issuer to be secure (PR #25). *(doc, high; blender-roblox-export-import)*
- c4: v1.0.1 extends upload timeout to server timeout plus 5s leeway (PR #27). *(doc, high; blender-roblox-export-import)*
- c5: v1.0.1 shows a better error message for upload timeouts (PR #29). *(doc, high; blender-roblox-export-import)*
- c6: Release notes do not mention blender-mcp, bpy scripting, or mesh/texture/rig/accessory specs; the source is a short changelog of plugin fixes only. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Upload timeout padding**: server timeout + 5s 
- n2: **Release date**: 2023-10-31 

## Points to
- https://github.com/Roblox/roblox-blender-plugin/compare/v1.0.0...v1.0.1
- https://github.com/Roblox/roblox-blender-plugin/pull/16
- https://github.com/Roblox/roblox-blender-plugin/pull/23
- https://github.com/Roblox/roblox-blender-plugin/pull/25
- https://github.com/Roblox/roblox-blender-plugin/pull/27
- https://github.com/Roblox/roblox-blender-plugin/pull/29
