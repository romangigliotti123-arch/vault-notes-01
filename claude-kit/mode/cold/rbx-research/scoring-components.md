<!-- cold: rbx-research/scoring-components.md | read when: read only to see how each score component is computed from data and model ratings. -->

## From skills/rbx-research/references/scoring.md :: | Component | From data (always) | From model ratings (`rank

| Component | From data (always) | From model ratings (`rank.py judge`, 0-5) |
|---|---|---|
| relevance | share of topic keywords in their titles (60%) and number of search hits (40%) | blended 70% rating, 30% data |
| depth | typical video length / description length / README size proxy | deep dives and primary sources high, news and clips low |
| recency | exp(-days since last post / 180) | n/a |
| consistency | posts per month from a sample of their latest items, capped at 4 per month | n/a |
| engagement | percentile of average views / stars / score among that source's candidates | n/a |
| credibility | official or organisation flag and followers percentile | practitioner, maintainer, primary source |
| originality | neutral 0.5 | original work and data vs rehash |
