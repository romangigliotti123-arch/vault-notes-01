---
id: "roblox-code-rate"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/roblox-code-rate/SKILL.md"
description: "Rates Luau/Roblox code 1.00-10.00 on weighted criteria (server authority and exploit resistance, data safety, correctness, error handling, performance, structure, testability) with a cited file:line evidence note per score, hard caps for exploitable remotes or data-loss bugs, a script-computed total and ordered fixes with the score each adds."
orig_name: "roblox-code-rate"
orig_argument_hint: "<script path or folder> [what it does]"
tags: [lib/skill, cat/roblox, src/own]
---

# roblox-code-rate

> Rates Luau/Roblox code 1.00-10.00 on weighted criteria (server authority and exploit resistance, data safety, correctness, error handling, performance, structure, testability) with a cited file:line evidence note per score, hard caps for exploitable remotes or data-loss bugs, a script-computed total and ordered fixes with the score each adds.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/roblox-code-rate/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--roblox-audit-fanout]], [[A--own--roblox-luau-reviewer]], [[S--own--game-dev-benchmark]], [[S--own--game-dev-critic]], [[S--own--game-dev-rate]], [[S--own--roblox-architecture-choice]], [[S--own--roblox-datastore-safe-save]], [[S--own--roblox-luau-style]], [[S--own--roblox-performance-pass]], [[S--own--roblox-remote-security]]

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
| test | Testability and verification (playtest script, assertions, observable checks; capped by the evidence ladder below) | 6 |
| maint | Maintainability (config separated, no magic numbers, no narrating comments) | 6 |

Anchors: 1-2 = broken or dangerous; 5 = works but with notable gaps; 8 = solid with only minor issues; 10 = exemplary and hard to improve.

## Steps
1. Read the scope (scripts and how they interact). Get the reviewer findings (roblox-luau-reviewer) with severities.
2. Run the sharp-edges checklist below over the scope and attach the open SE ids to the criterion they hurt. Score each criterion 1-10 starting from 5. Every score of 8+ or 3- cites at least one `path:line` or a metric; otherwise write `judgment`.
3. **Caps** (apply after the weighted total): a client-writable currency/progress remote or any unvalidated remote with server-side effect -> max 4.0; a confirmed data-loss path (no save on leave, overwritten saves) -> max 5.0; a server crash reachable from client input -> max 4.5; a receipt path that can grant twice or grant before the save (SE-10) -> max 5.0.
4. **Compute** with a script: `python -c "import json,sys;d=json.loads(sys.argv[1]);print(round(sum(w*s for w,s in d.values())/sum(w for w,s in d.values()),2))" '{"sec":[22,6],...}'` and apply caps by `min`.
5. Output: table (criterion | weight | score | evidence), total, band (<4 unsafe to ship, 4-5.9 needs work, 6-7.4 shippable with fixes, 7.5+ solid), cap notes.
6. **Fixes**: ordered by score gain; each names the finding id, the criterion it lifts and the expected new score. Offer a re-rate after fixes.

## Sharp-edges checklist
Severity: CRITICAL (exploit, data loss, dupes) > HIGH (leak, outage, broken economy) > MEDIUM (design debt, perf) > LOW (style). Report each open item as `SE-n path:line fix`; omit the ones that do not apply.

| ID | Sev | Issue | Fix |
|---|---|---|---|
| SE-1 | CRITICAL | Client-trusted state or currency | Server owns state; client displays |
| SE-9 | CRITICAL | Price or reward read from the remote payload | Server looks it up in its own config |
| SE-10 | CRITICAL | Dev product granted outside the receipt callback, twice, or before the save | One server receipt handler, record the purchase id durably, return the grant decision only after the save (see below) |
| SE-11 | CRITICAL | DataStore saves without session locking | Session-locked data module; otherwise servers overwrite each other |
| SE-12 | HIGH | NaN or inf accepted as a number | Reject `n ~= n` and `math.huge` in every numeric validator |
| SE-13 | HIGH | `RemoteFunction:InvokeClient` from the server | Never: an erroring or silent client breaks or hangs the server thread; use a RemoteEvent |
| SE-14 | HIGH | Saving on every change | Save on leave, in `BindToClose` and on an interval, within request budgets |
| SE-15 | HIGH | No save in `BindToClose` | Save all players there (30 second window) |
| SE-2 | HIGH | Leaked connections | Cleaner per lifetime (roblox-luau-style) |
| SE-3 | HIGH | Pooled objects keep stale state | End the lease on release, reset before reuse |
| SE-16 | HIGH | Per-player tables never cleared | `t[player] = nil` on `PlayerRemoving` |
| SE-4 | HIGH | Remote flooding | Per-player server rate limit |
| SE-5 | HIGH | Economy with sources but no sinks | Map sources and sinks before shipping |
| SE-17 | MEDIUM | Character connections survive respawn | Cleaner per character |
| SE-18 | MEDIUM | Misses players who joined before `PlayerAdded` connected | Also loop `Players:GetPlayers()` |
| SE-19 | MEDIUM | Client assumes workspace Instances exist (streaming) | `WaitForChild` with timeout, handle nil, tag signals |
| SE-20 | MEDIUM | Remote fired every frame per object | Batch per tick; `UnreliableRemoteEvent` for cosmetic streams |
| SE-21 | MEDIUM | One generic "action" remote dispatching on a string | One remote per intent or a strict allow-list |
| SE-22 | MEDIUM | Tuning numbers hard-coded in logic | Typed, frozen config tables |
| SE-23 | MEDIUM | Multipliers stack without a cap | Define caps and order of operations |
| SE-24 | MEDIUM | A streak wiped by one missed day | Grace days or partial keep |
| SE-25 | MEDIUM | Legacy `wait`, `spawn`, `delay` | `task` library |
| SE-26 | MEDIUM | ECS structural change during iteration | Follow the library's guarantees, defer changes |
| SE-29 | MEDIUM | Gameplay-critical unanchored parts owned by a client | `SetNetworkOwner(nil)` on the server |
| SE-6 | MEDIUM | Inheritance trees fighting each other | Components (roblox-architecture-choice) |
| SE-7 | MEDIUM | Abstraction added without workload evidence | Apply roblox-architecture-choice |
| SE-8 | MEDIUM | Loop with no early reward | Test an early reward against the intended pacing |
| SE-27 | LOW | `Instance.new(class, parent)` before properties are set | Properties first, `Parent` last |
| SE-28 | LOW | `Humanoid:LoadAnimation` | `Animator:LoadAnimation` |
| SE-30 | LOW | `:: any` casts to silence strict mode | Fix or narrow the type |
| SE-31 | LOW | Narrating comments (comment lines that say WHAT the code does) | Delete them; keep one line only for a non-obvious WHY (roblox-luau-style, Comments). `comment_scan.py` in game-dev-critic/scripts counts them |

Receipts, verified against the Roblox docs 2026-11-04: the `MarketplaceService.ProcessReceipt` callback (one script, server only) returns `Enum.ProductPurchaseDecision.PurchaseGranted` once the grant is saved and `NotProcessedYet` otherwise, which makes Roblox deliver the receipt again. The `MarketplaceService:BindReceiptHandler(receiptType, handler, filter)` handlers return `Enum.ReceiptDecision.Processed` or `NotProcessedYet`. Never mix the two enums, and dedupe by `PurchaseId` (or `TransferRequestId`).

## Evidence ladder: generated is not tested
| Rung | Establishes | Does not establish |
|---|---|---|
| Generated or read | The proposed logic | That it runs |
| Type-checked (luau-lsp with Roblox definitions, Studio analysis) | Compatibility with the type definitions | Runtime payload safety, engine behaviour |
| Unit-tested (Lune, TestEZ, Jest-Lua; project runner) | The tested logic and edge cases | Replication, physics, persistence |
| Studio or multiplayer playtest | Observed engine, client and server behaviour | Every device and production scenario |
| Profiled | Cost in a recorded workload | A universal speedup |
| Security test | The tested attack paths | That no exploit remains |

Report the highest rung actually reached and name the command or session. Never write tested, works or fixed for code that is only generated or read. Leaks need repeated join/leave cycles with counts; speedups need the same workload before and after. If nothing could run, list the static checks and the manual tests to run. The `test` criterion scores at most 4 when the top rung is generated or read.

## Code-quality gate record (for game-dev-benchmark)
When the code belongs to a game (`Games/<slug>/`), also write `code-quality/gate.json`; game-dev-benchmark discovers it as an extra gate (weight 10, not required):
```json
{"kind": "code-quality", "scorer": "critic", "pass_min": 7, "rung": "type-checked",
  "checks": {"SE-1": 10, "SE-9": 0, "SE-2": 3, "SE-25": 6, "SE-27": 8},
  "result": "fail", "reasons": ["SE-9 Shop.server.luau:42 price from payload"],
  "failing": [{"path": "Shop.server.luau:42", "check": "SE-9", "fix": "read price from config"}]}
```
The comment scan is its own gate: `comment_scan.py <project> --write Games/<slug>` writes `comment-scan/gate.json` (checks CM1-CM3, weight 10 like any extra gate), a scored finding that never blocks. Include only applicable ids. Passing item = 10; an open item scores CRITICAL 0, HIGH 3, MEDIUM 6, LOW 8. `result` is `fail` while any CRITICAL, HIGH or MEDIUM item is open.

Credit: checklist adapted from excaldev/ro-engineer `sharp-edges.md` and `testing.md` (MIT, Copyright (c) 2026 excaldev); reference copies in Imported/ro-engineer. Rows were re-checked against the Roblox docs.

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


## Triggers (moved out of the description)

Use when the user says rate my Luau code, score this script out of 10, how good is my Roblox code, compare these two implementations, code quality score before launch, or after a roblox-luau-reviewer pass.
