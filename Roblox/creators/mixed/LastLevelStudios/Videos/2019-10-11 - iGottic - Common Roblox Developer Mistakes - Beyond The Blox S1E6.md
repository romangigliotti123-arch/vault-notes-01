---
title: "iGottic - Common Roblox Developer Mistakes - Beyond The Blox S1E6"
url: https://youtu.be/vY0om5O-Oh8
creator: Last Level Studios
official: false
advice_density: high
date: 2019-10-11
views: 2376
transcript: auto-captions
confidence: medium
tags: [roblox, lastlevelstudios, youtube-learn]
creator_trust: MIXED
creator_score: 5.5
---

> [!note] Trust: MIXED (credibility audit score 5.5): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# iGottic - Common Roblox Developer Mistakes - Beyond The Blox S1E6

[Watch](https://youtu.be/vY0om5O-Oh8) | LastLevelStudios | 2,376 views | 2019-10-11

## Summary
Podcast on common Roblox developer mistakes that limit player count and revenue: neglecting updates, optimization, PC-only design, shutdowns, weak theme and target audience, thumbnails, lack of progression, paywalls and overpriced game passes, and using new APIs without understanding them.

## Tips
- [3:16](https://youtu.be/vY0om5O-Oh8?t=196) **[[updates-live-ops]]** Keep updating games; players leave when content stops, and starting new games rather than updating one loses the existing player base.
- [5:20](https://youtu.be/vY0om5O-Oh8?t=320) **[[optimization-and-streaming]]** Review memory and optimization regularly, not just at launch; server memory overuse causes freezing and lag, especially on mobile and console.
- [6:43](https://youtu.be/vY0om5O-Oh8?t=403) **[[cross-platform-and-console]]** Add Xbox or mobile support once the game has about 10 concurrent players; these audiences can be larger than PC.
- [7:23](https://youtu.be/vY0om5O-Oh8?t=443) **[[ui-ux-design]]** Design UI for mobile and console from the start; retrofitting Xbox selection onto a GUI-heavy game can require a separate selection layer.
- [10:46](https://youtu.be/vY0om5O-Oh8?t=646) **[[cross-platform-and-console]]** Use generic default input activation rather than many keyboard- or mouse-specific actions to ease porting.
- [12:13](https://youtu.be/vY0om5O-Oh8?t=733) **[[core-loops-and-game-design]]** Keep art style consistent; mixing realistic and cartoony assets confuses players and loses the style-based player base.
- [14:17](https://youtu.be/vY0om5O-Oh8?t=857) **[[core-loops-and-game-design]]** Define a clear target audience (age and demographic) before building; it drives style, marketing channels and platform choices.
- [16:22](https://youtu.be/vY0om5O-Oh8?t=982) **[[social-features-and-virality]]** Roblox only shows social and Discord buttons to players 13+, so Discord communities skew older.
- [16:22](https://youtu.be/vY0om5O-Oh8?t=982) **[[thumbnails-icons]]** Use colourful gradients or eye-catching backgrounds for icons and thumbnails, not solid white or plain colour; test variants.
- [18:45](https://youtu.be/vY0om5O-Oh8?t=1125) **[[updates-live-ops]]** Limit shutdowns; each one drives away players. Use a soft-shutdown script that moves players to a lobby and back via TeleportService.
- [20:47](https://youtu.be/vY0om5O-Oh8?t=1247) **[[retention-d1-d7]]** Add badges and clear progression (levels, XP, crates) so players have achievement and a reason to return.
- [21:28](https://youtu.be/vY0om5O-Oh8?t=1288) **[[core-loops-and-game-design]]** Make campaign modes fully linear or fully open-world; mixing both with hidden required steps frustrates players.
- [23:29](https://youtu.be/vY0om5O-Oh8?t=1409) **[[pricing]]** Keep game pass and product prices roughly 10 to 150 Robux, since most players have little Robux.
- [26:13](https://youtu.be/vY0om5O-Oh8?t=1573) **[[monetisation-gamepasses]]** Always provide a free path through the game; paywalls that block progress lose players, while paid tiers should add extra value.
- [27:34](https://youtu.be/vY0om5O-Oh8?t=1654) **[[monetisation-gamepasses]]** Do not sell pay-to-win power in competitive games; paid advantages make non-paying players feel cheated.
- [28:45](https://youtu.be/vY0om5O-Oh8?t=1725) **[[common-mistakes]]** Understand an API or script before implementing it; untested features like a camera bob script that tanks frame rate hurt the game.
- [30:48](https://youtu.be/vY0om5O-Oh8?t=1848) **[[common-mistakes]]** Learn from the Roblox Developer Hub and DevForum, and check the Toolbox for scripts, but verify and understand them before use.

## Numbers
- [6:43](https://youtu.be/vY0om5O-Oh8?t=403) Player split (Noscope Sniping): **About 80 PC players vs 4,800 console players** (Developer stats cited as reason for its popularity)
- [6:43](https://youtu.be/vY0om5O-Oh8?t=403) Concurrent players before adding Xbox/mobile: **About 10** (Suggested threshold for considering mobile or Xbox support)
- [25:30](https://youtu.be/vY0om5O-Oh8?t=1530) Game pass price range: **10 to 150 Robux** (Suggested range; some games price passes as high as 9,000 Robux)
- [24:10](https://youtu.be/vY0om5O-Oh8?t=1450) Robux spent by host in one game: **About 4,000 Robux** (Spent on Despedido, cited as a pay-heavy example)
- [16:22](https://youtu.be/vY0om5O-Oh8?t=982) Minimum age for Discord and Roblox social buttons: **13** (Discord sign-up and Roblox social button restriction)

## Games
- **Mad Paintball / Mad Murder (Matt's Studio)** [3:16](https://youtu.be/vY0om5O-Oh8?t=196): Stopped updating within weeks of release; players lost interest.
- **Phantom Forces** [4:38](https://youtu.be/vY0om5O-Oh8?t=278): Frequent small bug-fix and optimization updates keep a popular game healthy.
- **Noscope Sniping** [7:23](https://youtu.be/vY0om5O-Oh8?t=443): Most of its player base came from console players, not PC.
- **Stepford County Railway** [8:44](https://youtu.be/vY0om5O-Oh8?t=524): Needed a custom Xbox selection system because the default GUI navigation could not handle its many buttons.
- **Arsenal** [20:47](https://youtu.be/vY0om5O-Oh8?t=1247): Many badges keep PC and Xbox players engaged.
- **Red River** [20:47](https://youtu.be/vY0om5O-Oh8?t=1247): Released a gun system with little depth (no multiplayer, no progression) while hyping the full game.
- **Infinite Autocorrect** [26:53](https://youtu.be/vY0om5O-Oh8?t=1613): Paid tier offers a private island and customisation while keeping a complete free path.
- **Knife Ability Testing** [25:30](https://youtu.be/vY0om5O-Oh8?t=1530): Game passes priced as high as 9,000 Robux, far above typical price points.
- **Despedido** [24:10](https://youtu.be/vY0om5O-Oh8?t=1450): Everything had a Robux price, which felt like a cash grab despite being a popular meme.

## Tools
Roblox Developer Hub, Roblox DevForum, Roblox Toolbox, TeleportService (soft shutdown)

## He points to
- Beyond The Blocks podcast
- Red Dead Redemption 2
- Counter-Strike
- Overcooked
- Warface

## Quotes
- [18:45](https://youtu.be/vY0om5O-Oh8?t=1125) "every time you shut down the game for an update you risk losing a huge player account"
- [26:13](https://youtu.be/vY0om5O-Oh8?t=1573) "there's always a free path through so it's never a solid wall in your way that you have to pay through"

## Topics
[[common-mistakes]] [[core-loops-and-game-design]] [[cross-platform-and-console]] [[monetisation-gamepasses]] [[optimization-and-streaming]] [[pricing]] [[retention-d1-d7]] [[social-features-and-virality]] [[thumbnails-icons]] [[ui-ux-design]] [[updates-live-ops]]

Back to [[LastLevelStudios - How to make successful Roblox games]]
