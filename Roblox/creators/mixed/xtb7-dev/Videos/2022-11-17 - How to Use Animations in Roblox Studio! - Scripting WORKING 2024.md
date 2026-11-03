---
title: "How to Use Animations in Roblox Studio! - Scripting *WORKING 2024*"
url: https://youtu.be/k2p9KMrlSAA
creator: XTB7
official: false
advice_density: low
date: 2022-11-17
views: 3279
transcript: auto-captions
confidence: high
tags: [roblox, xtb7-dev, youtube-learn]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# How to Use Animations in Roblox Studio! - Scripting *WORKING 2024*

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/k2p9KMrlSAA) | xtb7-dev | 3,279 views | 2022-11-17

## Summary
Tutorial on animating NPCs/characters in Roblox Studio via scripting: copy default Animate script's walk animation into an Animator in a dummy's Animations folder, load it with humanoid:LoadAnimation, play while moving, stop after MoveTo finishes, and swap in a custom animation ID.

## Tips
- [0:18](https://youtu.be/k2p9KMrlSAA?t=18) **[[building-art-and-assets]]** Add an Animator object under the Humanoid before loading animations; animations only play through an Animator.
- [1:24](https://youtu.be/k2p9KMrlSAA?t=84) **[[3d-modeling-rigging-and-animation]]** Copy default animations from the Animate script of a character model to reuse Roblox's built-in walk animation.
- [2:15](https://youtu.be/k2p9KMrlSAA?t=135) **[[client-server-and-remotes]]** Put the animation script inside the model being animated so script.Parent points to the character.
- [2:56](https://youtu.be/k2p9KMrlSAA?t=176) **[[scripting-and-performance]]** Use humanoid.MoveToFinished:Wait() before stopping the animation so the animation stops when the character arrives.

## Tools
Roblox Studio, Animator, Animation objects, Animate script

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[xtb7-dev - How to make successful Roblox games]]
