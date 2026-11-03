---
title: ArTheDev - How to make successful Roblox games
tags: [roblox, arthedev, playbook]
videos: 17
generated: 2026-10-29
credibility: trusted
credibility_score: 8.5
creator_trust: TRUSTED
creator_score: 8.5
---

> [!note] Trust: TRUSTED (credibility audit score 8.5): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# ArTheDev - How to make successful Roblox games

Build small, finish, then scale. ArTheDev teaches Roblox as systems design: decompose a game into reusable ModuleScripts (state manager, animation handler, cooldowns, inventory, weather, abilities) driven by config tables. The server owns state, hits and data; clients handle input, UI, VFX and sound. Persist data by UserId with pcall. Start with a small finished game rather than a dream project, since learning and finishing matter more than money or virality. Launch, growth and monetisation are essentially absent from the 17 videos.

**Style:** Code-first, modular-architecture tutorial creator for beginner-to-intermediate scripters. Uses 'Stop doing X' framing and breaks systems into reusable ModuleScripts. Later 2026 videos turn motivational, stressing finishing small games. Best for learners building systems; offers little on launch, marketing or monetisation.

## Playbook
1. **Pick a small, finishable first game** [[development-process-and-speed]]: Scope to one system such as a shop, door or simple obby. A finished obby in about 1 week teaches more than an abandoned big RPG; six months of planning a dream game is the trap. (wG9XzLnJC5k, 3FB6ZzAON8I)
2. **Learn basics, then build on your own** [[mindset-and-strategy]]: Use tutorials for basics only (basics playlist, DevForum, mini projects). Read toolbox code critically but never run or insert it. Repetition beats watching more tutorials. (R3q6hZs8FDE, wG9XzLnJC5k)
3. **Decompose the idea into modules and config** [[code-architecture-and-frameworks]]: Split into input, states, animations, hitboxes, cooldowns, knockback and inventory modules. Keep rates, pools, weights, weather types and base cooldowns in one config ModuleScript so tuning edits numbers, not logic. (Aoc9HkGHu_8, Iy9xuT1bpY4, CnZEnFVAFSw, _6F6vRt_9sM)
4. **Persist player data safely** [[data-persistence]]: Key by player.UserId, never Name. Wrap DataStore calls in pcall and check success. Newer code uses UpdateAsync. Autosave on a loop (300 s default) and save on PlayerRemoving. Enable Studio API access. (RDjsR4iIRlg, V7PdX03D_hM)
5. **Keep the server authoritative** [[client-server-and-remotes]]: Clients only request actions; the server decides state, hits, damage, knockback and party checks. Reject requests when the player is blocked or stunned and send a decline back. Use WaitForChild for character and leaderstats on the client. (Pi8rQ9gGTKE, QRFuxryK4Vg, 5QZA1_0L9PU)
6. **Harden remotes and inputs** [[anti-exploit-and-security]]: Validate ability names against a known table and error on mismatch. Add a 10 s invite cooldown via an invitedBy attribute. Clamp dash and slide velocity by fixed values, not delta time. Never trust client hit results. (5QZA1_0L9PU, KaCj7Jld35Q, QRFuxryK4Vg)
7. **Centralise animations** [[3d-modeling-rigging-and-animation]]: Use one animation handler ModuleScript for load, play, stop and cleanup. Set Action priority, match R6 or R15 to the rig, publish via Animation Editor, copy the asset ID, preload, and keep tracks non-looping. Add an is-playing guard. (csxJTfPVW8U, Pi8rQ9gGTKE)
8. **Run VFX on the client** [[vfx-and-particles]]: Put each effect's emitters in an attachment, stamp EmitCount, EmitDelay and EmitDuration attributes on every emitter, and drive effects from a client FX handler with task.delay. The server only validates abilities. (HjDD_0cDfPg, CnZEnFVAFSw)
9. **Build UI with scale sizing and tweens** [[ui-ux-design]]: Size bars by scale (0-1) inside their background frame. Tween XP bars over about 2 s instead of snapping. Use Heartbeat updaters and disconnect old connections on re-trigger. Bind controller and keypad inputs beside keyboard. (V7PdX03D_hM, _6F6vRt_9sM, KaCj7Jld35Q)
10. **Tune combat feel with explicit timings** [[combat-and-gameplay-systems]]: Use a 0.1 s perfect-block window, a 1.5 s combo reset, a 0.5 s M1 cooldown and a 6 s stun on hit. Stun uses a stored end time and a coroutine loop; overlapping hits extend via math.max. Use ProximityPrompt, not ClickDetector. (Pi8rQ9gGTKE, WImDkrf3sAo)
11. **Debug each system before combining** [[testing-debugging-and-qa]]: Expect debugging to take longer than writing code. Test each module alone, use a visual test part to tune offsets, and treat fixing as the core skill. (3FB6ZzAON8I, QRFuxryK4Vg)
12. **Publish the finished small game** [[development-process-and-speed]]: The creator's launch advice is only to finish and publish. The 17 videos give no store page, thumbnail, pricing or marketing guidance; research those elsewhere. (wG9XzLnJC5k)
13. **Grow through community, not stated tactics** [[community-and-discord]]: The creator pushes Discord and channel membership. No discovery, ad, retention or revenue figures are given in these videos. (RDjsR4iIRlg, 3FB6ZzAON8I, wG9XzLnJC5k)
14. **Ship live updates via config and announcements** [[updates-live-ops]]: Retune rarity weights, rates and weather chances from the config module. Broadcast global announcements with MessagingService to all servers and push TextChatService messages to each client. (fIwzczfIu2U, CnZEnFVAFSw, Iy9xuT1bpY4)

## Key numbers
- Invite timeout 10 s; invite cooldown 10 s via invitedBy attribute (5QZA1_0L9PU)
- M1 combo max 3 hits, combo reset 1.5 s, M1 cooldown 0.5 s (Pi8rQ9gGTKE)
- Perfect block window 0.1 s; stun on hit 6 s; attack lockout 0.5 s (Pi8rQ9gGTKE)
- Evasive i-frames 1.5 s, evasive cooldown 10 s (Pi8rQ9gGTKE)
- Stun demo duration 1.5 s in state manager example (WImDkrf3sAo)
- Sprint: 2 s double-tap window, 1.5x base speed (base 12 = 18); double-jump flag reset 0.3 s (KaCj7Jld35Q)
- Weather chances: sunny 40%, rain 20%, cloudy, partly cloudy, foggy, snow 10% each; tick 1 s (CnZEnFVAFSw)
- Autosave interval 300 s default (RDjsR4iIRlg)
- Summon: 1 to 10 per request; reveal wait 2 s single, 0.5 s multi; click debounce 0.5 s; blur 24 during, 0 after (Iy9xuT1bpY4)
- Summon price conflict in notes: 50 gems at tier 1 vs 200 gems single default; demo starts with 600 gems. Verify in video (Iy9xuT1bpY4)
- XP bar tween 2 s (V7PdX03D_hM)
- Cooldown example: base 0.4 s; add +5 s modifier to reach 7 s (_6F6vRt_9sM)
- Ability demo: 7 s cooldown, 6 s client lock, 2.5 s windup, 6 s hitbox lifetime, 4 s hit-loop (QRFuxryK4Vg)
- VFX: PointLight tween 0.5 s; destroy after 7 s, disconnect 4 s later (HjDD_0cDfPg)
- Planning a dream game: 6 months example vs finishing a simple obby in about 1 week (wG9XzLnJC5k)

## Common mistakes
- Starting with a dream game and planning for months instead of shipping a small finished one (wG9XzLnJC5k)
- Letting clients set states or decide hits; the client must only request and the server must decide (Pi8rQ9gGTKE, QRFuxryK4Vg)
- Keying DataStore entries or cooldown tables by Name instead of UserId (V7PdX03D_hM, _6F6vRt_9sM)
- Forgetting Game Settings > Security > Enable Studio Access to API Services, so DataStore fails in Studio (V7PdX03D_hM)
- Not clearing per-player state tables on PlayerRemoving, so the server slows over time (WImDkrf3sAo)
- Using ClickDetector for interactions, which does not work on mobile (WImDkrf3sAo)
- Anchoring the root to block knockback; set WalkSpeed and JumpPower to zero and restore them instead (Pi8rQ9gGTKE, Aoc9HkGHu_8)
- Running or inserting toolbox items without reading them, since they can hide malicious code (R3q6hZs8FDE)
- Skipping preload or the is-playing guard, so first casts lag and spammed inputs overlap animations (csxJTfPVW8U)
- High emission rate with long lifetime and low speed, which clumps particles and drops FPS; also leaving effect rotation at zero when it faces the wrong way (HjDD_0cDfPg)

## Launch checklist
- [ ] Game is one small, finished system or loop; not a dream scope (wG9XzLnJC5k)
- [ ] Enable Studio Access to API Services before testing DataStore (V7PdX03D_hM)
- [ ] All DataStore keys use player.UserId; every GetAsync, SetAsync or UpdateAsync sits in pcall (V7PdX03D_hM, RDjsR4iIRlg)
- [ ] Autosave loop running (300 s default), save on PlayerRemoving, and per-player state tables cleared (RDjsR4iIRlg, WImDkrf3sAo)
- [ ] Every remote validates on the server: state, cooldown, ability name, party membership (QRFuxryK4Vg, 5QZA1_0L9PU)
- [ ] Invite spam limited with a 10 s invite cooldown via invitedBy attribute (5QZA1_0L9PU)
- [ ] Dash and slide velocity clamped by fixed values, not delta time (KaCj7Jld35Q)
- [ ] Animations published, Action priority, rig type matches, preloaded and non-looping (csxJTfPVW8U)
- [ ] Effects parented to attachments; emitter rate, lifetime and speed checked for FPS (HjDD_0cDfPg)
- [ ] Rarity weights, rates and weather chances live in one config ModuleScript (Iy9xuT1bpY4, CnZEnFVAFSw)
- [ ] UI sized by scale; bars tween about 2 s; Heartbeat connections disconnected on re-trigger (V7PdX03D_hM, _6F6vRt_9sM)
- [ ] Controller and keypad inputs bound alongside keyboard (KaCj7Jld35Q)
- [ ] ProximityPrompt used for interactions instead of ClickDetector (WImDkrf3sAo)
- [ ] Cooldowns routed through one module; every ability uses the same can-use check (_6F6vRt_9sM)
- [ ] Ability names validated; mismatches error loudly rather than failing silently (QRFuxryK4Vg)
- [ ] Toolbox items read but never run or inserted (R3q6hZs8FDE)
- [ ] Each module tested alone before the full game is combined (3FB6ZzAON8I)
- [ ] Announcement path ready via MessagingService; monetisation, store page and thumbnail decided elsewhere, as these videos do not cover them (fIwzczfIu2U, wG9XzLnJC5k)

## How the advice changed over time
- Early 2025 videos (V7PdX03D_hM, 5QZA1_0L9PU) are single-script code walkthroughs; from mid-2025 the focus moves to modular systems (WImDkrf3sAo, csxJTfPVW8U, _6F6vRt_9sM) and 'Stop doing X' framing.
- DataStore writes: the 2025 leveling video wraps GetAsync and SetAsync; the 2026 inventory video (RDjsR4iIRlg) uses UpdateAsync with autosave. Prefer UpdateAsync for new code.
- Ability hit detection: 2025 combat (Pi8rQ9gGTKE) uses GetPartBoundsInBox; the late-2026 ability system (QRFuxryK4Vg) uses Heartbeat with OverlapParams. Prefer the newer approach.
- Learning advice shifts: R3q6hZs8FDE (2026-03) offers a basics playlist and a seven-method learning path, while the 2026-05 and 2026-06 videos (3FB6ZzAON8I, wG9XzLnJC5k) stress building repeatedly and using tutorials only for basics. Prefer the later stance.
- Cooldown handling: 2025 cooldown manager (_6F6vRt_9sM) centralises timers per UserId; the 2026 ability video (QRFuxryK4Vg) uses state-based cooldowns. Both are presented as valid; no explicit deprecation.
- Tone moves from purely technical in 2025 to motivational in 2026 (3FB6ZzAON8I, wG9XzLnJC5k, R3q6hZs8FDE), with emphasis on finishing small games.

## Theme notes
- [[ArTheDev - Retention|Retention]]
- [[ArTheDev - Game Ideas|Game Ideas]]
- [[ArTheDev - Studio & Scripting|Studio & Scripting]]
- [[ArTheDev - Mindset & Process|Mindset & Process]]
- [[ArTheDev - Games Mentioned]]
- [[ArTheDev - Numbers & Benchmarks]]
- [[ArTheDev - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-03-18 - 🔥 How to Make a LEVELING SYSTEM with DataStore in Roblox Studio! (Save|🔥 How to Make a LEVELING SYSTEM with DataStore in ]] (5,136 views, 2025-03-18): DataStore leveling: save level, XP and max XP by UserId, show leaderstats, and tween the XP bar.
- [[2025-03-20 - 🎉 How to Create a CUSTOMIZABLE PARTY SYSTEM in Roblox Studio! (Invite|🎉 How to Create a CUSTOMIZABLE PARTY SYSTEM in Rob]] (5,649 views, 2025-03-20): Party system with name-search invites, 10 s timeout, size cap, leader-only invites and attribute-based UI sync.
- [[2025-07-13 - You NEED a State Manager in Your Roblox Game (Here’s Why)|You NEED a State Manager in Your Roblox Game (Here]] (97,732 views, 2025-07-13): Reusable player state manager with timed, auto-expiring states and a stun system for combat.
- [[2025-07-16 - Stop Playing Animations Like This – Use an Animation Handler Instead|Stop Playing Animations Like This – Use an Animati]] (42,324 views, 2025-07-16): Animation handler ModuleScript centralising load, play, stop and cleanup, with an is-playing guard.
- [[2025-07-20 - Don’t Build Your Combat System Until You Watch This|Don’t Build Your Combat System Until You Watch Thi]] (38,598 views, 2025-07-20): Why combat breaks: animation conflicts, hitboxes, input spam and state clashes; use modular architecture.
- [[2025-07-25 - The Combat System Tutorial Everyone's Been Waiting For – Roblox Studio|The Combat System Tutorial Everyone's Been Waiting]] (54,889 views, 2025-07-25): Full modular combat build: server hitboxes, perfect block, guard break, combos and i-frames.
- [[2025-07-31 - Stop Using wait() For Cooldowns – Build a Pro Roblox Cooldown Manager|Stop Using wait() For Cooldowns – Build a Pro Robl]] (13,326 views, 2025-07-31): Client-synced cooldown manager with per-UserId timers, modifiers and countdown bars via RemoteEvent.
- [[2025-10-03 - Make Your Game Feel Next Level. Advanced Roblox Movement System Tutori|Make Your Game Feel Next Level. Advanced Roblox Mo]] (41,613 views, 2025-10-03): Modular movement with double-tap sprint, dash, slide and double jump, synced via attributes and a remote.
- [[2026-03-31 - How To ACTUALLY Learn Scripting In Roblox Studio|How To ACTUALLY Learn Scripting In Roblox Studio.]] (46,635 views, 2026-03-31): Seven ways to learn scripting compared, plus a path from basics to small systems before full games.
- [[2026-04-03 - How To Make A Customizable Weather System + Day Night Cycle Tutorial R|How To Make A Customizable Weather System + Day Ni]] (10,617 views, 2026-04-03): Data-driven weather types with weighted random picks, a day-night cycle and late-joiner sync.
- [[2026-04-06 - Build a Modular Inventory System in Roblox Studio (Datastore + GUI + E|Build a Modular Inventory System in Roblox Studio ]] (7,793 views, 2026-04-06): Modular inventory: item data, UpdateAsync autosave DataStore, server add/remove functions and GUI remotes.
- [[2026-04-18 - You NEED This Roblox Summoning System (Full Setup Guide)|You NEED This Roblox Summoning System (Full Setup ]] (2,958 views, 2026-04-18): Weighted-rarity summon system with a rates config, server validation, saved unit IDs and reveal GUI.
- [[2026-05-04 - Roblox Scripting Stops Being About Coding|Roblox Scripting Stops Being About Coding]] (12,688 views, 2026-05-04): Roblox scripting is about decomposing ideas into systems, debugging and consistent practice, not syntax.
- [[2026-06-07 - Your First Roblox Game Should Be Bad|Your First Roblox Game Should Be Bad]] (2,002 views, 2026-06-07): Your first game should be small and finished; learning and finishing beat ambitious abandoned projects.
- [[2026-09-26 - How to Make Global Announcements in Roblox|How to Make Global Announcements in Roblox]] (619 views, 2026-09-26): Global announcements: formatted TextChatService messages, RemoteEvent to clients, MessagingService across servers.
- [[2026-09-30 - The RIGHT Way to Handle VFX in Roblox|The RIGHT Way to Handle VFX in Roblox]] (11,830 views, 2026-09-30): VFX structure: attachments per effect, stamped emit attributes, client FX handler; server only validates.
- [[2026-10-05 - The Ability System Tutorial You Actually Need|The Ability System Tutorial You Actually Need]] (1,965 views, 2026-10-05): Modular ability system: skill-set modules, client input remote, dispatcher, server hitboxes and cooldowns.
