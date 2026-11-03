---
type: research-source
id: web-fd09c3e820
title: "Roblox docs: art/characters/creating/caging"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/caging.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories"]
---
# web-fd09c3e820

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on caging a custom avatar head in Blender: adjust Head_OuterCage (wire display, symmetry on) to tightly wrap Head_Geo without deleting vertices, aligning the Head base with UpperTorso. Covers only head; other parts need their own _OuterCage. Does not cover bpy, blender-mcp, or Claude.

## Claims
- c1: Caging updates the avatar's cage mesh component so layered accessories and clothing can fit over sculpted head changes; default template cage must be adjusted to match sculpt. *(doc, high; avatar-ugc-accessories)*
- c2: Only the Head_OuterCage object needs adjusting for head-only changes; other body-part changes require adjusting their matching _OuterCage objects. *(doc, high; avatar-ugc-accessories)*
- c3: Never delete cage vertices or faces; destructive cage edits can cause import issues and prevent clothing and cosmetics from equipping. *(doc, high; avatar-ugc-accessories)*
- c4: Enable X-Axis symmetry and Topology Mirror in Edit mode so cage vertex edits stay symmetrical. *(doc, high; avatar-ugc-accessories)*
- c5: Set Head_OuterCage Object Properties > Viewport Display > Display As to Wire while fitting, then back to Solid to check intersections. *(doc, high; avatar-ugc-accessories)*
- c6: Verify a tight cage fit by moving cage vertices until the cage just covers Head_Geo with no Head_Geo geometry poking through solid cage sections. *(doc, high; avatar-ugc-accessories)*
- c7: Base of Head cage must align with top of UpperTorso cage. *(doc, high; avatar-ugc-accessories)*
- c8: For many-part body changes, the provided Blender Cage Template includes a full-body std_cage_deformable helper mesh that propagates vertex changes to all body-part cages. *(doc, medium; avatar-ugc-accessories)*

## Techniques
- t1: **Head cage fitting in Blender**: Hide all objects except Head_OuterCage and Head_Geo; set cage Display As Wire; enable X symmetry and Topology Mirror; G-grab vertices to hug head; set Solid and fix intersections.
- t2: **Full-body cage via template**: Use Blender Cage Template .blend with std_cage_deformable helper to push vertex changes to all body-part cages at once.

## Quotes (brief, for attribution)
> Do not delete any vertices or faces of the provided cages. Destructive modification of the cages can cause import issues and prevent the character model from equipping clothing and cosmetics.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/character-bodies#cage-meshes
- Body_Cage_Templates.zip
- 3_Goblin-caged.blend
