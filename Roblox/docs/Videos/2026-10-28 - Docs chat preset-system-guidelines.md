---
title: "Docs: chat / preset-system-guidelines"
url: https://create.roblox.com/docs/chat/preset-system-guidelines.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: chat / preset-system-guidelines

[Open](https://create.roblox.com/docs/chat/preset-system-guidelines.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on preset systems (predefined-text wheels for in-game coordination). Defines allowed and disallowed preset content, safety rules around age checks, and mandatory implementation requirements: TextService filtering, 10-second rate limit, 12-preset cap, no terminal punctuation, and "system preset" labeling. Recommends using built-in Quick Words where possible.

## Tips
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[community-and-discord]]** Prefer Roblox's built-in Quick Words system over building a custom preset system; it already complies with preset guidelines.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[common-mistakes]]** Do not build alphabet wheels, number-based encoding, or question/answer structures; these are explicitly disallowed preset patterns.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[common-mistakes]]** Do not let presets simulate free-form chat, flattery unrelated to gameplay, or back-and-forth dialogue across age groups.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[age-ratings-moderation-and-tos]]** Presets that enable dynamic or directed conversation require users to be age checked (Facial Age Estimation or ID verification) and of similar age to chat.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[age-ratings-moderation-and-tos]]** Presets limited to gameplay actions, confirmations, or basic reactions can be used regardless of age or age-check status.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[age-ratings-moderation-and-tos]]** Run every preset through Class.TextService:FilterStringAsync() before sending.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[ui-ux-design]]** Label all preset UI as 'system preset' in chat and make it visually distinct from native freeform chat.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[ui-ux-design]]** Omit terminal punctuation (! ? .) from presets so they are not confused with general chat messages.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[client-server-and-remotes]]** Rate-limit preset sends to one every 10 seconds per player.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[game-ideas-and-genres]]** Keep the preset list to 12 or fewer per universe, finite and creator-controlled.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[core-loops-and-game-design]]** Write presets that express immediate gameplay intent and stand alone, e.g. 'Need help', 'Defending this area', 'Enemy nearby', 'Reloading'.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[common-mistakes]]** Avoid slang or words with evolving meanings, real-world contact or identity references, and emotional pressure in presets.
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) **[[updates-live-ops]]** Expect Roblox review of preset content; be ready to change or remove presets, and keep future updates compliant.

## Numbers
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) Send rate limit: **10 seconds per send** (Required rate limit for preset sends)
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) Max presets displayed: **12 or fewer** (Per Universe, required cap)

## Tools
TextService:FilterStringAsync(), Quick Words (built-in)

## He points to
- Roblox Community Standards
- Roblox Terms of Use

## Quotes
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) "If players can use the wheel to "say anything, just slower," the design is not permitted."
- [page](https://create.roblox.com/docs/chat/preset-system-guidelines) "Preset systems must reinforce existing Roblox safety features – not work around them."

## Topics
[[age-ratings-moderation-and-tos]] [[client-server-and-remotes]] [[common-mistakes]] [[community-and-discord]] [[core-loops-and-game-design]] [[game-ideas-and-genres]] [[ui-ux-design]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
