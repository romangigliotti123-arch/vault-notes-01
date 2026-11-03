---
title: NotCumin - How to make successful Roblox games
tags: [roblox, notcumin, playbook]
videos: 12
generated: 2026-10-29
credibility: trusted
credibility_score: 7.9
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# NotCumin - How to make successful Roblox games

NotCumin's playbook is critique-driven: judge a Roblox game by whether its core loop has real mechanical depth, a fail state, and fair friction. Build readable, telegraphed combat, dense maps with fast travel, and in-game onboarding instead of fan wikis. Keep respawns short and monetisation fair: never paywall previously free rewards, and avoid FOMO aimed at children. Playtest with real players before launch, pitch creators with screenshots, a trailer and a playable link, and balance live updates against fixing onboarding. Most material is opinion, so treat the figures as examples.

**Style:** Opinionated critic-developer who reviews Roblox hits and flops through a design lens. Early videos are entertainment rants; later ones give concrete design lessons. Best for developers making RPG, action or hard-game projects who want a checklist of failure modes to avoid. Less useful for simulator growth or monetisation strategy.

## Playbook
1. **Pick a distinct idea, not a clone** [[game-ideas-and-genres]]: Collect-then-rebirth loops are easy to copy, so add a distinct mechanic or licensed IP with faithful movement (Sonic Speed Sim slopes, loops, homing attacks). Avoid one-button designs with nothing to master. (YmAwFbqUA0U, 2auVezIcNAE)
2. **Give the core loop depth and a fail state** [[core-loops-and-game-design]]: Add interacting systems and non-numeric challenges, not just a rising number. Include a fail state or challenge that raw stats cannot beat, or players only have patience to test. Check the core activity stays engaging for minutes. (YmAwFbqUA0U, E7bedfC8A10)
3. **Design around the core movement** [[genre-mechanics]]: Decide what movement is central and keep it fun from the start. Do not gut traversal with slow walking or stamina sprint. Scale PvE difficulty across stages so late content is not trivial. Build tall, reachable maps for movement-based games. (Z1tj1OPOEZg, jXogdTgtlXE)
4. **Build an interactive, in-game tutorial** [[first-session-onboarding]]: Let players practise each control and mechanic, with breadcrumb hints and an in-game codex. Explain every UI colour or signal. Avoid darkened-screen arrow tours and do not assume fans will explain the game on a wiki. (cbOZKwPmmko, hQpC_UHxJDU)
5. **Make combat readable and responsive** [[combat-and-gameplay-systems]]: Telegraph enemy attacks so players learn dodge timing. Make boss fights last more than a minute or two, with attacks matching their fiction. Add input buffering. Give dodge dashes i-frames tied to stamina. Avoid bosses that kill fast while the player deals tickle damage. (2auVezIcNAE, hQpC_UHxJDU)
6. **Keep hitboxes and timing honest** [[scripting-and-performance]]: End enemy hitboxes when the animation ends, since lingering hitboxes feel amateur and unfair. Account for server-side timing windows so valid parries and dodges register, otherwise players see failures with no reason. (hQpC_UHxJDU)
7. **Build dense maps with fast travel** [[building-and-level-design]]: Avoid long empty travel between objectives, ghost doors that do not match collision, and fog that hides the map. Place fast-travel before every major boss and across large maps. Guide players to key progression items rather than hiding them in random chests. (hQpC_UHxJDU, Z1tj1OPOEZg, jXogdTgtlXE)
8. **Design matchmaking for group content** [[matchmaking-and-teleport]]: Offer level-bracketed lobbies, a quick-queue that teleports the group once full, and player-created rooms with chosen dungeon and difficulty. Per-mission queues stop runs collapsing when others leave. Keep server population healthy; two servers per region means high ping. (kjLtxvB_iyk, Z1tj1OPOEZg)
9. **Monetise without paywalling free content** [[monetisation-gamepasses]]: Never move previously free rewards behind a paywall. Let players reset skill points for free. Avoid time-gated unlocks and FOMO tactics, especially where children play. The creator treats these as ethical as well as design issues. (2auVezIcNAE, Jf2RvsWMPes, 66n0P2NtBoQ)
10. **Playtest with real players before release** [[playtesting-and-feedback]]: Test combat, multiplayer and parries with real players before launch. Broken hitboxes, multiplayer flow and parries suggest the game was never tested. Playtesting is the creator's recurring fix for low-quality launches. (hQpC_UHxJDU, ROo_Xpms4ok)
11. **Pitch creators properly** [[influencer-and-creator-marketing]]: When contacting YouTubers, include screenshots, a trailer and a direct playable link in the first message. Do not send a bare play-my-game DM. Pitch a finished-enough build, since underbaked alphas get reviewed harshly. (ROo_Xpms4ok)
12. **Hook players in the first five hours** [[retention-d1-d7]]: The creator says he gives a game about five hours before judging it. Early movement and the core activity must already feel good; do not rely on a promise that it gets better later. Make respawns short so players keep playing. (hQpC_UHxJDU, E7bedfC8A10, Z1tj1OPOEZg)
13. **Judge discovery by real play** [[discovery-algorithm]]: Top-rated and front-page charts favour quick-return and inflated-like games. Treat like counts skeptically and judge your game by genuine play, not chart position. The creator wants better discovery methods but names few specifics. (Jf2RvsWMPes, hQpC_UHxJDU)
14. **Balance updates with onboarding fixes** [[updates-live-ops]]: Devs usually favour new content, which leaves newcomers lost. Spend some updates on tutorials and onboarding. Show a Coming Soon sign for unfinished features instead of an NPC error. Avoid off-platform code gates, which force players away. (cbOZKwPmmko, kjLtxvB_iyk, 2auVezIcNAE)

## Key numbers
- Respawn wait after death: up to ~10 minutes in AOT Freedom War (Z1tj1OPOEZg, jXogdTgtlXE)
- Respawn benchmark: a few seconds in shooters, about 1 minute max in MOBAs (jXogdTgtlXE)
- Campaign required 15 players vs 4 max for most PvE games (jXogdTgtlXE)
- Servers per region: 2 at most, forcing high-ping servers (Z1tj1OPOEZg)
- Blade strikes before reload: 4 (Z1tj1OPOEZg)
- Hook window: about 5 hours per game before judgement (hQpC_UHxJDU)
- Dungeon Quest Reborn: max 40 players per server, 2 hotbar abilities, 5 difficulty tiers per dungeon (kjLtxvB_iyk)
- Lobby level brackets proposed: 1+, 30+ (existing lobbies 100+ too broad) (kjLtxvB_iyk)
- Free UGC items gated behind about 100 hours of play, per speaker (Jf2RvsWMPes)
- Grow a Garden ~1 million concurrent, creator estimate, unverified (E7bedfC8A10)
- Starting funds in Grow a Garden: 20 cents, 7 Robux (E7bedfC8A10)
- Fandom wiki ads: half-screen video, one described as 40 minutes long (cbOZKwPmmko)
- Developer underpayment cited: about $20 at best (hQpC_UHxJDU)
- The Horde Comes: 4 maps, 2 artifacts of each needed, impossible to carry solo (ROo_Xpms4ok)
- Roblox annual revenue $3.6 billion, speaker's figure, unverified (66n0P2NtBoQ)

## Common mistakes
- Making the loop a single rising number with no fail state or non-numeric challenge (YmAwFbqUA0U)
- Permadeath with long respawn waits so players spend sessions spectating (Z1tj1OPOEZg, jXogdTgtlXE)
- Interconnected stages with dead travel time, ghost doors and slow walking (Z1tj1OPOEZg)
- Locking core movement such as an impulse or boost behind skill points (Z1tj1OPOEZg)
- Paywalling previously free rewards, such as tower chests (2auVezIcNAE)
- Level-locked grinds repeating the same kill-X quest template (2auVezIcNAE, kjLtxvB_iyk)
- Relying on fan wikis, which carry ad overload and may be outdated (cbOZKwPmmko)
- Unreadable boss telegraphs and lingering hitboxes that hit after attacks end (hQpC_UHxJDU)
- Hiding key progression items in random chests (hQpC_UHxJDU)
- Padding playtime to earn more Premium payouts, which the creator criticises (66n0P2NtBoQ)

## Launch checklist
- [ ] Core loop has a fail state or a challenge that raw stats cannot beat
- [ ] Core movement feels good in the first minutes, with no default-locked boost
- [ ] Every enemy attack has a visible telegraph
- [ ] Enemy hitboxes end with their animation
- [ ] Parries and dodges have server-side timing windows that register valid inputs
- [ ] Input buffering on attacks and blocks
- [ ] Interactive tutorial covers every control and mechanic
- [ ] In-game codex explains UI colours, signals and systems
- [ ] Fast-travel point before every boss and across large maps
- [ ] No ghost doors, no fog hiding the map, no long empty travel
- [ ] Respawn timers: a few seconds in shooters, 1 minute max in MOBAs
- [ ] Key progression items are signposted, not hidden in random chests
- [ ] Level-bracketed lobbies, player-created rooms and a quick-queue for group content
- [ ] Healthy server population, not two servers per region
- [ ] Playtested with real players, including multiplayer and parries
- [ ] Creator pitch kit ready: screenshots, trailer and direct playable link
- [ ] Free rewards are not paywalled; skill reset is free; no off-platform code gates
- [ ] Early game hooks players within their first five hours

## How the advice changed over time
- Apr to Jun 2025 videos were mostly entertainment rants with little actionable advice (YmAwFbqUA0U, E7bedfC8A10); concrete design guidance appears from Nov 2025 onward (cbOZKwPmmko, hQpC_UHxJDU).
- Monetisation criticism moved from specific gamepasses (2auVezIcNAE, Jf2RvsWMPes) to calling Roblox monetisation unethical and urging regulation (66n0P2NtBoQ).
- Matchmaking advice became specific only in the newest video: level-bracketed lobbies and a quick-queue are proposed (kjLtxvB_iyk), where earlier reviews only named the problem.
- No direct reversals found; later advice on telegraphing, fast travel and playtesting (hQpC_UHxJDU) is consistent with earlier critiques.

## Theme notes
- [[NotCumin - Retention|Retention]]
- [[NotCumin - Monetisation|Monetisation]]
- [[NotCumin - Discovery & Algorithm|Discovery & Algorithm]]
- [[NotCumin - Game Ideas|Game Ideas]]
- [[NotCumin - Thumbnails & Icons|Thumbnails & Icons]]
- [[NotCumin - Updates & Live Ops|Updates & Live Ops]]
- [[NotCumin - Studio & Scripting|Studio & Scripting]]
- [[NotCumin - Mindset & Process|Mindset & Process]]
- [[NotCumin - Games Mentioned]]
- [[NotCumin - Numbers & Benchmarks]]
- [[NotCumin - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-04-06 - Simulators are a PLAGUE on Roblox|Simulators are a PLAGUE on Roblox]] (54,009 views, 2025-04-06): Simulators feel hollow when a static, number-only loop has no fail state or real depth.
- [[2025-05-11 - The Sad State of Modern Roblox RPGs|The Sad State of Modern Roblox RPGs...]] (482,353 views, 2025-05-11): Many Roblox RPGs feel samey: repetitive quests, paywalls and unreadable combat.
- [[2025-05-24 - How is THIS the biggest game on Roblox|How is THIS the biggest game on Roblox?]] (84,678 views, 2025-05-24): Grow a Garden's slow seed and crop waits made the creator lose interest within minutes.
- [[2025-06-08 - When Roblox devs don't know the difference between challenging and bad|When Roblox devs don't know the difference between]] (186,615 views, 2025-06-08): AOT Freedom War confuses challenge with bad design: permadeath waits, dead travel, weak onboarding.
- [[2025-07-31 - No, Get Good doesn't excuse bad Roblox games|No, "Get Good" doesn't excuse bad Roblox games.]] (345,515 views, 2025-07-31): Hard games still need fair failure, sane respawns, scaling difficulty and a real tutorial.
- [[2025-09-06 - The Roblox Front Page is a Joke|The Roblox Front Page is a Joke.]] (300,047 views, 2025-09-06): Front-page charts reward quick-return, low-effort monetised games over well-made ones.
- [[2025-11-05 - Roblox monetization needs to stop|Roblox monetization needs to stop.]] (26,553 views, 2025-11-05): Robux opacity, FOMO and child-targeted pressure make monetisation unethical, the creator argues.
- [[2025-11-23 - Roblox has a Wiki Game problem|Roblox has a "Wiki Game" problem...]] (89,176 views, 2025-11-23): Wiki-dependent RPGs fail new players; teach in-game instead of relying on Fandom.
- [[2025-12-23 - Roblox RPGs Are In a Rough Patch|Roblox RPGs Are In a Rough Patch...]] (163,217 views, 2025-12-23): RPGs need direction, telegraphing, fast travel and playtesting, and must hook within five hours.
- [[2026-02-07 - This dev sent me their Roblox game, but|This dev sent me their Roblox game, but...]] (23,309 views, 2026-02-07): The Horde Comes is underbaked; the review also covers how to pitch YouTubers properly.
- [[2026-06-27 - We Need to Talk About Game Prices|We Need to Talk About Game Prices...]] (8,796 views, 2026-06-27): Off-topic rant on rising console and game prices; contains no Roblox development advice.
- [[2026-09-13 - Nostalgia Doesn't Make a Good Game|Nostalgia Doesn't Make a Good Game.]] (191,211 views, 2026-09-13): Dungeon Quest Reborn keeps its dungeon loop but needs better lobbies, less RNG and less level padding.
