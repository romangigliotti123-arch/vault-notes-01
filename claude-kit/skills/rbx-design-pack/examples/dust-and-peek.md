# Worked example: a museum-heist game, design pack before code

Source: lessons of a real build session (a multiplayer museum heist with per-player plots). No private data; numbers are the ones the user finally approved or labelled assumptions.

What went wrong without the pack: the UI was built blind and redone ("buttons are all unorganised ... not happy at all"; "do it many times and find the best one"); the world was redone several times ("looks like a baseplate when you zoom out", "too cluttered", "copy other similar games"); plot size ("at least 2x") and hall width ("3 times wider") changed after building. What worked: the voxel style tested first on one crown plus 8 models.

## Run with the pack (what the user sees)
1. `design_gate.py init dust-and-peek`. Figma check (stage start): not connected -> the connect steps are printed once. User: "no Figma for now" -> fallback noted, re-offered at stage style.
2. refs: 5 games (steal-a-collectible shapes, plot tycoons). Table row: "Game A: ring of plots around a plaza, hall at one end, phone HUD left stack; keep: plots visible from plaza; avoid: empty ground between zones". One lesson: "players leave when the walk from plot to goal is over 25 s". User confirms the list. `approve refs`.
3. style: 3 looks on the same 6 props (crown, vase, guard, pet, wall piece, coin icon): A flat pastel, B voxel with thick outline, C glossy toy. Rendered side by side. User picks B ("pixelated" look from his own reference photos). Palette hex, outline 4 px at 1080p, tri budget 300 per prop recorded. `approve style`.
4. ui: HUD, shop, inventory, upgrades at 844x390: 3 versions each in HTML (no Figma). User mixes: "HUD v2, shop v3, inventory v1, upgrades v2" and asks for 5 versions of the HUD; gets 5. Notes: left button stack, coin pill top right, goal pill, nothing under the 36 px topbar strip. `approve ui`.
5. map: three layouts at 1 cell = 10 studs: A ring of 10 plots around a plaza with the museum at the north; B linear (spawn, hall, plots); C hub and spokes. Comparison to the refs: A borrows the ring, new: the museum hall as a long zone-by-zone corridor; risk "plots too small". User picks A with "plots 2x bigger, hall 3x wider than the first idea": numbers go into `map.md` as the builders' constants (plot 120 x 120, hall 72 wide, 108 long per zone). `approve map`.
6. plan: one page (look B, four UI picks, map A, risks: guard chase readability on phone, plaza empty at night; M0 done, M1 = greybox of map A with the core loop steal -> carry -> place). User: "yes, that is it". `approve plan` -> `DESIGN GATE: PASS`.

Then `rbx-art` takes the style part as input, `rbx-ui-prototype` -> `rbx-ui` the picked screens, and M1 builds the greybox of map A. The rework of the first session (UI three times, map four times) becomes one pick each, done before code.
