---
type: research-source
id: web-6bbd7a95af
title: "Roblox docs: avatar/dynamic-heads/caging-best-practices"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/caging-best-practices.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "other"]
---
# web-6bbd7a95af

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs on dynamic head caging for avatar faces: equidistant geometry, vertex-colored alignment zones (lips, brows, hairline), tight cage without intersecting render mesh, neck alignment for HSR, eye/brow/mouth/nose/ear vert placement, and proportion rules for missing features. No Blender, bpy, Claude, or export-pipeline content.

## Claims
- c1: Dynamic head cage defines the head surface and plays a key role in Marketplace head validation; cage must be built accurately for accessory fit and animation. *(doc, high; avatar-ugc-accessories)*
- c2: Keep cage geometry equidistant where possible to mitigate texture and layered accessory distortion; doc notes this isn't always possible. *(doc, high; avatar-ugc-accessories)*
- c3: Cage should sit barely outside the render mesh without intersecting it; tight fit improves layered accessory fit and makeup transfer accuracy. *(doc, high; avatar-ugc-accessories)*
- c4: Cage neck part should line up closely to render mesh; this lets Hidden Surface Removal (HSR) hide underlying surface under layered accessories. HSR is disabled on head but not on body at neck. *(doc, high; avatar-ugc-accessories)*
- c5: Eyes: use three verts on upper eyelid and three on lower eyelid, equidistant; enclose open eye edge up to the eye mesh. *(doc, high; avatar-ugc-accessories)*
- c6: Mouth: outline outside and inside of lips; green vertex color on upper lip, purple on lower lip, equidistant spacing. *(doc, high; avatar-ugc-accessories)*
- c7: Nose bridge starts at inner eyes and ends two faces above the lips. *(doc, medium; avatar-ugc-accessories)*
- c8: Ears: top established by triangle portion of ear, bottom by quad; keep hairline shape around ear. *(doc, medium; avatar-ugc-accessories)*
- c9: Template includes vertex-colored areas at lips, eyebrows, hairline; align these for makeup transfer and hair/eyebrow/eyelash accessory fit. Non-vertex-colored areas (nose, eyes, ears) also need alignment. *(doc, high; avatar-ugc-accessories)*
- c10: Missing features guidance: face split into thirds (hairline-eyebrows, eyebrows-nose bottom, nose bottom-chin); eyes halfway down head; head about five eyes wide; tear ducts align with nostril edges; mouth corners align with pupils. *(doc, medium; avatar-ugc-accessories)*
- c11: Eyebrows: place three upper and three lower verts equidistant after establishing head and tail; missing eyebrows placed by facial proportion rules. *(doc, medium; avatar-ugc-accessories)*
- c12: Source is Roblox web docs on face/head caging for character creators; it does not cover Blender, bpy, blender-mcp, Claude, FBX/glTF export, or MeshPart import. *(doc, high; other)*

## Numbers
- n1: **eyelid vertex count**: 3 upper, 3 lower equidistant verts per eyelid
- n2: **head width**: about five eyes wide missing-feature proportion guidance
- n3: **face vertical thirds**: 3 equal parts hairline-brows, brows-nose bottom, nose bottom-chin
- n4: **nose bridge end**: two faces above lips nose bridge termination

## Techniques
- t1: **Tight cage fit**: Place cage close to render mesh without intersecting; use lower-res cage topology; align neck cage part near render mesh for HSR.
- t2: **Vertex-color alignment**: Align cage edges to template vertex-colored zones (lips, brows, hairline) and non-colored features (nose, eyes, ears).

## Quotes (brief, for attribution)
> The cage needs to be close to the render mesh without actually intersecting it.  (create.roblox.com)
> This ensures that HSR (Hidden Surface Removal) can accurately hide the underlying surface when layered accessories are worn on top.  (create.roblox.com)

## Points to
- https://create.roblox.com (head validation: ./validate.md)
- Layered accessory caging best practices (../layered-accessories/caging-best-practices.md)
