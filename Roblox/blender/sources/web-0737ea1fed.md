---
type: research-source
id: web-0737ea1fed
title: "Roblox docs: art/accessories/creating/caging-setup"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/caging-setup.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 2
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "common-mistakes-fixes"]
---
# web-0737ea1fed

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on caging setup for clothing accessories in Blender: defines inner/outer cages, states only the outer cage needs adjusting when using cage templates, and lists outliner/wireframe steps to isolate the outer cage before sculpting. Does not cover blender-mcp, bpy scripting, or Claude.

## Claims
- c1: Caging defines a clothing item's inner cage (fits over body/existing clothing) and outer cage (receives layered clothing on top); both must be set for layering. *(doc, high; avatar-ugc-accessories)*
- c2: If clothing was made using cage templates as a mannequin, the inner cage usually needs no change; only the outer cage must be adjusted to fit the new item. *(doc, high; avatar-ugc-accessories)*
- c3: Caging workflow in Blender: switch to Object mode, hide armature, unhide LongSleeve_OuterCage, set LongSleeve to unselectable to avoid accidental edits. *(doc, high; avatar-ugc-accessories)*
- c4: Enable Wireframe in Object Properties for the active outer cage mesh to make it easier to visualize and select. *(doc, high; avatar-ugc-accessories)*
- c5: Editing the clothing mesh by accident is prevented by making the clothing object unselectable in the Outliner while working on the outer cage. *(doc, medium; common-mistakes-fixes)*

## Techniques
- t1: **Outer cage isolation in Blender**: Object mode; hide armature; unhide *_OuterCage; lock clothing mesh as unselectable; enable Wireframe on cage object properties; then sculpt outer cage to wrap clothing.

## Points to
- /art/accessories/creating/modify-cage
- /art/accessories/creating/test-poses
