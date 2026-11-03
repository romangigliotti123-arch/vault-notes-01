---
title: DuckableDev - Studio & Scripting
creator: DuckableDev
tags: [roblox, duckabledev, theme]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# DuckableDev: Studio & Scripting

All DuckableDev tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2026-07-04 [4:04](https://youtu.be/eRhFPgj8tc4?t=244) Don't use math.random alone for rolls; players can predict pseudo-random output. Seed from multiple entropy sources (time, IDs) and hash them, server-side. ([[2026-07-04 - My Viral Roblox Game DIED… So I Made a Better One|My Viral Roblox Game DIED… So I Made a Better One]])
- 2026-08-04 [8:46](https://youtu.be/Cc7HT3uNjeQ?t=526) When merge logic fails, check for stale references: deleted droppers may still be indexed by old lookups, causing wrong merge results. ([[2026-08-04 - I Made a VIRAL Roblox Game Without AI|I Made a VIRAL Roblox Game Without AI]])
- 2026-08-30 [12:26](https://youtu.be/3XX3Y74hzq0?t=746) For bot AI, score every legal action (lane vulnerability, risk of losing a character) and pick the highest; add play-style weights for variety. ([[2026-08-30 - I’m Sick of SLOP… So I Made My DREAM Game|I’m Sick of SLOP… So I Made My DREAM Game]])

## [[building-art-and-assets]]
- 2026-07-04 [12:14](https://youtu.be/eRhFPgj8tc4?t=734) Fill empty maps early; a bare void map is an obvious flaw. Free nature asset packs can populate a map quickly. ([[2026-07-04 - My Viral Roblox Game DIED… So I Made a Better One|My Viral Roblox Game DIED… So I Made a Better One]])
- 2026-08-30 [6:52](https://youtu.be/3XX3Y74hzq0?t=412) Put repeated character animation code into one reusable animator module rather than duplicating it into every character model. ([[2026-08-30 - I’m Sick of SLOP… So I Made My DREAM Game|I’m Sick of SLOP… So I Made My DREAM Game]])

## [[ai-and-tools]]
- 2026-08-04 [21:21](https://youtu.be/Cc7HT3uNjeQ?t=1281) Creator's view: AI is useful as a tool for saving time but overuse removes the struggle that builds skill; use it deliberately. ([[2026-08-04 - I Made a VIRAL Roblox Game Without AI|I Made a VIRAL Roblox Game Without AI]])
- 2026-09-12 [18:20](https://youtu.be/MBRNAqkDEFA?t=1100) Ask AI for pointers and directions instead of full code ("follow the breadcrumbs") so you still write the logic yourself. ([[2026-09-12 - I Tested Every Roblox AI|I Tested Every Roblox AI]])
- 2026-09-12 [19:02](https://youtu.be/MBRNAqkDEFA?t=1142) Read every AI-generated chunk until you understand it; don't paste blindly. ([[2026-09-12 - I Tested Every Roblox AI|I Tested Every Roblox AI]])
- 2026-09-12 [19:02](https://youtu.be/MBRNAqkDEFA?t=1142) Type AI-suggested code out by hand instead of pasting it; it keeps you learning how the system works. ([[2026-09-12 - I Tested Every Roblox AI|I Tested Every Roblox AI]])
- 2026-09-12 [19:44](https://youtu.be/MBRNAqkDEFA?t=1184) Use AI sparingly. Vibe-coding without thinking erodes critical thinking and makes you dependent on the tool. ([[2026-09-12 - I Tested Every Roblox AI|I Tested Every Roblox AI]])
- 2026-09-12 [16:58](https://youtu.be/MBRNAqkDEFA?t=1018) Roblox lets you connect Claude or ChatGPT to Studio; this is an alternative to paid standalone Roblox AI generators. ([[2026-09-12 - I Tested Every Roblox AI|I Tested Every Roblox AI]])

## [[code-architecture-and-frameworks]]
- 2025-02-14 [3:15](https://youtu.be/6g8ZYtDKPBw?t=195) Use a component system with a module loader so objects like tables and chairs can find each other and form seating groups. ([[2025-02-14 - I'm Creating A Sandbox Tycoon on Roblox|I'm Creating A Sandbox Tycoon on Roblox]])
- 2026-08-04 [5:41](https://youtu.be/Cc7HT3uNjeQ?t=341) Use inheritance for repeated UI buttons: a base button class with subclasses (spawn, merge) instead of copy-pasting code. ([[2026-08-04 - I Made a VIRAL Roblox Game Without AI|I Made a VIRAL Roblox Game Without AI]])
- 2026-08-04 [6:22](https://youtu.be/Cc7HT3uNjeQ?t=382) Put reusable effects like tween/ripple/color flash into a ModuleScript so any button or system can call them. ([[2026-08-04 - I Made a VIRAL Roblox Game Without AI|I Made a VIRAL Roblox Game Without AI]])
- 2026-08-30 [10:24](https://youtu.be/3XX3Y74hzq0?t=624) Use a data-driven ability system with named event triggers (on ally enter, turn start, attacked) so new cards are added by data, not new code. ([[2026-08-30 - I’m Sick of SLOP… So I Made My DREAM Game|I’m Sick of SLOP… So I Made My DREAM Game]])

## [[client-server-and-remotes]]
- 2026-08-30 [2:44](https://youtu.be/3XX3Y74hzq0?t=164) Keep game state on the server and send visual updates to each client instead of spawning boards for everyone on the server; only two players use each board. ([[2026-08-30 - I’m Sick of SLOP… So I Made My DREAM Game|I’m Sick of SLOP… So I Made My DREAM Game]])

## [[building-and-level-design]]
- 2025-02-14 [1:55](https://youtu.be/6g8ZYtDKPBw?t=115) Build placement with build mode, click-to-place, delete toggle, and save progress; add satisfying placement/delete feedback effects. ([[2025-02-14 - I'm Creating A Sandbox Tycoon on Roblox|I'm Creating A Sandbox Tycoon on Roblox]])

## [[ui-ux-design]]
- 2025-02-14 [4:10](https://youtu.be/6g8ZYtDKPBw?t=250) Gather screenshots of other tycoons and make a mood board (Figma) before designing the building menu in Studio. ([[2025-02-14 - I'm Creating A Sandbox Tycoon on Roblox|I'm Creating A Sandbox Tycoon on Roblox]])
- 2025-02-14 [5:32](https://youtu.be/6g8ZYtDKPBw?t=332) Show a buy/sell cost popup so players see exactly how much they spent or refunded; use world-space pop-ups over billboard GUIs for text. ([[2025-02-14 - I'm Creating A Sandbox Tycoon on Roblox|I'm Creating A Sandbox Tycoon on Roblox]])
- 2026-05-01 [4:22](https://youtu.be/X9YYjb_mY5w?t=262) Design original UI instead of copying genre-standard styles; he prototyped in Figma before implementing to differentiate from similar games. ([[2026-05-01 - Can I Make $1M ROBUX in 30 DAYS|Can I Make $1M ROBUX in 30 DAYS?]])

## [[sound-and-music]]
- 2025-02-07 [3:22](https://youtu.be/OS-k2iOEfhM?t=202) Give every interaction a sound as feedback, and use atmospheric per-area music that complements gameplay rather than dominating it. ([[2025-02-07 - Roblox Fisch's Genius Strategy For Success|Roblox Fisch's Genius Strategy For Success]])

Up: [[DuckableDev - How to make successful Roblox games]]
