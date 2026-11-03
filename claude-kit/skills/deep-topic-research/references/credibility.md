# Creator credibility stage (optional)

Set at the start by depth: off (Light default and "just go"), top5, top10 (Moderate), all (Heavy / Exhaustive). Official sources are never audited. Runs after `synth.py themes` (so "most cited" is known) and before `trust.py verify`.

## Per creator or publisher
1. Pick exactly 2 pieces from the cache, no re-download: piece 1 = the most cited in the topic notes (ties: relevance, then id); piece 2 = random among the rest with a fixed seed (`random.Random("<seed>-<creator>")`, default seed 20260101, shown in the output). A creator with one extracted piece gets one.
2. Evidence packet per piece (code, no model): up to 10 extracted claims, for each the best-matching official facts and the matching claims of OTHER creators, plus regex counts and snippets for hype, income/result promises and sponsor/affiliate wording in the cached full text (transcript or page text).
3. One judge call per creator (headless pool = cap, or a worker in mode A) lists up to 6 checkable claims per piece with a verdict CORRECT / OUTDATED / WRONG / UNVERIFIABLE / OPINION and a basis (official, other-sources, both, own-knowledge, none), and rates evidence, depth and honesty 0-10 plus a one-line signals note (unsupported promises, clickbait, hype, sponsor pitching, outdated advice, original depth vs rehash).
4. Score in code (`cred.py score`): accuracy = 10 x (CORRECT + 0.5 x OUTDATED) / (CORRECT + OUTDATED + 3 x WRONG); score = 50% accuracy + 20% evidence + 15% depth + 15% honesty. TRUSTED >= 7.5, MIXED 5.0-7.4, WEAK < 5.0, INSUFFICIENT when fewer than 4 claims were verified (no score). Confidence is forced to low when most verified claims rest on model knowledge instead of shown evidence, and capped at medium for a single piece.

## Wording
Factual and non-defamatory: the judge is told to describe claims and evidence, never character; a reason containing accusatory words is replaced in code by a count summary; every table repeats that a verdict describes the sampled pieces and not the person, and that claims are AI-extracted summaries.

## Use in synthesis
- Theme synthesis sees `cred=WEAK|MIXED|TRUSTED` on each line and weights sources accordingly.
- WEAK is never the sole source of a claim (flagged "sole source rated WEAK", kept out of the cheat sheet) and does not count as the second source for CORROBORATED.
- MIXED needs a second source before a claim is trusted.
- INSUFFICIENT = unknown, treated neutrally.
Output: `creator-credibility.md` (table, method, seed, cost) and a credibility column in `creators.md`.
