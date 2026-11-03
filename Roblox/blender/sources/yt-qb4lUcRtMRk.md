---
type: research-source
id: yt-qb4lUcRtMRk
title: "How To Change The TEXTURE in Roblox Rigs Suite (Blender Roblox GFX)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=qb4lUcRtMRk"
published: "2025-05-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 3
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "roblox-export-settings", "texturing-baking-uv"]
---
# yt-qb4lUcRtMRk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short tutorial on getting clothing textures into a Roblox Rigs Suite blocky rig in Blender. Method: dress a blank R6/R15 avatar in Roblox Studio via Rig Builder, using classic shirt/pants asset IDs, centre HumanoidRootPart at 0,3,0, export selection as .obj, then use the exported texture in Blender's Material Settings. Accessories import as OBJ split by group and attach via Attach Accessories tool or Child Of constraint.

## Claims
- c1: [0:00] Clothing is not taken from the Roblox catalog into Blender; the clothing texture is taken from a character model exported out of Roblox Studio. *(demo, medium; avatar-ugc-accessories)*
- c2: [1:22] Classic shirts/pants are added in Studio by pasting the asset ID into the Shirt Template or Pants Template property. *(demo, high; avatar-ugc-accessories)*
- c3: [2:02] Set HumanoidRootPart CFrame position to 0,3,0 before export so the model sits on the baseplate origin and does not land elsewhere in the Blender scene. *(demo, medium; roblox-export-settings)*
- c4: [2:02] Export the character via right-click Export Selection, saved as a file named data in a project folder. *(demo, medium; roblox-export-settings)*
- c5: [2:44] In Roblox Rigs Suite, the texture is changed under Material Settings on the selected rig, using the texture from the exported model. *(demo, high; texturing-baking-uv)*
- c6: [2:44] Switching to Material view in Blender can be slow because Eevee shaders must compile first. *(experience, medium; common-mistakes-fixes)*
- c7: [2:44] Accessories are imported as .obj (must be split by group) and attached with the Attach Accessories tool, parenting, or a manual Child Of constraint. *(demo, high; avatar-ugc-accessories)*
- c8: [1:22] Load Catalog Items plugin is the author's recommended way to add catalog accessories to a rig in Studio. *(opinion, low; avatar-ugc-accessories)*

## Numbers
- n1: **HumanoidRootPart position**: 0,3,0 Centres rig on baseplate before export
- n2: **Rig types supported by Rigs Suite**: R6 and R15 Author uses R6 block avatar; R15 also supported

## Techniques
- t1: **Export clothed blank avatar as texture source**: Open baseplate, Avatar > Rig Builder, add blank avatar, add Shirt/Pants with asset ID, move HumanoidRootPart to 0,3,0, right-click Export Selection, save as data.obj-style file.
- t2: **Apply exported texture in Rigs Suite**: Import Blocky Rig in Roblox Rigs Suite, select rig, open Material Settings, pick texture from exported model folder, check Material view.

## Quotes (brief, for attribution)
> You don't do that. What you do instead is you put it in Roblox Studio, save the character model from Roblox Studio, and then put the texture from that model in Blender.  (at 0:00, Comix Productions)
> you can add in your accessories by importing your model as a wavefront (.obj). (make sure it's split by group!)  (at 2:44, Comix Productions)

## Points to
- Load Catalog Items plugin (author's Discord/description link)
- Roblox Rigs Suite (Blender addon)
