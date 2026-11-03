---
type: research-source
id: yt-x7-x4Oy645M
title: "Intro to 3D Modeling and Building Your First Map (feat. harht & Krissy3D) | Inspire 2026"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=x7-x4Oy645M"
published: "2026-07-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0060
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-x7-x4Oy645M

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Inspire 2026 beginner workshop on building maps: references, gray boxing in Studio, replacing gray boxes with final models, lighting. Blender is mentioned only as a free modeling tool. No blender-mcp, Claude, bpy, or FBX/glTF export content. Useful only for scale-matching and organization habits.

## Claims
- c1: [6:54] Presenters say Blender is free and widely used in the Roblox community; they describe its UI as streamlined and beginner-friendly. *(opinion, high; other)*
- c2: [7:37] Team prefers Blender because alternatives 3ds Max, Maya, and ZBrush are paid; ZBrush is described as a sculpting tool. *(opinion, medium; other)*
- c3: [8:19] Presenter says some builders sculpt in ZBrush and bake the results onto Blender models; no steps or settings given. *(experience, low; other)*
- c4: [27:28] Dresser Impress rig is noticeably larger than a normal Roblox rig; builders drag a rig into the map to check door and lamp sizes. *(experience, medium; rigging-animation)*
- c5: [40:35] When importing a model to Blender, keep the same scale and do not change proportions; otherwise the model comes out very large. *(experience, medium; blender-roblox-export-import)*
- c6: [41:16] Optimization target stated as running above 60 FPS; disable cast shadows and near collisions on parts players never touch. *(opinion, medium; mesh-texture-limits)*
- c7: [56:15] Unions are described as potentially unperformant; presenter says Roblox now stores them as meshes with adjustable triangle rendering, so they are better than before. *(opinion, low; mesh-texture-limits)*
- c8: [30:53] Archimedes plugin creates curves quickly; example used a 45-degree angle to build a lighthouse base shape. *(demo, medium; other)*
- c9: [1:03:08] Summer update build had a two-week timeframe, so the team used fewer and larger gray-box blocks. *(experience, medium; other)*
- c10: [38:29] Name and group parts into folders in Workspace (e.g., furniture folder, lamp model names) so large maps stay searchable across frequent updates. *(experience, high; automation-and-creator-workflows)*
- c11: [44:02] Team organizes assets into clear folder structures; parent folders like furniture hold related models for quick access. *(experience, high; automation-and-creator-workflows)*

## Numbers
- n1: **target frame rate**: over 60 fps presenter's performance guideline for Studio builds
- n2: **Archimedes curve angle**: 45 degrees angle used for lighthouse base curve
- n3: **summer build timeframe**: two weeks time to build a large summer map

## Techniques
- t1: **Scale check against rig**: Place a rig or avatar dummy in the Studio map next to the model. Compare door, lamp, and furniture sizes against it. Recolor the dummy to check visibility under different lighting.
- t2: **Gray box then replace**: Build a rough gray-box layout with simple parts and correct scale. Replace each block with a final model while preserving the gray box's scale and proportions. Compare back to the gray box as you go.
- t3: **Group parts into models**: Select related parts and group them into a Model named for its purpose (e.g., base, grass, light) so the Explorer stays searchable.

## Quotes (brief, for attribution)
> if you were to import this door to Blender, you want to keep the same scale and not change any like proportions  (at 40:35, Roblox Creators)

## Points to
- Pure Ref
- Blender
- F3X plugin
- Archimedes plugin
- Forsaken (game referenced for shape language)
- Dress To Impress
