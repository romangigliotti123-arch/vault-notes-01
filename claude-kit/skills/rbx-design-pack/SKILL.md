---
name: rbx-design-pack
description: "Plans the DESIGN of a Roblox game before any code, mostly in Figma: references, style test, UI screens, map layout, one-page plan; also thumbnails, models, animations, cutscenes, VFX, sound, menus, store, trailer. Use for 'design pack', 'plan the design', 'map layout', 'style test', 'UI options', 'redesign'."
argument-hint: "[game slug] [design thing, e.g. map, ui, style, thumbnail, cutscene]"
---

# rbx-design-pack

Code comments: none by default (see rbx-luau, Comments).

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Design first, code second. Roman's rule: no game code until the look, the UI and the map were SHOWN and the user picked. Every time a game skipped this the UI, the map or the style was built blind and redone (UI "not happy at all", map "looks like a baseplate", plot and hall sizes redone). This skill makes the design as cheap pictures, several versions, one pick.

## What it can design (say this list first, one line each, then ask what they want)
- Reference collection: what the top similar games do, screenshots and notes
- Style test: 3-8 hero props shown in the chosen look
- Map layout: zones, plots, halls, plaza, flow, in studs
- UI screens: HUD, menus, shop, inventory, 3 versions each
- Thumbnails and icons: image-gen prompts (rbx-thumbnail)
- Models and props, characters and pets
- Animations, transitions, cutscenes, VFX, sound and music
- Loading and menu screens, store and monetisation screens, trailer and ad shots
- Anything else the user names: same method (brief, 3 options, pick, record, hand off)

## The method (every design thing)
1. Brief: fill the compact template for that type (`references/design-types.md`), 5-8 lines, from `design.md`, `game-plan.md`, the approved parts so far. Unknown = a labelled assumption, not a question.
2. Figma check: `bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/tools/design_gate.py figma <slug> --stage <start|style|ui|map|approve|redesign-N> --tools "<tool names containing figma, or none>"`. Find the tool names in your tool list (ToolSearch "figma" when deferred). Print what it says. It prints the connect steps ONCE per stage and a one-line reminder after; never nag inside a stage, never ask for a token, never edit settings or MCP config: the user runs the command. Full steps, tools and limits: `references/figma.md`.
3. Options: make 3 versions (A/B/C, clearly different, not colour swaps) where it is drawn: Figma/FigJam when connected (frames named per `references/figma.md`), else HTML/SVG (`rbx-ui-prototype` for clickable UI, a single SVG or HTML sheet for maps and boards). Show them (Figma link or screenshot paths; Read shows images). A hero prop or character is built for real (Blender or Studio, `rbx-art`) and rendered, not drawn.
4. Pick: the user chooses one, or mixes ("A's top bar, C's shop"). One revision round is normal, a third is a sign the brief is wrong: re-brief. The user's pick and reasons are written down in the part file.
5. Record: write `Games/<slug>/design-pack/<part>.md` (brief, the options with links or paths, the pick, the specs the builders need), then `design_gate.py approve <slug> <part> --note "<pick>"`. It refuses an empty part file or an out-of-order part.
6. Hand off to the specialist, never rebuild it here: thumbnails/icons `rbx-thumbnail` (images) and `rbx-thumb-brief` (packaging text); UI `rbx-ui-prototype` then `rbx-ui-mockup` then `rbx-ui`; style, models, lighting `rbx-art`, `rbx-placement`, `rbx-lighting`; checks `rbx-visual`. The approved parts are INPUTS of every later brief.

## New game: the gate (strict, five steps in this order)
`bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/tools/design_gate.py init <slug>` then `status <slug>` after every approval. Output ends `DESIGN GATE: PASS` or `DESIGN GATE: STOP - next: <part>`.
1. `refs`: 3-6 similar top games BEFORE designing: the vault reference images (`.rbx/claude-kit/reference-path.txt`, grep its `INDEX.md`), `rbx-trends`/`rbx-research` for what leads now, and a look online. Table per game: what to keep (patterns only, never copy), what to avoid. Include the map-layout comparison of `references/map-and-plan.md`.
2. `style`: style test models, 3-8 hero props built and shown (`references/map-and-plan.md`). One look is approved before any world is built.
3. `ui`: the key screens (HUD, main menu, shop, inventory, the game's own panel), 3 versions each, phone frames first (`references/figma.md`).
4. `map`: the layout with stud scale: zones, plots/halls/plaza sizes, sightlines, spawn, flow arrows, landmarks, prop density.
5. `plan`: one page that fits the approved parts together (template in `references/map-and-plan.md`); approving it opens the build.
Missing part = STOP: tell the user which design step is next, in one line, and start it. Writing game code, M1 or a builder job while the gate says STOP is a defect. The user may override with a clear "skip the design pack" (all) or "skip the UI design" (one part): then run `design_gate.py skip <slug> <part|all> --reason "<their words>"`, which logs it in `APPROVED.md`; tell them in one line that skipping is how the UI, map and style got redone last time, and continue. Never skip on your own judgement, never infer a skip from silence.
Redesign requests mid-game ("redo the UI", "the map looks empty", "new style"): reuse the pack, open that part again (Figma check with `--stage redesign-N`), make 3 new versions, update the part file and re-approve. Existing games without a pack: offer it once, do not block work already in progress.

## Rules
- Patterns only, never copy another game's art, UI or map; no real brands; reference images are comparison only.
- Never writes game code, never publishes, spends or posts; image generation only through the user's own configured tools (`rbx-thumbnail`).
- Ids, prices and numbers in specs come from the user, the KB or labelled assumptions.
- Approved means the user said so in this session; the date in `APPROVED.md` is that day.
- Worked example from a real build (Dust & Peek lessons): `examples/dust-and-peek.md`.

## Self-check
`design_gate.py status <slug>` prints the part lines and the gate result; part files exist for every `[x]` line.

## Reply format
Short dot points (what was designed, versions shown, the pick), then bold footer:
**Done** - what is approved and where (`Games/<slug>/design-pack/`)
**You** - the next pick or approval, or the Figma step if it is not connected
**Next** - the next design step, or the build once the gate is PASS

## Learn
