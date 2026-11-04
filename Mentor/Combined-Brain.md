---
tags: [moc, mentor, combined-brain]
description: "The vault's combined brain: working principles, methods, decision rules and disagreements of every creator in both vaults (Roblox creators weighted by trust, plus Nate Herk, RoboNuggets and Andrej Karpathy), organised by job, each rule linked to its source notes."
---
# Combined brain

Generated from `claude-library/mentor/combined-brain.md` (hand-written spine) plus rules extracted from the Roblox knowledge base and the AI-creators research by `tools/mentor_brain.py`. Do not edit here. Used by the `mentor-rbxdev-vault` agent and the `/mentor-rbxdev-vault` skill.

## How to read this note (cheap order)

1. Read **Trust and weighting** and the **Job index** below (about 70 lines). Stop there unless the job needs more.
2. Jump to the one job section you need (search for its `## Job:` heading). Each has: spine (principles), top evidence rules with trust labels, disagreements, and what to use.
3. Open at most two of the linked source notes. Cite the note path for every fact.

## Trust and weighting

- **Roblox creators** are weighted by the credibility audit (`creator-credibility`, 92 creators): `T` = TRUSTED (score 7.5+, usable as a primary source), `M` = MIXED (confirm with a second source), `?` = INSUFFICIENT or not audited (unknown, not bad), `W` = WEAK (never the sole source). `official` = Roblox, Roblox Creators, Creator Docs or DevForum. Official 2026 docs override older indie advice on mechanics, metrics and payouts. Indie revenue and CCU figures are self-reported and unverified.
- **Rule filter used below:** a rule from the knowledge base is shown only if at least one official or TRUSTED source backs it, or a MIXED source plus a second source. Rules resting only on WEAK, INSUFFICIENT or unaudited creators are left out of this note (they stay in the topic files, flagged there).
- **AI creators** (Nate Herk, RoboNuggets, Andrej Karpathy) are not credibility-audited. Their notes tag each point `[demonstrated]` (shown working on screen) or `[opinion]` (advice or claim). Income and earnings claims in their videos are marketing, not evidence. Karpathy's coverage here is the educational series and the LLM talks (15 usable videos); his Software 3.0 / agents / vibe-coding talks are not in the vault, so none of that is claimed.
- Advice is dated. Prefer newer sources, flag anything older than about 12 months, and say "KB gap" when the vault has nothing.

## Job index

| Job | Section | Start with |
|---|---|---|
| Designing a game | Job: designing a game | `/game-dev-workflow`, `/game-dev-rate`, `/roblox-game-ideas` |
| Scripting and Luau | Job: scripting and Luau | `/roblox-luau-style`, `/roblox-remote-security`, agent `roblox-luau-engineer` |
| Monetisation | Job: monetisation | `/roblox-monetisation-setup`, `/roblox-monetization-audit`, agent `roblox-economy-designer` |
| Ads, thumbnails, packaging | Job: ads, thumbnails and packaging | `/game-dev-ads`, `/game-dev-thumbnail`, `/roblox-ad-campaign-planner` |
| Retention and analytics | Job: retention and analytics | `/roblox-analytics-review`, `/roblox-metrics-benchmarks`, agent `roblox-game-doctor` |
| Live-ops | Job: live-ops | `/game-dev-update`, `/roblox-leaderboards-and-events`, agent `roblox-liveops-planner` |
| 3D models and Blender | Job: 3D models and Blender | `/rbx model-rebuild`, `/rbx accessory-fitting-guide`, `/rbx rig-checker` |
| Running a game project | Job: running a game project | `/game-dev-plan`, `/game-dev-playtest`, `/roblox-launch-checklist` |
| Using agents and skills | Job: using agents and skills | `/use-ai-library-rbxdev-vault`, `/manager-mode-rbxdev-vault`, `/clarify-before-build-rbxdev-vault` |
| Coding with AI | Job: coding with AI | `/karpathy-coding-guidelines-rbxdev-vault`, agent `claim-verifier-rbxdev-vault`, `/rate-anything-1-10-rbxdev-vault` |
| Research | Job: research | `/deep-topic-research-rbxdev-vault`, `/roblox-trend-research`, agent `claim-verifier-rbxdev-vault` |
| Running a project with agents | Job: running a project with agents | `/manager-mode-rbxdev-vault`, `/low-usage-mode-rbxdev-vault`, `/clarify-before-build-rbxdev-vault` |
| "What would <creator> do?" | Creator cards | the cards at the end of this note |

## Job: designing a game

**Spine (consensus of official sources and TRUSTED creators; see [[master-playbook]]):**
- Build small, validate demand first. If you cannot say the game in one sentence and name its audience, do not build it yet. Study growing mid-size games, not front-page giants. A beginner makes 10 to 20 small games, not one dream game.
- Define the three-layer core loop and prove it with a graybox MVP, one mechanic at a time. The first 2 minutes and D1 retention decide everything after; get the player into the core action within seconds and teach one mechanic at a time.
- Plan the economy (sources and sinks) and accessibility at design time, not after launch. Mobile and low-end devices are the default test target.
- If a pivot is needed, decide early: no traction after early iterations means pivot or kill; a live game with an audience is not abandoned.
- Social design: never split friends into isolated servers or penalise solo players (official). Packaging text: literal title, at most 2 emojis, thumbnail 1920x1080 (official; critic-checks).
- Official docs beat indie advice on platform mechanics. Nobody knows for certain what will sell; validation reduces risk, it does not remove it.

**Use:** `/game-dev-workflow` (idea, rating, plan, build), `/game-dev-rate`, `/roblox-game-ideas`, `/roblox-gdd-template`, `/roblox-trend-research`; agent `roblox-game-designer`. Notes: [[core-loops-and-game-design]], [[game-ideas-and-genres]], [[trend-research-and-validation]], [[first-session-onboarding]], [[player-psychology-and-game-feel]], [[common-mistakes]].

**Evidence (top rules, trust-labelled; source topic note in brackets):**

- `official` **Define one core loop and make it fun before anything else**: The core loop is the most repeated minute-to-minute action. (multiple-creators; Roblox Creators) [[core-loops-and-game-design]]
- `official` **Break the core loop into three parts**: Roblox defines it as minute-to-minute interaction, the most repeated set of actions, and a progression engine that drives the player forward. (multiple-creators; Roblox Creator Docs, Roblox Creators) [[core-loops-and-game-design]]
- `M` **Don't invent a new genre; start from a proven loop**: Several creators say to take a working formula and add your own twist. (multiple-creators; VuukStudios, janisjanis01, rasdev) [[game-ideas-and-genres]]
- `T` **Change at least ~20% of the reference game; change more for bigger reach**: Tizzy and AlvinBlox use an 80/20 rule: keep 80-90% familiar and change 10-20%. Tizzy says 20% is enough for 5-10K CCU (self-reported). (multiple-creators; Tizzy) [[game-ideas-and-genres]]
- `M` **Get players into fun within seconds**: Attention is short (about 8-10 s per rasdev; 10 s per AlvinBlox). (multiple-creators; SmartyRBX, rasdev) [[first-session-onboarding]]
- `official` **Deliver fun and clarity within defined windows**: Official docs: fun within 5 minutes or less. (multiple-creators; Roblox Creator Docs, Tizzy) [[first-session-onboarding]]

*6 rules shown here; 26 more rules in these topics were not shown because they lack an official or TRUSTED source (or two MIXED ones); they remain in the topic notes with their flags.*

**Where sources disagree (check the topic note before choosing):**

- **Exponential/fast number progression versus honest progression** ([[core-loops-and-game-design]]): MoseyTube and rasdev `?`: keep progression fast, with huge numbers going up / ByteBlox `T`: don't fake progression with x2/x3 costs when content is thin / CORSO `M`: exponential costs that take months feel unwinnable
- **Original vs proven idea** ([[game-ideas-and-genres]]): rasdev `M`, RoyalDev `T`, VuukStudios `M`, Tizzy `T`: build on proven concepts / Daiorg `M`: just make something original; trends and ambition matter less / Roblox DevForum 2021 and 1Coal 2023 `official`: be original/unique
- **Tutorial or no tutorial** ([[first-session-onboarding]]): rasdev `M`, AlvinBlox `T`, SmartyRBX `M`, VuukStudios (T13426) `?`: avoid tutorials, drop players into fun

## Job: scripting and Luau

**Spine:**
- Never trust the client (see [[anti-exploit-and-security]], [[client-server-and-remotes]]): validate every client-sent argument on the server (type, nil, range, instance class and location), keep authoritative logic in server-only containers, re-verify context and economy on the server before granting rewards, rate-limit per player on the server, send minimal identifiers and let the server look things up. Purchases need correct `ProcessReceipt` handling.
- Save data defensively (see [[data-persistence]]): wrap every DataStore call in `pcall`, one table per player keyed by `UserId`, give new players defaults, never overwrite saved data after a failed load, save on `PlayerRemoving` and again in `BindToClose` (all players in parallel within the shared 30 s).
- Measure before optimising: 60 FPS target (under 16 ms CPU per frame), reuse meshes, stream large maps, clean up connections.
- Prompt AI per feature, playtest after each prompt, paste errors back to fix them (see the coding-with-AI job).
- When the KB conflicts with current Creator Docs, the docs win; check deprecations.

**Use:** `/roblox-luau-style`, `/roblox-architecture-choice`, `/roblox-remote-security`, `/roblox-datastore-safe-save`, `/roblox-performance-pass`, `/roblox-rojo-project-setup`, `/roblox-code-rate`, `/roblox-npc-pathfinding`, `/roblox-ui-responsive`; agents `roblox-luau-engineer`, `roblox-luau-reviewer`. Notes: [[luau-language-and-types]], [[scripting-and-performance]], [[client-server-and-remotes]], [[data-persistence]], [[anti-exploit-and-security]], [[code-architecture-and-frameworks]].

**Evidence (top rules, trust-labelled; source topic note in brackets):**

- `official` **Validate every client-sent argument on the server**: Check type, nil, numeric range, string length, and that each Instance argument exists and is the expected class and location (FindFirstChild, IsDescendantOf). (multiple-creators; B Ricey, Roblox Creator Docs, Roblox DevForum) [[anti-exploit-and-security]]
- `official` **Never rely on client-side security, client anti-cheat, or client kicks**: Client checks can be disabled, spoofed via __index or __namecall hooks, or deleted. (multiple-creators; Roblox DevForum) [[anti-exploit-and-security]]
- `official` **Wrap every DataStore call in pcall and check the result**: Applies to GetAsync, SetAsync, UpdateAsync, IncrementAsync and MemoryStore Subscribe/Publish. (multiple-creators; B Ricey, Roblox DevForum) [[data-persistence]]
- `official` **Store each player's data as one table under one key, keyed by UserId**: One DataStore key per player means one write per player. (multiple-creators; B Ricey, Roblox Creator Docs, Roblox DevForum) [[data-persistence]]
- `official` **Validate everything on the server**: Clients can send arbitrary values even with server authority. (multiple-creators; Leif, Roblox, Roblox Creators, TheDankDeveloper) [[scripting-and-performance]]
- `T` **Debounce/cooldown remotes and reward mechanics**: Add server-side cooldowns to ability/slap remotes (e.g. (multiple-creators; ItsZyonic, Leif, MoseyTube) [[scripting-and-performance]]

*6 rules shown here; 28 more rules in these topics were not shown because they lack an official or TRUSTED source (or two MIXED ones); they remain in the topic notes with their flags.*

**Where sources disagree (check the topic note before choosing):**

- **Client-side anti-cheat value** ([[anti-exploit-and-security]]): Roblox DevForum Q946 (2023) and T5796 `official`: client AC is good, especially combined with server AC. / Roblox DevForum Q920 `official`, Q925 `?`, T5611 (2021 to 2022) and Roblox Creator Docs T9127 `?`: client-based detection is bypassable and must not drive bans. / Consensus `?`: client AC is only a supplement; server validation is primary (T9130, T5792).
- **Write method: SetAsync vs UpdateAsync** ([[data-persistence]]): B Ricey (2021 `T`, T5563) `?`: SetAsync is fine for simple overwrite saves; UpdateAsync is optional. / B Ricey (2024 `T`, T5968) `?`: production saves should use UpdateAsync; SetAsync only for demos. / DevForum (2020-2021 `?`, T5341 `?`, T5521) `?`: use UpdateAsync only for session-locked saves.
- **Client vs server hit detection** ([[scripting-and-performance]]): RobloxOfficial 2018 `?`: favor active attacker with client-driven logic (T66); RobloxCreators 2022: FPS client detection with server c... / RobloxOfficial 2018 `?`: competitive games should move hits to server (T72) / Roblox 2026 `official`: server authority gives latency compensation without custom code (T2186, T3124), reducing the tradeoff

## Job: monetisation

**Spine:**
- Repeatable value is a developer product; a permanent perk is a game pass (keep passes to about 2 to 6). Official sources and several TRUSTED creators agree products usually earn more.
- Drive the first purchase: a cheap, time-limited starter offer after the tutorial or first milestone, not in the first 30 seconds. Offer at the moment of need.
- Never sell what removes challenge, breaks competitive balance or gates core progress (official stance). Pay-to-win in competitive games is an unverified counter-view.
- Price from comparables and test live. Use Price Optimization only with scripted prices and enough transactions (about 60k per 30 days).
- One server `ProcessReceipt`, `PurchaseGranted` only after the grant; cheapest tier 25-100 Robux; offers to players in their first 10-30 minutes cheap or hidden (official, mixed).
- Run sales rarely; frequent sales train players to wait. Keep hard currency scarce and protect the economy.

**Use:** `/roblox-monetisation-setup`, `/roblox-monetization-audit`; agents `roblox-economy-designer`, `roblox-monetization-consultant`. Notes: [[monetisation-devproducts]], [[monetisation-gamepasses]], [[monetisation-other]], [[pricing]], [[ugc-and-avatar-economy]], [[business-and-payouts]].

**Evidence (top rules, trust-labelled; source topic note in brackets):**

- `T` **Use developer products for anything repeatable; game passes for one-time perks**: Dev products can be bought many times, so spend is uncapped. (multiple-creators; AlvinBlox, kra_DeZ) [[monetisation-devproducts]]
- `T` **Convert one-time passes into consumables where possible**: Turn permanent perks such as 2x offline earnings into a rebuyable product, so it recurs every login/day. (multiple-creators; MoseyTube, Tizzy) [[monetisation-devproducts]]
- `official` **Never gate core progress or the game behind a paywall**: Passes should be optional extras. (multiple-creators; Roblox, Roblox Creators, Roblox DevForum) [[monetisation-gamepasses]]
- `official` **Don't sell items that remove challenge or fix a loss**: Items that remove challenge disengage players and they eventually leave. (one-creator-repeated; Roblox DevForum) [[monetisation-gamepasses]]
- `official` **There is no pricing formula: start, observe, adjust**: Pick a starting price, lower it if few buy, raise it on the next version. (multiple-creators; Roblox) [[pricing]]
- `official` **Test prices with live data on your own audience**: Don't copy competitor prices; test to maximise volume × price. (multiple-creators; Roblox, Roblox Creator Docs, Roblox Creators) [[pricing]]

*6 rules shown here; 60 more rules in these topics were not shown because they lack an official or TRUSTED source (or two MIXED ones); they remain in the topic notes with their flags.*

**Where sources disagree (check the topic note before choosing):**

- **Selling currency packs** ([[monetisation-devproducts]]): TheDevKing `M`, Roblox Creators `official`, Roblox DevForum `official`: sell spendable currency, tiered with best-value tags. / Alex Builds Games `T`: currency packs are weak (D tier); sell direct items instead. / Tizzy `T`: selling cash packs early likely hurt his economy.
- **Pay-to-win vs cosmetics/convenience** ([[monetisation-gamepasses]]): Alex Builds Games `T`: pay-to-win packs are S-tier in competitive games (unverified) / Roblox Creators `official`, Roblox DevForum `official`, AlvinBlox `T`, SmartyRBX `M`, CallMeDogey `T`: avoid pay-to-win

## Job: ads, thumbnails and packaging

**Spine:**
- Fix retention before ads. Do not use ads to rescue a weak game. Then seed with a modest burst (about $5 to $20 a day for 7 to 11 days), broad targeting, several creatives; stop when organic Recommended For You exceeds sponsored impressions.
- Official sources say ads are seed data, not a ranking signal. Daily versus lifetime budget is disputed.
- Title literal, icon and thumbnails show real gameplay, one focal point, high contrast, legible at mobile size. If a thumbnail or title misleads, change it: bounces hurt recommendations.
- Description: genre, objective and keywords in the first 160 characters.

**Use:** `/game-dev-ads`, `/game-dev-thumbnail`, `/roblox-ad-campaign-planner`, `/roblox-thumbnail-brief`, `/roblox-thumbnail-brief`; agents `roblox-launch-marketing-manager`. Notes: [[ads-and-sponsored-experiences]], [[thumbnails-icons]], [[titles-descriptions]], [[trailers-and-video-marketing]], [[influencer-and-creator-marketing]], [[ads-stats-monetisation-playbook]].

**Evidence (top rules, trust-labelled; source topic note in brackets):**

- `official` **Fix retention before buying ads**: Ads are the fastest way to get players but won't fix a bad game. (multiple-creators; DitchyDevelopments, Roblox Creator Docs, Tizzy, kra_DeZ) [[ads-and-sponsored-experiences]]
- `T` **Use ads to feed the algorithm, then stop**: Roblox won't recommend a new game until it has retention and return-play data; a paid run buys that data. (multiple-creators; MoseyTube, Tizzy) [[ads-and-sponsored-experiences]]
- `official` **Treat packaging as gating every other signal**: Click/play-through rate gates all other signals; weak icon/title/thumbnail means no impressions regardless of game quality. (multiple-creators; Roblox) [[thumbnails-icons]]
- `official` **Show real gameplay honestly; avoid clickbait**: Thumbnail, icon, title and description must match actual gameplay. (multiple-creators; Roblox, Roblox Creators) [[thumbnails-icons]]
- `official` **Make the title literal and specific**: Name the game after what it is so new players can guess the experience (Grow a Garden, Hide or Die). (multiple-creators; AlvinBlox, Roblox Creator Docs) [[titles-descriptions]]
- `T` **Let the title carry the core fantasy and pair with the thumbnail**: Title gives context to the thumbnail; together they convey a clear core fantasy. (one-creator-repeated; Tizzy) [[titles-descriptions]]

*6 rules shown here; 77 more rules in these topics were not shown because they lack an official or TRUSTED source (or two MIXED ones); they remain in the topic notes with their flags.*

**Where sources disagree (check the topic note before choosing):**

- **Daily vs lifetime budget** ([[ads-and-sponsored-experiences]]): CallMeDogey `T`: always daily, never lifetime (steady flow signals consistency). / Roblox Creators (2025-06) `official`: daily budget with recommendations over lifetime. / waveshine (2024) `?`: lifetime budget gives waves of players and beats daily.
- **Number of thumbnails to test** ([[thumbnails-icons]]): Roblox personalization `official`: 2–5 active (T1635), 3–5 (T2133) / MoseyTube `M`: 2–3 (T2664) / TheDankDeveloper `?`: two (T3104)
- **Emojis** ([[titles-descriptions]]): Roblox Creators 2021 `official`: avoid emojis and special characters in titles. / Creator Docs 2026 `?`: one or two well-placed emojis acceptable in name. / waveshine `?`: add emojis to description.

## Job: retention and analytics

**Spine:**
- Home Recommended For You drives most discovery; optimise play-through rate, first-play bounce, retention and co-play. Official 2026 definitions (for example 28-day retention) override older indie ones.
- Weak D1 or first-session funnel means fix the core loop, onboarding and performance before ads or monetisation.
- Read metrics by cohort, platform and device; change one thing per test and use Experiments for significance.
- Treat indie CCU, revenue and CTR numbers as unverified; use official benchmarks and [[all-numbers-and-benchmarks]] with their flags.

**Use:** `/roblox-analytics-review`, `/roblox-metrics-benchmarks`; agent `roblox-game-doctor`. Notes: [[retention-d1-d7]], [[analytics-metrics]], [[discovery-algorithm]], [[ab-testing-and-experiments]].

**Evidence (top rules, trust-labelled; source topic note in brackets):**

- `official` **Prioritise retention before acquisition and monetisation**: Roblox says order is fun/retention first, then monetisation, then acquisition. (multiple-creators; ItsZyonic, Roblox) [[retention-d1-d7]]
- `official` **Make the first 5 minutes (and first 30 seconds) fun and easy**: Free-to-play players not hooked in about 5 minutes are exponentially unlikely to return. (multiple-creators; MonzterDEV, Roblox Creators, VuukStudios) [[retention-d1-d7]]
- `official` **Instrument analytics before launch**: Set up funnels and event tracking before closed beta or launch, and watch feature engagement and drop-off on launch day to catch game-breaking flows. (multiple-creators; Roblox Creator Docs, Roblox Creators, Roblox DevForum) [[analytics-metrics]]
- `official` **Prioritise retention (D1/D7/D30) as the core health metric**: Retention is the key metric; without it you tread water with constant updates. (multiple-creators; Roblox Creators, Roblox DevForum) [[analytics-metrics]]
- `official` **Optimise engagement, retention and monetization together**: Roblox weighs engagement (by far the most weight), retention, monetization, social co-play, variety and relevance. (multiple-creators; Roblox) [[discovery-algorithm]]
- `official` **Track the current RFY signal set (2026 update)**: The older six signals were qPTR, 7d playtime, 7d play days, 7d Robux spend, 7d spend days and 7d intentional co-play days. (multiple-creators; Roblox, Roblox Creators, Roblox DevForum) [[discovery-algorithm]]

*6 rules shown here; 47 more rules in these topics were not shown because they lack an official or TRUSTED source (or two MIXED ones); they remain in the topic notes with their flags.*

**Where sources disagree (check the topic note before choosing):**

- **How aggressively to chase benchmarks** ([[analytics-metrics]]): CallMeDogey `T`: improve anything below 75th percentile; all six in green is the one true way to grow. / Deconstructor of Fun (Zach) `T`: aims for the 90th percentile on all six. / Roblox (official) `official`: push below-50th metrics above 50th for most surfacing gain; don't min-max the six metrics.
- **Do ads help or hurt?** ([[discovery-algorithm]]): Roblox Creators `official`: ads do not hurt organic discovery and can help cold start. / Erthlord (unverified) `?`: bad first ad round can hurt a place. / Erthlord `?`, LovJak `T`, Raul `T`: ads alone did not trigger pickup.

## Job: live-ops

**Spine:**
- Ship weekly or biweekly content on existing systems, with a major update every 2 to 3 months. If an update takes more than 3 weeks it is a major update, and the cadence keeps running meanwhile.
- Every update needs a social or co-play hook and a rollback rule; check retention, session time, payer conversion and ARPPU after each release.
- Space event announcements at least 3 days apart; refresh packaging at major updates.
- Community (Discord about a month before launch) is part of live-ops, not a side task.

**Use:** `/game-dev-update`, `/roblox-leaderboards-and-events`; agent `roblox-liveops-planner`. Notes: [[updates-live-ops]], [[events-and-seasonal-content]], [[community-and-discord]], [[social-features-and-virality]].

**Evidence (top rules, trust-labelled; source topic note in brackets):**

- `official` **Run a regular content cadence of 1-2 weeks**: Ship something (cosmetics, pets, furniture, outfits, event content) every 1-2 weeks, reusing existing systems. (multiple-creators; Roblox Creators) [[updates-live-ops]]
- `official` **Keep cadence releases to existing systems**: Don't add new features, currencies or mechanics in cadence drops. (multiple-creators; Roblox Creators) [[updates-live-ops]]
- `official` **Make event rewards earned, not handed out**: Tie prizes to completing a challenge or special play. (one-creator-repeated; Roblox DevForum, anomalousDucky) [[events-and-seasonal-content]]
- `official` **Use limited-time exclusives for urgency**: Limited-time eggs, holiday pets, golden or Aurora-style events with exclusive mutations, and special items drive return visits and dedicated grinding. (multiple-creators; Mulch, Roblox DevForum, janisjanis01, rasdev) [[events-and-seasonal-content]]
- `official` **Make every game social, not just chat-centric**: Any genre can be social. (multiple-creators; AlvinBlox, Roblox, Roblox Creators) [[social-features-and-virality]]
- `official` **Put a visible invite-friends button/prompt in the game**: waveshine calls an in-game invite button the most important tip. (multiple-creators; Roblox, waveshine) [[social-features-and-virality]]

*6 rules shown here; 72 more rules in these topics were not shown because they lack an official or TRUSTED source (or two MIXED ones); they remain in the topic notes with their flags.*

**Where sources disagree (check the topic note before choosing):**

- **Frequency versus meaningfulness** ([[updates-live-ops]]): RobloxOfficial (2025) and kra_DeZ `?`: update weekly or even daily; stale games shouldn't be rewarded. / Roblox Creators (2022-01) and RobloxCreators (2022-12) `official`: don't assume smaller, more frequent updates are better; meaningful updates beat frequent ones and you can bur...
- **Paying/commissioning influencers** ([[social-features-and-virality]]): RobloxOfficial 2018 and AlvinBlox `?`: promo codes, payment in items, commissioning small creators / Roblox (2025 `official`, Ninja Challenge) `?`: skip paying YouTubers/TikTokers early; a fun game attracts creators organically / SmartyRBX `M`: needs a very good game and lots of value

## Job: 3D models and Blender

**Spine (official Creator Docs; see `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md`):**
- Hard limits: 20,000 triangles per mesh (4,000 for rigid or layered accessories), one material per mesh, one UV set inside 0:1, 4 bone influences per vertex and none on Root. Texture caps depend on scope (4096 upload ceiling, 1024 PBR table, 2048 Marketplace accessories): name the scope.
- Export FBX with Apply Scalings = FBX Unit Scale, Add Leaf Bones off, selected objects only, modifiers applied; start rigs from Roblox's templates. Non-Stud import units use 25:7 studs per metre since 2026-06-16.
- Claude drives Blender through `mcp-for-blender` or headless `blender -b --python`: save the .blend first (the socket has no authentication), check the exit code and that the output file exists.

**Use:** `/rbx model-rebuild`, `/rbx part-to-mesh-planner`, `/rbx accessory-fitting-guide`, `/rbx rig-checker`, `/rbx animation-import-guide`, `/rbx texture-budget-checker`.

## Job: running a game project

**Spine:**
- Keep the team small; pay outside help only for your weakest skill first; keep creative direction and core systems in-house.
- Playtest early with a rough build, watch new players silently on mobile, recruit testers from the real audience, instrument the funnel.
- Check release requirements (age gates, tax and DevEx eligibility) before launch; soft-launch quietly, fix D1, then spend.
- Protect against burnout; reinvest and diversify income; decide keep versus sell with escrow and due diligence.

**Use:** `/game-dev-plan`, `/game-dev-playtest`, `/roblox-launch-checklist`, `/roblox-publish-checklist`, `/roblox-playtest-checklist`; agents `roblox-studio-lead`, `roblox-playtest-runner`, `roblox-pre-delivery-reviewer`. Notes: [[development-process-and-speed]], [[team-and-budget]], [[playtesting-and-feedback]], [[mindset-and-strategy]], [[business-and-payouts]], [[age-ratings-moderation-and-tos]].

**Evidence (top rules, trust-labelled; source topic note in brackets):**

- `official` **Start with small, simple, finishable games before a dream game**: Make 10-20 small projects first (SmartyRBX). (multiple-creators; AlvinBlox, Roblox Creators, SmartyRBX, TheDankDeveloper) [[development-process-and-speed]]
- `official` **Ship a barebones MVP around one core loop, then iterate**: Strip to core systems, map and fun; playable first, extras later as updates. (multiple-creators; Roblox Creators, SmartyRBX) [[development-process-and-speed]]
- `M` **Cover only your weakest skill with outside help first**: Identify the one thing you are weak at (e.g. (multiple-creators; MoseyTube, SmartyRBX) [[team-and-budget]]
- `official` **Start hiring small to learn how to hire**: Make a small first hire (e.g. (multiple-creators; Roblox, SmartyRBX) [[team-and-budget]]
- `official` **Playtest early with a rough build**: Put a bare-bones playable prototype in front of testers before polishing or heavy investment. (multiple-creators; AlvinBlox, Roblox Creators, TheDankDeveloper) [[playtesting-and-feedback]]
- `official` **Watch new players silently instead of only asking**: Have someone new (relatives, kids, people unfamiliar with mobile or the game) play with as little help as possible. (multiple-creators; Roblox Creators) [[playtesting-and-feedback]]

*6 rules shown here; 90 more rules in these topics were not shown because they lack an official or TRUSTED source (or two MIXED ones); they remain in the topic notes with their flags.*

**Where sources disagree (check the topic note before choosing):**

- **Ship rough vs delay for quality** ([[development-process-and-speed]]): AlvinBlox `T`, SmartyRBX `M`, Roblox Creators (T225 `official`, T255) `?`: ship MVP, done is better than perfect / Roblox Creators (T214 `official`, T267) `?`: push the date when testers say it isn't ready; first impression matters / Creators on the Blox (T2373) `M`: only ships games meeting a higher bar
- **Friends and fans as testers** ([[playtesting-and-feedback]]): Roblox and Roblox Creators `official`: use real critics, since fans and friends flatter or over-criticise (T3213, T3088). / Likely reconcile `?`: friends and fans for early basic builds, critics for closed tests.

## Job: using agents and skills

**Spine (Nate Herk, RoboNuggets, Karpathy, plus the Manager research):**
- Start with the simplest layer that works: a custom GPT or project, then plain automation, then an AI workflow, then an agent. Do not chase every new tool; planning, verification and minimal context transfer across tools. (Nate Herk)
- One agent per specific job; the orchestrator only delegates and logs. Send bulky, throwaway work to a sub-agent so only a summary returns. Skills run in the main session; sub-agents get a clean window and can use another model.
- Treat context as the main lever: thin CLAUDE.md as a router, progressive disclosure, skills under about 500 lines, reset or /clear between topics, hand state off explicitly between sessions. (RoboNuggets, Karpathy, Nate Herk)
- Hardcode stable lookups into the skill; delegate searching.
- Find a ready-made skill or agent before writing one: `vault-find`, then read the one note and follow it.

**Use:** `/use-ai-library-rbxdev-vault`, `/use-rbxdev-vault`, `/manager-mode-rbxdev-vault`, `/clarify-before-build-rbxdev-vault`; notes: [[topic-orchestration-patterns]], [[topic-context-engineering]], [[topic-claude-code-features]], hubs `nate-herk`, `robonuggets`, `andrej-karpathy`.

**Evidence (AI creators; tag = how the creator backed it; sources are the video notes):**

*Delegation and orchestration*
- **Make the orchestrator only delegate.** Tell it explicitly not to write emails, summaries or code itself. `demonstrated` `2025-06-10-multi-agent-systems-have-never-been-easier-to-build-n8n-no-c` @ 11:00 `2025-08-15-i-built-the-ultimate-army-of-media-agents-in-n8n-free-templa` @ 11:35
- **Brief the lead agent as a project manager.** Say: don't execute, delegate to cheaper sub-agents, parallelize independent work, log progress to a build plan or per-agent folder, and flag open issues. `demonstrated` `2026-08-10-build-sell-ai-saas-products-2-hour-course` @ 31:44

*Context and memory files*
- **Treat context as a precious resource and reset between topics.** Start a new chat or run /clear when switching tasks. `opinion` `2025-02-27-how-i-use-llms` @ 16:38 `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 5:31:20
- **Inspect what fills the window.** Run /context and /cost regularly, including on a fresh session. `demonstrated` `2026-04-02-18-claude-code-token-hacks-in-18-minutes` @ 5:07 `2026-03-27-everything-new-in-claude-code-explained-march-2026-edition` @ 5:03
- **Keep agent instruction files minimal, hand-written and for repeated mistakes only.** Skip /init output and repo overviews; add a line only for something the agent keeps getting wrong, and first try to fix the code or add a check. `opinion` `2026-02-23-delete-your-claude-md-and-your-agent-md-too` @ 14:55 `2026-01-24-ai-mistakes-you-re-probably-making` @ 18:42

*Skills and rules*
- **Build skills with a fixed framework.** Cover name and trigger, a one-sentence goal and output, steps, reference files, failure-mode rules, and a self-improvement loop. `demonstrated` `2026-02-27-master-95-of-claude-code-skills-in-28-minutes` @ 17:13 `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 6:25:10
- **Close the loop at session end.** Run a calibrate or reflect step that updates skills, memory and rules with learnings. `demonstrated` `2026-08-03-claude-code-just-changed-forever-6-new-rules-by-anthropic-en` @ 17:06 `2026-03-17-every-openclaw-concept-explained-for-normal-people` @ 11:09
- **Write a skill description as a trigger: when to load it, not a summary.** Why: the model sees only name and description for every skill and picks from them. `opinion` `2026-08-19-so-i-tried-matt-s-skills` @ 5:14 `2026-08-11-my-agents-md-skills-md-breakdown-don-t-copy-them` @ 12:09

## Job: coding with AI

**Spine:**
- Plan, then execute; wireframe first (trigger, data, transformation, where AI fits). (Nate Herk)
- Write prompts reactively: add one sentence per observed error. Use the A.G.E.N.T. structure (Ask, Guidelines/Goal, Examples, Notation/Negations, Tools) when a prompt must be reusable. (Nate Herk, RoboNuggets)
- Verify with checkable goals and loops; keep a human approval step on risky actions. Automated review and human review pull in different directions (see disagreements).
- Verify numerically and sanity-check initial values (Karpathy's gradient checks and initial-loss check generalise to: test the first output before building on it).
- Game code: prompt one mechanic at a time, playtest after each prompt, paste errors back, write long specific prompts with concrete numbers (Roblox KB `ai-and-tools`, backed by several creators).
- Loops stop on a measurable metric plus an iteration cap, never "until satisfied". Add an instruction-file line only for a repeated mistake, after trying to fix the code or add a check (Nate Herk, RoboNuggets; Theo MIXED + Anthropic docs).
- Reset context when the topic changes; long context costs more and lowers accuracy.

**Use:** `/karpathy-coding-guidelines-rbxdev-vault`, `/clarify-before-build-rbxdev-vault`, `/rate-anything-1-10-rbxdev-vault`; agents `claim-verifier-rbxdev-vault`, `self-verifying-game-builder-rbxdev-vault`, `roblox-luau-reviewer`. Notes: [[ai-and-tools]], [[topic-llm-judge-and-adversarial-verification]], [[topic-brief-prompt-engineering]].

**Evidence (AI creators; tag = how the creator backed it; sources are the video notes):**

*Plan, then execute*
- **Use plan mode before agents change things.** Review the proposal, then approve. `demonstrated` `2026-01-16-build-anything-with-claude-code-n8n-beginner-s-guide` @ 17:01 `2026-03-05-turn-claude-code-into-your-executive-assistant-in-27-mins` @ 17:31
- **Split planner, implementer and validator into separate sessions linked by handoff documents.** Why: it keeps each session out of the "dumb zone" of a bloated context. `opinion` `2026-06-18-how-to-use-claude-code-better-than-98-of-people` @ 33:40

*Verification and review loops*
- **Give loops a measurable done criterion.** Use "iterate until metric X equals Y", not "until you're satisfied". Why: subjective stop conditions never stop reliably. `demonstrated` `2026-06-19-finally-agent-loops-clearly-explained` @ 6:55 `2026-09-02-how-anthropic-actually-prompts-fable-5-1` @ 7:22
- **Separate the critic from the worker.** Use a scorer or critic sub-agent per worker, and a final check that parts meet spec. `demonstrated` `2026-08-05-this-new-claude-prompting-technique-is-blowing-people-s-mind` @ 4:02 `2026-09-02-how-anthropic-actually-prompts-fable-5-1` @ 7:22
- **Hand the agent the whole task with a finish line and a short stop rule.** Say what done looks like (tests pass, screenshot shown, every endpoint migrated) and when to stop and ask; put the stop rule in CLAUDE.md. `opinion` `2026-09-25-getting-the-most-out-of-opus-5-5` @ 3:08 `2026-09-25-getting-the-most-out-of-opus-5-5` @ 18:21

## Job: research

**Spine:**
- Official and primary sources first, newest first; label every claim with who said it and how strong the evidence is; say "KB gap" when the vault has nothing.
- Creators' income, CCU and revenue claims are self-reported or marketing; relay them as claims, never as facts.
- Prefer demonstrated over opinion; third-party tips relayed by a creator depend on the quoted source.
- Verify a recommendation with a second independent source before it drives a decision (MIXED creators need this; TRUSTED creators still defer to official docs on numbers).
- Roblox market research: use trend research with current data; study transferable patterns, never copy content.

**Use:** `/deep-topic-research-rbxdev-vault`, `/roblox-trend-research`, `/roblox-kb-answer`; agent `claim-verifier-rbxdev-vault`; search: `vault-find`, `kbq`. Notes: [[creator-credibility]], [[trend-research-and-validation]], [[topic-report-formats-and-verification]].

## Job: running a project with agents

**Spine:**
- Plan, then execute; brief the lead as a project manager (do not execute, delegate to cheaper sub-agents, parallelise independent work, log progress, flag open issues).
- Verification loops and independent verifiers beat self-reported success. Ask for evidence, not claims.
- Permissions and guardrails matter more as autonomy grows; keep a human in the loop for irreversible actions.
- Control cost: cheapest model that fits, one subagent at a time when usage is tight, short outputs, `/low-usage-mode-rbxdev-vault`.
- Failure handling: read the error, fix the script, retest, then update the workflow so it does not repeat.

**Use:** `/manager-mode-rbxdev-vault`, `/low-usage-mode-rbxdev-vault`, `/clarify-before-build-rbxdev-vault`; agents `claim-verifier-rbxdev-vault`, `roblox-audit-fanout`. Notes: [[Manager-README]], [[topic-orchestration-patterns]], [[topic-model-effort-routing-cost]], [[topic-agent-security]], [[topic-long-running-always-on-agents]].

**Evidence (AI creators; tag = how the creator backed it; sources are the video notes):**

*Parallelism*
- **Run independent work in parallel.** Examples are chapters, design variants, audits and test loops. `demonstrated` `2026-06-09-how-to-build-claude-subagents-better-than-99-of-people` @ 22:12 `2026-04-29-claude-canva-design-on-autopilot-beginners-course` @ 5:27
- **Match the term to the setup.** Parallel agents are separate terminals. `opinion` `2026-02-25-i-can-actually-watch-my-ai-agents-work-now` @ 8:44

*Permissions and guardrails*
- **Enforce never-break rules with hooks, not skill text.** Example: no invoice above a limit without sign-off. `opinion` `2026-10-05-anthropic-just-revealed-10-new-rules-for-claude-skills` @ 10:22
- **Add caution rules and prefer guarded tools.** Ask the agent to amend CLAUDE.md to be more careful about deleting files, and avoid tools without permission and deletion guardrails. `opinion` `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 5:27

*Human-in-the-loop*
- **Keep human checkpoints where outputs are probabilistic or hard to reverse.** Review dialogue and prompts, and approve email drafts. `demonstrated` `2025-12-09-ai-brand-ads-so-cinematic-you-ll-think-they-cost-30-000-it-c` @ 19:06 `2025-09-21-the-ultimate-agent-for-limitless-ugcs-seedream-x-nanobanana` @ 7:11

*Cost control*
- **Match model to job.** Use cheaper models for sub-agents and simple tasks, and the strongest for deep reasoning. `demonstrated` `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 5:40:59 `2026-06-19-glm-5-2-in-claude-code-is-blowing-my-mind` @ 6:42
- **Use deterministic workflows where no AI is needed.** Let the harness route events and call the LLM only when needed. `opinion` `2026-05-25-the-playbook-for-a-100m-ai-agency` @ 1:22:51 `2025-05-23-build-sell-n8n-ai-agents-8-hour-course-no-code` @ 5:13

*Failure handling*
- **Plan for failure, not only the happy path.** Test bad, missing and duplicate data. `opinion` `2025-12-27-how-to-actually-deliver-ai-projects-apis-hosting-handover-ex` @ 10:21 `2025-03-05-6-months-of-building-ai-agents-in-43-minutes-without-the-hyp` @ 32:13
- **Test scheduled tasks manually after creating them.** Why: each run is a fresh stateless session, so missing keys or permission prompts only show up in testing. `demonstrated` `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 2:52:05 `2026-05-15-how-to-deploy-your-claude-automations-3-methods` @ 17:14

*Autonomy levels*
- **Raise autonomy in steps.** Move from manual prompt-review-reprompt, to a critic loop, to a fleet of sub-agents each with a critic. `opinion` `2026-08-05-this-new-claude-prompting-technique-is-blowing-people-s-mind` @ 4:02 `2026-01-25-agentic-workflows-just-changed-ai-automation-forever-claude` @ 16:15

## Where the AI creators disagree

- **Long-running context.** Karpathy says to reset context on topic change. Nate notes loops keep continuous context as a pro, but context grows each firing and rots. `2025-02-27-how-i-use-llms` @ 16:38 vs `2026-03-07-this-new-claude-code-feature-is-a-game-changer` @ 1:43
- **Human review versus automated review.** Nate pitches an evaluator-optimizer loop as automating human review. RoboNuggets calls human-in-the-loop essential for probabilistic output. `2025-05-23-build-sell-n8n-ai-agents-8-hour-course-no-code` @ 5:07 vs `2025-12-09-ai-brand-ads-so-cinematic-you-ll-think-they-cost-30-000-it-c` @ 19:06
- **Permissions.** Nate's course setup refers to enabling "allow dangerously skip permissions" (text truncated). RoboNuggets stresses guardrails and warns against tools that lack them. `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 3:44:38 vs `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 14:49
- **Always-on agents.** RoboNuggets pitches a 24/7 multi-agent system. Nate says agents are not literally always on; they wake in loops. `2026-03-24-claude-code-just-became-unstoppable-claudeclaw` @ 0:00 vs `2026-03-06-cursor-automations-clearly-explained-worth-learning` @ 7:20
- **Verification versus cost.** Nate wants near-final, verified output. RoboNuggets notes verification loops made Fable about 3x costlier and slower than a cheaper model. `2026-09-02-how-anthropic-actually-prompts-fable-5-1` @ 7:22 vs `2026-07-23-i-made-fable-5-and-kimi-k3-build-the-same-app-raw-results` @ 23:07
- **Model switching.** Nate recommends mixing models (cheap sub-agents, a delegating orchestrator). RoboNuggets warns that switching models inside one chat forfeits cache discounts. `2026-07-11-claude-code-for-non-coders-6-hour-course` @ 5:40:59 vs `2026-10-12-claude-5-5-model-mistakes-you-may-still-be-making-23-tips-an` @ 2:10
- **Instruction files, memory and skills.** Nate and RoboNuggets advise moving anything you repeat into CLAUDE.md or a skill and building a self-improving memory. Theo (MIXED; opinion, measured on his own repos) says start with no agent file, add a line only after a repeated failure, keep skills few and pruned, and switch auto-memory off for code. Anthropic's docs keep memory on by default and the AGENTS.md paper supports minimal files, so treat "thin file, fix the code first" as the safe common ground. `2026-02-23-delete-your-claude-md-and-your-agent-md-too` @ 12:32 vs `2026-03-12-build-sell-with-claude-code-10-hour-course` @ 2:11:46; `2026-08-25-turn-off-claude-code-s-memory` @ 38:02
- **Ceremony and sub-agents.** Nate and RoboNuggets assign one specialist agent per job. Theo says match ceremony to the task: no sub-agents or panels for single-pass work, delegate only for breadth or adversarial review, state file ownership up front. `2026-08-11-my-agents-md-skills-md-breakdown-don-t-copy-them` @ 8:15 vs `2026-08-12-grok-bot-is-for-real-what-you-need-to-know` @ 8:29

## Creator cards: "what would <creator> do?"

Open the creator's hub or playbook, read the section for the question, answer in their voice only from what the note says, label it as their claim with the trust label, and say when the note does not cover it.

### AI creators

| Creator | Known for (from the hub) | Read |
|---|---|---|
| Nate Herk (366 videos) | simplest layer that works, wireframe first, reactive prompts, context engineering, verification loops, human approval on risky actions, sell outcomes | `nate-herk` |
| RoboNuggets | agency metaphor (you are the CEO), A.G.E.N.T. prompt framework, direct model access via aggregators, thin CLAUDE.md router and progressive disclosure, reuse proven formats | `robonuggets` |
| Andrej Karpathy (15 usable videos) | build from first principles, verify numerically, sanity-check initial loss, reset context on topic change | `andrej-karpathy` |
| Theo, t3.gg (16 videos, MIXED) | minimal hand-written agent files (fix the code or add a check first), skill descriptions as triggers, a stated done condition, long unattended loops with a machine check and a ratchet, a fix ladder (cause, check, CI, rule, human); his cost figures, memory-off and tool opinions are not recommendations | `theo-t3gg` |

Income and earnings claims by AI creators are marketing, not evidence. See each hub's reliability section.

### Roblox creators, TRUSTED (usable as primary sources; official docs still win on numbers)

| Creator | Score | Strongest themes | Playbook |
|---|---|---|---|
| 5uphi | 8.8 | Studio & Scripting, Mindset & Process, Game Ideas | [[5uphi - How to make successful Roblox games\|playbook]] |
| crusherfiredev | 8.7 | Studio & Scripting, Mindset & Process, Monetisation | [[crusherfiredev - How to make successful Roblox games\|playbook]] |
| ArTheDev | 8.5 | Studio & Scripting, Mindset & Process, Game Ideas | [[ArTheDev - How to make successful Roblox games\|playbook]] |
| PossiblePanda | 8.3 | Studio & Scripting, Mindset & Process | [[PossiblePanda - How to make successful Roblox games\|playbook]] |
| Yann4dev | 8.3 | Mindset & Process, Monetisation, Discovery & Algorithm | [[Yann4dev - How to make successful Roblox games\|playbook]] |
| FrenkyRBLX | 8.2 | Studio & Scripting | [[FrenkyRBLX - How to make successful Roblox games\|playbook]] |
| lnorroblox | 8.2 | Mindset & Process, Retention, Discovery & Algorithm | [[lnorroblox - How to make successful Roblox games\|playbook]] |
| MonarchSilgrit | 8.2 | Studio & Scripting, Mindset & Process, Game Ideas | [[MonarchSilgrit - How to make successful Roblox games\|playbook]] |
| RaulStudios | 8.2 | Mindset & Process, Retention, Game Ideas | [[RaulStudios - How to make successful Roblox games\|playbook]] |
| SimTekGameDevelopment | 8.2 | Studio & Scripting, Mindset & Process, Game Ideas | [[SimTekGameDevelopment - How to make successful Roblox games\|playbook]] |
| AlvinBlox | 8.1 | Mindset & Process, Studio & Scripting, Monetisation | [[AlvinBlox - How to make successful Roblox games\|playbook]] |
| byteblox100 | 8.1 | Studio & Scripting, Game Ideas, Mindset & Process | [[byteblox100 - How to make successful Roblox games\|playbook]] |
| GnomeCode | 8.1 | Studio & Scripting, Mindset & Process, Game Ideas | [[GnomeCode - How to make successful Roblox games\|playbook]] |
| Mulchmite | 8.1 | Monetisation, Mindset & Process, Studio & Scripting | [[Mulchmite - How to make successful Roblox games\|playbook]] |
| quezdev | 8.1 | Monetisation, Studio & Scripting, Discovery & Algorithm | [[quezdev - How to make successful Roblox games\|playbook]] |
| Roox4Official | 8.1 | Studio & Scripting, Mindset & Process, Game Ideas | [[Roox4Official - How to make successful Roblox games\|playbook]] |
| BloxxedDev | 8.0 | Studio & Scripting, Discovery & Algorithm, Mindset & Process | [[BloxxedDev - How to make successful Roblox games\|playbook]] |
| BRicey | 8.0 | Studio & Scripting, Mindset & Process, Monetisation | [[BRicey - How to make successful Roblox games\|playbook]] |
| callmedogey | 8.0 | Monetisation, Mindset & Process, Discovery & Algorithm | [[callmedogey - How to make successful Roblox games\|playbook]] |
| BubuTheDev | 7.9 | Studio & Scripting, Discovery & Algorithm, Monetisation | [[BubuTheDev - How to make successful Roblox games\|playbook]] |
| DuckableDev | 7.9 | Mindset & Process, Studio & Scripting, Game Ideas | [[DuckableDev - How to make successful Roblox games\|playbook]] |
| l_eif | 7.9 | Studio & Scripting, Game Ideas, Retention | [[l_eif - How to make successful Roblox games\|playbook]] |
| NotCumin | 7.9 | Game Ideas, Studio & Scripting, Retention | [[NotCumin - How to make successful Roblox games\|playbook]] |
| TizzyRBLX12 | 7.9 | Mindset & Process, Game Ideas, Retention | [[Tizzy - How to make successful Roblox games\|playbook]] |
| CritDEV | 7.8 | Studio & Scripting, Mindset & Process | [[CritDEV - How to make successful Roblox games\|playbook]] |
| JustDucksey | 7.8 | Studio & Scripting, Game Ideas, Mindset & Process | [[JustDucksey - How to make successful Roblox games\|playbook]] |
| SeiboRoblox | 7.8 | Monetisation, Mindset & Process, Discovery & Algorithm | [[SeiboRoblox - How to make successful Roblox games\|playbook]] |
| alexbuilds_games | 7.7 | Monetisation, Discovery & Algorithm, Thumbnails & Icons | [[alexbuilds_games - How to make successful Roblox games\|playbook]] |
| BloxianCode | 7.7 | Studio & Scripting, Mindset & Process | [[BloxianCode - How to make successful Roblox games\|playbook]] |
| bubDEV | 7.7 | Thumbnails & Icons, Mindset & Process, Game Ideas | [[bubDEV - How to make successful Roblox games\|playbook]] |
| DevTechSpectrum | 7.7 | Studio & Scripting, Mindset & Process | [[DevTechSpectrum - How to make successful Roblox games\|playbook]] |
| ItsZyonic | 7.7 | Mindset & Process, Discovery & Algorithm, Retention | [[ItsZyonic - How to make successful Roblox games\|playbook]] |
| LovJak | 7.7 | Mindset & Process, Studio & Scripting, Discovery & Algorithm | [[LovJak - How to make successful Roblox games\|playbook]] |
| pineappledevv | 7.7 | Studio & Scripting, Mindset & Process, Monetisation | [[pineappledevv - How to make successful Roblox games\|playbook]] |
| stewiepfing | 7.7 | Studio & Scripting, Game Ideas, Retention | [[stewiepfing - How to make successful Roblox games\|playbook]] |
| studiorookroblox | 7.7 | Studio & Scripting, Mindset & Process, Retention | [[studiorookroblox - How to make successful Roblox games\|playbook]] |
| Xaiyne | 7.7 | Studio & Scripting, Monetisation, Mindset & Process | [[Xaiyne - How to make successful Roblox games\|playbook]] |
| 1Coal | 7.6 | Game Ideas, Retention, Thumbnails & Icons | [[1Coal - How to make successful Roblox games\|playbook]] |
| Emancyphur | 7.6 | Studio & Scripting, Mindset & Process, Retention | [[Emancyphur - How to make successful Roblox games\|playbook]] |
| deconstructoroffun | 7.5 | Mindset & Process, Discovery & Algorithm, Retention | [[deconstructoroffun - How to make successful Roblox games\|playbook]] |
| TheRoyalDev | 7.5 | Mindset & Process, Game Ideas, Studio & Scripting | [[TheRoyalDev - How to make successful Roblox games\|playbook]] |

### Roblox creators, MIXED (confirm with a second source)

DaiorgYT (7.4), rasdevblox (7.4), vuukstudios7635 (7.4), MoseyTube77 (7.3), xtb7-dev (7.3), 1_Bruce (7.2), AmoraScripting (7.2), kra_DeZ (7.2), generalistprogrammer3233 (7.1), MattTheMethod (7.1), TheNexusAvenger (7.1), EISABOOSFF (6.9), CreatorsOnTheBlox (6.8), MonzterDEV (6.8), GameMakersDev (6.7), PolarbearRBLXX (6.6), TheDevKing (6.6), Theo-t3gg (6.6), ContextLost (6.4), janisjanis01 (6.1), SmartyRBX (5.9), LastLevelStudios (5.5), ThatGuyEvan (5.1), CORSOBLOX (5.0), ThePurpleGuy_0 (5.0)

### Not authorities (WEAK or INSUFFICIENT evidence): 23 creators

Their notes stay in the vault with a trust label; never use one as the sole source of a recommendation: 7PhantomS, AnomalousDucky, ArowDev, BadGameDev, BrawlDevRBLX, DevTotal, DitchyDevelopments, Erthlord, JustVeryYellow, MGFTUE, MaximumADHD, PerstileRBX, PokeRB, RapstrikeDev, TheDankDeveloper, TheDevBacon, WTMW20, chasehiggins69, gamediscoverco, mats-dept2, rool-studio, sunnybdrake, waveshinedev

Official sources (Roblox, Roblox Creators, Creator Docs, DevForum) are not audited; they are the reference for platform mechanics, metrics and payouts.
