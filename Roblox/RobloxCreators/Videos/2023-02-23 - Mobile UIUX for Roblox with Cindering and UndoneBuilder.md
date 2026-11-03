---
title: "Mobile UI/UX for Roblox with Cindering and UndoneBuilder"
url: https://youtu.be/BsyU-SJ9L-c
creator: Roblox Creators
official: true
advice_density: high
date: 2023-02-23
views: 1541
transcript: manual-subs
confidence: high
tags: [roblox, robloxcreators, youtube-learn]
---

# Mobile UI/UX for Roblox with Cindering and UndoneBuilder

[Watch](https://youtu.be/BsyU-SJ9L-c) | RobloxCreators | 1,541 views | 2023-02-23

## Summary
Level Up roundtable with Cindering (Cinder Studio, Roblox High School 2, Super Striker League) and UndoneBuilder (Nathan, Simple Games, War Simulator) on mobile UI/UX for Roblox. Covers universal scaling UI, scale vs offset sizing, aspect ratio constraints, device emulator, thumb-zone button placement, reducing text/friction, and measuring button discovery with badges.

## Tips
- [1:30](https://youtu.be/BsyU-SJ9L-c?t=90) **[[core-loops-and-game-design]]** Build one universal UI that scales to all devices instead of separate PC and mobile UIs; separate UIs are hard to maintain. Some devs use up to seven scaled UIs; avoid that.
- [11:08](https://youtu.be/BsyU-SJ9L-c?t=668) **[[building-art-and-assets]]** Use Scale for larger screens and Offset (raw pixels) for smaller screens so UI stays legible on phones.
- [12:34](https://youtu.be/BsyU-SJ9L-c?t=754) **[[building-art-and-assets]]** Add UI aspect ratio constraints so UI keeps its shape on any screen instead of stretching and distorting.
- [14:12](https://youtu.be/BsyU-SJ9L-c?t=852) **[[building-art-and-assets]]** Use Studio's device emulator to check phone and tablet layouts; verify text is legible and buttons are big enough for finger taps.
- [19:43](https://youtu.be/BsyU-SJ9L-c?t=1183) **[[building-art-and-assets]]** Place main actions in bottom-corner thumb zones (right side); keep few controls on screen and show context-sensitive buttons only when needed.
- [6:47](https://youtu.be/BsyU-SJ9L-c?t=407) **[[core-loops-and-game-design]]** Show as little UI as possible; move shops, quests and destinations into the physical world, but make them discoverable.
- [22:41](https://youtu.be/BsyU-SJ9L-c?t=1361) **[[common-mistakes]]** Avoid placing buttons on the left movement side of mobile screens, since pressing them stops character movement.
- [32:04](https://youtu.be/BsyU-SJ9L-c?t=1924) **[[common-mistakes]]** Remember live chat covers the top of the mobile screen; don't rely on upper-screen space when designing HUD.
- [24:13](https://youtu.be/BsyU-SJ9L-c?t=1453) **[[common-mistakes]]** Use color only to carry meaning; random rainbow buttons add noise and confuse players.
- [33:58](https://youtu.be/BsyU-SJ9L-c?t=2038) **[[monetisation-gamepasses]]** Make purchase buttons prominent and uncluttered; Nathan saw monetization roughly quadruple when the shop was easy to find and fewer buttons competed.
- [34:23](https://youtu.be/BsyU-SJ9L-c?t=2063) **[[ads-and-sponsored-experiences]]** Track whether players actually click key buttons by tying a badge to the click; a hacky but practical analytics method.
- [36:18](https://youtu.be/BsyU-SJ9L-c?t=2178) **[[first-session-onboarding]]** Use icons over text; many players are non-native English speakers and rarely read text, so keep text minimal.
- [36:58](https://youtu.be/BsyU-SJ9L-c?t=2218) **[[common-mistakes]]** Allow for longer translated text (e.g., German) in UI boxes so localized strings don't become illegible.
- [41:16](https://youtu.be/BsyU-SJ9L-c?t=2476) **[[monetisation-devproducts]]** Give visual and audio reward feedback on purchase (e.g., coins raining down) and confirm items landed in inventory to avoid scam complaints.
- [41:56](https://youtu.be/BsyU-SJ9L-c?t=2516) **[[playtesting-and-feedback]]** Watch people unfamiliar with mobile games, e.g. a relative, play without instruction to see where they get stuck.
- [38:08](https://youtu.be/BsyU-SJ9L-c?t=2288) **[[first-session-onboarding]]** Reduce friction by keeping the most important buttons highlighted and pathways clear; fewer windows is better.
- [39:35](https://youtu.be/BsyU-SJ9L-c?t=2375) **[[core-loops-and-game-design]]** Keep design consistent: buttons should look the same everywhere so players learn the interface once.
- [27:02](https://youtu.be/BsyU-SJ9L-c?t=1622) **[[core-loops-and-game-design]]** Design mobile first since it is the lowest spec; if it works on mobile it will work on other devices.
- [22:01](https://youtu.be/BsyU-SJ9L-c?t=1321) **[[development-process-and-speed]]** Study how other Roblox and mobile games solve hard problems like vehicle controls; expect multiple redesigns (Cindering redesigned vehicle controls 6-7 times).
- [29:56](https://youtu.be/BsyU-SJ9L-c?t=1796) **[[playtesting-and-feedback]]** Experiment with UI many times and let player feedback decide; UI iteration is ongoing.
- [6:04](https://youtu.be/BsyU-SJ9L-c?t=364) **[[core-loops-and-game-design]]** Mobile is often 70-80% of players if optimized; treat UI/UX as more important than first-time user experience.

## Numbers
- [6:04](https://youtu.be/BsyU-SJ9L-c?t=364) Mobile share of players: **70-80% if optimized (Nathan's estimate)**
- [34:23](https://youtu.be/BsyU-SJ9L-c?t=2063) Purple home button clicks: **less than 10% of players have clicked it**
- [33:58](https://youtu.be/BsyU-SJ9L-c?t=2038) Monetization effect of shop visibility: **quadruples monetization (Nathan's claim)**
- [33:58](https://youtu.be/BsyU-SJ9L-c?t=2038) Cluttered vs clean UI monetization: **cluttered game has about a quarter the monetization of War Simulator (two buttons)**
- [36:18](https://youtu.be/BsyU-SJ9L-c?t=2178) Non-native English speakers: **less than half of players speak English fluently (Nathan's estimate)**
- [22:01](https://youtu.be/BsyU-SJ9L-c?t=1321) Vehicle control redesigns: **about 6-7 iterations**
- [24:13](https://youtu.be/BsyU-SJ9L-c?t=1453) Roblox High School house editor versions: **v1 2014, v2 2018, v3 2021**

## Games
- **War Simulator** [6:47](https://youtu.be/BsyU-SJ9L-c?t=407): Moved most UI into the physical world; only two UI elements (money and shop). Nathan's most popular game, with high monetization.
- **Roblox High School 2** [1:30](https://youtu.be/BsyU-SJ9L-c?t=90): Cinder Studio's flagship; house editor iterated across three versions (2014, 2018, 2021) to be simpler and easier on all platforms.
- **Super Striker League** [19:43](https://youtu.be/BsyU-SJ9L-c?t=1183): Simple controls with main actions in thumb zones and context-sensitive buttons, since players use two thumbs.

## Tools
Roblox Studio device emulator, UDim2 Scale/Offset, UIAspectRatioConstraint, UIGridLayout, UIListLayout, UIScale, UISizeConstraint, Badges (as click analytics)

## He points to
- Level Up YouTube channel

## Quotes
- [6:04](https://youtu.be/BsyU-SJ9L-c?t=364) "It's probably if you're optimizing decently, 70, 80% of your players will be on mobile, but it's everything."
- [8:15](https://youtu.be/BsyU-SJ9L-c?t=495) "What you absolutely should do is make a universal UI that works for all devices and that automatically scales."
- [34:44](https://youtu.be/BsyU-SJ9L-c?t=2084) "to the players, less than 10% of players have ever seen or clicked on that purple home button."
- [43:08](https://youtu.be/BsyU-SJ9L-c?t=2588) "Mostly the easiest way I found currently is using badges... Which makes kind of the hackiest possible, most Robloxy type analytics you can think of."

## On screen
Shows mobile vs computer layout comparison of a placement/build UI (9:16), a scoreboard HUD on phone (20:45), and War Simulator-style HUD with Hunger/Sleep bars, $10.0B cash, left-side Map/Admin buttons and right-side icon menu (34:23, 35:15). Left-side buttons visible on the game screens.

## Topics
[[ads-and-sponsored-experiences]] [[building-art-and-assets]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[first-session-onboarding]] [[monetisation-devproducts]] [[monetisation-gamepasses]] [[playtesting-and-feedback]]

Back to [[RobloxCreators - How to make successful Roblox games]]
