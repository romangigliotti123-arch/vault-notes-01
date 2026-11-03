---
type: research-source
id: off-art_modeling_roblox-blender-plugin
title: "Roblox Creator Docs: art_modeling_roblox-blender-plugin"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/roblox-blender-plugin"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 2
density: low
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# off-art_modeling_roblox-blender-plugin

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Official Roblox doc page for the Roblox Blender plugin: a Blender add-on that links a Roblox account and sends objects directly to a Studio session, avoiding export/import of third-party files. Open-source, built on Open Cloud API; installation, licensing and contribution details live on the GitHub repo. Includes a demo video. Does not cover Claude, blender-mcp, bpy scripting, export settings, scale, triangle limits, rigging or accessories.

## Claims
- c1: Roblox Blender plugin is a Blender add-on that links a Roblox account and transfers 3D objects directly from Blender into a Studio session, skipping manual export/import of third-party files. *(doc, high; blender-roblox-export-import)*
- c2: Roblox Blender plugin is an open-source implementation of Roblox's Open Cloud API; developers are encouraged to extend it. Source repo: github.com/Roblox/roblox-blender-plugin. *(doc, high; automation-and-creator-workflows)*
- c3: Source page does not mention Claude, blender-mcp, bpy scripting, or blender -b batch workflows; it is only about the official plugin. *(doc, high; claude-blender-ai)*
- c4: Source gives no triangle limits, UV rules, texture sizes, or SurfaceAppearance guidance. *(doc, high; mesh-texture-limits)*
- c5: Source gives no rigging, skinning, Motor6D, or animation export details. *(doc, high; rigging-animation)*
- c6: Source gives no accessory specs, attachment, or validation requirements. *(doc, high; avatar-ugc-accessories)*

## Techniques
- t1: **Direct Blender-to-Studio transfer via plugin**: Install Roblox Blender plugin add-on in Blender, link Roblox account, then send selected objects straight to an open Studio session. Installation and usage details are on the GitHub page, not this doc.

## Quotes (brief, for attribution)
> allows you to link your Roblox account and quickly transfer 3D modeling objects directly from Blender to your Studio session.  (create.roblox.com)

## Points to
- https://github.com/Roblox/roblox-blender-plugin
- https://create.roblox.com/docs/cloud/guides/index.md
