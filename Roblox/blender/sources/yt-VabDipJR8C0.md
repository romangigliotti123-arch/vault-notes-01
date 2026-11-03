---
type: research-source
id: yt-VabDipJR8C0
title: "APX & AVX10: The Next Evolution of x86 — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=VabDipJR8C0"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 0
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-VabDipJR8C0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Intel BCON26 talk on x86 APX (16 extra GPRs, push2/pop2, conditional compare/cmov, data destination) and AVX10 unified 512-bit vector ISA, using Embree ray tracing (used by Blender Cycles) as the example. Nothing on Claude, blender-mcp, bpy, Roblox export, mesh/texture limits, rigging, or UGC accessories.

## Claims
- c1: Talk covers CPU instruction-set extensions APX and AVX10, not Blender-to-Roblox workflows, Claude, or bpy scripting. *(doc, high; other)*
- c2: [0:52] APX adds 16 general-purpose registers (R16 to R31) to reduce register spilling in complex functions. *(demo, high; other)*
- c3: [16:17] AVX10.1 unifies the 512-bit AVX512 feature set into one versioned ISA, replacing per-feature runtime checks. *(doc, high; other)*
- c4: [18:12] APX/AVX10 hardware is slated for Nova Lake P and E cores, beginning of next year; prototypes exist now. *(doc, medium; other)*
- c5: [21:48] Speaker's ballpark when asked about Blender speedup was 5x, and the white paper claims about 10% average across workloads; opinion/unclear. *(opinion, low; other)*

## Numbers
- n1: **GPR count**: 16 added (R16 to R31); x86-64 has 16 
- n2: **ICX compiler version**: 2026.2 supports APX/AVX10 
- n3: **Claimed average workload gain**: 10% per white paper (speaker quote, not verified) 

## Points to
- Intel Embree (ray tracing library, used by Blender Cycles)
- APX white paper (QR code, not in transcript)
- AVX10 specification (not in transcript)
