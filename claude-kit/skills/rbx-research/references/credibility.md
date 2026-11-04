# Creator credibility stage (optional)

Set at the start by depth: off (Light default and "just go"), top5, top10 (Moderate), all (Heavy / Exhaustive). Official sources are never audited. Runs after `synth.py themes` (so "most cited" is known) and before `trust.py verify`.

## Per creator or publisher
1. Pick exactly 2 pieces from the cache, no re-download: piece 1 = most cited in the topic notes (ties: relevance, then id); piece 2 = random among the rest with a fixed seed (`random.Random("<seed>-<creator>")`, default 20260101, shown in the output). One extracted piece = one.
2-3. Evidence packet per piece (code, no model: up to 10 extracted claims with official facts and other creators' matching claims, plus regex counts for hype, income/result promises and sponsor wording); one judge call per creator (headless pool = cap, or a worker in mode A) returns up to 6 checkable claims per piece with verdict CORRECT / OUTDATED / WRONG / UNVERIFIABLE / OPINION and basis, plus evidence, depth and honesty ratings 0-10. [cold:rbx-research/credibility-judge.md] read only to see the evidence-packet contents and the judge call's output fields.
4. Score in code (`cred.py score`): accuracy = 10 x (CORRECT + 0.5 x OUTDATED) / (CORRECT + OUTDATED + 3 x WRONG); score = 50% accuracy + 20% evidence + 15% depth + 15% honesty. TRUSTED >= 7.5, MIXED 5.0-7.4, WEAK < 5.0, INSUFFICIENT when fewer than 4 claims were verified (no score). Confidence is forced to low when most verified claims rest on model knowledge instead of shown evidence, and capped at medium for a single piece.

## Wording
Factual and non-defamatory: the judge describes claims and evidence, never character; a reason containing accusatory words is replaced in code by a count summary; every table says a verdict describes the sampled pieces and not the person, and that claims are AI-extracted summaries.

## Use in synthesis
- Theme synthesis sees `cred=WEAK|MIXED|TRUSTED` on each line and weights sources accordingly.
- WEAK is never the sole source of a claim (flagged "sole source rated WEAK", kept out of the cheat sheet) and is not the second source for CORROBORATED.
- MIXED needs a second source before a claim is trusted. INSUFFICIENT = unknown, treated neutrally.
Output: `creator-credibility.md` (table, method, seed, cost) and a credibility column in `creators.md`.
