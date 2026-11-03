---
title: "Docs: assistant / guide"
url: https://create.roblox.com/docs/assistant/guide.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: assistant / guide

[Open](https://create.roblox.com/docs/assistant/guide.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for Assistant, Studio's built-in AI helper. Covers chat threads, screen capture subagent, asking questions/explaining code, editing scripts and objects, searching/inserting Creator Store assets, generating materials, textured meshes, procedural models (50 per 24h), mesh segmentation with recommended part names, and Planning Mode with editable Markdown plans.

## Tips
- [page](https://create.roblox.com/docs/assistant/guide) **[[ai-and-tools]]** Select a Part before prompting /generate_mesh so Assistant uses its size and location as a bounding box, keeping the generated mesh within that space.
- [page](https://create.roblox.com/docs/assistant/guide) **[[ai-and-tools]]** Set a maximum triangle count for generated meshes when needed; lower values give lower-poly results. Default is 10,000.
- [page](https://create.roblox.com/docs/assistant/guide) **[[ai-and-tools]]** Use /generate_mesh with a reference image instead of text when you need a specific look; it accepts one input type per request, not both.
- [page](https://create.roblox.com/docs/assistant/guide) **[[building-art-and-assets]]** Segment generated or imported meshes into parts so you can apply different materials, scripts, or replace components without regenerating the whole model.
- [page](https://create.roblox.com/docs/assistant/guide) **[[building-art-and-assets]]** Use recommended part names (e.g. body, left front wheel, blade) for common object types; they produce the most reliable segmentation. Max five parts per /segment_mesh run.
- [page](https://create.roblox.com/docs/assistant/guide) **[[ai-and-tools]]** Run /plan or choose Plan mode for complex requests and review the Markdown plan before clicking Build; plans never auto-execute.
- [page](https://create.roblox.com/docs/assistant/guide) **[[ai-and-tools]]** Use separate chats per task and the branch icon to fork a response into a new chat, keeping the original context intact. Each chat has its own context window.
- [page](https://create.roblox.com/docs/assistant/guide) **[[team-and-budget]]** Avoid editing the same place from multiple devices at once; chat history syncs via the cloud and simultaneous work causes conflicts.
- [page](https://create.roblox.com/docs/assistant/guide) **[[ai-and-tools]]** Use Creator Store search filters (price, audio duration, verified creators) and asset type filters when inserting assets via Assistant.

## Numbers
- [page](https://create.roblox.com/docs/assistant/guide) Procedural model generation limit: **50 per 24-hour rolling window** (Procedural models via /generate_procedural_model)
- [page](https://create.roblox.com/docs/assistant/guide) Default max triangle count for generated meshes: **10,000** (Optional input for /generate_mesh)
- [page](https://create.roblox.com/docs/assistant/guide) Max parts per generated model: **8** (Segmentation via Part Names entries)
- [page](https://create.roblox.com/docs/assistant/guide) Preview images per mesh generation: **4** (Shown after Confirm on segmentation plan)
- [page](https://create.roblox.com/docs/assistant/guide) Max parts per /segment_mesh run: **5** (Run again on segmented mesh to exceed five)

## Tools
Roblox Studio Assistant, /generate_mesh, /generate_procedural_model, /segment_mesh, /insert_asset, /plan, Material Generator (lightweight), 3D Importer

## He points to
- Prompt guide and examples (Roblox docs)
- Roblox Staff livestream on Assistant tips
- Behaviors Reference game .rbxl file

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[team-and-budget]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
