---
title: "Docs: tutorials / use-case-tutorials / audio / speech-to-text"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / audio / speech-to-text

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on adding speech-to-text (STT) to a game. Covers the AudioDeviceInput, AudioSpeechToText and Wire objects, enabling microphone usage in Experience Settings, capturing speech with a LocalScript, and triggering a door-open RemoteEvent when the player says "Open Sesame".

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[client-server-and-remotes]]** Set AudioDeviceInput.Player to the LocalPlayer on the client so Roblox captures that user's microphone; the STT pipeline runs client-side.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[client-server-and-remotes]]** Fire a RemoteEvent from client to server to trigger gameplay actions like opening a door, keeping the server authoritative.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[ui-ux-design]]** Use push to chat alongside STT for more reliable voice detection, since mics are only active while the player holds a button.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[common-mistakes]]** Enable microphone usage in Experience Settings > Communication and publish the game before STT will work; it cannot be tested otherwise.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[scripting-and-performance]]** Clear AudioSpeechToText.Text after processing each recognized phrase so stale text doesn't re-trigger actions.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[scripting-and-performance]]** Match recognized text with string.find on lowercase phrases (e.g. 'open sesame') and ignore empty strings before acting.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[building-art-and-assets]]** Set VoiceChatService.UseAudioApi to Enabled to use the latest voice API required for AudioDeviceInput.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/speech-to-text) **[[first-session-onboarding]]** Use STT for hands-free controls like opening inventory or casting spells, and for accessibility for players with motor or vision limitations.

## Tools
AudioDeviceInput, AudioSpeechToText, Wire, VoiceChatService, RemoteEvent, TweenService, Team Test

## He points to
- Add 2D audio tutorial
- Add 3D audio tutorial
- Gingerbread House - Start .rbxl

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[first-session-onboarding]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
