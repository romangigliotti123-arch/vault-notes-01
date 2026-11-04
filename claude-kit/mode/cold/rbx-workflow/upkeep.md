<!-- cold: rbx-workflow/upkeep.md | read when: read only once a month or after a run with 2+ BLOCKED jobs. -->

## From skills/rbx-workflow/references/manager.md :: 11. Upkeep (monthly)

Once a month, or after a run with 2+ BLOCKED jobs, run the pack skill `workflow/failure-miner` (`skillpack.py path failure-miner`) over `jobs.md`, `briefs/` and critic files: it groups repeated failures into brief or routing fixes. Apply them to the brief template or `routing.md` (kit side: tell the user, do not edit the vault).
