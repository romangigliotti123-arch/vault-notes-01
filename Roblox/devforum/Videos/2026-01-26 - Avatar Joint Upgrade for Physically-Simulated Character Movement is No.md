---
title: "Avatar Joint Upgrade for Physically-Simulated Character Movement is Now Live!"
url: https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-01-26
views: 1066
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Avatar Joint Upgrade for Physically-Simulated Character Movement is Now Live!

[Open](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) | Roblox DevForum | 1,066 views | 2026-01-26

## Summary
Roblox Physics Team announces Avatar Joint Upgrade graduating from Studio Beta to live. R15 joints become force/torque-limited AnimationConstraints plus BallSocketConstraints, enabling physical animation and easy ragdolls. Opt-in via StarterPlayer.AvatarJointUpgrade; default flips to Enabled in H2 2026.

## Tips
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[scripting-and-performance]]** Search codebase (Ctrl+Shift+F) for Motor6D references; C0/C1/Part0/Part1 setters will error on AnimationConstraints, so switch to Attachments.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[scripting-and-performance]]** Scripts using instance:IsA("Motor6D") will not detect AnimationConstraints; update those checks.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[common-mistakes]]** Don't rely on opt-out long-term: it is temporary; migrate experiences before Phase 2 (H2 2026) when the default flips to Enabled and Phase 3 removes the property.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[development-process-and-speed]]** Enable StarterPlayer.AvatarJointUpgrade now to test breaking changes early; Phase 1 keeps the default Disabled with no breaking change.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[physics-pathfinding-and-npc-ai]]** Set IsKinematic=False on joints to get force/torque-driven behavior; kinematic joints stay locked to animation, as with Motor6D.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[physics-pathfinding-and-npc-ai]]** Disable or weaken AnimationConstraints and disable CharacterBreakJointsOnDeath to create immediate realistic ragdolls on death.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[optimization-and-streaming]]** The base joint upgrade has little to no performance impact, per the FAQ.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[common-mistakes]]** Upgraded joints apply only to players spawned via player/HumanoidDescription flows; existing NPC models in the place are not upgraded.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[client-server-and-remotes]]** Expect choppy replication of physically simulated parts on other clients when a character mixes kinematic and physics joints and animates the torso.
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) **[[physics-pathfinding-and-npc-ai]]** R6 is not covered by the upgrade; add BallSocketConstraints and AnimationConstraints via script if needed.

## Numbers
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) Phase 2 target: **H2 2026 (default flips to Enabled)**
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) AnimationConstraints default IsKinematic: **True for avatar joints; False for standalone AnimationConstraints**
- [page](https://devforum.roblox.com/t/avatar-joint-upgrade-for-physically-simulated-character-movement-is-now-live/4298561) Post count likes: **1066 likes on DevForum post**

## Tools
StarterPlayer.AvatarJointUpgrade, AnimationConstraint, BallSocketConstraint, CharacterBreakJointsOnDeath, Physically Simulated Characters Demo

## He points to
- Studio Beta announcement post for Avatar Joint Upgrade

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[development-process-and-speed]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
