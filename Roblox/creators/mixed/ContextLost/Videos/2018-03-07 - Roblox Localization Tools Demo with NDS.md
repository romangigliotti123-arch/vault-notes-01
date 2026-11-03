---
title: "Roblox Localization Tools Demo with NDS"
url: https://youtu.be/wKjTYdVi4KE
creator: ContextLost
official: false
advice_density: medium
date: 2018-03-07
views: 21932
transcript: auto-captions
confidence: high
tags: [roblox, contextlost, youtube-learn]
creator_trust: MIXED
creator_score: 6.4
---

> [!note] Trust: MIXED (credibility audit score 6.4): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Roblox Localization Tools Demo with NDS

[Watch](https://youtu.be/wKjTYdVi4KE) | ContextLost | 21,932 views | 2018-03-07

## Summary
Roblox engineer demos the Localization Tools plugin: enable Text Capture to scrape GUI text during play, export the generated LocalizationTable to CSV, translate in Google Sheets (machine translation as a first pass), re-import, and test with the play-mode language set to Spanish. Covers limits: text in images, rich text and text animations are not handled.

## Tips
- [0:41](https://youtu.be/wKjTYdVi4KE?t=41) **[[localization-and-international]]** Enable Text Capture in the Localization Tools plugin, play the game to collect GUI text, then toggle it off to generate a LocalizationTable.
- [2:43](https://youtu.be/wKjTYdVi4KE?t=163) **[[localization-and-international]]** Use machine translation only as a first pass. Pay for professional or bilingual-friend translation if the game earns money, since literal translations lose context.
- [1:21](https://youtu.be/wKjTYdVi4KE?t=81) **[[localization-and-international]]** Use the context column to disambiguate identical strings that need different translations in different UI locations.
- [3:25](https://youtu.be/wKjTYdVi4KE?t=205) **[[localization-and-international]]** Test translations by setting the play-mode language in the plugin and playing, to see what that locale's players will see.
- [4:06](https://youtu.be/wKjTYdVi4KE?t=246) **[[localization-and-international]]** Put text that must be translated on a GUI TextLabel over an image, not baked into image art, since image text cannot be translated automatically.
- [4:06](https://youtu.be/wKjTYdVi4KE?t=246) **[[localization-and-international]]** Handle rich text effects and text animations in scripts. The automatic text replacement system does not handle them well.
- [4:47](https://youtu.be/wKjTYdVi4KE?t=287) **[[localization-and-international]]** Localization means making the game feel native, not just translated. Put research and effort into it beyond quick translations.

## Games
- **Natural Disaster Survival** [0:00](https://youtu.be/wKjTYdVi4KE?t=0): Used as the demo game to translate into Spanish via the localization workflow.

## Tools
Roblox Studio Localization Tools plugin, Text Capture / text scraper, LocalizationTable (generative), Google Sheets with Google Translate macro

## He points to
- Roblox Developer Portal localization articles
- Roblox Developer Forum

## Quotes
- [2:43](https://youtu.be/wKjTYdVi4KE?t=163) "If you have better options use them. Some players do notice, and do you appreciate it."
- [4:47](https://youtu.be/wKjTYdVi4KE?t=287) "If you stop at throwing in some quick translations and think you're done, you can't expect automatic success."

## Topics
[[localization-and-international]]

Back to [[ContextLost - How to make successful Roblox games]]
