# Calibration: three sample ideas (so scores are not all 7s)

Scores were put through `scripts/score.py` (`python score.py file.json`). Use these as anchors for how far apart real ideas land. Order of ids: loop ret f30 feel social money disc scope diff trend ad upd.

| sample | idea | scores | overall | band | why it lands there |
|---|---|---|---|---|---|
| A | Co-op escape-room obby where each friend has a different ability and rooms need all of them | 8 7 8 7 9 7 8 6 7 7 7 8 | **7.49** | strong | co-play is the loop (social 9), clear hook word, modular rooms for updates; scope 6 because puzzle rooms need tuning |
| B | Single-player pizza tycoon, droppers and conveyor upgrades | 5 4 6 5 3 6 4 8 2 3 4 5 | **4.75** | weak | trivial to build (scope 8) but saturated formula (diff 2), solo (social 3), no reason to return after the upgrade path ends |
| C | Realistic open-world survival MMO, custom combat and netcode, paid loot crates | 4 5 3 4 6 2 5 1 5 4 4 6, violates_rules | **3.00** (raw 4.07) | reject | paid randomness triggers the rule cap; scope 1 and money 2 trip the gate cap as well |

Spread: 7.49, 4.75 and 3.00 from the same rubric. If your ratings for very different ideas land within 1 point of each other, the scoring is too soft: re-read the anchors in `rubric.md`.

Typical mistakes to avoid: scoring monetisation 8 because "passes exist" (anchor 7 needs well-placed moments, 9 needs it to be part of the fantasy), scoring first-30-seconds 8 without naming the second-by-second action, scoring trend fit from memory (it needs the live check), and giving every criterion the idea's overall mood.
