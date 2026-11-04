# Critic report body (verdict.py adds the frontmatter and the "Why" line above it)

## 1. WORKS (does it run safely?) - pass | fail | fail-severe
| Check | Command / how | Result (exact excerpt) |
|---|---|---|
| static scan | `static_scan.py <project>` | |
| luau-check / tests | | |
| Output / playtest (Studio MCP, or "Studio not connected") | | |

## 2. GOOD (would a stranger stay, return, pay?) - scored 1-10, only the factors of this stage
| Factor | Score | Evidence (file:line, measured time, quote, number + note path) | Compared with (hit game / benchmark) |
|---|---|---|---|
| F1 first 30 seconds | | | |
| F2 core loop | | | |
| F3 clarity | | | |
| F4 feel | | | |
| F5 progression | | | |
| F6 social | | | |
| F7 monetisation fairness | | | |
| F8 packaging | | | |
| F9 performance and stability | | | |
| F10 scope and polish | | | |
Mean (from verdict.py): | Critical factors: |

## 2b. LOOKS (visual gate: screenshots scored by the critic, stage prototype or later) - pass | fail | skipped
| Item | Score | Screenshot + what is visible | Open defects |
|---|---|---|---|
| V1 UI consistency | | | |
| V2 Layout and overlap | | | |
| V3 Readability and hierarchy | | | |
| V4 Models and world | | | |
| V5 Lighting and atmosphere | | | |
| V6 Effects and juice | | | |
| V7 First 30 seconds | | | |
Status line if not pass: `playable prototype, visuals not polished`. Backlog: `Games/<slug>/polish-backlog.md`.

## 2c. PLACEMENT (placement gate `rbx-placement`: the critic's own full-map scan, stage prototype or later) - pass | fail | skipped
| Check | Models failing | Worst example (path, measured value) | Fix |
|---|---|---|---|
| P1 pivot and size | | | |
| P2 grounded | | | |
| P3 upright | | | |
| P4 facing and yaw | | | |
| P5 clearance (overlap, z-fight, bounds) | | | |
| P6 physics flags | | | |
| P7 connections | | | |
Scan: `Games/<slug>/placement-qa/scan-critic.json` (models, waived, ignored, fingerprint). Status line if not pass: `playable prototype, placement not verified`.

## 2d. LIGHTING (lighting gate `rbx-lighting`: the critic's own scan, stage prototype or later) - pass | fail | skipped
| Check | Measured | Tolerance | Fix |
|---|---|---|---|
| L1 not default Roblox look | | | |
| L2 Atmosphere | | | |
| L3 Sky | | | |
| L4 effect ranges | | | |
| L5 palette cohesion | | | |
| L6 brightness (samples / screenshots) | | | |
| L7 shadows | | | |
| L8 fog density for the genre | | | |
| L9 interiors | | | |
| L10 performance budget | | | |
| L11 duplicates | | | |
| L12 time of day | | | |
Scan: `Games/<slug>/lighting-qa/scan-critic.json`. Status line if not pass: `playable prototype, lighting not verified`.
## 3. What the hits in this genre have that this does not
(2-4 bullets, each with a case-study note path, patterns only)

## 4. Top 3 fixes (ordered by score gain)
1. Fix | lifts F? from ? to ? | cheapest way | who/what does it
2.
3.

## 5. What would prove this wrong
Metric, threshold (with benchmark note and flag), when it can be measured.

## 6. Honest summary for the user (3 lines, plain words)

Links: [[<slug>/GAME|GAME]] | [[<slug>/design|design]] | KB notes used: [[Roblox/roblox-kb/...]]
