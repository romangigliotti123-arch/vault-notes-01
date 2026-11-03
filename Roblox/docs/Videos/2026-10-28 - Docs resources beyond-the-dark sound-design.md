---
title: "Docs: resources / beyond-the-dark / sound-design"
url: https://create.roblox.com/docs/resources/beyond-the-dark/sound-design.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / beyond-the-dark / sound-design

[Open](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs case study on sound design for Beyond the Dark's DSR-14 space station: a 2D omnipresent soundbed plus 3D spot ambiences, layered sounds for variety, EQ/chorus/reverb sound processing, and sidechain compression for mix clarity.

## Tips
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Use a 2D omnipresent soundbed as the base layer, then add 3D sounds attached to objects (spot ambiences) to pull the player's ear around the space.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Parent looping 3D sounds to a part inside the object so they have a real location in the scene to play from.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Layer two or more loops of different lengths instead of one long loop; combined variety is the LCM of lengths (6s + 5s loops stay unique for 30s).
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Reuse layered source recordings across areas (e.g. river sound reused in a rainforest room) to get more use from the same asset.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Use EqualizerSoundEffect to cut high frequencies for an underwater feel on a sound layer.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Use ChorusSoundEffect (rate 16, depth 0.21 in their example) to make synth loops sound otherworldly while keeping some original character.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Pitch down recordings and add reverb to imply large space size; reverb can make an area feel like a cave.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Use a nested SoundGroup bus structure and sidechain compression so loud local sounds duck the ambient bed, creating priority and clarity.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Tune sidechain compressor settings relative to your own source levels; preset values from one project will not transfer to another.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) **[[sound-and-music]]** Attack/Release sets how fast ducking starts and how slowly it recovers; Threshold sets the level where compression starts; Ratio sets how strongly ducking applies.

## Numbers
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) Audio count: **1 2D soundbed, 2 dialogue tracks, 3 custom music tracks, 10 scripted audio events, 50 3D sounds** (DSR-14 spaceship audio set, routed through custom mix hierarchy)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) Chorus rate: **16 cycles per second** (ChorusSoundEffect on synthesizer loop in fish tank)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) Chorus depth: **0.21** (Mild chorus setting preserving original sound character)
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/sound-design) Loop variety: **6s + 5s loops unique for 30s** (Two layered loops repeat only at their least common multiple)

## Games
- **Beyond the Dark**: Spot ambiences in distinct areas keep the space feeling fresh each time players enter or exit; layered loops add free variety.

## Tools
SoundGroup, SoundEffect (EqualizerSoundEffect, ChorusSoundEffect), Sidechain compressor

## Topics
[[sound-and-music]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
