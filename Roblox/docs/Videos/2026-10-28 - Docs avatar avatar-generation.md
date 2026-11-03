---
title: "Docs: avatar / avatar-generation"
url: https://create.roblox.com/docs/avatar/avatar-generation.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / avatar-generation

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/avatar/avatar-generation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs page for Roblox's alpha Photo-to-avatar feature. Covers requesting an AvatarCreationService generation session, taking a selfie to produce a 2D preview, generating a 3D avatar as HumanoidDescription, and publishing it. Aimed at scripters familiar with Studio.

## Tips
- [page](https://create.roblox.com/docs/avatar/avatar-generation) **[[ugc-and-avatar-economy]]** Feature is alpha; check the DevForum announcement for current behaviour before building on it.
- [page](https://create.roblox.com/docs/avatar/avatar-generation) **[[client-server-and-remotes]]** Call GenerateAvatarAsync and LoadGeneratedAvatarAsync on the server and LoadAvatar2DPreviewAsync on the client; send previewId to the client via remote.
- [page](https://create.roblox.com/docs/avatar/avatar-generation) **[[client-server-and-remotes]]** Apply edits to EditableMesh/EditableImage on both server and client copies so they stay in sync for publish.
- [page](https://create.roblox.com/docs/avatar/avatar-generation) **[[development-process-and-speed]]** Use the returned waitTime from RequestAvatarGenerationSessionAsync to tell players how long until generation is available.

## Numbers
- [page](https://create.roblox.com/docs/avatar/avatar-generation) Allowed2DGenerations: **Set per session; returned in session dictionary (value not stated)**
- [page](https://create.roblox.com/docs/avatar/avatar-generation) Allowed3DGenerations: **Set per session; returned in session dictionary (value not stated)**
- [page](https://create.roblox.com/docs/avatar/avatar-generation) SessionTime: **Maximum session length in seconds (value not stated)**

## Tools
AvatarCreationService, HumanoidDescription, EditableMesh, EditableImage

## Topics
[[ai-and-tools]] [[client-server-and-remotes]] [[development-process-and-speed]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
