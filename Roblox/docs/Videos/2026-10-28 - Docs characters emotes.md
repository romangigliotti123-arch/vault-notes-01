---
title: "Docs: characters / emotes"
url: https://create.roblox.com/docs/characters/emotes.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / emotes

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/characters/emotes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on emotes: opening/closing the emotes menu, setting and equipping up to 8 emotes via HumanoidDescription, disabling the menu, and playing emotes via Humanoid:PlayEmote. Includes code samples for each.

## Tips
- [page](https://create.roblox.com/docs/characters/emotes) **[[ugc-and-avatar-economy]]** Emotes can be bought in the Marketplace and equipped; default emotes (dance, point, cheer) are available to all users.
- [page](https://create.roblox.com/docs/characters/emotes) **[[client-server-and-remotes]]** Set emotes and equipped emotes from a LocalScript in StarterCharacterScripts, using Players.LocalPlayer.Character.Humanoid.HumanoidDescription.
- [page](https://create.roblox.com/docs/characters/emotes) **[[common-mistakes]]** Disabling the emotes menu does not block chat-command emotes like /e cheer; block those separately if needed.
- [page](https://create.roblox.com/docs/characters/emotes) **[[scripting-and-performance]]** UserEmotesEnabled in StarterPlayer > Character can only be set in Studio, not by scripts.

## Numbers
- [page](https://create.roblox.com/docs/characters/emotes) max equipped emotes: **8** (Maximum emotes equipped to the emotes menu via SetEquippedEmotes)

## Tools
GuiService, StarterGui, HumanoidDescription, Humanoid:PlayEmote

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[scripting-and-performance]] [[ugc-and-avatar-economy]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
