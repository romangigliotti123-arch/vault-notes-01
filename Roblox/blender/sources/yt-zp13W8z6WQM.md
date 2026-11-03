---
type: research-source
id: yt-zp13W8z6WQM
title: "I Tested Tripo P2.0 for Production: Is It Ready for Unreal Engine?"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=zp13W8z6WQM"
published: "2026-08-18"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0030
relevance: 1
density: low
tags: ["research-source", "youtube", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-zp13W8z6WQM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tripo P2.0 review: AI 3D mesh generator with quad topology and poly-count control, generation around 5-6 seconds. Creator tests faces, hair, garments, hard-surface, and a full character to Unreal Engine via AccuRig. No Roblox, blender-mcp, bpy, or Roblox export content; text on objects is not reproduced.

## Claims
- c1: [0:00] Video is about Tripo P2.0 AI 3D generation (quad topology, poly-count control), not Blender-Roblox pipeline, blender-mcp, or bpy scripting. *(demo, high; other)*
- c2: [1:18] Tripo P2 is a continuation of Tripo P1 (Smart Mesh); update released about five months after P1. *(demo, high; other)*
- c3: [3:24] Poly count setting (e.g., 1500, 2500, 3000 quads) strongly changes generated topology; creator says choice of budget is critical. *(demo, medium; mesh-texture-limits)*
- c4: [8:16] Creator opened P2 output in Blender; parts are linked meshes, selectable with Ctrl+L; recommends generating in parts for control. *(demo, medium; mesh-texture-limits)*
- c5: [9:38] Tripo P2 generates topology only; texturing is a separate step in the texture tab. *(demo, high; mesh-texture-limits)*
- c6: [10:19] Cat model at 1500 quads (2500 faces) produced clean low-poly topology; Tripo counts quads and faces differently. *(demo, medium; mesh-texture-limits)*
- c7: [19:26] Hard-surface rifle output had a poor connection pattern on some faces; creator judged it not professional-quality topology. *(opinion, medium; mesh-texture-limits)*
- c8: [21:29] Text on objects (e.g., coin, guild sign) is ignored or not reproduced as geometry even at 10,000 quads; a known limitation. *(demo, high; mesh-texture-limits)*
- c9: [25:51] Creator found inverted normals in P2 output (pre-release build), fixed manually in Blender; attributed partly to texturing. *(demo, medium; mesh-texture-limits)*
- c10: [27:47] Character rigged with AccuRig by placing markers for body and fingers; creator added bones to tail for physics in Unreal. *(demo, medium; rigging-animation)*
- c11: [28:44] Full character (generation, Blender assembly, rig) took about one hour; the creator uses Unreal Engine, not Roblox, for the final step. *(demo, high; other)*

## Numbers
- n1: **generation time**: 5-6 seconds 
- n2: **low-poly budget example**: 3000 faces house/grass asset example, 3600 faces total 
- n3: **asset face count**: 3600 faces 
- n4: **full character workflow time**: about 1 hour 

## Techniques
- t1: **Generate in parts**: Generate body, boots, weapon, hat, belt as separate objects with own poly budgets, then assemble in Blender and align.
- t2: **Ctrl+L linked-select check**: In Blender edit mode, Ctrl+L selects linked geometry to verify separate mesh parts.

## Quotes (brief, for attribution)
> It's probably the first time we can generate low poly without need of further refine.  (at 0:00, Stefan 3D AI)
> because a smart mesh produces only topology very fast  (at 9:38, Stefan 3D AI)

## Contradictions flagged
- Creator says P2 produces 'perfect quad topology' and generation needs no refinement. (vs Same video shows hard-surface rifle and car with poor connections and holes; creator says fixes are needed.)

## Points to
- Tripo (tripo3d)
- Tripo P1 Smart Mesh
- AccuRig
- Unreal Engine
- Blender
- Stefan 3D AI course
