---
type: research-source
id: yt-IeblIBmiPWI
title: "How To Get FREE ASSETS For Your Roblox Game"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=IeblIBmiPWI"
published: "2025-10-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits"]
---
# yt-IeblIBmiPWI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner video on sourcing free low-poly 3D asset packs for Roblox and importing them via File > Import 3D (FBX, extract zip first, scale down). Covers invisible collision borders from merged meshes and workarounds: separate leaf/trunk meshes, Render Fidelity Precise (weak), CanCollide off plus invisible cylinder parts. No Blender MCP, bpy, or Claude content; Blender only mentioned for editing .blend files.

## Claims
- c1: [0:41] Roblox Studio: File > Import 3D; asset zip must be extracted first; FBX chosen by speaker over OBJ. *(demo, high; blender-roblox-export-import)*
- c2: [2:41] Imported packs often arrive very large; speaker scales them down manually after import. *(demo, high; blender-roblox-export-import)*
- c3: [1:22] High-detail downloaded models may hit ~100,000 triangles; speaker believes Roblox limit is about 10k-15k triangles. *(opinion, low; mesh-texture-limits)*
- c4: [5:28] Invisible collision borders occur when multiple parts are merged into one mesh; small square-ish pieces are unaffected, large or tall merged meshes are affected. *(demo, medium; mesh-texture-limits)*
- c5: [6:09] Common fix from games: export leaves and branches as separate meshes and trunk as its own mesh, grouped into one model, to avoid invisible borders. *(opinion, medium; mesh-texture-limits)*
- c6: [6:50] Setting Render Fidelity to Precise helped only slightly for the invisible-border problem. *(demo, medium; mesh-texture-limits)*
- c7: [7:32] Workaround: set mesh CanCollide off, add an anchored, transparency-1 cylinder sized to the trunk, group it with the tree; player can brush against trunk but jumps pass through unless cylinder is taller. *(demo, high; mesh-texture-limits)*
- c8: [8:12] For rocks, turn CanCollide off on the mesh itself so players pass through the invisible border; apply such fixes before building the map to save time. *(demo, medium; mesh-texture-limits)*
- c9: [0:00] Free 3D asset packs are available from a browse-by-asset site with a Free/paid mix; the speaker bought a $10 pack for extra pieces and a $15 source .blend file option from one creator. *(experience, medium; automation-and-creator-workflows)*

## Numbers
- n1: **High-detail model triangle count**: ~100,000 
- n2: **Roblox triangle limit (speaker's belief)**: 10,000-15,000 
- n3: **Paid pack price (extra pieces)**: $10 
- n4: **Source .blend file price**: $15 
- n5: **Paid icon pack size and price**: ~3,000 icons, $20 

## Techniques
- t1: **FBX import into Studio**: Extract zip, File > Import 3D, shift-select FBX files, Import, then scale down oversized models and group them.
- t2: **Invisible collision cylinder**: Set mesh CanCollide off; add anchored cylinder part, transparency 1, sized to trunk; group with model; make taller to block jumps.
- t3: **Per-asset collision prep**: Before building the map, fix each tree/rock once (CanCollide off or add collider part), then copy-paste the fixed asset.

## Quotes (brief, for attribution)
> I forgot it does come in a zip folder. So, you do actually have to extract it first.  (at 2:41, Kingkade 3D)
> sometimes meshes have like this weird invisible border  (at 6:50, Kingkade 3D)
> do this before you start building your map  (at 8:12, Kingkade 3D)

## Points to
- it.io (asset site, as spoken in transcript)
- Roblox Studio File > Import 3D
