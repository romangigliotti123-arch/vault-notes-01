---
type: research-source
id: web-325bdbe8aa
title: "Roblox docs: art/characters/creating/final-checks"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/final-checks.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0006
relevance: 1
density: low
tags: ["research-source", "web", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-325bdbe8aa

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page "Final checks" for character models, a pre-export checklist. It covers removing extra mesh objects, removing stray animation data (extra keyframes, saved poses unrelated to facial animation), and verifying geometry, rig, and textures against avatar technical specifications. Not specific to Blender, Claude, or bpy.

## Claims
- c1: Before export, remove mesh objects that are not part of the character model geometry from the project. *(doc, high; blender-roblox-export-import)*
- c2: Remove extra animation data such as additional keyframes or saved poses/orientations not related to original facial animation data before export. *(doc, high; rigging-animation)*
- c3: Geometry, rig, and textures must be checked against the avatar technical specifications before exporting. *(doc, high; mesh-texture-limits)*

## Techniques
- t1: **Pre-export cleanup checklist**: Remove non-character mesh objects; strip extra keyframes and saved poses not tied to original facial animation; verify geometry, rig, and textures against avatar specs before exporting.

## Points to
- /avatar/character-bodies/specifications.md
- /art/characters/creating/export-textures
- /art/characters/creating/verify-attachments
