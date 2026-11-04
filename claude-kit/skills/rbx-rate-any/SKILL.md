---
name: rbx-rate-any
description: "General 1.00-10.00 rater for anything the user wants judged (idea, plan, prompt, design, document, product, code, skill): 5-8 weighted criteria against written anchors with evidence, caps, script-computed total, ordered fixes."
argument-hint: "<thing to rate or path> [what it is for]"
---

# rbx-rate-any

A repeatable rating, not a vibe. Roblox game ideas: rbx-rate (12 criteria with vault benchmarks); Luau code: rbx-code-rate; answers against a reference set: llm-answer-grader. This skill covers everything else.

## Steps
1. **Identify** what is rated and its purpose/audience (ask at most one question; otherwise write the assumption). Read the thing fully; open any file or URL.
2. **Choose criteria**: 5-8, specific to the type and the purpose, each with a weight (sum 100) and anchors:
   - 1-2: fails or missing; 5: acceptable/average, nothing special; 8+: clearly strong, with proof; 10: exceptional, hard to improve.
   Examples: idea = problem clarity, demand, feasibility, differentiation, effort, risk; landing page = message clarity, trust, call-to-action, visual hierarchy, speed, accessibility; prompt = goal clarity, constraints, examples, testability, robustness.
   State criteria and weights BEFORE scoring so the user can change them.
3. **Score** each criterion 1-10. Default 5. Any 8+ or 3- needs a concrete evidence line (quote, number, observation); mark unsupported judgments `judgment`.
4. **Spread rule**: if more than 60% of scores are within one point of each other, re-score against the anchors; real work rarely scores flat.
5. **Caps**: define 1-3 hard gates (for example "does not work as intended" caps the total at 4.0; "unsafe or deceptive" caps at 3.0). Apply them and say so.
6. **Compute** with a script, not in your head:
   ```
   python -c "import json,sys;d=json.loads(sys.argv[1]);print(round(sum(w*s for w,s in d.values())/sum(w for w,s in d.values()),2))" '{"clarity":[25,7],"demand":[20,5]}'
   ```
   Show the table: criterion | weight | score | evidence.
7. **Band**: <4 weak, 4-5.9 mixed, 6-7.4 solid, 7.5-8.9 strong, 9+ exceptional (almost never).
8. **Fixes**: top 3 strengths, top 3 weaknesses, then fixes ordered by score gain; each names the criterion it lifts and the expected new score. Add one "what would prove this wrong" test.
9. Comparing options: same criteria for each, side-by-side table; presentation order must not influence scores.

## Checks
Scores differ across criteria; every extreme score has evidence; weights sum to 100; the total matches the script output; no score is described as a promise of success.

## Failure modes
- Inflated scores (everything 7-8). Use anchors.
- Criteria chosen after seeing the result.
- Rating what you did not read.

## Related
rbx-rate, rbx-code-rate, llm-answer-grader, ui-critic and accessibility-reviewer agents for design critique.

## Sources

[cold:rbx-rate-any/sources.md] read only to verify the source of this idea or its licence/attribution.