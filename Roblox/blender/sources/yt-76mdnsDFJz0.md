---
type: research-source
id: yt-76mdnsDFJz0
title: "OpenPBR: Road to Expressive and Interoperable Material Models — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=76mdnsDFJz0"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0034
relevance: 1
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-76mdnsDFJz0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender BCON26 talk on OpenPBR, a layered physically based material spec, and how it differs from Principled BSDF. Covers new Blender OpenPBR node (feature complete on OpenPBR 1.1, planned for Blender 5.4), USD/MaterialX import-export, renderer mismatches, and a MaterialX GSoC shading-authoring project. No Roblox, FBX/glTF, or Studio content.

## Claims
- c1: Blender adds a new OpenPBR shading node, feature complete on OpenPBR 1.1; release planned for Blender 5.4. *(doc, high; other)*
- c2: [19:14] OpenPBR export/import to USD works via MaterialX nodes; simple texture-driven shading network rendered similarly in Karma and Houdini, but larger networks not yet supported. *(demo, medium; other)*
- c3: [11:05] Converting Principled BSDF materials to OpenPBR gives nearly the same look; conversion is not lossless, and Principled is kept for compatibility. *(demo, medium; other)*
- c4: [38:03] Feature status in Principled BSDF: thin-walled and negative subsurface anisotropy in 5.2, dispersion in 5.3, anisotropic glass in 5.3; coat darkening, transmission depth, anisotropic coat and thin film weight not yet added. *(doc, medium; other)*
- c5: [21:55] Renderer differences across Cycles, Adobe reference and Karma were traced to unclear spec wording; the team is working with Adobe and SideFX on spec clarification. *(opinion, medium; other)*
- c6: [27:23] OpenPBR 1.2 near release with specular haze and retroreflectivity; a peer-reviewed leaf paper (EGSR) motivates a future thin subsurface model. *(doc, medium; other)*
- c7: [29:13] A Google Summer of Code project produced a MaterialX shading graph import/export POC in Blender and renders it via Cycles' OSL backend. *(demo, medium; other)*
- c8: [40:46] Converting old Principled materials to OpenPBR is not one-to-one; a node group and examples are planned, with scale and subsurface method adjustments needed. *(doc, medium; other)*

## Numbers
- n1: **OpenPBR start**: 2023, Adobe and Autodesk, MaterialX subproject 
- n2: **Specular mapping**: OpenPBR specular weight = Principled specular IOR level x2 
- n3: **Dispersion scale**: 0 = none, 1 = full Abbe-number effect 
- n4: **Blender target**: 5.4 planned for OpenPBR node 

## Techniques
- t1: **Dispersion setup**: Look up material refractive index and Abbe number; set dispersion scale to 1 for physical values, lower for artistic control.
- t2: **Thin-walled mode**: Model a thin surface as one surface with thin-walled enabled instead of two close surfaces; reduces noise, approximate for rough glass.
- t3: **Thin subsurface via anisotropy**: For leaves/paper, use negative subsurface anisotropy to bias toward diffuse reflection, positive to bias toward transmission.
- t4: **Transmission depth**: Set depth at which transmission color is reached so thin areas look lighter and thick paths darker.

## Points to
- OpenPBR spec (ASWF)
- MaterialX
- USD
- Adobe OpenPBR reference implementation
- Karma
- Houdini
- Cycles OSL backend
