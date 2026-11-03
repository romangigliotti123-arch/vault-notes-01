---
title: "How to Make a Game Pass"
url: https://youtu.be/U22nZqDmTXI
creator: SimTek Game Development
official: false
advice_density: medium
date: 2023-08-18
views: 1995
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Make a Game Pass

[Watch](https://youtu.be/U22nZqDmTXI) | SimTekGameDevelopment | 1,995 views | 2023-08-18

## Summary
Tutorial on creating a Roblox gamepass (speed pass) end to end: enabling third-party sales, creating the pass on the creator dashboard, prompting purchase from a UI button via MarketplaceService, granting the benefit on spawn and respawn, and testing in the Roblox player since Studio grants gamepasses for free.

## Tips
- [0:40](https://youtu.be/U22nZqDmTXI?t=40) **[[monetisation-gamepasses]]** Gamepasses are one-time purchases that persist in the player's account across sessions; grant the benefit each time the player joins, not just at purchase.
- [1:21](https://youtu.be/U22nZqDmTXI?t=81) **[[monetisation-gamepasses]]** Enable 'Allow third party sales' in game Security settings before creating gamepasses, or purchases will fail.
- [2:46](https://youtu.be/U22nZqDmTXI?t=166) **[[pricing]]** Set the gamepass price to 1 Robux while testing to limit cost; the speaker notes Roblox takes 70% of sales.
- [3:27](https://youtu.be/U22nZqDmTXI?t=207) **[[common-mistakes]]** Creating a gamepass makes you own it, so delete it from your inventory before testing the purchase flow.
- [8:05](https://youtu.be/U22nZqDmTXI?t=485) **[[scripting-and-performance]]** Check ownership with MarketplaceService:UserOwnsGamePassAsync inside pcall on join, since it is asynchronous and can fail.
- [8:48](https://youtu.be/U22nZqDmTXI?t=528) **[[retention-d1-d7]]** Re-apply gamepass benefits on CharacterAdded so the benefit survives death and respawn.
- [10:10](https://youtu.be/U22nZqDmTXI?t=610) **[[scripting-and-performance]]** Connect PromptGamePassPurchaseFinished to grant the benefit right after purchase; it also fires on cancel, so check the purchased flag.
- [10:51](https://youtu.be/U22nZqDmTXI?t=651) **[[first-session-onboarding]]** When the ownership check errors, show a message telling the player to enable third-party sales.
- [12:15](https://youtu.be/U22nZqDmTXI?t=735) **[[ui-ux-design]]** Hide or disable the gamepass buy button once the player owns the pass to avoid confusing prompts.
- [14:08](https://youtu.be/U22nZqDmTXI?t=848) **[[testing-debugging-and-qa]]** Test the real purchase flow in the Roblox player, since Studio grants passes for free and does not keep them after death.
- [16:13](https://youtu.be/U22nZqDmTXI?t=973) **[[testing-debugging-and-qa]]** Verify that re-buying an owned pass shows 'already own this item' with no charge, and that the pass persists after reset and rejoin.

## Numbers
- [2:46](https://youtu.be/U22nZqDmTXI?t=166) Creator share of gamepass Robux sales: **70%** (Speaker says Roblox takes 70 percent of the sale price)
- [4:48](https://youtu.be/U22nZqDmTXI?t=288) Test gamepass price: **1 Robux** (Speaker uses 1 Robux to minimise cost during testing)
- [5:28](https://youtu.be/U22nZqDmTXI?t=328) Speed gamepass WalkSpeed boost: **+16 WalkSpeed** (Demo grants a walk speed increase on purchase)

## Games
- **Run Pass Video (demo game)** [0:00](https://youtu.be/U22nZqDmTXI?t=0): Demo speed-boost gamepass used to walk through the implementation; not a commercial benchmark.

## Tools
Roblox Studio, Roblox Creator Dashboard, MarketplaceService, Players service, Roblox Player (F9 developer console)

## Quotes
- [0:00](https://youtu.be/U22nZqDmTXI?t=0) "Game passes are great for one-time purchases; it goes into your account every time you play the game."
- [14:08](https://youtu.be/U22nZqDmTXI?t=848) "You can't really get the game pass in Roblox Studio, we're going to have to try it out with Roblox player."

## Topics
[[common-mistakes]] [[first-session-onboarding]] [[monetisation-gamepasses]] [[pricing]] [[retention-d1-d7]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
