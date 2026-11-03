---
title: "Mystery Code - Is this Free Model a VIRUS?"
url: https://youtu.be/oHgtXdgJF5U
creator: GnomeCode
official: false
advice_density: low
date: 2021-08-26
views: 386482
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Mystery Code - Is this Free Model a VIRUS?

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/oHgtXdgJF5U) | GnomeCode | 386,482 views | 2021-08-26

## Summary
Investigates a suspicious "night sky box" free model from the Creator Store. It contains an obfuscated script (hex-encoded strings) that checks friendship with a suspicious account, loads a second model, and posts server/game info to a Discord webhook. Concludes it's not a security risk (no password or cookie theft) but leaks data; advises deleting unknown scripts from free models.

## Tips
- [10:12](https://youtu.be/oHgtXdgJF5U?t=612) **[[anti-exploit-and-security]]** Delete any script in a free model you don't understand; free models can exfiltrate game data to external webhooks.
- [5:01](https://youtu.be/oHgtXdgJF5U?t=301) **[[anti-exploit-and-security]]** Format one-line minified scripts before reviewing them; decode hex-escaped strings to reveal hidden URLs like Discord webhooks.
- [3:40](https://youtu.be/oHgtXdgJF5U?t=220) **[[anti-exploit-and-security]]** Inspect Toolbox models' scripts, requires, and friend-gated logic before inserting them; a 'require' by asset ID can load hidden code.
- [0:37](https://youtu.be/oHgtXdgJF5U?t=37) **[[anti-exploit-and-security]]** Check free model creators for red flags like random usernames, no games, and clustered friend networks before trusting them.

## Numbers
- [1:25](https://youtu.be/oHgtXdgJF5U?t=85) Suspicious creator follower count: **~100,000 followers on a linked account (possibly botted)**

## Tools
Hex to decimal converter website, Hex to text converter website, Discord webhooks, Roblox Toolbox

## Topics
[[anti-exploit-and-security]]

Back to [[GnomeCode - How to make successful Roblox games]]
