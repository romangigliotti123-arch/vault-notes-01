---
id: "rbx-code-rate"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-code-rate/SKILL.md"
description: "Reviews, rates Luau/Roblox code ('review my code', pre-delivery) 1.00-10.00 on weighted criteria (server authority, exploits, data safety, correctness, performance, structure, testability) with file:line evidence, hard caps for exploits, scripted total, fixes."
orig_name: "rbx-code-rate"
orig_argument_hint: "<script path or folder> [what it does]"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-code-rate

> Reviews, rates Luau/Roblox code ('review my code', pre-delivery) 1.00-10.00 on weighted criteria (server authority, exploits, data safety, correctness, performance, structure, testability) with file:line evidence, hard caps for exploits, scripted total, fixes.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-code-rate/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[A--own--rbx-auditor]], [[A--own--rbx-reviewer]], [[S--own--rbx-bench]], [[S--own--rbx-critic]], [[S--own--rbx-datastore]], [[S--own--rbx-rate-any]], [[S--own--rbx-remote-sec]]

---
# rbx-code-rate

The code counterpart of rbx-rate (which rates game ideas). Rating is derived from evidence, so run or reuse a review first: invoke rbx-reviewer (or read its report) and use its findings as the evidence base. Do not re-implement the review here.

## Criteria and weights
| Key | Criterion | Weight |
|---|---|---|
| sec | Server authority and exploit resistance (remotes validated, rate-limited, no client trust) | 22 |
| data | Data safety (DataStore saves, retries, session locking, receipts, no dupes) | 16 |
| corr | Correctness (logic, nil/race/yield handling, edge cases) | 18 |
| err | Error handling and logging (pcall use, no silent failures, useful messages) | 10 |
| perf | Performance (no per-frame waste, connection cleanup, instance/table growth) | 12 |
| struct | Structure and readability (modules, naming, style per rbx-luau) | 10 |
| test | Testability and verification (playtest script, assertions, observable checks; capped by the evidence ladder below) | 6 |
| maint | Maintainability (config separated, no magic numbers, no narrating comments) | 6 |

Anchors: 1-2 = broken or dangerous; 5 = works but with notable gaps; 8 = solid with only minor issues; 10 = exemplary and hard to improve.

## Steps
1. Read the scope (scripts and how they interact). Get the reviewer findings (rbx-reviewer) with severities.
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
| SE-2 | HIGH | Leaked connections | Cleaner per lifetime (rbx-luau) |
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
| SE-6 | MEDIUM | Inheritance trees fighting each other | Components (rbx-arch) |
| SE-7 | MEDIUM | Abstraction added without workload evidence | Apply rbx-arch |
| SE-8 | MEDIUM | Loop with no early reward | Test an early reward against the intended pacing |
| SE-27 | LOW | `Instance.new(class, parent)` before properties are set | Properties first, `Parent` last |
| SE-28 | LOW | `Humanoid:LoadAnimation` | `Animator:LoadAnimation` |
| SE-30 | LOW | `:: any` casts to silence strict mode | Fix or narrow the type |
| SE-31 | LOW | Narrating comments (comment lines that say WHAT the code does) | Delete them; keep one line only for a non-obvious WHY (rbx-luau, Comments). `comment_scan.py` in rbx-critic/scripts counts them |

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

## Code-quality gate record (for rbx-bench)
When the code belongs to a game (`Games/<slug>/`), also write `code-quality/gate.json`; rbx-bench discovers it as an extra gate (weight 10, not required):
```json
{"kind": "code-quality", "scorer": "critic", "pass_min": 7, "rung": "type-checked",
  "checks": {"SE-1": 10, "SE-9": 0, "SE-2": 3, "SE-25": 6, "SE-27": 8},
  "result": "fail", "reasons": ["SE-9 Shop.server.luau:42 price from payload"],
  "failing": [{"path": "Shop.server.luau:42", "check": "SE-9", "fix": "read price from config"}]}
```
The comment scan is its own gate: `comment_scan.py <project> --write Games/<slug>` writes `comment-scan/gate.json` (checks CM1-CM3, weight 10 like any extra gate), a scored finding that never blocks. Include only applicable ids. Passing item = 10; an open item scores CRITICAL 0, HIGH 3, MEDIUM 6, LOW 8. `result` is `fail` while any CRITICAL, HIGH or MEDIUM item is open.

## Failure modes
- Rating without a review: scores become taste. Run the reviewer first.
- Flat scores: use the anchors; security and data usually score lowest in prototypes.
- Rating generated code the same as hand-written: rate what is there.

## Related
rbx-reviewer, rbx-remote-sec, rbx-datastore, rbx-luau, rbx-perf, rbx-rate, rbx-rate-any, rbx-auditor.

## Sources

[cold:rbx-code-rate/sources.md] read only to verify the source of this idea or its licence/attribution.
