---
title: "Docs: tutorials / use-case-tutorials / audio / add-3D-audio"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / audio / add-3D-audio

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on adding 3D audio using the Gingerbread House sample. Covers audio object types (AudioPlayer, AudioEmitter, AudioListener, Wire, device I/O), looping ambient audio, one-shot event feedback, object interaction sounds, and proximity-triggered character dialogue, with setup steps and sample code.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Set SoundService.DefaultListenerLocation to Character so an AudioListener is auto-created under each player's HumanoidRootPart.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Create seamless loops by matching end and start points precisely; use Reaper or Audacity to find a zero crossing and cut carefully.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Set AudioEmitter DistanceAttenuation to {0: 1}, {20: 0.8}, {40: 0.4}, {80: 0} for a gradual falloff every 20 studs.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Use a LocalScript calling AudioPlayer:Play() for looping ambience that should start when players join and stop when they leave.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Pair one-shot 3D audio with visual feedback for object interactions; this improves clarity and accessibility for players with visual impairments.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Don't rely on IsPlaying going true-to-false for state changes; it only fires false-to-true due to replication timing, so also listen to AudioPlayer.Ended.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Use a debounce (false to true to false after audio ends) on volume triggers to prevent repeated playback while players stay inside.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Use non-positional Audio (2D) for background music, UI sounds and voiceover cutscene dialogue; positional audio is for in-world sources.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[sound-and-music]]** Use 3D audio for situational events (e.g. door opening after objective completion) so players know where to go regardless of their position.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) **[[ui-ux-design]]** Use character dialogue audio in volumes near the spawn area to guide new players toward the objective.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) DistanceAttenuation falloff: **Full volume under 20 studs; 0.8 at 20, 0.4 at 40, 0 at 80 studs** (Sample AudioEmitter attenuation curve for waterfall)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) Door animation: **Moves 15 studs down over 2 seconds** (Gingerbread House door opens after 3 gumdrops)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) Gumdrops required: **3** (Objective threshold triggering door event audio)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) Button tween duration: **0.2 seconds, Exponential easing** (Button press animation in object interaction example)

## Games
- **Gingerbread House (sample)**: Demonstrates looping ambience, event feedback on door, button interaction sounds, and snowman dialogue volume.
- **Laser Tag (template)**: Blaster pop and reload beep sounds give positional awareness of nearby combat.
- **Plant (sample)**: Plant, water, harvest and place actions each have distinct sounds reinforcing interaction.
- **Beyond the Dark (showcase)**: Space station NPC dialogue delivers lore and direction via periodic positional audio.

## Tools
Roblox Studio, AudioPlayer, AudioEmitter, AudioListener, Wire, Reaper, Audacity

## He points to
- Creating Perfect Audio Loops (Roblox docs)
- Add 2D audio (Roblox docs)
- Debounce - Detect collisions (Roblox docs)
- Gingerbread House - Complete Audio (sample place)
- Gingerbread House - Start .rbxl (sample place)

## Topics
[[sound-and-music]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
