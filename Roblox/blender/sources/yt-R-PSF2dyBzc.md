---
type: research-source
id: yt-R-PSF2dyBzc
title: "TOP 7 issues with your Blender Extension"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=R-PSF2dyBzc"
published: "2024-10-01"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-R-PSF2dyBzc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Transcript on rejected Blender Extensions platform submissions (Oct 2024): docs, cross-platform testing, self-contained packaging, permissions in manifest, zip cleanup, no Blender branding, legacy add-on conversion. Contains nothing on blender-mcp, bpy-to-Roblox export, FBX/glTF settings, Roblox limits, rigging, or accessories. Off-topic for the target subject.

## Claims
- c1: Blender Extensions platform reviewers reject submissions with unclear descriptions, missing demo media, or untested cross-OS behavior. *(opinion, high; other)*
- c2: Extensions must be self-contained; dependencies go in the add-on folder and pip installs at load time are disallowed. *(doc, medium; other)*
- c3: Extension Manifest must declare permissions (files, network, clipboard) with a reason for each. *(doc, medium; other)*
- c4: Blender's extension build command packages the zip and can exclude file patterns defined in the manifest, avoiding __pycache__ and metadata files. *(doc, medium; other)*
- c5: Extension names and assets must not use Blender branding or a Blender version number in the name. *(doc, medium; other)*
- c6: Legacy bl_info dictionary is deprecated and replaced by blender_manifest.toml; imports should be relative. *(doc, medium; other)*
