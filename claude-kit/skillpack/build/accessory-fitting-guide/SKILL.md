---
name: accessory-fitting-guide
description: "Walk the UGC accessory path from model to upload - rigid versus layered, attachments or cages, the Accessory Fitting Tool, validation rules - and pre-flight the structure with a read-only script that catches missing Handles, attachments, cage meshes and transparency before the validator does. Use when making hats, hair, clothing or other wearables."
category: build
tags: accessory, ugc, layered clothing, cage, handle, attachment, fitting, wrap, avatar, upload, validation
kb: Roblox/roblox-kb/3d-modeling-rigging-and-animation.md, Roblox/roblox-kb/ugc-and-avatar-economy.md, Roblox/roblox-kb/building-art-and-assets.md
related: rig-checker, animation-import-guide, asset-license-checker, model-rebuild, attachment-fixer
---

# accessory-fitting-guide

Two kinds of wearable need two different setups. A rigid accessory has no skinning and attaches at one avatar point through an attachment in its Handle. Layered clothing has skinning data, inner and outer cages, and bends with the body. Choosing wrong, or half-setting-up either, is why uploads fail. Publishing and pricing are the owner's actions; this prepares and checks.

## When to use
Creating a hat, hair, back item, shirt, jacket or similar; an item that floats off the body, bloats, or will not validate. Not for: character rig problems (`rig-checker`), or in-game cosmetics sold as game assets (`gamepass-maker`).

## Inputs (max 2)
1. Rigid or layered (default: rigid if it sits on one point like a hat, layered if it wraps the body). 2. The attachment point or body area.

## Procedure
1. Start from Roblox's official templates (Rig_and_Attachments or Combined project file, R15 rig template, body cage template). Model at the origin with the origin set to a sensible volume centre.
2. Budget (official, `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md` section 3): rigid and layered accessories at most 4,000 triangles, a single mesh; Marketplace textures at most 2048 (rigid non-albedo maps 256); body parts have their own budgets (dynamic head 4000, torso 1750, each limb 1248, total 10,742). Live-check current UGC limits, they change.
3. Build the mesh, unwrap UVs early (seams on hard edges, islands away from borders, most UV area to the front), texture in layers.
4. Rigid: put the correct R15 attachment inside the Handle (for example `HatAttachment`, `HairAttachment`, `BodyBackAttachment`). Layered: skin to the armature (Automatic Weights, then paint), make `MeshName_InnerCage` and `MeshName_OuterCage` tight and enclosing (large gaps make clothing float or bloat), armature named `Armature`.
5. Fit with the Accessory Fitting Tool (Avatar tab > Accessory > fitting tool). Rely on its preview, not the viewport mannequin, for rigid attachment. Test on several body types and with moving poses.
6. Run `scripts/accessory_check.luau` with the Accessory selected: Handle exists, a known R15 attachment (rigid) or a WrapLayer with CageMeshId and ReferenceMeshId (layered), MeshPart Transparency exactly 0, MeshId set, CanCollide off, duplicate part names, Massless note. It prints what it cannot check (triangles, cage fit, UVs, textures).
7. Fix each problem, re-run to zero, then use the upload validator in Studio; its messages beat any script for current rules.
7b. Marketplace requirements to verify on the imported item: Material Plastic, Transparency 0, VertexColor 1,1,1, no extra Scripts or Parts; a cage must conform to and fully enclose the mesh, and cage vertices and cage UVs are never deleted or changed (official, validation-system docs). Transparent textures: connect the colour map to alpha in the Blender PBR material so the importer sets DoubleSided and Transparency.
8. Never delete or add body vertices on a template; only move them. Do not modify mouth or eye topology on heads.

## Studio MCP path
`list_roblox_studios` -> select the Accessory (`search_game_tree` to find it) -> `execute_luau` (Edit) with `scripts/accessory_check.luau` -> `screen_capture` on a rig wearing it -> owner runs the validator and publishes.

## Fallback
Command bar with the Accessory selected. The fitting tool and the validator are Studio UI only: those steps are `untested` from a script.

## Evidence
`Roblox/roblox-kb/3d-modeling-rigging-and-animation.md` (cage clothing tightly; rigid versus layered; Accessory Fitting Tool; validate MeshParts: Transparency exactly 0, same AvatarPartScaleType; never delete or add body vertices), `Roblox/roblox-kb/building-art-and-assets.md` (UGC modelling and export, layered clothing rules, UV workflow, 4,000-triangle examples), `Roblox/roblox-kb/ugc-and-avatar-economy.md`. UGC rules and limits change: live-check before relying on a number.

## Output
```
ACCESSORY CHECK: Workspace.TopHat
TopHat: type rigid accessory on HatAttachment | [problem] Handle CanCollide is on
not checked here: triangle count (limit 4000), cage fit, UVs, textures   1 accessories, 1 problems
```

## Acceptance checks
- [ ] The script ran and its output is quoted; problems fixed and re-run clean.
- [ ] The chosen type (rigid or layered) matches the setup found.
- [ ] Triangle count and cage fit were checked in the tool, or marked untested.
- [ ] The Studio validator result is recorded (pass or messages).
- [ ] Triangles are at most 4,000 and textures at most 2048 (rigid non-albedo 256), counted not assumed; cage vertex count equals the template's.
- [ ] Nothing was uploaded or priced by this skill.

## Pitfalls
A rigid item with no attachment, or a layered item with a rigid attachment. Cages with gaps. Non-zero MeshPart Transparency. Scaling the mesh instead of fixing the cage. Mixed AvatarPartScaleType across one upload. Copying marketplace items: licence and moderation rules apply (`asset-license-checker`).

## Related
`rig-checker`, `animation-import-guide`, `asset-license-checker`, `model-rebuild`, `attachment-fixer`.
