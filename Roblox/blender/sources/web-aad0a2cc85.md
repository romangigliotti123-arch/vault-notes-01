---
type: research-source
id: web-aad0a2cc85
title: "Roblox docs: avatar/makeup/import"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/makeup/import.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai"]
---
# web-aad0a2cc85

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc on importing makeup templates (.fbx/.gltf) into Studio via the Importer, inside the Makeup test place. Covers required mesh objects (target head, head cage, optional Lips/Face/Eyes), resulting Decal + WrapTextureTransfer children, moving decals into the character Makeup folder and eyebrows/eyelashes MeshParts into Accessories, and previewing in Avatar Setup. Not about Blender MCP or bpy.

## Claims
- c1: Makeup templates are imported into Studio as .fbx or .gltf files via the Studio Importer, producing a Model in workspace. *(doc, high; blender-roblox-export-import)*
- c2: Makeup template must include Target head mesh and Target head cage mesh; Lips, Face, Eyes meshes and textures only if modified. *(doc, high; avatar-ugc-accessories)*
- c3: After import, Decal children each carry a WrapTextureTransfer child; decals go into character Makeup folder. *(doc, high; avatar-ugc-accessories)*
- c4: Eyebrows and eyelashes are MeshParts moved into character Accessories folder; they need not be converted to Accessories first in the test place. *(doc, high; avatar-ugc-accessories)*
- c5: Avatar Setup tool (Avatar > Setup) previews makeup decals without playtesting; decals need a child WrapTextureTransfer and a type (eyes, face, lips) assigned. *(doc, high; avatar-ugc-accessories)*
- c6: Makeup fit quality depends on the head's underlying cage; non-Roblox avatars may appear misaligned. *(doc, medium; avatar-ugc-accessories)*
- c7: Source does not mention Blender MCP, bpy scripting, or Claude; it is off-topic for that part of the subject. *(doc, high; claude-blender-ai)*

## Techniques
- t1: **Makeup decal import**: Import .fbx/.gltf in Makeup test place, verify Decal children with WrapTextureTransfer, copy Decals to character Makeup folder, MeshParts to Accessories, playtest or preview in Avatar Setup.

## Quotes (brief, for attribution)
> Verify there are no errors with the imported components, then click Import to add the file into Studio. A new Model populates in the workspace.  (create.roblox.com)

## Points to
- https://github.com/Roblox/avatar/tree/main/Makeup
- https://www.youtube-nocookie.com/embed/BezI4tL4E5k
