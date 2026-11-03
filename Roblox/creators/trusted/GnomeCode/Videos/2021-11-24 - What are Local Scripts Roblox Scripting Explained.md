---
title: "What are Local Scripts? Roblox Scripting Explained"
url: https://youtu.be/myaGOnACzSY
creator: GnomeCode
official: false
advice_density: low
date: 2021-11-24
views: 117856
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# What are Local Scripts? Roblox Scripting Explained

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/myaGOnACzSY) | GnomeCode | 117,856 views | 2021-11-24

## Summary
Explains Local Scripts vs server Scripts in Roblox: client-server model, the only containers where LocalScripts run (StarterGui, StarterPack, StarterPlayerScripts, StarterCharacterScripts, StarterPlayer), and examples of client-only visual changes and GUI button handling. Points to RemoteEvents for client-server communication.

## Tips
- [0:28](https://youtu.be/myaGOnACzSY?t=28) **[[code-architecture-and-frameworks]]** Put LocalScripts only in StarterGui, StarterPack, StarterPlayerScripts, StarterCharacterScripts or StarterPlayer; elsewhere they never run.
- [1:43](https://youtu.be/myaGOnACzSY?t=103) **[[client-server-and-remotes]]** Client changes (transparency, CanCollide, GUI) only affect that player's copy; the server is unaffected, so game-state changes must go through the server.
- [5:47](https://youtu.be/myaGOnACzSY?t=347) **[[ui-ux-design]]** Use a LocalScript under the button and connect Activated to handle clicks, since server scripts can't read a player's device input.
- [8:08](https://youtu.be/myaGOnACzSY?t=488) **[[client-server-and-remotes]]** Use RemoteEvents to send a client action to the server so changes apply to all players in the game.

## Tools
Roblox Studio

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[ui-ux-design]]

Back to [[GnomeCode - How to make successful Roblox games]]
