---
title: LovJak - How to make successful Roblox games
tags: [roblox, lovjak, playbook]
videos: 10
generated: 2026-10-29
credibility: trusted
credibility_score: 7.7
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# LovJak - How to make successful Roblox games

LovJak's playbook: start from a proven hit or a purchased template, but change the theme, levels, models, prices and core loop so the game isn't 'not unique'. Plan the full loop, build in small layers, and add a first-join tutorial and daily or playtime rewards. Ship new content before paying for ads, cap ad budgets, and judge results on 7-day averages rather than daily swings. Never pay a large upfront share for a game transfer. His own results were modest, so treat his numbers as small-sample evidence.

**Style:** Devlog-driven and experiment-based: he documents full builds and paid-ad tests with real numbers, including failures. Best for beginners and small teams who want template-to-game and ad case studies. Much of the advice is anecdotal, and his games peaked at only about 10 to 200 CCU.

## Playbook
1. **Pick a twist on a proven hit, and validate it** [[game-ideas-and-genres]]: Use a known hit as a starting point but change the theme or core fantasy: Grow a Garden became a plushie theme, and a tycoon became a restaurant that grows from nothing. Compare peak and average CCU before copying a genre; a 2M-visit game peaked at 1,000 CCU but averaged about 50.
2. **Start from a template, then change it substantially** [[development-process-and-speed]]: Templates save build time because their instructions make swaps quick. Never publish one unchanged: reorder and recolor levels, add stages, theme the map, swap the core collectible, and re-hook items to rarity and value. Fix economy bugs such as sell price equal to buy price.
3. **Learn fundamentals with small scripts** [[scripting-and-performance]]: Practice about 10 minutes a day with small scripts. Use print() to confirm code runs, read the Output window for errors like 'attempt to index nil', break problems into small parts, and use WaitForChild for GUIs and parts that may load late.
4. **Plan the full loop, then build layer by layer** [[core-loops-and-game-design]]: Plan the whole loop (cook, serve, wrong-customer handling, cleanup, reset) before building, because one devlog ran out of time before finishing it. Add effects, damage or rewards only after each piece works. Use staged growth models with a ProximityPrompt on the final stage.
5. **Build stat-based combat and gated progression** [[combat-and-gameplay-systems]]: Scale melee damage with a stat: 7 base plus strength/200. Require players to be near training objects to gain stats. Put a 2-minute per-player cooldown on arena re-entry and a stamina cost per punch paired with interval-only health regen so fights last.
6. **Persist world state across server changes** [[data-persistence]]: Save plant position, growth stage, mutation and state, and make loading work across server changes. The creator called this the hardest and longest part, so budget time for it. Use server-side distance and line-of-sight checks for any steal or interaction.
7. **Animate with timing discipline** [[3d-modeling-rigging-and-animation]]: Space keyframes further apart to slow motion; packed keyframes look like a fast smack. For walk cycles, use bigger leg and arm swings. Test every animation in-game, because timing feels different in playback than in the editor. Free built-in editor was enough for basics.
8. **Add a first-join tutorial and comfort options** [[first-session-onboarding]]: Add a tutorial that runs on first join so new players understand the loop before leaving. Add a mute-background-music button, since looping music is a problem in long sessions. Check that NPCs sit correctly and floors have no Z-fighting before release.
9. **Design gamepasses as core revenue** [[monetisation-gamepasses]]: Over 28 days gamepasses earned 7,400 Robux versus 3,700 from developer products, so design passes as a main revenue source. Set dev product prices and update their shop UI. Use per-player stock so each buyer only depletes their own supply.
10. **Commission icon and thumbnail before advertising** [[thumbnails-icons]]: Get a professional icon and thumbnail before running ads. One campaign reached 1.95% CTR on 82,000 impressions. If you are not an artist, outsource to a collaborator with art skills, as he did for plots and UI.
11. **Ship new content, then run small capped ad tests** [[ads-and-sponsored-experiences]]: Ship fresh content (fruits, levels, events) before spending on ads so paid traffic lands in a fresh game. Set a custom daily budget and a fixed number of days, and turn off auto-reload. Latest test: 10 credits per day for 3 days. Aim for Friday to Sunday when players are most active.
12. **Judge results over a window, not one day** [[analytics-metrics]]: Day-one ad snapshots were poor and improved later, so read 7-day moving averages. Paid traffic is cold, so engagement and day-1 retention can drop during ads. Track CCU, session time, crash rate, FPS and server memory, and check 5-minute retention early.
13. **Use group rewards, shorts and community** [[social-features-and-virality]]: Give group-join rewards and badges such as Welcome and Play With Friends. Make short vertical gameplay clips for YouTube Shorts and TikTok; one promo reached 2.2K views, about 7% above his other shorts. Ask Discord members for usernames to place as NPCs.
14. **Run live ops: rewards, timed events, scheduled updates** [[updates-live-ops]]: Add daily chests, login and playtime rewards, and a progress bar. Run timed events that change gameplay, and shorten event waits (20 to 15 min) to bring players back. Schedule the next update on the Roblox calendar and plan badges and events in advance. Remove features that worsen retention stats.

## Key numbers
- Base punch damage: 7 plus strength/200 (strength 200 gives 8)
- Players per arena server: 6 (2 fighting, 4 training)
- Arena re-entry cooldown: 2 minutes
- Practice time: 10 minutes a day
- Template game results: 3,254 visits, 884 Robux, 2,000 plays over 3 days
- Ad campaign: 5,500 Robux for 21 credits, about 16 used over 3 days
- Ad test: 10 credits per day for 3 days (30 credits)
- Icon/thumbnail ad CTR: 1.95% on 82,000 impressions (day 2)
- Session time on ad day 2: 4.1 minutes; 22% of players still playing after 5 minutes
- Reach: about 500 highly engaged players needed for all-ages targeting; he had 300
- Spawn cap: no single item above 40% of spawn
- Gamepass vs developer product Robux (28 days): 7,400 vs 3,700
- Home recommendations vs sponsored ads (28 days): 30,000 vs 12,000 players
- Peak vs average CCU warning: 1,000 peak, about 50 average on a 2M-visit game
- Upfront payment scam: 50% paid before ownership transfer

## Common mistakes
- Publishing a template unchanged; he judged it 'not unique' and unlikely to go viral without changing levels, models, prices and gameplay.
- Spending on ads before shipping new content, so paid traffic lands in a stale game.
- Leaving economy bugs, such as sell price equal to buy price, which leaves no profit.
- Shipping visible bugs like Z-fighting floors and NPC sitting glitches.
- Paying 50% upfront for a game transfer; the seller went silent after the first payment.
- Uploading AI-generated or user images without moderation checks; one flagged image got the account and groups locked.
- Leaving ad credit auto-reload on, which allows unplanned spending.
- Judging campaigns on day-one or daily swings instead of 7-day averages.
- Relying on paid ads alone; with zero home recommendations after about 6 days, discovery did not trigger.
- Copying a concept that already exists (swing obby for brain rots) instead of changing the core theme.

## Launch checklist
- [ ] Change theme, levels, models, prices and gameplay from any template before publishing.
- [ ] Play the full loop end-to-end and fix economy bugs (sell price must exceed buy price).
- [ ] Add a first-join tutorial.
- [ ] Add a mute background music button.
- [ ] Check floors for Z-fighting and NPC sit animations for glitches.
- [ ] Check uploaded or AI-generated images for moderation risk.
- [ ] Make gamepass icons work in-game and set developer product prices and shop UI.
- [ ] Use per-player stock and server-side distance and line-of-sight checks for steal mechanics.
- [ ] Commission a professional icon and thumbnail.
- [ ] Add a group-join reward and badges such as Welcome and Play With Friends.
- [ ] Schedule the next update on the Roblox calendar.
- [ ] Ship new content (fruits, levels, events) before buying ads.
- [ ] Set a custom daily ad budget, a fixed number of days, and turn off auto-reload.
- [ ] Track CCU, session time, crash rate, FPS and server memory during ads.
- [ ] Post on the Developer Forum asking for feedback and act on it.
- [ ] Ask Discord members for Roblox usernames to place in-game as NPCs.
- [ ] Confirm ownership transfer before paying the balance on any purchased game.
- [ ] Compare peak and average CCU on any game you plan to buy or copy.

## How the advice changed over time
- 2025 videos focused on basic Luau habits and free animation tools; 2026 videos shifted to buying templates and running paid ad experiments.
- Template stance changed: early reskins were framed as publish-ready, but later videos (KZ_mxVrvHCI, VHdyHvHOId8) say to change the core theme first and not publish unchanged.
- Ad budgets varied: 10 credits/day for 3 days (feVPsViqceo), 12 credits/day continuous with auto-reload off (Y602HH_KdOc), $16/day for 6 days (KZ_mxVrvHCI), and 10 credits/day again (VHdyHvHOId8). The most recent advice is a short, fixed, capped campaign.
- Stat judgement changed: early ad snapshots were read as poor; later he advised 7-day moving averages and not reacting to daily swings.
- Monetisation emphasis moved toward gamepasses as the main revenue source, after earlier videos leaned on group and badge rewards.
- Later videos added a warning about scams and moderation (VHdyHvHOId8), which earlier videos did not cover.

## Theme notes
- [[LovJak - Retention|Retention]]
- [[LovJak - Monetisation|Monetisation]]
- [[LovJak - Discovery & Algorithm|Discovery & Algorithm]]
- [[LovJak - Game Ideas|Game Ideas]]
- [[LovJak - Thumbnails & Icons|Thumbnails & Icons]]
- [[LovJak - Updates & Live Ops|Updates & Live Ops]]
- [[LovJak - Studio & Scripting|Studio & Scripting]]
- [[LovJak - Mindset & Process|Mindset & Process]]
- [[LovJak - Games Mentioned]]
- [[LovJak - Numbers & Benchmarks]]
- [[LovJak - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-05-03 - 5 Roblox Scripting Tips to Instantly Improve (With Code Examples!)|5 Roblox Scripting Tips to Instantly Improve (With]] (572 views, 2025-05-03): Five beginner Luau habits: print debugging, small pieces, WaitForChild, reading Output errors, and daily practice.
- [[2025-07-27 - I Tried Roblox Animation For 24 Hours!|I Tried Roblox Animation For 24 Hours!]] (1,004 views, 2025-07-27): A 24-hour animation log: spacing keyframes and bigger walk swings fix stiff, rushed-looking motion.
- [[2026-04-01 - I made a VIRAL Game with a FAMOUS Developer!|I made a VIRAL Game with a FAMOUS Developer!]] (4,326 views, 2026-04-01): April Fools fake collab, but its training and arena loop shows stat scaling and cooldown ideas.
- [[2026-05-01 - I Made a VIRAL Game Using a Roblox Game TEMPLATE|I Made a VIRAL Game Using a Roblox Game TEMPLATE]] (128,864 views, 2026-05-01): Template-to-game case: reskin, events, group rewards, and a 3-day ad test reaching 3,254 visits.
- [[2026-06-19 - I Remade The 1 Roblox Game!|I Remade The #1 Roblox Game!]] (12,335 views, 2026-06-19): Grow a Garden remake devlog: plots, saving plant state, Robux seed shop, and AI-assisted scripting.
- [[2026-07-09 - I spent $100 on Roblox Ads.. Was it worth it|I spent $100 on Roblox Ads.. Was it worth it?]] (12,080 views, 2026-07-09): A $100 ad test on a Grow a Garden clone: about 10 peak CCU, mostly USA and UK players.
- [[2026-07-31 - Can My DEAD ROBLOX GAME Go VIRAL!|Can My DEAD ROBLOX GAME Go VIRAL?!]] (17,809 views, 2026-07-31): Reviving a dead fruit game with 15,000 Robux of ads: gamepasses led revenue, and home recommendations drove more players than ads.
- [[2026-08-07 - I Got a ROBLOX GAME TEMPLATE And Turned It Around|I Got a ROBLOX GAME TEMPLATE And Turned It Around]] (61,654 views, 2026-08-07): Template turned fruit swing-obby, but 22% five-minute retention and a 21+ audience exposed onboarding gaps.
- [[2026-08-21 - Can I Make a VIRAL ROBLOX TYCOON GAME!|Can I Make a VIRAL ROBLOX TYCOON GAME?!]] (8,965 views, 2026-08-21): Restaurant tycoon devlog: party-size seating, cooking timers, and a 40% spawn cap for item variety.
- [[2026-09-12 - I Bought a Roblox Game... And GOT SCAMMED!!|I Bought a Roblox Game... And GOT SCAMMED?!?!]] (24,770 views, 2026-09-12): Scam warning: a 50% upfront payment to a vanished seller, then a banned account from one flagged image.
