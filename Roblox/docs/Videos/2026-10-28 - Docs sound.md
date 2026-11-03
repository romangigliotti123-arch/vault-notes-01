---
title: "Docs: sound"
url: https://create.roblox.com/docs/sound.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: sound

[Open](https://create.roblox.com/docs/sound.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on the legacy Sound system: Sound objects, positional vs background audio via parenting, SoundGroups as mixers, and dynamic effects (Equalizer, Compressor, Reverb). Notes that a newer Audio object set exists and is recommended for more control.

## Tips
- [page](https://create.roblox.com/docs/sound) **[[sound-and-music]]** Use the newer Audio objects instead of Sound for more control and robust use cases; the page itself warns the legacy Sound system is superseded.
- [page](https://create.roblox.com/docs/sound) **[[sound-and-music]]** For positional audio, parent the Sound to a 3D object or Attachment so users only hear it near that position.
- [page](https://create.roblox.com/docs/sound) **[[sound-and-music]]** For position-independent background audio (music, ambience), insert the Sound directly into Workspace or SoundService.
- [page](https://create.roblox.com/docs/sound) **[[sound-and-music]]** Group related Sounds or sub-SoundGroups under a SoundGroup to control volume and effects for many signals at once.
- [page](https://create.roblox.com/docs/sound) **[[sound-and-music]]** Apply EqualizerSoundEffect to muffle sounds, e.g. rain, and CompressorSoundEffect to cap a sound's maximum volume.
- [page](https://create.roblox.com/docs/sound) **[[sound-and-music]]** Add ReverbSoundEffect to interior spaces for realistic sound reflections.
- [page](https://create.roblox.com/docs/sound) **[[sound-and-music]]** Source free-to-use audio from the Creator Store or import your own audio assets.

## Tools
Sound, SoundGroup, SoundService, Attachment, EqualizerSoundEffect, CompressorSoundEffect, ReverbSoundEffect, Creator Store

## He points to
- Audio (newer audio objects and effects documentation)

## Topics
[[sound-and-music]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
