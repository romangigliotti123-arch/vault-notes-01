---
title: DitchyDevelopments - How to make successful Roblox games
tags: [roblox, ditchydevelopments, playbook]
videos: 3
generated: 2026-10-29
credibility: insufficient
credibility_score: n/a
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# DitchyDevelopments - How to make successful Roblox games

New Roblox games need players before they need ads. Build a fun, bug-free, retentive game first, then borrow audiences from dev communities and small reviewers. The strongest method is regular devlog shorts that tell a development story, involve viewers in decisions, and then use that audience for playtesting and launch. Keep scope tight: a "small" hide-and-seek project grew into a 200-day build. Work at a pace you can sustain. Buy ads only after retention holds. The 40,000-visit no-ads result comes from the speaker's own game, so treat it as one data point.

**Style:** Personal-journey devlogger who frames a first game as a beginner's story. Distinctive for turning build logs into a community funnel and letting viewers shape features. Suits solo developers making a first game who can post short-form updates consistently and want honest warnings about feature creep, burnout, and rushed events.

## Playbook
1. **Pick a scoped core loop with built-in replay** [[game-ideas-and-genres]]: Choose a simple core mechanic, then add replayability so players don't just repeat it: round events (low gravity, infected mode), map voting, collectible power-ups. Hide-and-seek plus parkour grew from one idea (3Pa8QmFB_TE, O9fIqTik9ik). Write scope limits before building.
2. **Tune movement and cap speed before adding features** [[core-loops-and-game-design]]: Nerf overpowered mechanics and remove overlapping ones (a dash that carries further on second use and combo-able slide jumps felt broken). Cap max speed at 70 studs/sec so tracking and collision keep up with chained movement (O9fIqTik9ik).
3. **Make tag and hit detection reliable at speed** [[scripting-and-performance]]: Use sub-step position checks between frames so fast-moving players still register tags and hits. Test this specifically with chained, high-speed movement after the speed cap is set (O9fIqTik9ik).
4. **Add ongoing rewards and fix soft-locks** [[core-loops-and-game-design]]: Pay coins per tag and for surviving 30 seconds, on top of round win/loss rewards, to sustain progression. Fix map exits where players fall off and get stuck: add climbable spots and timed off-path penalties instead of allowing soft-locks.
5. **Build a personal asset pack** [[building-art-and-assets]]: Make your own asset pack (learning Blender for custom assets helped) instead of relying on the Toolbox, to keep maps original and visually consistent (O9fIqTik9ik).
6. **Post devlog shorts from day one** [[social-features-and-virality]]: Start short-form devlog content early, showing progress and the story of a beginner becoming a developer. This built the audience behind the speaker's ~40,000 visits (cfLbW2j2VLs). Stay consistent; balance building the game with building its community.
7. **Build community before launch** [[community-and-discord]]: Use Discord and viewer comments to involve people: let them name maps, suggest features, and improve mechanics, and implement some suggestions. Launch goes to people already following the journey, not strangers (cfLbW2j2VLs, O9fIqTik9ik).
8. **Run scheduled private and open playtests** [[playtesting-and-feedback]]: Hold private, scheduled testing sessions via Discord. Announce open-test days on YouTube and Discord before alpha. Expect testers to report faster than you fix; the first session turned up a couple of major and about 67 minor bugs (3Pa8QmFB_TE).
9. **Reach small reviewers and dev communities** [[social-features-and-virality]]: Share the game with dev Discords, feedback groups, and playtest exchanges. Approach small creators who review games in Shorts or Discord. Do not spam links or cold-DM creators. Quick reviews from good games can bring many players fast (cfLbW2j2VLs).
10. **Check retention before any paid ads** [[ads-and-sponsored-experiences]]: Only consider ads once gameplay and retention are solid. One speaker's ad test peaked at ~20 concurrent players and fell to near zero within an hour, on a game built in 24 hours (cfLbW2j2VLs).
11. **Run community map contests** [[community-and-discord]]: Host map submission contests via Discord and add submitted maps to the game to reward many creators at once. The 2026 contest awarded 500 Robux to each of 8 entrant maps (O9fIqTik9ik).
12. **Polish the lobby experience** [[updates-live-ops]]: Add music to the lobby, voting, and countdown screens so the game feels alive between matches. These are small QoL changes that shipped alongside freeze tag and map fixes (O9fIqTik9ik).
13. **Don't rush seasonal events** [[updates-live-ops]]: Seasonal events built under pressure can backfire. The rushed Halloween update with currency and shop got mixed feedback (3Pa8QmFB_TE). Ship smaller, planned events instead.
14. **Pace work sustainably** [[mindset-and-strategy]]: Burnout hit around day 50 at about 5 hours of sleep per night and 10-hour studio sessions, which was unsustainable (3Pa8QmFB_TE). Schedule breaks and set realistic daily hours.

## Key numbers
- 100 days from zero Lua experience to first playable (3Pa8QmFB_TE)
- Channel growth over 100 subscribers per day around week two (3Pa8QmFB_TE)
- First testing session: a couple of major bugs and about 67 smaller ones (3Pa8QmFB_TE)
- Obby built as a 24-hour challenge; race mode took 25 hours (3Pa8QmFB_TE)
- About 5 hours of sleep per night around day 50 during burnout (3Pa8QmFB_TE)
- Momentum speed cap: 70 studs/sec (O9fIqTik9ik)
- 200 days of development, still unfinished (O9fIqTik9ik)
- Playable WIP test game: 30,000+ visits (O9fIqTik9ik)
- 25,000+ Robux earned, mostly from donations (O9fIqTik9ik)
- 8 community map entries, 500 Robux each (O9fIqTik9ik)
- Ad test: ~20 peak concurrent players, near zero within 1 hour (cfLbW2j2VLs)
- First Roblox game without ads: over 40,000 visits, speaker's own game (cfLbW2j2VLs)

## Common mistakes
- Feature creep from short-form comment requests: adding an obby and race mode expanded scope fast; the speaker later said it probably wasn't a good idea (3Pa8QmFB_TE)
- Starting a 'small' project that grows into a 200+ day build with no scope limit (O9fIqTik9ik)
- Rushing a seasonal update under pressure; the Halloween currency and shop got mixed feedback (3Pa8QmFB_TE)
- Letting movement speed go uncapped, so tracking and collision cannot keep up with chained movement (O9fIqTik9ik)
- Leaving map exits where players fall off and get stuck (O9fIqTik9ik)
- Buying ads before gameplay and retention are solid; the test peaked at ~20 players and died within an hour (cfLbW2j2VLs)
- Relying on Toolbox assets, which makes maps less original and inconsistent in style (O9fIqTik9ik)
- Opening public testing without capacity to triage reports; testers reported bugs faster than they could be fixed (3Pa8QmFB_TE)
- Launching to strangers instead of an audience already following the devlog (cfLbW2j2VLs)
- Spamming links or cold-DMing creators instead of joining dev communities and playtest exchanges (cfLbW2j2VLs)

## Launch checklist
- [ ] Core loop is fun and replayable beyond one mechanic
- [ ] No major known bugs; minor bugs triaged
- [ ] Movement speed capped (70 studs/sec) and tested with chained movement
- [ ] Tag and hit checks use sub-step position checks
- [ ] Map exits reachable; no fall-off soft-locks
- [ ] Ongoing rewards in place (per-tag coins, survival coins)
- [ ] Lobby, voting, and countdown screens have music
- [ ] Private scheduled test sessions run via Discord
- [ ] Open-test days announced on YouTube and Discord before alpha
- [ ] Devlog shorts posted consistently and audience invited to test
- [ ] Dev Discords, feedback groups, and playtest exchanges lined up
- [ ] List of small Shorts and Discord reviewers prepared, approached politely
- [ ] Retention checked before any paid ads are considered
- [ ] No seasonal event rushed to a fixed date
- [ ] Community map contest or viewer-suggested features ready to showcase
- [ ] Asset pack consistent in style, not Toolbox-dependent
- [ ] Sleep and work hours sustainable
- [ ] Bug-report intake and fix capacity planned for tester surge

## How the advice changed over time
- Earlier devlogs (3Pa8QmFB_TE) took feature requests from short-form comments freely, expanding scope to an obby and race mode; the speaker later said this probably wasn't a good idea. Newer guidance is to scope feature requests deliberately.
- The 2026 devlog (O9fIqTik9ik) shifted focus from new modes to fixing core systems (movement overhaul, speed cap, tracking reliability) and planned ability and leveling systems.
- Newest guidance (cfLbW2j2VLs, 2026-06) says players and community come before ads, and devlog shorts are the main growth engine. Earlier videos mentioned community and public testing but did not address paid ads.

## Theme notes
- [[DitchyDevelopments - Retention|Retention]]
- [[DitchyDevelopments - Discovery & Algorithm|Discovery & Algorithm]]
- [[DitchyDevelopments - Game Ideas|Game Ideas]]
- [[DitchyDevelopments - Updates & Live Ops|Updates & Live Ops]]
- [[DitchyDevelopments - Studio & Scripting|Studio & Scripting]]
- [[DitchyDevelopments - Mindset & Process|Mindset & Process]]
- [[DitchyDevelopments - Games Mentioned]]
- [[DitchyDevelopments - Numbers & Benchmarks]]
- [[DitchyDevelopments - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-11-07 - I Spent 100 Days Making My First Roblox Game|I Spent 100 Days Making My First Roblox Game]] (74,032 views, 2025-11-07): 100-day devlog from zero Lua to first playable; covers feature creep, burnout, and a rushed Halloween update.
- [[2026-03-14 - I Spent 200 Days Working On My First Roblox Game|I Spent 200 Days Working On My First Roblox Game]] (42,042 views, 2026-03-14): 200-day hide-and-seek/parkour devlog: movement nerfs, 70 studs/sec cap, Discord map contest, unfinished build.
- [[2026-06-18 - How to ACTUALLY get Players in your ROBLOX Game in 2026|How to ACTUALLY get Players in your ROBLOX Game in]] (31,968 views, 2026-06-18): Get players before ads: build a retentive game, then borrow audiences via devlog shorts and small reviewers.
