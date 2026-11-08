# Sample run: "Lava Climb" (an invented obby, drawn from scratch)

A real run of the workflow in SKILL.md steps 2a, 4b and 4a with `scripts/thumb_compose.py`. The game, the blocky hero, the tower, the lava and the lava drop are all drawn by `scripts/thumb_demo.py`: no real person, no other game's art, no studied thumbnail. Redraw everything with
`python -I scripts/thumb_compose.py demo --out <dir>` (about 10 seconds, needs Pillow).

## Step 2a: hook and three concepts
- Game facts (invented): obby, climb a 50-floor block tower while lava rises; the first minute is a climb with rising lava.
- Hook (verb + object + stake, true in the first minute): outclimb rising lava.
- Three concepts that differ in composition (`references/composition-templates.md`), with the library entries they borrow from (`references/example-library.md`):

| Concept | Template | Library entries | Subject and expression | Colour pair | Text |
|---|---|---|---|---|---|
| A `concept-a-face-left` | face-left-prize-right | 6 (terror, wall of threat), 7 (prize beside a calm crowd), 25 (outline as the rule) | hero close-up, wide-eyed fear, looks toward the tower | yellow hero on deep purple, orange lava at the foot | RUN! (1 word) |
| B `concept-b-tiny-hero` | tiny-hero-huge-scene | 9 (tiny figure, huge danger), 17 (planks over a void) | tiny hero arms up on top of a 50-floor tower | warm hero on navy, lava glow | 50 FLOORS (2 words) |
| C `concept-c-object` | object-only | 28 (one object on flat colour), 39 (radical minimalism) | one giant lava drop, hero small at the side (thumbnail only) | orange on violet | none |

## Step 4b: compose and critique at 100 px
Command per concept (spec files are `concept-*/spec.json`; layer files in `layers/`):
`python -I scripts/thumb_compose.py compose concept-a-face-left/spec.json --out out/a`
Printed by the composer (concept A): `SUMMARY: 12 PASS, 0 WARN`. Concept B first run: `WARN ... hero vs background luminance difference 0.02`; one round of fixes (darker navy sky, hero moved above the tower top, text moved to the left slot and enlarged from 6 px to 8+ px tall at 100 px) gave `SUMMARY: 10 PASS, 2 WARN`, the 2 WARN being the remaining hero/background luminance difference on the thumbnail (0.15) and icon (0.06). Concept A first run also warned on the hero (0.09); a darker background lifted it to a pass. Concept C passes all checks.

Reading `concept-a-face-left/strip-thumbnail.png` (true-size 100/200/400 px, colour above, greyscale below): at 100 px the face, the tower and RUN! are all still readable and the hero separates from the background in greyscale. In the same file the lava bar at the bottom is the only busy area, and it sits in the bottom 15% where no text is placed (`guides-thumbnail.jpg` shows the zones).

Files kept here: concept A full set (thumbnail and icon PNG, both strips, guides, report.json); concepts B and C as JPEG thumbnail and icon plus report.json (JPEG only to keep the kit small; the composer itself writes PNG); `contact-sheet.jpg` shows all three with their icons.

## Step 4a: scored with `thumb_score.py` (the rubric in `[cold:rbx-thumbnail/rubric.md]`)
`python -I scripts/thumb_score.py score scores.json` (output in `score-output.txt`): A 40/46 PASS, B 30/46 FAIL (pass bar 32 is the vault's assumption). Fix-first list for A: genre legibility (the tower is small), the curiosity gap, implied motion. Gates G1 (promise is real) and G3 (original against competitors) are marked pass because the game is invented: with a real game they need the first-minute screenshot and a look at 5 to 10 competitor tiles.

## What the sample shows and what it does not
- It shows the process end to end and what the checks print. It does not measure click-through: only a Roblox variant test with qualified play-through decides (`[cold:rbx-thumbnail/protocol.md]`).
- The art style (flat blocky vector) is a stand-in for the owner's real character render; replace `layers/hero.png` and `layers/tower.png` with your own cut-outs.
