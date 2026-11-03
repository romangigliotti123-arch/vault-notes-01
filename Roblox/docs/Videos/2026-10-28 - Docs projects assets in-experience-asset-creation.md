---
title: "Docs: projects / assets / in-experience-asset-creation"
url: https://create.roblox.com/docs/projects/assets/in-experience-asset-creation.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / assets / in-experience-asset-creation

[Open](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on in-game asset creation: letting players save in-experience creations (currently Image assets from EditableImage) to inventories via AssetService:PromptCreatePlatformContentAsync, with attribution back to the game. Covers requirements, server-side example, post-creation locations, and attribution versioning caveat.

## Tips
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) **[[ui-ux-design]]** Call PromptCreatePlatformContentAsync from a server-side script only; the Submit dialog (name/description) is Roblox-provided UI, so no custom save UI is needed.
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) **[[client-server-and-remotes]]** Invoke the prompt on the server, and wait for player.CharacterAdded before prompting so CoreGui is loaded, or the Prompt method will fail.
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) **[[testing-debugging-and-qa]]** Publish the place before testing; the save prompt fails in Studio on unpublished places. Check Output/Developer Console for save errors.
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) **[[anti-exploit-and-security]]** Enable 'Allow Mesh/Image APIs' in experience settings; EditableImage creation requires it and the script warns otherwise.
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) **[[ugc-and-avatar-economy]]** Attribution is tied to a specific asset version; editing a saved package in Studio to make a new version removes attribution for that new version.
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) **[[ugc-and-avatar-economy]]** Let players save creations as a visibility driver: saved assets show attribution links to your game on profiles and inventories, so friends can click through and create their own.
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) **[[building-art-and-assets]]** Generate images procedurally with AssetService:CreateEditableImage, DrawRectangle and DrawImageTransformed, then destroy temporary EditableImages after compositing.

## Numbers
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) Supported in-game asset types: **Image only (Enum.AssetType.Image); packages (Model) not currently supported**
- [page](https://create.roblox.com/docs/projects/assets/in-experience-asset-creation) Example image size: **400x400 canvas, 200x200 logo, 56px inner square, 15 degree rotation**

## Games
- **In-Experience Creation Demo Arena**: Official demo showing the in-game creation workflow; join as a user or open in Studio to reference the design.

## Tools
AssetService:PromptCreatePlatformContentAsync, AssetService:CreateEditableImage, EditableImage:DrawRectangle, EditableImage:DrawImageTransformed, Roblox Creator Dashboard, Studio Toolbox Inventory tab

## He points to
- In-Experience Creation Demo Arena

## Topics
[[anti-exploit-and-security]] [[building-art-and-assets]] [[client-server-and-remotes]] [[testing-debugging-and-qa]] [[ugc-and-avatar-economy]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
