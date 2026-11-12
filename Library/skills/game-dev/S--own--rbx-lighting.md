---
id: "rbx-lighting"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/rbx-lighting/SKILL.md"
description: "Mandatory lighting gate: apply the genre lighting preset early (LightingKit.apply), scan the place against 12 checks (default Roblox, Atmosphere, Sky, effects, brightness, shadows, fog, interiors, mobile budget). Done only at LIGHTING GATE: PASS; run before visual QA and the critic."
orig_name: "rbx-lighting"
orig_argument_hint: "[game slug or project folder] [genre]"
tags: [lib/skill, cat/game-dev, src/own]
---

# rbx-lighting

> Mandatory lighting gate: apply the genre lighting preset early (LightingKit.apply), scan the place against 12 checks (default Roblox, Atmosphere, Sky, effects, brightness, shadows, fog, interiors, mobile budget). Done only at LIGHTING GATE: PASS; run before visual QA and the critic.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/rbx-lighting/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--rbx-critic]], [[S--own--rbx-visual]]

---
# rbx-lighting

Code comments: none by default (see rbx-luau, Comments).

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Why this exists: a generated map with the engine's default lighting (flat grey ambient, no Atmosphere, no tuned sky, no colour grading, shadows nobody checked) looks amateur no matter how good the models are. WORKS (no errors), GOOD (fun), LOOKS (screenshots) and PLACEMENT (geometry) all miss it, and `rbx-visual` V5 only scores it by eye after the fact. This gate sets the look at the START and measures it, every time. `rbx-critic` re-runs it independently and refuses GOOD without it.

## The rule
**Set the lighting preset when the map is first built (right after art direction and the genre are known): `LightingKit.apply(genre)` in Studio Edit mode. Build the map under that light. Before visual QA, and again before calling anything done, run `LightingKit.scan` and pass `lighting_gate.py`.** Do not leave the engine defaults on and "polish later": the preset also decides colours, brightness and contrast the models were chosen against.

## Definition of done (lighting)
- The words done, complete, finished, ready, shipped, "good to go" about a game, map, level or build are allowed only when `lighting_gate.py` printed `LIGHTING GATE: PASS` for the CURRENT build (scan newer than the last Luau source) AND the placement and visual gates passed.
- Otherwise the status line is exactly: `playable prototype, lighting not verified`, followed by the failing checks (id, measured value, fix).
- A builder never grades itself: its scan guides the fix loop; the critic's own fresh scan (`scorer: critic`) decides.

## Loop
1. **Prereq**: the genre (`obby`, `simulator` (also tycoon), `tower_defense`, `horror`, `cartoony` (also anime), `open_world` (also adventure), `sci_fi`) and the time of day (`day`, `golden`, `night`) from the design / `art-direction.md`; the StyleKit `Theme` palette when there is one (the scan reads `ReplicatedStorage.Shared.StyleKit.Theme` by itself). Presets and their reasons: `references/presets.md`.
2. **Apply** (early, Edit mode): `execute_luau` with `scripts/lighting_run.luau`, `CONFIG.mode = "apply"`, `CONFIG.preset = "<genre>"`, `CONFIG.time`, `CONFIG.mobile`; or call `LightingKit.apply(genre, { time = ..., mobile = ..., <section overrides> })` from build code (module `scripts/LightingKit.luau`, or `src/shared/LightingKit.luau` in a Rojo project). It creates or reuses exactly one Atmosphere, Sky, Bloom, ColorCorrection, SunRays (and DepthOfField where the genre allows), removes duplicates, sets Lighting and stamps the preset on `Lighting` (attribute `LightingKitPreset`). Technology cannot be changed by a script at runtime: apply in Edit mode (or the result lists it under `skipped`). Custom skybox: search the asset library (`search_asset`), pass the real ids as `sky = { SkyboxBk = ... }`; never invent ids.
3. **Look at it**: take the spawn screenshot for the visual QA anyway and hold it against 2-3 frames of the same genre from the reference library (`.rbx/claude-kit/reference-path.txt` points at the folder; `grep "| lighting-atmosphere |" INDEX.md` and `grep "| lighting |" INDEX.md`): sky colour, haze depth, warm/cool contrast, how the focal object is lit. The presets are starting values (not render-verified in live Studio); adjust with overrides (`{ lighting = { ExposureCompensation = 0.3 }, bloom = { Intensity = 0.2 } }`) and keep the result inside the check ranges.
4. **Scan** (before every visual QA round and before done): `CONFIG.mode = "scan"`, `CONFIG.genre`, `CONFIG.platform` (`both` default; `mobile` when the game is phone-first), `CONFIG.scorer = "builder"`, datamodel Edit. Save the console output and run `python scripts/lighting_gate.py ingest <file> --game <slug> --genre <genre> --scorer builder --write Games/<slug> --shots-from-visual Games/<slug>`. It writes `Games/<slug>/lighting-qa/scan-builder.json` + `gate.json` and prints PASS or FAIL with every failing check, its measured value and the first suggested fix. `--shots-from-visual` adds the real screenshot brightness (PNG) from the visual QA run.
5. **Fix**: `CONFIG.mode = "fix"` applies the concrete fixes of the failed checks (whole-look failures re-apply the preset, single ones change one property; interior lights, genre decisions and sky choices are listed as manual) and re-scans, up to three passes. Fix by hand what it lists as manual, scan again.
6. **Critic**: `rbx-critic` makes its own scan (`CONFIG.scorer = "critic"`), ingests it as `--scorer critic` (file `lighting-qa/scan-critic.json`) and passes it to `verdict.py` as `lighting_gate`. GOOD needs `lighting: pass` there; `games.py advance` refuses any verdict file without `lighting: pass` (older verdict files have no such line: run a fresh critic pass).
7. **Stop rule**: three scans in a row that still fail, or a failure that needs a decision only the user can make (the genre, a deliberate dark look, a paid sky asset): stop, report `playable prototype, lighting not verified` and the failing list. Do not widen the bands to get a PASS; a waiver (`CONFIG.waive = { L5 = "reason of at least 10 characters" }`) is for a deliberate, explained exception, at most two.
8. Update `GAME.md` (`## Lighting gate`: preset, time, platform, last scan) and `decisions.md`.

## Rules
- Evidence only: lighting is verified when the report says so; reading the script that set the properties is not verification. No Studio (no way to run Luau) = the gate stays `skipped`, say so, never claim it passed.
- Checks and tolerances: `references/checks.md`; presets and why: `references/presets.md`; Luau API and limits: `references/api.md`; JSON formats of the scan and the gate record (stable, read by other tools): `references/gate-format.md`.
- The scene-brightness numbers (L6, L9) are an ESTIMATE from sampled surfaces (colour, normal, sun, shade, roof, nearby lights) with a fixed model; screenshots (`--shots-from-visual`) are the measurement and win when they disagree. Say which one you relied on.
- This skill changes only the Lighting service, its effect objects and (on request) Light/CastShadow flags of existing parts; it never moves models or edits scripts or UI. Do not edit anything outside the PROJECT folder and `Games/<slug>/lighting-qa/`.
- Scripts: `scripts/presets.json` (all presets, bands, model constants: the single source), `scripts/LightingCore.luau` (pure checks, tested under Lune), `scripts/lighting_ref.py` (Python twin used by the tests and by the gate to recompute every scan), `scripts/adapter.src` + `runner.src` (Roblox side), `scripts/LightingData.luau`, `scripts/LightingKit.luau`, `scripts/lighting_run.luau` (GENERATED by `python scripts/build_inline.py`), `scripts/lighting_gate.py` (gate maths, PNG brightness, CLI). Tests: `tests/Lighting.test.luau`, `tests/Adapter.test.luau`, `tests/fixtures.json` (`tests/make_fixtures.py`).

## Learn
