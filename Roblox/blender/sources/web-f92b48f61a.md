---
type: research-source
id: web-f92b48f61a
title: "Roblox docs: avatar/dynamic-heads/test"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/test.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# web-f92b48f61a

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on testing dynamic heads in Studio: import a character model with a dynamic head, optionally import face accessories as MeshParts and convert them to Accessories with the Accessory Fitting Tool, then animate via the generated FaceControls. Lists FBX head import error and warning messages. Little direct Blender content; relevant mainly to FBX head import requirements.

## Claims
- c1: Importing a dynamic head model into Studio creates a FaceControls instance; facial Bones of the head mesh cannot be accessed directly in Studio. *(doc, high; blender-roblox-export-import)*
- c2: Face accessories import as MeshPart by default and must be converted to Accessory via the Accessory Fitting Tool (Avatar tab > Accessory, Clothing category > Face) to work with a dynamic head. *(doc, high; avatar-ugc-accessories)*
- c3: WrapLayer.AutoSkin options: Disabled (default), EnabledOverride (replaces existing skinning), EnabledPreserve (keeps existing skinning, creates new skinning only if none exists). *(doc, high; avatar-ugc-accessories)*
- c4: Character-specific face accessories can only be equipped on their designed character; accessories can be saved to Toolbox and reused by asset ID. *(doc, medium; avatar-ugc-accessories)*
- c5: FBX head error: Head_Geo must have Extra Attributes mapping FACS controls to animation frames, otherwise facial expressions do not animate. *(doc, high; rigging-animation)*
- c6: Correctives can combine at most 3 control names; a corrective with more than 3 poses is unsupported and must be deleted. *(doc, high; rigging-animation)*
- c7: Extra attributes must be named Frame0, Frame1, etc.; each FACS pose or corrective may map to only a single frame; one frame must be set to Neutral. *(doc, high; rigging-animation)*
- c8: Every joint must have a unique name; duplicate joint names produce a 'Found more than one joint named X' error. *(doc, high; rigging-animation)*
- c9: A corrective requires all its base poses to be set in extra attributes (e.g., Funneler_JawDrop requires Funneler and JawDrop poses). *(doc, high; rigging-animation)*
- c10: Warning: a 3-corrective without its base 2-corrective imports but may deform oddly; defining only a subset of base poses yields a warning that the character may not express itself. *(doc, medium; rigging-animation)*
- c11: Unrecognized FACS control names must be renamed to standard FACS poses; 'Neutral cannot be part of a corrective'. *(doc, high; rigging-animation)*
- c12: Animate heads in the Animation Editor by adding individual tracks or using the Face Animation Editor; quick preview available via Avatar Setup presets. *(doc, medium; rigging-animation)*

## Numbers
- n1: **max poses per corrective**: 3 Studio rejects correctives with more than 3 control names
- n2: **Head_Geo extra attribute naming**: Frame0, Frame1, ... Required format for frame mapping attributes

## Techniques
- t1: **Convert MeshPart face accessory to Accessory**: Import mesh via Importer; open Avatar > Accessory (AFT); select MeshPart; Next; Clothing > Face; optionally adjust in Edit; preview; Next to create Accessory. Optionally enable WrapLayer.AutoSkin.
- t2: **Test head animation in Studio**: Import character model with dynamic head; use generated FaceControls properties in Animation Editor to pose or animate expressions.

## Points to
- https://create.roblox.com/docs/avatar/dynamic-heads/test
- https://create.roblox.com/docs/art/characters/facial-animation/animate-heads
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/avatar/dynamic-heads/facs-poses-reference
