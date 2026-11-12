# Reference step, style test, map layout, one-page plan

## 1. Reference collection (before any design)
Pick 3-6 games that already work in the same shape (the vault KB `rbx-trends`/`rbx-research` lists what leads; ask the user for 1-2 they love). Sources: vault reference images (`.rbx/claude-kit/reference-path.txt` line 1 = folder with `INDEX.md`; grep it for genre words, Read 3-6 images; they are third-party frames, comparison only), the KB case studies, and a quick web look. Write `refs.md`:

| Game (genre) | First 30 s | Map shape and size (studs if known) | UI on screen | Look | Keep | Avoid |
|---|---|---|---|---|---|---|

then 5 lines: what ALL of them share (the genre contract), what none of them do (the opening), the three map shapes seen (ring, hall, hub and spokes, ...), the three UI layouts seen, the one lesson. Patterns only; never copy names, art or layouts 1:1. The user confirms the list ("these are the right games") before step 2.

## 2. Style test (brief and approval)
Brief: mood words, palette idea, shape rule (blocky, rounded, voxel), outline thickness, tri budget per prop, the rule "one look for everything".
Pick 3-8 hero props that cover the look: the most repeated prop, the most valuable item, one character or pet, one building piece, one ground/wall piece, one UI-facing icon. Build them for real (Blender, or `generate_mesh` / Studio) and render them in the lighting of the game (`rbx-lighting` preset): a drawing is not a style test. 3 looks on the same props (A/B/C), shown side by side with the same camera. The user picks; the part file records palette hex, outline, tri budget, material rules, the rendered image paths. Lesson (Dust & Peek): testing the style on a crown plus 8 models first worked well; it is the cheapest step in the pack. Approval hands the look to `rbx-art` (StyleKit values, art-direction.md).

## 3. Map layout template (`map.md`; draw as one image or Figma frame, 1 cell = 10 studs)
1. Scale line: world size in studs and in minutes of walking (walk speed 16 studs/s: a 200-stud hall is about 12 s).
2. Zones: name, job, size in studs (W x D), who is there, entry points. Starting guesses (UNVERIFIED, replace them with numbers measured from the reference games): plot 60 x 60 per player (bigger when it has levels or a build area), hall width 24-40 and length 100+ per progression zone, plaza 120 x 120 or more so players see each other's plots, spawn 20 x 20 with 2 exits.
3. Flow arrows: spawn -> goal -> home -> repeat; mark the shortest and the main routes; the loop must be walkable in the target time.
4. Sightlines: what the player sees from spawn (a landmark within 150 studs), from the plaza (other players' plots), from the goal (the next goal).
5. Landmarks: 3-5 numbered pins visible from far; each has a silhouette and a colour different from the zone around it.
6. Prop density per zone: low (open play), medium, high (visual interest), as props per 100 x 100 studs, plus "ground variation" (not one flat colour, not a baseplate when zoomed out); no empty gaps over 40 studs without a reason.
7. Reference comparison: this layout against the 2-3 map shapes in `refs.md`: what is borrowed (pattern), what is new, and one line per risk (cluttered, empty, too long, plots too small).
8. Phone check: the key objects stay readable at 1/3 scale (a phone-sized screenshot of the layout).
Three layouts A/B/C (different shapes, not size changes); the user picks; size numbers in `map.md` become the builders' constants (Config table).

## 4. UI examples (summary; frames in `figma.md`)
Key screens: HUD, main menu, shop, inventory, the game's own panel (upgrades, goals). 3 versions each, phone frames first (780x360, 844x390, 667x375), then tablet and desktop for the picked version only. Each version differs in structure (where the stack sits, what is always visible), not only colour. Show with the style-test palette applied. A pick per screen, a one-line note per pick.

## 5. One-page plan (`plan.md`, fits one screen)
```
# <Game> design plan (approved <date>)
Fantasy and one-line loop: ...
Look: style v<n> (palette hex, outline, tri budget), hero props: ...
UI: HUD v<n>, menu v<n>, shop v<n>, inventory v<n> (frames/links)
Map: layout <A/B/C>, size, zones with stud sizes, flow, landmarks
References: 3-6 games, the one lesson
Open risks (max 3) and what the first playtest must answer
Build order: M0 design pack (done) -> M1 core loop on the greybox of this map -> ...
Not decided yet: (list; each has an owner and a date)
```
Approval = the user says it matches what they pictured. Then `design_gate.py approve <slug> plan` and the build may start; M1 builds the picked map's greybox with the approved sizes, never invented ones.
