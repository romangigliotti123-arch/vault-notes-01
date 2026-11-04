# Gate formats (stable: other tools read these)

W3 benchmark tooling and `verdict.py` / `games.py` / `visual_gate.py` read the files below. Fields may be added; existing fields keep their names and meaning. Version fields: scan `version` 1.

## Folder layout (per game)
```
Games/<slug>/lighting-qa/
  scan-builder.json     the builder's scan (evidence, guides the fix loop)
  scan-critic.json      the critic's own fresh scan (decides; --scorer critic)
  gate.json             gate record for the builder scan
  gate-critic.json      gate record for the critic scan
```

## scan JSON (`kind: "lighting-scan"`)

Version 1, produced by `LightingKit.scan` and `lighting_gate.py ingest`; colours `[r, g, b]` 0-255 except `samples[].albedo` (0-1). [cold:rbx-lighting/gate-json-schemas.md] read only to hand-write, parse or debug a scan JSON.

## report JSON (`kind: "lighting-report"`, inside the scan)

`status` is `fail` when any check is `fail` and not waived with a reason of >= 10 characters; a `skip` does not fail the report, the gate fails a skipped L6. [cold:rbx-lighting/gate-json-schemas.md] read only to hand-write, parse or debug a report JSON or its fix actions.

## gate record (`gate.json`, `gate-critic.json`)

`visual_gate.py` reads `result`; `verdict.py` evaluates the critic's scan itself and does not trust this file. [cold:rbx-lighting/gate-json-schemas.md] read only to hand-write, parse or debug a gate record.

## verdict file line
`Games/<slug>/critic/<date>-<stage>.md` front matter gains `lighting: pass | fail | skipped | n/a` next to `visual:` and `placement:`. `games.py advance` needs `lighting: pass` from prototype on; a file without the line reads as `missing` (blocked until a fresh critic pass).

## CLI and exit codes
```
python lighting_gate.py <scan.json> [--project DIR] [--write Games/<slug>] [--scorer critic] [--genre G] [--platform P] [--shots-from-visual Games/<slug>] [--shots a.png ...]
python lighting_gate.py ingest <console.txt> --write Games/<slug> [--scorer builder|critic] [--game SLUG] [--genre G] [--platform P] [--name N] [--shots-from-visual DIR]
python lighting_gate.py recheck <scan.json>
python lighting_gate.py image-stats <a.png> [b.png ...]
```
Exit 0 = PASS (or SAME for recheck), 1 = FAIL (or DIFF, or an unreadable file). First output line: `LIGHTING GATE: PASS|FAIL | scorer S | genre G | phase P | platform X | n/12 checks pass`; then `STATUS LABEL: ...`, the reasons, and `  FAIL L<n> <name> :: <issues>` with `       suggested fix: ...`.

`--genre` and `--platform` (from GAME.md) override what the scan recorded: the critic passes the game's declared genre, so a horror game cannot pass by applying the obby preset. `image-stats` prints one JSON line per PNG: `{ "path", "mean", "crushed", "blown", "w", "h" }` (8-bit PNG, not interlaced; JPEG is not supported, capture PNG).
