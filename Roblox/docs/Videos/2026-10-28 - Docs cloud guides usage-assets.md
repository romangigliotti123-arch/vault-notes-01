---
title: "Docs: cloud / guides / usage-assets"
url: https://create.roblox.com/docs/cloud/guides/usage-assets.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / usage-assets

[Open](https://create.roblox.com/docs/cloud/guides/usage-assets.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud Assets API docs: uploading new assets and updating existing ones via HTTP, supported types and size/upload limits, API key and OAuth 2.0 scope setup, operation status polling, and using uploaded assets in Studio.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[ai-and-tools]]** Use the Assets API to upload/update assets with one HTTP request instead of manual Studio imports; beta endpoints may change.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[version-control-and-tooling]]** Create the API key with assets access permission plus Read/Write on the target game, depending on which endpoints you call.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[version-control-and-tooling]]** Only .fbx content updates are supported for existing assets; each update creates a new version.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[building-art-and-assets]]** Use Importer instead of the API for custom 3D models when you need a 3D preview, error checks and import settings.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[building-art-and-assets]]** Don't edit .rbxm/.rbxmx files outside Roblox Studio; they may fail to upload or function.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[building-art-and-assets]]** Meshes are accepted only if downloaded from the Asset Delivery API; otherwise use Importer for meshes.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[ai-and-tools]]** Poll the Get Operation endpoint with the returned operation ID to check upload status, or read the status field to see why an upload failed.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[client-server-and-remotes]]** Reference uploaded assets in scripts via rbxassetid:// strings or Content.fromAssetId() using the assetId from the operation response.
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[ai-and-tools]]** Use asset:read and asset:write scopes when registering an OAuth 2.0 app that uploads assets for users (beta).
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) **[[common-mistakes]]** Metadata-only Update Asset calls are not subject to the content upload limits; only content uploads are restricted.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) Max file size per Create/Update Asset call: **20 MB** (One asset per call for content uploads)
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) Audio max duration: **7 minutes** (Formats mp3, ogg, wav, flac; not available for updating)
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) Audio uploads per month, ID-verified: **100** (10 per month if not ID-verified)
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) Decal/Image max dimensions: **Smaller than 8000x8000 px** (png, jpeg, bmp, tga; not available for updating)
- [page](https://create.roblox.com/docs/cloud/guides/usage-assets) Video max duration / resolution / size: **5 min / 4096x2160 / 3.75 GB** (mp4, mov; 20 uploads per day if 13+ and ID-verified)

## Tools
Roblox Open Cloud Assets API, Get Operation endpoint, Importer, Creator Dashboard, Toolbox / Asset Manager, OAuth 2.0

## He points to
- rbxassetid
- Group roles and permissions
- Asset delivery API
- Importer

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
