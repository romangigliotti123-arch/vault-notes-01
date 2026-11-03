---
type: research-topic
title: "Mesh limits, UVs, textures, PBR and performance"
slug: mesh-texture-limits
topic: "Blender 3D for Roblox Studio: using Claude with Blender (blender-mcp, bpy scripting) and the Blender-to-Roblox asset pipeline"
date: 2026-11-01
tags: [research-topic]
---
# "Mesh limits, UVs, textures, PBR and performance"

Back to [[blender-README]] | [[blender-playbook]]

Roblox mesh/texture limits: meshes max 20k tris (import auto-simplifies larger); layered accessories single mesh ≤4k tris; body part budgets total 10,742 tris. Geometry must be watertight, quad-friendly, one material per mesh, single UV set within 0:1. Textures: basic up to 4096 in engine, but Marketplace avatar assets now allow 2048 (low-RAM devices cap at 1k). PBR uses SurfaceAppearance with color, normal (OpenGL tangent), roughness, metalness, emissive maps, sized by volume (256 per 2x2x2). Accessory PBR maps have a stricter 256 (normal/rough/metal) / 1024 (color) cap and must be opaque. Mesh Streaming and improved LoDs are opt-in, becoming default around July 2026. Blender glTF export drops AO/displacement/SSS unless baked.

## Key points
- **[OFFICIAL]** [OFFICIAL] Individual meshes cannot exceed 20,000 triangles; Import 3D auto-simplifies meshes above that using a newer simplification engine (staff claim of much higher quality). *(multiple-sources, high)* [[sources/web-7195087017|web-7195087017]] [[sources/off-dev_3958222|off-dev_3958222]]
- **[OFFICIAL]** [OFFICIAL] Rigid accessories must be one mesh with ≤4,000 triangles; clothing max size is 8x8x8 studs centered on attachment; eyebrows/eyelashes 1.5x0.5x0.5. *(multiple-sources, high)* [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]] [[sources/web-04cef4e0ee|web-04cef4e0ee]]
- **[OFFICIAL]** [OFFICIAL] Body triangle budgets: DynamicHead 4000, Torso 1750, each arm 1248, each leg 1248 (total 10,742). Roblox converts quads to tris, so tri count ≈ 2x quad count. *(multiple-sources, high)* [[sources/off-avatar_character-bodies_specifications|off-avatar_character-bodies_specifications]] [[sources/web-2a50b96cb8|web-2a50b96cb8]]
- **[OFFICIAL]** [OFFICIAL] Geometry must be watertight with no holes/backfaces and non-zero thickness; use quads and avoid N-gons. Bodies should be manifold (heads exempt from watertight requirement). *(multiple-sources, high)* [[sources/off-art_modeling_specifications|off-art_modeling_specifications]] [[sources/web-7195087017|web-7195087017]] [[sources/off-dev_4950522|off-dev_4950522]] [[sources/web-04cef4e0ee|web-04cef4e0ee]]
- **[OFFICIAL]** [OFFICIAL] Mesh objects can have only one material. UV rules: single UV set per component, all UVs inside 0:1, overlaps allowed. The UV check has no auto-fix. *(multiple-sources, high)* [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] [[sources/web-2cd06949f0|web-2cd06949f0]] [[sources/web-ad826ab7cf|web-ad826ab7cf]]
- **[OFFICIAL]** [OFFICIAL] Engine supports textures up to 4096x4096 and ramps quality up from lower-res versions. Marketplace avatar textures (bodies, layered clothing, rigid accessories) max 2048x2048, and larger ones are downscaled. Devices under 3.5GB RAM stay at 1k. *(multiple-sources, high)* [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] [[sources/off-dev_4358444|off-dev_4358444]] [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]] [[sources/web-04cef4e0ee|web-04cef4e0ee]]
- **[OFFICIAL]** [OFFICIAL] Texture sizing guidance: 5x5 studs 256; 10x10 512; 20x20 1024. PBR: 256 per 2x2x2 units, rounding up, 1024 max at 8x8x8; 1x1x1 items 64–128. *(multiple-sources, high)* [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] [[sources/web-2cd06949f0|web-2cd06949f0]]
- **[OFFICIAL]** [OFFICIAL] PBR accessory maps: Normal/Roughness/Metalness capped at 256x256, ColorMap at 1024x1024; Normal and Color maps must be opaque. Transparency isn't yet supported there (AlphaMode defaults to Overlay). *(single-source, high)* [[sources/off-dev_3816937|off-dev_3816937]]
- **[OFFICIAL]** [OFFICIAL] PBR map formats: albedo and normal are RGB 24-bit; roughness, metalness and emissive mask are 8-bit grayscale. Normal maps must be OpenGL tangent-space (flat = 127,127,255). Only the metalness workflow is supported; use albedo without baked lighting. *(multiple-sources, high)* [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] [[sources/off-art_modeling_surface-appearance|off-art_modeling_surface-appearance]] [[sources/web-5464514816|web-5464514816]]
- **[OFFICIAL]** [OFFICIAL] PBR is applied through a SurfaceAppearance under a MeshPart; it overrides TextureID, and SurfaceAppearance takes precedence over MaterialVariant maps. Properties generally can't be changed by scripts at runtime. Manual fallback names: _ALB, _MTL, _NOR, _RGH. *(multiple-sources, high)* [[sources/off-art_modeling_surface-appearance|off-art_modeling_surface-appearance]] [[sources/web-903b57f8b0|web-903b57f8b0]] [[sources/off-avatar_layered-accessories_import|off-avatar_layered-accessories_import]]
- **[OFFICIAL]** [OFFICIAL] AlphaMode: Opaque, Overlay (default), Transparency, TintMask. For Transparency, MeshPart.Transparency 0 suits hard cutouts and ≥0.02 suits soft gradients. Eyelashes need DoubleSided plus AlphaMode Transparency. *(multiple-sources, high)* [[sources/web-5464514816|web-5464514816]] [[sources/off-dev_4137281|off-dev_4137281]]
- **[OFFICIAL]** [OFFICIAL] Mesh Streaming streams per-mesh LoDs under a strict memory budget. Enable it with Workspace.MeshStreamingAndImprovedLoDs (opt-in, Default→Enabled planned ~July 2026). While enabled it ignores RenderFidelity, doesn't need StreamingEnabled, and doesn't change collision geometry. Studio restart is required after changing it. *(multiple-sources, high)* [[sources/off-dev_4525340|off-dev_4525340]] [[sources/off-dev_4601232|off-dev_4601232]]
- **[OUTDATED/UNSURE]** [OUTDATED/UNSURE] Blender glTF export loses some maps: of 7 PolyHaven maps only 3 survived; standalone AO and displacement are dropped, SSS and toon shaders don't export. Bake them (Cycles, Non-Color for data maps) before export. *(multiple-sources, medium)* [[sources/gh-elithril-blender-kiln-f-plugin-references-texturing-strategy.md|gh-elithril-blender-kiln-f-plugin-references-texturing-strategy.md]] [[sources/gh-elithril-blender-kiln-f-plugin-references-reference-fidelity.md|gh-elithril-blender-kiln-f-plugin-references-reference-fidelity.md]]
- **[OFFICIAL]** [OFFICIAL] Mesh content changes get a new Mesh ID. The Known Asset Cache reuses IDs for identical content, but float differences (e.g. moving a mesh in Blender) cause cache misses. Cage UVs must match between target and layered cages, and cage vertices must not be added or deleted. *(multiple-sources, high)* [[sources/off-dev_4068650|off-dev_4068650]] [[sources/web-565bb91116|web-565bb91116]] [[sources/off-art_modeling_cage-meshes_create-cages|off-art_modeling_cage-meshes_create-cages]]

## Numbers
- **[OFFICIAL]** **[OFFICIAL] Max triangles per mesh**: 20,000 [[sources/web-7195087017|web-7195087017]]
- **[OFFICIAL]** **[OFFICIAL] Layered accessory max tris**: Rigid accessory max tris = 4,000 [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]]
- **[OFFICIAL]** **[OFFICIAL] Body total tris**: 10,742 (head 4000, torso 1750, limbs 1248 each) [[sources/off-avatar_character-bodies_specifications|off-avatar_character-bodies_specifications]]
- **[OFFICIAL]** **[OFFICIAL] Marketplace avatar texture max**: 2048x2048 [[sources/off-dev_4358444|off-dev_4358444]] [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]]
- **[OFFICIAL]** **[OFFICIAL] Engine max texture**: 4096x4096 [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]]
- **[OFFICIAL]** **[OFFICIAL] Low-RAM device texture cap**: 1k under 3.5GB RAM [[sources/off-dev_4358444|off-dev_4358444]]
- **[OFFICIAL]** **[OFFICIAL] PBR accessory map caps**: Normal/Rough/Metal 256; Color 1024 [[sources/off-dev_3816937|off-dev_3816937]]
- **[OFFICIAL]** **[OFFICIAL] PBR budget**: 256 per 2x2x2 units; 1024 max at 8x8x8 [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]]
- **[OFFICIAL]** **[OFFICIAL] RenderFidelity Automatic distances**: Highest <250 studs; Medium 250–500; Lowest 500+ [[sources/web-903b57f8b0|web-903b57f8b0]]
- **[OFFICIAL]** **[OFFICIAL] Cage vertex example**: head render mesh up to 12,000 verts vs cage 335 [[sources/web-565bb91116|web-565bb91116]]

## Techniques
- **[OFFICIAL]** **[OFFICIAL] Size textures by footprint**: Pick map size from stud size (5→256, 10→512, 20→1024) or from volume (256 per 2x2x2, round up). [[sources/web-2cd06949f0|web-2cd06949f0]]
- **[SINGLE-SOURCE]** **[SINGLE-SOURCE] Bake procedural materials**: Use Cycles, add an active image node per material, ensure UVs, run bpy.ops.object.bake, save PNG, set Non-Color for roughness/normal, reconnect and re-audit. [[sources/gh-elithril-blender-kiln-f-plugin-references-texturing-strategy.md|gh-elithril-blender-kiln-f-plugin-references-texturing-strategy.md]]
- **[OFFICIAL]** **[OFFICIAL] Four-map SurfaceAppearance reimport**: Select one texture; same-folder maps with matching name and suffix are auto-detected. [[sources/off-dev_4068650|off-dev_4068650]]
- **[OFFICIAL]** **[OFFICIAL] Enable Mesh Streaming**: Set Workspace.MeshStreamingAndImprovedLoDs = Enabled, restart Studio, test, publish. [[sources/off-dev_4601232|off-dev_4601232]]
- **[OFFICIAL]** **[OFFICIAL] A/B LoD comparison**: Set all MeshParts to RenderFidelity Performance, toggle the property, restart Studio between toggles. [[sources/off-dev_4601232|off-dev_4601232]]
- **[SINGLE-SOURCE]** **[SINGLE-SOURCE] Multi-pass decimation**: Back up the original, decimate in several small passes, and apply only after confirming the before/after poly count. [[sources/gh-elithril-blender-kiln-f-plugin-references-topology-rules.md|gh-elithril-blender-kiln-f-plugin-references-topology-rules.md]]
- **[OUTDATED/UNSURE]** **[OUTDATED/UNSURE] Material atlas consolidation**: Convert toon shaders to PBR, consolidate_materials into a 2048 atlas, then optimize_draw_calls. [[sources/gh-sandraschi-blender-mcp-f-docs-blender-TOOL_REFERENCE.md|gh-sandraschi-blender-mcp-f-docs-blender-TOOL_REFERENCE.md]]
- **[OFFICIAL]** **[OFFICIAL] Trim sheet / overlapping UVs**: Unwrap many objects onto a shared trim sheet; overlaps are allowed to save texture memory. [[sources/off-art_blender|off-art_blender]] [[sources/web-2cd06949f0|web-2cd06949f0]]

## Disagreements
- **Maximum UV/texture size**: UV rules say max 1024x1024 texture map; PBR budget 1024 max [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] [[sources/web-2cd06949f0|web-2cd06949f0]] | Newer: 2048 uploadable for avatar heads/bodies/layered/rigid accessories; engine supports up to 4096 [[sources/off-dev_4358444|off-dev_4358444]] [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] | PBR accessory maps: Normal/Rough/Metal 256, Color 1024 [[sources/off-dev_3816937|off-dev_3816937]] Note: These apply to different contexts. The 2026-02 post (S259) is the newest for avatar assets. The older UV and PBR budget guidance is likely stale or general-purpose, and the 256 accessory cap is from 2025-07, so it may have been superseded.

## Gaps
- No Roblox-specific texel-density or vertex-count guidance for non-avatar environment props beyond the 20k mesh cap.
- Unclear whether the 256 PBR accessory cap (2025-07) still holds after the 2k texture update (2026-02).
- No verified Blender shader setup details for PBR import; the DevForum post is referenced but not summarized.
- Whether Mesh Streaming Phase 2 default-on actually shipped is not confirmed.
- Generic platform budgets (VRChat etc.) are not Roblox-specific and don't give Roblox performance numbers.
