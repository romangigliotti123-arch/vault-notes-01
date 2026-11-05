---
name: rbx-visual
description: "Mandatory visual gate and definition of done: screenshots of the running game (phone and desktop), layout and overlap at three sizes, 7-item rubric, max 3 fix rounds. Done only after it passes with screenshots; else 'playable prototype, visuals not polished'."
argument-hint: "[game slug or project folder]"
---

# rbx-visual

Code comments: none by default (see rbx-luau, Comments).

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Why: a game that runs and follows its design was repeatedly declared done with overlapping UI, bare-block models, flat sprites and default lighting and effects. WORKS and GOOD are not LOOKS; this is the third axis, and `rbx-critic` re-scores it independently and refuses GOOD without it.

## Definition of done (the rule everyone follows)
- The words done, complete, finished, ready, shipped, "good to go" about a game or a visual change are allowed only when `visual_gate.py` printed `VISUAL GATE: PASS` for the CURRENT build and the screenshots are attached (paths) in the report, AND `placement_gate.py` printed `PLACEMENT GATE: PASS` for the same build (skill `rbx-placement`) AND `lighting_gate.py` printed `LIGHTING GATE: PASS` for the same build (skill `rbx-lighting`).
- Otherwise the status line is exactly: `playable prototype, visuals not polished`, followed by the polish backlog (open rubric items, defects, who fixes them). Say it even when everything else works.
- A builder never grades itself: its scores guide the fix loop; the critic's score decides.

## Loop (max 3 rounds; one round = capture, check, score, fix)
1. **Prereq**: `Games/<slug>/art-direction.md` exists (skill `rbx-art`). If not, the first defect is "no art direction": write it first, do not polish blind.
1b. **Placement first**: `Games/<slug>/placement-qa/gate.json` must say `result: pass` (`PLACEMENT GATE: PASS` for the current build). Floating, sunken, crooked, overlapping and mis-facing models are placement defects, not polish: fix them there first. `visual_gate.py --write` refuses to pass without it.
1c. **Lighting first (L-checks before V-checks)**: `Games/<slug>/lighting-qa/gate.json` must say `result: pass` (skill `rbx-lighting`, `LIGHTING GATE: PASS` for the current build). Flat, dark, washed-out, over-glowing or default-Roblox lighting is a lighting defect with a number (L1-L12), fixed there before V5 is scored by eye. Run `visual_gate.py` with `--require-lighting` so a missing or failing lighting gate fails the visual gate too.
2. **Capture** into `Games/<slug>/visual-qa/r<N>/` (create it). With Studio MCP (`rbx-studio`): `start_stop_play`; `screen_capture` at `spawn` (first frame), `action` (core loop running, HUD busy, a popup open), `effect` (mid particle or tween), each at desktop; then run `scripts/ui_overlap.luau` via `execute_luau` (datamodel Client) for layout findings at phone, tablet and desktop; set `CONFIG.render = "phone"` once and `screen_capture` the phone preview, then `CONFIG.clean = true`. Save every image as `<viewport>-<moment>.png` in the round folder; if the tool only returns images inline and cannot save them, say so: no files = no gate pass. No Studio MCP: ask the user for screenshots (phone/emulator and desktop), or mark the gate `untested` and stop. Never launch Studio or GUI apps yourself.
3. **Score** with `references/rubric.md`: V1-V7, 1-10, each with a screenshot citation; list hard fails. Write `visual-qa/r<N>/gate.json` (format in the `scripts/visual_gate.py` docstring: scores, hard_fails, overlap totals per viewport, screenshots with viewport and moment, defects) and run `python scripts/visual_gate.py <gate.json> --project <project> --write Games/<slug>`. Exit 0 = PASS.
3b. **REFERENCE COMPARE (optional)**: read `<claude config dir>/claude-kit/reference-path.txt`; absent or empty = skip silently (written by `claude-kit/tools/refs-sync.py` at setup and `/rbx-update`). Line 1 = absolute path of a folder with `INDEX.md` (one row per image: path | game | category | why good | tags). For each failing or borderline item (score <= 7), grep `INDEX.md` for the category or tag, `Read` 3-6 matching images plus your own screenshot of the same screen, and write 3-5 CONCRETE differences (spacing, stroke width, palette count, icon style, lighting, effects) into the defect list. Fix from those, and cite the paths in the QA report line `References compared: <paths or none>`. Reference images are for comparison only: never copy, trace or re-create them, never copy any file into the game or its repo, and never write reference paths or images into the game, its docs or any shipped file (paths go only in the QA report and `gate.json` under `Games/<slug>/visual-qa/`). Third-party frames: see NOTICE.md in that folder.
3c. **UI design (advisory)**: with UI, the `rbx-ui-mockup` compare runs in these rounds (`ui_overlap.luau` prints `UI-RECTS`); report `UI design: done (auto|figma|manual) / skipped: <reason>`; never changes the result.
4. **Defects**: one line each: `V4 | pufferfish is a flat 2D sprite | models/Pufferfish | rebuild as a multi-part model`. Order by rubric item, hard fails first.
5. **Fix** through the manager ledger (one brief per defect group; the worker re-reads `art-direction.md` and uses the StyleKit): UI, models, lighting and effects specialists [cold:rbx-visual/fix-specialists.md] read when choosing which specialist to brief for a defect group (or find others with `/rbx find <words>`). After each fix batch repeat from step 2 with N+1: screenshots must be re-taken; the gate rejects pictures older than the newest Luau source.
6. **Stop**: PASS = done (say so with the screenshot paths and the gate output). Round 3 still FAIL, or a defect needs something only the user can supply (art assets, paid items): stop. Report the status line, the failing items, `References compared: <paths or none>`, and write `Games/<slug>/polish-backlog.md` (defect | rubric item | fix | owner). No 4th round; do not soften the label.
7. Update `GAME.md` (`## Latest critic verdict` area: "Visual gate: PASS r2 / FAIL r3, backlog: polish-backlog.md") and `decisions.md`.

## Rules
- Evidence only: a score without a screenshot citation is `judgment` and counts as 5.
- Screenshots of the editor, a menu-only state or an empty map do not count; the moments are fixed (spawn, action, effect).
- Placeholder or invented asset ids are not polish: ids come only from `search_asset`/`insert_asset` results, the user's assets, or `0` (silent), which the report must list as a V6 gap.
- `ui_overlap` layout findings are leads, not verdicts; explain every one you keep. Safe areas other than the top bar are not emulated: check them with the Device Emulator or `safe-area-checker`.
- No publishing, spending or posting; edit nothing outside the PROJECT folder and `Games/<slug>/visual-qa/`.
- Scripts: `scripts/Overlap.luau` (pure, Lune-tested), `scripts/ui_overlap.luau` (generated for `execute_luau`; rebuild with `python scripts/build_inline.py`), `scripts/visual_gate.py` (gate maths).
