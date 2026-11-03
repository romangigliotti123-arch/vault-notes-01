---
title: "Docs: avatar / in-experience-creation"
url: https://create.roblox.com/docs/avatar/in-experience-creation.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / in-experience-creation

[Open](https://create.roblox.com/docs/avatar/in-experience-creation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on in-experience avatar creation: letting players create, customize and purchase avatar bodies inside an experience via EditableImage, EditableMesh and WrapDeformer, then publishing through AvatarCreationService with a creation token. Covers base body setup, editing tools, prompt flow, and attribution join handling.

## Tips
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[ugc-and-avatar-economy]]** Buy an Avatar Creation Token with Robux first; the token sets the in-experience creation price and sale settings.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[building-art-and-assets]]** Base body must meet the 15-MeshPart avatar spec; single-mesh bodies can use Avatar Auto Setup to add required components.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[common-mistakes]]** HumanoidDescription for creation must not contain pre-existing asset IDs for body parts or accessories; only new assets.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[scripting-and-performance]]** Reuse EditableImage instances per TextureID via a lookup map instead of creating duplicates for each MeshPart.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[building-art-and-assets]]** Match imported base body scales to HumanoidDescription scales (BodyTypeScale, HeadScale, HeightScale, WidthScale, ProportionScale).
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[ugc-and-avatar-economy]]** Experience owners earn Marketplace commission as publisher; the player who creates the item is the creator. Created items are not resellable or tradable and are not listed on the Marketplace.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[client-server-and-remotes]]** Each of the 15 MeshParts needs an EditableImage and, for body parts, a WrapDeformer with an EditableMesh; hair uses EditableMesh set directly on the MeshPart.
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) **[[social-features-and-virality]]** Handle CreatedItemAttribution join source via Player:GetJoinData() GameJoinContext so players inspecting a created avatar land correctly.

## Numbers
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) Base body MeshParts: **15 MeshParts across 6 body parts** (Required for in-experience avatar creation base body)
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) Body parts in creation HumanoidDescription: **6** (Head, Torso, LeftArm, LeftLeg, RightArm, RightLeg each need new assets)

## Tools
AssetService, AvatarCreationService, EditableImage, EditableMesh, WrapDeformer, HumanoidDescription, Avatar Auto Setup, Creator Hub

## He points to
- Avatar Creator demo
- Avatar references
- Avatar Creation Tokens docs

## Quotes
- [page](https://create.roblox.com/docs/avatar/in-experience-creation) "Avatar assets created in-experience are not listed on the Marketplace, and cannot be resold or traded."

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[scripting-and-performance]] [[social-features-and-virality]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
