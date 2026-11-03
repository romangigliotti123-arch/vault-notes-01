---
title: "Docs: resources / modules / profile-card"
url: https://create.roblox.com/docs/resources/modules/profile-card.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / profile-card

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/resources/modules/profile-card.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs page for the ProfileCard package module. Covers installing it from the Creator Store, how the card behaves for your own character versus other players (including age-based status filtering), and the configure() function with its keys and defaults for styling and behaviour.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/profile-card) **[[ui-ux-design]]** Call ProfileCard.configure() from a LocalScript in StarterPlayerScripts to override default styling and behaviour, rather than editing the module.
- [page](https://create.roblox.com/docs/resources/modules/profile-card) **[[ui-ux-design]]** Set maxClickDistance to limit how far away clicking a character opens its card; default is 100 studs.
- [page](https://create.roblox.com/docs/resources/modules/profile-card) **[[anti-exploit-and-security]]** Players' custom status text is subject to text filtering; expect free-text fields to be filtered and plan for it.
- [page](https://create.roblox.com/docs/resources/modules/profile-card) **[[age-ratings-moderation-and-tos]]** Players under 13 only see status messages that are appropriate for their age group; do not rely on status text being visible to all players.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/profile-card) maxClickDistance default: **100 studs** (Max distance from camera at which a clicked character's card appears)
- [page](https://create.roblox.com/docs/resources/modules/profile-card) backgroundTransparency default: **0.2** (Default card background transparency)
- [page](https://create.roblox.com/docs/resources/modules/profile-card) cornerRadiusValue default: **20** (UICorner radius used when hasRoundedCorners is true)
- [page](https://create.roblox.com/docs/resources/modules/profile-card) borderThickness default: **3** (Border thickness when hasBorder is true)

## Tools
Creator Store Packages (ProfileCard module), ProfileCard.configure()

## Topics
[[age-ratings-moderation-and-tos]] [[anti-exploit-and-security]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
