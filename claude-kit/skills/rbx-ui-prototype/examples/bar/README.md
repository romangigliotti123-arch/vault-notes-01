# Moonlit Bakery: the quality-bar prototype

`index.html` is the reference for how good a vault UI prototype looks and feels (open it in a browser; `Notes` shows the craft checklist, not-buildable list and sound cues). It is a mock-up, not a game. `examples/index.html` (Candy Quarry) stays the small template for the page chrome and the 11 sections; this folder shows the craft level to aim for.

Copy from it:
- Buttons (`.btn`: ring, lip, face gradient, gloss, shine; 3 sizes x 5 colours; press, release, hover, disabled, loading, success, hold ring, badge) and the Lab screen that shows them.
- Currency pills, panels with header band and close, cards with rarity, tabs with a sliding indicator, nav (bottom bar or side rail), progress bars with moving stripe.
- Motion helpers in section 6: `fly` (currency along a curve into the counter), `burst` (canvas particles with gravity), `shake`, `flash`, `flip` (list reorder and shared element), count-up in the loop.
- Reward stage (chest shake, burst, slam, rarity text, rays) and level-up.
- Per device layout table in DATA (`DEVICES`: nav bottom or rail, columns, detail pane side or below).
- Sound cue names and the Reduce Motion handling.
Do not copy the pastries, names, prices or art; replace the theme and keep the structure. `handoff.md` maps each part to Roblox instances and TweenInfo values; `spec.json` is the brief for `/rbx-ui`.
