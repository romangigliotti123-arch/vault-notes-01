---
title: "How to make a Tycoon in Roblox #11 - Gamepasses"
url: https://youtu.be/TmiU5CY6BW0
creator: B Ricey
official: false
advice_density: medium
date: 2022-04-16
views: 15934
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Tycoon in Roblox #11 - Gamepasses

[Watch](https://youtu.be/TmiU5CY6BW0) | BRicey | 15,934 views | 2022-04-16

## Summary
Tutorial on adding a gamepass to a Roblox tycoon: creating the pass on the Creator Dashboard, a reusable GUI button driven by a game pass ID attribute and tag, client-side MarketplaceService prompts, and server-side ownership checks via a registry module that applies a 2x money multiplier.

## Tips
- [1:34](https://youtu.be/TmiU5CY6BW0?t=94) **[[monetisation-gamepasses]]** Gamepasses apply globally across the game, so they suit permanent boosts like a money multiplier rather than consumable items.
- [2:14](https://youtu.be/TmiU5CY6BW0?t=134) **[[monetisation-gamepasses]]** Copy the gamepass ID from the URL (roblox.com/game-pass/ID/...). It is needed to prompt purchases in-game.
- [6:02](https://youtu.be/TmiU5CY6BW0?t=362) **[[core-loops-and-game-design]]** Store the gamepass ID as a number attribute on each button and tag buttons with a shared tag, so one reusable script can wire up any number of passes.
- [9:08](https://youtu.be/TmiU5CY6BW0?t=548) **[[scripting-and-performance]]** Use MarketplaceService:PromptGamePassPurchase for gamepasses; PromptProductPurchase silently fails for them.
- [10:31](https://youtu.be/TmiU5CY6BW0?t=631) **[[scripting-and-performance]]** Handle both CollectionService GetTagged and GetInstanceAddedSignal so buttons added later or loaded in a different order still work.
- [11:11](https://youtu.be/TmiU5CY6BW0?t=671) **[[common-mistakes]]** A gamepass you created is auto-owned by you, so testing shows an 'already own' prompt; test with a separate account or expect that message.
- [12:17](https://youtu.be/TmiU5CY6BW0?t=737) **[[scripting-and-performance]]** Keep a server module mapping gamepass ID to a handler function; add new passes by adding entries without changing the player-join code.
- [13:39](https://youtu.be/TmiU5CY6BW0?t=819) **[[scripting-and-performance]]** Default the multiplier with 'or 1' when the attribute is nil so non-owners get unchanged values.
- [15:03](https://youtu.be/TmiU5CY6BW0?t=903) **[[scripting-and-performance]]** Check ownership on the server with MarketplaceService:UserOwnsGamePassAsync when the player joins and apply the perk there, not on the client.

## Numbers
- [1:34](https://youtu.be/TmiU5CY6BW0?t=94) Money multiplier gamepass effect: **2x money per collector drop** (Example pass in tutorial; copper drop 5 becomes 10)

## Games
- **Tycoon video 8 (creator's own tutorial place)** [0:54](https://youtu.be/TmiU5CY6BW0?t=54): Used as the base place to add a gamepass; no performance or revenue data shared.

## Tools
Roblox Creator Dashboard, Roblox Studio, StarterGui / ScreenGui / UIListLayout, CollectionService, MarketplaceService

## He points to
- Next video in series on developer products

## Quotes
- [1:34](https://youtu.be/TmiU5CY6BW0?t=94) "every time your block hits the collector that's value it's worth will be multiplied by two... it just applies globally to your game all the time"
- [9:08](https://youtu.be/TmiU5CY6BW0?t=548) "it's very important that it says prompt game pass purchase because... i just used prop product purchase and it never worked"

## Topics
[[common-mistakes]] [[core-loops-and-game-design]] [[monetisation-gamepasses]] [[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
