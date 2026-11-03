---
type: research-source
id: web-db1fb3e2fa
title: "making better materials"
source_type: "web"
creator: "www.blenderguru.com"
url: "https://www.blenderguru.com/posts/making-better-materials"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "web", "other"]
---
# web-db1fb3e2fa

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Generic Blender shading tutorial by Andrew Price (BlenderGuru, May 25, year not stated). Covers building a porcelain teapot material from Diffuse with raised roughness, two Subsurface Scattering shaders, Layer Weight/Fresnel-driven Mix with glossy, HDRI reflections, Node Wrangler Emission Viewer, and testing under multiple lighting setups. No Roblox, Claude, MCP, bpy, FBX/glTF, or asset-pipeline content.

## Claims
- c1: Source is a general Cycles/node-based shading article; it does not mention Roblox, Claude, blender-mcp, bpy, or any export pipeline. *(doc, high; other)*
- c2: Author recommends Fresnel/Layer Weight node in a Mix Shader factor to add angle-dependent reflections on non-metal surfaces. *(doc, high; other)*
- c3: Author advises testing materials under several HDRIs/lamp setups before use in animation or games, since lighting changes how a shader looks. *(opinion, medium; other)*

## Techniques
- t1: **Fresnel-weighted glossy mix**: Plug Layer Weight (or Fresnel node, set IOR) into the Factor of a Mix Shader with a glossy shader, so reflections increase at grazing angles.
- t2: **Dual subsurface scattering**: Use two Subsurface Scattering shaders with different scales mixed together for a softer falloff on translucent materials.

## Points to
- https://www.marmoset.co (Basic Theory of Physically-Based Rendering)
- Node Wrangler add-on
