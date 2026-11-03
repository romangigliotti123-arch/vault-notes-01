---
title: "Docs: tutorials / use-case-tutorials / audio / in-game-sounds"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / audio / in-game-sounds

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on in-game sounds. Covers positional sounds (Sound parented to a part, SoundId, Playing/Looped, RollOffMaxDistance/RollOffMinDistance/RollOffMode, SoundGroup) and feedback sounds (SoundService Sound played from a LocalScript on Touched of collectable parts).

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[building-art-and-assets]]** Parent a Sound to a part or attachment to make it positional; volume scales with player distance.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[optimization-and-streaming]]** Set RollOffMaxDistance (e.g. 30 studs) so positional sounds only play near the source instead of everywhere.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[ui-ux-design]]** Use RollOffMode InverseTapered for a smoother fade-in as players approach a sound source.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[sound-and-music]]** Group background music and effects with SoundGroup to balance volume between categories.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[sound-and-music]]** Use Toolbox or Asset Manager to add free or custom sounds via rbxassetid SoundIds.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[player-psychology-and-game-feel]]** Play a short chime on collectable touch as feedback so pickups feel rewarding.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[client-server-and-remotes]]** Feedback sounds are played from a LocalScript in StarterPlayerScripts, keeping audio on the client.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) **[[scripting-and-performance]]** Check that the touched part is a character (Humanoid present) and CanCollide before triggering effects, to avoid false triggers.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) RollOffMaxDistance: **30 studs (example value)** (Distance at which positional sound becomes inaudible in tutorial)

## Tools
Roblox Studio, Toolbox, Asset Manager

## He points to
- Collectable Gems Model (Roblox Creator Hub model page)

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[optimization-and-streaming]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[sound-and-music]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
