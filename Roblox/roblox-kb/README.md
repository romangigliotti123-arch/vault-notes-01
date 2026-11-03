---
title: Roblox knowledge base (README)
tags: [roblox, knowledge-base, index]
---

# Roblox game-making knowledge base

Built 2026-11-01 from 2573 sources (YouTube videos plus Roblox Creator Docs and DevForum pages) by 133 creators/channels (local transcripts, compressed, extracted by a small model, merged by Sonnet). Every claim links to the video and timestamp. Official Roblox sessions are marked [official]; indie revenue/CCU claims are self-reported and unverified. Advice is dated: Roblox's algorithm, payouts and ad tools change, so prefer newer sources when they conflict, and treat revenue figures as creator-stated or third-party estimates.

## How to use with an agent
1. Give the agent this README plus [[master-playbook]] (overview, decision rules, prompt starters).
2. Add the topic files for the task from the table below (each file is self-contained: rules, checklist, numbers, disagreements, date context, agent instructions, appendix of every raw tip).
3. Tell the agent to cite the linked timestamps and to flag advice older than ~12 months.
4. For platform mechanics (algorithm signals, payouts, pricing tools, analytics) trust official sources first: Roblox Creator Docs (sibling folder `docs`), Roblox and Roblox Creators sessions. Indie revenue/CCU figures are self-reported.

## Which files for which task

| Task | Give the agent |
|---|---|
| Come up with / evaluate a game idea | [[game-ideas-and-genres]], [[trend-research-and-validation]], [[core-loops-and-game-design]], the matching case studies (list below), [[common-mistakes]] |
| Plan the first minutes and retention | [[first-session-onboarding]], [[retention-d1-d7]], [[core-loops-and-game-design]], [[social-features-and-virality]] |
| Design monetisation and pricing | [[monetisation-gamepasses]], [[monetisation-devproducts]], [[monetisation-other]], [[pricing]], [[analytics-metrics]] |
| Run ads / get players | [[ads-and-sponsored-experiences]], [[discovery-algorithm]], [[thumbnails-icons]], [[titles-descriptions]], [[social-features-and-virality]] |
| Make thumbnails, icons, title and description | [[thumbnails-icons]], [[titles-descriptions]], [[discovery-algorithm]] |
| Launch and keep a live game alive | [[updates-live-ops]], [[analytics-metrics]], [[community-and-discord]], [[roblox-platform-changes]], [[retention-d1-d7]] |
| Build the game (scripting, art, AI tools) | [[scripting-and-performance]], [[building-art-and-assets]], [[ai-and-tools]], [[development-process-and-speed]], [[playtesting-and-feedback]] |
| Team, budget, business | [[team-and-budget]], [[business-and-payouts]], [[mindset-and-strategy]] |
| Avoid known pitfalls | [[common-mistakes]], [[mindset-and-strategy]] |
| Write Luau code and structure a project | [[luau-language-and-types]], [[code-architecture-and-frameworks]], [[scripting-and-performance]], [[version-control-and-tooling]] |
| Networking, remotes and security | [[client-server-and-remotes]], [[anti-exploit-and-security]], [[data-persistence]] |
| Save player data and scale servers | [[data-persistence]], [[matchmaking-and-teleport]], [[optimization-and-streaming]] |
| Gameplay systems, combat, NPCs, physics | [[combat-and-gameplay-systems]], [[physics-pathfinding-and-npc-ai]], [[genre-mechanics]], [[player-psychology-and-game-feel]] |
| Build worlds, art, animation, VFX, sound | [[building-and-level-design]], [[3d-modeling-rigging-and-animation]], [[vfx-and-particles]], [[sound-and-music]] |
| UI/UX and cross-platform input | [[ui-ux-design]], [[cross-platform-and-console]], [[first-session-onboarding]] |
| Optimise performance and debug | [[optimization-and-streaming]], [[testing-debugging-and-qa]], [[scripting-and-performance]] |
| Marketing: trailers, TikTok, influencers, community | [[trailers-and-video-marketing]], [[influencer-and-creator-marketing]], [[community-and-discord]], [[social-features-and-virality]] |
| Events, seasonal content and A/B tests | [[events-and-seasonal-content]], [[updates-live-ops]], [[ab-testing-and-experiments]], [[analytics-metrics]] |
| UGC, avatar items and brand deals | [[ugc-and-avatar-economy]], [[brand-deals-and-ip-licensing]], [[ads-and-sponsored-experiences]] |
| Localisation, ToS, age ratings, moderation | [[localization-and-international]], [[age-ratings-moderation-and-tos]], [[roblox-platform-changes]] |
| Studio, hiring, contracts, funding | [[studio-business-funding-and-publishing]], [[team-and-budget]], [[business-and-payouts]] |

## Topic files

- [[game-ideas-and-genres]] (Game Ideas): which genres/ideas to make, what makes an idea good, genre saturation.
- [[trend-research-and-validation]] (Game Ideas): finding trending games early, tools like RoTrends, validating demand/competition before building.
- [[core-loops-and-game-design]] (Game Ideas): core loop, progression systems, game feel, what makes gameplay sticky.
- [[first-session-onboarding]] (Retention): first 30 seconds, tutorials, new-player experience, early conversion.
- [[retention-d1-d7]] (Retention): day-1/day-7 retention, session length, daily rewards, hooks that bring players back.
- [[monetisation-gamepasses]] (Monetisation): gamepasses: which to sell, design, placement.
- [[monetisation-devproducts]] (Monetisation): developer products, consumables, offers, limited-time deals.
- [[monetisation-other]] (Monetisation): Premium payouts, subscriptions, UGC/items, cosmetics, revenue models in general.
- [[pricing]] (Monetisation): Robux price points, discounts, anchoring, conversion rate vs price.
- [[ads-and-sponsored-experiences]] (Discovery & Algorithm): Roblox sponsored ads, ad spend/ROAS, user acquisition, off-platform promotion.
- [[thumbnails-icons]] (Thumbnails & Icons): thumbnails, icons, CTR, A/B testing creatives.
- [[titles-descriptions]] (Thumbnails & Icons): game titles, descriptions, naming, SEO/keywords on Roblox.
- [[discovery-algorithm]] (Discovery & Algorithm): Roblox recommendation algorithm, QPTR/CTR/engagement signals, getting recommended.
- [[updates-live-ops]] (Updates & Live Ops): update cadence, events, seasonal content, keeping a live game alive.
- [[social-features-and-virality]] (Retention): multiplayer/social hooks, friends, sharing, going viral, creator/influencer promotion.
- [[analytics-metrics]] (Mindset & Process): which metrics to track, dashboards, benchmarks, reading the data.
- [[playtesting-and-feedback]] (Mindset & Process): testing with players, feedback loops, iteration, soft-launch.
- [[scripting-and-performance]] (Studio & Scripting): Luau scripting practice, architecture, performance, mobile optimisation, security/exploits.
- [[building-art-and-assets]] (Studio & Scripting): building, UI, art, animation, audio, asset pipelines, UGC assets.
- [[ai-and-tools]] (Studio & Scripting): AI-assisted development (vibe coding), Studio plugins, external tools.
- [[team-and-budget]] (Mindset & Process): hiring, outsourcing, revenue share, contracts, budgets, working solo.
- [[development-process-and-speed]] (Mindset & Process): how to build fast, scope, MVP, release cadence, workflow, quitting/pivoting.
- [[community-and-discord]] (Retention): community building, Discord, groups, social following, player feedback channels.
- [[business-and-payouts]] (Monetisation): DevEx/cash-out, taxes, selling games, studio economics, long-term business.
- [[common-mistakes]] (Mindset & Process): mistakes, traps and misconceptions explicitly called out.
- [[mindset-and-strategy]] (Mindset & Process): attitude, consistency, portfolio approach, expectations, big-picture strategy.
- [[roblox-platform-changes]] (Discovery & Algorithm): platform policy/feature changes (e.g. algorithm updates, new payout rules) and their effects.
- [[luau-language-and-types]] (Studio & Scripting): Luau language features, strict typing, idioms, coroutines/task library, code-level performance and style.
- [[code-architecture-and-frameworks]] (Studio & Scripting): OOP, modules, services, Knit/Promise/ECS/signals, project structure, reusable systems, clean code.
- [[client-server-and-remotes]] (Studio & Scripting): client/server model, replication, RemoteEvents/Functions, network ownership, latency, server authority patterns.
- [[anti-exploit-and-security]] (Studio & Scripting): exploiters, input validation, server-side checks, anti-cheat, securing remotes and economy, abuse prevention.
- [[data-persistence]] (Studio & Scripting): DataStores, ProfileStore/ProfileService, session locking, MemoryStore, MessagingService, saving/loading, migrations.
- [[matchmaking-and-teleport]] (Studio & Scripting): TeleportService, matchmaking, reserved/private servers, server browsers, cross-place travel, lobbies.
- [[physics-pathfinding-and-npc-ai]] (Studio & Scripting): physics and constraints, vehicles, PathfindingService, NPC behaviour, enemy AI, behaviour trees.
- [[combat-and-gameplay-systems]] (Studio & Scripting): combat, weapons, abilities, hitboxes, inventory, shops, quests, leveling and other gameplay systems implementation.
- [[genre-mechanics]] (Game Ideas): genre-specific design/mechanics: tycoon, simulator, obby, horror, RPG, FPS, tower defense, roleplay, fighting, racing.
- [[building-and-level-design]] (Studio & Scripting): map and level design, terrain, lighting, atmosphere, environment art workflow, world building.
- [[3d-modeling-rigging-and-animation]] (Studio & Scripting): Blender and modelling for Roblox, meshes/textures, rigging, animation, avatars, import pipelines.
- [[vfx-and-particles]] (Studio & Scripting): particle effects, beams/trails, shaders-like tricks, tweening, post-processing, polish and juice visuals.
- [[ui-ux-design]] (Studio & Scripting): UI/UX design, mobile/console/PC layouts, HUD, menus, accessibility, UI scripting and animation.
- [[sound-and-music]] (Studio & Scripting): sound design, music, audio implementation, mixing, licensing, audio assets.
- [[optimization-and-streaming]] (Studio & Scripting): memory, instance streaming, rendering cost, mobile and low-end performance, profiling, lag diagnosis.
- [[testing-debugging-and-qa]] (Mindset & Process): debugging tools, logging, unit/integration testing, QA, bug triage, release checks.
- [[version-control-and-tooling]] (Studio & Scripting): Rojo, Wally, Argon, Git, VS Code/Luau LSP, Open Cloud, plugins, build pipelines, external tooling.
- [[trailers-and-video-marketing]] (Discovery & Algorithm): trailers, TikTok/Shorts, gameplay clips, social media content, video production for games.
- [[influencer-and-creator-marketing]] (Discovery & Algorithm): YouTuber/influencer outreach, creator programs, sponsored creator content, affiliate/Video Stars, collabs.
- [[ugc-and-avatar-economy]] (Monetisation): UGC items, avatar marketplace, Creator Store, limited items, avatar economy, selling assets.
- [[localization-and-international]] (Discovery & Algorithm): localization, translation, regional pricing and markets, international growth.
- [[age-ratings-moderation-and-tos]] (Mindset & Process): Roblox ToS, community standards, moderation, age ratings and age checks, safety, compliance, copyright.
- [[studio-business-funding-and-publishing]] (Mindset & Process): studio structure, hiring, contracts, revenue splits, group funds, funding and investors, publishers, growing a company.
- [[brand-deals-and-ip-licensing]] (Monetisation): brand partnerships, IP licensing, licensed games, sponsored experiences for brands, immersive ads.
- [[player-psychology-and-game-feel]] (Retention): player motivation, psychology, rewards, game feel and juice, difficulty, flow, behavioural design.
- [[ab-testing-and-experiments]] (Mindset & Process): A/B testing, Roblox Experiments/Configs, hypothesis-driven iteration, statistics for tests.
- [[events-and-seasonal-content]] (Updates & Live Ops): live events, seasonal/holiday content, limited-time modes, collabs and event calendars.
- [[cross-platform-and-console]] (Studio & Scripting): console, VR, mobile and cross-platform support, input handling, platform-specific design.

## Case studies (games)

- [[case-studies-dont-splash]]: DONT SPLASH (Obby / platformer (eerie runner))
- [[case-studies-island-jump]]: Island Jump (3D platformer (official tutorial project))
- [[case-studies-racing-game-unnamed]]: Racing game (unnamed, well-known-dev and background examples) (Racing)
- [[case-studies-racing-soccer-laser-tag-templates]]: Racing, Soccer, Laser Tag template games (Template/sample games (multi-genre))
- [[case-studies-island-royale]]: Island Royale (Battle royale)
- [[case-studies-plane-crazy]]: Plane Crazy (Plane / flight game (genre inferred from title))
- [[case-studies-midnight-racing-tokyo]]: Midnight Racing: Tokyo (Racing)
- [[case-studies-grow-a-garden]]: Grow a Garden (Farming / idle simulator)
- [[case-studies-adopt-me]]: Adopt Me! (Pet collection / life roleplay)
- [[case-studies-steal-a-brainrot]]: Steal a Brainrot (Tycoon / steal-and-defend PvP simulator)
- [[case-studies-jailbreak]]: Jailbreak (Action roleplay / cops and robbers)
- [[case-studies-brookhaven]]: Brookhaven (Kids' roleplay life sim)
- [[case-studies-doors]]: DOORS (Horror / procedural survival)
- [[case-studies-99-nights-in-the-forest]]: 99 Nights in the Forest (Horror survival)
- [[case-studies-rivals]]: Rivals (Competitive FPS (PvP))
- [[case-studies-steal-an-egg]]: Steal An Egg (Simulator with PvP stealing)
- [[case-studies-blox-fruits]]: Blox Fruits (Anime RPG / grinder)
- [[case-studies-arsenal]]: Arsenal (Competitive FPS)
- [[case-studies-dead-rails]]: Dead Rails (Train survival)
- [[case-studies-bloxburg]]: Bloxburg (Life sim / house-building roleplay)
- [[case-studies-piggy]]: Piggy (Horror escape / chase)
- [[case-studies-animal-hospital]]: Animal Hospital (Co-op horror / night-shift survival)
- [[case-studies-driving-empire]]: Driving Empire (Driving / open-world)
- [[case-studies-pet-simulator-x]]: Pet Simulator X (Simulator / collection)
- [[case-studies-mystery-of-duvall-drive|case-studies-the-mystery-of-duvall-drive]]: The Mystery of Duvall Drive (Horror demo / technical showcase)
- [[case-studies-phantom-forces]]: Phantom Forces (Realistic FPS)
- [[case-studies-dragon-adventures]]: Dragon Adventures (Open-world dragon / flight)
- [[case-studies-natural-disaster-survival]]: Natural Disaster Survival (Party survival)
- [[case-studies-pet-simulator]]: Pet Simulator (Simulator (pet collecting, eggs, currency))
- [[case-studies-pet-simulator-99]]: Pet Simulator 99 (Simulator (pets, eggs, rebirths, trading))
- [[case-studies-beyond-the-dark]]: Beyond the Dark (Sci-fi environment showcase (space station))
- [[case-studies-fish]]: Fish (Fishing and collection)
- [[case-studies-world-zero]]: World Zero (Open-world MMO RPG)
- [[case-studies-creatures-of-sonaria]]: Creatures of Sonaria (Creature survival and battling)
- case-studies-fortnite: Fortnite (Battle royale (reference, not a Roblox game))
- [[case-studies-murder-mystery-2]]: Murder Mystery 2 (Social deduction (round-based hidden role))
- [[case-studies-bed-wars]]: Bed Wars (Competitive team PvP)
- [[case-studies-please-donate]]: Please Donate (Donation-based social game)
- [[case-studies-tower-defense-simulator]]: Tower Defense Simulator (Tower defense)
- [[case-studies-escape-tsunami-for-brainrots]]: Escape Tsunami For Brainrots! (Survival and idle hybrid)
- [[case-studies-galactic-speedway]]: Galactic Speedway (Racing (educational course project))
- [[case-studies-super-striker-league]]: Super Striker League (Sports (soccer))
- case-studies-minecraft: Minecraft (Sandbox (reference, not a Roblox game))
- [[case-studies-brookhaven|case-studies-brookhaven-rp]]: Brookhaven RP (Social roleplay sandbox)
- [[case-studies-fish-it]]: Fish It (Fishing simulator (luck-based, idle-friendly))
- [[case-studies-front-lines]]: Front Lines (Team FPS shooter (realistic vs arcade))
- [[case-studies-grow-a-garden|case-studies-grow-a-garden-2]]: Grow A Garden 2 (Farming/garden simulator with PvP elements)
- [[case-studies-sell-lemons]]: Sell Lemons (Idle clicker/tycoon)
- [[case-studies-dress-to-impress]]: Dress to Impress (Social dress-up and voting-round game)
- [[case-studies-jujutsu-shenanigans]]: Jujutsu Shenanigans (Anime battle royale / PvP action)
- [[case-studies-tower-of-hell]]: Tower of Hell (Obby / platformer)
- [[case-studies-deepwoken]]: Deepwoken (Dark-fantasy RPG / skill-based PvP combat)
- [[case-studies-hack-a-business]]: Hack a Business (Business/tycoon sim (Tizzy's own game))
- [[case-studies-bee-swarm-simulator]]: Bee Swarm Simulator (Collect-and-upgrade simulator)
- [[case-studies-blade-ball]]: Blade Ball (Reaction-based sword combat)
- [[case-studies-mansion-of-wonder]]: Mansion of Wonder (Roblox Education template / tutorial game)
- case-studies-candy-crush: Candy Crush (King) (Mobile match-three (not a Roblox experience; external marketing benchmark))
- [[case-studies-blue-lock-rivals]]: Blue Lock Rivals (Licensed anime sports PvP)
- [[case-studies-piggy-intercity]]: Piggy Intercity (Open-world multiplayer RPG)
- [[case-studies-plant]]: Plant (Farming tycoon / microgame (official reference))
- [[case-studies-rainbow-friends]]: Rainbow Friends (Chapter-based Roblox experience)
- [[case-studies-the-forge]]: The Forge (Mining and forging / idle-crafting)
- [[case-studies-bloxburg|case-studies-welcome-to-bloxburg]]: Welcome to Bloxburg (House-building and economy simulation)
- [[case-studies-slap-battles]]: Slap Battles (Physics combat / slap arena)
- [[case-studies-island-of-move]]: Island of Move (Animation course sample (official))
- [[case-studies-meep-city]]: Meep City (Social hangout Roblox game)
- case-studies-overwatch: Overwatch (Non-Roblox reference game (team shooter))
- [[case-studies-pets-go]]: Pets Go! (Pet-collection simulator with egg RNG)
- [[case-studies-plus-one-speed-keyboard-escape]]: +1 Speed Keyboard Escape (Short-session party / casual)
- [[case-studies-build-a-base-and-steal]]: Build a Base and Steal (PvP build-and-steal)
- [[case-studies-evade]]: Evade (Nextbot-inspired Roblox game)
- [[case-studies-finish-the-word]]: Finish The Word (Word-chain puzzle)
- [[case-studies-grow-a-garden|case-studies-grow-garden]]: Grow Garden (Growing / garden simulator)
- case-studies-lua-learning: Lua Learning (Educational / in-experience coding tutorial)
- [[case-studies-obby|case-studies-obby-generic]]: Obby (generic) (Obstacle course / platformer)
- [[case-studies-panic-button]]: Panic Button (Casual mobile action (genre not specified in notes))
- [[case-studies-spin-or-die]]: Spin or Die (Party elimination (bottle-spin, last player standing))
- [[case-studies-spongebob-tower-defense]]: Spongebob Tower Defense (Tower defense with gacha and live-ops monetisation (licensed IP))
- [[case-studies-vesteria]]: Vesteria (Fantasy MMORPG)
- [[case-studies-violence-district]]: Violence District (Asymmetrical survival horror (1 vs all))
- [[case-studies-winds-of-fortune]]: Winds of Fortune (Combat RPG (inferred from mentions))
- [[case-studies-work-at-a-pizza-place]]: Work at a Pizza Place (Open-ended roleplay (job simulator))
- case-studies-clash-of-clans: Clash of Clans (Mobile strategy (non-Roblox reference))
- [[case-studies-pressure]]: Pressure (Horror (randomised rooms))
- [[case-studies-robloxian-high-school]]: Robloxian High School (Social life sim / roleplay)
- case-studies-team-fortress-2: Team Fortress 2 (Class-based team shooter)
- [[case-studies-clean-all-the-leaves]]: Clean All the Leaves (Chore simulator)
- [[case-studies-dungeon-quest]]: Dungeon Quest (Co-op dungeon crawler)
- [[case-studies-farmer-die]]: Farmer Die (Survival (co-op), inferred from Alien Ranch-style loop)
- [[case-studies-fisch]]: Fisch (Fishing game (Roblox))
- [[case-studies-griffins-destiny]]: Griffin's Destiny (Animal roleplay (free-to-play))
- [[case-studies-rb-battles]]: RB Battles (Community mini-game tournament (YouTuber event))
- [[case-studies-rebirth-speed-run]]: Rebirth Speed Run (Speedrun / rebirth simulator)
- [[case-studies-simulator-plugin-built]]: Simulator (plugin-built, 12-hour build) (Simulator)
- [[case-studies-simulator-genre-notes]]: Simulator genre notes (generic references) (Simulator (genre-level, not a single game))
- [[case-studies-stepford-county-railway]]: Stepford County Railway (Railway simulation)
- [[case-studies-teddy]]: Teddy (Horror escape game (inferred from scary cutscenes and escape routes))
- case-studies-brawl-stars: Brawl Stars (Competitive multiplayer with collection and loot boxes (monetisation reference, not a Roblox game))
- [[case-studies-kick-a-lucky-block]]: Kick a Lucky Block (Escape-tsunami loop with kick mechanic and social trading)
- [[case-studies-laser-tag-sample-game]]: Laser Tag sample game (Roblox official) (Team FPS tutorial sample)
- [[case-studies-squishmallows]]: Squishmallows (Collection and combination game (Roblox Creator Docs example))
- [[case-studies-ttk]]: TTK (Tactical shooter)
- [[case-studies-catalog-avatar-creator]]: Catalog Avatar Creator (Avatar try-on utility)
- case-studies-apex-legends: Apex Legends (Battle royale (monetisation and pitch reference, not a Roblox game))
- [[case-studies-big-games]]: Big Games (Game group / publisher brand)
- [[case-studies-boxing-stars]]: Boxing Stars (Boxing simulator (training sim))
- [[case-studies-concrete-cleaning]]: Concrete Cleaning (Cleaning simulator)
- [[case-studies-defend-your-brain-rot]]: Defend Your Brain Rot (Defense game (brainrot meme theme))
- [[case-studies-defend-the-village]]: Defend the Village (Zombie defense (tower-defense-style with classes))
- case-studies-fifa-super-soccer: FIFA Super Soccer (Sports (football))
- [[case-studies-plus-one-speed-keyboard-escape|case-studies-keyboard-escape]]: Keyboard Escape (Escape game)
- [[case-studies-ride-storm]]: Ride Storm (Social motorbike roleplay)
- [[case-studies-roblox-high-school-2]]: Roblox High School 2 (Social roleplay (high school))
- [[case-studies-store-simulator]]: Store Simulator (Tycoon / simulator)
- [[case-studies-sussy-imposter-land]]: Sussy Imposter Land (Meme / social-deduction themed)
- [[case-studies-swordburst-3]]: Swordburst 3 (Action RPG / open world)
- [[case-studies-ultimate-football]]: Ultimate Football (Sports (American football))
- [[case-studies-3008]]: 3008 (Horror)
- [[case-studies-alien-ranch]]: Alien Ranch (Farming / creature sim)
- [[case-studies-botclash-simulator]]: BotClash Simulator (Battle/simulator UI (Roblox Creator Docs example))
- [[case-studies-defend-your-brain-rot|case-studies-brain-rot]]: Brain Rot (trend) (Viral meme-driven trend; Roblox games inspired by it)
- [[case-studies-clipit]]: Clipit (Social clip-sharing platform / feed-style game)
- [[case-studies-forsaken]]: Forsaken (Externally promoted Roblox game (genre not stated))
- [[case-studies-freeze-tag]]: Freeze Tag (Rescue-tag / starter game)
- [[case-studies-gold-rush]]: Gold Rush (Official Roblox sample game (tutorial))
- [[case-studies-laser-tag]]: Laser Tag (Team shooter / sample game)
- [[case-studies-livetopia]]: Livetopia (Open-world life/roleplay playground)
- [[case-studies-mad-city]]: Mad City (Cop roleplay / prison-escape hybrid)
- [[case-studies-miners-haven]]: Miners Haven (Tycoon / mining)
- [[case-studies-mini-war]]: Mini War (Multiplayer strategy)
- [[case-studies-mining-simulator]]: Mining Simulator (Simulator / mining)
- [[case-studies-ninja-challenge]]: Ninja Challenge (Obstacle / challenge game)
- [[case-studies-ocean-conservation-game]]: Ocean Conservation Game (Educational / immersive learning)
- [[case-studies-oil-empire]]: Oil Empire (Tycoon / resource-stealing)
- [[case-studies-island-jump|case-studies-island-jump-final]]: Island Jump - Final (Platformer (jumping, sample game))
- [[case-studies-island-jump|case-studies-island-jump-building]]: Island Jump - Building (Platformer (jumping, sample game))
- [[case-studies-mystery-of-duvall-drive]]: The Mystery of Duvall Drive (Narrative horror demo (Roblox official sample))
- [[case-studies-plus-one-speed-keyboard-escape|case-studies-plus-1-speed-keyboard-escape]]: +1 Speed Keyboard Escape (Party / casual)
- [[case-studies-obby]]: Obby (Obstacle course / platformer (genre, not one named game))
- [[case-studies-poppa-balloon]]: Poppa Balloon (Tower defense / RNG (Roblox))
- [[case-studies-prison-life]]: Prison Life (Prison roleplay (Roblox))

## Reference files

- [[master-playbook]]: pipeline, decision rules, prompt starters
- [[all-numbers-and-benchmarks]]: every figure stated, newest first
- [[quotes-by-topic]]: near-verbatim quotes
- [[tools-and-resources]]: tools mentioned and further sources creators point to
- [[sources]]: every video used

## Creators / sources

- **Roblox Creator Docs** (official Roblox): 971 pages, 2026-10-28 to 2026-10-30
- **Roblox DevForum** (indie or community, figures self-reported): 344 pages, 2014-09-03 to 2026-10-30
- **Roblox Creators** (official Roblox): 93 videos, 2021-07-16 to 2026-10-30
- **Roblox** (official Roblox): 82 videos, 2018-07-24 to 2026-10-12
- **Roblox DevForum** (official Roblox): 52 pages, 2019-03-01 to 2026-10-30
- **janisjanis01** (indie or community, figures self-reported): 45 videos, 2023-08-29 to 2026-10-25
- **TheDankDeveloper** (indie or community, figures self-reported): 39 videos, 2023-04-14 to 2026-10-23
- **GnomeCode** (indie or community, figures self-reported): 33 videos, 2020-04-02 to 2026-02-28
- **SimTek Game Development** (indie or community, figures self-reported): 33 videos, 2020-12-11 to 2026-09-26
- **SmartyRBX** (indie or community, figures self-reported): 33 videos, 2021-08-11 to 2025-09-09
- **ByteBlox** (indie or community, figures self-reported): 32 videos, 2023-10-22 to 2025-03-15
- **PineappleDev** (indie or community, figures self-reported): 30 videos, 2023-11-07 to 2025-09-28
- **rasdev** (indie or community, figures self-reported): 30 videos, 2026-04-27 to 2026-10-23
- **B Ricey** (indie or community, figures self-reported): 28 videos, 2020-04-10 to 2024-04-14
- **Suphi Kaner** (indie or community, figures self-reported): 28 videos, 2021-11-10 to 2025-03-26
- **VuukStudios** (indie or community, figures self-reported): 28 videos, 2023-09-24 to 2026-10-21
- **Crusherfire** (indie or community, figures self-reported): 28 videos, 2024-01-18 to 2026-10-24
- **Tizzy** (indie or community, figures self-reported): 22 videos, 2026-05-11 to 2026-10-14
- **AlvinBlox** (indie or community, figures self-reported): 21 videos, 2018-08-07 to 2026-01-13
- **BloxianCode** (indie or community, figures self-reported): 20 videos, 2020-03-20 to 2024-04-20
- **ArTheDev** (indie or community, figures self-reported): 20 videos, 2025-02-03 to 2026-10-05
- **Cumin** (indie or community, figures self-reported): 20 videos, 2025-04-06 to 2026-09-13
- **Mulch** (indie or community, figures self-reported): 18 videos, 2021-09-05 to 2026-09-20
- **RoyalDev** (indie or community, figures self-reported): 17 videos, 2026-08-07 to 2026-10-22
- **Deconstructor of Fun** (indie or community, figures self-reported): 16 videos, 2025-04-08 to 2026-10-29
- **Roblox public API** (official Roblox): 16 pages, 2026-11-01 to 2026-11-01
- **MaximumADHD** (indie or community, figures self-reported): 15 videos, 2018-07-19 to 2026-09-09
- **Last Level Studios** (indie or community, figures self-reported): 15 videos, 2019-09-06 to 2025-11-05
- **Stewiepfing** (indie or community, figures self-reported): 14 videos, 2024-02-16 to 2026-09-13
- **Duckable** (indie or community, figures self-reported): 14 videos, 2025-02-07 to 2026-10-18
- **MoseyTube** (indie or community, figures self-reported): 14 videos, 2026-04-30 to 2026-10-14
- **Emancyphur** (indie or community, figures self-reported): 13 videos, 2014-12-27 to 2023-03-08
- **LovJak** (indie or community, figures self-reported): 13 videos, 2022-12-21 to 2026-10-15
- **Possible Panda** (indie or community, figures self-reported): 13 videos, 2024-11-27 to 2026-10-04
- **GameMakers** (indie or community, figures self-reported): 12 videos, 2020-03-30 to 2025-02-04
- **ItsZyonic** (indie or community, figures self-reported): 11 videos, 2023-06-29 to 2026-10-27
- **JustDucksey** (indie or community, figures self-reported): 11 videos, 2025-01-29 to 2026-08-09
- **Creators on the Blox** (indie or community, figures self-reported): 11 videos, 2025-10-18 to 2026-06-05
- **PolarBear** (indie or community, figures self-reported): 10 videos, 2024-02-02 to 2025-01-26
- **Raul** (indie or community, figures self-reported): 10 videos, 2026-06-15 to 2026-09-06
- **Generalist Programmer** (indie or community, figures self-reported): 10 videos, 2026-07-02 to 2026-07-07
- **MonarchDev** (indie or community, figures self-reported): 10 videos, 2026-08-18 to 2026-10-26
- **TheNexusAvenger** (indie or community, figures self-reported): 9 videos, 2015-04-22 to 2023-01-22
- **TheDevKing** (indie or community, figures self-reported): 9 videos, 2019-11-27 to 2020-07-24
- **BloxxedDev** (indie or community, figures self-reported): 9 videos, 2024-08-04 to 2025-08-02
- **ThatGuyEvan** (indie or community, figures self-reported): 8 videos, 2018-10-28 to 2022-08-26
- **Roox4** (indie or community, figures self-reported): 8 videos, 2023-04-15 to 2025-09-01
- **BubuTheDev** (indie or community, figures self-reported): 8 videos, 2024-09-06 to 2025-06-09
- **RoWatcher (tracker blog)** (indie or community, figures self-reported): 8 pages, 2026-00-00 to 2026-10-00
- **XTB7** (indie or community, figures self-reported): 7 videos, 2022-11-17 to 2023-10-31
- **Daiorg** (indie or community, figures self-reported): 7 videos, 2023-12-28 to 2025-12-21
- **CallMeDogey** (indie or community, figures self-reported): 7 videos, 2025-01-15 to 2026-04-25
- **Arow** (indie or community, figures self-reported): 7 videos, 2025-05-18 to 2026-05-30
- **Xaiyne** (indie or community, figures self-reported): 7 videos, 2025-08-08 to 2026-10-30
- **kra_DeZ** (indie or community, figures self-reported): 7 videos, 2026-08-26 to 2026-10-23
- **bubDEV** (indie or community, figures self-reported): 6 videos, 2024-08-24 to 2026-01-28
- **Leif** (indie or community, figures self-reported): 6 videos, 2025-05-19 to 2026-09-16
- **{EISABOOS} "RBX"** (indie or community, figures self-reported): 6 videos, 2025-05-21 to 2025-12-04
- **Erthlord** (indie or community, figures self-reported): 6 videos, 2025-06-08 to 2026-07-23
- **1_Bruce** (indie or community, figures self-reported): 6 videos, 2025-12-24 to 2026-04-17
- **TheDevBacon** (indie or community, figures self-reported): 5 videos, 2024-04-25 to 2026-08-30
- **FrenkyRBLX** (indie or community, figures self-reported): 5 videos, 2025-03-29 to 2025-12-24
- **#7Phantom** (indie or community, figures self-reported): 5 videos, 2025-07-18 to 2025-12-30
- **GamesBeat** (indie or community, figures self-reported): 5 pages, 2025-08-00 to 2026-09-12
- **studio rook.** (indie or community, figures self-reported): 5 videos, 2025-11-04 to 2026-10-21
- **anomalousDucky** (indie or community, figures self-reported): 4 videos, 2019-05-13 to 2022-06-03
- **waveshine** (indie or community, figures self-reported): 4 videos, 2024-10-12 to 2026-07-27
- **Quez** (indie or community, figures self-reported): 4 videos, 2025-02-09 to 2026-04-13
- **Lnor Roblox** (indie or community, figures self-reported): 4 videos, 2025-12-03 to 2026-09-23
- **GosuGamers** (indie or community, figures self-reported): 4 pages, 2026-00-00 to 2026-09-00
- **ThePurpleGuy** (indie or community, figures self-reported): 4 videos, 2026-02-03 to 2026-07-04
- **Yann** (indie or community, figures self-reported): 4 videos, 2026-05-12 to 2026-07-23
- **Seibo** (indie or community, figures self-reported): 4 videos, 2026-09-26 to 2026-10-10
- **1Coal** (indie or community, figures self-reported): 3 videos, 2023-05-07 to 2024-03-14
- **CORSO** (indie or community, figures self-reported): 3 videos, 2023-10-07 to 2025-05-29
- **MGFTUE** (indie or community, figures self-reported): 3 videos, 2025-03-28 to 2025-10-28
- **Crit** (indie or community, figures self-reported): 3 videos, 2025-07-25 to 2025-10-07
- **PocketGamer.biz** (indie or community, figures self-reported): 3 pages, 2025-10-11 to 2026-09-00
- **DitchyDevelopments** (indie or community, figures self-reported): 3 videos, 2025-11-07 to 2026-06-18
- **Matt The Method** (indie or community, figures self-reported): 3 videos, 2025-12-01 to 2026-08-26
- **AllThingsHow (guide)** (indie or community, figures self-reported): 3 pages, 2026-00-00 to 2026-08-25
- **Alex Builds Games** (indie or community, figures self-reported): 3 videos, 2026-05-16 to 2026-10-09
- **Roblox Newsroom** (official Roblox): 3 pages, 2026-06-00 to 2026-09-11
- **ContextLost** (indie or community, figures self-reported): 2 videos, 2018-03-07 to 2018-11-06
- **Game Maker's Toolkit** (indie or community, figures self-reported): 2 videos, 2018-05-27 to 2022-04-25
- **Amora** (indie or community, figures self-reported): 2 videos, 2023-07-31 to 2023-08-03
- **MonzterDEV** (indie or community, figures self-reported): 2 videos, 2024-03-01 to 2024-09-23
- **StudioKrew (agency blog, GGAID data)** (indie or community, figures self-reported): 2 pages, 2026-05-00 to 2026-08-20
- **Chase Higgins** (indie or community, figures self-reported): 2 videos, 2026-07-08 to 2026-07-24
- **Roblox Investor Relations** (official Roblox): 2 pages, 2026-07-30 to 2026-09-30
- **Rapstrike GFX** (indie or community, figures self-reported): 2 videos, 2026-10-09 to 2026-10-25
- **mats-dept2** (indie or community, figures self-reported): 2 videos, 2026-10-10 to 2026-10-10
- **The Letus Garden** (indie or community, figures self-reported): 1 videos, 2020-11-13 to 2020-11-13
- **TechSpectrum** (indie or community, figures self-reported): 1 videos, 2021-01-23 to 2021-01-23
- **TanookiAlex** (indie or community, figures self-reported): 1 videos, 2021-02-06 to 2021-02-06
- **GDC Festival of Gaming** (indie or community, figures self-reported): 1 videos, 2022-02-01 to 2022-02-01
- **GameDiscoverCo** (indie or community, figures self-reported): 1 videos, 2022-05-24 to 2022-05-24
- **Dev Total** (indie or community, figures self-reported): 1 videos, 2022-11-23 to 2022-11-23
- **AlexDev** (indie or community, figures self-reported): 1 videos, 2023-03-31 to 2023-03-31
- **Itz_FloppyFish** (indie or community, figures self-reported): 1 videos, 2023-04-02 to 2023-04-02
- **MiniBloxia** (indie or community, figures self-reported): 1 videos, 2023-06-09 to 2023-06-09
- **Big Turtle** (indie or community, figures self-reported): 1 videos, 2024-03-11 to 2024-03-11
- **BadGameDev** (indie or community, figures self-reported): 1 videos, 2024-10-21 to 2024-10-21
- **Syrax** (indie or community, figures self-reported): 1 videos, 2025-03-11 to 2025-03-11
- **RoDev** (indie or community, figures self-reported): 1 videos, 2025-05-23 to 2025-05-23
- **Perstile** (indie or community, figures self-reported): 1 videos, 2025-05-30 to 2025-05-30
- **RoBuilder** (indie or community, figures self-reported): 1 videos, 2025-06-26 to 2025-06-26
- **Bemmy** (indie or community, figures self-reported): 1 videos, 2025-06-28 to 2025-06-28
- **BrawlDev** (indie or community, figures self-reported): 1 videos, 2025-11-09 to 2025-11-09
- **JustVeryYellow** (indie or community, figures self-reported): 1 videos, 2025-11-16 to 2025-11-16
- **Poke** (indie or community, figures self-reported): 1 videos, 2025-12-12 to 2025-12-12
- **Britt Drake** (indie or community, figures self-reported): 1 videos, 2025-12-14 to 2025-12-14
- **Ventures** (indie or community, figures self-reported): 1 videos, 2025-12-18 to 2025-12-18
- **Tubefilter** (indie or community, figures self-reported): 1 pages, 2026-00-00 to 2026-00-00
- **Player.One** (indie or community, figures self-reported): 1 pages, 2026-00-00 to 2026-00-00
- **Dexerto** (indie or community, figures self-reported): 1 pages, 2026-00-00 to 2026-00-00
- **Izzzyzzz** (indie or community, figures self-reported): 1 videos, 2026-01-16 to 2026-01-16
- **CaberJaber** (indie or community, figures self-reported): 1 videos, 2026-03-14 to 2026-03-14
- **Naavik Gaming Podcast** (indie or community, figures self-reported): 1 videos, 2026-03-17 to 2026-03-17
- **DudeGuy** (indie or community, figures self-reported): 1 videos, 2026-03-18 to 2026-03-18
- **Rool-Studio** (indie or community, figures self-reported): 1 videos, 2026-04-11 to 2026-04-11
- **Platform Aeronaut (transcript)** (indie or community, figures self-reported): 1 pages, 2026-07-30 to 2026-07-30
- **Pwnedbloxx** (indie or community, figures self-reported): 1 videos, 2026-08-20 to 2026-08-20
- **Business of Creators** (indie or community, figures self-reported): 1 videos, 2026-08-21 to 2026-08-21
- **eGamers** (indie or community, figures self-reported): 1 pages, 2026-08-25 to 2026-08-25
- **NetInfluencer** (indie or community, figures self-reported): 1 pages, 2026-09-00 to 2026-09-00
- **Vindooly** (indie or community, figures self-reported): 1 videos, 2026-09-09 to 2026-09-09
- **revolver agz** (indie or community, figures self-reported): 1 videos, 2026-09-18 to 2026-09-18
- **OtakuKart** (indie or community, figures self-reported): 1 pages, 2026-09-30 to 2026-09-30
- **RoTrends (tracker)** (indie or community, figures self-reported): 1 pages, 2026-10-00 to 2026-10-00
- **Where The Money Went** (indie or community, figures self-reported): 1 videos, 2026-10-01 to 2026-10-01
- **GuideRealm** (indie or community, figures self-reported): 1 videos, 2026-10-17 to 2026-10-17
- **ProjectSupreme** (indie or community, figures self-reported): 1 videos, 2026-10-20 to 2026-10-20
- **tef** (indie or community, figures self-reported): 1 videos, 2026-10-23 to 2026-10-23

## Per-creator notes
Each source has its own sibling folder next to this one (folder name = channel handle, plus `docs` for Roblox Creator Docs pages and `devforum` for DevForum posts, `must-watch` for the mixed official-session list). Inside: `Videos/` (one note per video or page), `Themes/`, games/numbers/tools notes and the playbook below.

- [[1Coal - How to make successful Roblox games]] (folder `1Coal`)
- [[1_Bruce - How to make successful Roblox games]] (folder `1_Bruce`)
- [[5uphi - How to make successful Roblox games]] (folder `5uphi`)
- [[7PhantomS - How to make successful Roblox games]] (folder `7PhantomS`)
- [[AlvinBlox - How to make successful Roblox games]] (folder `AlvinBlox`)
- [[AnomalousDucky - How to make successful Roblox games]] (folder `AnomalousDucky`)
- [[ArTheDev - How to make successful Roblox games]] (folder `ArTheDev`)
- [[ArowDev - How to make successful Roblox games]] (folder `ArowDev`)
- [[BRicey - How to make successful Roblox games]] (folder `BRicey`)
- [[BloxianCode - How to make successful Roblox games]] (folder `BloxianCode`)
- [[BloxxedDev - How to make successful Roblox games]] (folder `BloxxedDev`)
- [[BrawlDevRBLX - How to make successful Roblox games]] (folder `BrawlDevRBLX`)
- [[BubuTheDev - How to make successful Roblox games]] (folder `BubuTheDev`)
- [[CORSOBLOX - How to make successful Roblox games]] (folder `CORSOBLOX`)
- [[CreatorsOnTheBlox - How to make successful Roblox games]] (folder `CreatorsOnTheBlox`)
- [[CritDEV - How to make successful Roblox games]] (folder `CritDEV`)
- [[DaiorgYT - How to make successful Roblox games]] (folder `DaiorgYT`)
- [[DitchyDevelopments - How to make successful Roblox games]] (folder `DitchyDevelopments`)
- [[DuckableDev - How to make successful Roblox games]] (folder `DuckableDev`)
- [[Emancyphur - How to make successful Roblox games]] (folder `Emancyphur`)
- [[Erthlord - How to make successful Roblox games]] (folder `Erthlord`)
- [[FrenkyRBLX - How to make successful Roblox games]] (folder `FrenkyRBLX`)
- [[GameMakersDev - How to make successful Roblox games]] (folder `GameMakersDev`)
- [[GnomeCode - How to make successful Roblox games]] (folder `GnomeCode`)
- [[ItsZyonic - How to make successful Roblox games]] (folder `ItsZyonic`)
- [[JustDucksey - How to make successful Roblox games]] (folder `JustDucksey`)
- [[LastLevelStudios - How to make successful Roblox games]] (folder `LastLevelStudios`)
- [[LovJak - How to make successful Roblox games]] (folder `LovJak`)
- [[MGFTUE - How to make successful Roblox games]] (folder `MGFTUE`)
- [[MattTheMethod - How to make successful Roblox games]] (folder `MattTheMethod`)
- [[MaximumADHD - How to make successful Roblox games]] (folder `MaximumADHD`)
- [[MonarchSilgrit - How to make successful Roblox games]] (folder `MonarchSilgrit`)
- [[MonzterDEV - How to make successful Roblox games]] (folder `MonzterDEV`)
- [[MoseyTube - How to make successful Roblox games]] (folder `MoseyTube77`)
- [[Mulchmite - How to make successful Roblox games]] (folder `Mulchmite`)
- [[NotCumin - How to make successful Roblox games]] (folder `NotCumin`)
- [[PolarbearRBLXX - How to make successful Roblox games]] (folder `PolarbearRBLXX`)
- [[PossiblePanda - How to make successful Roblox games]] (folder `PossiblePanda`)
- [[RaulStudios - How to make successful Roblox games]] (folder `RaulStudios`)
- [[RobloxOfficial - How to make successful Roblox games]] (folder `Roblox`)
- [[RobloxCreators - How to make successful Roblox games]] (folder `RobloxCreators`)
- [[Roox4Official - How to make successful Roblox games]] (folder `Roox4Official`)
- [[SeiboRoblox - How to make successful Roblox games]] (folder `SeiboRoblox`)
- [[SimTekGameDevelopment - How to make successful Roblox games]] (folder `SimTekGameDevelopment`)
- [[SmartyRBX - How to make successful Roblox games]] (folder `SmartyRBX`)
- [[ThatGuyEvan - How to make successful Roblox games]] (folder `ThatGuyEvan`)
- [[TheDankDeveloper - How to make successful Roblox games]] (folder `TheDankDeveloper`)
- [[TheDevBacon - How to make successful Roblox games]] (folder `TheDevBacon`)
- [[TheDevKing - How to make successful Roblox games]] (folder `TheDevKing`)
- [[TheNexusAvenger - How to make successful Roblox games]] (folder `TheNexusAvenger`)
- [[ThePurpleGuy_0 - How to make successful Roblox games]] (folder `ThePurpleGuy_0`)
- [[TheRoyalDev - How to make successful Roblox games]] (folder `TheRoyalDev`)
- [[Tizzy - How to make successful Roblox games]] (folder `TizzyRBLX12`)
- [[Yann4dev - How to make successful Roblox games]] (folder `Yann4dev`)
- [[alexbuilds_games - How to make successful Roblox games]] (folder `alexbuilds_games`)
- [[bubDEV - How to make successful Roblox games]] (folder `bubDEV`)
- [[byteblox100 - How to make successful Roblox games]] (folder `byteblox100`)
- [[callmedogey - How to make successful Roblox games]] (folder `callmedogey`)
- [[crusherfiredev - How to make successful Roblox games]] (folder `crusherfiredev`)
- [[deconstructoroffun - How to make successful Roblox games]] (folder `deconstructoroffun`)
- [[Roblox DevForum - How to make successful Roblox games]] (folder `devforum`)
- [[Roblox Creator Docs - How to make successful Roblox games]] (folder `docs`)
- [[gamediscoverco - How to make successful Roblox games]] (folder `gamediscoverco`)
- [[generalistprogrammer3233 - How to make successful Roblox games]] (folder `generalistprogrammer3233`)
- [[janisjanis01 - How to make successful Roblox games]] (folder `janisjanis01`)
- [[kra_DeZ - How to make successful Roblox games]] (folder `kra_DeZ`)
- [[l_eif - How to make successful Roblox games]] (folder `l_eif`)
- [[leads - How to make successful Roblox games]] (folder `leads`)
- [[lnorroblox - How to make successful Roblox games]] (folder `lnorroblox`)
- [[MustWatch - How to make successful Roblox games]] (folder `must-watch`)
- [[pineappledevv - How to make successful Roblox games]] (folder `pineappledevv`)
- [[quezdev - How to make successful Roblox games]] (folder `quezdev`)
- [[rasdevblox - How to make successful Roblox games]] (folder `rasdevblox`)
- [[stewiepfing - How to make successful Roblox games]] (folder `stewiepfing`)
- [[studiorookroblox - How to make successful Roblox games]] (folder `studiorookroblox`)
- [[vuukstudios7635 - How to make successful Roblox games]] (folder `vuukstudios7635`)
- [[waveshinedev - How to make successful Roblox games]] (folder `waveshinedev`)
- [[xtb7-dev - How to make successful Roblox games]] (folder `xtb7-dev`)

## Big sheets: read the TL;DR first

- [[BENCHMARKS-TLDR]]: short index of [[BENCHMARKS]]
- [[DECISION-RULES-TLDR]]: short index of [[DECISION-RULES]]
- [[CHECKLIST-launch-TLDR]]: short index of [[CHECKLIST-launch]]
- [[AD-PLAYBOOK-TLDR]]: short index of [[AD-PLAYBOOK]]
- [[all-numbers-and-benchmarks-TLDR]]: short index of [[all-numbers-and-benchmarks]]
- [[tools-and-resources-TLDR]]: short index of [[tools-and-resources]]
