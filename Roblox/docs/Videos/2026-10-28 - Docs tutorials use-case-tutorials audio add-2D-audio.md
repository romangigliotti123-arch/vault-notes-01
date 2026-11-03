---
title: "Docs: tutorials / use-case-tutorials / audio / add-2D-audio"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / audio / add-2D-audio

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on adding 2D audio (non-positional sound). Covers the AudioPlayer, AudioDeviceOutput and Wire object chain, looping background music via a client script with DefaultListenerLocation set to Character, one-shot gameplay feedback (gumdrop pickups with volume boost), and UI button feedback with a jingle paired with tweened visual state.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[building-art-and-assets]]** Set SoundService.DefaultListenerLocation to Character so a default listener follows the player; the engine then auto-creates an AudioDeviceOutput under SoundService.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[sound-and-music]]** Use looping 2D background music so the game is never silent; silence can disorient players. Set AudioPlayer Volume low (e.g. 0.2) so other sounds stay audible.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[sound-and-music]]** Create seamless loops by matching end and start points at a zero crossing in third-party editors like Reaper or Audacity.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[sound-and-music]]** Set the looping AudioPlayer's RunContext-based script to Client and call Play() so music starts as soon as the player joins.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[player-psychology-and-game-feel]]** Choose opening music to set the intended mood immediately on join; swapping an upbeat track for a metal track changes the experience.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[player-psychology-and-game-feel]]** Prioritise important feedback with louder volume: the sample raised gumdrop-collect sound to Volume 3 versus lower volume for jump sounds.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[player-psychology-and-game-feel]]** Give immediate one-shot audio feedback on objectives (score, health, level progress) so players understand the result of actions without relying on visuals alone.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[ui-ux-design]]** Pair UI interaction sounds with visual feedback (tween position, tint) so the state is clear for players with visual impairments and multiple senses are covered.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[scripting-and-performance]]** Listen to AudioPlayer.Ended as well as IsPlaying changes, because IsPlaying false-to-true events fire but true-to-false may not replicate reliably from server to client.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) **[[scripting-and-performance]]** Prevent rapid-click audio restarts by checking IsPlaying/Ended before replaying a UI sound.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) Looping background music Volume: **0.2** (Low volume so other audio sources remain audible)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) Gumdrop one-shot AudioPlayer Volume: **3** (Raised volume so gumdrop sound is heard over other sources)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) Gumdrop TimePosition: **0.15** (Starts clip closer to the actual chomp sound)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) Button tween duration: **0.2 seconds** (Exponential easing for pressed/default button state)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) Gumdrops required to open door: **3** (Sample objective triggers door animation and event audio)

## Games
- **Gingerbread House (sample place)**: Reference place for 2D audio: looping music, gumdrop pickup chomp at boosted volume, and peppermint button jingle with tween feedback.
- **Platformer template**: Jump whoosh and coin ding are instantly recognisable one-shot feedback; coin sound is slightly louder as more valuable information.
- **UGC Homestore template**: Purchase buttons provide visual and auditory feedback across in-focus, hover and selected states for accessibility.
- **Hazardous Space Station (sample)**: Background music transforms a hollow, lifeless space into an ominous, dangerous atmosphere.

## Tools
Roblox Studio, Reaper, Audacity

## He points to
- Add 3D audio (Roblox docs)
- Creating Perfect Audio Loops (Roblox docs)

## Topics
[[building-art-and-assets]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[sound-and-music]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
