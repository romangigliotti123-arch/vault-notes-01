---
title: "[Studio Beta] Introducing Procedural Models: Build Parametrized 3D Models with Code or AI"
url: https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-04-23
views: 937
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Studio Beta] Introducing Procedural Models: Build Parametrized 3D Models with Code or AI

[Open](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) | Roblox DevForum | 937 views | 2026-04-23

## Summary
Roblox Studio beta announcement for Procedural Models: ProceduralModel instances regenerate geometry via a Generator ModuleScript (Attributes map + OnGenerate) when Size or attributes change. Covers setup, sandboxing, Assistant/MCP generation, known issues and FAQs.

## Tips
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[building-art-and-assets]]** Enable via File → Beta Features → 'Edit-Time Procedural Models', then restart Studio. Insert Object → ProceduralModel gives a template.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[building-art-and-assets]]** Write OnGenerate to only write into targetContainer; never modify the DataModel directly, so undo, Team Create and Dragger integration work.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[scripting-and-performance]]** Call parameters:Pause() inside long generation loops to spread work across frames and avoid dropping frames.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[building-art-and-assets]]** Generate geometry around the origin at the given Size; the system applies PivotTo/ScaleTo positioning automatically.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[building-art-and-assets]]** To make bespoke manual edits, finalize parameters then clear the Generator property to bake the result; otherwise edits to the Generated folder are overwritten.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[building-art-and-assets]]** Doubling Size regenerates with twice the extent, while doubling Scale uniformly scales the existing results; choose based on whether details should stay constant.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[client-server-and-remotes]]** The peer that changes a parameter performs generation; server-side changes replicate results, client runtime changes generate locally.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[anti-exploit-and-security]]** Generators are sandboxed when inserted from the Creator Store: no DataStore/HttpRequest access and no AccessOutsideWrite, so keep untrusted generators locked down.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[ai-and-tools]]** Use /generate_procedural_model with a text prompt or reference image in Assistant or Studio MCP; reference images improve accuracy.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[common-mistakes]]** Don't expect generators to modify existing model contents; copy a template model under the generator and clone it during generation.
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) **[[common-mistakes]]** Scale tool can leave a ProceduralModel stuck at zero size; fix by editing the Size property in Properties.

## Numbers
- [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056) Beta access: **Edit-Time Procedural Models Studio beta, available to all creators** (Announced April 2026 in Roblox Studio beta features)

## Tools
Roblox Studio, Assistant, Studio MCP, generate_procedural_model

## He points to
- Full ProceduralModel documentation (linked from post)

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
