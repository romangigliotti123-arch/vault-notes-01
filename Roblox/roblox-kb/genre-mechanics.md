---
title: Genre Mechanics
topic: genre-mechanics
theme: Game Ideas
sources: 63 videos
creators: [AlexDev, ArTheDev, ByteBlox, Cumin, Emancyphur, Game Maker's Toolkit, GnomeCode, JustDucksey, Last Level Studios, LovJak, MonarchDev, Mulch, PineappleDev, Raul, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox DevForum, Roblox Newsroom, Roox4, RoyalDev, SimTek Game Development, StudioKrew (agency blog, GGAID data), VuukStudios, bubDEV, janisjanis01]
source_dates: 2020-09-17 to 2026-10-28
tags: [roblox, knowledge-base, genre-mechanics]
---

# Genre Mechanics

_genre-specific design/mechanics: tycoon, simulator, obby, horror, RPG, FPS, tower defense, roleplay, fighting, racing._

Evidence base: 83 extracted items from 63 videos by AlexDev, ArTheDev, ByteBlox, Cumin, Emancyphur, Game Maker's Toolkit, GnomeCode, JustDucksey, Last Level Studios, LovJak, MonarchDev, Mulch, PineappleDev, Raul, RoWatcher (tracker blog), Roblox, Roblox Creator Docs, Roblox DevForum, Roblox Newsroom, Roox4, RoyalDev, SimTek Game Development, StudioKrew (agency blog, GGAID data), VuukStudios, bubDEV, janisjanis01 (2020-09-17 to 2026-10-28). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Creators teach genre design on Roblox through horror craft, combat/NPC mechanics, and progression design. Horror: gradual build-up, varied fears, sparing jumpscares, no big pure-dark areas, visible objectives. Combat/PvE: varied enemy behaviours, scaling difficulty, bosses that teach mechanics, target priority in tower defense, simple status effects, separate PvP/PvE, mobile vs PC balance. Tycoon/simulator: needs a build/upgrade loop; optimisation-style progression; reusing proven loops is viable but categorise correctly. Technical: Raycast for projectiles, constraints over BodyMovers/tweens, pathfinding limits (~3.5 studs), disabling unused Humanoid states on NPCs, CollectionService tags for detection. Official docs add age-based access rules per genre, weapon config (ChargeRate), and cooldown patterns. Indie claims are self-reported.

## Rules and findings
- **Build horror gradually, then reveal** (single-mention): Hint with small incremental changes (e.g. slightly thicker fog each step) so players notice subconsciously, then give a sudden reveal at the end. Sources: [ByteBlox 2025-01 1:05](https://youtu.be/K-KvVwt_Y4I?t=65). Newest source 2025-01-05.
- **Avoid large areas of pure darkness** (one-creator-repeated): Total darkness reads as frustrating on a 2D screen rather than scary. Give a flashlight only if needed and let it aim freely vertically instead of locking it to view height. Sources: [GnomeCode 2024-10 7:20](https://youtu.be/H9CbgCe47Mo?t=440), [GnomeCode 2024-10 8:02](https://youtu.be/H9CbgCe47Mo?t=482). Newest source 2024-10-12.
- **Make the horror escape objective visible** (single-mention): Place the final objective (e.g. button) far from spawn but reachable, and make it visible in the dark with a neon part rather than highlights. Sources: [ByteBlox 2025-01 26:57](https://youtu.be/K-KvVwt_Y4I?t=1617). Newest source 2025-01-05.
- **Mix horror elements, phobias and uncanny visuals** (one-creator-repeated): Include a little fear, shock and disgust; use a range of phobias (nyctophobia, arachnophobia, astraphobia, agoraphobia, mysophobia). Turn happy things scary (FNAF-style) and use uncanny-valley monsters. Treat horror as a theme/style and design mechanics around it. Sources: [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2023-03](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571). Newest source 2023-03-09.
- **Use jumpscares and distress sounds sparingly** (one-creator-repeated): Avoid overusing jumpscares; place them where least expected and only when they enhance the story. Use beings in distress (crying, screaming, panting) only when tied to lore; placement matters. Sources: [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917). Newest source 2021-12-10.
- **Gate teleporting monsters with Dot** (single-mention): Use a dot product look-check so teleport-behind-player monsters only move when the player is not looking at them. Sources: [Roblox DevForum 2020-12](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984). Newest source 2020-12-31.
- **Name difficulties Normal/Hard/Extreme; reward easter eggs** (one-creator-repeated): Easy options feel less intimidating to select, so avoid Easy/Normal/Hard. Hide easter eggs and award badges for discovery, hinting in the badges tab. Sources: [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917), [Roblox DevForum 2021-12](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917). Newest source 2021-12-10.
- **Offer modes that change the enemy, not the objective** (single-mention): Same objective with enemy as bot, player-controlled, traitor or infection adds replayability without new content. Sources: [Emancyphur 2020-09 5:02](https://youtu.be/C0ybJ5ghSHk?t=302). Newest source 2020-09-17.
- **Vary enemy behaviours and scale PvE difficulty** (one-creator-repeated): Single-note enemies lead to kiting into an AoE clump. Flat difficulty plus player power growth makes late game trivial; ramp difficulty across campaign stages. Sources: [Cumin 2026-09 8:11](https://youtu.be/kjLtxvB_iyk?t=491), [Cumin 2025-07 11:43](https://youtu.be/jXogdTgtlXE?t=703). Newest source 2026-09-13.
- **Bosses and practice must teach** (one-creator-repeated): Check the first boss can't be cheesed by running, or players never learn core mechanics. Make practice viable; a private server with clumped, unkillable AI titans gives no real practice. Sources: [Cumin 2025-12 11:57](https://youtu.be/hQpC_UHxJDU?t=717), [Cumin 2025-06 3:55](https://youtu.be/Z1tj1OPOEZg?t=235). Newest source 2025-12-23.
- **Consider separating PvP from PvE** (single-mention): So PvP players don't block campaign progress. Sources: [Cumin 2025-07 15:21](https://youtu.be/jXogdTgtlXE?t=921). Newest source 2025-07-31.
- **Design maps around the core movement** (one-creator-repeated): In movement-based games, tall reachable structures matter more than realism. Physics rigs with grabbable ledges (Edgeworks, Boneworks-inspired) allow free climbing. Sources: [Cumin 2025-07 5:35](https://youtu.be/jXogdTgtlXE?t=335), [Last Level Studios 2021-12 11:14](https://youtu.be/v_TGu45AD_g?t=674). Newest source 2025-07-31.
- **Handle mobile/PC imbalance and audience fit** (multiple-creators): Mouse/keyboard beats mobile at equal skill; consider mobile-only lobbies (Blade Ball reportedly). Match concept to the majority audience, largely children on mobile; space games are niche because of complexity for a young audience. Sources: [ByteBlox 2024-11 25:31](https://youtu.be/1KKQ6YrktTk?t=1531), [RoyalDev 2026-08 5:28](https://youtu.be/RXmiJkaZWV4?t=328), [Roblox DevForum 2025-01](https://devforum.roblox.com/t/i-made-a-planetaryspherical-gravity-system/3383865), [Roblox DevForum 2025-01](https://devforum.roblox.com/t/i-made-a-planetaryspherical-gravity-system/3383865). Newest source 2026-08-07.
- **Tycoons need depth; progression as optimisation** (multiple-creators): A collect pad alone lacks depth; add build or upgrade choices. Factorio/Satisfactory-style optimisation makes progression reward planning rather than repetition. Sources: [Cumin 2025-08 3:30](https://youtu.be/wdf6cfH3rnA?t=210), [Game Maker's Toolkit 2022-04 8:16](https://youtu.be/Zrf1cou_yVo?t=496). Newest source 2025-08-31.
- **Reusing proven loops is viable; categorise correctly** (multiple-creators): Combine successful games plus one or two twists (PineappleDev, as a joke); bubDEV reports Escape Tsunami template games earning (unverified); destruction upgrade loops proven (Last Level Studios). An RNG/idle game belongs under Simulator, not RPG (MonarchDev). Shooters resist pay-to-win and need cohesive gunplay (Cumin). Sources: [PineappleDev 2025-07 2:02](https://youtu.be/ggWeHThD_3Q?t=122), [bubDEV 2026-01 0:32](https://youtu.be/2lPsxPtj2mM?t=32), [Last Level Studios 2021-08 19:14](https://youtu.be/3djSOjdGaE8?t=1154), [MonarchDev 2026-09 0:40](https://youtu.be/LD7LGP10dRc?t=40), [Cumin 2025-09 5:05](https://youtu.be/Jf2RvsWMPes?t=305). Newest source 2026-09-11.
- **RPG: vary dungeons, add bestiary** (one-creator-repeated): Each dungeon should feel unique (World Zero cited). A built-in bestiary with defeated enemies and drop chances is a good resource that should be common. Sources: [Cumin 2025-05 14:49](https://youtu.be/2auVezIcNAE?t=889), [Cumin 2025-12 5:57](https://youtu.be/hQpC_UHxJDU?t=357). Newest source 2025-12-23.
- **Tower defense: target priority and balance** (multiple-creators): Add closest/strongest/last modes with a hotkey toggle. Balance or cut towers nobody uses (creator found only two of several used). Sources: [janisjanis01 2026-06 4:36](https://youtu.be/CltiB53QTHw?t=276), [Raul 2026-06 0:12](https://youtu.be/kKavvUDtHOg?t=12). Newest source 2026-06-23.
- **Keep status effects simple** (single-mention): Burn, slow, chill, shock; avoid multi-step ailment chains. Sources: [AlexDev 2023-03 3:54](https://youtu.be/bYyD6tyz6Dg?t=234). Newest source 2023-03-31.
- **Projectiles and physics** (multiple-creators): Raycast for about 99% of projectiles; GetPartsInBox for large mostly linear ones; avoid .Touched unless physics-heavy bouncing. Use VectorForce/AngularVelocity (Attachment on HumanoidRootPart) for knockback instead of BodyMovers; LinearVelocity instead of tweens for platforms (heavy or oddly oriented parts can misbehave). Sources: [Roblox DevForum 2024-06](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332), [SimTek Game Development 2023-02 0:00](https://youtu.be/-sQHMwuVAu4?t=0), [SimTek Game Development 2023-09 0:00](https://youtu.be/6sgx1elbhwU?t=0). Newest source 2024-06-24.
- **Weapon config and pickups (official)** (one-creator-repeated): ChargeRate makes a charging weapon (railgun, bow); DischargeRate defaults to 0. Use cooldown pattern for limits like rocket reload. Pickups need Action, Pickup, WeaponPickup, WeaponSystemIgnore plus one rarity tag. Laser Tag extends to a fast FPS prototype. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/weapons-kit), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/debounce), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/battle-royale/pickup-system), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/templates). Newest source 2026-10-28.
- **NPC setup and performance** (multiple-creators): Disable unused HumanoidStateTypes (Climbing, Swimming) via SetStateEnabled to cut stepHumanoid cost. Copy Animate script under NPC humanoid (server script). Pathfinding jumps clear only ~3.5 studs in one test; keep obstacles low. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/performance-optimization/improve), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table), [Roblox DevForum 2022-07](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779), [SimTek Game Development 2021-07 18:13](https://youtu.be/lJktfRT2pbg?t=1093). Newest source 2026-10-28.
- **NPC vision, detection and soldiers** (multiple-creators): Sphere point generation plus raycasting gives vision (example 30 stud range, 70 degree FOV). Tag NPCs 'NPC' and detectables 'Detectable' via CollectionService (Models need PrimaryPart). Soldier AttackMode: 1 SoldierEnemy only, 2 everything without SoldierFriend, 3 all characters (official). Sources: [Roblox DevForum 2020-11](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144), [Roblox DevForum 2023-07](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522), [Roblox DevForum 2023-07](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522), [Roblox DevForum 2023-07](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/npc-kit). Newest source 2026-10-28.
- **Match safety/access levels to genre (official)** (single-mention): Competitive FPS: Unknown only in casual; Standard and Full in ranked. Fighting: separate or trusted servers. Racing: keep Unknown and None off leaderboards. Idle/tycoon: withhold AFK rewards from None, not Unknown. Trade: block at None. Roleplay/social: full access. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/security/device-trust), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/security/device-trust). Newest source 2026-10-28.
- **Obby hazards and platforms** (multiple-creators): Neon kill bricks stand out against stage colors; avoid clashing colors. Duplicate fading platforms across wider gaps and tune fade speed for difficulty. Sources: [Mulch 2024-07 4:06](https://youtu.be/y9Ii0VEFaEU?t=246), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap). Newest source 2026-10-28.
- **Terrain and weather generation** (one-creator-repeated): Fractal noise (4 octaves, lacunarity 3, persistence 0.35) over single Perlin. Weather via weighted random (sunny 40%, rain 20%, others 10%) rolled after each ends. Sources: [Roblox DevForum 2021-10](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362), [Roblox DevForum 2021-10](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362), [ArTheDev 2026-04 7:01](https://youtu.be/CnZEnFVAFSw?t=421). Newest source 2026-04-03.
- **Camera, UI and character conventions (official)** (one-creator-repeated): ~2 stud offset aiming camera from HumanoidRootPart; Consistent Gameplay preset for collision consistency; genre iconography (sword, beaker); one task at a time for younger players. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/avatar-settings), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/choose-an-art-style), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/developer/planning-for-educational-settings). Newest source 2026-10-28.
- **Mobile toggle-run handling** (single-mention): Track a 0/1 count per tap and use a short task.wait before resetting so the stop tap doesn't restart running. Sources: [VuukStudios 2023-09 9:15](https://youtu.be/dcJtZnan7i8?t=555). Newest source 2023-09-24.
- **2D tooling and misc platform features** (one-creator-repeated): Orthographic cameras, sprite containers, sprite sheets ease 2D/2.5D. Team-only voice via AudioDeviceInput.AccessType and SetUserIdAccessList. Harvestables need BoolValue CanHarvest = true. A shotgun no-reload bug became a minigun enemy idea. Sources: [Roblox 2026-09 11:39](https://youtu.be/3a2RbLOAl4A?t=699), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/lesson-plans/roblox-developer/roblox-developer-4), [Roox4 2023-04 6:19](https://youtu.be/Pbrvfdn9UN8?t=379). Newest source 2026-10-28.
- **Use meme aesthetics as a hook, not a retention plan** (single-mention): RoWatcher says collection mechanics wrapped in viral 'brainrot' meme aesthetics can drive scale, citing Steal a Brainrot and Escape Tsunami For Brainrots. Treat the meme theme as top-of-funnel. Indie, self-reported, low-advice source; no figures given. Sources: [RoWatcher (tracker blog) 2026-03](https://rowatcher.com/news/the-10-fastest-growing-roblox-games-in-march-2026). Newest source 2026-03-00.
- **Pair viral spikes with deeper systems** (single-mention): RoWatcher reports meme/viral games get huge visit spikes but average only 8–12 min sessions and normalise quickly after the novelty window. Plan progression, collection or tycoon depth, and retention loops before launch rather than relying on the spike. Sources: [RoWatcher (tracker blog) 2026-03](https://rowatcher.com/news/top-10-roblox-games-by-players-march-2026-data-breakdown). Newest source 2026-03-00.
- **Calibrate competitive shooters for touchscreen first** (single-mention): StudioKrew, citing RIVALS' approach, says shooters should be tuned for touchscreen first: controls, hitbox forgiveness and matchmaking. Scale up to PC and console after that. This refines the general mobile/PC imbalance rule with FPS-specific detail. Self-reported. Sources: [StudioKrew (agency blog, GGAID data) 2026-05](https://studiokrew.com/blog/top-roblox-games-may-2026/). Newest source 2026-05-00.
- **Extend horror sessions with survival systems, not scares** (single-mention): StudioKrew cites 99 Nights in the Forest: prioritise atmosphere and survival systems over cheap jump scares to earn longer sessions. This complements the existing sparing-jumpscare rule by adding a survival loop as the session-length driver. Self-reported. Sources: [StudioKrew (agency blog, GGAID data) 2026-05](https://studiokrew.com/blog/top-roblox-games-may-2026/). Newest source 2026-05-00.
- **Signal wrong paths visually, not with invisible walls** (single-mention): In chase sequences, invisible walls used as the only route signal make players feel cheated when they hit them mid-escape. Use visible cues such as lighting, signage, props, or physical barriers so the wrong path is readable before the player commits. Sources: [Cumin 2026-08 6:21](https://youtu.be/rjPW4GeeyFg?t=381). Newest source 2026-08-22.
- **Cap enemy count per map and give each enemy a distinct purpose** (single-mention): Overlapping, crowded enemies make tension feel unfun. Limit how many enemies a map spawns and assign each one a clear role, so each threat reads separately. This extends the existing enemy-variety rule with a count limit. Sources: [Cumin 2026-08 11:14](https://youtu.be/rjPW4GeeyFg?t=674). Newest source 2026-08-22.
- **Plan more areas after the starting zone** (single-mention): A single starting area gets exhausted quickly once players have seen everything, and the map then feels boring. Plan additional areas as later content so retention does not depend on the first zone alone. Source is low-advice and self-reported. Sources: [LovJak 2026-10 2:46](https://youtu.be/YXcV0Ba0RJc?t=166), [LovJak 2026-10 2:46](https://youtu.be/YXcV0Ba0RJc?t=166). Newest source 2026-10-15.
- **Build a progressive obby challenge library with cooperative mechanics** (single-mention): Use a library of obby challenges that get progressively harder, then add unique mechanics such as shared-momentum zones that reward players for cooperating. Difficulty ramps across the library instead of being uniform across stages. Sources: [MonarchDev 2026-10 5:46](https://youtu.be/hPWJlFwp5Xs?t=346). Newest source 2026-10-16.
- **Generate endless levels procedurally from a small piece set** (single-mention): Use procedural track and map generation to assemble effectively endless levels from a small set of hand-built pieces. This keeps authoring cost low while varying each run. Pair it with a deliberate piece library so generated layouts stay playable. Sources: [JustDucksey 2025-06 3:26](https://youtu.be/XRvcKGSLr4g?t=206). Newest source 2025-06-14.
- **Stress-test momentum and swing physics in obbies** (single-mention): Swinging can be a fun core obby mechanic, but janky swing physics made a reviewer quit. Test momentum, pendulum arcs, release timing and landing thoroughly before release, and treat swing feel as a core QA item rather than polish. Sources: [Cumin 2026-05 4:20](https://youtu.be/tT-u3b6LMkQ?t=260). Newest source 2026-05-30.

## Checklist
- [ ] Confirm genre categorisation (RNG/idle = Simulator)
- [ ] Match concept to young mobile majority audience
- [ ] Decide mobile/PC balance
- [ ] Horror: avoid big pure-dark zones, build gradually, sparing jumpscares
- [ ] Make final objective visible (neon part)
- [ ] Name difficulties Normal/Hard/Extreme
- [ ] Add easter eggs with badges
- [ ] Scale PvE difficulty per stage
- [ ] Ensure first boss teaches mechanics
- [ ] Vary enemy behaviours and dungeon designs
- [ ] Add target priority modes in tower defense
- [ ] Balance or cut unused towers
- [ ] Keep status effects simple
- [ ] Use Raycast for projectiles
- [ ] Use constraints, not BodyMovers
- [ ] Disable unused Humanoid states on NPCs
- [ ] Keep jumpable obstacles low (~3.5 studs)
- [ ] Tag NPCs and detectables via CollectionService
- [ ] Configure ChargeRate for charging weapons; use cooldowns
- [ ] Apply genre-appropriate safety/access settings
- [ ] Add build/upgrade depth to tycoons
- [ ] Provide real practice mode and bestiary
- [ ] Before building a meme- or brainrot-themed game, plan the depth systems (progression, collection, retention loops) because virality normalises quickly. Cite T17463 and T17471.
- [ ] Use the 8–12 min average session figure (T17471, self-reported) as a reference point. If retention sits at or below it, suspect a novelty-only hook.
- [ ] For a competitive shooter, test controls, hitbox forgiveness and matchmaking on touchscreen before tuning for PC or console. Cite T17477.
- [ ] For horror, add a survival loop before adding scares, and keep jump scares rare. Cite T17484.
- [ ] In chase sequences, mark wrong paths with visible cues (lighting, signs, props, barriers) and avoid invisible walls as the only signal.
- [ ] Set a maximum enemy count per map and confirm each enemy has a distinct role before adding more.
- [ ] Plan at least one additional area beyond the starting zone so the map does not exhaust once players have seen it.
- [ ] For obbies, build a sequence of challenges that increase in difficulty and consider one cooperative mechanic, such as a shared-momentum zone.
- [ ] If the obby includes swings or ropes, playtest momentum, release timing and landing before release.
- [ ] If the genre needs endless variety, build a small library of hand-made pieces and assemble levels procedurally from them.
- [ ] When using procedural level assembly, playtest multiple generated outputs, not just one seed.
- [ ] Treat swing feel as a core obby mechanic to tune, not a cosmetic detail.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| Pathfinding jump clearance | ~3.5 studs | Speaker's test; character can jump higher | [SimTek Game Development 2021-07 18:13](https://youtu.be/lJktfRT2pbg?t=1093) |
| Fractal noise | 4 octaves, lacunarity 3, persistence 0.35 | Mountain terrain | [Roblox DevForum 2021-10](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362), [Roblox DevForum 2021-10](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362) |
| NPC view range | 30 studs | Default in example script | [Roblox DevForum 2023-07](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) |
| NPC field of view | 70 degrees | Default in example script | [Roblox DevForum 2023-07](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522) |
| Raycast share of projectiles | ~99% | Recommended use | [Roblox DevForum 2024-06](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332) |
| Weather weights | sunny 40%, rain 20%, others 10% | Example | [ArTheDev 2026-04 7:01](https://youtu.be/CnZEnFVAFSw?t=421) |
| HumanoidRootPart below head | ~2 studs | Camera offset (official) | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera) |
| 2-player obby visits | almost 4 million | Self-reported, unverified, ~a year before 2025-11 | [VuukStudios 2025-11 9:51](https://youtu.be/AbjI7ygMnao?t=591) |
| AttackMode values | 1, 2, 3 | Official soldier config | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/npc-kit) |
| DischargeRate default | 0 | Official | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/weapons-kit) |
| Average session length, meme/viral games | 8–12 min | Self-reported by RoWatcher tracker blog. Visit spikes are large, but sessions are short and interest normalises after the novelty window. | [RoWatcher (tracker blog) 2026-03](https://rowatcher.com/news/top-10-roblox-games-by-players-march-2026-data-breakdown) |

## Where creators agree
- GnomeCode and ByteBlox agree horror should rely on atmosphere with visible objectives; Roblox DevForum horror posts agree on variety and restraint.
- Cumin repeatedly argues for depth and variety in enemies, difficulty and modes.
- Roblox Creator Docs and SimTek/DevForum agree on reducing NPC cost and avoiding legacy approaches.
- RoWatcher (T17471) and StudioKrew (T17484) both favour longer-session design (depth or survival systems) over one-off hooks such as spikes or cheap scares. This is a loose cross-creator agreement based on one item each.

## Where creators disagree
- **Copying proven games**
  - bubDEV: reusing proven loops is viable and earning (unverified)
  - PineappleDev: combine successful games plus twists, presented as a joke
  - Cumin: criticises shallow tycoons and cash-grab simulators; wants depth
- **Darkness in horror**
  - Roblox DevForum: use nyctophobia among phobias
  - GnomeCode: avoid large areas of pure darkness

## Date context (what may be outdated)
- Official Roblox Creator Docs items (2026-10) take priority on platform mechanics.
- Older 2020-2021 tips (Touched, BodyMovers era) are superseded by 2023-2024 advice favouring Raycast and constraints.
- 2D/2.5D tooling is new as of 2026-09.
- Age/safety-level guidance is recent (2026-10); verify current settings.
- The new items are dated 2026-03 (RoWatcher) and 2026-05 (StudioKrew). As of 2026-11-01 they are about 6–8 months old.
- Meme and brainrot trends decay quickly. Re-check whether Steal a Brainrot, Escape Tsunami For Brainrots, RIVALS and 99 Nights in the Forest still reflect current performance before citing them as examples.
- All four new items are indie or agency sources that are self-reported and low-advice. None are official Roblox guidance.
- T17686 (Roblox Newsroom [OFFICIAL], 2026-09) confirms the 2D and puzzle focus and the new engine features (orthographic camera, animated image containers, sprite-sheet import). This dates the existing '2D tooling and misc platform features' rule, so the rule is current as of 2026-11.
- New items are dated 2026-08 (Cumin) and 2026-10 (LovJak, MonarchDev). None conflict with existing rules, so no advice is superseded.
- LovJak's area-count advice is flagged low-advice and all four new items are indie, self-reported sources rather than official Roblox documentation.
- T18361 (2026-05) and T18264 (2025-06) are new additions; neither supersedes earlier advice in the file.
- Both new items are single indie, self-reported sources flagged low-advice, so treat them as lightly validated.

## Instructions for an agent using this file
- If designing horror, avoid large pure-dark areas, build tension gradually, and make objectives visible with neon.
- If adding projectiles, use Raycast by default; GetPartsInBox only for large linear projectiles.
- If implementing knockback or moving platforms, use constraints, not BodyMovers.
- If NPCs path or climb, disable unused Humanoid states and keep obstacles under ~3.5 studs.
- If building a tycoon, include build/upgrade choices beyond collect pads.
- If building PvE, scale difficulty by stage, vary enemy behaviours, and make the first boss teach mechanics.
- If building tower defense, add target priority modes and audit tower usage.
- If gating features by age/safety level, follow official per-genre guidance.
- If combat game spans platforms, consider mobile-only lobbies or balancing.
- If citing indie revenue or visit numbers, label them unverified.
- If a request involves a viral or meme-themed concept, plan retention and depth systems alongside the hook. Cite T17463 and T17471.
- If a request is for a competitive shooter, default to touchscreen-first calibration of controls, hitboxes and matchmaking. Cite T17477.
- If a request is for horror, add a survival loop before adding scares, and keep jump scares rare. Cite T17484 and the existing jumpscare rule.
- Label all figures from RoWatcher and StudioKrew as self-reported and indie. Do not present them as platform ground truth.
- Verify the current status of named example games before using them as evidence.
- If a chase or escape sequence has route choices, use visible cues to show wrong paths and never rely on invisible walls alone.
- If a map has many enemies, cap the count and give each enemy a distinct role before adding more.
- If a game has a single starting area, plan additional areas in the roadmap rather than treating the first zone as the full experience.
- If building an obby, sequence challenges by increasing difficulty and consider cooperative mechanics as a distinct layer.
- Treat all sources here as indie, self-reported advice unless verified against official Roblox documentation.
- If a proposed obby uses swinging mechanics, then require a swing physics and momentum playtest before adding it to the progressive obby library.
- If a genre needs effectively endless levels, then build procedural assembly from a small piece library instead of hand-authoring each level.
- If citing procedural or swing advice, then note it comes from a single self-reported indie source.

## Not covered here (research elsewhere)
- No concrete monetisation or economy balance numbers for tycoon/simulator.
- Little on racing, fighting, and roleplay mechanics beyond access settings.
- No retention/CCU benchmarks by genre.
- Tower defense wave design and obby checkpoint design not covered.
- Mobile controls and UI per genre barely covered.
- Horror sound design and lighting settings not covered.
- No official Roblox data on session length or retention by genre.
- No sample sizes or methodology behind the RoWatcher 8–12 min figure.
- No detail on how RIVALS calibrates hitbox forgiveness or matchmaking.
- No detail on the specific survival systems used in 99 Nights in the Forest.
- No longitudinal data on how long meme-driven games stay relevant after the novelty window.
- No monetisation or cost data for these genres.
- No concrete enemy-count caps or per-map enemy budgets were given; the recommended number is unknown.
- No guidance on how many areas to plan or when to release them after launch.
- No implementation details for shared-momentum or cooperative obby zones (scripting, physics, or detection approach).
- No official Roblox documentation was cited for invisible-wall collision, chase-route signage, or enemy AI limits.
- No source explains procedural generation specifics such as reachability validation, seeding, or piece-count guidance.
- No swing tuning values (gravity, damping, rope length, release windows) are given.
- No official Roblox documentation for procedural generation or swing-style physics is included in these additions.

## Quotes (near-verbatim)
- "the whole genre is seen a niche by most, mainly because its hard to capitalize off of roblox's young audience through a rather complicated base idea." ([Roblox DevForum 2025-01 ](https://devforum.roblox.com/t/i-made-a-planetaryspherical-gravity-system/3383865))
- "The map is getting pretty boring. You start in the first area, steal a couple of sheep, and eventually you've seen everything." ([LovJak 2026-10 2:46](https://youtu.be/YXcV0Ba0RJc?t=166))

## Verified additions

_Chunk 4 (2026-11-01). Labels: OFFICIAL / CORROBORATED / SINGLE-SOURCE / CONTRADICTED / OUTDATED-UNSURE. Hand-added rows kept in `youtube-learn/supplements/topics/genre-mechanics.md`; they survive rebuilds._

- **2D / 2.5D support** (OFFICIAL, RDC 2026 keynote, announcement): orthographic cameras, animated sprite containers, sprite sheet import and new UI primitives make 2D and 2.5D games easier. Rollout status not verified in docs (OUTDATED-UNSURE until checked).

## Appendix: every extracted tip on this topic

- 2020-09-17 Emancyphur [5:02](https://youtu.be/C0ybJ5ghSHk?t=302): Offer multiple modes that keep the same objective but change who the enemy is (bot, player-controlled, traitor, infection) to add replayability without new content.
- 2020-11-16 Roblox DevForum [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144): Combine sphere point generation with raycasting to build basic character or NPC vision for AI and obstacle avoidance.
- 2020-12-31 Roblox DevForum [page](https://devforum.roblox.com/t/the-ultimate-guide-to-vector3cross-and-vector3dot/953984): Dot can gate teleport-behind-player monsters so they only teleport when the player is not looking at them.
- 2021-07-04 SimTek Game Development [18:13](https://youtu.be/lJktfRT2pbg?t=1093): Pathfinding jump only clears about 3.5 studs in the speaker's test even though the character can jump higher; keep jumpable obstacles low or expect NPCs to get stuck.
- 2021-08-27 Last Level Studios [19:14](https://youtu.be/3djSOjdGaE8?t=1154): Destruction games with blow-up-and-upgrade loops (like Blow Stuff Up for Fun) are a proven format; Demolition Crew added combos and weapons.
- 2021-10-04 Roblox DevForum [page](https://devforum.roblox.com/t/creating-procedural-mountains-a-fractal-noise-tutorial/1494362): Use fractal noise (4 octaves, lacunarity 3, persistence 0.35) rather than single Perlin noise for mountainous terrain; single noise looks too flat.
- 2021-12-09 Last Level Studios [11:14](https://youtu.be/v_TGu45AD_g?t=674): Physics-based character rigs with grabbable ledges let players climb and solve platforming freely, a major Edgeworks draw inspired by Boneworks.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Include a little of each horror element: fear, shock, and disgust, even if Roblox limits some of them.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Turn happy, fun things scary (the FNAF-style cover-up approach) to mess with player expectations.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Use a range of common phobias (nyctophobia, arachnophobia, astraphobia, agoraphobia, mysophobia), not just darkness.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Use beings in distress (crying, screaming, panting) only when tied to the game's lore; placement matters.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Avoid overusing jumpscares; place them where players least expect them and only when they enhance the story.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Use uncanny-valley visuals (human-like but off) for monsters and environments to unsettle players.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Offer Normal, Hard, Extreme difficulties rather than Easy/Normal/Hard, since easy options feel less intimidating.
- 2021-12-10 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-make-a-terrifying-horror-game/1583917): Add easter eggs throughout the game and reward discovery with badges, hinting at them in the badges tab.
- 2022-04-25 Game Maker's Toolkit [8:16](https://youtu.be/Zrf1cou_yVo?t=496): Turn power growth into a puzzle of optimisation (Factorio, Satisfactory style) so progression rewards planning rather than repetition.
- 2022-07-03 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-use-roblox-pathfinding-service-20/1857779): Use the Animate script copied from a player character (or the uploaded Animate-R15/R6 scripts) under the NPC humanoid so it plays idle and run animations; convert to server script.
- 2023-02-03 SimTek Game Development [0:00](https://youtu.be/-sQHMwuVAu4?t=0): Use VectorForce and AngularVelocity constraints for knockback rather than legacy BodyMovers; both need an Attachment on the target's HumanoidRootPart.
- 2023-03-09 Roblox DevForum [page](https://devforum.roblox.com/t/guide-to-making-better-horror-experiences/2212571): Treat horror as a theme or style rather than a genre, and design mechanics around it.
- 2023-03-31 AlexDev [3:54](https://youtu.be/bYyD6tyz6Dg?t=234): Keep elemental status effects simple (burn, slow, chill, shock) rather than multi-step ailment chains, so players don't get confused by extra calculations.
- 2023-04-15 Roox4 [6:19](https://youtu.be/Pbrvfdn9UN8?t=379): Accidental bugs can spark design ideas; the creator turned a shotgun no-reload bug into a minigun enemy concept.
- 2023-07-07 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-create-a-realistic-npc-eyesight-system/2456522): Tag NPCs with 'NPC' and objects to detect with 'Detectable' via CollectionService; players are detected automatically. Detectable tag only works on Models with a valid PrimaryPart.
- 2023-09-24 VuukStudios [9:15](https://youtu.be/dcJtZnan7i8?t=555): For toggle-run on mobile, track a count (0/1) per tap and use a short task.wait before resetting so the stop tap does not immediately restart running.
- 2023-09-30 SimTek Game Development [0:00](https://youtu.be/6sgx1elbhwU?t=0): Use physics constraints (LinearVelocity) instead of tweening for moving platforms; forces are more realistic but can misbehave if parts are heavy or oriented oddly.
- 2024-06-24 Roblox DevForum [page](https://devforum.roblox.com/t/the-basics-of-combat-games-projectiles/3038332): Use Raycast for about 99% of projectiles; use GetPartsInBox only for large, mostly linear projectiles; avoid .Touched unless physics-heavy bouncing is needed.
- 2024-07-19 Mulch [4:06](https://youtu.be/y9Ii0VEFaEU?t=246): Use neon kill bricks for hazards so they stand out against the stage colors; avoid clashing color combos.
- 2024-10-12 GnomeCode [7:20](https://youtu.be/H9CbgCe47Mo?t=440): In horror, avoid large areas of pure darkness; it reads as frustrating on a 2D screen rather than scary.
- 2024-10-12 GnomeCode [8:02](https://youtu.be/H9CbgCe47Mo?t=482): Only give a flashlight if needed, and make it aim freely vertically; don't lock it to view height.
- 2024-11-17 ByteBlox [25:31](https://youtu.be/1KKQ6YrktTk?t=1531): In combat games, mouse/keyboard players beat mobile players at equal skill; consider mobile-only lobbies, as Blade Ball reportedly does.
- 2025-01-05 ByteBlox [1:05](https://youtu.be/K-KvVwt_Y4I?t=65): Build horror gradually: hint with small changes (slightly thicker fog each step) so players notice subconsciously, then give a sudden reveal at the end.
- 2025-01-05 ByteBlox [26:57](https://youtu.be/K-KvVwt_Y4I?t=1617): Keep the escape objective (find the final button) far from spawn but reachable, and make it visible in the dark, e.g., a neon part, instead of using highlights.
- 2025-01-15 Roblox DevForum [page](https://devforum.roblox.com/t/i-made-a-planetaryspherical-gravity-system/3383865): Space/planetary games are niche on Roblox because the base idea is complicated for a young audience; the author argues polish and playability are needed to bring the genre mainstream.
- 2025-05-11 Cumin [14:49](https://youtu.be/2auVezIcNAE?t=889): Vary dungeon designs so each feels unique; the speaker cites World Zero's dungeons as the most engaging part of Roblox RPGs.
- 2025-06-08 Cumin [3:55](https://youtu.be/Z1tj1OPOEZg?t=235): Make practice mode viable; a private server with clumped, unkillable AI titans gives no real practice.
- 2025-06-14 JustDucksey [3:26](https://youtu.be/XRvcKGSLr4g?t=206): Use procedural track and map generation to create effectively endless levels from a small set of pieces.
- 2025-07-11 PineappleDev [2:02](https://youtu.be/ggWeHThD_3Q?t=122): Play several successful games in your chosen genre, then combine their features and add one or two twists. Speaker presents this as a joke.
- 2025-07-31 Cumin [5:35](https://youtu.be/jXogdTgtlXE?t=335): In a movement-based game, design maps around the core movement; tall, reachable structures matter more than realism.
- 2025-07-31 Cumin [11:43](https://youtu.be/jXogdTgtlXE?t=703): Make PvE difficulty scale up across campaign stages; a flat difficulty with player power growth makes the late game trivial.
- 2025-07-31 Cumin [15:21](https://youtu.be/jXogdTgtlXE?t=921): Consider separating PvP from PvE modes so PvP players don't block campaign progress.
- 2025-08-31 Cumin [3:30](https://youtu.be/wdf6cfH3rnA?t=210): A tycoon with only a collect pad and no building loop lacks the depth players expect; add build or upgrade choices.
- 2025-09-06 Cumin [5:05](https://youtu.be/Jf2RvsWMPes?t=305): Shooters are harder to turn into pay-to-win cash grabs than simulators; gunplay must feel cohesive, which takes real effort to build.
- 2025-12-23 Cumin [11:57](https://youtu.be/hQpC_UHxJDU?t=717): Check whether the first boss can be cheesed by simply running. If so, players never learn the core mechanics the boss should teach.
- 2025-12-23 Cumin [5:57](https://youtu.be/hQpC_UHxJDU?t=357): Use a built-in bestiary showing defeated enemies and loot drop chances. The speaker called it a good resource that should be common.
- 2026-01-28 bubDEV [0:32](https://youtu.be/2lPsxPtj2mM?t=32): Reusing core loops proven engaging by successful games is a viable path; template games built on Escape Tsunami loops are earning.
- 2026-03-00 RoWatcher (tracker blog) [page](https://rowatcher.com/news/the-10-fastest-growing-roblox-games-in-march-2026): Wrap collection mechanics in viral meme aesthetics (brainrot); the page cites Steal a Brainrot and Escape Tsunami For Brainrots as proof of scale.
- 2026-03-00 RoWatcher (tracker blog) [page](https://rowatcher.com/news/top-10-roblox-games-by-players-march-2026-data-breakdown): Meme/viral games show huge visit spikes but average only 8–12 min sessions and normalize quickly after the novelty window; pair virality with deeper systems.
- 2026-04-03 ArTheDev [7:01](https://youtu.be/CnZEnFVAFSw?t=421): Use weighted random chances per weather type (e.g. sunny 40%, rain 20%, others 10%) rolled after each previous weather ends for varied but controllable weather.
- 2026-05-00 StudioKrew (agency blog, GGAID data) [page](https://studiokrew.com/blog/top-roblox-games-may-2026/): Competitive shooters should be calibrated for touchscreen first (controls, hitbox forgiveness, matchmaking), per RIVALS' approach.
- 2026-05-00 StudioKrew (agency blog, GGAID data) [page](https://studiokrew.com/blog/top-roblox-games-may-2026/): In horror, prioritise atmosphere and survival systems over cheap jump scares to earn longer sessions (99 Nights in the Forest).
- 2026-05-30 Cumin [4:20](https://youtu.be/tT-u3b6LMkQ?t=260): In an obby, test momentum and swing physics thoroughly; janky swing physics made the reviewer quit, despite swinging being a fun core mechanic.
- 2026-06-06 janisjanis01 [4:36](https://youtu.be/CltiB53QTHw?t=276): In tower defense, add target priority modes (closest, strongest, last) and a hotkey to toggle them; adds strategy.
- 2026-06-23 Raul [0:12](https://youtu.be/kKavvUDtHOg?t=12): Defense games: the creator says only two of several towers (Maya, Golem) were actually used, so balance or cut the rest.
- 2026-08-07 RoyalDev [5:28](https://youtu.be/RXmiJkaZWV4?t=328): Match the concept to the majority audience (largely children on mobile) rather than a very niche or hard audience.
- 2026-08-22 Cumin [6:21](https://youtu.be/rjPW4GeeyFg?t=381): Don't put invisible walls in chase sequences as the only way to signal wrong paths; players hit them and feel cheated.
- 2026-08-22 Cumin [11:14](https://youtu.be/rjPW4GeeyFg?t=674): Give each enemy a distinct purpose and limit enemy count per map; overlapping, crowded enemies make tension feel unfun.
- 2026-09-11 MonarchDev [0:40](https://youtu.be/LD7LGP10dRc?t=40): Don't misfile games: an RNG/idle-progression game belongs under Simulator, not RPG, as the creator learned after miscategorizing.
- 2026-09-11 Roblox Newsroom [page](https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play): 2D and puzzle games are a new focus; engine adds orthographic camera, animated image containers and sprite-sheet import for these genres.
- 2026-09-13 Cumin [8:11](https://youtu.be/kjLtxvB_iyk?t=491): Give enemies varied behaviours beyond walking straight at the player; single-note enemies lead to kiting into an AoE clump and nothing else.
- 2026-09-17 Roblox [11:39](https://youtu.be/3a2RbLOAl4A?t=699): 2D and 2.5D games are easier to build now with orthographic cameras, animated sprite containers, sprite sheet import and new UI primitives.
- 2026-10-15 LovJak [2:46](https://youtu.be/YXcV0Ba0RJc?t=166): Add more areas later because a single starting area gets exhausted quickly once players have seen everything.
- 2026-10-16 MonarchDev [5:46](https://youtu.be/hPWJlFwp5Xs?t=346): Ask for a library of obby challenges that get progressively harder, then add unique mechanics such as shared-momentum zones that reward cooperation.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/weapons-kit): Add a ChargeRate configuration value to make a weapon a charging weapon (e.g. Railgun or bow); DischargeRate defaults to 0.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/control-the-users-camera): HumanoidRootPart sits about 2 studs below the head, so add a height offset when aiming the camera at the character.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/npc-kit): Set soldier AttackMode to 1 (only SoldierEnemy-tagged targets), 2 (everything without SoldierFriend), or 3 (attack all characters).
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/performance-optimization/improve): Disable unused HumanoidStateTypes on NPCs with SetStateEnabled (e.g. Climbing unless NPCs climb ladders).
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system): Tag pickup models with Action, Pickup, WeaponPickup, WeaponSystemIgnore and one rarity tag so the system recognises them.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/security/device-trust): For competitive FPS, allow Unknown in casual only. Put Standard and Full in ranked. For fighting games, use separate or trusted servers. For racing, keep Unknown and None off leaderboards.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/security/device-trust): For idle or tycoon games, withhold AFK rewards from None but not Unknown. For trade hangouts, block trading only at None. Roleplay or social games can give full access to all levels.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/basic-scripting/fading-trap): Duplicate fading platforms across wider gaps and adjust fade speed to tune obstacle difficulty.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/lesson-plans/roblox-developer/roblox-developer-4): Support multiple harvestable items by adding a BoolValue named CanHarvest set to true on each item.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/developer/planning-for-educational-settings): For younger students focus gameplay on one task at a time such as a simple quest; older students can handle simultaneous tasks.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/choose-an-art-style): Embrace genre iconography symbolism (e.g. sword for strength, beaker for magic) so players understand icons without guidance.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/chat/voice-chat): For team-only voice, use AudioDeviceInput.AccessType and SetUserIdAccessList, updating the allowed list on Team PlayerAdded/PlayerRemoved.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/templates): Extend Laser Tag's simple round system with custom modes and scoring for a faster FPS prototype.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/avatar-settings): Use the Consistent Gameplay preset (same height and box collider) when collision consistency matters, rather than Player Choice.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/debounce): Apply the same cooldown pattern to weapon limits, such as a rocket launcher reload time, to cap how often players can fire.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/performance-optimization/microprofiler/tag-table): Disable unneeded Humanoid states (e.g. Climbing, Swimming) on NPCs that don't need them to cut stepHumanoid cost.

Index: [[README]] | Master: [[master-playbook]]
