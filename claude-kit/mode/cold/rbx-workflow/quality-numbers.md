<!-- cold: rbx-workflow/quality-numbers.md | read when: read when you must quote a benchmark band (D1/D7/session/PTR/CTR/conversion); compare.py gives the same numbers. -->

## From skills/rbx-workflow/references/quality-model.md :: Numbers that decide "is it working"

Use `rbx-metrics/compare.py`. The official method is the Creator Hub Similar Experience Benchmarks (50th-90th percentile for similar games): read those first.

| Metric | Weak / broken | Typical | Strong | Flag |
|---|---|---|---|---|
| D1 retention | under 6 broken, 6-10 weak | 10-16 | over 16 (90th percentile for the genre per an official talk) | mixed |
| D7 retention | under 1.5 weak | 2-4 | over 4 | indie |
| D30 | KB gap (low D30 = missing endgame, official) | - | - | official |
| Average session | under 5 min bad | 5-7 average, 7-9 good | 9+ excellent, 15+ very strong | mixed |
| Play-through (PTR) | under 2 low | 2-3 okay | over 3 healthy | mixed |
| Ad/thumbnail CTR | under 1 replace the creative | 1.5-2.5 below average | 2.5-3.5+ | indie |
| Payer conversion | under 1 low | 1-2 okay (official sample 1.63) | 2-3+ | mixed |

Genre, audience age and traffic source (ads and external traffic retain worse than Home recommendations) move every number. A number with no benchmark is `KB gap`, never a guess.

## From skills/rbx-workflow/references/quality-model.md :: Hits versus flops in the 120 case studies (`case-studies-*.md`; patterns only, never copy another game)

Patterns: hype without a reason to return fades; big updates revive games; reputation does not rescue a weak concept; a proven loop plus 10-20% change beats a pure clone or a pure original.

## From skills/rbx-workflow/references/quality-model.md :: The one rule behind everything

Importance order (official, `retention-d1-d7`): fun and retention, then monetisation, then acquisition. Doubling the retention of a game whose core loop is not fun still gives zero (`core-loops-and-game-design`). A polished game nobody wants is the commonest flop (`common-mistakes`: validate demand and ship).
