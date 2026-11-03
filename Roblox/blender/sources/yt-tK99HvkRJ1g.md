---
type: research-source
id: yt-tK99HvkRJ1g
title: "One Click Geo Nodes to Add-on"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=tK99HvkRJ1g"
published: "2025-01-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai"]
---
# yt-tK99HvkRJ1g

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video demos the free 'Node to Python' Blender add-on, which converts a geometry node group into an installable add-on zip (blender_manifest.toml + Python). Covers install and test in Blender. Not about Roblox, Claude/MCP, or FBX/glTF export; only tangentially related to Blender scripting.

## Claims
- c1: [0:00] Node to Python add-on generates a Blender add-on from a geometry node group; the user does not need to know Python. *(demo, high; automation-and-creator-workflows)*
- c2: [1:03] Before generating, user must set the save location and rename the geometry node setup, since that name is used as the add-on name when distributing. *(demo, high; automation-and-creator-workflows)*
- c3: [1:45] Generation is done by selecting the node group and clicking 'save geometry node group to' path; output is a zip archive. *(demo, high; automation-and-creator-workflows)*
- c4: [1:45] Generated archive contains a license file, blender_manifest.toml (new extensions format), and a Python file; also includes legacy bl_info dict for backward compatibility. *(demo, high; automation-and-creator-workflows)*
- c5: [3:23] Generated zip installs via Blender Preferences 'Install from Disk' as an extension and exposes the node group in the Geometry Nodes add menu. *(demo, high; automation-and-creator-workflows)*
- c6: [0:23] The add-on generator also can produce plain scripts (not add-ons) that run the node setup. *(demo, medium; claude-blender-ai)*
- c7: [1:03] Creator suggests a generate-code button would be better UX; the tool currently requires selecting the node group and saving. *(opinion, medium; automation-and-creator-workflows)*

## Numbers
- n1: **video length**: 4:37 

## Techniques
- t1: **Node group to add-on export**: Open Geometry Nodes editor, open Node to Python panel, set save path, rename node group, select group, click save to path, install zip via Install from Disk.

## Quotes (brief, for attribution)
> there's a blender add-on that can help you generate an add-on that will contain your geometry node setup  (at 0:00, CG Python)

## Points to
- Node to Python (Blender Extensions platform)
- CG Python community
