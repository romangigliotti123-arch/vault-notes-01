---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i79
title: "Roblox/roblox-blender-plugin#79 No textures?"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/79"
published: "2025-02-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 3
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits"]
---
# gh-Roblox-roblox-blender-plugin-i79

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #79 on Roblox/roblox-blender-plugin (Feb 2025): imported mesh works but textures do not come through and no texture ID appears. Maintainer itsfrank says Roblox importers do not support all Blender material setups and points to a DevForum PBR shader-setup guide. A commenter says a fix exists, but the text cuts off before it is given. No reproduction result is shown.

## Claims
- c1: Roblox Blender plugin imports geometry correctly but may import no textures and produce no texture ID for some .blend files. *(doc, medium; blender-roblox-export-import)*
- c2: Maintainer itsfrank says Roblox importers do not support all possible Blender material/texturing options. *(doc, medium; blender-roblox-export-import)*
- c3: Roblox PBR import, added with the Unified Smart Mesh Importer beta, requires Blender shaders set up in a specific way; a DevForum post (1735648) has a how-to for common tools. *(doc, medium; mesh-texture-limits)*
- c4: Related issue #74 suggests textures can upload, but incorrectly in that case. *(doc, low; blender-roblox-export-import)*
- c5: Commenter DaytimeDev's suspected cause is a guess; the workaround they describe is cut off in the source and not shown. *(opinion, low; blender-roblox-export-import)*
- c6: Reporter says they had not done Roblox game development for about two years and suspected a user-side mistake; the reproduction .blend was shared via Google Drive after a private-link fix. *(experience, low; automation-and-creator-workflows)*

## Numbers
- n1: **issue number**: #79 Roblox/roblox-blender-plugin, dated 2025-02-25
- n2: **related issue**: #74 cited as evidence textures can upload
- n3: **DevForum topic id**: 1735648 PBR support for Unified Smart Mesh Importer beta, shader setup guide

## Techniques
- t1: **Follow the PBR shader setup guide**: Check the DevForum PBR guide section 'how to set up the shaders properly in common tools' and rebuild the Blender material to match the supported node setup before exporting.
- t2: **Share a minimal repro .blend**: Share the file with link access (not private) or DM it so maintainers can reproduce a texture-import failure.

## Quotes (brief, for attribution)
> Roblox importers don't support all possible material/texturing options in Blender.  (Roblox)
> The importing works perfectly, however no texture gets imported at all? There is no texture ID?  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/74
- https://devforum.roblox.com/t/pbr-support-for-the-unified-smart-mesh-importer-beta/1735648#how-to-set-up-the-shaders-properly-in-common-tools-1
