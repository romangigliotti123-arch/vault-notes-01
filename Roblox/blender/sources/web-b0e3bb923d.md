---
type: research-source
id: web-b0e3bb923d
title: "Blender manual: render/cycles/baking"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/render/cycles/baking.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 2
density: high
tags: ["research-source", "web", "other", "texturing-baking-uv"]
---
# web-b0e3bb923d

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page for Cycles render baking. Covers setup (UV map plus an active Image Texture node or Color Attribute as target), bake types (Combined, AO, Normal, UV, Roughness, Emit, Diffuse, Glossy, Transmission, Position, Environment, Shadow), Selected-to-Active cage and ray settings, output targets, and margin/bleed options. No Roblox-specific content.

## Claims
- c1: Baking requires the mesh to have a UV map and either a Color Attribute or an Image Texture node with an image as the bake target. *(doc, high; texturing-baking-uv)*
- c2: Cycles uses the scene render settings (samples, bounces) for baking, so baked quality should match the rendered result. *(doc, high; texturing-baking-uv)*
- c3: Baking AO into main objects avoids enabling AO for the full render, saving render time. *(doc, medium; texturing-baking-uv)*
- c4: Target 'Image Textures' bakes only into the active and selected Image Texture node; materials without one get nothing baked. *(doc, high; texturing-baking-uv)*
- c5: Margin (bleed) is generated around UV islands by default to avoid seam discontinuities from filtering and mip-mapping; types are Extend or Adjacent Faces, size in pixels. *(doc, high; texturing-baking-uv)*
- c6: Normal space default is Tangent, which works for animated objects; Object space depends on deformation. *(doc, high; texturing-baking-uv)*
- c7: Selected to Active casts rays from low-poly inward to high-poly; use Max Ray Distance (no cage) or Cage Extrusion / Cage Object to control ray start. *(doc, high; texturing-baking-uv)*
- c8: Without a cage, rays follow mesh normals, causing edge glitches, but this is preferred for baking onto planes to avoid extra edge loops. *(doc, medium; texturing-baking-uv)*
- c9: Cage Extrusion rays use a version of the active object with Edge Split modifiers disabled; hard splits cause non-smooth normals. Cage copy must match topology (face count and order). *(doc, high; texturing-baking-uv)*
- c10: High-poly objects have a fixed CPU memory footprint per object; joining them before baking avoids crashes. *(doc, high; texturing-baking-uv)*
- c11: Target 'Active Color Attribute' bakes into the active vertex colour layer on a mesh; other object types cannot be used. *(doc, high; texturing-baking-uv)*
- c12: Bake from Multires can produce Normal, Displacement, or Vector Displacement maps from viewport level (low) vs render level (high). *(doc, medium; texturing-baking-uv)*
- c13: Page does not mention Roblox, SurfaceAppearance, texture size limits, or export settings. *(doc, high; other)*

## Numbers
- n1: **Margin size**: set in pixels (no default value given) Margin Size option for UV island bleed

## Techniques
- t1: **Selected to Active baking**: Select low-poly, then active high-poly target. Enable Selected to Active, set Max Ray Distance or Cage Extrusion/Cage Object, bake to active Image Texture node or Color Attribute.
- t2: **Multires normal bake**: Use Bake from Multires with Viewport Levels as low-res base and Render Levels as high-res; choose Normals, Displacement, or Vector Displacement.

## Quotes (brief, for attribution)
> Baking requires a mesh to have a UV map, and either a Color Attribute or an Image Texture node with an image to be baked to.  (docs.blender.org)
> When not using a cage the rays will conform to the mesh normals. This produces glitches on the edges.  (docs.blender.org)

## Points to
- https://docs.blender.org/manual/en/latest/render/cycles/baking.html
- Multiresolution Modifier manual
- Image Texture node manual
- Vertex Paint / Color Attributes manual
