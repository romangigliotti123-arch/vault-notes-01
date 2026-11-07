---
name: rebirth-system-builder
description: "Build a prestige (rebirth) loop: growing cost, explicit reset and keep lists, permanent multiplier, stale-request guard against double clicks, max rebirths, on the pack Wallet. Use for simulators and idle games; wallet design is currency-system-builder."
category: systems
tags: rebirth, prestige, reset, multiplier, simulator, idle, progression, cost curve, double click, wallet
kb: Roblox/roblox-kb/case-studies-rebirth-speed-run.md, Roblox/roblox-kb/case-studies-simulator-genre-notes.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/retention-d1-d7.md
related: currency-system-builder, upgrade-tree-builder, pet-system-builder, boost-potion-builder, core-loop-designer, datastore-schema-builder
---

# rebirth-system-builder

One job: let a player trade progress for a permanent bonus without exploits. `scripts/Rebirth.luau` prices each rebirth (`floor(baseCost * growth^n)`), refuses stale or repeated requests by comparing the count the client saw, spends through the Wallet, runs YOUR reset function, then raises the count; the multiplier is `1 + count * gainPerRebirth` (additive so late numbers stay readable). Configs that make rebirth free or a pure loss are rejected at construction.

## When to use
Prestige/rebirth systems in simulators, tycoons and idle games. Not for: designing the whole loop (`core-loop-designer`), skill-tree upgrades (`upgrade-tree-builder`), temporary boosts (`boost-potion-builder`).

## Inputs (max 2)
1. What resets and what is kept (default: reset currency, zones, tools; keep premium currency, passes, pets, badges, settings). 2. Cost curve and gain (default: base 1000, growth 2.5, +0.5x per rebirth, cap 50).

## Procedure
1. Write the reset and keep lists explicitly in `design/rebirth.md`; anything not on the keep list resets. Vault: a rebirth must feel faster than the first run (new multiplier) or players stop using it; also decide what the player sees as the reward before confirming (`nextMultiplier`).
2. Pick the curve with numbers, not feel: simulate time-to-afford for rebirth 1..10 against the expected earn rate and check the gap stays within the session length you want; tune `growth` and `gainPerRebirth` until each rebirth takes similar or slowly rising time. Mark values as first guesses.
3. Copy `Rebirth.luau`; `Rebirth.new({ wallet, currency = "Coins", baseCost, growth, gainPerRebirth, maxRebirths, reset = function(data) ... end })`. The reset function sets the currency to 0 through your own code path and reinitialises zone/tool fields; it must not touch kept fields.
4. Remote `Rebirth(seenCount)` (rate-limited): `rebirth:attempt(data, seenCount)`. A double click or replay carries a stale count and is refused ("stale request"). The client only sees the result string and the new state.
5. Apply the multiplier on the server where earnings are computed: `earn = base * rebirth:multiplier(data) * pets:power(...)`; combine multipliers by a written rule (multiply across systems, add inside one) and cap the product.
6. Save immediately after a successful rebirth (`PlayerData:SaveAsync`) so a crash cannot revert the reset but keep the benefit or the reverse.
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/rebirth-system-builder/scripts/tests/Rebirth.test.luau` (quote the "N passed, 0 failed" line); test the reset function against a data table with kept and reset fields.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Rebirth.luau` and your reset function -> `start_stop_play` -> `execute_luau` (Server) to grant coins, rebirth twice with the same seen count, and print the data table -> `get_console_output` to read the result. The confirm dialog and effects are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (UI, the real reset function against the real data template) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/case-studies-rebirth-speed-run.md` and `case-studies-simulator-genre-notes.md` (rebirth/prestige as the main long-term loop in simulators; creator-reported), `Roblox/roblox-kb/core-loops-and-game-design.md` (keep sources and sinks balanced; scale conversion costs), `Roblox/roblox-kb/retention-d1-d7.md`. No verified vault numbers exist for rebirth curves: every number here is a labelled guess to playtest.

## Output
`Rebirth.luau` with config and reset function, the remote, `design/rebirth.md` (reset/keep lists, cost table for rebirth 1..10, multiplier rule).

## Acceptance checks
- [ ] A replayed or double-clicked request does not rebirth twice (Rebirth test 3).
- [ ] Cannot-afford changes nothing (test 4); max rebirths is enforced (test 5).
- [ ] Kept fields survive and reset fields reset (test 2, and your own test on the real template).
- [ ] Free or losing configs are rejected (test 6).
- [ ] Rebirth Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/rebirth-system-builder/scripts/tests/Rebirth.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
A reset that forgets a field (players keep a zone or tool and skip the loop). A cost that grows slower than income so rebirth becomes spam. Multiplier stacking with pets and boosts into numbers that overflow display or break leaderboards. No confirmation, so a stray click wipes progress. Rebirth available in the first minutes.

## Related
`currency-system-builder`, `upgrade-tree-builder`, `pet-system-builder`, `boost-potion-builder`, `core-loop-designer`.
