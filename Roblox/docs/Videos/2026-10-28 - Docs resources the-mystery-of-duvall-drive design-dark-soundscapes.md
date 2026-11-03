---
title: "Docs: resources / the-mystery-of-duvall-drive / design-dark-soundscapes"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / design-dark-soundscapes

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on designing dark horror soundscapes for The Mystery of Duvall Drive. Covers volumetric audio (SoundService.VolumetricAudio, invisible anchored parts with Sound objects, RollOff distances) and nested SoundGroup mixing with CompressorSoundEffect ducking for prioritising progression audio.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) **[[building-art-and-assets]]** Enable SoundService.VolumetricAudio, then put a Sound inside an anchored, non-collidable, transparent Part sized to the sound source (e.g. a car) so audio spreads across its surface.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) **[[sound-and-music]]** Use volumetric emitters for large or area sounds (rain, rooms, waterfalls, cities) rather than point sounds; disabling volumetric audio collapses them to one point.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) **[[sound-and-music]]** Keep a constant ambient sound bed so the game never feels silent when the player is idle.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) **[[sound-and-music]]** Set Sound RollOffMinDistance and RollOffMaxDistance to control falloff; the example used 15 and 60 studs for looping rain.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) **[[sound-and-music]]** Nest SoundGroups into a priority mix tree; put a CompressorSoundEffect on low-priority groups with Sidechain set to the high-priority group to duck them.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) **[[sound-and-music]]** Tune CompressorSoundEffect Threshold (lower = triggers on quieter signals), Ratio (higher = more ducking), and Attack/Release by ear.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) **[[building-and-level-design]]** Place sounds of interest in every room so there is always a more intriguing sound in the distance, encouraging players to explore.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) RollOffMaxDistance: **60 studs** (Looping rain surface sound on a car part in example)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) RollOffMinDistance: **15 studs** (Full volume distance for looping rain surface sound on a car part)

## Games
- **The Mystery of Duvall Drive**: Horror game using volumetric emitters for most SFX and nested SoundGroup ducking so progression audio stands out over ambience.

## Tools
Roblox Studio, SoundService, Sound, SoundGroup, CompressorSoundEffect

## He points to
- Nesting SoundGroups and Ducking (Roblox docs)

## Quotes
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) "We always wanted there to be a more intriguing sound in the distance no matter where the player is located in the house."
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes) "Sounds that directly contribute to player progression were given priority over sounds that don't, such as wind, rain, footsteps, and atmosphere."

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[sound-and-music]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
