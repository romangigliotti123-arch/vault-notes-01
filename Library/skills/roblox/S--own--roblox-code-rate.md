---
id: "roblox-code-rate"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-code-rate/SKILL.md"
description: "Rates Luau/Roblox code 1.00-10.00 on weighted criteria (server authority and exploit resistance, data safety, correctness, error handling, performance, structure and readability, testability) with a cited file:line evidence note per score, hard caps for exploitable remotes or data-loss bugs, a script-computed total and ordered fixes with the score each adds. Use when the user says rate my Luau code, score this script out of 10, how good is my Roblox code, compare these two implementations, code quality score before launch, or after a roblox-luau-reviewer pass."
orig_name: "roblox-code-rate"
orig_argument_hint: "<script path or folder> [what it does]"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-code-rate

> Rates Luau/Roblox code 1.00-10.00 on weighted criteria (server authority and exploit resistance, data safety, correctness, error handling, performance, structure and readability, testability) with a cited file:line evidence note per score, hard caps for exploitable remotes or data-loss bugs, a script-computed total and ordered fixes with the score each adds. Use when the user says rate my Luau code, score this script out of 10, how good is my Roblox code, compare these two implementations, code quality score before launch, or after a roblox-luau-reviewer pass.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-code-rate/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--roblox-audit-fanout]], [[A--own--roblox-luau-reviewer]], [[S--own--game-dev-rate]], [[S--own--roblox-datastore-safe-save]], [[S--own--roblox-luau-style]], [[S--own--roblox-performance-pass]], [[S--own--roblox-remote-security]]

Creator videos (notes are in the AI Library Vault, Creators/videos): 2025-01-30-best-model-for-rag-gpt-4o-vs-claude-3-5-vs-gemini-flash-2-0, 2025-02-05-deep-dive-into-llms-like-chatgpt, 2025-09-03-beginner-s-guide-to-workflow-evaluation-in-n8n-stop-guessing, 2025-09-26-3-hidden-data-table-hacks-for-smarter-ai-agents, 2026-08-04-5000-hours-of-building-ai-in-just-17-minutes, 2026-10-02-how-to-actually-build-sell-software-with-ai-as-a-non-techie

---
# roblox-code-rate

The code counterpart of game-dev-rate (which rates game ideas). Rating is derived from evidence, so run or reuse a review first: invoke roblox-luau-reviewer (or read its report) and use its findings as the evidence base. Do not re-implement the review here.

## Criteria and weights
| Key | Criterion | Weight |
|---|---|---|
| sec | Server authority and exploit resistance (remotes validated, rate-limited, no client trust) | 22 |
| data | Data safety (DataStore saves, retries, session locking, receipts, no dupes) | 16 |
| corr | Correctness (logic, nil/race/yield handling, edge cases) | 18 |
| err | Error handling and logging (pcall use, no silent failures, useful messages) | 10 |
| perf | Performance (no per-frame waste, connection cleanup, instance/table growth) | 12 |
| struct | Structure and readability (modules, naming, style per roblox-luau-style) | 10 |
| test | Testability and verification (playtest script, assertions, observable checks) | 6 |
| maint | Maintainability (config separated, no magic numbers, comments where needed) | 6 |

Anchors: 1-2 = broken or dangerous; 5 = works but with notable gaps; 8 = solid with only minor issues; 10 = exemplary and hard to improve.

## Steps
1. Read the scope (scripts and how they interact). Get the reviewer findings (roblox-luau-reviewer) with severities.
2. Score each criterion 1-10 starting from 5. Every score of 8+ or 3- cites at least one `path:line` or a metric; otherwise write `judgment`.
3. **Caps** (apply after the weighted total): a client-writable currency/progress remote or any unvalidated remote with server-side effect -> max 4.0; a confirmed data-loss path (no save on leave, overwritten saves) -> max 5.0; a server crash reachable from client input -> max 4.5.
4. **Compute** with a script: `python -c "import json,sys;d=json.loads(sys.argv[1]);print(round(sum(w*s for w,s in d.values())/sum(w for w,s in d.values()),2))" '{"sec":[22,6],...}'` and apply caps by `min`.
5. Output: table (criterion | weight | score | evidence), total, band (<4 unsafe to ship, 4-5.9 needs work, 6-7.4 shippable with fixes, 7.5+ solid), cap notes.
6. **Fixes**: ordered by score gain; each names the finding id, the criterion it lifts and the expected new score. Offer a re-rate after fixes.

## Failure modes
- Rating without a review: scores become taste. Run the reviewer first.
- Flat scores: use the anchors; security and data usually score lowest in prototypes.
- Rating generated code the same as hand-written: rate what is there.

## Related
roblox-luau-reviewer, roblox-remote-security, roblox-datastore-safe-save, roblox-luau-style, roblox-performance-pass, game-dev-rate, rate-anything-1-10-rbxdev-vault, roblox-audit-fanout.

## Sources
Idea from AI-creator research (catalogue ideas idea-0071). Credit and where it appears:
- Nate Herk, "Best Model for RAG? GPT-4o vs Claude 3.5 vs Gemini Flash 2.0 (n8n Experiment Results)" (2025-01-30) @ 2:39, https://www.youtube.com/watch?v=_DbZjllXDv8&t=159s. Seen there as: Consistent LLM response grader (ChatGPT with source PDF)
- Andrej Karpathy, "Deep Dive into LLMs like ChatGPT" (2025-02-05) @ 1:28:44, https://www.youtube.com/watch?v=7xTGNNLPyMI&t=5324s. Seen there as: LLM judge (answer checker)
- Nate Herk, "Beginner's Guide to Workflow Evaluation in n8n (Stop Guessing!)" (2025-09-03) @ 13:15, https://www.youtube.com/watch?v=-zFd1nPn6U0&t=795s. Seen there as: AI correctness judge (1-5 rater)
- Nate Herk, "3 Hidden Data Table Hacks for Smarter AI Agents" (2025-09-26) @ 13:29, https://www.youtube.com/watch?v=lcNN3X9gXls&t=809s. Seen there as: Correctness evaluator (LLM-as-judge scorer)
- Nate Herk, "5000 Hours of Building AI in Just 17 Minutes" (2026-08-04) @ 9:41, https://www.youtube.com/watch?v=7WZ6XldxX0U&t=581s. Seen there as: LLM-as-a-judge
- Nate Herk, "How to Actually Build & Sell Software with AI as a Non-Techie" (2026-10-02) @ 36:42, https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=2202s. Seen there as: LLM-as-a-judge (customer support reply grader)
The library item is an original Claude Code implementation of the creator's idea, not a copy of their file.
