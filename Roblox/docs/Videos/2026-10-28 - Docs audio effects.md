---
title: "Docs: audio / effects"
url: https://create.roblox.com/docs/audio/effects.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: audio / effects

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/audio/effects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on audio effects. Explains how to insert audio effects (Equalizer, Compressor, Reverb, Chorus, Distortion, Echo, Flanger, Pitch Shifter, Tremolo, Fader, Analyzer) into the 2D/3D audio wiring between audio players and output, and what each effect is useful for. Notes effect order matters.

## Tips
- [page](https://create.roblox.com/docs/audio/effects) **[[sound-and-music]]** Insert effects between the audio player and the output in the Audio object wiring; unwired streams play the original recording unchanged.
- [page](https://create.roblox.com/docs/audio/effects) **[[sound-and-music]]** Effect order changes the result: Chorus then Distortion can sound different from Distortion then Chorus. Test orders deliberately.
- [page](https://create.roblox.com/docs/audio/effects) **[[sound-and-music]]** Wire multiple audio players through one effect instance instead of duplicating effect objects with identical settings.
- [page](https://create.roblox.com/docs/audio/effects) **[[sound-and-music]]** Use AudioEqualizer to muffle all game audio when a player is underwater.

## Tools
AudioEqualizer, AudioCompressor, AudioReverb, AudioChorus

## Topics
[[sound-and-music]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
