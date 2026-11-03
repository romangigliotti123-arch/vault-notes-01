---
type: research-source
id: web-e55dbf852a
title: "DevForum thread 1064467"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/1064467"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "web", "roblox-mesh-limits"]
---
# web-e55dbf852a

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic DevForum thread (2021) on whether RenderFidelity Performance helps FPS for many 10k-30k tri clothing meshes on zombies. Not about Blender, Claude, blender-mcp, bpy, or the Blender-to-Roblox pipeline. Forum replies claim RenderFidelity depends on distance from character, not graphics setting, and a 10k tri per-mesh limit. Both are unverified forum claims.

## Claims
- c1: Forum reply says RenderFidelity Performance reduces mesh quality based on distance from the character, not on player graphics settings; the poster says they tested this in Studio. *(experience, low; roblox-mesh-limits)*
- c2: Forum reply claims the per-mesh triangle limit is 10k, so larger meshes must be split into separate parts. *(opinion, low; roblox-mesh-limits)*
- c3: OP's clothing outfits are 10k-30k+ triangles, with up to about 80 zombies in view; they split clothing into parts under 10k tris each. *(experience, low; roblox-mesh-limits)*

## Numbers
- n1: **Triangle limit per mesh (forum claim)**: 10k 
- n2: **OP clothing triangle count**: 10k-30k+ per outfit 
- n3: **Zombies in field (OP)**: around 80 max 

## Contradictions flagged
- RenderFidelity Performance may depend on graphics quality setting (OP hope, unconfirmed) (vs Reply claims it is purely distance-based, per testing in Studio)

## Points to
- https://developer.roblox.com/en-us/api-reference/enum/RenderFidelity
