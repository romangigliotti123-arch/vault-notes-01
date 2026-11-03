---
title: "STOP Asking Claude to Make Your Whole Roblox Game"
url: https://youtu.be/WA4RzzT39Dw
creator: MonarchDev
official: false
advice_density: medium
date: 2026-10-26
views: 16258
transcript: auto-captions
confidence: medium
tags: [roblox, monarchsilgrit, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# STOP Asking Claude to Make Your Whole Roblox Game

[Watch](https://youtu.be/WA4RzzT39Dw) | MonarchSilgrit | 16,258 views | 2026-10-26

## Summary
Argues AI models cannot one-shot a full Roblox game. Advises building in stages: core features first, then map design, models, and lighting last. Recommends specific, iterative prompts over "make it better", compressing long sessions, and avoiding parallel AI sessions editing the same code. Mostly opinion and promotion.

## Tips
- [0:00](https://youtu.be/WA4RzzT39Dw?t=0) **[[ai-and-tools]]** Don't expect AI to generate a complete game from one prompt. Build iteratively in stages, with frequent detailed instructions.
- [1:04](https://youtu.be/WA4RzzT39Dw?t=64) **[[development-process-and-speed]]** Build order: create the place, then core features first, then layer everything else on top.
- [1:16](https://youtu.be/WA4RzzT39Dw?t=76) **[[building-art-and-assets]]** Work on visuals in tiers: overall map design first, then models, then lighting and polish last.
- [2:26](https://youtu.be/WA4RzzT39Dw?t=146) **[[ai-and-tools]]** Avoid vague prompts like 'make this better'. Name the specific problem and the target look, e.g. 'too low-saturation, make it cartoonish and highly saturated'.
- [3:06](https://youtu.be/WA4RzzT39Dw?t=186) **[[building-art-and-assets]]** Give concrete art direction: sunset lighting, outlined characters for a cartoon look, and specified base colours.
- [3:18](https://youtu.be/WA4RzzT39Dw?t=198) **[[thumbnails-icons]]** Generate a colour palette first (e.g. with ChatGPT), then reuse it as the baseline for all later visual work.
- [4:48](https://youtu.be/WA4RzzT39Dw?t=288) **[[ai-and-tools]]** Long AI sessions degrade (around 900k of a 1M context in his example). Compress or start fresh sessions rather than expecting one long prompt to succeed.
- [5:20](https://youtu.be/WA4RzzT39Dw?t=320) **[[development-process-and-speed]]** Don't run multiple AI sessions editing the same code at once; they overwrite each other and cause broken code loops. Use one main session for integration.
- [5:20](https://youtu.be/WA4RzzT39Dw?t=320) **[[version-control-and-tooling]]** Current Roblox API and MCP connections are limited, so parallel AI work on shared scripts clashes. Split work by file or feature with one integrator.
- [5:20](https://youtu.be/WA4RzzT39Dw?t=320) **[[ai-and-tools]]** Basic coding knowledge helps you judge and fix AI output; users without it can still succeed, just more slowly.
- [4:00](https://youtu.be/WA4RzzT39Dw?t=240) **[[building-art-and-assets]]** AI-generated meshes often need conversion for Roblox and may be lower quality; check them against Roblox's polygon requirements before relying on them.

## Numbers
- [4:48](https://youtu.be/WA4RzzT39Dw?t=288) context window: **~900,000 of ~1,000,000 tokens used in a long session** (Speaker's example of a session that needs compressing)
- [6:16](https://youtu.be/WA4RzzT39Dw?t=376) speaker training: **3 years of coding school, now a master's in AI** (Speaker's stated background, not a benchmark)

## Tools
Claude, ChatGPT, Roblox Studio, Blender, MCP connections

## Quotes
- [2:26](https://youtu.be/WA4RzzT39Dw?t=146) "You can't simply say, "Oh, yeah, make this better." What does it even mean?"
- [5:20](https://youtu.be/WA4RzzT39Dw?t=320) "you cannot have multiple sessions working on the same thing at the same time simply because they'll clash one another"

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[development-process-and-speed]] [[thumbnails-icons]] [[version-control-and-tooling]]

Back to [[MonarchSilgrit - How to make successful Roblox games]]
