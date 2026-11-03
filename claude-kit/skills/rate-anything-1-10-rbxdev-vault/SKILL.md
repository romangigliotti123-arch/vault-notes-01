---
name: rate-anything-1-10-rbxdev-vault
description: "General-purpose 1.00-10.00 rater for any thing the user wants judged (an idea, plan, pitch, prompt, design, document, landing page, product, code, skill): picks 5-8 relevant weighted criteria, scores each 1-10 against written anchors with a one-line evidence note, applies a spread rule and caps, computes the weighted total with a script, then lists strengths, weaknesses and ordered fixes with the score each would add. Use when the user says rate this out of 10, score this 1-10, how good is this really, grade my idea, compare these two options, or give me a number and why."
argument-hint: "<thing to rate or path> [what it is for]"
---

# rate-anything-1-10-rbxdev-vault

A repeatable rating, not a vibe. For Roblox game ideas use the specialised game-dev-rate (12 criteria with vault benchmarks); for Luau code use roblox-code-rate; for answers against a reference set use llm-answer-grader. This skill covers everything else.

## Steps
1. **Identify** what is being rated and its purpose/audience (ask at most one question; otherwise write the assumption). Read the thing fully; if a file or URL, open it.
2. **Choose criteria**: 5-8, specific to the type and the purpose, each with a weight (sum 100) and anchors:
   - 1-2: fails or missing; 5: acceptable/average, nothing special; 8+: clearly strong, with proof; 10: exceptional, hard to improve.
   Examples: idea = problem clarity, demand, feasibility, differentiation, effort, risk; landing page = message clarity, trust, call-to-action, visual hierarchy, speed, accessibility; prompt = goal clarity, constraints, examples, testability, robustness.
   State the criteria and weights BEFORE scoring so the user can change them.
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
9. When comparing options, rate each with the same criteria and show a side-by-side table; do not let the order of presentation influence scores.

## Checks
Scores differ across criteria; every extreme score has evidence; weights sum to 100; the total matches the script output; no score is described as a promise of success.

## Failure modes
- Inflated scores (everything 7-8). Use anchors.
- Criteria chosen after seeing the result.
- Rating what you did not read.

## Related
game-dev-rate, roblox-code-rate, llm-answer-grader, ui-critic and accessibility-reviewer agents for design critique.

## Sources
Idea from AI-creator research (catalogue ideas idea-0071). Credit and where it appears:
- Nate Herk, "Best Model for RAG? GPT-4o vs Claude 3.5 vs Gemini Flash 2.0 (n8n Experiment Results)" (2025-01-30) @ 2:39, https://www.youtube.com/watch?v=_DbZjllXDv8&t=159s. Seen there as: Consistent LLM response grader (ChatGPT with source PDF)
- Andrej Karpathy, "Deep Dive into LLMs like ChatGPT" (2025-02-05) @ 1:28:44, https://www.youtube.com/watch?v=7xTGNNLPyMI&t=5324s. Seen there as: LLM judge (answer checker)
- Nate Herk, "Beginner's Guide to Workflow Evaluation in n8n (Stop Guessing!)" (2025-09-03) @ 13:15, https://www.youtube.com/watch?v=-zFd1nPn6U0&t=795s. Seen there as: AI correctness judge (1-5 rater)
- Nate Herk, "3 Hidden Data Table Hacks for Smarter AI Agents" (2025-09-26) @ 13:29, https://www.youtube.com/watch?v=lcNN3X9gXls&t=809s. Seen there as: Correctness evaluator (LLM-as-judge scorer)
- Nate Herk, "5000 Hours of Building AI in Just 17 Minutes" (2026-08-04) @ 9:41, https://www.youtube.com/watch?v=7WZ6XldxX0U&t=581s. Seen there as: LLM-as-a-judge
- Nate Herk, "How to Actually Build & Sell Software with AI as a Non-Techie" (2026-10-02) @ 36:42, https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=2202s. Seen there as: LLM-as-a-judge (customer support reply grader)
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.

