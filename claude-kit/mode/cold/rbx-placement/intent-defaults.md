<!-- cold: rbx-placement/intent-defaults.md | read when: read only when setting project-wide defaults or name-pattern rules for intents. -->

## From skills/rbx-placement/references/intent.md :: Project-wide defaults go in `Placement.config.core` (floatTo

Project-wide defaults go in `Placement.config.core` (floatTol, buryTol, defaultYawGrid, bounds ...) or per call in `opts`. Rules by name pattern: `opts.rules = { { pattern = "^lamp", intent = { kind = "lamp" } } }`; explicit by path: `opts.intents = { ["Workspace.Map.Door1"] = {...} }`. Precedence (later wins): defaultIntent, ground name, inferred kind, rules, `opts.intents`, the stored attribute.
