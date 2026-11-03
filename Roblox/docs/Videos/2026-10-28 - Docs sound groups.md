---
title: "Docs: sound / groups"
url: https://create.roblox.com/docs/sound/groups.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: sound / groups

[Open](https://create.roblox.com/docs/sound/groups.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on SoundGroups: creating them under SoundService, assigning Sounds to groups, nesting into mix trees, adjusting volume with multipliers, and ducking via CompressorSoundEffect. Notes SoundGroup is discouraged in favor of audio objects.

## Tips
- [page](https://create.roblox.com/docs/sound/groups) **[[sound-and-music]]** SoundGroup is discouraged now; prefer the newer audio objects (see Audio objects docs) for mixing and effects.
- [page](https://create.roblox.com/docs/sound/groups) **[[sound-and-music]]** Keep all SoundGroups in one location under SoundService for organization as audio grows.
- [page](https://create.roblox.com/docs/sound/groups) **[[sound-and-music]]** Assign Sounds to a SoundGroup via the Properties SoundGroup field; parenting in the workspace does not assign them, and location only affects where audio emits from.
- [page](https://create.roblox.com/docs/sound/groups) **[[sound-and-music]]** Nest SoundGroups into categories (e.g. player abilities vs environment) so you can adjust a whole category's volume at once.
- [page](https://create.roblox.com/docs/sound/groups) **[[sound-and-music]]** Use SoundGroup.Volume as a 0-10 multiplier to test volume balance without editing each Sound; child volumes multiply (0.5 Sound x 0.5 group = 0.25).
- [page](https://create.roblox.com/docs/sound/groups) **[[sound-and-music]]** Duck low-priority groups (music, ambience) under high-priority ones (GUI, weapons, dialogue) using CompressorSoundEffect with SideChain set to the priority Sound or SoundGroup.
- [page](https://create.roblox.com/docs/sound/groups) **[[sound-and-music]]** Tune CompressorSoundEffect values per source audio; Threshold -80 to 0 dB, Attack and Release 0.001 to 1 s, Ratio 1 to 50. Playtest and adjust.

## Numbers
- [page](https://create.roblox.com/docs/sound/groups) SoundGroup.Volume multiplier range: **0 to 10**
- [page](https://create.roblox.com/docs/sound/groups) CompressorSoundEffect.Threshold range: **-80 (full compression) to 0 dB (full volume)**
- [page](https://create.roblox.com/docs/sound/groups) CompressorSoundEffect.Attack range: **0.001 to 1 second**
- [page](https://create.roblox.com/docs/sound/groups) CompressorSoundEffect.Release range: **0.001 to 1 second**
- [page](https://create.roblox.com/docs/sound/groups) CompressorSoundEffect.Ratio range: **1 (no compression) to 50**

## Tools
Roblox Studio Explorer, Properties window, CompressorSoundEffect, SoundGroup

## He points to
- Audio objects documentation

## Topics
[[sound-and-music]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
