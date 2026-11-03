# Rating rubric (12 criteria, 1-10 each, weighted overall 1.00-10.00)

Default weights live in `scripts/score.py` (sum 100) and are derived from the vault. Where the freshest `_tools/DECISION-RULES` / `BENCHMARKS` contradict a rationale below, pass a weight override and say why in the report.

| id | criterion | wt | why this weight (vault evidence; paths under `Roblox/roblox-kb/`) |
|---|---|---|---|
| loop | Core loop strength | 14 | Official docs rank D1 levers core loop first, first-time experience second, performance third (`retention-d1-d7.md`, flag mixed, 2026-10). "Define a ~30-second loop before coding" (`core-loops-and-game-design.md`). |
| ret | Retention potential (D1 / D7 / D30) | 14 | Roblox: engagement carries by far the most weight in Home ranking: time played, session count, retention over weeks (`discovery-algorithm.md`, official, 2026-05). Targets and flags come from `_tools/BENCHMARKS.md` (headline D1/D7 rows; indie rows are anecdotes). |
| f30 | First-30-seconds hook | 10 | "Give a win or reward in the first 30 seconds" and match the thumbnail promise (`first-session-onboarding.md`, mixed, 2026-08). A gate criterion. |
| feel | Fluidity and feel | 8 | Game feel/juice, input response, camera, sound (`player-psychology-and-game-feel.md`, `vfx-and-particles.md`, `sound-and-music.md`); felt in the first minute and at 60 fps on a phone (`optimization-and-streaming.md`). |
| social | Virality and co-play | 9 | Co-play is a Home ranking signal; players with friends: about 30% longer sessions, 60% more likely to return D0-D1 (`retention-d1-d7.md`, official, 2026-10; `social-features-and-virality.md`). |
| money | Monetisation fit | 9 | Cosmetics/convenience/passes without gating core progress; repeatable = product, permanent = pass (`monetisation-gamepasses.md`, `_tools/CHECKLIST-monetization.md`, `_tools/PRICE-LADDER.md`). A gate criterion. |
| disc | Discoverability and thumbnail-ability | 8 | Play-through rate and thumbnail quality drive Home (`thumbnails-icons.md`, `titles-descriptions.md`, `discovery-algorithm.md`): one searchable hook word and an obvious image. |
| scope | Production cost and scope | 8 | Solo first release is a 2-4 week MVP; finished simple beats unfinished complex (`development-process-and-speed.md`, indie). A gate criterion. Scored for the team/time the plan assumes. |
| diff | Differentiation | 5 | Saturation and "known formula plus one twist" (`trend-research-and-validation.md`, `game-ideas-and-genres.md`). |
| trend | Trend fit | 5 | Alignment with what is performing now; correlation is not cause, so low weight (`trend-research-and-validation.md`; live check). |
| ad | Ad-ability | 3 | `_tools/AD-PLAYBOOK.md`: ads cannot rescue a weak game; fix retention first. Low weight on purpose. |
| upd | Update potential | 7 | Players leave when out of content; cadence and events (`updates-live-ops.md`, `events-and-seasonal-content.md`). |

## Scoring rules
- Integers or halves, 1-10. **Default is 5, not 7.** Every score of 8+ or 3- needs a cited fact (note path, kbq link or live source) or the words `judgment` / `ESTIMATE` in its evidence line. One evidence line (<= 25 words) per criterion.
- Anchors (use them; 2, 4, 6, 8 sit between):
  | id | 1 | 3 | 5 | 7 | 9 |
  |---|---|---|---|---|---|
  | loop | no repeatable action-reward cycle | cycle over 5 min or weak reward | action, reward, upgrade under 2 min, thin variety | under 1 min, 3 layers (moment/session/meta), varied | tight under 30 s, deep meta, still pulls on day 7 |
  | ret | nothing to return for | one hook (progression only) | two hooks | three hooks incl. social or collection that reinforce | persistent goals, live events, social ties, clear D7 reason |
  | f30 | tutorial/reading before fun | action understood in a minute | fun action within 10 s, taught by doing | reward in 15 s and first upgrade in 2 min | wow moment in 5 s, instantly readable, first win guaranteed |
  | feel | clunky controls, no feedback | works, flat | decent feedback on core action | strong juice, sound, camera, smooth on phone | every action feels great, polish is the hook |
  | social | solo only, nothing to show | optional leaderboard | co-op possible | co-play inside the loop, invites, friends bonus | friends 10x more fun, strong clips, trading/parties safe |
  | money | only pay-to-win or paid randomness | passes feel bolted on | cosmetics/convenience, free players get the full game | 3-6 well-placed passes/products with clear moments | monetisation is part of the fantasy, others see it, never gates progress |
  | disc | no hook, hard to title | clear genre, generic title/image | one searchable hook word, readable image | strong thumbnail concept, top-3 search terms owned | iconic image + title, easy to clip |
  | scope | needs a team, custom netcode, over 3x time | fits time, 1-2 risky systems | MVP in the planned time | MVP in half the time using libraries/CC0 assets | trivially small MVP, content scales cheaply |
  | diff | reskin | known formula + 1 twist | fresh combination, clear in 30 s | new verb in a proven frame | unseen yet obvious |
  | trend | against what is rising | neutral | matches 1 current pattern | matches 2+ patterns and a rising one | right pattern at the right moment, low saturation |
  | ad | cannot show the game in 5 s | possible | clear hook visual | strong 5 s clip + thumbnail test ready | creative sells itself |
  | upd | one-shot content | monthly content needed, costly | seasonal/event hooks | modular content, cheap weekly drops | content is player-generated or systemic |
- **Spread rule:** after scoring, if the 12 scores sit within a 2-point band, re-score the best and worst criterion strictly against the anchors, and state the new spread. Real ideas are rarely 7 everywhere.
- **Caps (computed by `scripts/score.py`):** any gate criterion (loop, f30, money, scope) at 2 or less caps the overall at 5.00; `violates_rules` (pay-to-win, paid randomness, real-money gambling, stranger contact without safeguards) caps it at 3.00.
- **Bands:** 8.50+ exceptional (build now) · 7.00-8.49 strong · 5.50-6.99 viable with fixes · 4.00-5.49 weak, rework · below 4.00 reject/restart. No score is a promise of success; give the result that would prove it wrong.
