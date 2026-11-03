---
type: research-source
id: web-21daf6242f
title: "Roblox docs: art/accessories/creating/modeling-setup"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/modeling-setup.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 4
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "common-mistakes-fixes", "creator-workflows", "texturing-baking-uv"]
---
# web-21daf6242f

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for Blender modeling setup of layered clothing. Uses the Clothing_Cage.blend template: duplicate the InnerCage as a clothing base mesh, clean the parent and naming, and remove helper vertex colour attributes (colorSet1) that could clash with textures in Studio. Next steps cover trimming, smoothing, fitting, sculpting, and watertight closing.

## Claims
- c1: Roblox's Clothing_Cage.blend template includes InnerCage and OuterCage mesh objects used as temporary mannequins for clothing modeling. *(doc, high; avatar-ugc-accessories)*
- c2: Duplicate the InnerCage object, clear parent with Clear and Keep Transformation, delete extra 'Clothing Cages.001', rename copy to LongSleeve, rename cages to LongSleeve_OuterCage/InnerCage and hide them. *(doc, high; avatar-ugc-accessories)*
- c3: Cage template meshes carry helper vertex colour attributes (colorSet1) that must be removed from the clothing mesh because they may clash with the texture after import into Studio. *(doc, high; common-mistakes-fixes)*
- c4: Remove colorSet1 via Object Data Properties > Color Attributes > minus button. *(doc, high; texturing-baking-uv)*
- c5: Modeling workflow steps: base mesh setup, clear attributes, trim to clothing type, smooth vertices, scale and position onto mannequin, sculpt fabric details, close holes to make watertight. *(doc, medium; creator-workflows)*
- c6: Same cage-trim-sculpt technique is described as applicable to pants, skirts and shoes, not only t-shirts. *(doc, medium; avatar-ugc-accessories)*

## Techniques
- t1: **Cage-based layered clothing setup**: Open Roblox Clothing_Cage.blend, Save As new project, duplicate InnerCage, clear parent keeping transform, rename to LongSleeve, hide original cages.
- t2: **Remove helper color attributes**: Select LongSleeve, Object Data Properties > Color Attributes, select colorSet1, press minus.

## Quotes (brief, for attribution)
> remove extra attribute data ... vertex colors may clash with the texture of the object after importing in Studio  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/accessories/creating/trimming
- Clothing_Cage_Templates.zip
