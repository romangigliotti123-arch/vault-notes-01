---
title: "Every Game is Soulless; And There's a Really Easy Fix"
url: https://youtu.be/Issrodr_wK8
creator: ByteBlox
official: false
advice_density: medium
date: 2024-09-24
views: 393575
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Every Game is Soulless; And There's a Really Easy Fix

[Watch](https://youtu.be/Issrodr_wK8) | byteblox100 | 393,575 views | 2024-09-24

## Summary
Beginner tutorial showing how to make a trivially simple Roblox obby (jump on parts) feel polished: touch-triggered bounce tween, per-player client-side visuals via RemoteEvent, highlight color feedback, a UI progress bar, and a particle aura that grows with progress. Argues cheap flashy details add personality and monetisation value.

## Tips
- [5:16](https://youtu.be/Issrodr_wK8?t=316) **[[core-loops-and-game-design]]** Add small juice to even a trivial game (bounce, color change, progress, aura); the speaker says it takes about 20-30 minutes for a beginner.
- [10:02](https://youtu.be/Issrodr_wK8?t=602) **[[scripting-and-performance]]** Use a loop over the parts folder to connect Touched events instead of wiring each part manually; name-independent and scales when parts are added.
- [14:09](https://youtu.be/Issrodr_wK8?t=849) **[[scripting-and-performance]]** Filter Touched events by checking for a Humanoid in the hit's parent, and debounce with a flag so one touch doesn't fire repeatedly.
- [15:34](https://youtu.be/Issrodr_wK8?t=934) **[[scripting-and-performance]]** Store per-part state (e.g. an IsCleared attribute) on the part so the progress and highlight logic can check it without extra variables.
- [33:44](https://youtu.be/Issrodr_wK8?t=2024) **[[player-psychology-and-game-feel]]** Make feedback play only on first interaction (e.g. bounce once per part) so effects stay meaningful rather than repeating.
- [27:28](https://youtu.be/Issrodr_wK8?t=1648) **[[ui-ux-design]]** Add a progress bar to goal-based games like obbies or tycoons; scale its bar width by cleared/total count, computed from #folder:GetChildren() so it updates automatically.
- [26:42](https://youtu.be/Issrodr_wK8?t=1602) **[[player-psychology-and-game-feel]]** Delay a visual state change slightly (about 0.1s) so it lands with the tween animation rather than before it.
- [29:32](https://youtu.be/Issrodr_wK8?t=1772) **[[ui-ux-design]]** Set ScreenGui ResetOnSpawn to false so progress UI persists across respawns.
- [19:18](https://youtu.be/Issrodr_wK8?t=1158) **[[scripting-and-performance]]** Run per-player animations on the client via a RemoteEvent, not on the server, so each player sees their own state.
- [36:39](https://youtu.be/Issrodr_wK8?t=2199) **[[vfx-and-particles]]** Reward progress with a particle aura whose transparency is set to 1 minus progress, so it becomes more visible as the player advances.
- [23:29](https://youtu.be/Issrodr_wK8?t=1409) **[[optimization-and-streaming]]** Be aware Roblox limits the number of Highlight instances; very large part counts may hit the cap.

## Numbers
- [22:07](https://youtu.be/Issrodr_wK8?t=1327) Highlight limit: **Roblox caps the number of Highlights allowed** (Speaker notes hitting limit when parts count grows)
- [41:12](https://youtu.be/Issrodr_wK8?t=2472) Build time: **20-30 minutes** (Estimated time for a solo beginner to add these features)
- [19:59](https://youtu.be/Issrodr_wK8?t=1199) Bounce tween: **0.2s, Back easing, size +2 studs X/Z, reverse** (Tween settings used for the touch bounce animation)

## Games
- **Doors** [1:24](https://youtu.be/Issrodr_wK8?t=84): Cited as an example of a monetized game that kept rich, creative, soulful detail.
- **Team Fortress 2** [3:27](https://youtu.be/Issrodr_wK8?t=207): Cited as a game with clear character and personality.
- **Subnautica** [3:27](https://youtu.be/Issrodr_wK8?t=207): Cited as a game with soul and life.
- **Overwatch** [3:27](https://youtu.be/Issrodr_wK8?t=207): Cited as a game with cool characters, though speaker says it has declined since the second game.

## Tools
Roblox Studio, Luau, Toolbox (free model green aura), TweenService

## He points to
- Gnome Code (YouTube channel)

## Quotes
- [0:00](https://youtu.be/Issrodr_wK8?t=0) "Games that try to monetize but also ensure their game stays an amazing and unique and creative experience will succeed."
- [27:28](https://youtu.be/Issrodr_wK8?t=1648) "A lot of Roblox games seemingly don't have progress bars; in something like an obby or tycoon a progress bar would do wonders."

## Topics
[[core-loops-and-game-design]] [[optimization-and-streaming]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[byteblox100 - How to make successful Roblox games]]
