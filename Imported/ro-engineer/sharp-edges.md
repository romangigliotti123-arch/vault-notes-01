---
title: "ro-engineer reference - sharp-edges"
source: https://github.com/excaldev/ro-engineer/blob/d86f0c04d902ddd7d1d600359940dcf7524ff604/references/sharp-edges.md
source_repo: https://github.com/excaldev/ro-engineer
source_commit: d86f0c04d902ddd7d1d600359940dcf7524ff604
license: MIT
copyright: "Copyright (c) 2026 excaldev"
status: imported, reference only (third-party text, not verified by this vault, not loaded into sessions)
tags: [imported, reference-only, third-party]
---
> Imported, reference only. Third-party text by excaldev (MIT, see LICENSE and THIRD-PARTY-NOTICES.md in this folder), pinned commit `d86f0c04d9`. Modified: frontmatter added, unverified-tool references removed or marked unverified, vault notes added where marked "vault rule" or "vault note". Where this text and the vault's own skills differ, the skills win (roblox-luau-style, roblox-architecture-choice, roblox-code-rate, roblox-monetisation-setup). Links to files that were not imported (client-server-boundaries, game-loops, market-references, progression-economy, networking-remotes, performance) lead nowhere.

# Sharp edges

Severity: CRITICAL (exploit, data loss) > HIGH (leaks, broken economy,
outages) > MEDIUM (design debt, perf) > LOW (style, minor).

Add real incidents here as you hit them: ID, severity, symptom, cause, fix.

## Security and data

| ID | Severity | Issue | Fix |
|---|---|---|---|
| SE-1 | CRITICAL | Client-trusted state or currency | Authoritative state server-side; client is display only |
| SE-9 | CRITICAL | Price or reward amount taken from the remote payload | Server looks up price/reward from its own config |
| SE-10 | CRITICAL | Granting dev products outside server receipt processing, or not idempotently | Use supported server receipt processing, record ids durably, acknowledge only after saving (vault note: the `MarketplaceService.ProcessReceipt` callback returns `Enum.ProductPurchaseDecision.PurchaseGranted` or `NotProcessedYet`; handlers bound with `BindReceiptHandler` return `Enum.ReceiptDecision.Processed` or `NotProcessedYet`) |
| SE-11 | CRITICAL | DataStore saves without session locking | Use a session-locked data library; otherwise cross-server overwrites lose data |
| SE-12 | HIGH | NaN/inf accepted as numbers (`n ~= n`) | Reject NaN and inf in every numeric validator |
| SE-13 | HIGH | `RemoteFunction:InvokeClient` from the server | Never; a client can yield the server thread forever |
| SE-14 | HIGH | Saving on every change | Save on leave, BindToClose and on an interval; respect budgets |
| SE-15 | HIGH | No save in `BindToClose` | Save all players there; server shutdown otherwise drops recent progress |

## Lifecycle and memory

| ID | Severity | Issue | Fix |
|---|---|---|---|
| SE-2 | HIGH | Leaked connections | Store connections; disconnect via Maid/Trove on cleanup |
| SE-3 | HIGH | Pooled objects keep stale state | End the lease on release, make idle objects inert, reset before reuse |
| SE-16 | HIGH | Per-player tables never cleared | `t[player] = nil` on `PlayerRemoving` |
| SE-17 | MEDIUM | Character connections survive respawn | One trove per character, destroyed on the next `CharacterAdded`/`CharacterRemoving` |
| SE-18 | MEDIUM | Script misses players who joined before it connected `PlayerAdded` | Also loop `Players:GetPlayers()` at start |
| SE-19 | MEDIUM | Streaming: client assumes workspace instances exist | `WaitForChild` with timeout or handle nil; use CollectionService signals |

## Networking

| ID | Severity | Issue | Fix |
|---|---|---|---|
| SE-4 | HIGH | Remote flooding | Per-player server rate limiting |
| SE-20 | MEDIUM | Firing remotes every frame per object | Batch per tick; use UnreliableRemoteEvent for cosmetic streams |
| SE-21 | MEDIUM | Generic "action" remote with string dispatch, unchecked | One remote per intent, or a strict allow-list |

## Design and architecture

| ID | Severity | Issue | Fix |
|---|---|---|---|
| SE-5 | HIGH | Economy with sources but no sinks | Map sources/sinks before shipping; see `progression-economy.md` |
| SE-6 | MEDIUM | Inheritance trees that fight each other | Use components; see `composition.md` |
| SE-7 | MEDIUM | New abstraction without project/workload justification | Apply `pattern-selection.md` criteria |
| SE-8 | MEDIUM | A loop with no early reward | Test an early meaningful reward against intended pacing; see `player-incentives.md` |
| SE-22 | MEDIUM | Hardcoded tuning numbers in logic | Typed, frozen config tables |
| SE-23 | MEDIUM | Unbounded multiplier stacking | Define caps and order of operations |
| SE-24 | MEDIUM | Streak systems that wipe progress on one missed day | Forgiving streaks (grace days, partial keep) |

## Luau and engine

| ID | Severity | Issue | Fix |
|---|---|---|---|
| SE-25 | MEDIUM | Legacy `wait`/`spawn`/`delay` | `task` library |
| SE-26 | MEDIUM | Structural ECS changes invalidate iteration | Follow library guarantees; defer changes when required |
| SE-27 | LOW | `Instance.new(class, parent)` then setting properties | Set properties first, parent last |
| SE-28 | LOW | `Humanoid:LoadAnimation` | `Animator:LoadAnimation` |
| SE-29 | MEDIUM | Gameplay-critical unanchored parts owned by a client | `SetNetworkOwner(nil)` on the server |
| SE-30 | LOW | `:: any` casts to silence strict mode | Fix or narrow the type |
