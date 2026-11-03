---
type: research-source
id: web-49f00d77aa
title: "Blender manual: render/shader_nodes/shader/principled"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/render/shader_nodes/shader/principled.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 2
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "other", "texturing-baking-uv"]
---
# web-49f00d77aa

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page for the Principled BSDF shader node: its layer structure (base, coat, sheen, thin film, emission), inputs, and which options are Cycles-only. It says the node is OpenPBR-based and that Substance Painter textures can link directly. It does not mention Roblox, bpy, blender-mcp, or export.

## Claims
- c1: Principled BSDF is based on the OpenPBR Surface model and accepts textures painted or baked in software like Substance Painter linked directly to its inputs. *(doc, high; texturing-baking-uv)*
- c2: Alpha input is usually linked to the Alpha output of an Image Texture node, with 1.0 fully opaque. *(doc, high; texturing-baking-uv)*
- c3: Normal input controls base-layer normals; Coat has its own Normal input for smooth coating over rough surfaces. *(doc, high; texturing-baking-uv)*
- c4: Diffuse Roughness, Subsurface IOR, Subsurface Anisotropy, Specular Anisotropy, Dispersion, and Thin Film are marked Cycles Only, so they likely do not carry over to EEVEE. *(doc, high; other)*
- c5: Thin Wall mode treats the surface as a zero-thickness slab; in EEVEE set Thickness to 0 and Thickness Mode to Slab, and Subsurface Radius/Scale/Method are ignored. *(doc, high; other)*
- c6: Metallic 0.0 is dielectric with diffuse or transmissive base; 1.0 is fully specular tinted by base color with no diffuse. *(doc, high; other)*
- c7: Default IOR is 1.5 (glass approximation); Thin Film default IOR is 1.33 (water); Thin Film effect is strongest roughly between 100 and 1000 nm. *(doc, high; other)*
- c8: Random Walk subsurface needs closed meshes; overlapping faces and holes can cause problems. Christensen-Burley is faster but less accurate. *(doc, high; other)*
- c9: Dispersion is noisy; reducing color noise requires higher Samples and higher Indirect Light Clamping. *(doc, medium; common-mistakes-fixes)*

## Numbers
- n1: **Default IOR**: 1.5 Approximates glass; IOR range for most materials 1.0 to 4.0
- n2: **Thin Film default IOR**: 1.33 Approximation for water
- n3: **Thin Film effective thickness**: 100 to 1000 nm Range where interference effect is strongest
- n4: **Skin anisotropy**: 0.8 Measured value cited in Subsurface Anisotropy section
- n5: **Anisotropic Rotation offset**: 0.25 Add to value to match Glossy BSDF orientation (90 degree rotation)
- n6: **Emission Strength for shadeless**: 1.0 Makes object match Emission Color exactly

## Techniques
- t1: **Thin-walled surface**: Enable Thin Wall for paper, leaves, or window sheets. In EEVEE set Thickness 0 and Thickness Mode Slab. Subsurface inputs are ignored in this mode.
- t2: **Metallic/IOR Level texturing**: Use IOR Level (0.5 = no change) as a texturable input to control specular intensity, separate from IOR.

## Quotes (brief, for attribution)
> Image textures painted or baked from software like Substance Painter may be directly linked to the corresponding input in this shader.  (docs.blender.org)

## Points to
- https://www.rp-photonics.com/abbe_number.html
- OpenPBR Surface shading model
- Substance Painter
