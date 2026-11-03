---
type: research-source
id: web-ce404af0d8
title: "Roblox docs: art/characters/manually-update-catalog-heads"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/manually-update-catalog-heads.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai"]
---
# web-ce404af0d8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for creators whose marketplace heads fail dynamic head validation. Steps: re-validate via a Studio command-bar script and glTF export, fix in Blender (import with Guess Original Bind Pose off, rotate 180, swap in Roblox cage template, remove vertex colors, keep rig with FACS-mapped blink/mouth/expressions), re-validate, upload as Development Item, then submit asset ID via web form. Not about blender-mcp or bpy.

## Claims
- c1: Roblox updated dynamic head validation parameters to let more existing catalog heads pass while still requiring all catalog heads to be dynamic. *(doc, high; avatar-ugc-accessories)*
- c2: Heads that fail validation can be fixed by deleting the original cage and fitting a Roblox-provided cage template with correct UV settings; the doc says this is usually faster than editing the original cage. *(doc, high; avatar-ugc-accessories)*
- c3: Head must have eyes that blink, mouth that opens and closes, and face expressions for happy and sad, mapped to the FACS standard. *(doc, high; avatar-ugc-accessories)*
- c4: Disable 'Guess Original Bind Pose' in the glTF import settings in Blender. *(doc, high; blender-roblox-export-import)*
- c5: Roblox Studio flips avatars 180 degrees on import; rotate the asset back 180 in Blender (R, Z, 180). *(doc, high; blender-roblox-export-import)*
- c6: Remove vertex color attributes (Data tab > Color Attributes) and vertex color shading nodes before FBX export, since Blender's FBX exporter rejects nodes between texture and shader. *(doc, medium; blender-roblox-export-import)*
- c7: Textures imported from glTF cannot be exported to FBX by default; save each image to disk locally as a workaround. *(doc, high; blender-roblox-export-import)*
- c8: Ensure Blender animation start value is set to 0 before export. *(doc, medium; blender-roblox-export-import)*
- c9: Export a head from Studio by running a command-bar Lua script using AssetService:GetBundleDetailsAsync and CreateHumanoidModelFromDescriptionAsync, then Save/Export as glTF with the glTF Export beta enabled. *(doc, high; automation-and-creator-workflows)*
- c10: Validation is checked by Save to Roblox > Avatar Item > Head and then canceling the publish to avoid fees; re-check after each fix. *(doc, high; automation-and-creator-workflows)*
- c11: Fixed heads are uploaded as a Development Item (Model category, Public privacy) to obtain an asset ID; the asset ID is then submitted via the web form linked in the notification email. *(doc, high; automation-and-creator-workflows)*
- c12: The web form requires date of birth per update and accepts multiple submissions; the last submission is used as final. *(doc, high; automation-and-creator-workflows)*
- c13: Body bundle updates are unnecessary when the head was published in a body bundle; only the head needs updating. *(doc, high; automation-and-creator-workflows)*
- c14: The source does not mention Claude, blender-mcp, or bpy scripting; it covers only manual Blender steps. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **rotation fix**: 180 degrees 

## Techniques
- t1: **Re-cage with Roblox template**: Delete original cage, pick the closest-shaped Roblox HeadCages template, align eye and mouth regions to head, re-validate.
- t2: **Head glTF round trip**: Export head glTF from Studio, import into empty Blender scene with Guess Original Bind Pose off, fix, export FBX (save images locally first).

## Quotes (brief, for attribution)
> Roblox recently updated the dynamic head validation parameters to allow more existing catalog heads to pass validation while still enforcing that all heads in the catalog are dynamic.  (create.roblox.com)

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/validate.md
- https://www.youtube.com/watch?v=OwhkWzSBnf0
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/caging-best-practices.md
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/assets/art/reference-files/HeadCages.zip
