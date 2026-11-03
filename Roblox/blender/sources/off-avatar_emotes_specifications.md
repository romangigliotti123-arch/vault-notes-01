---
type: research-source
id: off-avatar_emotes_specifications
title: "Roblox Creator Docs: avatar_emotes_specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/emotes/specifications"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "rigging-animation"]
---
# off-avatar_emotes_specifications

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs spec page for emotes. An emote is an Animation object with AnimationId set to an uploaded animation asset; no meshes or textures needed. Lists validation requirements: under 10 seconds, root joint limited drift, speed threshold, standard R15 rig only (advanced R15 in closed beta), animation sourced from CurveAnimation, and Community Standards compliance. Little Blender-specific content.

## Claims
- c1: Emotes must be under 10 seconds to pass Marketplace validation. *(doc, high; rigging-animation)*
- c2: Emote animation data must reference a standard R15 rig; advanced R15 rigs are in closed beta for emotes. *(doc, high; rigging-animation)*
- c3: Emote animation must be sourced from a CurveAnimation; the docs point to Import emotes > Generate asset ID for conversion. *(doc, high; rigging-animation)*
- c4: An emote needs only an Animation object with AnimationId set to the animation asset ID; meshes and textures are not required for Marketplace upload. *(doc, high; automation-and-creator-workflows)*
- c5: Validation also checks that the root joint stays near its starting position and that per-frame movement speed stays under a threshold (no numeric values given). *(doc, medium; rigging-animation)*

## Numbers
- n1: **max emote length**: < 10 seconds Emotes must be less than 10 seconds before Marketplace upload

## Quotes (brief, for attribution)
> The Animation object is the only component required to upload an emote to the Marketplace because animations do not require meshes, textures, or other 3D art components.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://devforum.roblox.com/t/upload-and-publish-for-emotes-with-additional-joints-is-now-open/4710932
- https://create.roblox.com/docs/avatar/emotes/import
