---
type: research-source
id: web-4aa391c3fb
title: "Roblox docs: art/modeling/material-reference"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/material-reference.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "mesh-texture-limits"]
---
# web-4aa391c3fb

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs page listing PBR roughness/metalness reference values for common materials (plastic, rubber, wood, fabrics, leather, fur, skin, metals, glass) and four layered-clothing examples comparing Substance Painter and Roblox Studio renders. Useful as material value baselines for SurfaceAppearance; says nothing about Blender, bpy, MCP, or the export pipeline.

## Claims
- c1: Roblox docs give baseline PBR values: Glossy Plastic roughness 0.1, Matte Plastic 0.4, both metalness 0.0. *(doc, high; mesh-texture-limits)*
- c2: Pure metals (gold, silver, bronze) listed at roughness 0.2-0.3 with metalness 1.0. *(doc, high; mesh-texture-limits)*
- c3: Glass Mirror listed at roughness 0.0 and metalness 0.1. *(doc, high; mesh-texture-limits)*
- c4: Fabric baselines: cotton/canvas/denim roughness 0.8-0.9; wool/linen 0.9-0.96; polyester/nylon 0.6-0.8; all metalness 0.0 except silk/satin and velvet/suede at 0.4-0.6. *(doc, high; mesh-texture-limits)*
- c5: Layered clothing example: leather jacket uses leather roughness 0.62 metalness 0.0 and brass zipper roughness 0.25 metalness 1.0. *(doc, high; avatar-ugc-accessories)*
- c6: Puffer jacket example: metallic puffer fabric roughness 0.62 metalness 1.0; fur hood roughness 0.75; cotton band roughness 0.8. *(doc, high; avatar-ugc-accessories)*
- c7: Denim jacket example: denim roughness 0.9 metalness 0.0; tarnished steel buttons roughness 0.33 metalness 1.0. *(doc, high; avatar-ugc-accessories)*
- c8: Page states that combining roughness and metalness with PBR textures lets Roblox render nearly every surface type; this is marketing-style framing, not a measured claim. *(opinion, medium; mesh-texture-limits)*

## Numbers
- n1: **Glossy plastic roughness / metalness**: 0.1 / 0.0 
- n2: **Matte plastic roughness / metalness**: 0.4 / 0.0 
- n3: **Pure metals roughness / metalness**: 0.2-0.3 / 1.0 
- n4: **Glass mirror roughness / metalness**: 0.0 / 0.1 
- n5: **Skin roughness / metalness**: 0.65 / 0.0 
- n6: **Jade roughness / metalness**: 0.15 / 0.0 
- n7: **Leather jacket leather roughness**: 0.62 (metalness 0.0) 
- n8: **Brass zipper roughness / metalness**: 0.25 / 1.0 

## Techniques
- t1: **Pick PBR baseline by material**: Start from listed roughness/metalness values for a material class (e.g. wood 0.2-0.3 glossy, 0.7-0.9 worn), then tune in Roblox Studio against the reference renders.

## Points to
- https://create.roblox.com
- https://github.com/Roblox/creator-docs
