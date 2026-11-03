---
title: "Docs: animation / graph-editor-state-machine"
url: https://create.roblox.com/docs/animation/graph-editor-state-machine.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / graph-editor-state-machine

[Open](https://create.roblox.com/docs/animation/graph-editor-state-machine.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Graph Editor state machines in the Animation Graph Editor. Explains states (clips, blend nodes, nested state machines), transitions driven by Expression or Finished conditions, priorities, durations, and easing curves. Walks through a Locomotion/Fall/LandIdle example using a Grounded boolean parameter.

## Tips
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) **[[building-art-and-assets]]** Set Play Mode to OnceAndHold on fall and land clips so they hold their final pose until the transition fires.
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) **[[building-art-and-assets]]** Name state machine states to exactly match the state machine input names; the state name must match the input name.
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) **[[building-art-and-assets]]** Assign distinct Priority values to competing transitions; equal priorities pick randomly among true expressions, making behaviour unpredictable.
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) **[[building-art-and-assets]]** Use BeforeFinished on a Finished transition to start blending before a clip ends, avoiding a visible pause when returning to locomotion.
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) **[[building-art-and-assets]]** Drive transitions from gameplay code by updating boolean graph parameters (e.g. Grounded) as the character leaves or touches the ground.

## Numbers
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) Transition Length (Locomotion to Fall): **0.2 seconds** (Expression not Grounded, Wait For Expression)
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) Transition Length (Fall to LandIdle): **0.1 seconds** (Expression Grounded)
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) Transition Length (LandIdle to Locomotion): **0.2 seconds** (Wait For Finished, When BeforeFinished)
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) Default transition Duration: **0.15 seconds** (Blend time into destination state)
- [page](https://create.roblox.com/docs/animation/graph-editor-state-machine) Priority range: **0 to 65,535** (Higher values take precedence)

## Tools
Animation Graph Editor, State Machine view, Graph parameters

## He points to
- JumpFallLandRunExample reference place
- API integration docs (graph parameters)

## Topics
[[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
