# Quick critique at 100 px (run before the full scored rubric)

This is a 60-second filter, not a replacement for `[cold:rbx-thumbnail/rubric.md]` (3 gates and 13 weighted checks, scored with `scripts/thumb_score.py`). It decides which candidates are worth scoring. Look at the strip that `thumb_compose.py compose` or `strip` writes (true-size 100/200/400 px, colour above and greyscale below). Answer each line yes or no and write the answers into the candidate's notes.

| # | Question (at 100 px wide, colour row) | If no |
|---|---|---|
| 1 | Subject: can a stranger name the hero in one noun? | enlarge the hero, remove the second subject |
| 2 | Action: can they say what is happening in one verb? | change the pose or add the prize or threat |
| 3 | Emotion: one clear feeling on the face or in the pose? | exaggerate the eyes and mouth, or add the reaction |
| 4 | Text: readable and 3 words or fewer (or none)? | cut words, thicken the outline, enlarge |
| 5 | Greyscale row: does the hero still separate from the background? | change value contrast: darken the scene or lighten the hero, add outline and glow |
| 6 | Colour: at most two saturated hues plus the hero's? | cut a hue, desaturate the background |
| 7 | Edges: nothing important in the bottom 15% or within 4% of an edge? | move it up or in |
| 8 | Honest: is everything shown in the game's first minute? | remove the element, or change the game's first minute (never the other way round) |

Decision: 7 or 8 yes = score it fully; 5 or 6 yes = fix the failed lines, then re-render; 4 or less = pick a different template.
Then: `thumb_score.py template` -> fill the gates and the 13 checks by looking at the full-size image and the 100 px strip -> `thumb_score.py score`. Pass is 32 of 46 with no failed gate (the vault's assumption). Cap three rounds, then ship the best or change the concept.

Notes for pairs: judge the icon and each thumbnail on their own strips (different job, see roblox-mapping.md); put the candidates beside 5 to 10 competitors from the live front page at the same size before gate G3 (originality).
