---
title: "Roblox Developer Conference 2018 - Accessing a Global Market"
url: https://youtu.be/qoWMP-AFT08
creator: Roblox
official: true
advice_density: high
date: 2018-07-24
views: 4147
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Roblox Developer Conference 2018 - Accessing a Global Market

[Watch](https://youtu.be/qoWMP-AFT08) | RobloxOfficial | 4,147 views | 2018-07-24

## Summary
Roblox DevConf 2018 talk by engineer Giovanni Contini on game localization. Covers why localize (about 20% of world speaks English, roughly 5% natively), a live Jailbreak Spanish demo using the localization service and Google Sheets translation, language pitfalls (grammatical gender, conjugation, plurals, number formatting, text length), creative translation with translator notes, and tips on using localization tables and the auto-translation system.

## Tips
- [4:19](https://youtu.be/qoWMP-AFT08?t=259) **[[building-art-and-assets]]** Export the localization table, run a rough first-pass translation (Google Sheets Translate macro), fix broken parameter tokens, re-import CSV, and test with the Spanish button.
- [9:15](https://youtu.be/qoWMP-AFT08?t=555) **[[common-mistakes]]** Don't build kill feeds or messages from concatenated sentences with parameters; grammar in Spanish etc. changes verb forms and gender, forcing sentence rewrites.
- [9:56](https://youtu.be/qoWMP-AFT08?t=596) **[[building-art-and-assets]]** Use icons instead of words for weapons and currency; icons avoid gender, plural, and conjugation problems in translation.
- [12:02](https://youtu.be/qoWMP-AFT08?t=722) **[[building-art-and-assets]]** Use the localization system's format strings for numbers instead of hand-formatting, since digit grouping and decimal rules vary by locale.
- [13:24](https://youtu.be/qoWMP-AFT08?t=804) **[[ai-and-tools]]** Leave roughly 30-50% extra space for long-text languages and up to 2-3x for short strings; plan UI for text overflow.
- [15:18](https://youtu.be/qoWMP-AFT08?t=918) **[[common-mistakes]]** Machine translation loses idioms, puns and memes; add translator notes explaining intent and maintain two-way communication with translators.
- [18:03](https://youtu.be/qoWMP-AFT08?t=1083) **[[building-art-and-assets]]** Consider tailoring art and cultural preferences per region, as League of Legends did with Karma art for China versus North America.
- [18:44](https://youtu.be/qoWMP-AFT08?t=1124) **[[community-and-discord]]** Plan community support for foreign players: local Twitter, YouTubers, giveaways, codes, and issue reporting channels.
- [19:26](https://youtu.be/qoWMP-AFT08?t=1166) **[[ai-and-tools]]** Automatic translation can't handle typewriter text or incomplete strings and breaks when source text changes; use it as a fallback and move to localization APIs for maintained games.
- [20:06](https://youtu.be/qoWMP-AFT08?t=1206) **[[development-process-and-speed]]** Put all text in localization tables from the start, even before localizing, to avoid costly refactoring later.
- [21:28](https://youtu.be/qoWMP-AFT08?t=1288) **[[building-art-and-assets]]** Write a thin localization helper module and a small plugin (e.g. one-button dialogue table update) that knows where your text lives.
- [22:09](https://youtu.be/qoWMP-AFT08?t=1329) **[[scripting-and-performance]]** Disable auto-localize on GUIs you handle in scripts, and localize on the client; send event info over RemoteEvents, not localized text.

## Numbers
- [1:41](https://youtu.be/qoWMP-AFT08?t=101) Global English reach: **~20% of world speaks English (incl. non-native); ~5% native** (Speaker's figure justifying localization)
- [5:41](https://youtu.be/qoWMP-AFT08?t=341) Jailbreak Spanish demo time: **~1.5 minutes (sub-minute possible)** (Minimal first-pass localization workflow shown live)
- [8:34](https://youtu.be/qoWMP-AFT08?t=514) Spanish verb forms: **~30 forms for 'demonstrate'** (Illustrates conjugation complexity)
- [10:38](https://youtu.be/qoWMP-AFT08?t=638) Russian plural forms: **3 forms (singular plus two plural forms by last digit)** (Plural rules vary by language)
- [13:24](https://youtu.be/qoWMP-AFT08?t=804) Text expansion allowance: **Long strings expand less; allow ~30-50% extra; short strings can be 2-3x longer** (IBM globalization guidelines table)

## Games
- **Jailbreak** [4:19](https://youtu.be/qoWMP-AFT08?t=259): Used as the live demo; scraped texts, machine-translated via Sheets, tested in Spanish in about 1.5 minutes.
- **2018 Egg Hunt** [15:18](https://youtu.be/qoWMP-AFT08?t=918): Loading screen puns were creatively re-written for Spanish (Thursday replaced by a pun on huevos) rather than literally translated.
- **League of Legends** [18:03](https://youtu.be/qoWMP-AFT08?t=1083): Karma character art differs between China and North America to suit regional tastes.
- **Mining Simulator** [15:18](https://youtu.be/qoWMP-AFT08?t=918): Mentioned as possibly the first top-played game localized to Spanish with the Roblox system.
- **TF2 / Counter-Strike / Overwatch** [9:56](https://youtu.be/qoWMP-AFT08?t=596): Use username plus weapon icon kill feeds, which avoid translation grammar problems.

## Tools
Roblox Localization Service, Localization tables, Localization table API, Automatic text scraper, Google Sheets Translate macro, Roblox Studio Spanish test button

## He points to
- Roblox developer forums (Q&A contact)
- IBM globalization guidelines (text expansion table)
- Roblox DevHub localization docs

## Quotes
- [1:41](https://youtu.be/qoWMP-AFT08?t=101) "localization is way more than just translation; a lot of people miss that"
- [15:18](https://youtu.be/qoWMP-AFT08?t=918) "A computer can't pull off stunts like this for you; without open communication with translators, they won't rewrite content."
- [2:21](https://youtu.be/qoWMP-AFT08?t=141) "Your first pass localization will pretty much be a weekend project, but getting it right can take a lot more effort."

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[common-mistakes]] [[community-and-discord]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
