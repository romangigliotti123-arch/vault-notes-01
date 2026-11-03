---
type: research-source
id: off-marketplace_validation-system
title: "Roblox Creator Docs: marketplace_validation-system"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/marketplace/validation-system"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0052
relevance: 2
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "mesh-texture-limits", "rigging-animation"]
---
# off-marketplace_validation-system

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on the UGC validation system, which checks avatar assets (bodies, cosmetics, accessories, heads, animations) before Studio upload to the Marketplace. Lists validation categories and per-error fixes. Relevant to Blender-to-Roblox avatar export only indirectly; no Blender, bpy, or MCP content.

## Claims
- c1: UGC validation runs on Studio Marketplace upload and on AvatarCreationService calls; assets not meant for Marketplace need not pass. *(doc, high; avatar-ugc-accessories)*
- c2: Bodies and layered accessories must include skinning data; rigid accessories must not; skin weight count must match vertex count. *(doc, high; avatar-ugc-accessories)*
- c3: MeshPart Transparency must be exactly 0 on all body part meshes. *(doc, high; avatar-ugc-accessories)*
- c4: All MeshParts in one upload must share the same AvatarPartScaleType; accepted values are Classic, ProportionsSlender, ProportionsNormal. *(doc, high; avatar-ugc-accessories)*
- c5: Instances in uploaded asset must not have custom Attributes (GUID attribute excepted); otherwise validation fails. *(doc, high; avatar-ugc-accessories)*
- c6: Rig attachments must have identity rotation (0,0,0); non-rig attachments like LeftGrip_Att must be within a per-attachment deviation from recommended orientation. *(doc, high; avatar-ugc-accessories)*
- c7: Body part opacity is checked by rasterizing the mesh from six orthographic views (front, back, left, right, top, bottom) and counting opaque pixels per view. *(doc, high; mesh-texture-limits)*
- c8: Mesh geometry checks include triangle budgets, bounding box size, surface area, centering at origin, watertightness, and rejection of N-gons, vertex colors, and zero-area triangles. *(doc, high; mesh-texture-limits)*
- c9: Cage UVs must match Roblox's official body cage template; UVs outside [0,1] and zero-area UV triangles are rejected. *(doc, high; mesh-texture-limits)*
- c10: Render mesh and outer cage bounding boxes must be close in size; cage vertices must stay close to render mesh surface; render mesh must sit inside outer cage. *(doc, medium; mesh-texture-limits)*
- c11: MeshPart CollisionFidelity must match the expected value (typically Default) for body part uploads. *(doc, high; mesh-texture-limits)*
- c12: Bones must be skinned only to the advanced R15 rig hierarchy; skinning to other joints is rejected. *(doc, high; rigging-animation)*
- c13: Bone Transform must be identity CFrame for Marketplace uploads; bone child must be measurably separated from its parent. *(doc, high; rigging-animation)*
- c14: Animations must be CurveAnimation from the Animation Editor; legacy KeyframeSequence is rejected. *(doc, high; rigging-animation)*
- c15: Animation Weight values must be greater than 0 (typically 1.0). *(doc, high; rigging-animation)*
- c16: HRD/DRD bone animation is gated to trusted creators and not allowed from in-experience creation; bones may only rotate, with no Position track. *(doc, high; rigging-animation)*
- c17: Body parts in CurveAnimation must stay above a minimum height and within a max distance from HumanoidRootPart on every sampled frame; exact thresholds not given in the text. *(doc, medium; rigging-animation)*
- c18: Dynamic head requires at least 17 FACS poses and landmarks must move for blink, mouth open, happy and sad expressions. *(doc, high; avatar-ugc-accessories)*
- c19: Minimum/maximum bounding box checks are per body scale type; meshes too small or joints/meshes too large on any axis fail. *(doc, high; avatar-ugc-accessories)*
- c20: Error fixes often point to re-importing meshes in Studio or re-exporting from the official body cage template rather than editing in place. *(doc, medium; avatar-ugc-accessories)*

## Numbers
- n1: **orthographic views for opacity check**: 6 
- n2: **minimum FACS poses for dynamic head**: 17 
- n3: **accepted AvatarPartScaleType values**: 3 (Classic, ProportionsSlender, ProportionsNormal) 
- n4: **animation Weight minimum**: > 0 (typically 1.0) 
- n5: **UV coordinate range**: [0, 1] 
- n6: **MeshPart Transparency**: 0 exactly 
- n7: **rig attachment rotation**: (0,0,0) 

## Techniques
- t1: **Cage UV template matching**: Re-export cage from official body cage template without adding, removing, or merging UV vertices; keep UVs within [0,1] and non-degenerate.
- t2: **Visualization checks for troubleshooting**: Use the validation visualization tools in Studio to see asset-specific guides for fixing failed checks before re-upload.
- t3: **Bone rotation-only animation**: For HRD/DRD bones, animate with EulerRotationCurve only; remove Position tracks to avoid joint separation.

## Quotes (brief, for attribution)
> Assets that you don't intend to use for the Marketplace, such as those for in-game use only, do not need to pass the validation process.  (create.roblox.com)
> Bone animations are a gated feature requiring trusted creator status.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/avatar/dynamic-heads/specifications
- https://create.roblox.com/docs/avatar/makeup/specifications
- https://create.roblox.com/docs/avatar/rigid-accessories/specifications
- https://create.roblox.com/docs/avatar/layered-accessories/specifications
- https://create.roblox.com/docs/avatar/animation-packs
- https://create.roblox.com/docs/avatar/resources
