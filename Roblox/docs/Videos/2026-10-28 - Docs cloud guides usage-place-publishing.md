---
title: "Docs: cloud / guides / usage-place-publishing"
url: https://create.roblox.com/docs/cloud/guides/usage-place-publishing.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / usage-place-publishing

[Open](https://create.roblox.com/docs/cloud/guides/usage-place-publishing.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Cloud API docs guide for publishing place files to existing places via the Place Publishing API: requirements (API key with universe-places and Write permissions, Universe ID, Place ID), unsupported instance types, and a curl POST example for .rbxlx/.rbxl uploads.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing) **[[ai-and-tools]]** Automate publishing by calling the Place Publishing API from CI (e.g. a GitHub Action) after integration tests pass, instead of publishing manually from Studio.
- [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing) **[[version-control-and-tooling]]** Create an API key with universe-places access permission and Write operation scoped to the specific game before calling the publish endpoint.
- [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing) **[[common-mistakes]]** Publish from Studio if your game contains EditableImage, EditableMesh, PartOperation, SurfaceAppearance, or BaseWrap instances; the API does not update them.
- [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing) **[[version-control-and-tooling]]** Send the place file as Content-Type application/xml for .rbxlx or application/octet-stream for .rbxl; the API only supports HTTPS requests.
- [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing) **[[version-control-and-tooling]]** Check the returned versionNumber in the success response and verify the upload in Studio or on the Creator Dashboard.

## Tools
Roblox Place Publishing API (Open Cloud), Creator Dashboard, curl, GitHub Actions

## He points to
- https://create.roblox.com/dashboard/creations

## Topics
[[ai-and-tools]] [[common-mistakes]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
