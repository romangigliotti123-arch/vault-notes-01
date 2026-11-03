---
title: "How to script the BEST First Person in Roblox!"
url: https://youtu.be/hHKQEohHqwU
creator: PineappleDev
official: false
advice_density: medium
date: 2025-01-10
views: 27253
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to script the BEST First Person in Roblox!

[Watch](https://youtu.be/hHKQEohHqwU) | pineappledevv | 27,253 views | 2025-01-10

## Summary
Tutorial for scripting a custom first-person camera controller in a single LocalScript in StarterCharacterScripts. Covers mouse lock/unlock, mouse-look with touch support, view bobbing, walk-speed FOV, camera tilt on turns, Z-axis smoothing, syncing the character's facing to the camera, and hiding the body. Settings are tunable at the top of the script.

## Tips
- [0:36](https://youtu.be/hHKQEohHqwU?t=36) **[[client-server-and-remotes]]** Put the first-person LocalScript in StarterCharacterScripts so it runs per character on the client; use UserInputService for input so touch works on mobile too.
- [1:19](https://youtu.be/hHKQEohHqwU?t=79) **[[building-art-and-assets]]** Set Camera.CameraType to Scriptable before driving the camera in RenderStepped, and hide your own body parts and decals (Transparency = 1) for first person.
- [2:00](https://youtu.be/hHKQEohHqwU?t=120) **[[first-session-onboarding]]** Re-lock the mouse on UserInputService.WindowFocused so players who alt-tab back into the game aren't left with a free cursor.
- [3:24](https://youtu.be/hHKQEohHqwU?t=204) **[[player-psychology-and-game-feel]]** When tuning unknown camera settings, bump one value to an extreme, play-test, and observe the effect before settling on a value.
- [4:07](https://youtu.be/hHKQEohHqwU?t=247) **[[player-psychology-and-game-feel]]** Camera smoothing around 16 is a good default; raise it for snappier camera, lower it for floaty, cinematic feel (useful for horror).
- [5:29](https://youtu.be/hHKQEohHqwU?t=329) **[[player-psychology-and-game-feel]]** Tilt the camera's Z-angle proportional to horizontal turn rate and clamp it, then smooth it back to upright each frame for an immersive lean.
- [8:14](https://youtu.be/hHKQEohHqwU?t=494) **[[player-psychology-and-game-feel]]** Drive FOV from normalized velocity (clamped to a max speed) and lerp it, so running widens the view and stopping zooms back in.
- [11:40](https://youtu.be/hHKQEohHqwU?t=700) **[[player-psychology-and-game-feel]]** Make the bob frequency and amplitude scale with walking state so walking bobs faster than idle, using a sine of tick() times speed.
- [13:01](https://youtu.be/hHKQEohHqwU?t=781) **[[client-server-and-remotes]]** Set the character's pivot to match the camera's yaw each frame so the server knows where the player is facing.
- [15:02](https://youtu.be/hHKQEohHqwU?t=902) **[[development-process-and-speed]]** Expose all feel parameters (bob speed, distance, FOV, lean, smoothing, sensitivity, unlock key) as top-level variables so they can be tuned or moved to a ModuleScript.

## Numbers
- [2:43](https://youtu.be/hHKQEohHqwU?t=163) Default FOV: **60, walk FOV change 8, max FOV velocity 10, FOV smooth 3**
- [4:07](https://youtu.be/hHKQEohHqwU?t=247) Camera smooth: **16**
- [2:00](https://youtu.be/hHKQEohHqwU?t=120) Bob settings: **Bob speed 2, bob distance 2, walk bob multiplier 55, walk velocity threshold 9**
- [3:24](https://youtu.be/hHKQEohHqwU?t=204) Camera offset / lean / max vertical angle: **Y offset 2 studs, turn lean 320, turn lean smoothing 0.9, max vertical angle 80 degrees**

## Tools
Roblox Studio, Luau LocalScript

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[development-process-and-speed]] [[first-session-onboarding]] [[player-psychology-and-game-feel]]

Back to [[pineappledevv - How to make successful Roblox games]]
