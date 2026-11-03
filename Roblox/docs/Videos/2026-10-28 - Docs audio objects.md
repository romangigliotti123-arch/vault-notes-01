---
title: "Docs: audio / objects"
url: https://create.roblox.com/docs/audio/objects.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: audio / objects

[Open](https://create.roblox.com/docs/audio/objects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on audio objects: the producer/consumer/modifier/carrier model, plus step-by-step setup for 2D audio, 3D positional audio, text-to-speech (300-char limit, 30 voice IDs) and speech-to-text (17 languages, UseAudioApi), and audio effects and triggering via Play().

## Tips
- [page](https://create.roblox.com/docs/audio/objects) **[[scripting-and-performance]]** Avoid the legacy Sound, SoundGroup and SoundEffect objects; Roblox now discourages them in favor of AudioPlayer, AudioEmitter, Wire and audio effect objects.
- [page](https://create.roblox.com/docs/audio/objects) **[[sound-and-music]]** For 2D audio, wire AudioPlayer to AudioDeviceOutput under SoundService with a Wire (SourceInstance = player, TargetInstance = output).
- [page](https://create.roblox.com/docs/audio/objects) **[[sound-and-music]]** For 3D audio, place AudioPlayer plus AudioEmitter on the 3D object, wire them, and set AudioEmitter.DistanceAttenuation to control falloff over distance.
- [page](https://create.roblox.com/docs/audio/objects) **[[sound-and-music]]** Set SoundService.ListenerLocation to Default, Character, Camera or None; use None when creating the listener via script.
- [page](https://create.roblox.com/docs/audio/objects) **[[sound-and-music]]** Reuse repeated TTS lines by generating an audio asset with AssetService:CreateAssetAsync() instead of calling the TTS API each time.
- [page](https://create.roblox.com/docs/audio/objects) **[[sound-and-music]]** Keep AudioTextToSpeech Text under 300 characters per request.
- [page](https://create.roblox.com/docs/audio/objects) **[[sound-and-music]]** Use audio effects (AudioEqualizer, AudioCompressor, AudioReverb) to modify streams non-destructively, e.g. muffle rain or add interior reflections.
- [page](https://create.roblox.com/docs/audio/objects) **[[scripting-and-performance]]** Trigger audio from scripts by calling AudioPlayer:Play() on a correctly wired AudioPlayer, e.g. connected to a gameplay event.
- [page](https://create.roblox.com/docs/audio/objects) **[[ui-ux-design]]** For speech-to-text, set VoiceChatService.UseAudioApi to Enabled and set AudioDeviceInput.Player to the local player at runtime.
- [page](https://create.roblox.com/docs/audio/objects) **[[player-psychology-and-game-feel]]** To use speech-to-text without broadcasting voice, disable VoiceChatService.EnableDefaultVoice.
- [page](https://create.roblox.com/docs/audio/objects) **[[testing-debugging-and-qa]]** Filter STT results by sanitizing text (remove punctuation, lowercase, split on whitespace) and matching against prepared word tables, allowing substitutions.
- [page](https://create.roblox.com/docs/audio/objects) **[[age-ratings-moderation-and-tos]]** All TTS text and STT audio must adhere to Roblox Community Standards and Terms of Use.

## Numbers
- [page](https://create.roblox.com/docs/audio/objects) TTS character limit: **300 characters per request** (AudioTextToSpeech Text property)
- [page](https://create.roblox.com/docs/audio/objects) Distance attenuation example: **volume halves at 50 studs, zero at 70 studs** (AudioEmitter DistanceAttenuation example curve)
- [page](https://create.roblox.com/docs/audio/objects) TTS voices: **30 voice IDs (1-11, 101-1002)** (Artificial voices list, English US/UK/AU plus many languages)
- [page](https://create.roblox.com/docs/audio/objects) STT supported languages: **17** (Arabic through Vietnamese, auto-detected, no config needed)

## Tools
Roblox Studio, AudioPlayer, AudioEmitter, AudioDeviceOutput, AudioTextToSpeech, AudioSpeechToText, Wire, AudioListener

## He points to
- Add 2D audio tutorial
- Add 3D audio tutorial
- Add text-to-speech tutorial
- Add speech-to-text tutorial
- Audio effects docs page
- AssetService:CreateAssetAsync()

## Topics
[[age-ratings-moderation-and-tos]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[sound-and-music]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
