# Design types: brief, versions, output, where drawn, hand-off

Each brief is 5-8 lines in the part file. Every type: 3 versions, user picks, record, hand off. "Drawn" = Figma/FigJam when connected (naming in `figma.md`), else the fallback shown.

| Type | Brief (fill these) | 3 versions are | Produce | Fallback drawing | Hand-off |
|---|---|---|---|---|---|
| refs | game fantasy, genre, audience, platform; 3-6 comparison games | n/a: a table of games | `refs.md`: per game: what it does well (loop, UI, map), keep, avoid, screenshot path | vault reference images (`reference-path.txt`, grep `INDEX.md`) + web | feeds every later part |
| style | mood words, palette idea, silhouette rule (blocky, rounded, voxel), outline, 3-8 hero props (the most repeated + the most valuable + one character) | 3 looks (palette + shape + outline) on the same 3 props | `style-test.md`: the chosen look, palette hex, outline, tri budget, rendered props (real models, not drawings) | Blender render or Studio screenshot | `rbx-art` (StyleKit values), `rbx-placement`, `rbx-lighting` |
| map | zones and their jobs, player count, plot or hall counts, spawn, goal, travel time spawn to goal, landmarks | 3 layouts (e.g. ring, linear hall, hub and spokes) | `map.md` + layout image/frame: stud scale, zones, flow arrows, sightlines, landmarks, density per zone | one SVG/HTML grid with 1 cell = 10 studs | world builders via `rbx-art` + `rbx-placement` |
| ui | screen list, what each shows, buttons, device first (phone landscape), tone | 3 layouts per key screen (HUD, menu, shop, inventory, game panel) | `ui.md` + frames: tokens (colours, fonts, corner, stroke), button states, one frame per screen at 780x360 / 844x390 / 667x375, then tablet and desktop | `rbx-ui-prototype` clickable HTML | `rbx-ui-mockup` -> `rbx-ui` (real ScreenGui) |
| thumbnail | game fantasy, hero subject, emotion, 3 colours, title words | 3 concepts (subject, angle, colour) | `thumbnail.md`: 3 image-gen prompts (subject, camera, lighting, palette, text safe zone, "no logos/brands"), 100 px legibility note | none: prompts + comp sketch | `rbx-thumbnail` (makes and scores images), `rbx-thumb-brief` (titles, A/B plan) |
| icon | same as thumbnail, square crop, one subject | 3 | icon prompt + crop notes | none | `rbx-thumbnail` |
| model/prop | what it is, role, size in studs, silhouette, tri budget, materials | 3 silhouettes or turnarounds | `models.md`: front/side sketches, size, pivot, the picked one | Blender blockout render | `rbx-art`, `rbx-placement` |
| character/pet | name, role, personality, scale, rarity tiers | 3 designs; for pets a tier ladder | `characters.md`: turnaround, palette, idle pose, rarity colours | sketch frame | `rbx-art`, `rbx-npc` for behaviour |
| animation | which object, states (idle, walk, hit, reward), length, loop, feel (snappy, bouncy) | 3 timing/easing sets (e.g. 0.12 s snap, 0.25 s bounce, 0.4 s float) | `animations.md`: keyframe table (time, pose or value, easing), reference clip description | Figma prototype/smart animate, or a CSS demo | `rbx-art` juice list, animation skills via `/rbx find animation` |
| transition | from-screen to-screen, length, what hides the load | 3 (fade, slide, iris/wipe) | `transitions.md`: type, duration, easing, sound cue | prototype frames | `rbx-art` Juice, `rbx-ui` |
| cutscene | story beat, length (seconds), shots, camera moves, who is on screen, skippable | 3 shot lists (storyboard, 4-8 frames each) | `cutscenes.md`: shot table (shot, camera, subject, seconds, sound), skip rule, trigger | FigJam storyboard / HTML strip | cutscene/camera skills via `/rbx find cutscene` |
| vfx | event (hit, pickup, rebirth, level up), mood, budget (particle count) | 3 intensity levels (subtle, normal, loud) | `vfx.md`: per event: shape, colour, count, lifetime, sound | HTML canvas sketch | `rbx-art` Juice, particle-effect-planner pack skill |
| sound/music | events list, mood, loop length, mix rules | 3 palettes (described, with reference words) | `sound.md`: cue table (event, mood, length, volume, loop), music brief | text table | `sound-placement-planner` pack skill; licences via `rbx-assets` |
| loading/menu | brand moment, tips, progress feel, play button | 3 layouts | `menus.md` + frames | frames | `rbx-ui-mockup` -> `rbx-ui` |
| store/monetisation | passes, products, price points (from the KB, never final), what is shown first | 3 shop layouts | `store.md` + frames: tabs, offer cards, price chips, no paid randomness | frames | `rbx-monetize`, `rbx-ui` |
| trailer/ad | 15-30 s hook, 5-8 shots, text overlays, ending card | 3 shot lists | `trailer.md`: shot table, captions, sound, aspect ratios | FigJam storyboard | `rbx-ads`, `rbx-thumb-brief` (video shot list) |
| other | the user names it: brief (what, where seen, size, tone), 3 options, pick | 3 | `<name>.md` | HTML/SVG | the closest specialist, else `/rbx find <words>` |

Extra parts are recorded with `design_gate.py extra <slug> <name> --note "<pick>"`.

## Options-and-approval loop (all types)
Show 3 versions in one message, each with one line: what is different and what it costs to build. Ask for one pick or a mix, nothing else. After the pick, restate it in one line ("UI v2: left stack, coin pill top right, shop 4 columns") and write that line into the part file. If the user asks for "many" (Roman: "don't just do it one, do it many times and find the best"), make 5 instead of 3 for that part, not more.
