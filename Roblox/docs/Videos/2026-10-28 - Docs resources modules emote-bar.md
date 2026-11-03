---
title: "Docs: resources / modules / emote-bar"
url: https://create.roblox.com/docs/resources/modules/emote-bar.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / emote-bar

[Open](https://create.roblox.com/docs/resources/modules/emote-bar.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs for the EmoteBar Creator Store module: installation, configuring default vs custom emotes, mega emote and tempo mechanics, and the full client/server API (configureServer, configureClient, setEmotes, playEmote, lock/unlock, events).

## Tips
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[social-features-and-virality]]** Emotes are a core component of social games; a customizable emote bar facilitates meaningful player interaction.
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[scripting-and-performance]]** Call configureServer and setEmotes only from a Script; changes replicate automatically to all clients.
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[ugc-and-avatar-economy]]** Owned emotes from past Roblox events (Lil Nas X, Royal Blood, Twenty One Pilots) auto-appear in the bar; disable UserEmotesEnabled on StarterPlayer in Studio to turn this off.
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[common-mistakes]]** Module modifies the local user's emotes via HumanoidDescription:SetEmotes, so GetEmotes returns the module-modified values.
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[core-loops-and-game-design]]** Mega emotes form when 3-50 nearby players perform the same emote simultaneously; defaults are emoteMinPlayers 3 and emoteMaxPlayers 50, tune them to your player density.
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[ui-ux-design]]** Use maxEmotesPerPage to limit visible emotes; smaller screens automatically show fewer. Default is 4. Switch guiType to EmoteWheel for a ring layout.
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[cross-platform-and-console]]** Emote bar position differs by orientation: set emoteBarPosLandscape and emoteBarPosPortrait separately; hotkeys cover only numeric keys 1-9.
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) **[[ui-ux-design]]** Set defaultTempo greater than 0 per emote; tempo is the playback speed factor, and tapping the button rhythmically within tempoActivationWindow (default 3s) changes speed.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) Default emote count: **7 preconfigured emotes** (EmoteBar module ships with 7 emotes)
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) emoteMinPlayers default: **3** (Minimum players performing same emote to form mega emote)
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) emoteMaxPlayers default: **50** (Maximum players contributing to a mega emote)
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) maxEmotesPerPage default: **4** (Max emotes displayed at once in bar mode)
- [page](https://create.roblox.com/docs/resources/modules/emote-bar) tempoActivationWindow default: **3 seconds** (Time between activations to count toward tempo)

## Tools
EmoteBar Creator Store module, Roblox Studio Toolbox, HumanoidDescription

## He points to
- Roblox Creator Store Packages

## Topics
[[common-mistakes]] [[core-loops-and-game-design]] [[cross-platform-and-console]] [[scripting-and-performance]] [[social-features-and-virality]] [[ugc-and-avatar-economy]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
