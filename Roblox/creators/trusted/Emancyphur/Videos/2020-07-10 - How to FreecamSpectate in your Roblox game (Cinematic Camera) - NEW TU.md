---
title: "How to Freecam/Spectate in your Roblox game (Cinematic Camera) - [NEW TUTORIAL IN DESCRIPTION]"
url: https://youtu.be/7aqTd3PzWWM
creator: Emancyphur
official: false
advice_density: low
date: 2020-07-10
views: 121009
transcript: manual-subs
confidence: high
tags: [roblox, emancyphur, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.6
---

> [!note] Trust: TRUSTED (credibility audit score 7.6): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Freecam/Spectate in your Roblox game (Cinematic Camera) - [NEW TUTORIAL IN DESCRIPTION]

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/7aqTd3PzWWM) | Emancyphur | 121,009 views | 2020-07-10

## Summary
Tutorial showing how to enable Roblox Studio freecam/cinematic mode (Shift+P, WASD, Q/E, scroll FOV) and how to disable it for players via a server script that fires a RemoteEvent on CharacterAdded and a LocalScript that destroys the Freecam GUI in PlayerGui.

## Tips
- [1:12](https://youtu.be/7aqTd3PzWWM?t=72) **[[anti-exploit-and-security]]** Freecam is only usable by game owners/editors, but disable it for all players by destroying the Freecam GUI from PlayerGui on every respawn.
- [2:35](https://youtu.be/7aqTd3PzWWM?t=155) **[[client-server-and-remotes]]** Use a server Script that fires a RemoteEvent to each client on CharacterAdded, since PlayerGui is reset on respawn and must be cleaned again.
- [5:31](https://youtu.be/7aqTd3PzWWM?t=331) **[[client-server-and-remotes]]** Pair the server RemoteEvent with a LocalScript in StarterPlayerScripts that listens via OnClientEvent and removes the Freecam GUI.

## Tools
Roblox Studio

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]]

Back to [[Emancyphur - How to make successful Roblox games]]
