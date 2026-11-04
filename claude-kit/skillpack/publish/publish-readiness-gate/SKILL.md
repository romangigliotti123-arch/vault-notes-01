---
name: publish-readiness-gate
description: "Run the final go/no-go gate: 13 launch gates, each pass needs evidence, each waiver needs a reason and an accountable owner, any fail or missing status is NO-GO. gate.py computes the verdict so it cannot be argued into. Use as the last step before pressing publish."
category: publish
tags: launch, go no-go, gate, readiness, checklist, evidence, waiver, publish, release
kb: Roblox/roblox-kb/_tools/CHECKLIST-launch.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/updates-live-ops.md
related: age-rating-prep, rbx-launch-check, rbx-publish, post-launch-monitor, exploit-audit, playtest-bot-writer
---

# publish-readiness-gate

One job: turn "are we ready?" into evidence. The gate list covers playtest, data safety, purchases, security, performance, mobile/console UI, content rules, asset licences, store page, settings, analytics, backup and the first-72-hours plan. `scripts/gate.py` reads a JSON of gates and prints a verdict: pass needs evidence (a command with output, a path, a link or a sourced number), waived needs a reason and an owner, na needs a reason, fail or unknown is blocking. Pressing publish is the owner's action.

## When to use
Before the first public publish and before major updates. Not for: running the checks themselves (each gate names the skill that does), post-launch monitoring (`post-launch-monitor`), the long checklist in the vault (`rbx-launch-check`).

## Inputs (max 2)
1. The project and what changed (default: the whole game for a first launch). 2. Who accepts risk (default: the owner).

## Procedure
1. Create the file: `python -I ~/.claude/claude-kit/skillpack/publish/publish-readiness-gate/scripts/gate.py --template > release/gates.json`. Edit the gate list to the game (add gates, mark genuinely irrelevant ones `na` WITH a reason).
2. For each gate, run the named skill or check NOW (not from memory), paste the evidence line (command + exact output excerpt, file path + hash, or link), and set `status`. Vault checklist items to include where relevant: validate gifting and trading on the server and run dupe tests, test on mobile, save/rejoin tests, store assets final.
3. Anything you cannot verify yet is `fail` or an explicit `waived` with an owner and a reason. A waiver is a decision someone owns, not a way to turn red into green.
4. Run `python -I .../gate.py release/gates.json`; it prints each gate, the waived list and `VERDICT: GO` or `NO-GO` (exit 0 / 1).
5. On NO-GO: list blocking gates with the skill that fixes each, fix, re-run the evidence and the script. Do not edit the script to pass.
6. On GO: save `release/gates.json` and the verdict output with the date (it is the release record), record the version/restore point (`version-history-keeper`), and tell the owner it is theirs to publish.
7. Self-test the script: `python -I .../gate.py --selftest` prints `selftest ok`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add nothing (this skill records evidence from other skills) -> `start_stop_play` -> `execute_luau` (Server) to run the quick playtest evidence (`get_console_output` after a short play session) that feeds the playtest gate -> `get_console_output` to read the result. Studio tools produce evidence; they do not decide the verdict.

## Fallback
Same: the gate file and script are plain files. Everything that needs a running Studio session (every gate's underlying check unless its evidence shows it ran) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/_tools/CHECKLIST-launch.md` (the merged launch checklist: gifting/trading validated on the server with dupe tests, pre-release test with the content audience, final store assets), `Roblox/roblox-kb/playtesting-and-feedback.md`, `Roblox/roblox-kb/testing-debugging-and-qa.md`, `Roblox/roblox-kb/updates-live-ops.md`. The 13 gates are this pack's synthesis of those lists; the vault checklist is longer.

## Output
`release/gates.json` (all gates with status and evidence), the printed verdict, and the list of waivers with owners.

## Acceptance checks
- [ ] Every gate has a status; every `pass` has evidence; every `waived` has a reason and an owner (the script enforces it).
- [ ] `gate.py release/gates.json` printed a verdict (quote the `VERDICT:` line).
- [ ] `gate.py --selftest` prints `selftest ok`.
- [ ] A NO-GO was never turned GO by editing the script or deleting a gate without a reason.
- [ ] The release record is saved with the date.

## Pitfalls
Filling evidence from memory. Using `waived` as a pass. Dropping gates that are inconvenient (use `na` with a reason so it shows). Treating GO as proof the game is good: it only says the checks ran. Running the gate once at the start and not after the last change.

## Related
`age-rating-prep`, `rbx-launch-check`, `rbx-publish`, `post-launch-monitor`, `exploit-audit`, `playtest-bot-writer`.
