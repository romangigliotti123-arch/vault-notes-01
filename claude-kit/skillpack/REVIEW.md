# Skill pack review log

Scored against [QUALITY.md](QUALITY.md) by the author on 2026-11-01 (self-review; an independent critic pass has NOT been done). Rows: T trigger, I inputs, P procedure, M Studio MCP path, F fallback, E evidence, O output, A acceptance checks, C code, R pitfalls/related. Each 0-2, built = at least 16/20 and no zero.

Honesty rules used for the scores:
- M is 1 for every skill that names Studio MCP calls, because NO Studio MCP call in this pack has been run live (the host cannot sign in to Studio). It is 2 only where the skill correctly says MCP is not needed.
- A is 2 only when an acceptance item is a command with a quotable result (a test, a script, a recount); 1 when every item is a manual judgement.
- C is 1 for Studio-side audit scripts that pass stylua/selene/luau-lsp but were never run in Studio; 2 for pure logic that passes Lune tests, or for no-code skills where no code is right.
- Weak evidence (single indie source, unverified live facts) costs E a point.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| thumbnail-maker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | image_specs.py selftest and live-spec numbers passed in; no render-staging script |
| gamepass-maker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | feeds the kit Shop system (no duplicate code); Studio purchase flow untested |
| game-reviewer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | acceptance is manual; a scoring helper would lift A |
| model-cleaner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | audit_model.luau static-checked only |
| model-rebuild | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 17 | rebuild construction is described, not scripted; manifest.luau static-checked only |
| game-optimizer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | scan_place.luau static-checked only; profiler windows are manual |
| idea-validator | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | no executed check; verdict recount is by hand |
| core-loop-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | cycle times estimated until a prototype is measured |
| first-minute-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | timings estimated until measured |
| datastore-schema-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | re-scoped after finding PlayerData already migrates; module is the offline tester/validator, 8 Lune tests |
| remote-guard-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | RemoteGuard 8 Lune tests; bad-input run against real remotes untested |
| exploit-audit | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | audit_remotes.luau is a heuristic, static-checked only |
| playtest-bot-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Harness 4 Lune tests; never run as a live bot |
| devproduct-handler | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | re-scoped to the kit Shop system after finding it already owns ProcessReceipt; Catalogue 5 Lune tests incl. the real Shop |
| price-ladder-planner | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 19 | spacing rule rests on one indie DevForum guide, labelled |
| mobile-ui-audit | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | 44 px / 14 px thresholds are heuristics (labelled); ui_audit.luau static-checked only |
| game-description-writer | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | limits must be live-checked each run (by design) |
| ctr-ab-test-planner | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 18 | test-mechanism availability is not verified in this session |
| retention-diagnoser | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 19 | two of five floors are chosen by the skill, labelled as such; selftest passes |
| event-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | design skill, acceptance is manual |
| lag-hunter | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | remote_probe.luau static-checked only; the 10 calls/s triage number is the skill's own heuristic |
| script-profiler | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | bench.luau run once under Lune (output quoted in the build log); profiler windows manual |
| rig-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | check_rig.luau static-checked only |
| asset-license-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 2 | 17 | not legal advice; audio rules live-check; list_assets.luau static-checked only |
| discord-server-setup | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 18 | Discord age rule is general knowledge, not in the vault (flagged in the skill) |

Gaps common to all 25: no live Studio run, no independent reviewer, no measured improvement on a real game. Next review step: run each Studio-side script once in a real place and re-score C and M.


## Batch 4 (marketing)

Scored 2026-11-01 by the author on a cold re-read against QUALITY.md (no independent reviewer exists: no sub-agents allowed). The re-read found and fixed: a wrong "official guidance" label on a single-source localization tip, an unclear sourcing sentence in influencer-outreach-writer, a Studio-path line in sponsored-ad-reviewer that named irrelevant tools, and six skills whose acceptance checks had nothing executed (now wired to title_screen.py, image_specs.py, outreach_lint.py, shot_check.py, shorts_report.py, roles_check.py or a grep). Columns as above.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| game-icon-maker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | image_specs check runs only once art exists; glance test is manual |
| title-generator | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | title_screen.py selftest 10 assertions; limit is passed in, never built in |
| keyword-researcher | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 17 | Roblox publishes no search volumes: ranking is manual observation, labelled indie; acceptance leans on title_screen |
| tagline-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | reuses title_screen.py with tagline limits |
| store-page-audit | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | scorecard is judgement; executed part covers title and image specs only |
| screenshot-set-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | image_specs only once files exist; image count and quota are live-check |
| trailer-script-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | separates page vs external vs ad mode; shot_check.py selftest 8 assertions; cinematic/lyrics rules stay human |
| short-video-planner | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | almost all numbers indie self-reported (labelled); shorts_report.py selftest 7 assertions |
| influencer-outreach-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | outreach_lint.py selftest 7 cases; no price list exists in the vault, says so |
| press-kit-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | executed check is an ls of listed assets; usage rules left "owner to confirm" |
| launch-day-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | table generated by calendar_gen.py launch; Friday/Wednesday rule is multi-creator indie |
| social-post-calendar | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | calendar_gen.py selftest 5 assertions; cadence floor is a creator figure, labelled |
| update-announcement-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | headline checked with title_screen.py; truth-check table is manual |
| roblox-group-setup | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | roles_check.py selftest 5 cases; real Roblox permission names must be mapped live |
| store-localization-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | loc_check.py selftest 6 cases; quality of translation is a human judgement |
| brand-kit-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | contrast.py WCAG maths selftested (black on white = 21:1) |
| codes-campaign-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | CodeBook.luau luau-check clean + 6 Lune tests; codes.py selftest 150 unique codes; DataStore count and grant path untested; vault coverage of promo codes is thin (stated) |
| collab-pitch-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | executed check reuses outreach_lint; licensing terms are live-check and owner/lawyer decisions |
| sponsored-ad-reviewer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ad_read.py selftest 8 cases; thresholds are playbook defaults with override flags; 80% ad-cohort D1 line is an unsourced heuristic (labelled) |
| discovery-signal-reader | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | signal_read.py selftest 6 cases; floors indie/third-party, bounce has no target (says so) |
| community-showcase-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | executed check is a grep; Captures API behaviour untested |
| launch-teaser-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | phase timings are indie defaults; date check is partly by hand |

Gaps common to Batch 4: no Studio run (M stays 1), no independent reviewer, no live-checked Roblox page or Ads Manager values (every skill instructs a live check and none stores a fast-moving number as fact), no measured result on a real game. The 22 skills were not run end to end by a live `claude -p` session (forbidden by the brief).

## Batch 2 (systems + publish)

Cold re-read of each generated SKILL.md against QUALITY.md after building, by the same worker (NOT an independent agent). Checks done: every test number cited in Acceptance matches the real Lune test list (one mismatch, trading 'test 9' -> 8, fixed); lint 0 failing with CLAUDES_VAULT set; scripts formatted and checked by stylua, selene and luau-lsp. M is 1 everywhere except where no MCP is needed: no Studio MCP call was run live. Columns as above.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| currency-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Wallet 8 tests incl. real Shop retried receipt; DataStore/purchase untested |
| inventory-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Inventory 7 tests; vault has no stack-limit benchmark (said so) |
| trading-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Trade 10 tests incl. rollback and totals/uid conservation; crash-between-saves window narrowed not closed (stated); two-client race untested |
| pet-system-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Pets 6 tests; power curve is a labelled guess, evidence is indie case studies |
| crafting-system-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Crafting 5 tests; evidence for timers is indie-labelled |
| quest-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Quests 6 tests; UI/event hooks untested |
| leaderboard-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 18 | Leaderboard 6 tests with fake fetch; OrderedDataStore glue untested; request budget must be live-checked; overlaps installed roblox-leaderboards-and-events (scoped to tested logic) |
| rebirth-system-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Rebirth 6 tests; no verified vault numbers for curves (labelled) |
| upgrade-tree-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | UpgradeTree 5 tests; growth range 1.1-2 is an assumption (labelled) |
| loot-drop-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LootTable 9 tests incl. 20000 seeded rolls; egg-hatch merged in; disclosure rules need live check |
| boost-potion-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Boosts 6 tests; HUD untested |
| achievement-badge-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Achievements 5 tests; BadgeService behaviour untested and live-check; thin vault evidence |
| round-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 18 | Rounds 6 tests; overlaps installed roblox-round-based-game-loop (scoped to tested logic); cleanup leak check is a manual Studio step |
| checkpoint-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Checkpoints 6 tests; min stage time must come from playtest |
| spawn-system-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Spawns 5 tests; 3 s / 10 s limits are assumptions (labelled) |
| tool-weapon-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Weapons 5 tests; client prediction untested |
| hitbox-combat-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | HitCheck 6 tests; lag cap and cone are guesses (labelled); real latency untested |
| health-damage-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Health 6 tests; regen numbers are guesses; thin vault evidence |
| npc-spawner-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | NpcBudget 6 tests; caps must be measured on a device (stated) |
| lobby-matchmaking-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Matchmaker 6 tests; skill-based rating not covered (stated); teleports untested |
| teleport-hub-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Portals 5 tests; TeleportService calls untested |
| vehicle-system-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Vehicles 4 tests; ownership handover untested; evidence mostly general exploit guidance |
| kit-system-integrator | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | integrate_check.py selftest (3 scenarios); static only, not a live test |
| age-rating-prep | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | feature_scan.py selftest; questionnaire wording must be read live; keyword scan has false positives (stated) |
| publish-readiness-gate | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 19 | gate.py selftest (7 negative cases); 13 gates are this pack's synthesis of a longer vault checklist |

Gaps common to Batch 2: no Studio run; numeric defaults (cooldowns, caps, curves) are labelled assumptions, the vault has no verified benchmarks for them; trading crash-window not closed; two skills overlap installed skills (leaderboard, rounds) and say so.

## Batch 3 (scripting)
Reviewed cold against QUALITY.md after writing (separate pass: each SKILL.md re-read against the rubric, every command and runner snippet executed once, test counts compared with the numbers quoted in the skill). Fixes made in that pass: TweenKit lost its list when the last tween was cancelled before the new one was registered (found by the conflict test, fixed); TagBinder re-bound instances whose behaviour returned no cleanup (fixed with a bound marker); Retry gained the vault's official DataStore preset and throttle codes; cross-skill helpers are injected (selene/luau-lsp cannot resolve path requires), so DependencyMap, StrictPlan, ModulePlan and ActorDispatcher take their helpers as arguments.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| luau-type-annotator | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | TypeScan 7 Lune tests; behaviour check is the user's own test |
| module-architecture-planner | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 18 | side classification and 300/20 thresholds are heuristics (labelled); split proposals are judgement; ModulePlan 6 tests |
| event-bus-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Signal 7 tests; engine signal ordering untested |
| state-machine-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | StateMachine 7 tests incl. queued re-entry; real NPC use untested |
| cooldown-manager-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Cooldowns 7 tests; double-fire against a real remote untested |
| connection-leak-auditor | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | LeakScan is an indentation heuristic (labelled); Janitor and scan 9 tests; leaks must be confirmed with engine memory tools |
| strict-mode-migrator | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | StrictPlan 5 tests and runner snippet executed; effort buckets are the skill's own heuristic |
| require-cycle-finder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | RequireGraph 7 tests (Tarjan SCC, layers); dynamic requires invisible (stated) |
| actor-parallel-converter | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | reworked from 16: dispatcher got injectable io and 5 fake-Actor tests, ParallelBatch 7; worker template and real messaging static-checked only; Actor counts are indie figures (labelled) |
| tween-helper-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | TweenKit 6 tests with a fake service; real easing untested |
| raycast-recipes | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | reworked from 16: cast/clamp/sweep tested against a fake world (5 tests, Lune Vector3); real engine geometry untested |
| collision-group-setup | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | CollisionMatrix 6 tests; adapter must be written from the live WorldRoot docs (names not in the vault); assign() untested |
| attribute-config-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | AttributeConfig 8 tests with a fake instance; replication untested |
| object-pool-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Pool 6 tests; performance gain untested |
| input-handler-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | InputMap 6 tests with fake ContextActionService; Server Authority input rules need a live docs check |
| proximity-prompt-wiring | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | PromptGuard.evaluate 6 tests; bind() static-checked only |
| collection-tag-wiring | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | TagBinder 6 tests with a fake service; streaming timing untested |
| lune-unit-test-writer | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Mocks 7 tests; the vault has no coverage of unit-test frameworks (stated), Lune comes from the kit |
| error-logger-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | ErrorLog 7 tests; vault has no crash-reporting coverage so the sink design is the skill's own |
| deprecated-api-migrator | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | DeprecatedScan 8 tests; rules labelled vault or general, general ones need a docs check before use |
| retry-wrapper-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Retry 8 tests; error-message wording from real services untested |
| script-dependency-mapper | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | DependencyMap 4 tests and runner executed; alias and dynamic names missed (stated) |
| replicated-loader-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | ClientLoader 5 tests with a fake tree; real replication and streaming untested |

Two skills first scored 16 (actor-parallel-converter, raycast-recipes); both were reworked (injectable world / io plus Lune tests) and re-scored 18. Engine behaviour of both stays untested until a Studio run.

## Batch 5 (money)

Reviewed 2026-11-02 by the author in a separate re-read pass against QUALITY.md (still not an independent critic). Scoring rules as above. Executed checks: 11 Lune suites (check-scripts.sh skillpack/money) and 9 python `--selftest` runs; no Studio MCP call was run live.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| starter-pack-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | StarterOffer 6 tests; purchase window values are docs examples to live-check; purchase untested |
| vip-pass-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | PerkStack 6 tests; cap default 3 is the skill's heuristic (stated) |
| battle-pass-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | SeasonTrack 8 tests incl. idempotent claim and mid-season unlock; UI and purchase untested |
| subscription-planner | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 17 | subplan.py 5 selftest checks; no delivery code (kit has no subscription system); rules are fast-moving, single-source docs |
| offer-timing-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | OfferGate 7 tests; cooldown numbers are defaults to A/B test |
| premium-benefits-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | no code (correct); acceptance is mostly manual/kbq quote; Premium branch untestable in Studio |
| ugc-item-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | no code (correct); fees/commission are live-check; acceptance mostly manual |
| private-server-planner | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | privserver.py 5 selftest checks; vault gives no private-server share so it is a required input; thin KB |
| regional-pricing-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | regional.py 7 selftest checks; bounds 30-100% from pricing.md, live-check; no region lists encoded on purpose |
| economy-balancer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Economy 7 tests; thresholds 0.6/0.3 are defaults; model, not measurement |
| sink-source-mapper | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Ledger 5 tests; Grant/Spend wrapper pattern untested in a real project |
| pay-to-win-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | OfferLint 7 tests; encodes vault rules, not Roblox's validator; platform restriction API names live-check |
| receipt-flow-tester | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ReceiptScenarios 3 tests (passes kit Shop, fails a naive handler); live purchase script untested |
| pass-ownership-cache-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | OwnershipCache 8 tests; first step may conclude Shop already covers it; real API untested |
| shop-conversion-optimizer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | funnel.py 4 selftest checks; no universal conversion target in vault (stated); experiments untested |
| limited-offer-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LimitedWindow 5 tests; dissent on stock caps recorded |
| devex-planner | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 19 | devex.py 4 selftest checks; rates/rules fast-moving and partly conflicting across vault eras (flagged); MCP not applicable (correct) |
| price-optimization-readiness | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | price_scan.py 4 selftest checks and CLI run on a sample; clean scan is not eligibility proof (stated) |
| donation-system-builder | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Donations 7 tests; transfer API facts rest mainly on one DevForum notice plus talk, live-check; transfer flow untested |
| rewarded-ad-planner | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | ad_plan.py 4 selftest checks; beta eligibility and targets platform-reported, live-check |
| payer-segment-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | segments.py 6 selftest checks; concentration claims from mixed eras labelled as claims |
| upsell-moment-finder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | moments.py 4 selftest checks; correlation only (stated) |

Lowest: subscription-planner, ugc-item-planner, premium-benefits-planner, private-server-planner, donation-system-builder, rewarded-ad-planner (17-18); lifts: a live Studio/publish run, and a live-check of each platform rule on the build date.

## Batch 7 (ui)

Reviewed 2026-11-02 by the author in a separate re-read pass against QUALITY.md (not an independent critic). Scoring rules as above. Executed checks: 21 Lune suites (check-scripts.sh skillpack/ui), luau-check (stylua, selene, luau-lsp) on all ui scripts, skillpack.py lint. mobile-ui-audit (batch 1) is the reference bar and is unchanged.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hud-layout-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | HudLayout 6 tests; thumb-zone defaults illustrative (stated), real zones must come from the emulator |
| shop-ui-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ShopLayout 5 tests incl. dark-pattern audit; purchase flow only in a published place (untested) |
| ui-scale-fixer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ScaleMath 5 tests; Instance edits untested; example viewports illustrative |
| safe-area-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | SafeArea 4 tests; no device cutout numbers invented, read from emulator; engine inset behaviour untested |
| gamepad-ui-navigator | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | FocusNav 6 tests (geometry model, not the engine's own selection); real pad walk-through untested |
| ui-animation-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | UiMotion 5 tests; duration ceilings are heuristics (stated); feel untested |
| button-feedback-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ButtonState 7 tests incl. leave-cancels and locked states; Activated wiring untested in Studio |
| notification-system-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ToastQueue 6 tests with injected clock; limits are heuristics; vault has no toast-specific evidence (policy is the skill's own) |
| currency-display-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | CurrencyCounter 5 tests (floor formatting, no overshoot, snap); caught a Luau typing bug in checks |
| inventory-ui-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | InventoryView 6 tests; rendering/virtualisation untested |
| menu-flow-mapper | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | MenuGraph 5 tests; depth 3 is a heuristic; runtime-created screens need code search |
| font-and-color-picker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Contrast 5 tests incl. known #767676 pair; WCAG is an external standard, labelled |
| localization-ready-checker | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | TextFit 5 tests; expansion factors are general i18n heuristics not in the vault (stated), lift with measured translations |
| loading-screen-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LoadingProgress 6 tests (monotonic, capped, stall); real join time untested |
| tooltip-system-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | TooltipPlacement 6 tests; long-press/focus behaviour on devices untested |
| settings-menu-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Settings 6 tests incl. hostile payloads and migrations; persistence via PlayerData untested in Studio |
| damage-number-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | FloatingNumbers 6 tests; relies on object-pool-builder Pool (no duplicate); frame cost untested |
| minimap-planner | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | MinimapMath 5 tests incl. rotation case; vault evidence is indirect (world cues), decision test is the skill's own |
| accessibility-checker | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | Colorblind 5 tests; Machado matrices an approximation and photosensitivity guidance must be live-checked (stated) |
| ui-kit-consistency-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | Consistency 5 tests; ui_scan.luau passes the checks but was never run in Studio (C=1) |
| billboard-ui-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | BillboardFade 5 tests incl. hysteresis; frame-time gain untested |

## Batch 6 (build)
Reviewed cold against QUALITY.md after writing (separate pass: each SKILL.md re-read against the rubric, scripts formatted with stylua and checked with selene and luau-lsp, every Lune suite run). Fixes made in that pass: removed unsupported claims (heightmap banding advice, water-on-mobile claim, KB attribution for Rojo name mapping), corrected a pointer to a nonexistent Cluster.format, gave the 10 percent Persistent and 64 stud figures their labels, added the Blender Forward/Up/Embed Textures settings from the vault, fixed a Windows case-insensitive file clash (graybox.luau vs Graybox.luau, Studio script renamed build_graybox.luau). sky-atmosphere-setter was merged into lighting-preset-picker (near-duplicate: both set Lighting, Atmosphere and post effects), so the build category has 26 rows.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| palette-picker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Palette 7 Lune tests (WCAG contrast, Machado simulation, deltaE, grayscale gap); thresholds 12/25 are the skill's defaults |
| texture-budget-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | TextureBudget 5 tests; byte model is a labelled estimate, sizes must be supplied; inventory script static-checked only |
| terrain-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | TerrainPlan 7 tests (4 px per voxel, 4096 px tiles); terrain_audit static-checked only; heightmap height scaling needs a docs check |
| lod-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LodPlan 6 tests; lod_audit inlines the rules, LevelOfDetail enum name deliberately not written; 10 percent and 64 stud figures labelled |
| particle-effect-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ParticleBudget 7 tests; rate caps from the vault, live-particle budgets are labelled assumptions; audit static-checked only |
| sound-placement-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | SoundPlan 5 tests; densities and emitter cap are labelled defaults; sound_audit static-checked only |
| prop-set-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | PropKit 5 tests using the vault's instance figures; densities are inputs; prop_census static-checked only |
| part-to-mesh-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Cluster 5 tests; dump_parts static-checked only; export and visual match are the owner's and untested |
| graybox-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Graybox 7 tests; build_graybox inlines validation and builds in one undo step; build step untested in Studio |
| naming-convention-enforcer | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | NamingRules 5 tests; the convention is the skill's own and Rojo name mapping is general knowledge (labelled) |
| workspace-organizer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | OrganizerPlan 5 tests; organize skips script-referenced names and refuses when sources unreadable; apply untested in Studio |
| material-consistency-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | StyleStats 5 tests; read-only; thresholds are defaults; neon/glass lag figure is a single indie rating (labelled) |
| animation-priority-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | AnimRules 7 tests; anim_audit needs Play mode and owned animations; keyword table is the skill's convention |
| lighting-preset-picker | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | LightingPresets 6 tests (ranges, mobile trims, serializer); only the cartoon density/blur and warm ambient cite the vault, other values are starting points; sky-atmosphere-setter merged in |
| pivot-fixer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Pivot 5 tests; fix_pivots moves only the pivot (PivotOffset or WorldPivot) and was static-checked only |
| anchor-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | Engine-bound script, static-checked only (luau-lsp with Roblox definitions); AssemblyRootPart test and attribute convention are the skill's own |
| collision-fidelity-tuner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | Engine-bound script, static-checked only; refuses decor changes when script sources are unreadable; fidelity feel untested |
| union-fixer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | Engine-bound script, static-checked only; only fidelity is automated, replacement is a human or modelling job (stated) |
| attachment-fixer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | Engine-bound script, static-checked only; re-weld to PrimaryPart is the skill's convention; runtime-created welds invisible in Edit |
| accessory-fitting-guide | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | accessory_check static-checked only; R15 attachment names to be verified against a Rig Builder rig; UGC limits flagged live-check |
| animation-import-guide | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | play_test_animation static-checked only and rejects an empty id; exporter menu names flagged live-check |
| art-bible-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | No code of its own (correct); executed check is the Palette run; template and the five unifying elements follow the vault |

Gaps common to Batch 6: no Studio run (M stays 1), so every Studio-side script is static-checked only (stylua, selene, luau-lsp) and applying fixes was never exercised against a real place; no independent reviewer; figures the vault does not give (live-particle budgets, spot densities, texture budget, clearance multipliers, lighting values) are labelled defaults; UGC limits, exporter menus and enum names are flagged live-check.

## Batch 8 (perf)
Reviewed cold against QUALITY.md after writing (separate pass: every SKILL.md re-read against the rubric, doc-note paths checked to exist in the vault, related skills checked against CATALOGUE, scripts formatted with stylua and checked with selene and luau-lsp, every Lune suite run). Fixes from the pass: invalid KB path (retention-and-engagement.md) replaced by first-session-onboarding.md; unknown related skills removed; Workspace/Lighting properties missing from the type defs read through any-casts; two test-data bugs found by the suites (tie-break in LeakTrend.diff test, spike density in TickStats test). texture-memory-reducer was dropped as a near-duplicate of build/texture-budget-checker (same inventory, estimate and rank-by-saving job).

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| streaming-enabler | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | stream_audit engine-bound, static-checked only; radii and integrity read through any-cast (not in the type defs); StreamingEnabled effect untested on a device |
| part-count-auditor | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | PartBudget 4 tests; budgets are sourced (docs 1,000/1M, indie 5k parts) or labelled; count_regions static-checked only |
| memory-budget-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | MemoryBudget 5 tests incl. the docs 30-player 9.18 GiB example; tiers above 2 GB are a labelled heuristic |
| network-traffic-auditor | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | NetBudget 5 tests; byte sizes from vault figures, wire format unmeasured; reuses lag-hunter remote_probe |
| physics-load-reducer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | physics_census engine-bound, static-checked only; PhysicsSteppingMethod read through any-cast; sleep thresholds cited from docs |
| render-cost-auditor | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | render_census engine-bound, static-checked only; per-fix GPU gains not published, measure |
| join-time-reducer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | JoinTimeline 5 tests; docs give no seconds target (stated), budget is user supplied; join_marks static-checked only |
| mobile-perf-tester | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | MobileSession 5 tests; 25 percent thermal and 2x spike rules are heuristics; sampler untested on a device |
| heartbeat-loop-auditor | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LoopScan 6 tests; textual heuristic (indentation) so output is candidates only; loop_scan_studio needs the module placed in ServerStorage, untested in Studio |
| datastore-throttle-auditor | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | DataStoreBudget 5 tests from the docs formulas (live-check flagged); 60 percent warn and 50 percent autosave share are heuristics |
| animation-cost-reducer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | anim_census engine-bound, static-checked only; vendor gains (Dead Rails, 60 doors) are creator reports |
| npc-cost-reducer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | UpdateRate 5 tests (staggering gives exactly 10 per frame); ring Hz values are heuristics; texture overlap merged out (see Batch 8 note) |
| instance-leak-finder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LeakTrend 6 tests; slope/R2 thresholds heuristic; leak_watch static-checked only |
| server-tick-analyzer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | TickStats 5 tests; 33 ms stall line and run of 3 are heuristics; tick_sampler untested on a live server |
| ping-sensitivity-tester | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | set_lag static-checked only; IncomingReplicationLag is in the type defs but untested in Studio; packet loss and jitter explicitly untested; matrix is a heuristic |
| effects-budget-setter | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | EffectsBudget 5 tests; live-particle caps are a labelled heuristic because the vault gives none (E stays 1) |
| cpu-vs-gpu-diagnoser | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | BoundDiagnosis 5 tests encode the vault colour rules; the four inputs need a manual profiler read |

Gaps common to Batch 8: no Studio or device run (M stays 1), so every Studio-side script is static-checked only and no gain was measured on a phone; heuristic thresholds (warn bands, caps, rings) are labelled as such in each script header and SKILL.md; no independent human reviewer. Official numbers cited come from the vault's Creator Docs notes dated 2026-10-28 and are flagged live-check.


## Batch 9 (liveops)
Reviewed cold against QUALITY.md after writing (separate re-read of each SKILL.md against the rubric; every script's selftest or Lune suite run; skillpack.py lint with CLAUDES_VAULT set so every kb path is checked). Fixes from that pass: two selftest-found script bugs (patchlint balance regex, session stop-point rule), cohort selftest case, a muddled pitfall sentence in churn-reason-finder, and a hotfix-playbook line that implied the vault covers BindToClose (now labelled general practice). No planned row was merged or replaced: all 21 liveops rows built (the category already had retention-diagnoser and event-planner), reusing analytics-pull.py, the kit Analytics system, CodeBook and Admin. codes-system-builder stays distinct from codes-campaign-planner (design vs server implementation).

| skill | total /20 | notes / what would lift it |
|---|---|---|
| update-cadence-planner | 19 | cadence.py 5 selftests; 60/40 capacity split is a labelled default |
| patch-notes-writer | 19 | patchlint.py 4 selftests; wording heuristics are defaults; 60/99 char limits live-check |
| funnel-analyzer | 19 | funnel.py 4 selftests; 30 percent big-drop line is a default; Analytics step caps from kit README |
| cohort-reader | 19 | cohort.py 4 selftests; pooled z test ignores weekday and source mix (stated) |
| kpi-dashboard-planner | 18 | no code of its own (correct); executed check is analytics-pull --dry-run (shape only); API metric names beta |
| experiment-designer | 19 | experiment.py 6 selftests; textbook sample size, not Creator Hub's; API field names deliberately not written |
| feature-flag-config-builder | 18 | FlagConfig 8 Lune tests; real Configs fetch not written (live-check), glue untested |
| economy-health-monitor | 19 | econ_drift.py 6 selftests; verdict thresholds are defaults, cumulative change is not a wallet |
| churn-reason-finder | 19 | churn.py 4 selftests; correlation only (stated) |
| session-length-analyzer | 19 | session.py 5 selftests; bucket/stop rule is a default |
| ccu-forecaster | 18 | ccu.py 4 selftests; multipliers are user inputs or labelled placeholders; vault has only reported extremes |
| seasonal-calendar-builder | 19 | seasons.py 8 selftests (Easter, Thanksgiving computed); holiday list is a Western default (stated) |
| codes-system-builder | 18 | RedeemService 6 Lune tests with fake store; real UpdateAsync cross-server behaviour untested; vault has no code-redemption guide (stated) |
| hotfix-playbook | 18 | hotfix.py 5 selftests; severity scale is the skill's own (vault has none); BindToClose labelled general practice |
| rollback-planner | 19 | rollback.py 4 selftests; migration/backup rules labelled as the skill's practice |
| live-balance-tuner | 18 | TuneGuard 8 Lune tests; 25 percent / 1 h defaults labelled; live write is manual |
| feedback-synthesizer | 18 | feedback.py 6 selftests; keyword matching only (stated), counts mentions not players |
| metrics-snapshot-logger | 19 | snapshot.py 5 selftests; uses analytics-pull --json shape (last point of unbroken series); API beta |
| dau-drop-investigator | 19 | dau_drop.py 5 selftests; thresholds are defaults |
| ab-result-reader | 19 | abread.py 6 selftests; proportion metrics only, mean metrics via guardrail input (stated) |
| stat-sheet-explainer | 18 | no code (correct); executed check is analytics-pull --dry-run; page labels flagged live-check |

Gaps common to Batch 9: no Studio run (M stays 1), so Studio-side glue (Configs fetch, DataStore UpdateAsync, Analytics logging in Play) is untested; no independent human reviewer; thresholds not in the vault (sink ratio, big-drop, stop-point, step limits) are labelled skill defaults; Creator Hub page names and the Experiments/Configs/Analytics Query APIs are flagged live-check.

## Batch 10 (qa)

Scored 2026-11-02 by the author in a second cold pass against QUALITY.md (same agent, no sub-agent reviewer, so NOT independent). Honesty rules as above: M is 1 where Studio MCP calls are named but never run (2 only where MCP is correctly not needed); A is 2 only where an acceptance item is an executed command with quotable output; C is 1 for heuristic scanners and Studio-side scripts that were only static-checked.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| regression-checklist-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | checklist_lint.py selftest executed; rows' quality is judged by hand |
| bug-report-template | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 19 | bug_report_lint.py selftest; severity scale is the skill's own convention (labelled) |
| repro-step-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | no code (correct); executed check is the bug-report lint; confirmation run is manual |
| multiplayer-test-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | no code (correct); multi-client MCP run never executed; acceptance is by hand |
| edge-case-lister | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | no code (correct); seven axes are the skill's own checklist (labelled) |
| save-load-tester | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 2 | 17 | save_roundtrip.luau static-checked only, never run in Studio; needs published place + API access |
| purchase-flow-tester | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | PurchaseScenarios 3 Lune tests incl. real Shop 7/7 and a naive handler failing 4; real prompts/Robux untested |
| device-test-matrix | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Pairwise 7 tests; full 6-parameter example gives 17 rows of 864; real-device rows untested |
| output-error-triager | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LogParse 6 tests; impact weights are the skill's heuristic (labelled) |
| honeypot-remote-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Honeypot 6 tests; HoneypotService.luau glue static-checked only; weights are skill defaults |
| remote-fuzzer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | Fuzz 6 tests (naive handler caught, RemoteGuard-guarded clean, burst vs limiter); Instance-argument fuzzing needs the engine |
| dupe-exploit-hunter | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | LedgerCheck 8 tests + RaceScheduler reuse; flows are modelled, real two-client dupes untested |
| speed-teleport-detector | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | MovementCheck 10 tests; defaults are starting points; engine physics/vehicles untested |
| server-authority-checker | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | AuthorityScan 5 tests; name-based heuristic misses odd names (stated); every lead must be read |
| input-validation-auditor | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | ArgScan 5 tests; needs formatted code, misses helper-validated handlers (stated) |
| data-loss-simulator | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | DataLoss: kit PlayerData passes 8/8, naive saver fails the lock+autosave scenarios; real DataStore untested |
| join-leave-race-tester | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | RaceScheduler 6 tests (oversell found with schedule A1 B1 A2 B2, atomic version clean); model fidelity assumed |
| balance-sim-runner | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 19 | Sim 8 tests; every input is a design number, no vault benchmark is asserted; no Studio needed |
| load-test-planner | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | LoadMath 6 tests; platform limits deliberately not hard-coded (live-check), so evidence is thin |
| chat-filter-tester | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | FilterScan 5 tests; filter inside a helper looks unfiltered (stated); live filter behaviour untested |
| crash-log-reader | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 18 | CrashSignals 6 tests; keyword matching only, memory thresholds are indie-sourced; no Roblox error codes invented |
| secrets-leak-scanner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | SecretScan 8 tests plus folder runner run on a fixture (CRITICAL found, value redacted, exit 1) |

Gaps common to Batch 10: no Studio run (M stays 1), so Studio-side glue (HoneypotService, save_roundtrip, scanner runs inside Studio) is untested; no independent human or sub-agent reviewer; heuristic scanners (ArgScan, AuthorityScan, FilterScan, CrashSignals, SecretScan) produce leads, not verdicts, and say so; planned catalogue rows merged: none (22 built, save-load-tester kept apart from data-loss-simulator: live Studio round trip vs offline failure injection).


## Batch 11 (design)
Cold re-read by the author against QUALITY.md on 2026-11-02 (self-review, no independent human reviewer; no sub-agents used). Same honesty rules as above. Logic scripts have stdlib Python selftests (run with `python -I <script> --selftest`); `docheck.py` checks document STRUCTURE only (headings, placeholders, length), so skills whose only executed check is docheck score A=1.

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| one-sentence-pitch | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | docheck is structure only; cold-read test is manual |
| genre-twist-finder | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | 10-40 percent share is a judgement; Tizzy/AlvinBlox numbers self-reported |
| competitor-teardown | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | needs a played session for full value; web facts live-check |
| core-fantasy-definer | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | fantasy quality is judged by game-dev-critic, not the script |
| progression-curve-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | progcurve.py 6 selftests; thresholds are skill defaults; income values estimated until playtest |
| reward-schedule-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | rewardsched.py 6 selftests; paid-randomness policy is live-check |
| difficulty-tuner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | difficulty.py 5 selftests; thresholds are skill defaults; bot data is not human data |
| level-flow-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | levelflow.py 6 selftests; 16 studs/s is the Roblox default (live-check) |
| session-length-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | sessionplan.py 7 selftests; gap and tolerance are defaults |
| social-hook-designer | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | multi-client test not available via MCP (stated); platform averages are not your game's |
| tutorial-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | 20 percent skip threshold is a skill default; docheck structure only |
| scope-cutter | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 20 | reuses featureprio.py (4 selftests); weights are defaults |
| mvp-definer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | acceptance numbers are skill defaults from vault 30 s / 5 min rules; docheck structure only |
| gdd-one-pager | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 20 | docheck.py 6 selftests plus a real PASS/FAIL run; content quality still needs the critic |
| feature-prioritizer | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 20 | featureprio.py 4 selftests; impact scores are hypotheses (stated) |
| game-feel-polisher | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | 100 ms latency target is a default; latency measure needs a client run (untested) |
| boss-encounter-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | bosscheck.py 5 selftests; 0.5 s / 50 percent / 600 s are skill defaults |
| quest-chain-designer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 18 | docheck structure only; session-sized daily target is a default |
| world-theme-picker | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | readability test needs a greybox screenshot (untested until built) |
| sequel-planner | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 19 | case-study evidence is official-talk or tracker claims (labelled); decision rules are the skill's |

Gaps common to Batch 11: no Studio run (M stays 1 where MCP is named); no independent reviewer; design-skill outputs are scored for the critic by structure only (docheck), not by running game-dev-critic on a real design; all numeric thresholds not found in the vault (0.5 s wind-up, 8 percent quit, 3-minute reward gap, 10 s leg) are labelled skill defaults in the scripts.

## Batch 12 (community)

| skill | T | I | P | M | F | E | O | A | C | R | total | notes / what would lift it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| moderation-rules-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ladder_check 8-case selftest + CLI run on a sample CSV (all PASS); platform policy deliberately live-check |
| welcome-message-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | text_lint 8-case selftest; regex leads, human reads the text; shared by 12 community skills |
| faq-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | faq_cluster 4-assert selftest (singular/plural clustering); word-overlap only, human merges clusters |
| feedback-channel-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | no code (correct for the job); executed check is text_lint on the post templates; in-game form untested |
| tester-recruitment-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | roster_check 7-case selftest; thresholds labelled design defaults; vault admits no consent guidance, safety rules are conservative defaults |
| community-event-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | event_run dated beats verified by selftest and CLI (2026-12-05 -> tease Wed 2026-11-25); in-game hook untested |
| group-management-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | reuses roles_check.py (CLI run PASS) + payout_split 7 asserts; live payout rules deliberately not hard-coded |
| ambassador-program-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | reuses roles_check.py and text_lint; no new code; minors/payment rules are live-check items, evidence indirect |
| bug-intake-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | intake_triage 5-assert selftest + CLI run on a 3-row CSV (ranked P5.66 / P1.0); Studio reproduction untested |
| community-poll-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | poll_lint 9-case selftest + CLI run (leading wording flagged FAIL, rc=1 as designed) |
| creator-collab-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | program doc; reuses codes-campaign-planner and text_lint; no new code; disclosure/minors rules are live-check |
| social-proof-collector | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | proof_log 6-case selftest; permission/source/label rules enforced, no invented proof |
| toxicity-response-playbook | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | process doc; executed check is text_lint shaming/dm patterns; RED routing relies on live platform channels |
| support-macro-writer | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | macros linted by text_lint with --max-words 90; no compensation promised by default |
| fan-art-contest-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | contest_score 6-assert selftest (weights, missing/out-of-range scores, judge disagreement, ties) |
| leaderboard-hooks-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 18 | planning doc, build handed to leaderboard-builder; text_lint on copy; friends API live-check |
| clan-system-planner | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | ClanRules 6 Lune tests green; filtering/DataStore wiring untested (needs published place) |
| friend-invite-reward-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | InviteReward 6 Lune tests green; ReferredByPlayerId field name flagged for live-check; platform calls untested |
| streamer-kit-builder | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 19 | StreamerAlias 4 Lune tests green (1000 distinct aliases, order-independent); alias is a display hash, not security (stated) |

Gaps common to Batch 12: no Studio run (M stays 1), so engine-side wiring (invite prompts, join data, TextService filtering, DataStore persistence, private servers) is untested; self-review by the author with no separate reviewer (strict cold re-read done, scores capped accordingly); heuristic linters (text_lint, poll_lint, faq_cluster) give leads, not verdicts; platform policy on minors, payments, sponsorship and off-platform links is deliberately a live-check item. Planned rows merged: none (19 built; discord-server-setup was already built in batch 1).

## Batch 13 (publish)

Strict cold re-read against QUALITY.md after writing (author = reviewer; scores capped accordingly). Built = 17+ and no row at 0.

| skill | total /20 | notes / what would lift it |
|---|---|---|
| tos-compliance-checker | 19 | compliance_gap 2-scenario selftest + CLI run on a sample project (FAIL rc=1 as designed); reuses feature_scan; static hooks are leads only |
| chat-compliance-checker | 18 | reuses compliance_gap --focus chat; two-account filter test untested; rules read from live pages |
| paid-random-compliance | 19 | odds_check 4-case selftest + CLI run (95/5 -> 200 Robux EV); PolicyService branches untested without restricted account |
| ad-policy-checker | 18 | reuses compliance_gap --focus ads; creative review is manual; ad delivery untested |
| ugc-moderation-checker | 18 | path-table method + compliance_gap --focus ugc; filters/reporting untested; age rule conflict between two docs flagged for live-check |
| privacy-data-checker | 19 | rtbf_check selftest incl. template matching + CLI run; deletion end-to-end test is an owner step |
| regional-availability-checker | 18 | reuses compliance_gap --focus region; real country behaviour cannot be tested in Studio (stated) |
| experience-settings-configurator | 19 | settings_check 8-FAIL selftest with limit override; limits are a dated snapshot, live-check; dashboard untested |
| device-support-setter | 18 | device_scan selftest (FAIL/WARN paths); emulators approximate, device rows untested unless played |
| private-server-settings-setter | 19 | server_plan selftest incl. price-change ack and teleport-data scan; dashboard/teleport runtime untested |
| matchmaking-settings-setter | 18 | mm_config_check selftest (6 FAILs); config value untested until Preview/Test in Creator Hub |
| localization-setup | 19 | loc_scan selftest; chains to loc_check.py (selftest ok); Studio-side GUI text not seen by scan (stated) |
| version-history-keeper | 19 | release_log selftest (refusals, bumps, rollback order) + CLI add/check run; Version History is UI-only |
| place-backup-planner | 19 | backup_check selftest + CLI make/verify run; restore test is an owner step |
| post-launch-monitor | 19 | monitor_plan selftest (blank template must fail) + CLI run; template bug found and fixed during CLI run; real metrics untested |
| copyright-checker | 18 | ip_scan selftest + CLI run; legal status is not decidable by a script (stated) |
| audio-permission-checker | 19 | audio_check selftest + CLI scan run (missing id 111 FAIL); playback test with a non-collaborator is manual |
| thumbnail-guideline-checker | 18 | no new code: reuses image_specs.py with live-checked numbers (selftest ok); content rules by eye |
| experience-name-checker | 18 | no new code: reuses title_screen.py (selftest ok, CLI run PASS); description rules are a manual list |
| group-ownership-setup | 19 | transfer_gates selftest feeds gate.py (blank NO-GO, full GO); transfer itself is an owner action |
| collaborator-permissions-setter | 18 | no new code: reuses roles_check.py (selftest ok); real permission names mapped live |

Gaps common to Batch 13: no Studio run, so PolicyService branches, filter behaviour, Creator Hub dashboards, Version History and restore are untested; every policy fact is a dated snapshot of Creator Docs notes (2026-10-28) and each skill tells the user to live-check; heuristic scans give leads, not verdicts. Catalogue: 18 planned publish rows built, 3 rows added (ad-policy-checker, localization-setup, matchmaking-settings-setter) to cover ads policy, localization and matchmaking settings; publish category 23/23 built.

## Batch 14 (workflow)

Cold re-read by the author against QUALITY.md after writing; scored 0-2 per row on the ten rubric rows, only the total is recorded here. M (Studio MCP path) stays at 1 where no Studio run was possible. No skill below 17.

| skill | total /20 | notes / what would lift it |
|---|---|---|
| project-kickoff | 18 | wfdoc.py (shared by 22 workflow skills) selftest 5 cases + CLI PASS/FAIL on a real handoff doc; kickoff itself not run on a live project |
| task-breaker | 19 | tasks.py 6-case selftest + CLI run on 3-task CSV (waves A | B,C, critical path 5.0 h) |
| session-handoff | 18 | doc skill; wfdoc handoff PASS and missing-heading FAIL shown; git state step untested on a live project |
| git-workflow-setter | 19 | gitcheck.py 6-case selftest + CLI (msg PASS, bad branch FAIL); found kit template .gitignore lacks 5 entries (reported, not edited) |
| sprint-planner | 19 | sprint.py 4-case selftest + CLI (12.0 h capacity, solo factor applied, overflow listed); 3 h/day and 20% buffer are own defaults |
| decision-log-writer | 18 | doc skill; wfdoc decision check only; evidence labels are procedural |
| tech-debt-lister | 19 | debt.py 5-case selftest + CLI; score formula is own ranking aid (stated); fixed a test/formula mismatch found by selftest |
| ai-brief-writer | 19 | briefcheck.py 7-case selftest + CLI FAIL on a vague DONE WHEN item; thresholds are own |
| worker-verifier | 19 | reportcheck.py 8-case selftest + CLI REJECT on narration evidence; WARN is noisy for command names that look like paths (stated) |
| usage-budgeter | 18 | budget.py 4-case selftest + CLI (cap WARN, rc=1); weights are relative ratios from the Manager KB, not money; live-check prices |
| release-checklist-builder | 18 | doc skill; gates reuse luau-check/rojo build; Version History restore semantics flagged live-check |
| code-style-guide-writer | 18 | doc skill; enforcement delegated to existing luau-check; baseline count untested on a live project |
| folder-structure-planner | 19 | foldercheck.py 3-case selftest + CLI PASS on the kit template project; Explorer match untested without Studio |
| dependency-pinner | 19 | pincheck.py 4-case selftest + CLI PASS on template rokit.toml (5 entries); network version freshness is live-check |
| ci-check-setter | 19 | hookgen.py 4-case selftest; real git repo test with installed stylua/selene/luau-lsp: bad file BLOCKED rc=1, good file rc=0 |
| changelog-writer | 19 | changelog.py 4-case selftest + CLI on 3 subjects (Added/Fixed/Unsorted) |
| docs-writer-roblox | 19 | moddoc.py 5-case selftest + run on systems/Shop/src/Shop.luau (8 functions found = 8 definitions); multi-line types show first line only (stated) |
| onboarding-new-dev | 18 | doc skill; setup commands are instructions to run on a clean clone, not run here |
| scope-creep-guard | 19 | scopeguard.py 5-case selftest + CLI FAIL on an under-sized swap (rc=1); swap rule is own policy (stated) |
| post-mortem-writer | 18 | doc skill; evidence-mark check via wfdoc; no real incident to run it on |
| team-roles-planner | 18 | doc skill; Team Create menu paths flagged live-check (2021 guidance) |
| milestone-reviewer | 19 | milestone.py 5-case selftest + CLI HOLD on an untested row (rc=1) |
| kb-lookup-routine | 18 | vault-find (manager hits) and kbq find/section run in this session; wfdoc kblookup check only |
| studio-mcp-session-planner | 17 | no Studio run in this batch; tool names taken from roblox-studio-connect; plan untested against a live MCP |
| playtest-evidence-logger | 18 | doc skill; wfdoc playtestlog needs evidence marks; Studio mode untested here |
| devlog-writer | 18 | added row (devlog not in original plan); numbers only from files; posting stays with the user |
| asset-pipeline-planner | 18 | added row; grep acceptance check is executed; Creator Hub upload and AI-content rules are live-check |

Gaps common to Batch 14: no Studio MCP run (engine-side steps stay untested); 22 skills share wfdoc.py, which checks structure and evidence marks only, not truth; heuristics (briefcheck, reportcheck, debt score, swap rule, budget weights) are the skill's own and labelled so. Catalogue: devlog-writer and asset-pipeline-planner ADDED to cover devlog and asset-pipeline topics; total 307; no rows merged.
