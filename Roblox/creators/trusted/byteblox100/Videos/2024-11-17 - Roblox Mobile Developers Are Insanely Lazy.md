---
title: "Roblox Mobile Developers Are Insanely Lazy"
url: https://youtu.be/1KKQ6YrktTk
creator: ByteBlox
official: false
advice_density: high
date: 2024-11-17
views: 428331
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Mobile Developers Are Insanely Lazy

[Watch](https://youtu.be/1KKQ6YrktTk) | byteblox100 | 428,331 views | 2024-11-17

## Summary
Argues most Roblox mobile games are poor because developers build only for PC and ignore mobile. Covers UI scale vs offset, using Activated instead of MouseButton1Click, detecting device via UserInputService to reduce particles/effects on mobile, and mobile-only lobbies for combat games.

## Tips
- [2:35](https://youtu.be/1KKQ6YrktTk?t=155) **[[first-session-onboarding]]** Test UI on multiple device presets in Studio (iPhone 4S, iPhone 14 Pro, PS5, desktop) before release; default layouts clip on phones.
- [8:05](https://youtu.be/1KKQ6YrktTk?t=485) **[[ui-ux-design]]** Set UI sizes to Scale (not Offset) and set Scale to 0 for Offset so elements resize proportionally across screen sizes.
- [15:18](https://youtu.be/1KKQ6YrktTk?t=918) **[[ui-ux-design]]** Use Activated instead of MouseButton1Click for buttons so taps on touchscreens and controller presses also register.
- [20:06](https://youtu.be/1KKQ6YrktTk?t=1206) **[[scripting-and-performance]]** Detect platform with UserInputService: KeyboardEnabled, MouseEnabled, TouchEnabled combinations identify PC vs mobile.
- [22:07](https://youtu.be/1KKQ6YrktTk?t=1327) **[[optimization-and-streaming]]** On mobile, reduce particle sizes or destroy heavy particles and excess meshes client-side to avoid lag spikes; keep PC version unchanged.
- [24:10](https://youtu.be/1KKQ6YrktTk?t=1450) **[[ui-ux-design]]** Offer players a choice to switch between PC and a lower-quality mobile graphics mode.
- [25:31](https://youtu.be/1KKQ6YrktTk?t=1531) **[[genre-mechanics]]** In combat games, mouse/keyboard players beat mobile players at equal skill; consider mobile-only lobbies, as Blade Ball reportedly does.
- [26:54](https://youtu.be/1KKQ6YrktTk?t=1614) **[[common-mistakes]]** Don't treat mobile as an afterthought; developers who build for PC first get bad mobile experiences, while top games cater to mobile heavily.

## Numbers
- [8:45](https://youtu.be/1KKQ6YrktTk?t=525) Default UI sizing: **Offset default; a button was 82px tall, 354px wide at default** (Offset uses fixed pixels, so layouts break across devices)
- [22:07](https://youtu.be/1KKQ6YrktTk?t=1327) Mobile fire particle size: **Set size to 3 on mobile** (Example reduction; script waits 2 seconds before device check)
- [17:20](https://youtu.be/1KKQ6YrktTk?t=1040) Target frame rate: **Above ~40 FPS** (Speaker's minimum for good mobile experience)

## Games
- **Blade Ball** [25:31](https://youtu.be/1KKQ6YrktTk?t=1531): Reportedly has mobile-only lobbies so mobile players aren't stomped by mouse-and-keyboard players in a combat game.
- **Arsenal** [25:31](https://youtu.be/1KKQ6YrktTk?t=1531): Example of a combat game where mobile players are at a skill disadvantage against keyboard players.

## Tools
Roblox Studio, UserInputService, Device preview in Studio Test tab

## He points to
- Speaker's own loading screen video (referenced, not named)
- Speaker's Roblox course (promotional, skipped)

## Quotes
- [26:13](https://youtu.be/1KKQ6YrktTk?t=1573) "Mobile players are being neglected because developers mainly develop for PCs and have mobile games as more of an afterthought."
- [14:10](https://youtu.be/1KKQ6YrktTk?t=850) "Roblox never tells you to use scale; it lets you do whatever, and a lot of people don't test on phone."

## Topics
[[common-mistakes]] [[first-session-onboarding]] [[genre-mechanics]] [[optimization-and-streaming]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[byteblox100 - How to make successful Roblox games]]
