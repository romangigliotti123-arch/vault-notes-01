---
title: studiorookroblox - How to make successful Roblox games
tags: [roblox, studiorookroblox, playbook]
videos: 5
generated: 2026-10-29
credibility: trusted
credibility_score: 7.7
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# studiorookroblox - How to make successful Roblox games

Win the early marketing game before launch. Enter a game jam to get a finished prototype and an audience. Build a DataStore progression core and capped loadouts. Build a pre-release audience through short reels and Instagram. Playtest with a community Discord of about 200 active players, then spend about two weeks fixing bugs before wider launch. Act on prominent YouTuber criticism in live updates. Expect a launch spike followed by a decline. Evidence is thin: only two of five videos carry substantive advice.

**Style:** Candid, process-first solo developer documenting Trench (later Trench: Decay) with real numbers and honest reflection. Shows systems, placeholder art and tooling openly. Suits solo or small-team developers building a progression-driven game who want a concrete pre-launch marketing and playtest path. Lighter on design theory.

## Playbook
1. **Use a game jam as the idea-to-prototype filter** [[events-and-seasonal-content]]: Enter a game jam to force a finished, prize-winning prototype quickly. Trench Decay began as a Ro Devs Discord 2026 jam win that became the basis for a front-page game in about 2 months (EuaV0qc6UXQ).
2. **Scope the team against the game's size** [[team-and-budget]]: Solo development was a major speed disadvantage per the developer. For a large scope, plan for a team early rather than stretching one person across systems, art and marketing.
3. **Build DataStore progression first** [[data-persistence]]: Save currency (medals), unlocks, ranks, classes and loadout first; the developer called it the biggest chunk and it saves purchases and equips (WCIBNClvUrQ). Test with a 1000-medal Studio grant to exercise purchases.
4. **Cap equip slots and force unequip** [[combat-and-gameplay-systems]]: Limit armory tools to two equip slots so players must choose. Require unequipping before equipping another item; a third slot would require removing one (WCIBNClvUrQ).
5. **Plan 4-player campaign lobbies** [[matchmaking-and-teleport]]: Design campaign lobbies for up to 4 players with selectable difficulty and lobby size. The developer started this as the first multiplayer step after the progression update (WCIBNClvUrQ).
6. **Model low-poly and push detail into textures** [[building-art-and-assets]]: Block rough low-poly shapes and bake detail into normals and textures to keep poly counts and draw calls low for Roblox. Bevel all sharp corners in one pass instead of placing exact bevels everywhere (z04_RTBiMgg, EuaV0qc6UXQ notes).
7. **Use hard-surface CAD for guns** [[ai-and-tools]]: Rough a gun in Plasticity (one-time purchase, not subscription), topology in Blender 4.0 via the Plasticity-Blender bridge, texture in Substance Painter, then import to Roblox Studio. A Gatling gun took about 30-40 minutes excluding talking (z04_RTBiMgg).
8. **Run a Discord playtest before launch** [[playtesting-and-feedback]]: Playtest with a community Discord of about 200 active players. It surfaced broken UI, teleports and unsaved data that the developer had not caught (EuaV0qc6UXQ).
9. **Reserve about two weeks for post-playtest fixes** [[development-process-and-speed]]: After a rough playtest, spend roughly two weeks fixing most bugs and adding console and mobile support before a wider launch (EuaV0qc6UXQ).
10. **Post short devlog reels early** [[trailers-and-video-marketing]]: Short devlog reels drew far more views than expected within days; one video hit 501 views against an expected ~100. Use feedback from reels to choose what to build next (WCIBNClvUrQ).
11. **Build an Instagram audience before release** [[community-and-discord]]: Instagram pushed the developer's videos to millions of views during development, while TikTok averaged about 2 views per video. Prioritise Instagram reach and treat TikTok as unproven (EuaV0qc6UXQ).
12. **Partner with a friend for a YouTube video** [[influencer-and-creator-marketing]]: A friend-made YouTube video covering the game reached new players. Use partnerships for launch-window reach (EuaV0qc6UXQ).
13. **Answer prominent YouTuber criticism with a big update** [[updates-live-ops]]: Acting on criticism from prominent YouTubers via a big update drew more attention and a rare response video from them (EuaV0qc6UXQ).
14. **Plan for a launch spike then decline** [[analytics-metrics]]: The game peaked at over 1,700 CCU in the first 2 weeks after reaching the Roblox front page, then settled around 700 CCU. Plan retention and updates for the post-spike baseline, not the peak (EuaV0qc6UXQ).

## Key numbers
- Development: about 2 months, May 14 to July 3 release, solo developer (EuaV0qc6UXQ)
- Test currency grant: 1000 medals in Studio (WCIBNClvUrQ)
- Armory tool equip slots: 2 (WCIBNClvUrQ)
- Multiplayer campaign lobby: max 4 players (WCIBNClvUrQ)
- Devlog reel views: 501 vs expected ~100 (WCIBNClvUrQ)
- Discord members: expected 5-10, actual far higher (unquantified) (WCIBNClvUrQ)
- TikTok: about 2 views per video on average during development (EuaV0qc6UXQ)
- Instagram: millions of views during development (EuaV0qc6UXQ)
- Pre-launch playtest: about 200 active Discord players (EuaV0qc6UXQ)
- Post-playtest fix window: about 2 weeks (EuaV0qc6UXQ)
- Peak CCU: over 1,700 in first 2 weeks after front page (EuaV0qc6UXQ)
- Settled CCU after decline: about 700 (EuaV0qc6UXQ)
- Gatling gun model: about 30-40 minutes excluding talking (z04_RTBiMgg)
- Plasticity: one-time purchase (z04_RTBiMgg)

## Common mistakes
- Relying on TikTok for reach: it averaged about 2 views per video during development while Instagram drove millions.
- Playtesting too late, so broken UI, teleports and unsaved data reach players at launch.
- Launching without a bug-fix window after a rough playtest.
- Deferring the save system: the developer calls DataStore the biggest chunk, so leaving it late risks unsaved purchases and equips.
- Placing exact bevels on every edge instead of bevelling sharp corners in one pass.
- Building high-poly geometry instead of baking detail, which raises poly counts and draw calls.
- Going solo on a large scope, which the developer called a major speed disadvantage.
- Planning around the launch peak; CCU fell from over 1,700 to about 700.
- Ignoring creator feedback; acting on YouTuber criticism drew attention and a response video.
- Shipping PC-only when console and mobile support was added after playtesting.

## Launch checklist
- [ ] DataStore saves currency, unlocks, loadouts and purchases; test with a Studio grant (WCIBNClvUrQ)
- [ ] Loadout slots capped and unequip-before-equip enforced (WCIBNClvUrQ)
- [ ] Campaign lobbies capped at 4 players with difficulty selection (WCIBNClvUrQ)
- [ ] Discord playtest with about 200 active players run before launch (EuaV0qc6UXQ)
- [ ] Playtest bugs logged: broken UI, teleports, unsaved data (EuaV0qc6UXQ)
- [ ] About two weeks reserved for bug fixes after a rough playtest (EuaV0qc6UXQ)
- [ ] Console and mobile support scoped before wider launch (EuaV0qc6UXQ)
- [ ] Short devlog reels posted early and tracked for views (WCIBNClvUrQ)
- [ ] Instagram audience built before release; TikTok treated as lower reach (EuaV0qc6UXQ)
- [ ] Friend or creator YouTube partnership planned for launch window (EuaV0qc6UXQ)
- [ ] Post-launch update plan ready to address prominent YouTuber criticism (EuaV0qc6UXQ)
- [ ] Retention planned around ~700 CCU baseline, not the 1,700 peak (EuaV0qc6UXQ)

## How the advice changed over time
- June 2026 focus was progression systems, placeholder art and devlog reels (WCIBNClvUrQ); August 2026 advice adds pre-launch playtesting, a post-playtest fix window, console/mobile support and YouTuber-driven updates (EuaV0qc6UXQ). These extend rather than contradict each other.
- August 2026 reflection says solo development was a speed disadvantage and suggests a team for large scope. Treat this as the most recent guidance on team size.
- October 2026 modelling workflow (z04_RTBiMgg) reaffirms the earlier low-poly and baked-texture approach; no contradiction found.

## Theme notes
- [[studiorookroblox - Retention|Retention]]
- [[studiorookroblox - Discovery & Algorithm|Discovery & Algorithm]]
- [[studiorookroblox - Updates & Live Ops|Updates & Live Ops]]
- [[studiorookroblox - Studio & Scripting|Studio & Scripting]]
- [[studiorookroblox - Mindset & Process|Mindset & Process]]
- [[studiorookroblox - Games Mentioned]]
- [[studiorookroblox - Numbers & Benchmarks]]
- [[studiorookroblox - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-11-04 - Spiral Roblox Devlog 1 — Roblox Horror Game With Procedural Floors|Spiral | Roblox Devlog #1 — Roblox Horror Game Wit]] (817 views, 2025-11-04): Spiral devlog #1 on procedural horror floors; transcript is empty, so only the title is usable.
- [[2026-05-29 - Trench Devlog Main Menu and Model Showcase|Trench Devlog: Main Menu and Model Showcase]] (603 views, 2026-05-29): Trench main menu and model showcase; the transcript is only 'Heat', so little advice is extractable.
- [[2026-06-10 - Trench Devlog - Data Stores and More!|Trench Devlog - Data Stores and More!]] (501 views, 2026-06-10): Solo Trench update: DataStore progression, two equip slots, 4-player lobbies, and reels reaching 501 views.
- [[2026-08-09 - How I Made a Front Page Roblox Game... In 2 Months! Roblox Trench Deca|How I Made a Front Page Roblox Game... In 2 Months]] (29,386 views, 2026-08-09): Jam win to front page in about 2 months: Instagram reach, 200-player playtest, peak 1,700 CCU, then decline.
- [[2026-10-21 - Gatling Gun Full Modelling Process Trench Decay|Gatling Gun Full Modelling Process | Trench: Decay]] (4,404 views, 2026-10-21): Unedited Gatling gun build: Plasticity low-poly, Blender topology, Substance texturing; audio muted.
