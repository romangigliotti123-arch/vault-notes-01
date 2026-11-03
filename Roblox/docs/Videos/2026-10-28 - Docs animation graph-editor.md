---
title: "Docs: animation / graph-editor"
url: https://create.roblox.com/docs/animation/graph-editor.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / graph-editor

[Open](https://create.roblox.com/docs/animation/graph-editor.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for the Animation Graph Editor: building node-based animation graphs (Clip, Add, parameters), publishing AnimationGraphDefinition assets, driving them via AnimationTrack:SetParameter, transition timing settings, and replication differences between Automatic and Server AuthorityMode.

## Tips
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[building-art-and-assets]]** Keep clip authoring in the Animation Editor and use the Animation Graph Editor only to organize clips into logic trees driving behaviour.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[core-loops-and-game-design]]** Test graphs with different weights, speeds, playmodes and animations in Studio play mode before publishing.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[scripting-and-performance]]** Use AnimationTrack:SetParameter from every script that runs the graph; NPCs need RunServer, server-authority players need both RunServer and RunClient.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[client-server-and-remotes]]** Set Workspace.AuthorityMode before creating the Animate script; it determines the replication strategy for the graph.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[scripting-and-performance]]** Multiple SetParameter calls in one frame are coalesced last-writer-wins; set only the final value per frame.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[data-persistence]]** Leave PreviewInStudio true to iterate on unpublished graphs locally; it is not supported in Server authority mode.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[ai-and-tools]]** Use Graph > Create Animate script to generate the Animate, RunClient and RunServer scaffolding instead of writing it by hand.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[client-server-and-remotes]]** In Server authority mode the owning client enables PredictionMode for rollback-based local prediction; the server reconciles on mismatch.
- [page](https://create.roblox.com/docs/animation/graph-editor) **[[common-mistakes]]** Automatic mode: other clients see parameter updates with a small delay (one send interval plus network latency); do not rely on instant remote parameter state.

## Numbers
- [page](https://create.roblox.com/docs/animation/graph-editor) Default Walk animation ID: **507777826** (Example clip in the docs' basic graph tutorial)
- [page](https://create.roblox.com/docs/animation/graph-editor) Default Wave animation ID: **507770239** (Example additive clip in the docs' basic graph tutorial)
- [page](https://create.roblox.com/docs/animation/graph-editor) Transition curve options: **Linear, CubicV2** (Only these PoseEasingStyle values are supported for transitions)
- [page](https://create.roblox.com/docs/animation/graph-editor) BeforeFinished overlap example: **0.2 s transition starts in final 0.2 s of clip** (Blend overlaps end of animation when WaitFor is Finished)

## Tools
Roblox Studio Animation Graph Editor, Animation Editor, Avatar tab Character > My Avatar, Graph > Create Animate script, AnimationTrack:SetParameter, Enum.AnimationNodeType, Enum.PredictionMode

## He points to
- Animation Graph Reference File (Roblox reference place)
- Enum.AnimationNodeType docs
- Transition properties docs

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
