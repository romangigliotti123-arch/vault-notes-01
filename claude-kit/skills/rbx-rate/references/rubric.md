# Rating rubric (12 criteria, 1-10 each, weighted overall 1.00-10.00)

Default weights live in `scripts/score.py` (sum 100) and are derived from the vault. Where the freshest `_tools/DECISION-RULES` / `BENCHMARKS` contradict a rationale below, pass a weight override and say why in the report.

| id | criterion | wt |
|---|---|---|
| loop | Core loop strength | 14 |
| ret | Retention potential (D1 / D7 / D30) | 14 |
| f30 | First-30-seconds hook | 10 |
| feel | Fluidity and feel | 8 |
| social | Virality and co-play | 9 |
| money | Monetisation fit | 9 |
| disc | Discoverability and thumbnail-ability | 8 |
| scope | Production cost and scope | 8 |
| diff | Differentiation | 5 |
| trend | Trend fit | 5 |
| ad | Ad-ability | 3 |
| upd | Update potential | 7 |

Gate criteria: loop, f30, money, scope. Why each weight (vault evidence): [cold:rbx-rate/weight-evidence.md] read only to justify or override a criterion weight (vault evidence per criterion).

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

## Ethics column: fair or pressure (retention, monetisation, social, update hooks)
Many Roblox players are children. Label each hook the idea uses fair or pressure; treat design hypotheses as hypotheses and measure with the real audience. A `pressure` label is a weakness on its criterion and a fix; paid randomness and pay-to-win still set `violates_rules` (cap 3.00).
| Principle (criterion) | Fair | Pressure |
|---|---|---|
| Variable reward (ret, money) | Free rolls earned by play, a guaranteed minimum value, honest odds | Paid rolls (this vault bans them), hidden odds, faked near-misses |
| Scarcity and urgency (ret, upd) | Restock cycles of minutes that create a rush in play; rare spawns that reward whoever is online | Purchase countdowns, "never coming back", deadlines of days that force a login time |
| Loss aversion (ret) | Theft or loss with ways to protect yourself by playing, cheap to rebuild | Losses only a purchase prevents, streak wipe after one missed day, guilt messages |
| Goal gradient, completion (ret) | Bars and sets where every slot is earnable by play | A bar that slows near the end to sell a skip; sets finishable only with paid or expired items |
| Return hooks (ret, upd) | Daily or offline rewards that never destroy progress when skipped; offline caps | Absence costs progress |
| Social proof (social) | Showing off, co-op bonuses, achievable leaderboard tiers | Status for sale, shaming non-payers |
| Peak-end (ret, money) | Best moment at the end of a run, quick retry after failure | A purchase prompt timed to the emotional peak or during intense play |
Hook test (write the answers in the report): which principle, fair or pressure version, what the player gets if they ignore it, does missing it punish or only not reward, would you explain it to a parent. Vault rules win over the source ideas: no paid random rewards (Roblox allows them with disclosed odds and `PolicyService` `ArePaidRandomItemsRestricted` checks; this vault does not), no pressure timers aimed at kids.
Credit: adapted from excaldev/ro-engineer `retention-psychology.md` (MIT, Copyright (c) 2026 excaldev); copy in Imported/ro-engineer.
