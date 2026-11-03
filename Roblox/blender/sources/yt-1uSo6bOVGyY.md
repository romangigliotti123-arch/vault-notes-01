---
type: research-source
id: yt-1uSo6bOVGyY
title: "COMPOSITOR 🫶 SEQUENCER — Blender Today LIVE #266"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=1uSo6bOVGyY"
published: "2025-09-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0075
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-1uSo6bOVGyY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today Live #266 (2025-09-30) recaps Blender 5.0 beta-cycle changes: compositor, sequencer, geometry nodes, UI. It does not cover Roblox, blender-mcp, Claude, or bpy scripting. Only tangential pipeline notes: 5.0 files break backward compatibility, 4.5 LTS is the bridge, and portable installs keep versions separate.

## Claims
- c1: [1:12:33] Blender 5.0 files saved with 5.0 cannot open in older versions; 4.5 LTS is the bridge for opening them in older Blender. *(doc, high; other)*
- c2: [1:14:28] Render pass renames in 5.0 (e.g., Emit to emission, AO to ambient occlusion) break compositing setups and add-on scripts relying on old names. *(doc, high; other)*
- c3: [1:54:37] Portable Blender zip installs each keep their own folder, so add-ons in a 5.x install do not affect older versions. *(opinion, medium; other)*
- c4: [0:43] Blender 5.0 release date stayed 11 November 2025; beta started 8 October; one-week release candidate precedes release. *(doc, medium; other)*
- c5: [2:02:16] Release timing depends on bug report volume; the speaker asks users to report crashes and bugs during beta. *(opinion, low; other)*

## Numbers
- n1: **Blender 5.0 beta start**: 8 Oct 2025 (one month before 11 Nov release) 
- n2: **Blender 5.0 release date**: 11 Nov 2025 
- n3: **Changes in this release cycle**: about 400 this week 

## Quotes (brief, for attribution)
> Blender 5.0 ... render pass names changed; set passes will lose links for reading compositing node setups, use 4.5 LTS to fix it.  (at 1:12:33, Blender)

## Points to
- blender.org/projects (5.0 release page)
- flamenco.blender.org
- Blender Development Fund
- Blender Extensions platform
