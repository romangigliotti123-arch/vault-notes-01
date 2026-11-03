---
type: research-source
id: web-a7e1bdb3ea
title: "Roblox docs: art/accessories/creating-rigid/modeling-setup"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating-rigid/modeling-setup.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "creator-workflows", "other", "roblox-mesh-limits"]
---
# web-a7e1bdb3ea

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator-docs tutorial for box-modeling a rigid accessory (treasure chest) in Blender by hand: block out a cube, bevel a rounded lid, merge vertices, inset and extrude sides, loop-cut the front, then close the metal border. No scripting, Claude, or MCP content. Useful only as a modeling reference for rigid accessories.

## Claims
- c1: Doc says the steps are based on the Roblox DevForum 'Box Modeling 101' staff article; manual modeling only, no scripting or automation. *(doc, high; creator-workflows)*
- c2: Doc warns to keep geometry within a polycount budget per the rigid accessory specifications page. *(doc, high; roblox-mesh-limits)*
- c3: Bevel can leave near-duplicate vertices unmerged; doc fixes this with Merge Vertices by Distance at 0.01. *(doc, high; common-mistakes-fixes)*
- c4: Rounded lid made by selecting top front and back edges, Ctrl+B bevel with 6 segments and Clamp Overlap enabled. *(doc, high; other)*
- c5: Lid extruded to about half the height of the main body in the General Shape step. *(doc, medium; other)*
- c6: Horizontal loop-cut lines are straightened by scaling Z to 0, and bottom line is snapped with Magnet Snapping to existing vertices. *(doc, high; other)*
- c7: Missing border faces are closed with New Face from Edges after deleting the top metal border faces. *(doc, high; other)*
- c8: Doc says policy checks apply: avoid infringing other creators' IP inside and outside Roblox. *(doc, high; other)*

## Numbers
- n1: **bevel segments**: 6 Rounded lid bevel on top front and back edges, Clamp Overlap on
- n2: **merge distance**: 0.01 Merge Vertices by Distance after bevel
- n3: **vertical loop cuts**: 2 Front insets, scaled along Y toward chest edges
- n4: **horizontal loop cuts**: 2 Straightened with Z scale 0
- n5: **lid height**: about half body height Top extrude amount

## Techniques
- t1: **Box modeling a chest**: Scale cube with S then Y; extrude top face with E; bevel top edges Ctrl+B with 6 segments; inset side faces I and extrude along normals.
- t2: **Merge by distance**: A to select all vertices, right-click, Merge Vertices by Distance, set 0.01 to share vertices after bevel.
- t3: **Loop cut then straighten**: Ctrl+R loop cut, set cut count 2, scale line on axis (S then Z, 0) to flatten, then Magnet Snap to vertices.
- t4: **Close border gaps**: Delete border faces, shift-select two corner edges, right-click New Face from Edges.

## Points to
- https://devforum.roblox.com/t/modeling-101-in-blender-box-modeling/2963814
- ../../../avatar/rigid-accessories/specifications.md
- ../../../marketplace/marketplace-policy.md
- ../../../assets/art/accessories/creating-rigid/Chest-Modeling-Complete.blend
