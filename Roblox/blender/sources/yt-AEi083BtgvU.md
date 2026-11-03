---
type: research-source
id: yt-AEi083BtgvU
title: "Yuify Your Mesh to Say Who Made It: Micromarking and Self-Sovereign Identity — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=AEi083BtgvU"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-AEi083BtgvU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Wacom UFI talk on invisible "micromarking" of 3D meshes for provenance and ownership, using a Blender add-on still in research/early-user phase. Nothing on Roblox, Claude, blender-mcp, bpy workflows, or the Roblox export pipeline. Only marginally relevant to Blender 3D asset identity.

## Claims
- c1: [1:35] UFI Blender add-on is not publicly released; speaker says it is in validation/research phase, with early-user testing planned toward end of 2026. *(doc, high; other)*
- c2: [16:49] Blind micromark embeds a decentralized identifier into mesh vertex positions; speaker says modifications are small but may matter for 3D printing or precision use. *(doc, medium; other)*
- c3: [20:44] Non-blind method extracts distinctive mesh features without modifying geometry, but matching is similarity-based and can yield false positives. *(doc, medium; other)*
- c4: [22:07] With the UFI add-on installed, operator actions are tracked into a creation history record; speaker says many operators are filtered out. *(doc, medium; other)*
- c5: [33:47] Speaker says provenance metadata is lost on Blender export when the target 3D format has no metadata field; no common 3D metadata standard exists. *(opinion, medium; other)*
- c6: [29:47] DID method used by UFI is not yet in the universal DID resolver; speaker says inclusion is pending. *(doc, low; other)*

## Numbers
- n1: **randomness per DID**: 122 bits 

## Points to
- UFI (ufi.com)
- UFI blog (QR code in talk)
- C2PA
- W3C DID standard
