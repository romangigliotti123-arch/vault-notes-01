---
title: "Docs: sound / objects"
url: https://create.roblox.com/docs/sound/objects.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: sound / objects

[Open](https://create.roblox.com/docs/sound/objects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on legacy Sound objects: where to place them (BaseParts, attachments, SoundService/Workspace) and how positional vs background audio behaves. Covers Volume, RollOff properties and modes, PlaybackSpeed, TimePosition, Looped, and playing sounds from scripts or button clicks. Notes a newer Audio object set exists.

## Tips
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Check the docs' warning: a newer set of audio objects offers more control than Sound objects. Consider it before building new audio systems.
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Use volumetric audio (child of a large BasePart) for ambience and concert-style sound that should surround the player; use point source for explosions, impacts, devices and dialogue.
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Keep background music Sound objects in one organised location under SoundService, since they play at the same volume everywhere.
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Keep Volume at around 2 or below if the source audio is already loud; Volume is multiplicative, so 4 is four times as loud as 1.
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Set a higher RollOffMaxDistance for Inverse and Linear modes; low values make audio cut off abruptly at max distance.
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Use sound groups to control the volume of multiple Sound objects together and apply dynamic effects.
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Use TimePosition in a Heartbeat loop to trigger visual effects, such as enabling a particle emitter, during a specific window of a track.
- [page](https://create.roblox.com/docs/sound/objects) **[[sound-and-music]]** Enable Looped on background tracks so the game never has abrupt silence.
- [page](https://create.roblox.com/docs/sound/objects) **[[ui-ux-design]]** Play a Sound on GuiButton.Activated for auditory feedback on button presses; preload with Loaded:Wait() before playing.

## Numbers
- [page](https://create.roblox.com/docs/sound/objects) Volume range: **0 (silence) to 10 (booming); 2 or below usually sufficient**
- [page](https://create.roblox.com/docs/sound/objects) PlaybackSpeed: **2 = twice as fast, one octave higher; 0.5 = half speed, one octave lower**

## Tools
Roblox Studio, Sound object, SoundService, Attachment, ParticleEmitter

## He points to
- Audio (newer audio objects, linked from warning)

## Topics
[[sound-and-music]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
