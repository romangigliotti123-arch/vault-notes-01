# Manager routing: job -> worker (pack skill / kit agent / system) -> model

Pack skills are opened by a general worker (Agent tool) whose master brief says "read `<skillpack.py path name>` and follow it". Confirm every name with `skillpack.py find "<words>"` before use (307 skills). haiku = lookups, greps, checks; sonnet = default. No other model unless the plan allows. This file is the ONLY routing source: `rbx-plan` copies its table from here, the manager reads the plan's table. Agent calls: pack skill = `subagent_type: general-purpose` reading the skill file; kit agent = its own name as `subagent_type`.

| stage / job | pack skill(s) | kit agent / system | model | mode |
|---|---|---|---|---|
| idea: validate, one sentence, scope | idea-validator, one-sentence-pitch, scope-cutter, mvp-definer | rbx-rate, rbx-judge | sonnet | serial |
| design: loop, first minute, progression, rewards | core-loop-designer, first-minute-designer, progression-curve-designer, reward-schedule-designer | rbx-designer | sonnet | parallel, no project edits (each writes only its own `docs/audits/` report file) |
| economy | (money: `find "economy sink"`) | rbx-economist | sonnet, high | serial |
| scaffold and loop code | (scripting/systems: `find "<system>"`) | rbx-engineer; systems/PlayerData, Shop, DailyRewards | sonnet | serial per owned folder |
| art direction (J00, before any UI/world/effect job) | art-bible-writer, palette-picker, font-and-color-picker, lighting-preset-picker, game-feel-polisher | skill rbx-art (StyleKit) | sonnet | serial, first |
| UI | mobile-ui-audit, shop-ui-planner, hud-layout-planner, ui-kit-consistency-checker | rbx-engineer (StyleKit components only) | sonnet | parallel with non-UI writers |
| models, world, lighting, effects | model-rebuild, prop-set-planner, part-to-mesh-planner, lighting-preset-picker, particle-effect-planner | rbx-engineer; Studio MCP search_asset / insert_asset / generate_mesh | sonnet | serial (MCP) |
| placement checks while building and the full-map scan | `rbx-placement` (`Placement.place` / `verify` / `scan` through Studio MCP) | the building worker itself, then a serial scan job | sonnet | serial, Studio MCP, before the visual gate |
| lighting preset (early) and the lighting scan | `rbx-lighting` (`LightingKit.apply` / `scan` / `fix` through Studio MCP, Edit mode) | the building worker (preset, job J00b), then a serial scan job | sonnet | serial, Studio MCP, preset before the first map job, scan before the visual gate |
| visual gate and polish rounds | ui-kit-consistency-checker, safe-area-checker, game-feel-polisher | skill rbx-visual; fresh rbx-judge re-scores | sonnet | serial, after the last feature job |
| after prototype | playtest-bot-writer, lag-hunter, exploit-audit | rbx-tester, rbx-reviewer (read-only) | sonnet; haiku for sweeps | parallel, no project edits (own `docs/audits/` report file each) |
| fixes | skill of the finding (dupe-exploit-hunter, texture-budget-checker, model-cleaner ...); a bug follows the Fix loop of `rbx-playtest` (red check first) | rbx-engineer | sonnet | serial |
| gate | rbx-critic | rbx-judge, rbx-predelivery | sonnet, fresh context | after every milestone |
| launch | thumbnail-maker, game-icon-maker, thumbnail-guideline-checker; ads/launch by find | rbx-launch-kit, rbx-marketer | sonnet | parallel (disjoint docs) |
| growth / live-ops | patch-notes-writer, update-announcement-writer; analytics by find | rbx-weekly, rbx-game-update, rbx-doctor, rbx-liveops | sonnet | serial |
| vault facts for a brief | - | agent rbx-coach; skills rbx-use, rbx-kb | haiku | any |

Rule: read-only auditors run in parallel; anything that writes the same folder runs one after another.

## Job-level defaults (effort, mode, budget; the plan adjusts these)
Models: haiku = lookups, listing, simple verification; sonnet = default. Writers sharing files run serial; readers may run parallel ("parallelise reading, serialise writing", `Manager/topic-orchestration-patterns.md`; "split by ownership" and "default to one worker unless the work is independent", `Manager/topic-multi-agent-failure-modes.md`).

| job | skill / agent | model | effort | mode | typical budget |
|---|---|---|---|---|---|
| Vault facts for a job (kbq, grep, price lookups) | `rbx-use`, `rbx-kb` | haiku | low | parallel | 1 run, 10 turns |
| Asset search in <vault>/Assets | `rbx-assets` | haiku | low | parallel | 1 run, 10 turns |
| GDD and balance of design | `rbx-designer`, `rbx-gdd` | sonnet | medium | serial | 1 run, 30 turns |
| Economy numbers and simulation | `rbx-economist`, `game-economy-simulation`, `rbx-tune` (metric ledger) | sonnet | high | serial | 1 run, 30 turns |
| Scaffold project (Rojo layout, Config, services) | `rbx-engineer` + `rbx-rojo` (or `rbx-builder` for a very small game) | sonnet | medium | serial | 1 run, 40 turns |
| Core loop and game state | `rbx-engineer` + `rbx-rounds`, `rbx-luau`, `rbx-arch` | sonnet | high | serial (owns Services/GameLoop) | 1-2 runs, 60 turns |
| Data saving | `rbx-engineer` + `rbx-datastore` | sonnet | high | serial | 1 run, 40 turns |
| Remotes and anti-exploit | `rbx-engineer` + `rbx-remote-sec` | sonnet | high | serial | 1 run, 40 turns |
| Art direction (J00) | `rbx-art` | sonnet | medium | serial, before visual jobs (owns art-direction.md, src/shared/StyleKit) | 1 run, 30 turns |
| UI (HUD, shop, popups) | `rbx-engineer` + `rbx-ui` + StyleKit | sonnet | medium | parallel with non-UI writers (owns src/client/UI) | 1 run, 40 turns |
| Monetisation hooks | `rbx-money` (design) then `rbx-engineer` + `rbx-monetize` | sonnet | medium | serial | 2 runs |
| NPCs / enemies | `rbx-engineer` + `rbx-npc` | sonnet | high | serial | 1 run |
| Leaderboards, events, daily rewards | `rbx-engineer` + `rbx-leaderboard` | sonnet | medium | serial | 1 run |
| Map / world build from code | `rbx-engineer`; Studio MCP when present for instances Rojo cannot hold | sonnet | medium | serial, `MCP` | 1 run |
| Performance pass | `rbx-perf`, `rbx-tune` (frame or part cost as the metric) | sonnet | medium | serial | 1 run |
| Code review (exploits, data loss, leaks) | `rbx-reviewer` | sonnet | high | parallel (read-only) | 1 run per milestone |
| Static checks and banned-pattern greps | the manager itself, or a `haiku` checker with a 5-line brief | haiku | low | parallel | per job |
| Placement scan (every model, fix, re-scan) | `rbx-placement` | sonnet | medium | serial, Studio MCP | up to 3 scans, 30 turns each |
| Lighting preset + scan (apply, scan, fix, re-scan) | `rbx-lighting` | sonnet | medium | serial, Studio MCP | up to 3 scans, 20 turns each |
| Visual QA round (capture, score, fix list) | `rbx-visual` | sonnet | medium | serial, Studio MCP | up to 3 rounds, 40 turns each |
| Bug fix (reproduce first) | `rbx-playtest` Fix loop + `rbx-engineer` | sonnet | medium | serial | 1 run, 30 turns |
| Tune, balance or polish with a metric | `rbx-tune` | sonnet | medium | serial (owns the tuned files) | up to 10 experiments |
| Code gates | `rbx-critic/scripts/code_gates.py` (the manager runs it, or a haiku checker) | haiku | low | serial | per milestone |
| Playtest and feel review | `rbx-playtest` (+ `rbx-tester`) | sonnet | medium | serial | 1 run |
| Launch checklist | `rbx-launch-check`, `rbx-publish` | haiku | low | serial | 1 run |
| Icon, thumbnail, screenshots | `rbx-thumbnail` (+ `rbx-marketer`) | sonnet | medium | parallel (no code files) | 1 run |
| Ad plan | `rbx-ads` (+ `rbx-marketer`) | sonnet | medium | parallel (no code files) | 1 run |
| Update roadmap | `rbx-game-update` (+ `rbx-liveops`) | sonnet | medium | parallel (no code files) | 1 run |
| Diagnose weak numbers (post-launch) | `rbx-doctor` | sonnet | medium | serial | 1 run |

Caps: 6-12 jobs -> cap 3 alive; under 6 jobs -> cap 2; never above 4. Total runs = jobs + 1 retry for at most a third of them + playtest. Nesting depth 0.
