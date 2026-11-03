---
type: research-source
id: yt-cjRYWLQDwAA
title: "BBC’s 'Crongton' - From design to realization — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=cjRYWLQDwAA"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-cjRYWLQDwAA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Roblox. BCON26 talk on BBC's 'Crongton' (Factory Fifteen) using Blender Grease Pencil, Eevee and a template .blend pipeline, with Maya for character animation exported via Alembic. No blender-mcp, bpy, Claude, Roblox export, or mesh/texture limits covered. Only a generic template-file workflow is loosely relevant.

## Claims
- c1: [20:32] Studio reused a pre-built Blender template file: animation imported via Alembic into collections, with line-art objects auto-picking up objects in those collections, so shots were not rebuilt. *(experience, medium; automation-and-creator-workflows)*
- c2: [21:14] Render output nodes and scene states were preset in the template so artists only chose a save location and rendered, per the speaker. *(experience, medium; automation-and-creator-workflows)*
- c3: [19:08] Pipeline kept Maya for character setup because most animators were trained in Maya; Blender used for staging, lighting, line art and rendering. *(experience, medium; automation-and-creator-workflows)*
- c4: [24:22] Eevee rendered backlit shadow-puppet shots quickly; speaker described it as lightning fast, no timing given. *(opinion, low; other)*

## Techniques
- t1: **Alembic handoff into template .blend**: Export animated character as Alembic, import into prebuilt template scene, split character into body-part objects placed in existing collections so line-art objects auto-apply.
