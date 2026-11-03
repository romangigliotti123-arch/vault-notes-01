---
title: TheDankDeveloper - How to make successful Roblox games
tags: [roblox, thedankdeveloper, playbook]
videos: 39
generated: 2026-10-29
credibility: insufficient
credibility_score: n/a
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# TheDankDeveloper - How to make successful Roblox games

TheDankDeveloper is a hobbyist dev whose advice is light and mostly experiential: pick a simple, finishable genre (simulator, obby, clone of a trending game), plan monetisation up front, build fast with templates and AI (Lemonade, later Claude + Studio MCP + Forge GUI), playtest with fans and fix bugs before spending on ads, test two thumbnails, and keep shipping. His own cash-grab tests show ads rarely pay back quickly (about break-even at best), so expect small returns and treat each game as practice.

**Style:** Casual, experiment-driven devlogs and timed challenges (1-hour clones, 7-day builds) showing real, often disappointing numbers. Heavy on AI-assisted prototyping workflows. Suits beginners and solo devs wanting fast prototypes and honest cash-grab and ad-ROI reality checks, not deep design or retention theory.

## Playbook
1. **Pick a simple, finishable idea** [[game-ideas-and-genres]]: Choose a role first, then a first game you can finish: a simulator or obby rather than FPS. Plan concept, build list and monetisation upfront. In crowded genres like tower defense, differentiate deliberately.
2. **Ride trends with a twist** [[trend-research-and-validation]]: Clone a booming format (RNG, Steal An Egg, Grow a Garden style) and add a theme twist, e.g. YouTuber rarities. Ask the AI for ideas based on your existing project. Don't republish others' games.
3. **Prototype fast with templates and AI** [[ai-and-tools]]: Use the Generate a Simulator plugin or AI tools (Lemonade, Claude Code with Studio MCP) to script core mechanics, then reskin art, UI and map. Prompt in small steps, give a reference game or screenshot for UI.
4. **Time-box and cut scope** [[development-process-and-speed]]: Use hard time limits (1 hour to 7 days), split work between collaborators, and keep a final ~10-minute buffer for bug fixing. AI code often errors on first run; paste errors back to fix.
5. **Make the core loop fun with a currency** [[core-loops-and-game-design]]: An obby alone isn't enough; add a currency to buy fun things. Balance drop rates, scale difficulty, use hold-to-jump, and cap pet and egg counts to avoid exploits.
6. **Make visuals cheap but polished** [[building-art-and-assets]]: Use low-poly Blender models with a shared palette, and Lighting effects (Atmosphere, Blur 4, ColorCorrection, SunRays, skybox) for a cartoon look. Sound and music add polish. Use Scale not Offset for UI.
7. **Plan monetisation** [[monetisation-other]]: Plan gamepasses and shop items before building (about 10 areas and 7 items for his clicker). Only the Robux spin wheel sold in his test, so prioritise offers players actually buy.
8. **Playtest before launch** [[playtesting-and-feedback]]: Test with a fan group or Discord playtest: it exposed exploits, an invisible wall and group-gate bugs. Check shops and soft shutdown before paying for ads. Keep value logic server-side.
9. **Make icon and thumbnails** [[thumbnails-icons]]: Make two thumbnails and A/B test click-through rate. Outsourcing part of the icon is fine (his took nearly 2 hours).
10. **Launch with a small ad test** [[ads-and-sponsored-experiences]]: Run a small visits campaign: about 10 credits, US and Canada, console off, max bid 0.01. Expect roughly break-even at best: 3,135 Robux gave 182 Robux from players; 2,800 gave about 1,200.
11. **Promote socially and build community** [[social-features-and-virality]]: Post short TikToks during development, do playtest livestreams, link a Discord in the description, and crowdsource feature ideas from viewers.
12. **Measure honestly** [[analytics-metrics]]: Use Creator Dashboard analytics (90-day range) and exclude your own purchases. Net equals gross minus ad spend.
13. **Update and keep shipping** [[updates-live-ops]]: Plan post-launch content, which he expects helps the algorithm. Expect low returns from cash grabs, don't be discouraged by a flop, and keep shipping.

## Key numbers
- Blur size 4; Atmosphere density 0.269; ColorCorrection brightness/contrast/saturation 0.1/0.1/0.8
- Blender border start: 8-sided cylinder
- Ad test: 3,135 Robux spent, 1,600 visits, 182 Robux player revenue, net -2,953 (2024-07)
- Same game peaked 400+ concurrent; 78 group members
- Cash grab 90-day: over 5,500 gross, 10.72 credits (~2,850 Robux) ad spend, ~2,714 net (2024-09)
- 2025 ad test: 10 credits, 2,654 visits, ~2,800 Robux spent, ~1,200 earned; 20 credits cost 5,700 Robux
- Recommended ad setup: US and Canada, console unchecked, max bid 0.01
- Game icon took nearly 2 hours
- Talent Hub example: 5,000 Robux scripter commission
- Challenge builds: 1 hour; 24-hour contest; 7-day AI cash grab; Geometry Dash in 1.5 hours
- Claude usage: simple prompt ~1% of session; Max first prompt 23% of 5-hour limit; Pro hit 100% and reset in ~1h34m
- Tower defense playtest overwhelmed by round 9
- Kill part damage 20% of health per step
- Streak bonus +10% per perfect hit

## Common mistakes
- Assuming a sponsored campaign will pay back (3,135 Robux spent, 182 recovered)
- Running ads before playtesting (broken gem shop and missing soft shutdown found after launch)
- Unbounded egg or pet purchases causing infinite pets, lag and exploits
- Client-side currency and values that are easy to exploit
- Not anchoring parts and towers
- Copying or republishing others' uncopylocked games
- Accepting AI UI or code without checking fit, parent folder, unlock logic or errors
- Overly complex first game, or an obby with no currency or reward
- No enemy scaling, so towers were overwhelmed by round 9; counting your own purchases as revenue
- Quitting after a first flop

## Launch checklist
- [ ] Concept, build list and monetisation plan written
- [ ] Core loop has a currency and rewards
- [ ] Rarity and drop rates balanced; pet and egg caps set
- [ ] Values and currency handled on the server
- [ ] Parts anchored; hazards use invisible hitboxes
- [ ] UI uses Scale and is checked on device previews
- [ ] Bigger buttons and text for mobile
- [ ] Group-gated or other gated access tested for members
- [ ] Shops and gamepasses tested; soft shutdown added
- [ ] Playtest with fans or Discord and fix bugs
- [ ] Two thumbnails made for CTR A/B test
- [ ] Discord link in the description
- [ ] Small ad campaign set (10 credits, US and Canada, bid 0.01)
- [ ] TikTok clips posted
- [ ] Analytics checked excluding own purchases
- [ ] Post-launch update plan ready

## How the advice changed over time
- 2023 to 2024: low-poly Blender, Studio tutorials, and one-hour clone challenges, with mostly beginner advice to finish a simple game and plan monetisation.
- 2024 to 2025: cash-grab ad experiments with real numbers; conclusion that ads rarely pay back quickly.
- 2025 to 2026: shift to AI scripting with Lemonade (ChatGPT/Gemini comparisons). By late 2026 he uses Claude (Pro/Max) with Studio MCP, Blender MCP and Forge GUI, and tracks usage limits. Prefer this newer AI workflow over hand-scripting.

## Theme notes
- [[TheDankDeveloper - Retention|Retention]]
- [[TheDankDeveloper - Monetisation|Monetisation]]
- [[TheDankDeveloper - Discovery & Algorithm|Discovery & Algorithm]]
- [[TheDankDeveloper - Game Ideas|Game Ideas]]
- [[TheDankDeveloper - Thumbnails & Icons|Thumbnails & Icons]]
- [[TheDankDeveloper - Updates & Live Ops|Updates & Live Ops]]
- [[TheDankDeveloper - Studio & Scripting|Studio & Scripting]]
- [[TheDankDeveloper - Mindset & Process|Mindset & Process]]
- [[TheDankDeveloper - Games Mentioned]]
- [[TheDankDeveloper - Numbers & Benchmarks]]
- [[TheDankDeveloper - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2023-04-14 - How To Make Low Poly Roblox Borders in Blender (Blender Tutorial)|How To Make Low Poly Roblox Borders in Blender (Bl]] (5,047 views, 2023-04-14): Build low-poly terrain borders from an 8-sided cylinder, separate parts, and color with a palette gradient.
- [[2023-04-15 - How to Import Meshes into Roblox Studio! (Roblox Studio)|How to Import Meshes into Roblox Studio! (Roblox S]] (4,194 views, 2023-04-15): Export FBX from Blender and bulk import via Asset Manager, leaving Import as One Mesh unchecked.
- [[2023-04-28 - How to use Unions in Roblox Studio (Roblox Studio)|How to use Unions in Roblox Studio (Roblox Studio)]] (1,533 views, 2023-04-28): Unions combine parts; negate parts carve holes and corners.
- [[2023-05-12 - How To Texture in Blender (Blender Tutorial)|How To Texture in Blender (Blender Tutorial)]] (764 views, 2023-05-12): Texture in Blender with a palette image via project from view UVs; Studio texturing is weaker.
- [[2023-05-12 - How to TURN ON Dark Mode in Roblox Studio (2023)|How to TURN ON Dark Mode in Roblox Studio (2023)]] (1,277 views, 2023-05-12): Switch Studio to dark mode under File > Studio Settings > Theme.
- [[2023-05-14 - How to make 3D Text in Roblox Studio (Roblox Studio)|How to make 3D Text in Roblox Studio (Roblox Studi]] (42,055 views, 2023-05-14): Make 3D text with the free 3D Text 2 plugin.
- [[2023-06-01 - How to make your Roblox Game 10X Better!|How to make your Roblox Game 10X Better!]] (24,363 views, 2023-06-01): Cartoon look via Atmosphere, Blur 4, ColorCorrection, SunRays and a skybox.
- [[2023-06-08 - Blender Basics - Blender Beginner Tutorial|Blender Basics - Blender Beginner Tutorial]] (2,668 views, 2023-06-08): Beginner Blender basics ending with a mug model.
- [[2023-06-25 - Making A Roblox Tower Defense Dev Log 1|Making A Roblox Tower Defense | Dev Log 1]] (64,605 views, 2023-06-25): Tower defense dev log: pathing, waves, enemies, with viewer-suggested features.
- [[2023-07-10 - Making a Roblox Tower Defense with your comments Dev Log 2|Making a Roblox Tower Defense with your comments |]] (16,957 views, 2023-07-10): Tower defense update: tower placement with rotation, themed enemies, remade Blender map, viewer input.
- [[2023-07-26 - 6 Roblox Devs Make a Game in 1 Hour|6 Roblox Devs Make a Game in 1 Hour]] (4,067 views, 2023-07-26): One-hour challenge yielding a Subway Surfers-style highway game; entertainment mostly.
- [[2023-08-06 - How to Change Roblox Studio Icons|How to Change Roblox Studio Icons]] (4,090 views, 2023-08-06): Swap Studio toolbar icons using a custom icon directory pack.
- [[2023-10-14 - Making Blade Ball in 1 HOUR in ROBLOX|Making Blade Ball in 1 HOUR in ROBLOX]] (536,431 views, 2023-10-14): One-hour Blade Ball remake; scripting struggles and last-minute bug fixing.
- [[2023-10-20 - How to become a ROBLOX Developer and make ROBUX!|How to become a ROBLOX Developer and make ROBUX!]] (20,192 views, 2023-10-20): Pick a role, find work via Talent Hub, then finish a simple monetised first game with a currency.
- [[2023-10-25 - Making a Tower Defense Game in 1 HOUR in ROBLOX|Making a Tower Defense Game in 1 HOUR in ROBLOX]] (19,931 views, 2023-10-25): One-hour tower defense: split work, but towers were overwhelmed by round 9.
- [[2023-10-29 - How to make Floating Text in ROBLOX Studio!|How to make Floating Text in ROBLOX Studio!]] (59,749 views, 2023-10-29): Floating text with BillboardGui; use scale sizing so it doesn't grow with distance.
- [[2023-11-17 - I STOLE Roblox Games|I STOLE Roblox Games]] (3,348 views, 2023-11-17): Uncopylocked games can be studied for learning, but don't copy or republish them.
- [[2023-12-12 - Making Pet Simulator 99 in 1 HOUR in ROBLOX|Making Pet Simulator 99 in 1 HOUR in ROBLOX]] (6,474 views, 2023-12-12): One-hour Pet Sim clone exposed unbounded egg spam and client-side exploit risk.
- [[2024-01-09 - Roblox Developer tries Fortnite UEFN|Roblox Developer tries Fortnite UEFN...]] (5,808 views, 2024-01-09): Tried UEFN for a dirt-bike map; a tool comparison, not growth advice.
- [[2024-04-16 - I made a Roblox RNG Game in 10 DAYS|I made a Roblox RNG Game in 10 DAYS...]] (34,413 views, 2024-04-16): Ten-day RNG game riding the trend with a YouTuber twist; icon took nearly 2 hours.
- [[2024-07-16 - How much Robux do Roblox Cash Grabs make|How much Robux do Roblox Cash Grabs make?]] (610,625 views, 2024-07-16): Plugin cash grab with 3,135 Robux of ads earned 182 Robux, a net loss of 2,953.
- [[2024-09-17 - How much my Roblox Cash Grab Made... roblox robloxdevs|How much my Roblox Cash Grab Made... #roblox  #rob]] (547,740 views, 2024-09-17): Cash grab grossed over 5,500 Robux in 90 days, about 2,714 net after ads.
- [[2024-10-05 - Best Roblox Game WINS $10,000 Robux|Best Roblox Game WINS $10,000 Robux]] (8,100 views, 2024-10-05): 24-hour dev contest won on fun, polish and expansion potential; sound mattered.
- [[2025-02-11 - Top 5 Roblox Studio Plugins! shorts|Top 5 Roblox Studio Plugins! #shorts]] (91,068 views, 2025-02-11): Five useful plugins: Easy Textures, Archimedes, 3D Text, Brush Tool, simulator generator.
- [[2025-04-12 - Is this Engine easier than Roblox 🤔 programming jamango|Is this Engine easier than Roblox? 🤔 #programming ]] (14,145 views, 2025-04-12): Promo for Jamango, a no-code browser game engine; no Roblox advice.
- [[2025-08-20 - I made a Roblox Cash Grab with AI|I made a Roblox Cash Grab with AI]] (514,122 views, 2025-08-20): AI-scripted tower obby with a 10-credit ad campaign recovered about half of ad spend.
- [[2025-09-23 - Can I Make a ROBLOX Game Using 0 Effort|Can I Make a ROBLOX Game Using 0 Effort]] (13,775 views, 2025-09-23): Near-zero-effort game: ChatGPT idea, Lemonade scripting, quick fan playtest.
- [[2025-12-02 - I Remade Geometry Dash in Roblox|I Remade Geometry Dash in Roblox]] (7,805 views, 2025-12-02): Geometry Dash remade in 1.5 hours with AI; hold-to-jump improved feel.
- [[2026-01-09 - ChatGPT vs Lemonade Remake Fish It|ChatGPT vs Lemonade Remake Fish It]] (74,498 views, 2026-01-09): Same Fish It prompt: Lemonade beat ChatGPT in head-to-head AI build.
- [[2026-01-27 - Claude vs Lemonade Remake The Forge|Claude vs Lemonade Remake The Forge]] (41,666 views, 2026-01-27): Lemonade built a working Forge remake; Claude broke after combat was added.
- [[2026-01-28 - why is roblox development so hard 😭 robloxrobloxstudio|why is roblox development so hard 😭  #roblox#roblo]] (28,984 views, 2026-01-28): A 13-second Short lamenting how hard Roblox development is.
- [[2026-04-11 - I remade my Roblox GUI's with AI|I remade my Roblox GUI's with AI]] (12,343 views, 2026-04-11): Forge UI generates GUI variants; check style fit before committing.
- [[2026-04-17 - How to make Signs and Floating Text in Roblox Studio roblox robloxstud|How to make Signs and Floating Text in Roblox Stud]] (7,962 views, 2026-04-17): Signs via SurfaceGui and floating text via BillboardGui.
- [[2026-04-19 - Gemini vs Lemonade Remake Grow a Garden|Gemini vs Lemonade Remake Grow a Garden]] (30,115 views, 2026-04-19): Lemonade beat Gemini at a Grow a Garden remake built feature by feature.
- [[2026-05-25 - I Made a Roblox Game using Cards|I Made a Roblox Game using Cards]] (18,377 views, 2026-05-25): Sponsored demo of Lemonade cards building a survival game by prompting.
- [[2026-10-06 - I made a Roblox Cash Grab in 7 Days|I made a Roblox Cash Grab in 7 Days]] (67,085 views, 2026-10-06): Seven-day Claude-built cash grab: A/B test two thumbnails, run ads, TikToks and livestream playtests.
- [[2026-10-13 - How to make Roblox Games Using Claude|How to make Roblox Games Using Claude]] (166,605 views, 2026-10-13): Claude Code with Studio MCP: small prompts, a reference game for UI, and Blender MCP for models.
- [[2026-10-21 - I Remade Steal An Egg with AI|I Remade Steal An Egg with AI]] (30,583 views, 2026-10-21): Steal An Egg cloned mechanic by mechanic with Claude Opus, despite bugs and usage limits.
- [[2026-10-23 - I Paid AI $100 to make a Roblox Game|I Paid AI $100 to make a Roblox Game]] (60,795 views, 2026-10-23): Claude Max plus Forge GUI built a parkour system and lava tower race in about an hour.
