---
type: research-source
id: yt-RqxOoaPE_0Q
title: "Bye 2025! — Blender Today LIVE #271"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=RqxOoaPE_0Q"
published: "2025-12-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0067
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other", "rigging-animation"]
---
# yt-RqxOoaPE_0Q

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today Live #271 (Dec 23, 2025) recaps about a month of Blender 5.x dev changes. It does not cover Roblox, Claude, blender-mcp, bpy automation, or FBX/glTF export. Only tangential items: Python 3.13 in the VFX-platform update, Python 3.14 build fix, a Bone Info geometry node, and a file-hash service for asset libraries.

## Claims
- c1: [1:10] Dec 2025 dev cycle: VFX Platform 2026 library updates include Python 3.13, NumPy 2.3, OpenColorIO 2.5 (stated as bumps, versions partly garbled in transcript). *(doc, medium; other)*
- c2: [9:53] Python 3.14 build fix landed while Blender ships with Python 3.13 (Blender 5.1 target); speaker says 3.14 compatibility is good but not default. *(doc, medium; claude-blender-ai)*
- c3: [41:40] New Bone Info geometry node takes an armature object and bone name, exposes pose/rest transforms and rest length; outputs added incrementally to avoid breakage. Depends on evaluated armature. *(doc, medium; rigging-animation)*
- c4: [1:09:51] New Python disk file hash service for efficiently hashing files to verify against expected hash; aimed at remote/online asset libraries and later Blender Asset Tracer. *(doc, medium; automation-and-creator-workflows)*
- c5: [52:35] Extensions can now request camera and system audio permissions (macOS prompts for camera). *(doc, medium; automation-and-creator-workflows)*
- c6: [2:06:54] Blender 2025 community survey (~100 responses at time of stream): 7% regularly use AI in work; 69% answered no and not interested. *(data, low; other)*
- c7: [1:52:24] Speaker says the 2026 focus includes texturing in Blender as the missing asset-creation piece; opinion, not a committed schedule. *(opinion, low; other)*

## Numbers
- n1: **Python version in VFX platform update**: 3.13 
- n2: **Changes covered this episode**: ~700 changes over four weeks 
- n3: **Armature with many bones, average frame time**: 0.051 to 0.025 
- n4: **Cycles first-time shader compile**: 114 s reduced to about half 
- n5: **Edit mesh undo speedup from array hashing change**: about 20-30% faster 
- n6: **Teleport arc control points**: 12 to 24 

## Points to
- chat.blender.org
- devtalk.blender.org
- developer.blender.org
- blender.org/download (5.0.1 released Dec 16, 2025)
