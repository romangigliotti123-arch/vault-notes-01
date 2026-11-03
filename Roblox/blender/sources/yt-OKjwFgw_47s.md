---
type: research-source
id: yt-OKjwFgw_47s
title: "Blender 5.0 BETA & 5.1 ALPHA — Blender Today LIVE #267"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=OKjwFgw_47s"
published: "2025-10-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0085
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "other", "procedural-generation"]
---
# yt-OKjwFgw_47s

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live #267 (Oct 2025) covering Blender 5.0 beta and 5.1 alpha changes. Nothing on Roblox, Claude, blender-mcp, or Roblox export. Only tangential bpy/API version-drift notes: removed legacy conversion operator, Python default node-tree change, Python 3.11 to 3.13 planned for 2026, and API breaking-change docs in release notes.

## Claims
- c1: [4:23] Blender 5.0 removed the legacy pose library conversion operator; users needing it are pointed to Blender 4.5 to run the conversion first. *(doc, high; bpy-scripting-headless)*
- c2: [1:10:36] Blender 5.0 Python change: default node tree for new materials and worlds is now created in Python, to keep backward compatibility after deprecating material use_nodes. *(doc, high; bpy-scripting-headless)*
- c3: [1:10:36] New Python callback for bpy.data file path iteration remapping was added in Blender 5.0 beta. *(doc, medium; bpy-scripting-headless)*
- c4: [2:04:36] Release notes (5.0 beta, Python API breaking changes) list old-to-new replacements; add-on authors should search and replace removed calls before release. *(doc, medium; bpy-scripting-headless)*
- c5: [18:09] Per VFX Platform guidance, Blender 2025 uses OpenColorIO 2.4; 2026 draft expects OCIO 2.5 and Python 3.13 (from 3.11), with C++20 mentioned for developers. *(doc, medium; bpy-scripting-headless)*
- c6: [35:07] Essential asset node groups added to a scene are packed locally and do not auto-update when Blender changes; users must replace them manually after upgrading. *(doc, medium; procedural-generation)*
- c7: [1:57:11] Speaker says the Blender 5.0 beta API is frozen once beta starts; breaking changes are documented, not guaranteed unchanged across betas. *(opinion, low; other)*

## Numbers
- n1: **Commits covered**: about 80 of ~500 in the week Presenter's sampling of Blender 5.0/5.1 commits in this episode.
- n2: **Python version**: 3.11 now, 3.13 planned for next year Blender follows VFX Platform guidance for Python upgrades.
- n3: **OpenColorIO**: 2.4 (2025 VFX Platform), 2.5 expected 2026 Library version tied to VFX Platform yearly guideline.

## Quotes (brief, for attribution)
> the API is not going to change until the the release is on beta.  (at 2:04:36, Blender)

## Points to
- blender.org
- vfxplatform.com
- network.blender.org
- fund.blender.org
