---
title: ArTheDev - Numbers & Benchmarks
tags: [roblox, arthedev]
creator_trust: TRUSTED
creator_score: 8.5
---

> [!note] Trust: TRUSTED (credibility audit score 8.5): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# ArTheDev: Numbers & Benchmarks

| Date | Topic | Metric | Value | Context | Source |
|---|---|---|---|---|---|
| 2025-03-18 | core-loops-and-game-design | XP requirement increase per level | +5 XP in the example, scaled per level | Demo example; XP requirement rises each level | [0:42](https://youtu.be/V7PdX03D_hM?t=42) |
| 2025-03-18 | ui-ux-design | Tween duration for XP bar | 2 seconds | Default TweenInfo duration in the example | [14:20](https://youtu.be/V7PdX03D_hM?t=860) |
| 2025-03-20 | social-features-and-virality | invite timeout | 10 seconds | Invite popup auto-dismisses after 10 seconds | [16:22](https://youtu.be/5QZA1_0L9PU?t=982) |
| 2025-03-20 | social-features-and-virality | invite cooldown | present | Cooldown before re-inviting a player who left; exact length not stated | [1:21](https://youtu.be/5QZA1_0L9PU?t=81) |
| 2025-07-13 | combat-and-gameplay-systems | Example state duration | 4 seconds (clicked=true), 1.5 seconds in demo | ProximityPrompt demo state timers | [19:52](https://youtu.be/WImDkrf3sAo?t=1192) |
| 2025-07-25 | combat-and-gameplay-systems | Combo max | 3 hits in demo | M1 combo chain length in the demo; changing it needs edits in server script | [0:00](https://youtu.be/Pi8rQ9gGTKE?t=0) |
| 2025-07-25 | combat-and-gameplay-systems | Combo reset time | 1.5 s | M1 combo resets if no hit within this window | [15:11](https://youtu.be/Pi8rQ9gGTKE?t=911) |
| 2025-07-25 | combat-and-gameplay-systems | M1 cooldown | 0.5 s | Client-side cooldown between M1 attacks | [15:11](https://youtu.be/Pi8rQ9gGTKE?t=911) |
| 2025-07-25 | player-psychology-and-game-feel | Perfect block window | 0.1 s | Time after pressing block that counts as a perfect block | [29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772) |
| 2025-07-25 | combat-and-gameplay-systems | Attack can't-do-anything state | 0.5 s | Lockout applied to all actions after an attack | [24:00](https://youtu.be/Pi8rQ9gGTKE?t=1440) |
| 2025-07-25 | combat-and-gameplay-systems | Stun duration on hit | 6 s | Stun applied to target on hit in server attack logic | [29:32](https://youtu.be/Pi8rQ9gGTKE?t=1772) |
| 2025-07-25 | vfx-and-particles | Hit effect lifetime | 0.5 s | Debris cleanup time for cloned effect attachments | [34:22](https://youtu.be/Pi8rQ9gGTKE?t=2062) |
| 2025-07-25 | combat-and-gameplay-systems | Evasive i-frame duration | 1.5 s | I-frame duration in the demo evasive | [42:38](https://youtu.be/Pi8rQ9gGTKE?t=2558) |
| 2025-07-25 | combat-and-gameplay-systems | Evasive cooldown | 10 s | Cooldown preventing evasive spam | [43:19](https://youtu.be/Pi8rQ9gGTKE?t=2599) |
| 2025-07-31 | scripting-and-performance | Example base M1 cooldown | 0.4 seconds | Example value from base cooldowns table | [6:03](https://youtu.be/_6F6vRt_9sM?t=363) |
| 2025-07-31 | combat-and-gameplay-systems | Example add modifier value | +5 seconds (cooldown 7s) | Demonstration of add modifier on equip ability | [29:52](https://youtu.be/_6F6vRt_9sM?t=1792) |
| 2025-10-03 | player-psychology-and-game-feel | Sprint double-tap threshold | 2 seconds | Time window between two W presses to trigger sprint | [2:38](https://youtu.be/KaCj7Jld35Q?t=158) |
| 2025-10-03 | core-loops-and-game-design | Sprint speed multiplier | 1.5x base speed | Default in module; base speed 12 | [0:00](https://youtu.be/KaCj7Jld35Q?t=0) |
| 2025-10-03 | core-loops-and-game-design | Double jump reset | 0.3 seconds | Double-jump flag cleared after 0.3s | [22:02](https://youtu.be/KaCj7Jld35Q?t=1322) |
| 2026-03-31 | development-process-and-speed | Learning methods covered | 7 | YouTube, Discord, DevForum, AI, toolbox code, mini projects, coaching | [0:00](https://youtu.be/R3q6hZs8FDE?t=0) |
| 2026-04-03 | core-loops-and-game-design | Weather chance (sunny) | 40% |  | [7:01](https://youtu.be/CnZEnFVAFSw?t=421) |
| 2026-04-03 | core-loops-and-game-design | Weather chance (rain) | 20% |  | [7:01](https://youtu.be/CnZEnFVAFSw?t=421) |
| 2026-04-03 | core-loops-and-game-design | Weather chance (cloudy, partly cloudy, foggy, snow) | 10% each |  | [7:01](https://youtu.be/CnZEnFVAFSw?t=421) |
| 2026-04-03 | scripting-and-performance | Weather tick interval | 1 second |  | [10:25](https://youtu.be/CnZEnFVAFSw?t=625) |
| 2026-04-06 | retention-d1-d7 | Autosave interval | 300 seconds (configurable) | Autosave loop default in server DataStore script | [2:43](https://youtu.be/RDjsR4iIRlg?t=163) |
| 2026-04-18 | monetisation-devproducts | summon price | 50 gems per summon at price tier 1 (example from video) | Demo player started with 600 gems; single summon costs 200 at default setting | [0:52](https://youtu.be/Iy9xuT1bpY4?t=52) |
| 2026-04-18 | monetisation-devproducts | multi-summon size | 10 max per request | Server rejects amounts above 10 or below 1 | [9:26](https://youtu.be/Iy9xuT1bpY4?t=566) |
| 2026-04-18 | ui-ux-design | click debounce | 0.5 seconds | Delay between reveal clicks, adjustable | [24:25](https://youtu.be/Iy9xuT1bpY4?t=1465) |
| 2026-04-18 | ui-ux-design | reveal wait | 2s single summon, 0.5s per multi summon | Wait time between reveals, adjustable | [16:57](https://youtu.be/Iy9xuT1bpY4?t=1017) |
| 2026-04-18 | ui-ux-design | blur size | 24 during summon, 0 when finished | Lighting blur tween on summon start and end | [27:11](https://youtu.be/Iy9xuT1bpY4?t=1631) |
| 2026-04-18 | core-loops-and-game-design | example rarity weight | common = 100 in weight table | Weights summed to total; higher weight means higher chance | [12:11](https://youtu.be/Iy9xuT1bpY4?t=731) |
| 2026-06-07 | common-mistakes | Time spent planning before building | 6 months | Example of beginner planning a dream game for 6 months | [0:00](https://youtu.be/wG9XzLnJC5k?t=0) |
| 2026-06-07 | analytics-metrics | Players in a finished small game vs unfinished large game | 12 players vs zero | Speaker's comparison of finished versus abandoned projects | [2:43](https://youtu.be/wG9XzLnJC5k?t=163) |
| 2026-06-07 | development-process-and-speed | Time to finish a simple obby | 1 week | Speaker says finishing it teaches more than a giant RPG abandoned later | [2:43](https://youtu.be/wG9XzLnJC5k?t=163) |
| 2026-09-26 | ui-ux-design | Message color presets | 3 starting (red, blue, pink) plus added green; name and message colors set per preset | Preset table in module; name color fixed, message color changes | [6:17](https://youtu.be/fIwzczfIu2U?t=377) |
| 2026-09-26 | client-server-and-remotes | Random color pick range | math.random(0.1,3) indexing 3 options | Demo button picks a random color preset | [15:56](https://youtu.be/fIwzczfIu2U?t=956) |
| 2026-09-26 | first-session-onboarding | Demo wait before announce | 2 seconds | Task wait before firing test announcement | [5:28](https://youtu.be/fIwzczfIu2U?t=328) |
| 2026-09-30 | scripting-and-performance | Movement speed (Z offset per second) | 75 (tuned value used in example) | Forward speed for cloned hollow purple effect, scaled by delta time | [27:52](https://youtu.be/HjDD_0cDfPg?t=1672) |
| 2026-09-30 | vfx-and-particles | PointLight brightness tween duration | 0.5 seconds (example 0.25 with TweenSpeed attribute) | Default tween for light fade in/out in FX handler | [13:07](https://youtu.be/HjDD_0cDfPg?t=787) |
| 2026-09-30 | scripting-and-performance | Effect cleanup timing | Destroy after 7s, disconnect after additional 4s | Example ability lifetime cleanup values | [30:35](https://youtu.be/HjDD_0cDfPg?t=1835) |
| 2026-10-05 | combat-and-gameplay-systems | Ability cooldown (state duration) | 7 seconds | Demo ability cooldown set via server state handler | [16:41](https://youtu.be/QRFuxryK4Vg?t=1001) |
| 2026-10-05 | combat-and-gameplay-systems | Client lock duration after cast | 6 seconds | Client-side lock task.delay in the demo ability | [13:20](https://youtu.be/QRFuxryK4Vg?t=800) |
| 2026-10-05 | combat-and-gameplay-systems | Windup before hit | 2.5 seconds | Wait before firing the demo ability's hitbox | [22:09](https://youtu.be/QRFuxryK4Vg?t=1329) |
| 2026-10-05 | combat-and-gameplay-systems | Hitbox lifetime | 6 seconds | Debris cleanup of hitbox part | [20:07](https://youtu.be/QRFuxryK4Vg?t=1207) |
| 2026-10-05 | combat-and-gameplay-systems | Hit-loop duration before disconnect | 4 seconds | Heartbeat hit detection runs then disconnects | [26:23](https://youtu.be/QRFuxryK4Vg?t=1583) |
