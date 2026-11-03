---
type: research-source
id: web-6efeca2001
title: "DevForum thread 3784307"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/3784307"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 2
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "other", "rigging-animation", "roblox-export-settings"]
---
# web-6efeca2001

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum Q&A from June 2025. A creator wants to export a Roblox character to Blender, reshape limbs, and re-import without breaking rig, scale, or mesh. Reported failures: OBJ/FBX exports from Studio lose rigging or cause Blender import issues, and proportions distort. No working method is given. A reply suggesting per-limb export and re-rigging in Studio was rejected by the poster. Little actionable content; no blender-mcp or bpy details.

## Claims
- c1: Poster reports OBJ and FBX exports from Roblox Studio either strip rigging or cause import issues in Blender. *(experience, medium; roblox-export-settings)*
- c2: Poster reports meshes lose original proportions and distort after the Studio-to-Blender-to-Studio roundtrip. *(experience, medium; common-mistakes-fixes)*
- c3: Poster reports rigs end up misaligned or unusable after re-import into Roblox. *(experience, medium; rigging-animation)*
- c4: Suggested workaround of exporting each limb separately and re-rigging inside Roblox Studio was rejected by the poster as flawed; no specifics given. *(experience, low; common-mistakes-fixes)*
- c5: Thread contains no confirmed solution; the referenced YouTube method is described only as not delivering clean, editable rigs. *(experience, medium; other)*

## Quotes (brief, for attribution)
> The exports I've tested either lose critical structure, distort the mesh, or break the rigging entirely.  (devforum.roblox.com)

## Points to
- https://www.youtube.com/watch?v=5V8IwJNPlqw
