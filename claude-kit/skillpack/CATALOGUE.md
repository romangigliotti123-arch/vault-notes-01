# Roblox skill pack - catalogue

Every planned skill with its one-line job. Skills live in `skillpack/<category>/<name>/SKILL.md` (kit folder `.rbx/claude-kit/skillpack/`) and are loaded on demand with `/rbx <name>`; they are NOT installed as skills, so they cost no context until used. Status `built` = full skill exists and passes `skillpack.py lint`; `planned` = name and purpose fixed, not written yet (`/rbx <name>` then does a best-effort job from the purpose and the vault, and says so).

Quality bar: [QUALITY.md](QUALITY.md). Search: `/rbx find <words>`. Statuses are rewritten by `python tools/skillpack.py catalogue --write`.

Totals: 310 skills, 310 built, 0 planned.

## design - Design and ideas

| skill | what it does | status |
|---|---|---|
| idea-validator | Score a game idea against the vault's proven-loop, one-sentence and young-mobile tests before any build time is spent | built |
| core-loop-designer | Turn a premise into one three-layer core loop with cycle times, feedback beats and a cut list of competing systems | built |
| first-minute-designer | Script the first 30 seconds to 5 minutes (spawn, first action, first reward, reason to stay) with a timed checkpoint list | built |
| game-reviewer | Review a Roblox game (yours or a rival's) from its page and a play session: loop, retention, monetisation, packaging, with a scored verdict | built |
| one-sentence-pitch | Compress an idea into the single sentence a stranger can repeat, with title and thumbnail implications | built |
| genre-twist-finder | Pick the 10-20 percent twist on a proven genre formula and test that it stays instantly readable | built |
| competitor-teardown | Break a top competitor into transferable patterns (never content) with sources and a what-to-copy-as-pattern list | built |
| core-fantasy-definer | Write the role and feeling the player buys into and check every feature serves it | built |
| progression-curve-designer | Design level, XP and unlock curves with quick early wins and a visible long-term goal | built |
| reward-schedule-designer | Plan what drops when: fixed, variable and milestone rewards by time horizon without paid randomness | built |
| difficulty-tuner | Set difficulty ramps and fail states from playtest data so players are challenged but not stuck | built |
| level-flow-planner | Plan the path, landmarks, pacing and rest spots of a map or obby before building geometry | built |
| session-length-designer | Shape target session length, natural stopping points and return hooks | built |
| social-hook-designer | Add co-play and friend-invite hooks that make a session with a friend likelier | built |
| tutorial-designer | Teach one mechanic at a time through contextual, skippable, show-dont-tell triggers | built |
| scope-cutter | Cut a feature list to what the core loop needs, with a deferred list and reasons | built |
| mvp-definer | Define the smallest playable version with pass/fail acceptance tests and a one-week build order | built |
| gdd-one-pager | Write a one-page game design doc an AI or a teammate can build from | built |
| feature-prioritizer | Rank candidate features by loop impact, cost and risk with an explicit score table | built |
| game-feel-polisher | List the juice pass (sound, tween, particle, camera, haptic beats) for each core action | built |
| boss-encounter-designer | Design a readable boss or wave encounter: telegraphs, phases, rewards and fairness checks | built |
| quest-chain-designer | Design a quest or objective chain that teaches systems and paces rewards | built |
| world-theme-picker | Choose a setting and art direction that matches the fantasy and is cheap to build and read on mobile | built |
| sequel-planner | Decide whether to update, spin off or sequel a game, with the evidence rules | built |

## systems - Core loops and game systems

| skill | what it does | status |
|---|---|---|
| pet-system-builder | Plan and wire pets: hatch, equip, stats, rarity tiers and inventory limits without paid randomness | built |
| inventory-system-builder | Server-owned inventory with slots, stacking, limits and a client view | built |
| trading-system-builder | Safe player-to-player trading with confirm steps, dupe guards and logs | built |
| crafting-system-builder | Recipes, ingredients, timers and queue handling as data-driven modules | built |
| quest-system-builder | Data-driven quest tracker with progress events, rewards and save fields | built |
| leaderboard-builder | Global and server leaderboards with ordered DataStores and cache-friendly refresh | built |
| lobby-matchmaking-builder | Lobby, queue, teleport-to-match and return flow for round games | built |
| round-system-builder | Intermission-round-reward state machine with late joiners and cleanup | built |
| checkpoint-system-builder | Obby checkpoint and stage save with respawn and anti-skip checks | built |
| spawn-system-builder | Team, safe and respawn spawn logic with protection windows | built |
| currency-system-builder | Multi-currency wallet with sources, sinks and server-authoritative changes | built |
| rebirth-system-builder | Prestige loop with reset rules, multipliers and save schema | built |
| upgrade-tree-builder | Data-driven upgrade tree with prerequisites, costs and respec rules | built |
| tool-weapon-system-builder | Tools and weapons with server-validated activation, cooldowns and ammo | built |
| hitbox-combat-builder | Melee and ranged hit detection with server checks and lag allowance | built |
| health-damage-builder | Health, damage types, armor, regen and death handling | built |
| npc-spawner-builder | Spawn, patrol, aggro and despawn rules for NPCs with a cost cap | built |
| loot-drop-builder | Weighted loot, egg and crate rolls with pity, odds shown, server rolls and a drop log (egg-hatch merged in) | built |
| boost-potion-builder | Timed boosts that stack safely, persist across sessions and show on the HUD | built |
| achievement-badge-builder | Badges and achievements awarded server-side with idempotent checks | built |
| teleport-hub-builder | Hub world with portals, TeleportService reserved servers and party carry | built |
| vehicle-system-builder | Vehicle spawn, ownership, seats, network ownership and cleanup | built |
| kit-system-integrator | Wire the kit's tested systems (PlayerData, Shop, DailyRewards, Analytics, Admin) into a project and verify | built |

## scripting - Luau scripting

| skill | what it does | status |
|---|---|---|
| datastore-schema-builder | Design a versioned save schema and migrations for the kit's PlayerData system and test them offline with old-record fixtures | built |
| remote-guard-builder | Generate a validated, rate-limited RemoteEvent and RemoteFunction wrapper for a project | built |
| luau-type-annotator | Add strict-mode types to an untyped module without changing behaviour | built |
| module-architecture-planner | Split a growing script into services and modules with a dependency map | built |
| event-bus-builder | Typed signal or event bus for decoupled systems with leak-safe disconnects | built |
| state-machine-builder | Reusable state machine for NPCs, rounds and abilities | built |
| cooldown-manager-builder | Per-player cooldown and debounce helper used by every remote | built |
| connection-leak-auditor | Find connections, loops and instances that are never cleaned up | built |
| strict-mode-migrator | Move a codebase to --!strict one module at a time with a fix order | built |
| require-cycle-finder | Detect circular requires and propose a break | built |
| actor-parallel-converter | Move a hot loop to Actors and parallel Luau safely | built |
| tween-helper-builder | Small tween and animation utility module with cancel and chaining | built |
| raycast-recipes | Pick and write the right raycast, spatial query or overlap call with correct params | built |
| collision-group-setup | Design collision groups and the matrix, then script them | built |
| attribute-config-builder | Config via attributes and a tunable ModuleScript with live-change hooks | built |
| object-pool-builder | Pool frequently spawned instances (projectiles, effects, damage numbers) | built |
| input-handler-builder | One input layer for keyboard, gamepad, touch and ContextActionService | built |
| proximity-prompt-wiring | Server-validated ProximityPrompt interactions with distance and state checks | built |
| collection-tag-wiring | CollectionService tag-driven behaviours instead of per-part scripts | built |
| lune-unit-test-writer | Write Lune unit tests with mocks for pure game logic | built |
| error-logger-builder | Centralised pcall wrapper and error reporter with throttling | built |
| deprecated-api-migrator | Find deprecated Roblox APIs and replace them with current ones, checked against docs | built |
| retry-wrapper-builder | Backoff-and-retry helper for DataStore, MarketplaceService and HTTP calls | built |
| script-dependency-mapper | Map which scripts touch which remotes, folders and modules | built |
| replicated-loader-builder | Safe client bootstrap that waits for shared modules and assets | built |

## build - Building, models and assets

| skill | what it does | status |
|---|---|---|
| model-cleaner | Audit and clean a model: names, anchors, collision, unions, scripts, unused parts, pivots, with a report and safe auto-fixes | built |
| model-rebuild | Rebuild an imported or messy model as an efficient, organised one (meshes, hierarchy, pivots) without changing how it looks | built |
| rig-checker | Validate R15 or custom rigs: joints, attachments, naming, animation compatibility | built |
| asset-license-checker | Check the provenance and rules of Toolbox and third-party assets before shipping | built |
| part-to-mesh-planner | Decide which part clusters become meshes and how to export them | built |
| union-fixer | Replace risky unions with parts or meshes and fix collision fidelity | built |
| lighting-preset-picker | Pick a lighting, atmosphere, sky, fog, bloom and colour-grading preset by mood and device budget, dry-run diff then apply (sky-atmosphere-setter merged in) | built |
| terrain-planner | Plan terrain regions, materials and water that perform on mobile | built |
| graybox-builder | Block out a level with plain parts and a playtest checklist before art | built |
| art-bible-writer | Write the palette, shape language and material rules a team can follow | built |
| palette-picker | Pick a consistent colour palette with contrast and colour-blind checks | built |
| material-consistency-checker | Find off-style materials, textures and colour outliers in a place | built |
| naming-convention-enforcer | Apply and verify naming rules across Workspace and ReplicatedStorage | built |
| workspace-organizer | Reorganise the Explorer into a clear folder structure with Rojo-safe names | built |
| collision-fidelity-tuner | Set CollisionFidelity, CanCollide, CanTouch and CanQuery by purpose | built |
| anchor-checker | Find unanchored parts that fall, jitter or cost physics | built |
| prop-set-planner | Plan a reusable prop kit that builds a whole map cheaply | built |
| texture-budget-checker | Audit texture and mesh sizes against memory budgets | built |
| accessory-fitting-guide | Walk the UGC accessory path: fit, cage, validate, publish | built |
| animation-priority-checker | Fix animation priorities, looping and overrides | built |
| animation-import-guide | Export, upload and wire animations with correct settings | built |
| particle-effect-planner | Design cheap, readable VFX with budgets per effect | built |
| sound-placement-planner | Plan music, ambience and SFX with a mix and cost plan | built |
| pivot-fixer | Fix model pivots and primary parts so placement and rotation behave | built |
| attachment-fixer | Repair attachments, welds and constraints that break models | built |
| lod-planner | Plan render fidelity, streaming and distance culling for detail-heavy scenes | built |

## ui - UI and UX

| skill | what it does | status |
|---|---|---|
| mobile-ui-audit | Audit every screen for phone size, touch targets, safe areas, scale and legibility | built |
| hud-layout-planner | Plan a HUD that shows only what the loop needs, in thumb-safe zones | built |
| shop-ui-planner | Design a shop screen that converts without dark patterns | built |
| ui-scale-fixer | Convert Offset-based UI to Scale with constraints and test at several aspect ratios | built |
| safe-area-checker | Check notch, inset and corner safe areas on phones | built |
| gamepad-ui-navigator | Make menus navigable with a controller | built |
| ui-animation-planner | Plan tweened open, close and feedback animations that stay cheap | built |
| button-feedback-designer | Define hover, press, disabled and purchase feedback states | built |
| notification-system-planner | Toast and alert queue with priority and spam limits | built |
| currency-display-designer | Currency counters with change animation and plus-to-shop buttons | built |
| inventory-ui-planner | Grid inventory with filters, sorting and selection states | built |
| menu-flow-mapper | Map screens, entry points and back paths and remove dead ends | built |
| font-and-color-picker | Choose readable fonts and a UI colour system | built |
| localization-ready-checker | Find text that will break in other languages and wire translation | built |
| loading-screen-builder | Loading screen with real progress and tips | built |
| tooltip-system-builder | Tooltips that work on touch as well as mouse | built |
| settings-menu-builder | Settings menu with saved preferences | built |
| damage-number-builder | Pooled, readable damage and reward numbers | built |
| minimap-planner | Decide whether a minimap earns its screen space and plan it | built |
| accessibility-checker | Colour-blind, motion and text-size accessibility pass | built |
| ui-kit-consistency-checker | Find inconsistent corner radii, strokes, fonts and spacing | built |
| billboard-ui-planner | In-world nameplates and prompts with distance fade and cost cap | built |

## perf - Performance and optimisation

| skill | what it does | status |
|---|---|---|
| game-optimizer | Measure, rank and fix a game's performance (memory, CPU, network, join time) with before/after numbers | built |
| lag-hunter | Find the cause of lag or rubber-banding from symptoms, using profiler and remote traffic evidence | built |
| script-profiler | Profile Luau scripts with the Script Profiler and MicroProfiler and rank hot spots | built |
| streaming-enabler | Turn on and tune StreamingEnabled and fix the scripts it breaks | built |
| part-count-auditor | Count parts, meshes, unions and effects by region against a budget | built |
| memory-budget-planner | Set per-device memory budgets and track against them | built |
| network-traffic-auditor | Measure remote calls and replication volume and cut them | built |
| physics-load-reducer | Reduce unanchored parts, constraints and touch events | built |
| render-cost-auditor | Find shadow, transparency, light and effect cost | built |
| join-time-reducer | Cut time to first playable with preloading and deferral | built |
| mobile-perf-tester | Test on a real low-end phone and record frame time and memory | built |
| heartbeat-loop-auditor | Find expensive per-frame loops and replace with events or throttling | built |
| datastore-throttle-auditor | Find DataStore request bursts and queue overflow | built |
| animation-cost-reducer | Reduce animated rig cost for crowds | built |
| npc-cost-reducer | Scale AI update rate by distance and relevance | built |
| instance-leak-finder | Find instance counts that grow over time | built |
| server-tick-analyzer | Diagnose slow server heartbeat and long frames | built |
| ping-sensitivity-tester | Test gameplay under added latency and packet loss | built |
| effects-budget-setter | Set particle, beam and trail caps per scene | built |
| cpu-vs-gpu-diagnoser | Decide whether a frame drop is CPU or GPU bound and where | built |

## money - Monetisation

| skill | what it does | status |
|---|---|---|
| gamepass-maker | Design a game's gamepass set (what, price tier, when offered) from the vault's rules and wire it into the kit's Shop system with a Creator Hub checklist | built |
| devproduct-handler | Define the developer-product catalogue, wire it into the kit's Shop system (idempotent ProcessReceipt) and verify every grant offline | built |
| price-ladder-planner | Build a Robux price ladder with tiers, spacing and test plan from the vault's sourced rules | built |
| starter-pack-designer | Design the first-purchase offer and the moment to show it | built |
| vip-pass-designer | Design a VIP tier with perks that do not break the economy | built |
| battle-pass-designer | Design a season pass with free and paid tracks and fair pacing | built |
| subscription-planner | Evaluate and plan Roblox subscriptions for an experience | built |
| offer-timing-planner | Choose the moments in a session where offers convert | built |
| premium-benefits-planner | Use Premium-related engagement and payouts without pressure | built |
| ugc-item-planner | Plan UGC and avatar items that fit the game | built |
| private-server-planner | Price and configure private servers | built |
| regional-pricing-checker | Review regional pricing settings and bounds | built |
| economy-balancer | Balance currency sources and sinks with a simulation | built |
| sink-source-mapper | Map every currency source and sink and find inflation | built |
| pay-to-win-checker | Check offers against pay-to-win and paid-randomness rules | built |
| receipt-flow-tester | Test purchase flows end to end including failures | built |
| pass-ownership-cache-builder | Cache pass ownership safely with refresh on purchase | built |
| shop-conversion-optimizer | Find the reasons a shop does not convert and fix order | built |
| limited-offer-designer | Design limited-time offers without dark patterns | built |
| devex-planner | Plan cashing out: thresholds, fees, timing, records | built |
| price-optimization-readiness | Check eligibility and scripting rules for automatic price tests | built |
| donation-system-builder | Donation boards and tip flows done safely | built |
| rewarded-ad-planner | Plan rewarded ad placements and rewards | built |
| payer-segment-planner | Segment players into spend bands and tailor offers | built |
| upsell-moment-finder | Find the moments of need to attach an offer | built |

## marketing - Marketing and discovery

| skill | what it does | status |
|---|---|---|
| thumbnail-maker | Produce a game thumbnail set end to end: concept, composition, mobile-size check, A/B variants, upload checklist | built |
| game-description-writer | Write the title, description and keyword set for the experience page, checked against the vault's rules | built |
| ctr-ab-test-planner | Plan thumbnail, icon and title tests with one variable each and a decision rule | built |
| game-icon-maker | Design and check a game icon that reads at small phone size | built |
| title-generator | Generate and screen game titles for clarity and search | built |
| keyword-researcher | Research genre keywords and competitors' naming for search | built |
| trailer-script-writer | Script a short trailer or video ad with hook, proof and call to play | built |
| screenshot-set-planner | Plan the gallery images that sell the loop | built |
| short-video-planner | Plan TikTok and Shorts clips that show the hook in seconds | built |
| influencer-outreach-writer | Write respectful creator outreach with a clear offer | built |
| press-kit-builder | One-page press kit with facts, art and contact | built |
| launch-day-planner | Hour-by-hour launch day plan with monitoring | built |
| social-post-calendar | A month of posts tied to updates and events | built |
| update-announcement-writer | Write the update post for Roblox and Discord | built |
| roblox-group-setup | Set up the group page, roles and wall | built |
| store-page-audit | Audit the experience page for first-impression problems | built |
| store-localization-writer | Write store text for other languages | built |
| brand-kit-builder | Colours, logo, fonts and tone for all assets | built |
| codes-campaign-planner | Plan redeem codes tied to milestones and creators | built |
| collab-pitch-writer | Pitch a cross-promotion or collab | built |
| sponsored-ad-reviewer | Review an ad campaign's results and choose the next test | built |
| discovery-signal-reader | Read impressions, CTR and PTR and decide what to fix first | built |
| tagline-writer | Short taglines and hooks for ads and pages | built |
| community-showcase-planner | Showcase player creations and clips as marketing | built |
| launch-teaser-planner | Pre-launch teasers and waitlist plan | built |
| unslop-pass | Edit AI-sounding store, update and community text into specific human copy | built |

## liveops - Analytics and live-ops

| skill | what it does | status |
|---|---|---|
| retention-diagnoser | Diagnose D1/D7 retention problems against benchmarks and name the likely cause and the first test | built |
| event-planner | Plan a limited-time event: theme, rewards, schedule, balance for casual and grinding players, rollback plan | built |
| update-cadence-planner | Set a realistic update cadence and content pipeline | built |
| patch-notes-writer | Write clear patch notes players read | built |
| funnel-analyzer | Build and read onboarding and purchase funnels | built |
| cohort-reader | Compare cohorts before and after a change | built |
| kpi-dashboard-planner | Choose the few metrics that matter and their targets | built |
| experiment-designer | Design a Creator Hub experiment with hypothesis, variants, metric and duration | built |
| feature-flag-config-builder | Live config and feature flags for tunable values | built |
| economy-health-monitor | Track sources, sinks and wallet balance for drift | built |
| churn-reason-finder | Find why players leave using session and feedback data | built |
| session-length-analyzer | Analyse session length distribution and fix stop points | built |
| ccu-forecaster | Forecast concurrent players around events | built |
| seasonal-calendar-builder | A year of seasonal content slots | built |
| codes-system-builder | Redeem code system with limits and logging | built |
| hotfix-playbook | Steps to ship and verify an emergency fix | built |
| rollback-planner | Plan reversible releases and data rollbacks | built |
| live-balance-tuner | Tune values live from data without a publish | built |
| feedback-synthesizer | Cluster player feedback into ranked themes | built |
| metrics-snapshot-logger | Log the day's numbers for trend comparison | built |
| dau-drop-investigator | Investigate a sudden drop in players | built |
| ab-result-reader | Read A/B results with significance and guardrails | built |
| stat-sheet-explainer | Explain Creator Hub analytics pages and what to do about each | built |

## qa - Testing, QA and security

| skill | what it does | status |
|---|---|---|
| exploit-audit | Audit remotes, prompts and economy code for exploitable trust in the client and return ranked findings with fixes | built |
| playtest-bot-writer | Write a scripted bot or execute_luau harness that plays the core loop and asserts outcomes | built |
| regression-checklist-builder | Build the checklist to re-run after each change | built |
| bug-report-template | A bug report format that gets bugs fixed | built |
| repro-step-writer | Turn a vague bug into exact reproduction steps | built |
| multiplayer-test-planner | Plan multi-client tests for sync and race bugs | built |
| edge-case-lister | List the edge cases a feature must survive | built |
| save-load-tester | Test save, load, leave and shutdown paths | built |
| purchase-flow-tester | Test every purchase path including failure and refunds | built |
| device-test-matrix | Which devices and settings to test and how | built |
| output-error-triager | Read the Output log and rank errors by impact | built |
| honeypot-remote-builder | Add trap remotes and a ban or flag policy | built |
| remote-fuzzer | Fuzz remotes with bad values in a test place | built |
| dupe-exploit-hunter | Hunt item and currency duplication paths | built |
| speed-teleport-detector | Detect speed and teleport cheating server-side | built |
| server-authority-checker | Check that the server owns every outcome | built |
| input-validation-auditor | Check every client argument is validated | built |
| data-loss-simulator | Simulate DataStore failure and shutdown | built |
| join-leave-race-tester | Test joins and leaves during critical flows | built |
| balance-sim-runner | Simulate economy and combat balance in Lune | built |
| load-test-planner | Plan a load test with many clients | built |
| chat-filter-tester | Verify all user text goes through filtering | built |
| crash-log-reader | Read client and server crash reports | built |
| secrets-leak-scanner | Scan a project for ids, keys and secrets that should not ship | built |

## community - Social and community

| skill | what it does | status |
|---|---|---|
| discord-server-setup | Design a game community Discord: channels, roles, rules, bots, onboarding and the feedback loop | built |
| moderation-rules-writer | Clear community rules and an enforcement ladder | built |
| faq-writer | Write the FAQ from real player questions | built |
| feedback-channel-planner | Pick and run the right feedback channel | built |
| tester-recruitment-planner | Find and brief playtesters | built |
| community-event-planner | Community events that are cheap to run | built |
| group-management-planner | Group roles, ranks and payouts | built |
| ambassador-program-planner | Reward helpful community members | built |
| bug-intake-builder | Bug report intake form and triage routine | built |
| community-poll-writer | Polls that give usable answers | built |
| welcome-message-writer | Welcome flow for new members | built |
| creator-collab-planner | Work with content creators on a game | built |
| social-proof-collector | Gather quotes, clips and numbers | built |
| toxicity-response-playbook | Respond to harassment and drama | built |
| support-macro-writer | Canned replies for common support issues | built |
| fan-art-contest-planner | Run a safe fan content contest | built |
| leaderboard-hooks-planner | Use leaderboards to build community | built |
| clan-system-planner | Clans and groups inside the game | built |
| friend-invite-reward-builder | Rewards for inviting friends | built |
| streamer-kit-builder | A kit that makes streaming the game easy | built |

## publish - Publishing and compliance

| skill | what it does | status |
|---|---|---|
| age-rating-prep | Prepare answers for the experience maturity questionnaire and check content against them | built |
| privacy-data-checker | Check what data the game collects and stores | built |
| tos-compliance-checker | Check a design against Roblox rules | built |
| chat-compliance-checker | Check chat and text features against safety rules | built |
| paid-random-compliance | Check paid random items rules and disclosures | built |
| ugc-moderation-checker | Check user-generated content paths for moderation | built |
| audio-permission-checker | Check audio asset permissions and replacements | built |
| thumbnail-guideline-checker | Check images against content guidelines | built |
| copyright-checker | Check for copied or restricted material | built |
| experience-settings-configurator | Configure experience settings for launch | built |
| regional-availability-checker | Check regional and device availability | built |
| device-support-setter | Set supported devices and controls | built |
| private-server-settings-setter | Configure private server access | built |
| experience-name-checker | Check names and descriptions against rules | built |
| group-ownership-setup | Move an experience under a group safely | built |
| collaborator-permissions-setter | Set team permissions with least privilege | built |
| version-history-keeper | Keep restore points and a release log | built |
| place-backup-planner | Back up places and assets | built |
| post-launch-monitor | The first 72 hours after launch | built |
| publish-readiness-gate | Run the final go/no-go gate with evidence | built |
| ad-policy-checker | Check ad surfaces and ad content against the advertising standards | built |
| localization-setup | Set up languages, translation table and AutoLocalize, and scan code for untranslatable strings | built |
| matchmaking-settings-setter | Plan and validate the matchmaking configuration before entering it | built |

## workflow - Workflow and project management

| skill | what it does | status |
|---|---|---|
| project-kickoff | Start a Roblox project: folder, Rojo, checks, notes | built |
| task-breaker | Break a goal into verifiable tasks for an AI worker | built |
| session-handoff | Write a handoff so the next session resumes cleanly | built |
| git-workflow-setter | Branching, commits and ignore rules for a Rojo project | built |
| sprint-planner | Plan a week for a solo or small team | built |
| decision-log-writer | Record decisions and their evidence | built |
| tech-debt-lister | List and rank debt with fix cost | built |
| ai-brief-writer | Write a brief an AI worker can execute | built |
| worker-verifier | Verify a worker's claims with a cheap check | built |
| usage-budgeter | Plan AI usage and model choice per task | built |
| release-checklist-builder | Build the per-release checklist | built |
| code-style-guide-writer | Write the project's Luau style guide and enforce with tools | built |
| folder-structure-planner | Design the repo and Explorer layout | built |
| dependency-pinner | Pin Rojo, Selene, StyLua and Wally versions | built |
| ci-check-setter | Set up the Luau check script and run it on commit | built |
| changelog-writer | Keep a changelog from commits | built |
| docs-writer-roblox | Write module docs from code | built |
| onboarding-new-dev | Onboard a new teammate in a day | built |
| scope-creep-guard | Detect and stop scope creep with a rule set | built |
| post-mortem-writer | Write a blameless post-mortem | built |
| team-roles-planner | Who does what in a small team | built |
| milestone-reviewer | Review a milestone against its acceptance tests | built |
| kb-lookup-routine | Find the right vault evidence fast | built |
| studio-mcp-session-planner | Plan a Studio MCP session with checkpoints | built |
| playtest-evidence-logger | Record playtest evidence in a standard format | built |
| devlog-writer | Write an honest weekly devlog from shipped facts and real numbers | built |
| asset-pipeline-planner | Route assets from source to a registered Roblox asset id with licences and naming | built |
| failure-miner | Mine session transcripts for repeated worker failures and fix them at the cheapest rung | built |
| eval-bank | Keep a private bank of solved problems and rerun it when the model or instructions change | built |
