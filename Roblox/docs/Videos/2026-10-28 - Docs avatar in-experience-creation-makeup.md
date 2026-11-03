---
title: "Docs: avatar / in-experience-creation-makeup"
url: https://create.roblox.com/docs/avatar/in-experience-creation-makeup.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / in-experience-creation-makeup

[Open](https://create.roblox.com/docs/avatar/in-experience-creation-makeup.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on in-experience makeup creation: letting players paint, assemble and purchase makeup assets on their avatar head at runtime. Covers single vs multi-layer prompts, tokens, projected painting via WrapTextureTransfer, cage/target UV conversion, decal submission, and moderation events.

## Tips
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[development-process-and-speed]]** Only attempt in-experience makeup if you're comfortable with scripting and Studio; the docs flag it as an advanced workflow.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[monetisation-other]]** As experience owner you earn Marketplace commissions as publisher of player-created makeup; the creator keeps creator status.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[ugc-and-avatar-economy]]** In-experience created makeup isn't listed on Marketplace and can't be resold or traded; plan monetisation around that.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[common-mistakes]]** Makeup only works on R15 characters with MeshPart heads; other rigs will not support it.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[ugc-and-avatar-economy]]** Generate a creation token whose creation type matches each makeup asset type before building submission entries.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[scripting-and-performance]]** Call WrapTextureTransfer:PrepareProjectionMeshDataAsync() before any projected draw/sample, and re-prepare if the head mesh changes.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[optimization-and-streaming]]** Check AssetService:CreateEditableImage() return value; nil means not enough editable memory, so handle it gracefully.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[scripting-and-performance]]** Limit cage-space conversion to MakeupRules.WrapTextureTransferUVBounds from GetValidationRules(), not the whole cage; bounds must be finite with max > min on both axes.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[age-ratings-moderation-and-tos]]** Listen to AvatarAssetModerationCompleted per asset and AvatarOutfitModerationCompleted for the whole outfit before using creations in-experience.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[anti-exploit-and-security]]** Creation prompts show the player a final confirmation before submission and moderation; don't try to bypass that step.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[combat-and-gameplay-systems]]** Use PromptCreateAvatarAssetAsync for one layer; PromptCreateMakeupAsync requires at least two entries and shares one head color.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) **[[ugc-and-avatar-economy]]** Test in-experience makeup creation in Roblox's Avatar Creator demo before implementing.

## Numbers
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) Makeup asset types supported: **5 (FaceMakeup, LipMakeup, EyeMakeup, EyebrowAccessory, EyelashAccessory)**
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) Minimum layers for PromptCreateMakeupAsync: **2**
- [page](https://create.roblox.com/docs/avatar/in-experience-creation-makeup) Supported rig/head: **R15 with MeshPart heads only**

## Tools
Roblox Studio, AvatarCreationService, EditableImage, EditableMesh, WrapDeformer, WrapTarget, WrapTextureTransfer, AssetService

## He points to
- Avatar makeup (Studio authoring guide)
- Roblox Avatar Creator demo

## Topics
[[age-ratings-moderation-and-tos]] [[anti-exploit-and-security]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[development-process-and-speed]] [[monetisation-other]] [[optimization-and-streaming]] [[scripting-and-performance]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
