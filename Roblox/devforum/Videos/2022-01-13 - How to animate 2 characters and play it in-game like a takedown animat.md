---
title: "How to animate 2 characters and play it in-game like a takedown animation"
url: https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-01-13
views: 314
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to animate 2 characters and play it in-game like a takedown animation

[Open](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) | Roblox DevForum | 314 views | 2022-01-13

## Summary
Tutorial on making a two-character takedown animation in Roblox: create two R15 dummies facing each other 5 studs apart, animate both rigs in Moon Animator as two exported animations, then use a server-side RemoteFunction to position characters and play both animations, with a LocalScript triggering it via F key near a dummy.

## Tips
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) **[[development-process-and-speed]]** Name each rig in Moon Animator and its exported animation (e.g. main/enemy) so you can tell which animation belongs to which character.
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) **[[core-loops-and-game-design]]** Position both characters relative to each other (about 5 studs apart, facing) before playing a paired animation so the two rigs line up.
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) **[[client-server-and-remotes]]** Use a RemoteFunction with InvokeServer when the client needs a return value after the server finishes the animation; a RemoteEvent won't return the result.
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) **[[client-server-and-remotes]]** Handle character positioning and animation playback on the server so both characters replicate to all clients.
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) **[[combat-and-gameplay-systems]]** Disable movement (WalkSpeed = 0) during a scripted animation and restore it after the main animation's Stopped event fires.
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) **[[development-process-and-speed]]** Wait for the main character's animation to finish rather than the enemy's before restoring control.
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) **[[client-server-and-remotes]]** Add a debounce on the client input to prevent animation spam from repeated key presses.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) distance between characters: **5 studs** (recommended spacing so paired animation plays properly)
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) proximity check for trigger: **10 studs** (LocalScript magnitude threshold to trigger takedown near dummy)
- [page](https://devforum.roblox.com/t/how-to-animate-2-characters-and-play-it-in-game-like-a-takedown-animation/1625809) spam cooldown: **2 seconds** (wait after each takedown invocation before debounce resets)

## Games
- **Right 2 Fight**: Referenced as an example of a Roblox takedown animation the tutorial aims to replicate.

## Tools
Roblox Studio, Moon Animator, Luau scripting, RemoteFunction

## He points to
- TakeDown animation Testing (Roblox experience linked by author)

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[core-loops-and-game-design]] [[development-process-and-speed]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
