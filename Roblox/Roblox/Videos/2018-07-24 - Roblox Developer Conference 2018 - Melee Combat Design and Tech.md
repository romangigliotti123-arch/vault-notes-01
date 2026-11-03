---
title: "Roblox Developer Conference 2018 - Melee Combat: Design and Tech"
url: https://youtu.be/f8cSSzVnh9s
creator: Roblox
official: true
advice_density: high
date: 2018-07-24
views: 25331
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Roblox Developer Conference 2018 - Melee Combat: Design and Tech

[Watch](https://youtu.be/f8cSSzVnh9s) | RobloxOfficial | 25,331 views | 2018-07-24

## Summary
Roblox Developer Conference 2018 talk by senior physics engineer Val C on designing melee combat for Roblox. Covers why melee is harder than shooters (latency, bidirectional interaction), core systems (stagger, parry, block/dodge, stamina, directional attacks, guard break), client-driven vs server hit detection, polish loops, and a niche opportunity for intense melee games. Includes Q&A on projectiles, tunneling, and younger audiences.

## Tips
- [8:14](https://youtu.be/f8cSSzVnh9s?t=494) **[[core-loops-and-game-design]]** Build stagger into every hit so the hit player gets feedback to stop spamming; stagger communicates mistakes better than a health bar.
- [12:33](https://youtu.be/f8cSSzVnh9s?t=753) **[[core-loops-and-game-design]]** Give parries a risky, mastery-rewarding payoff; players who parry consistently become feared yet learnable, adding depth over time.
- [11:54](https://youtu.be/f8cSSzVnh9s?t=714) **[[core-loops-and-game-design]]** Balance offense and defense so neither extreme dominates; design feedback that discourages spamming, passive blocking, and rewards calculated risk.
- [15:27](https://youtu.be/f8cSSzVnh9s?t=927) **[[core-loops-and-game-design]]** Add a stamina system to prevent attack spam, and use directional attacks and blocks so defense is an active choice, not a passive hold.
- [17:30](https://youtu.be/f8cSSzVnh9s?t=1050) **[[development-process-and-speed]]** Build data-driven attack systems: add new attacks as data entries rather than writing unique code per attack.
- [18:31](https://youtu.be/f8cSSzVnh9s?t=1111) **[[scripting-and-performance]]** For 1v1 duels, use fixed animation timing (e.g. 700ms heavy attack) and a non-physics range/time check so timing is consistent for players.
- [19:12](https://youtu.be/f8cSSzVnh9s?t=1152) **[[scripting-and-performance]]** Favor the active attacker with client-driven logic for responsiveness, accepting some desync; keep slow attacks so desync is a small share of duration.
- [21:18](https://youtu.be/f8cSSzVnh9s?t=1278) **[[core-loops-and-game-design]]** Make parry a timed window at the end of an attack that costs your block for that period; this creates a read-and-counter risk.
- [22:56](https://youtu.be/f8cSSzVnh9s?t=1376) **[[building-art-and-assets]]** Make hit feedback unambiguous: unique animation per hit direction plus sparkle effects for blocks, so players know why an attack failed.
- [24:17](https://youtu.be/f8cSSzVnh9s?t=1457) **[[building-art-and-assets]]** Invest in parry animations and particle effects that are slowed down and obvious; they make players feel cool without health bars or status icons.
- [26:03](https://youtu.be/f8cSSzVnh9s?t=1563) **[[playtesting-and-feedback]]** Expect polish to take most of the time: play your prototype repeatedly and tune stagger, hit movement and animations until they feel weighty.
- [26:44](https://youtu.be/f8cSSzVnh9s?t=1604) **[[building-art-and-assets]]** Push characters back on stagger based on hit direction so attacks feel impactful and fights have momentum.
- [27:26](https://youtu.be/f8cSSzVnh9s?t=1646) **[[scripting-and-performance]]** For competitive games, move hit logic to the server to resist exploiters, accepting some loss of client responsiveness and latency-related misfires.
- [29:12](https://youtu.be/f8cSSzVnh9s?t=1752) **[[game-ideas-and-genres]]** Intense, in-depth melee combat is an underserved Roblox niche compared with FPS; being first with a deep melee game gives easier market entry.
- [29:52](https://youtu.be/f8cSSzVnh9s?t=1792) **[[development-process-and-speed]]** Expect to write your own melee engine in Lua on top of Roblox; melee is art-intensive, requiring many custom animations.
- [33:18](https://youtu.be/f8cSSzVnh9s?t=1998) **[[core-loops-and-game-design]]** Add a guard break mechanic so blocking cannot be spammed; avoid having two options with identical results and weaknesses.
- [33:59](https://youtu.be/f8cSSzVnh9s?t=2039) **[[core-loops-and-game-design]]** Avoid solved, tic-tac-toe-like combat where one strategy always wins; add layers of depth so mastery remains possible.
- [36:05](https://youtu.be/f8cSSzVnh9s?t=2165) **[[scripting-and-performance]]** For fast projectiles, set network ownership to the player with SetNetworkOwnership and enlarge projectile colliders to counter discrete-physics tunneling.
- [40:09](https://youtu.be/f8cSSzVnh9s?t=2409) **[[core-loops-and-game-design]]** Use combos to gate powerful attacks behind setup steps, making high-reward moves predictable and fair to defend.
- [45:04](https://youtu.be/f8cSSzVnh9s?t=2704) **[[first-session-onboarding]]** For younger audiences, keep systems simple but discoverable; accidental parries that feel good let kids learn the mechanic by playing.
- [45:44](https://youtu.be/f8cSSzVnh9s?t=2744) **[[game-ideas-and-genres]]** Target older Roblox players seeking depth when designing complex combat; don't force that complexity on younger audiences.

## Numbers
- [2:09](https://youtu.be/f8cSSzVnh9s?t=129) Speaker tenure at Roblox: **about 4.5 years** (Speaker says he has been at Roblox about four and a half years)
- [17:30](https://youtu.be/f8cSSzVnh9s?t=1050) Latency example: **50 ms** (Speaker's example of lag; attacks faster than this may be unreactable)
- [18:31](https://youtu.be/f8cSSzVnh9s?t=1111) Heavy attack duration: **700 ms** (Fixed heavy attack timing used in demo for consistent 1v1 duel timing)
- [43:02](https://youtu.be/f8cSSzVnh9s?t=2582) Demo wind-up example: **200 ms wind-up, damage at 700 ms** (Non-physics check delays damage until fixed attack time)
- [36:46](https://youtu.be/f8cSSzVnh9s?t=2206) Physics rate: **240 Hz** (Roblox physics frame rate cited in discussing tunneling of fast projectiles)

## Games
- **Legendary** [5:10](https://youtu.be/f8cSSzVnh9s?t=310): Has a stagger system; speaker says it's closest to the ideal melee design but needs more layers of depth for mastery.
- **Phantom Forces** [3:31](https://youtu.be/f8cSSzVnh9s?t=211): Shows Roblox shooter gameplay quality and animation standards rivaling Call of Duty-style games.
- **Polygons** [3:31](https://youtu.be/f8cSSzVnh9s?t=211): Cited as a high-quality Roblox shooter with strong animation and gameplay standards.
- **Dragon Ball Z games** [12:33](https://youtu.be/f8cSSzVnh9s?t=753): Even light hits cause brief stagger, showing stagger is a common feedback tool in melee games.
- **Counter Blox / Beyond / Swordburst 2 / Dragon Ball Z Final Stand** [31:52](https://youtu.be/f8cSSzVnh9s?t=1912): Listed as Roblox gameplay sources the speaker used for reference videos.
- **For Honor** [16:07](https://youtu.be/f8cSSzVnh9s?t=967): Inspiration for directional attacks and guard break mechanics.

## Tools
Roblox Studio, Luau, Roblox physics engine, SetNetworkOwnership (set network round-trip API)

## He points to
- Game Maker's Toolkit - What Makes a Good Combat System (YouTube)
- Overwatch (melee character design reference)
- Mount and Blade (complex melee reference)
- Dark Souls (combat system reference)
- Street Fighter (combo system reference)

## Quotes
- [16:49](https://youtu.be/f8cSSzVnh9s?t=1009) "You don't want to be the tic-tac-toe of a melee combat game because everyone knows how to not lose a tic-tac-toe and it's just not fun."
- [29:12](https://youtu.be/f8cSSzVnh9s?t=1752) "I think there is a huge roblox market niche for really intense melee combat games just like there is for first-person shooters."
- [12:33](https://youtu.be/f8cSSzVnh9s?t=753) "Stagger is such an important feedback tool for saying hey I messed up I should stop doing whatever I just did."

## On screen
Contact sheet shows the table of contents slide, a shooter gameplay clip, raw melee prototype gameplay (blocky character, programmer art, a sword and health UI), an External Material slide linking Game Maker's Toolkit, and a Roblox Gameplay Sources list (Polyguns, Phantom Forces, Counter Blox, Beyond, Dragon Ball Z Final Stand, Swordburst 2, Legendary).

## Topics
[[building-art-and-assets]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[first-session-onboarding]] [[game-ideas-and-genres]] [[playtesting-and-feedback]] [[scripting-and-performance]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
