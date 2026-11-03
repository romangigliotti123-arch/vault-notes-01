---
title: BubuTheDev - How to make successful Roblox games
tags: [roblox, bubuthedev, playbook]
videos: 8
generated: 2026-10-29
credibility: trusted
credibility_score: 7.9
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BubuTheDev - How to make successful Roblox games

BubuTheDev teaches small, script-light Roblox Studio tricks (death fades, conveyors, climbable ladders, FPS counters, pathfinding chase NPCs) and then tests whether Robux ads pay back. His core message: keep builds lean and cheap to run, price low to sell volume, sell cheap passes and developer products, and check ad delivery and net returns before scaling spend. His own ~2x ad-return claim is weakly supported by the numbers he shows, and his evidence comes from a single game.

**Style:** Fast, short Studio how-to videos aimed at beginners and hobbyists, with exact property values and snippets. Light on design theory, retention, or discovery. Strongest on single-game monetization and ad experiments, which are anecdotal. Suits developers who want quick fixes and a cautious, test-first attitude toward paid traffic.

## Playbook
1. **IDEA: Start from a simple, testable concept** [[game-ideas-and-genres]]: The creator's largest test was a simple basketball simulator (82HrjFTdPkU). A low-effort brainrot-style clone got zero impressions in its first 30 minutes (T3la9iXIGHQ). No formal ideation method is given, so favor concepts you can prototype quickly and check with a small test.
2. **BUILD: Prototype mechanics from ready-made pieces** [[core-loops-and-game-design]]: Mechanics are built from existing assets and models (ladders, stairs, conveyors, a chase NPC) rather than custom systems (0UYtSJvYe4U, UM7UtF4e0-0, xVUqKk3OnnU). No loop or retention design theory is given, so treat these as tactical snippets.
3. **BUILD: Fix level blockers with invisible collidable parts** [[building-and-level-design]]: Make ladders climbable with transparency-1 but collidable Truss Ladder parts placed behind the ladder. Make tall stairs walkable with a transparent collidable WedgePart ramp over the steps (0UYtSJvYe4U). Organize builds into named folders as you go.
4. **BUILD: Script-free moving parts** [[building-art-and-assets]]: Set a conveyor belt's AssemblyLinearVelocity in Properties (X = -50, or Z on rotated belts; flip the sign if it moves the wrong way) and delete the Toolbox per-0.1-second script (xVUqKk3OnnU). The creator claims a performance gain but shows no measurements.
5. **BUILD: Pathfinding chase NPC** [[physics-pathfinding-and-npc-ai]]: Place the Forbidden API pathfinding module from the Toolbox in ReplicatedStorage. Tune shortest-distance (example value 300) and refresh settings in the AI script so the NPC paths around obstacles (UM7UtF4e0-0). The tutorial is short and low-depth.
6. **BUILD: Death feedback fade** [[vfx-and-particles]]: On Humanoid.Died, wait 0.25 s, then tween every BasePart except Head, plus the face decal and accessory handles, to transparency 1 with TweenService instead of an instant reset (oYQ5jIZKE8s). This is entertainment-focused with little strategy.
7. **BUILD: Performance hygiene** [[optimization-and-streaming]]: Set CanTouch to false on decorative parts without Touched events and keep it true for triggers. Use transparency exactly 0 or 1 rather than values like 0.05 (0UYtSJvYe4U). The creator gives no measured frame-time data for these claims.
8. **BUILD: FPS counter in a screen corner** [[scripting-and-performance]]: Use a LocalScript that counts frames and updates the label once per second. Right-align it in a corner, slightly down, so it does not block the HUD. Test under Settings > Maximum frame rate caps of 120 and 144 (zc7vWpLOejE). Uncapped readings were about 200-240 FPS.
9. **BUILD: Price for volume, then add premium items** [[monetisation-gamepasses]]: A 99 Robux cosmetic-style pass (Rainbow Basketball) sold 135 copies and was the top gamepass. A ~1,000 Robux pass sold only 5 (82HrjFTdPkU). Amazing Deal at ~30 Robux sold 155 times for 3,234 Robux and was the top developer product. Low prices drove volume in this data.
10. **LAUNCH: Finish the game icon before paid traffic** [[thumbnails-icons]]: The game icon drives clicks in the sponsored tab and is the ad creative (0NK_JBYEILA). Finish and review the icon before spending any Robux on ads.
11. **LAUNCH: Configure a capped, narrow ad campaign** [[ads-and-sponsored-experiences]]: Create the ad at advertise.roblox.com (account must be 13+ and verified). Use a daily budget to cap spend, a sponsored experience ad set, and start with US and Canada. Narrow age and gender to your actual spenders and bid about 0.01-0.03 Robux per game (0NK_JBYEILA). The bid range is the creator's own practice and is unverified.
12. **LAUNCH: Verify delivery and net return before scaling** [[analytics-metrics]]: A 5,700 Robux ad test showed zero impressions after ~30 minutes (T3la9iXIGHQ), so confirm delivery first. The claimed ~2x ad return (82HrjFTdPkU) ignores Robux-to-cash fees and does not match the listed figures (~25k Robux revenue against 70k spent). Concurrency fell to 13 once ads were turned off.
13. **LIVE OPS: Retune prices against sales** [[pricing]]: Review gamepass and developer product sales in 72-hour windows (82HrjFTdPkU). Keep cheap items for volume. Raise prices only where sales hold up, since the ~1,000 Robux pass sold 5, up from 2 the day before.
14. **LIVE OPS: Keep the project updatable** [[development-process-and-speed]]: Organize the workspace into folders (for example Map, scripts, lighting) and give models descriptive names such as stairs or ladder so future updates are easy to navigate (0UYtSJvYe4U).

## Key numbers
- Death fade delay: 0.25 s before tweening to transparency 1 (oYQ5jIZKE8s)
- Conveyor: AssemblyLinearVelocity X = -50 replaces a script that loops every 0.1 s (xVUqKk3OnnU)
- FPS label update interval: 1 s; uncapped about 200-240 FPS, capped 120 and 144 (zc7vWpLOejE)
- Chase NPC shortest-distance example: 300 (UM7UtF4e0-0)
- Ad spend: 70,000 Robux (about 300 ad credits) on a basketball sim (82HrjFTdPkU)
- 72-hour revenue about 25,000 Robux: gamepasses 22,577 and developer products about 2,500 (82HrjFTdPkU)
- Rainbow Basketball: 99 Robux, 135 buyers, top gamepass (82HrjFTdPkU)
- Amazing Deal: about 30 Robux, 155 sales, 3,234 Robux earned (82HrjFTdPkU)
- About 1,000 Robux pass: 5 buyers, up from 2 (82HrjFTdPkU)
- Ad test budget 5,700 Robux, quoted reach about 3.2 million, zero impressions after ~30 min (T3la9iXIGHQ)
- Bid used by creator: about 0.01-0.03 Robux vs Roblox suggested 0.04-0.25 (0NK_JBYEILA, unverified)
- Ad creator minimum: 13+ and verified (0NK_JBYEILA)
- Claimed ad return about 2x, fees excluded; listed figures do not show 2x (82HrjFTdPkU)
- Concurrent players 13 after ads turned off (82HrjFTdPkU)
- Transparency: use 0 or 1, not 0.05; cost claim is unmeasured (0UYtSJvYe4U)

## Common mistakes
- Leaving a per-0.1-second Toolbox script on a conveyor instead of setting AssemblyLinearVelocity (xVUqKk3OnnU).
- Using near-zero transparency such as 0.05 on large-map parts; use exactly 0 or 1 (0UYtSJvYe4U). The cost claim is unmeasured.
- Leaving CanTouch true on decorative parts that have no Touched events (0UYtSJvYe4U).
- Spending Robux on ads before the game icon is finished, even though the icon drives sponsored-tab clicks (0NK_JBYEILA).
- Assuming an ad works without checking impressions; one ad had zero after 30 minutes (T3la9iXIGHQ).
- Treating gross Robux as profit: the ~2x return claim ignores fees (82HrjFTdPkU).
- Using a lifetime budget when you want to avoid spending credits quickly; a daily cap is the tool for that (0NK_JBYEILA).
- Using broad age and gender targeting without checking who actually spends Robux in your game (0NK_JBYEILA).
- Pricing a pass near 1,000 Robux and expecting volume; it sold 5 copies (82HrjFTdPkU).
- Following Roblox's suggested 0.04-0.25 bid range without testing; the creator says it is unnecessary (0NK_JBYEILA, unverified).

## Launch checklist
- [ ] Game icon finished, reviewed for click appeal, and used as ad creative (0NK_JBYEILA)
- [ ] Advertiser account is 13+ and verified before creating the ad (0NK_JBYEILA)
- [ ] Ad set is a sponsored experience with a daily budget cap, not a lifetime budget (0NK_JBYEILA)
- [ ] Audience starts with US and Canada; test before assuming it fits your game (0NK_JBYEILA)
- [ ] Age and gender narrowed to actual spenders once data exists (0NK_JBYEILA)
- [ ] Bid kept low (about 0.01-0.03 Robux per game) and checked against results (0NK_JBYEILA)
- [ ] Impressions checked within the first 30 minutes; if zero, check delivery status (T3la9iXIGHQ)
- [ ] Cheap cosmetic-style gamepass (about 99 Robux) included (82HrjFTdPkU)
- [ ] Low-price developer product (about 30 Robux) included (82HrjFTdPkU)
- [ ] Per-frame or per-interval loops removed; moving parts use AssemblyLinearVelocity (xVUqKk3OnnU)
- [ ] CanTouch set to false on decorative parts; true only for triggers (0UYtSJvYe4U)
- [ ] Transparency values set to exactly 0 or 1 (0UYtSJvYe4U)
- [ ] Death fade delay of 0.25 s in place if used (oYQ5jIZKE8s)
- [ ] FPS counter tested against 120 and 144 max frame rate caps (zc7vWpLOejE)
- [ ] Workspace organized into folders with descriptive model names (0UYtSJvYe4U)
- [ ] Gamepass and developer product sales tracked in 72-hour windows (82HrjFTdPkU)
- [ ] Concurrent players tracked after ads are turned off (82HrjFTdPkU)
- [ ] Net ad ROI calculated after Robux-to-cash fees before scaling spend (82HrjFTdPkU)

## How the advice changed over time
- Sep 2024 tutorials (oYQ5jIZKE8s, zc7vWpLOejE) are pure how-to with no monetization advice; business content appears from Dec 2024 onward.
- Dec 2024 (82HrjFTdPkU) makes a positive ad-return claim (~2x) with no ad-delivery caveats and fees excluded.
- Feb 2025 (T3la9iXIGHQ) reports zero ad impressions; the creator becomes more skeptical and stresses checking delivery first.
- Mar 2025 (0NK_JBYEILA) recommends bids of 0.01-0.03 Robux and rejects Roblox's suggested 0.04-0.25 range. This is the most recent bidding advice and supersedes the implied spend-first stance of Dec 2024; it is unverified.
- Jun 2025 (0UYtSJvYe4U) shifts to micro-performance tips (CanTouch, transparency 0 or 1) with no measurements, so the most recent performance guidance is unverified.
- No direct contradictions found on conveyors or the FPS counter across videos.

## Theme notes
- [[BubuTheDev - Monetisation|Monetisation]]
- [[BubuTheDev - Discovery & Algorithm|Discovery & Algorithm]]
- [[BubuTheDev - Thumbnails & Icons|Thumbnails & Icons]]
- [[BubuTheDev - Studio & Scripting|Studio & Scripting]]
- [[BubuTheDev - Mindset & Process|Mindset & Process]]
- [[BubuTheDev - Games Mentioned]]
- [[BubuTheDev - Numbers & Benchmarks]]
- [[BubuTheDev - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2024-09-06 - DON’T do this mistake in your Roblox games!|DON’T do this mistake in your Roblox games!]] (213 views, 2024-09-06): Script fades a dying character's parts after a 0.25s delay; entertainment-focused tutorial with little strategy.
- [[2024-09-07 - This makes your Roblox game slow, here’s how to fix it!|This makes your Roblox game slow, here’s how to fi]] (170 views, 2024-09-07): Replace a scripted conveyor with AssemblyLinearVelocity X = -50; claims performance gains, minimal depth.
- [[2024-09-08 - How to add a FPS COUNTER to your Roblox game!|How to add a FPS COUNTER to your Roblox game!]] (192 views, 2024-09-08): Adds an FPS counter updated once per second, tested against 120 and 144 frame caps.
- [[2024-09-17 - How to make an advanced NPC CHASE AI in Roblox Studio SIMPLE|How to make an advanced NPC CHASE AI in Roblox Stu]] (19,701 views, 2024-09-17): Toolbox Forbidden API chase NPC; tune shortest-distance and refresh settings in a short tutorial.
- [[2024-12-03 - I spent 70K ROBUX on ads, did I make profit|I spent 70K ROBUX on ads, did I make profit?]] (44,756 views, 2024-12-03): 70K Robux ad test with 22.6K gamepass earnings; claims 2x return while ignoring fees.
- [[2025-02-21 - I’ve advertised a trash brainrot game|I’ve advertised a trash brainrot game...]] (2,090 views, 2025-02-21): 5,700 Robux ad for a brainrot game got zero impressions after 30 minutes; low-effort test.
- [[2025-03-16 - How to set up Roblox ads PROPERLY!|How to set up Roblox ads PROPERLY!]] (4,275 views, 2025-03-16): UI walkthrough of Roblox ad setup: daily budgets, US and Canada targeting, low bids, icon creative.
- [[2025-06-09 - You NEED to know these TRICKS in Roblox Studio|You NEED to know these TRICKS in Roblox Studio]] (1,271 views, 2025-06-09): Seven Studio tips: autocomplete, truss ladders, wedge stairs, Reclass, CanTouch, transparency, folders.
