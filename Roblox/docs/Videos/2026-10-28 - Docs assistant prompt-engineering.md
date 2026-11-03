---
title: "Docs: assistant / prompt-engineering"
url: https://create.roblox.com/docs/assistant/prompt-engineering.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: assistant / prompt-engineering

[Open](https://create.roblox.com/docs/assistant/prompt-engineering.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official Assistant prompt guide: best practices (be specific, use selection, specify edit vs run time, multi-step prompts with ### separators, asset-generation prompting, procedural model prompting with reference images) plus example prompts across game mechanics, camera, UI, and building.

## Tips
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[ai-and-tools]]** Be specific: use exact instance names, name the function/service to use (e.g. TweenService), and state the instance type such as part or model.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[ai-and-tools]]** If Assistant fails, add more detail and retry; outputs are non-deterministic, so small prompt tweaks can change results.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[ai-and-tools]]** Use selection in Studio to reference objects in prompts, e.g. to modify multiple objects, duplicate them, or continue a placement pattern.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[scripting-and-performance]]** Distinguish edit time from run time: ask Assistant to 'add a script that does X' for runtime behaviour, since it otherwise biases toward edit-time changes.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[ai-and-tools]]** Separate code from questions with ### delimiters in multi-step prompts to get better step-by-step explanations.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[building-art-and-assets]]** For asset generation, start with the object name and add material, age and distinctive details; omit backgrounds, camera angles, lighting and generic quality terms.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[building-art-and-assets]]** For procedural models, explicitly name the properties to expose and define how parts scale with size or count (e.g. add chairs proportionally when table length grows).
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[building-art-and-assets]]** For procedural model reference images, use .png with good lighting, a clear subject, simple background, and isometric or 3/4 angles; avoid low-poly style images.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[building-art-and-assets]]** For objects that cannot be captured from one angle, include multiple viewpoints in a single reference image.
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) **[[ai-and-tools]]** Procedural model generation is slower than text replies; you can type the next prompt while it generates.

## Numbers
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) Example spec: NPC detection range: **30 studs (laser NPC), 50 studs (look-at/chase NPC), 10 studs (patrol chase)** (Sample prompt thresholds from the guide)
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) Example time cycle: **1 in-game hour per real second; 3pm start; spotlights on at 7pm, off at 8am** (Day/night cycle example prompt)
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) Example scatter randomization: **0-5 mushrooms per tree** (Scatter-with-randomization example prompt)
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) Health bar warning threshold: **turns red below 20% health; touch part deals 10% damage** (Health bar example prompt)
- [page](https://create.roblox.com/docs/assistant/prompt-engineering) Modular track curvature range: **0-90 degrees** (Procedural train track example prompt)

## Tools
Roblox Assistant, TweenService, Roblox Studio Selection

## He points to
- Roblox forum (share prompts and games to help improve Assistant)

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
