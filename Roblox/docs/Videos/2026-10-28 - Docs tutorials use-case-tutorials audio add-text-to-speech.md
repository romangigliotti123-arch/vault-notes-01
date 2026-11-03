---
title: "Docs: tutorials / use-case-tutorials / audio / add-text-to-speech"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / audio / add-text-to-speech

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on adding text-to-speech (TTS) to games. Covers the audio object chain (AudioTextToSpeech → Wire → AudioEmitter → AudioListener → AudioDeviceOutput), basic TTS with fixed text and voice IDs, and context-aware TTS driven by gumdrop attributes that change the spoken hint.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[sound-and-music]]** Use TTS for dynamic dialogue (UI, tutorials, vendor lines, enemy barks) instead of pre-recording audio for every narrative scenario.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[sound-and-music]]** Set SoundService.DefaultListenerLocation to Character so each player gets an AudioListener under their HumanoidRootPart for positional 3D audio.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[sound-and-music]]** Set AudioTextToSpeech Volume high (e.g. 3) when TTS must be heard over other audio sources.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[sound-and-music]]** Tune AudioTextToSpeech VoiceID, Pitch and Speed to make the same text sound like different characters without new audio files.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[scripting-and-performance]]** Guard Touched-triggered TTS with a debounce flag set true before Play and false after Ended:Wait() to prevent repeated triggering.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[scripting-and-performance]]** Check the touching player with Players:GetPlayerFromCharacter and compare to LocalPlayer so only the touching client plays the audio.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[core-loops-and-game-design]]** Track objective state with custom instance attributes (ColorDescription, HintOrder, LocationDescription, Active) so context-aware dialogue can adapt to progress.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) **[[core-loops-and-game-design]]** Build context-aware hints by sorting remaining objectives by a HintOrder attribute and generating the message string from current state.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) Supported TTS voice IDs: **19 voices: 1-11 English variants, 101/102 Spanish, 201/202 German, 301/302 Italian, 401/402 French** (AudioTextToSpeech VoiceID options listed in docs)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) Example Volume setting: **3** (High volume so TTS is heard over other sources in sample)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-text-to-speech) Example Pitch/Speed settings: **Pitch -12 to 12; Speed 0.8 to 2** (Sample variations shown in docs table)

## Games
- **Gingerbread House - Text-to-Speech**: Official sample place file demonstrating basic and context-aware TTS with gumdrop attributes and volume triggers.

## Tools
Roblox Studio, AudioTextToSpeech, AudioEmitter, AudioListener, AudioDeviceOutput, Wire, LocalScript

## He points to
- Gingerbread House - Start .rbxl file
- Gingerbread House - Text-to-Speech .rbxl file
- Debounce - Detect collisions
- Properties and attributes

## Topics
[[core-loops-and-game-design]] [[scripting-and-performance]] [[sound-and-music]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
