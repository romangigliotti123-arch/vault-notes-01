---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i40
title: "Roblox/roblox-blender-plugin#40 Unknown Error when attempting upload"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/40"
published: "2024-01-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai"]
---
# gh-Roblox-roblox-blender-plugin-i40

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #40 on Roblox/roblox-blender-plugin (Jan 2024). User reports the plugin's upload fails with "Unknown Error" after about 10 seconds, following a fixed dependency-module problem. A Roblox maintainer says a recent Open Cloud backend change may help, asks for the .blend file to diagnose, and closes the issue for lack of information. No fix or settings are given.

## Claims
- c1: Roblox Blender plugin upload failed with a generic 'Unknown Error' in Jan 2024; error appeared about 10 seconds after clicking upload. *(doc, high; blender-roblox-export-import)*
- c2: Maintainer said a recent backend change to the Open Cloud API might fix the upload failure; user confirmed it still failed. *(doc, medium; automation-and-creator-workflows)*
- c3: Earlier dependency-module error in the plugin was reported fixed before this upload error appeared. *(doc, medium; blender-roblox-export-import)*
- c4: Maintainer's diagnostic approach: request the user's .blend file containing the object or collection to check whether file contents cause server-side failure. *(doc, medium; blender-roblox-export-import)*
- c5: Private .blend sharing for this issue was routed via Roblox DevForum direct message to the maintainer rather than public posting. *(doc, low; automation-and-creator-workflows)*
- c6: Issue closed by maintainer as 'not enough information provided'; no root cause or resolution recorded. *(doc, high; blender-roblox-export-import)*
- c7: Source contains nothing about blender-mcp, bpy scripting, or Claude integration. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **time to 'Unknown Error'**: ~10 seconds reported by user after the backend change, before error displays
- n2: **issue date**: 2024-01-23 issue opened date

## Quotes (brief, for attribution)
> Can you confirm if this is still happening? We made a change recently on the backend open cloud API that might fix this.  (Roblox)
> Closing this as not enough information is provided. Feel free to comment again if you have more information.  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/40
- https://devforum.roblox.com/u/Nightriff/
