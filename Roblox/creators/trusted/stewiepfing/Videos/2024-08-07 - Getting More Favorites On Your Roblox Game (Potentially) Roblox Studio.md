---
title: "Getting More Favorites On Your Roblox Game (Potentially) | Roblox Studio"
url: https://youtu.be/OLrTDcjYWGw
creator: Stewiepfing
official: false
advice_density: medium
date: 2024-08-07
views: 6208
transcript: auto-captions
confidence: high
tags: [roblox, stewiepfing, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Getting More Favorites On Your Roblox Game (Potentially) | Roblox Studio

[Watch](https://youtu.be/OLrTDcjYWGw) | stewiepfing | 6,208 views | 2024-08-07

## Summary
Shows how to use AvatarEditorService:PromptSetFavorite in a LocalScript to prompt players to favorite the game during play. Covers getting the place ID, item type enum (Asset), and a RunService timer that prompts after a set duration (e.g. 5 to 10 minutes) instead of on join.

## Tips
- [2:25](https://youtu.be/OLrTDcjYWGw?t=145) **[[social-features-and-virality]]** Use the place ID (not universe ID) when prompting favorites; get it from Asset Manager or the creations URL.
- [5:04](https://youtu.be/OLrTDcjYWGw?t=304) **[[first-session-onboarding]]** Don't prompt for favorites on join; new players haven't seen the game yet. Prompt after a delay of several minutes of play instead.
- [8:33](https://youtu.be/OLrTDcjYWGw?t=513) **[[social-features-and-virality]]** Set the favorite prompt delay to roughly 2 to 5 minutes depending on retention; shorter if the game has weaker retention.

## Numbers
- [8:33](https://youtu.be/OLrTDcjYWGw?t=513) Suggested favorite prompt delay: **2 to 5 minutes (300 seconds)** (Speaker's suggested range based on retention, for a fairly good game)

## Tools
Roblox Studio, AvatarEditorService:PromptSetFavorite, RunService.RenderStepped, Asset Manager

## Topics
[[first-session-onboarding]] [[social-features-and-virality]]

Back to [[stewiepfing - How to make successful Roblox games]]
