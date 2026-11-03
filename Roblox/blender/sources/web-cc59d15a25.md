---
type: research-source
id: web-cc59d15a25
title: "Blender manual: scene_layout/object/editing/apply"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/scene_layout/object/editing/apply.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: high
tags: ["research-source", "web", "common-mistakes-fixes", "other", "procedural-generation", "rigging-animation", "roblox-export-settings"]
---
# web-cc59d15a25

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page on the Object > Apply menu: Transforms (Location/Rotation/Scale, with Corrective Flip Normals for negative scale), Transforms to Deltas, Animated Transform to Deltas, Visual Transform, Visual Geometry to Mesh/Objects, Make Instances Real, and Parent Inverse. Relevant to Roblox prep mainly for applying scale/rotation before export; no Roblox-specific content and no blender-mcp or bpy scripting details.

## Claims
- c1: Applying transforms resets Location/Rotation/Scale to 0/0/1 while the geometry is adjusted so the object looks unchanged; recommended before rigging and animation. *(doc, high; roblox-export-settings)*
- c2: Applying transforms to an object sharing Object Data with others requires making it Single User first; Blender prompts for confirmation. *(doc, high; common-mistakes-fixes)*
- c3: Applying transforms to armatures does not affect pose locations, animation curves, or constraints. *(doc, high; rigging-animation)*
- c4: Corrective Flip Normals option flips surface normals when applying a negative scale, preventing inverted shading. *(doc, high; common-mistakes-fixes)*
- c5: Transforms to Deltas moves Location/Rotation/Scale into delta transforms; existing deltas are added; Reset Values clears primary values. *(doc, high; roblox-export-settings)*
- c6: Visual Transform applies constraint results to the object's own transform so it stays in place if constraints are removed. *(doc, high; other)*
- c7: Visual Geometry to Objects creates new objects from evaluated geometry (modifiers, constraints, instancing) without modifying the original; instance attributes are not preserved. *(doc, high; procedural-generation)*
- c8: Make Instances Real on tens of thousands of instances (e.g. particles) can significantly slow Blender. *(doc, high; procedural-generation)*
- c9: Applying transforms affects how modifiers, constraints and parenting behave, since they depend on transform values. *(doc, medium; common-mistakes-fixes)*

## Numbers
- n1: **Scale reset value**: 1.0 (location and rotation reset to 0) 
- n2: **Apply shortcut**: Ctrl-A 

## Techniques
- t1: **Apply scale before export**: Select object, Object > Apply > Scale (or Rotation & Scale) so scale is 1.0 and rotation 0 before exporting; make data single-user first if shared.
- t2: **Negative scale fix**: When applying negative scale, keep Corrective Flip Normals enabled in the redo panel to avoid inverted shading.

## Quotes (brief, for attribution)
> Applying transforms resets an object's Location, Rotation, or Scale values while visually keeping the object in place.  (docs.blender.org)

## Points to
- https://docs.blender.org/manual/en/latest/scene_layout/object/editing/apply.html
