---
type: research-source
id: web-36dcd10d06
title: "Blender manual: modeling/meshes/uv/unwrapping/introduction"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/modeling/meshes/uv/unwrapping/introduction.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 1
density: low
tags: ["research-source", "web", "texturing-baking-uv"]
---
# web-36dcd10d06

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page on the UV unwrapping introduction: what UVs are, that each face can link to a different image, that Face Select mode is needed to assign images, and the basic unwrap workflow in the UV Editing workspace. Generic Blender UV content, not Roblox or bpy/MCP specific.

## Claims
- c1: Unwrap is done in Edit Mode; choose UV Editing workspace, select faces, pick method from UV > Unwrap, adjust in Adjust Last Operation panel, then test with an image. *(doc, high; texturing-baking-uv)*
- c2: Each mesh face gets four UV coordinates; a 3D Viewport must be in Face Select mode to assign images or change UVs of the active object. *(doc, high; texturing-baking-uv)*
- c3: Mark seams before unwrapping when needed; unwrapping is best started once geometry needs only minor changes. *(doc, medium; texturing-baking-uv)*

## Techniques
- t1: **Standard unwrap workflow**: Mark seams, select faces, UV > Unwrap method, adjust in Adjust Last Operation, apply test image to check distortion, then edit UVs in UV Editor.

## Points to
- Marking seams page
- Applying Images to UVs
- Editing UVs
