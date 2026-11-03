---
type: research-source
id: yt-SYR4oBiezbc
title: "Every Hair Deliberate: A Photoreal Cat in Hair Curves — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=SYR4oBiezbc"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-SYR4oBiezbc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Conference talk (BCON26) by VFX Greece on building a photoreal British Shorthair cat with Blender hair curves. Covers vertex-group region splits, clump/curl/freeze modifier order, texture-driven trim for fur splays, transparent BSDF with Light Path for dense-fur shadows, and a top-coat layer added after shading. No mention of Claude, blender-mcp, bpy, Roblox, FBX/glTF export, or UGC limits.

## Claims
- c1: Source is about fur grooming with Blender hair curves in Cycles; it does not address Claude, blender-mcp, bpy scripting, or Roblox export. *(doc, high; other)*
- c2: [6:56] Speaker recommends splitting fur into only two regions (head and body) via vertex group, citing reliability over texture paths. *(experience, medium; other)*
- c3: [11:20] Curl modifier also uses guide curves; disabling use-guide only on clump left curl producing an over-curled perm, fixed by disabling it on curl too. *(experience, medium; other)*
- c4: [14:01] Trim length driven by a texture instead of weight avoids polygon-count limits on split precision; requires manual wiring in Geometry Node editor. *(experience, medium; other)*

## Techniques
- t1: **Transparent BSDF + Light Path shadow tweak**: Mix transparent BSDF with Light Path to make dense-fur shadows slightly transparent rather than solid black; toggle viewport solid/rendered to refresh.
