# Manager routing: job -> worker (pack skill / kit agent / system) -> model

Pack skills are opened by a general worker (Agent tool) whose master brief says "read `<skillpack.py path name>` and follow it". Confirm every name with `skillpack.py find "<words>"` before use (307 skills). haiku = lookups, greps, checks; sonnet = default. No other model unless the plan allows. This file is the ONLY routing source: `game-dev-plan` copies its table from here, the manager reads the plan's table. Agent calls: pack skill = `subagent_type: general-purpose` reading the skill file; kit agent = its own name as `subagent_type`.

| stage / job | pack skill(s) | kit agent / system | model | mode |
|---|---|---|---|---|
| idea: validate, one sentence, scope | idea-validator, one-sentence-pitch, scope-cutter, mvp-definer | game-dev-rate, game-critic-rbxdev-vault | sonnet | serial |
| design: loop, first minute, progression, rewards | core-loop-designer, first-minute-designer, progression-curve-designer, reward-schedule-designer | roblox-game-designer | sonnet | parallel, no project edits (each writes only its own `docs/audits/` report file) |
| economy | (money: `find "economy sink"`) | roblox-economy-designer | sonnet, high | serial |
| scaffold and loop code | (scripting/systems: `find "<system>"`) | roblox-builder, roblox-luau-engineer; systems/PlayerData, Shop, DailyRewards | sonnet | serial per owned folder |
| art direction (J00, before any UI/world/effect job) | art-bible-writer, palette-picker, font-and-color-picker, lighting-preset-picker, game-feel-polisher | skill game-dev-art-direction (StyleKit) | sonnet | serial, first |
| UI | mobile-ui-audit, shop-ui-planner, hud-layout-planner, ui-kit-consistency-checker | roblox-builder (StyleKit components only) | sonnet | parallel with non-UI writers |
| models, world, lighting, effects | model-rebuild, prop-set-planner, part-to-mesh-planner, lighting-preset-picker, particle-effect-planner | roblox-builder; Studio MCP search_asset / insert_asset / generate_mesh | sonnet | serial (MCP) |
| visual gate and polish rounds | ui-kit-consistency-checker, safe-area-checker, game-feel-polisher | skill game-dev-visual-qa; fresh game-critic-rbxdev-vault re-scores | sonnet | serial, after the last feature job |
| after prototype | playtest-bot-writer, lag-hunter, exploit-audit | roblox-tester, roblox-playtest-runner, roblox-luau-reviewer (read-only) | sonnet; haiku for sweeps | parallel, no project edits (own `docs/audits/` report file each) |
| fixes | skill of the finding (dupe-exploit-hunter, texture-budget-checker, model-cleaner ...) | roblox-luau-engineer | sonnet | serial |
| gate | game-dev-critic | game-critic-rbxdev-vault, roblox-pre-delivery-reviewer | sonnet, fresh context | after every milestone |
| launch | thumbnail-maker, game-icon-maker, thumbnail-guideline-checker; ads/launch by find | game-dev-launch-kit, roblox-launch-marketing-manager | sonnet | parallel (disjoint docs) |
| growth / live-ops | patch-notes-writer, update-announcement-writer; analytics by find | game-dev-weekly, game-dev-update, roblox-analytics-reviewer, roblox-liveops-planner | sonnet | serial |
| vault facts for a brief | - | agent mentor-rbxdev-vault; skills use-rbxdev-vault, roblox-kb-answer | haiku | any |

Rule: read-only auditors run in parallel; anything that writes the same folder runs one after another.

## Job-level defaults (effort, mode, budget; the plan adjusts these)
Models: haiku = lookups, listing, simple verification; sonnet = default. Writers sharing files run serial; readers may run parallel ("parallelise reading, serialise writing", `Manager/topic-orchestration-patterns.md`; "split by ownership" and "default to one worker unless the work is independent", `Manager/topic-multi-agent-failure-modes.md`).

| job | skill / agent | model | effort | mode | typical budget |
|---|---|---|---|---|---|
| Vault facts for a job (kbq, grep, price lookups) | `use-rbxdev-vault`, `roblox-kb-answer` | haiku | low | parallel | 1 run, 10 turns |
| Asset search in <vault>/Assets | `roblox-asset-finder` | haiku | low | parallel | 1 run, 10 turns |
| GDD and balance of design | `roblox-game-designer`, `roblox-gdd-template` | sonnet | medium | serial | 1 run, 30 turns |
| Economy numbers and simulation | `roblox-economy-designer`, `game-economy-simulation` | sonnet | high | serial | 1 run, 30 turns |
| Scaffold project (Rojo layout, Config, services) | `roblox-builder` + `roblox-rojo-project-setup` (or `roblox-game-builder` for a very small game) | sonnet | medium | serial | 1 run, 40 turns |
| Core loop and game state | `roblox-luau-engineer` + `roblox-round-based-game-loop`, `roblox-luau-style` | sonnet | high | serial (owns Services/GameLoop) | 1-2 runs, 60 turns |
| Data saving | `roblox-luau-engineer` + `roblox-datastore-safe-save` | sonnet | high | serial | 1 run, 40 turns |
| Remotes and anti-exploit | `roblox-luau-engineer` + `roblox-remote-security` | sonnet | high | serial | 1 run, 40 turns |
| Art direction (J00) | `game-dev-art-direction` | sonnet | medium | serial, before visual jobs (owns art-direction.md, src/shared/StyleKit) | 1 run, 30 turns |
| UI (HUD, shop, popups) | `roblox-builder` + `roblox-ui-responsive` + StyleKit | sonnet | medium | parallel with non-UI writers (owns src/client/UI) | 1 run, 40 turns |
| Monetisation hooks | `roblox-monetization-consultant` (design) then `roblox-luau-engineer` + `roblox-monetisation-setup` | sonnet | medium | serial | 2 runs |
| NPCs / enemies | `roblox-luau-engineer` + `roblox-npc-pathfinding` | sonnet | high | serial | 1 run |
| Leaderboards, events, daily rewards | `roblox-luau-engineer` + `roblox-leaderboards-and-events` | sonnet | medium | serial | 1 run |
| Map / world build from code | `roblox-builder`; Studio MCP when present for instances Rojo cannot hold | sonnet | medium | serial, `MCP` | 1 run |
| Performance pass | `roblox-performance-pass` | sonnet | medium | serial | 1 run |
| Code review (exploits, data loss, leaks) | `roblox-luau-reviewer` | sonnet | high | parallel (read-only) | 1 run per milestone |
| Static checks and banned-pattern greps | the manager itself, or a `haiku` checker with a 5-line brief | haiku | low | parallel | per job |
| Visual QA round (capture, score, fix list) | `game-dev-visual-qa` | sonnet | medium | serial, Studio MCP | up to 3 rounds, 40 turns each |
| Playtest and feel review | `game-dev-playtest` (+ `roblox-tester`, `roblox-playtest-runner`) | sonnet | medium | serial | 1 run |
| Launch checklist | `roblox-launch-checklist`, `roblox-publish-checklist` | haiku | low | serial | 1 run |
| Icon, thumbnail, screenshots | `game-dev-thumbnail` (+ `roblox-ad-creative-planner`) | sonnet | medium | parallel (no code files) | 1 run |
| Ad plan | `game-dev-ads` (+ `roblox-launch-marketing-manager`) | sonnet | medium | parallel (no code files) | 1 run |
| Update roadmap | `game-dev-update` (+ `roblox-liveops-planner`) | sonnet | medium | parallel (no code files) | 1 run |
| Diagnose weak numbers (post-launch) | `roblox-game-doctor`, `roblox-analytics-reviewer` | sonnet | medium | serial | 1 run |

Caps: 6-12 jobs -> cap 3 alive; under 6 jobs -> cap 2; never above 4. Total runs = jobs + 1 retry for at most a third of them + playtest. Nesting depth 0.
