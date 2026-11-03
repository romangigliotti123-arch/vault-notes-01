---
type: research-source
id: web-da2f0a3fc4
title: "the ultimate guide to buying a computer for blender"
source_type: "web"
creator: "www.blenderguru.com"
url: "https://www.blenderguru.com/posts/the-ultimate-guide-to-buying-a-computer-for-blender"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 0
density: low
tags: ["research-source", "web", "other"]
---
# web-da2f0a3fc4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
2013 BlenderGuru post on buying a PC for Blender's Cycles renderer, written by Andrew Price. Covers GPU (Nvidia only, VRAM matters), CPU core count, RAM as the limit on scene and texture size, case cooling, and RAID 1 backups. Nothing on Claude, blender-mcp, bpy, Roblox export, mesh/texture limits for Roblox, rigging, or UGC. Outdated hardware advice.

## Claims
- c1: Nvidia is the only GPU brand that works with Cycles; AMD/ATI cards are unusable with Cycles per developers citing AMD driver limits. *(opinion, low; other)*
- c2: GPU VRAM caps scene complexity: render crashes on large textures/geometry, forcing fallback to slower CPU rendering. *(opinion, medium; other)*
- c3: Dual GPUs reportedly increase Cycles render times by 1.6x, but memory stays limited to a single card. *(opinion, low; other)*
- c4: RAM sets the ceiling on large image textures and high-res simulations; out of RAM means Blender crashes. *(opinion, medium; other)*
- c5: Hard drive speed makes no noticeable difference in Blender; author recommends RAID 1 mirroring for backup. *(opinion, medium; other)*
- c6: Standard PC cases overheat during long renders; gaming cases with better cooling are recommended. *(experience, medium; other)*

## Numbers
- n1: **Dual-GPU render speedup**: 1.6x (reported) Cycles dual cards; memory not pooled
- n2: **CPU tiles rendered in parallel**: 8 (8-core CPU) Blender renders one tile per core
- n3: **Fluid domain resolution example**: 100 at 2GB RAM vs 200 at 16GB Anecdotal sim limit by RAM
- n4: **Author PC (2013)**: i7 950, 12GB RAM, GTX 470 1280MB, 2x1TB RAID 1 Personal spec list, now obsolete
- n5: **Benchmark thread length**: 42 pages Cycles benchmark forum thread, dated 2013

## Techniques
- t1: **RAID 1 mirroring for data safety**: Buy two identical hard drives and configure RAID 1 in BIOS so one drive failure leaves a mirror copy.

## Quotes (brief, for attribution)
> The brand I recommend is Nvidia, because that's actually the only brand that currently works with Cycles.  (www.blenderguru.com)
> You can only go as far as your RAM.  (www.blenderguru.com)

## Contradictions flagged
- AMD/ATI cards are dead in the water for Cycles. (vs Current Blender releases support AMD GPUs for Cycles (outside knowledge, not in source; low confidence).)

## Points to
- Blender Cycles GPU FAQ (blenderguru)
- Cycles Benchmark forum thread
- 4 Easy Ways to Speed Up Cycles (blenderguru)
- 13 Ways to Reduce Your Render Times (blenderguru)
