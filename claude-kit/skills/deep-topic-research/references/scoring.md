# Creator and publisher score (transparent)

Score = 0.25 relevance + 0.20 depth + 0.15 recency + 0.10 consistency + 0.10 engagement + 0.10 credibility + 0.10 originality. Each component is 0-1. Weights live in `scripts/rank.py` (`W`); change them there if a topic needs it (for example raise recency for fast-moving tech).

| Component | From data (always) | From model ratings (`rank.py judge`, 0-5) |
|---|---|---|
| relevance | share of topic keywords in their titles (60%) and number of search hits (40%) | blended 70% rating, 30% data |
| depth | typical video length / description length / README size proxy | deep dives and primary sources high, news and clips low |
| recency | exp(-days since last post / 180) | n/a |
| consistency | posts per month from a sample of their latest items, capped at 4 per month | n/a |
| engagement | percentile of average views / stars / score among that source's candidates | n/a |
| credibility | official or organisation flag and followers percentile | practitioner, maintainer, primary source |
| originality | neutral 0.5 | original work and data vs rehash |

Unrated candidates are marked "(heuristic)" in `creators.md`. Always run the judge: heuristics cannot tell the Hawaiian "luau" party from the Luau language. Once a source has been judged, only judged candidates (the 30 with the most search hits) can be selected. Candidates with relevance below 0.15 are dropped, so a source with nothing relevant yields no creators and is reported as such. The top N per source are selected (N = 3 / 6 / 10 for Quick / Thorough / Exhaustive).

Within a creator, items are ordered newest-first and most-engaged-first (union of both rankings), divided by title relevance. Across creators the run order is `creator_score x (0.5 + relevance) / (1 + rank_within_creator / 20)`, so the best creators come first but no single back-catalogue starves the rest.
