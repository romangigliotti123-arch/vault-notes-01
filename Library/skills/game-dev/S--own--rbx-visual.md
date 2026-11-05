---
id: "rbx-visual"
type: skill
category: "game-dev"
source: "own"
license: "first-party"
repo_path: "skills/game-dev/rbx-visual/SKILL.md"
description: "Mandatory visual gate and definition of done: screenshots of the running game (phone and desktop), layout and overlap at three sizes, 7-item rubric, max 3 fix rounds. Done only after it passes with screenshots; else 'playable prototype, visuals not polished'."
orig_name: "rbx-visual"
orig_argument_hint: "[game slug or project folder]"
tags: [lib/skill, cat/game-dev, src/own]
---

# rbx-visual

> Mandatory visual gate and definition of done: screenshots of the running game (phone and desktop), layout and overlap at three sizes, 7-item rubric, max 3 fix rounds. Done only after it passes with screenshots; else 'playable prototype, visuals not polished'.

Type: skill | Category: [[categories/cat-game-dev|game-dev]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/game-dev/rbx-visual/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--rbx-critic]], [[S--own--rbx-lighting]], [[S--own--rbx-placement]], [[S--own--rbx-studio]]

---
# rbx-visual

Code comments: none by default (see rbx-luau, Comments).

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Why this exists: a game that runs and follows its design was repeatedly declared done while the UI overlapped, models were bare blocks and flat sprites, and lighting and effects were default. WORKS (no errors) and GOOD (fun) are not LOOKS. This gate is the third axis; `rbx-critic` re-scores it independently and refuses GOOD without it.

## Definition of done (the rule everyone follows)
- The words done, complete, finished, ready, shipped, "good to go" about a game or a visual change are allowed only when `visual_gate.py` printed `VISUAL GATE: PASS` for the CURRENT build and the screenshots are attached (paths) in the report, AND `placement_gate.py` printed `PLACEMENT GATE: PASS` for the same build (skill `rbx-placement`) AND `lighting_gate.py` printed `LIGHTING GATE: PASS` for the same build (skill `rbx-lighting`).
- Otherwise the status line is exactly: `playable prototype, visuals not polished`, followed by the polish backlog (open rubric items, defects, who fixes them). Say it even when everything else works.
- A builder never grades itself: its own scores guide the fix loop; the critic's score decides.

## Loop (max 3 rounds; one round = capture, check, score, fix)
1. **Prereq**: `Games/<slug>/art-direction.md` exists (skill `rbx-art`). If it does not, the first defect is "no art direction": write it first, do not polish blind.
1b. **Placement first**: `Games/<slug>/placement-qa/gate.json` must say `result: pass` (skill `rbx-placement`, `PLACEMENT GATE: PASS` for the current build). Floating, sunken, crooked, overlapping and wrongly facing models are placement defects, not polish: fix them there first. `visual_gate.py --write` refuses to pass without it.
1c. **Lighting first (L-checks before V-checks)**: `Games/<slug>/lighting-qa/gate.json` must say `result: pass` (skill `rbx-lighting`, `LIGHTING GATE: PASS` for the current build). Flat, dark, washed-out, over-glowing or default-Roblox lighting is a lighting defect with a number (L1-L12), fixed there before V5 is scored by eye. Run `visual_gate.py` with `--require-lighting` so a missing or failing lighting gate fails the visual gate too.
2. **Capture** into `Games/<slug>/visual-qa/r<N>/` (create it). With Studio MCP (`rbx-studio`): `start_stop_play`; `screen_capture` at `spawn` (first frame), `action` (core loop running, HUD busy, a popup open), `effect` (mid particle or tween), each at desktop; then run `scripts/ui_overlap.luau` via `execute_luau` (datamodel Client) for the layout findings at phone, tablet and desktop; set `CONFIG.render = "phone"` once and `screen_capture` the phone preview, then `CONFIG.clean = true`. Save every image as a file `<viewport>-<moment>.png` in the round folder; if the tool only returns images inline and cannot save them, say so: no files = no gate pass. No Studio MCP: ask the user for screenshots (their phone/emulator and desktop), or mark the gate `untested` and stop. Never launch Studio or GUI apps yourself.
3. **Score** with `references/rubric.md`: V1-V7, 1-10, each with a screenshot citation; list hard fails. Write `visual-qa/r<N>/gate.json` (format in `scripts/visual_gate.py` docstring: scores, hard_fails, overlap totals per viewport, screenshots with viewport and moment, defects) and run `python scripts/visual_gate.py <gate.json> --project <project> --write Games/<slug>`. Exit 0 = PASS.
3b. **REFERENCE COMPARE (optional)**: read the file `<claude config dir>/claude-kit/reference-path.txt`; if it is absent or empty, skip this step silently (setup and `/rbx-update` write it through `claude-kit/tools/refs-sync.py` after fetching the public reference screenshots; absent = they could not be fetched). Line 1 is the absolute path of a folder containing `INDEX.md` (one row per image: path | game | category | why good | tags). For each failing or borderline rubric item (score <= 7), grep `INDEX.md` for the matching category or tag, `Read` 3-6 matching reference images plus your own screenshot of the same kind of screen, and write 3-5 CONCRETE differences (spacing, stroke width, palette count, icon style, lighting, effects) into the defect list in the usual defect format. Fix from those differences, and cite the reference paths in the QA report line `References compared: <paths or none>`. Reference images are for comparison only: never copy, trace or re-create them, never copy any file into the game or its repo, and never write reference paths or images into the game, its docs or any shipped file (paths go only in the QA report and `gate.json` under `Games/<slug>/visual-qa/`).
3c. **UI design (advisory)**: with UI, the `rbx-ui-mockup` compare runs in these rounds (`ui_overlap.luau` prints `UI-RECTS`); report `UI design: done (auto|figma|manual) / skipped: <reason>`; never changes the result.
4. **Defects**: one line each: `V4 | pufferfish is a flat 2D sprite | models/Pufferfish | rebuild as a multi-part model`. Order by rubric item, hard fails first.
5. **Fix** through the manager ledger (one brief per defect group; the worker re-reads `art-direction.md` and uses the StyleKit): UI (`ui-kit-consistency-checker`, `ui-scale-fixer`, `hud-layout-planner`, `safe-area-checker`, `button-feedback-designer`, `ui-animation-planner`), models (`art-bible-writer`, `material-consistency-checker`, `part-to-mesh-planner`, `prop-set-planner`, `model-rebuild`; Studio MCP `search_asset` + `insert_asset`, `generate_mesh`, `generate_procedural_model`), lighting (`lighting-preset-picker`), effects (`particle-effect-planner`, `game-feel-polisher`, `sound-placement-planner`). Find others with `/rbx find <words>`. After each fix batch, repeat from step 2 with N+1: screenshots must be re-taken, the gate rejects pictures older than the newest Luau source.
6. **Stop**: PASS = done (say so with the screenshot paths and the gate output). Round 3 still FAIL, or a defect needs something only the user can supply (art assets, paid items): stop. Report the status line, the failing items, the line `References compared: <paths or none>`, and write `Games/<slug>/polish-backlog.md` (defect | rubric item | fix | owner). Do not run a 4th round and do not soften the label.
7. Update `GAME.md` (`## Latest critic verdict` area: "Visual gate: PASS r2 / FAIL r3, backlog: polish-backlog.md") and `decisions.md`.

## Rules
- Evidence only: a score without a screenshot citation is `judgment` and counts as 5.
- Screenshots of the editor, of a menu-only state, or of an empty map do not count; the moments are fixed (spawn, action, effect).
- Placeholder or invented asset ids are not polish: ids come only from `search_asset`/`insert_asset` results, the user's assets, or `0` (silent) which the report must list as a V6 gap.
- Layout findings from `ui_overlap` are leads, not verdicts; explain every one you keep. Safe areas other than the top bar are not emulated: check them with the Device Emulator or `safe-area-checker`.
- No publishing, spending or posting; do not edit anything outside the PROJECT folder and `Games/<slug>/visual-qa/`.
- Scripts: `scripts/Overlap.luau` (pure, tested with Lune), `scripts/ui_overlap.luau` (generated single file for `execute_luau`; rebuild with `python scripts/build_inline.py`), `scripts/visual_gate.py` (gate maths). Source of the rules: `Roblox/roblox-kb/ui-ux-design.md`, `building-art-and-assets.md`, `vfx-and-particles.md`.

## Learn

When this run verifies something non-obvious (a fix, a gotcha, a corrected assumption, a technique that worked), record it with `/rbx-learn` (`learn.py add`, one finding per note). Before researching a problem, check the curated `learned/` notes: `vault-find.py "<problem>" --type learned`.
