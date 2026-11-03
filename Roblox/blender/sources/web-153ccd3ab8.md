---
type: research-source
id: web-153ccd3ab8
title: "Roblox docs: avatar/in-experience-creation"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/in-experience-creation.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0568
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits"]
---
# web-153ccd3ab8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on in-experience avatar body creation via AvatarCreationService: base body requirements (15 MeshParts, 6 body parts, FACS), EditableMesh/EditableImage/WrapDeformer setup, PromptCreateAvatarAsync with HumanoidDescription, creation tokens, attribution join data. No Blender or Claude content; only indirect relevance to import/setup of avatar bodies.

## Claims
- c1: A base body must have 15 MeshParts making up 6 body parts (head, torso, left/right arm, left/right leg), plus other avatar components, and meet avatar body guidelines including minimum FACS controls for facial rigging. *(doc, high; avatar-ugc-accessories)*
- c2: Custom base body assets can be imported with the Studio Importer and set up through Avatar Setup; single-mesh bodies can try Avatar Auto Setup to add required avatar components. *(doc, high; blender-roblox-export-import)*
- c3: Each of the 15 body MeshParts must include an EditableImage and a WrapDeformer with an EditableMesh (cage mesh). *(doc, high; avatar-ugc-accessories)*
- c4: Hair accessory in creation: MeshPart needs an EditableImage and an EditableMesh set directly on the MeshPart, with no WrapDeformer child. *(doc, high; avatar-ugc-accessories)*
- c5: HumanoidDescription passed to PromptCreateAvatarAsync must contain 6 BodyPartDescription children, each referencing a Folder of that part's MeshParts (e.g. LeftArm: LeftHand, LeftUpperArm, LeftLowerArm), and no pre-existing asset IDs. *(doc, high; avatar-ugc-accessories)*
- c6: HumanoidDescription may include scales (BodyTypeScale, HeadScale, HeightScale, WidthScale, ProportionScale); they should match the scales the base body was imported with. *(doc, high; avatar-ugc-accessories)*
- c7: Experiences need at least one Avatar Creation Token (purchased with Robux) to set prices; the token ID is passed to PromptCreateAvatarAsync. Experience owner is publisher and earns commissions; the player is creator. *(doc, high; automation-and-creator-workflows)*
- c8: Avatar assets created in-experience are not listed on the Marketplace and cannot be resold or traded; they save to the player's inventory and are wearable in other experiences. *(doc, high; avatar-ugc-accessories)*
- c9: Inspecting an in-experience-created avatar shows an attribution link; Player:GetJoinData() GameJoinContext has JoinSource=CreatedItemAttribution plus optional ItemType, AssetId, OutfitId, AssetType. *(doc, high; avatar-ugc-accessories)*
- c10: WrapDeformer deforms the rendered MeshPart live while keeping skinning and FACS data; editing the cage EditableMesh (SetPosition, FindVerticesWithinSphere) reshapes the body. *(doc, high; mesh-texture-limits)*

## Numbers
- n1: **MeshParts per base body**: 15 making up 6 body parts
- n2: **BodyPartDescription children**: 6 required in HumanoidDescription for creation
- n3: **minimum creation tokens**: 1 required per experience

## Techniques
- t1: **Prepare editable base body**: For each MeshPart in model: if WrapTarget exists, add WrapDeformer with cage EditableMesh (CreateEditableMeshAsync, FixedSize); else build rigid EditableMesh, CreateMeshPartAsync, copy Size/CFrame/TextureContent, ApplyMesh. Create/reuse EditableImage per TextureID.
- t2: **Prompt avatar creation**: Build HumanoidDescription with BodyPartDescription per part (Instance=Folder of MeshParts, BodyPart enum), call AvatarCreationService:PromptCreateAvatarAsync(tokenId, player, description) in pcall; check Enum.PromptCreateAvatarResult.Success; returns bundleId and outfitId.
- t3: **Runtime texture editing**: Use EditableImage DrawRectangle for recolor, DrawImage with BlendSourceOver for stickers, DrawImageProjected with ProjectionParams and BrushConfig for projected decals on a MeshPart.

### Code: Deform a body part by moving cage vertices within a sphere
```lua
local verticesWithinSphere =
	cageEditableMesh:FindVerticesWithinSphere(controlPointCenter, controlPointRadius)
for _, vertexId in verticesWithinSphere do
	local vertexPosition = cageEditableMesh:GetPosition(vertexId)
	cageEditableMesh:SetPosition(vertexId, vertexPosition + controlPointDeformation)
end

wrapDeformer:SetCageMeshContent(Content.fromObject(cageEditableMesh))
```

### Code: Prompt avatar creation
```lua
local success, result, bundleIdOrErrorMessage, outfitId = pcall(function()
	return AvatarCreationService:PromptCreateAvatarAsync(tokenId, player, humanoidDescription)
end)
```

## Points to
- AvatarCreationService
- Avatar Setup / Avatar Auto Setup
- Studio Importer
- Avatar Creation Tokens
- Roblox Avatar Creator demo experience
- Avatar body guidelines (marketplace policy)
