---
title: PossiblePanda - How to make successful Roblox games
tags: [roblox, possiblepanda, playbook]
videos: 12
generated: 2026-10-29
credibility: trusted
credibility_score: 8.3
creator_trust: TRUSTED
creator_score: 8.3
---

> [!note] Trust: TRUSTED (credibility audit score 8.3): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# PossiblePanda - How to make successful Roblox games

PossiblePanda's advice is developer-tooling advice, not a full game-success formula. His core position: build on small, open-source Luau libraries for each system (UI, state, permissions, data, admin commands, cleanup, zones) and keep authority on the server. Build UI on the client. Use typed data templates and validated registries. Protect player data with session locking, kick-on-failed-load, and reconcile. Keep debug and admin tools hidden behind keys like F2. He does not cover game ideation, monetisation, marketing, or live-ops planning beyond data and debugging basics.

**Style:** Hands-on, library-by-library walkthroughs (install, minimal code, demo). Honest about gaps, such as QueryAuth having no formal docs yet, and shows a failed plugin attempt. Suits intermediate developers who want to adopt specific packages rather than a design or marketing playbook.

## Playbook
1. **Idea: pick systems before genre** [[game-ideas-and-genres]]: Creator's videos do not cover game concepts, genre choice, or market validation. Scope the project by systems it needs: UI, shared state, permissions, saved data, admin tools, zones. Each maps to one of the libraries he covers.
2. **Build: set up packages and project structure** [[version-control-and-tooling]]: Install libraries via Wally or release .rbxm into a packages folder in ReplicatedStorage. Use Wally to keep versions updated. Load shared modules with a loader (RbxUtil Loader) rather than scattered requires.
3. **Build: client-side UI with Fusion** [[code-architecture-and-frameworks]]: Create Fusion scopes (fusion.scoped) listing every function used. Store UI data in scope:value state, read it with peek(), and wrap reusable components as ModuleScripts that take a props table. Create state inside the component function.
4. **Build: preview components in UI Labs** [[development-process-and-speed]]: Write a .story ModuleScript per component and expose controls (color, text size). Group stories into a storybook so you can iterate on UI outside gameplay before wiring it into the game.
5. **Build: shared state with Charm** [[code-architecture-and-frameworks]]: Use typed atoms for player points and items, update them from client scripts, and bridge them into Fusion UI through a helper module. Use server-side atoms and replication when state must be shared between server and client.
6. **Build: server-authoritative permissions and remotes** [[anti-exploit-and-security]]: Gate doors and actions with QueryAuth composable conditions (team, rank, premium, account age). Expose game actions through Net static RemoteEvents declared once in ReplicatedStorage. Validate on the server.
7. **Build: player data with ProfileStore or Scribe** [[data-persistence]]: Define a typed data template. Start a session per player, kick them if the profile fails to load, add profile:AddUserId for GDPR deletion, call profile:Reconcile() after load, and kick on OnSessionEnd. Scribe offers an alternative with replication and leaderboards.
8. **Build: static data registries with validation** [[luau-language-and-types]]: Store item definitions as ModuleScripts in a folder. Use RegistryFactory get, exists, and getAll, and assert required fields at startup so bad data fails before play. Type-cast registry contents with exported types.
9. **Build: zones, timers, and cleanup** [[scripting-and-performance]]: Create zones from tags with QuickZone observer enter/exit callbacks. Use Timer.new(interval) instead of while-wait loops. Track connections and instances with Scythe scopes and clean them with scythe.clean, checking scythe.isAlive first.
10. **Test: debug menus and Studio data access** [[testing-debugging-and-qa]]: Toggle Iris debug windows and Conch commands with F2, kept off by default. Enable Studio Access to API Services before testing DataStores. Test persistence by reloading sessions and inspecting data.
11. **Launch: log economy events** [[analytics-metrics]]: Pass an economy analytics transaction type and item SKU whenever currency changes so economy flows are logged automatically (Scribe example). Check that logs fire during playtests before release.
12. **Growth: share packages publicly** [[trailers-and-video-marketing]]: Creator grows his audience by releasing open-source packages with tutorial videos (QueryAuth tutorial reached 5,125 views at listing). No evidence on Roblox discovery or ad strategy.
13. **Live ops: reconcile schema changes** [[updates-live-ops]]: When you add new template keys, Reconcile adds them to existing player data automatically. Keep data templates typed so schema changes are visible in editor checks.
14. **Live ops: admin commands for support** [[updates-live-ops]]: Use role-permissioned Conch commands (for example kick, debug give-money) for moderation and debugging. Keep them hidden and restricted to admin roles in production.

## Key numbers
- Xi--YI0Hk7M: QueryAuth took about 1 day to build (creator statement)
- Xi--YI0Hk7M: 5,125 video views at listing (2025-11-09)
- aSE2D4_TwoU: Timer demo interval is 2 seconds (demo value)
- aSE2D4_TwoU: Net demo fires remote after 5-second delay (demo value)
- KVmPyoOPmRI: inventory quantity 1-64 per stack (Scribe.int bounds in example)
- KVmPyoOPmRI: max 10 inventory items (array cap in example template)
- KVmPyoOPmRI: starting money 0, +50 test increment on join (example values)
- gjUtuovH41w: demo points +150 per update and +1 per second timer (example values, not real metrics)
- AOAh-4Q9ARw: example diamond pickaxe durability 3,000 (sample data, not a metric)
- C0cOB7Xqc1M: creator benchmark FPS with 500 moving entities and 10,000 zones: QuickZone 60, QuickBounds 58, SimpleZone 5, ZonePlus 4
- 0rmh0FpHBYM: Enable Studio Access to API Services is required for DataStores in Studio
- L-2GA_xX-SA: Iris debug menu toggled with F2
- B6VDcOTKKRY: Conch debug menu bound to F2 and includes a mock give-money command

## Common mistakes
- Stray or extra comma, or forgetting to return the instance from a Fusion component function (3e406QQHt7o)
- Reading Fusion 0.3 state with :get() instead of peek(value) (3e406QQHt7o)
- Creating state outside the component, so every instance shares one counter (3e406QQHt7o)
- Forgetting Iris End after each window, causing overlapping draws and error buildup (L-2GA_xX-SA)
- Passing an Iris.State object directly instead of reading it with :get() (L-2GA_xX-SA)
- Connecting to Iris button events instead of checking clicked() per frame in an if statement (L-2GA_xX-SA)
- Letting players play when the profile fails to load, which loses unsaved progress (0rmh0FpHBYM)
- Accessing player data before the profile loads, causing nil errors (0rmh0FpHBYM)
- Testing DataStores in Studio without enabling Studio Access to API Services (0rmh0FpHBYM, KVmPyoOPmRI)
- Calling scythe methods on scope objects instead of scythe.add(scope, object), since scopes are numeric IDs (WN1S4BDrrDg)

## Launch checklist
- [ ] Debug and admin menus (Iris, Conch) are off by default and toggled by a key (L-2GA_xX-SA, B6VDcOTKKRY)
- [ ] Enable Studio Access to API Services and test DataStore saves (0rmh0FpHBYM)
- [ ] Kick the player if the profile fails to load (0rmh0FpHBYM)
- [ ] Call profile:AddUserId(player.UserId) for GDPR deletion (0rmh0FpHBYM)
- [ ] Call profile:Reconcile() after load to add new template keys (0rmh0FpHBYM)
- [ ] Kick players on profile.OnSessionEnd (0rmh0FpHBYM)
- [ ] Block gameplay until data is loaded with an is-loaded check (0rmh0FpHBYM)
- [ ] Assert required fields on registry data at startup (AOAh-4Q9ARw)
- [ ] Type-cast data template and registry contents with exported types (0rmh0FpHBYM, AOAh-4Q9ARw)
- [ ] Build Fusion UI in client-side scripts to keep server load down (3e406QQHt7o)
- [ ] Preview each UI component as a story before wiring it into the game (qo0x-Et5NPk)
- [ ] Use Timer instead of while-wait loops for intervals (aSE2D4_TwoU)
- [ ] Pass economy analytics transaction type and SKU on every currency change (KVmPyoOPmRI)
- [ ] Check scythe.isAlive(scope) before scythe.clean(scope) (WN1S4BDrrDg)
- [ ] Verify permission conditions on protected doors and actions (Xi--YI0Hk7M)
- [ ] Clone atom tables with table.clone before modifying them (gjUtuovH41w)
- [ ] Route all game actions through server-validated remotes (aSE2D4_TwoU)
- [ ] Benchmark zone-heavy scenes if using zone libraries (C0cOB7Xqc1M)

## How the advice changed over time
- Newest videos (Scribe, Charm, Conch, Scythe, QuickZone; Sep-Oct 2026) add state, admin, cleanup, and zone systems. They do not retract earlier advice.
- Fusion 0.3 (Nov 2025) requires peek(); Charm (Sep 2026) moves shared state into atoms and bridges them into Fusion UI. Use Charm for state shared across components and Fusion scope:value for component-local state.
- ProfileStore (Dec 2025) recommends it over ProfileService. Scribe (Sep 2026) adds a second player-data option with replication, gifting, and leaderboards. No video says ProfileStore is superseded.
- Scribe's Studio plugin attempt failed in the newest data video, so the creator now recommends a fallback when using plugins for data inspection.

## Theme notes
- [[PossiblePanda - Studio & Scripting|Studio & Scripting]]
- [[PossiblePanda - Mindset & Process|Mindset & Process]]
- [[PossiblePanda - Games Mentioned]]
- [[PossiblePanda - Numbers & Benchmarks]]
- [[PossiblePanda - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-11-04 - Fusion 0.3 Roblox Open Source Showcase 1|Fusion 0.3 | Roblox Open Source Showcase #1]] (17,401 views, 2025-11-04): Fusion 0.3 tutorial: scopes, scope:new, peek state, and reusable props-based component ModuleScripts.
- [[2025-11-05 - Iris Roblox Open Source Showcase 2|Iris | Roblox Open Source Showcase #2]] (8,156 views, 2025-11-05): Iris immediate-mode debug GUI: Init/End, buttons, input states, F2 toggle, and live FPS.
- [[2025-11-07 - UILabs Roblox Open Source Showcase 3|UILabs | Roblox Open Source Showcase #3]] (14,575 views, 2025-11-07): UI Labs story-booking walkthrough for previewing Fusion UI outside gameplay with live controls.
- [[2025-11-09 - QueryAuth Roblox Open Source Showcase 4|QueryAuth | Roblox Open Source Showcase #4]] (5,125 views, 2025-11-09): QueryAuth composable permission checks for team, rank, premium, and account-age doors.
- [[2025-12-21 - RbxUtil - Loader, Signal, Timer, Net Roblox Open Source Showcase 5|RbxUtil - Loader, Signal, Timer, Net | Roblox Open]] (7,121 views, 2025-12-21): RbxUtil tour: Loader, Signal, Timer instead of while loops, and static Net remotes.
- [[2025-12-29 - ProfileStore Roblox Open Source Showcase 6|ProfileStore | Roblox Open Source Showcase #6]] (5,805 views, 2025-12-29): ProfileStore walkthrough: typed data template, session locking, kick-on-fail, money and items.
- [[2026-01-27 - RegistryFactory Roblox Open Source Showcase 7|RegistryFactory | Roblox Open Source Showcase #7]] (5,903 views, 2026-01-27): RegistryFactory builds typed, assert-validated registries from ModuleScript static item data.
- [[2026-09-20 - Charm Roblox Open Source Showcase 9|Charm | Roblox Open Source Showcase #9]] (11,472 views, 2026-09-20): Charm atoms, effects, and computeds for typed player state, bridged into Fusion UI.
- [[2026-09-20 - Scribe Roblox Open Source Showcase 8|Scribe | Roblox Open Source Showcase #8]] (20,058 views, 2026-09-20): Scribe player data: typed template, server increments, economy analytics, persistence testing.
- [[2026-09-25 - Conch Roblox Open Source Showcase 10|Conch | Roblox Open Source Showcase #10]] (16,632 views, 2026-09-25): Conch command bar: role-permissioned commands like kick and a debug give-money command.
- [[2026-09-27 - Scythe Roblox Open Source Showcase 11|Scythe | Roblox Open Source Showcase #11]] (22,931 views, 2026-09-27): Scythe memory-efficient cleanup with numeric scopes, scythe.add, and scythe.clean.
- [[2026-10-04 - QuickZone Roblox Open Source Showcase 12|QuickZone | Roblox Open Source Showcase #12]] (8,618 views, 2026-10-04): QuickZone tag-based zones with observer enter/exit; creator benchmark beats ZonePlus on FPS.
