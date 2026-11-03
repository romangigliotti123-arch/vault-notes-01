---
type: research-source
id: gh-Roblox-creator-docs-f-content-en-us-audio-assets.md
title: "Roblox/creator-docs/content/en-us/audio/assets.md"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/creator-docs/blob/HEAD/content/en-us/audio/assets.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: medium
tags: ["research-source", "github", "open-cloud-automation", "other"]
---
# gh-Roblox-creator-docs-f-content-en-us-audio-assets.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on audio assets: finding audio in the Creator Store, and import requirements (formats, size, duration, sample rate, channels) and quotas for Asset Manager, Creator Dashboard and Open Cloud. Does not cover Blender, bpy, mesh export or rigging, so it is off-topic for this research.

## Claims
- c1: Roblox audio import accepts single-track .mp3, .ogg, .wav or .flac under 20 MB and 7 minutes, sample rate at most 48 kHz, mono or stereo/5.1 channels. *(doc, high; other)*
- c2: ID-verified creators can import 2,000 free audio assets per 30 days; unverified creators get 100 per 30 days. *(doc, high; other)*
- c3: Audio can be uploaded via Open Cloud Create Asset endpoint (POST /assets/v1/assets) with x-api-key header, assetType Audio, and userId or groupId creator context. *(doc, high; open-cloud-automation)*

## Numbers
- n1: **max file size**: 20 MB 
- n2: **max duration**: 7 minutes 
- n3: **max sample rate**: 48 kHz 
- n4: **verified audio import quota**: 2,000 per 30 days 
- n5: **unverified audio import quota**: 100 per 30 days 

## Points to
- https://github.com/Roblox/creator-docs/blob/HEAD/content/en-us/audio/assets.md
