---
title: "Docs: parts / procedural-models"
url: https://create.roblox.com/docs/parts/procedural-models.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / procedural-models

[Open](https://create.roblox.com/docs/parts/procedural-models.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on ProceduralModels: parameter-driven Models whose generator ModuleScript's OnGenerate(params, targetContainer) rebuilds contents when attributes or Size change. Covers insertion methods, regeneration/dirty-state flow, sizing vs scaling, timeouts via Pause, undo, sandboxing, nesting and limitations.

## Tips
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[common-mistakes]]** Procedural models can make permanent edit-time changes to your game; review Creator Store generators before trusting them, since they are sandboxed by default for safety.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[anti-exploit-and-security]]** Keep Creator Store procedural model generators Sandboxed=true; a sandboxed generator typically needs RunServerScript, CreateInstances and Basic capabilities.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[optimization-and-streaming]]** Call parameters:Pause() liberally at the start of loops in generators; it is inexpensive and prevents Script Timeout errors by deferring work to later frames.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[building-and-level-design]]** Generate content around the origin in targetContainer and never modify the main DataModel hierarchy directly from OnGenerate.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[building-art-and-assets]]** Use Size for structural changes (regenerates content) and Scale for uniform resizing (ScaleTo on existing results) to avoid unnecessary regeneration.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[development-process-and-speed]]** Use parameter-driven generators to iterate non-destructively: change attributes like StepSize instead of rebuilding models by hand.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[scripting-and-performance]]** Procedural models are not supported inside Actor instances; do not plan generation there.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[data-persistence]]** If a place is saved while a model is dirty, regeneration is queued and runs on next load; failed generation clears dirty state until the next parameter change.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[scripting-and-performance]]** If parameters change while a generation thread is yielded, the outstanding generation is cancelled and restarted with the new parameters, so avoid unnecessary yields.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[testing-debugging-and-qa]]** Set Workspace.SandboxedInstanceMode = Experimental to expose Sandboxed and Capabilities properties on generator ModuleScripts when debugging permissions.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[building-and-level-design]]** Nested ProceduralModels generate top-down in the same step; deeper nesting generates last, so structure hierarchies with that order in mind.
- [page](https://create.roblox.com/docs/parts/procedural-models) **[[ai-and-tools]]** Procedural models can be generated with Assistant or the Roblox Studio MCP server, or inserted from the Creator Store and customized.

## Numbers
- [page](https://create.roblox.com/docs/parts/procedural-models) Required sandbox capabilities: **RunServerScript, CreateInstances, Basic** (Typical minimum for sandboxed generator module)

## Tools
Roblox Studio, Assistant, Roblox Studio MCP server, Creator Store

## He points to
- Creator Store

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]] [[building-and-level-design]] [[building-art-and-assets]] [[common-mistakes]] [[data-persistence]] [[development-process-and-speed]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
