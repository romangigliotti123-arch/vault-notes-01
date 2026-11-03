---
type: research-source
id: web-facc9842e8
title: "Roblox docs: art/characters/creating/export-textures"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/export-textures.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 3
density: low
tags: ["research-source", "web", "blender-roblox-export-import", "other"]
---
# web-facc9842e8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on exporting character textures from Blender. Covers two methods: embedding PBR maps in the FBX by rewiring the custom skin tone shader (Mix node removed, texture Color wired straight to Base Color), or unpacking images as PNG files to a textures folder. No bpy, blender-mcp, or triangle/UV limits content.

## Claims
- c1: Roblox template character has four separate image maps forming its surface appearance (default PBR textures), which can be embedded in FBX or exported as separate PNG files. *(doc, high; blender-roblox-export-import)*
- c2: Embedding textures in FBX requires editing custom skin tone shader nodes: disconnect the Mix node from Principled BSDF Base Color and connect the file26 Color texture node directly to Base Color. *(doc, high; blender-roblox-export-import)*
- c3: To prep embedding: in Object mode select a character part, Shading tab, set Shader Type to Object, then rewire the Base Color input. *(doc, high; blender-roblox-export-import)*
- c4: Separate texture export path: File > External Data > Unpack Resources, choose 'Use files in current directory'; Blender writes images to a textures directory in the project's parent directory. *(doc, high; blender-roblox-export-import)*
- c5: Doc advises testing assets multiple times at every stage, in Blender and after importing into Studio. *(doc, medium; other)*
- c6: Separately exported textures let creators access, test and swap image maps more quickly than embedded textures. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **texture image maps per character surface appearance**: 4 template character includes four separate image maps

## Techniques
- t1: **Embed skin texture into FBX**: Object mode, Shading tab, Shader Type=Object; disconnect Mix node from Base Color; drag file26 Color output to Base Color; export FBX.
- t2: **Unpack resources to PNG**: File > External Data > Unpack Resources > Use files in current directory; textures land in parent-directory textures folder.

## Quotes (brief, for attribution)
> Embedding the texture maps to your .fbx export can simplify the Blender export and Studio import process.  (create.roblox.com)

## Points to
- /art/avatar/character-bodies/test.md
- /art/characters/creating/export-character
- /art/characters/creating/final-checks
