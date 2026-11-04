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
Produced by `LightingKit.scan` (console `LIGHTING_SCAN_PART` chunks) and by `lighting_gate.py ingest`.
```
{ "kind": "lighting-scan", "version": 1, "game": "slug", "scorer": "builder" | "critic", "datamodel": "Edit",
  "captured_at": "2026-11-04T10:00:00Z",
  "config": { "genre": "obby", "time": null, "platform": "both" | "pc" | "mobile", "theme": { "bg": [r,g,b], "panel": ..., "accent": ..., "accent2": ... }, "waive": { "L5": "reason" }, "bands": { } },
  "state": { "lighting": { "Technology", "Brightness", "ClockTime", "GeographicLatitude", "Ambient", "OutdoorAmbient", "ColorShift_Top", "ColorShift_Bottom",
                           "EnvironmentDiffuseScale", "EnvironmentSpecularScale", "ExposureCompensation", "GlobalShadows", "ShadowSoftness", "FogColor", "FogStart", "FogEnd", "sunDir": [x,y,z] },
             "atmospheres": [ { "path", "Density", "Offset", "Color", "Decay", "Glare", "Haze" } ],
             "skies": [ { "path", "SkyboxBk", "SkyboxDn", "SkyboxFt", "SkyboxLf", "SkyboxRt", "SkyboxUp", "SunTextureId", "MoonTextureId", "SunAngularSize", "MoonAngularSize", "StarCount", "CelestialBodiesShown" } ],
             "blooms": [ { "path", "Enabled", "Intensity", "Size", "Threshold" } ],
             "colorCorrections": [ { "path", "Enabled", "Brightness", "Contrast", "Saturation", "TintColor" } ],
             "sunRays": [ { "path", "Enabled", "Intensity", "Spread" } ],
             "dofs": [ { "path", "Enabled", "FarIntensity", "FocusDistance", "InFocusRadius", "NearIntensity" } ],
             "blurs": [ { "path", "Enabled", "Size" } ],
             "lightStats": { "total", "shadowed", "keyTotal", "keyUnshadowed", "largeParts", "largePartsNoShadow" },
             "samples": [ { "albedo": [r,g,b] 0-1, "n": [x,y,z], "lit": bool, "indoor": bool, "emissive": bool, "lightE": number } ],
             "marks": { "preset": "obby", "time": "day", "mobile": false } },
  "report": { ...see below... },
  "shots": [ { "path": "visual-qa/r1/desktop-spawn.png", "mean": 0.52, "crushed": 0.01, "blown": 0.03, "w": 1280, "h": 720 } ],      // optional, added by --shots / --shots-from-visual
  "no_world": "reason of >= 10 characters" }                                                                                             // optional: a game with no 3D map
```
Colours in `state` and `config` are `[r, g, b]` 0-255 except `samples[].albedo` (0-1).

## report JSON (`kind: "lighting-report"`, inside the scan)
```
{ "kind": "lighting-report", "version": 1, "genre": "obby" | null, "time": "day", "phase": "day" | "dusk" | "night", "platform": "both",
  "status": "pass" | "fail", "failed": ["L4"], "waived": ["L5"], "skipped": ["L6"], "unverified": ["L5: theme (...)"], "warnings": ["L3: ..."],
  "summary": { "sun_elevation": 52.66, "cost": 6.75, "cost_mobile_variant": 3.75 },
  "checks": { "L1": { "name", "status": "pass" | "fail" | "skip", "measured": { }, "tolerance": { }, "issues": ["..."], "fixes": [ { "action", ... } ], "unverified": [], "warnings": [], "waived": "reason"? }, ... "L12": { } } }
```
`status` is `fail` when any check is `fail` and not waived with a reason of >= 10 characters. A `skip` does not fail the report; the gate fails a skipped L6.

Fix actions (`fixes[].action`): `applyPreset {preset, time, mobile}`, `set {target: "Bloom.Intensity" | "Lighting.ExposureCompensation" | "Atmosphere.Density" ..., value}`, `remove {target: "Atmosphere" | "Bloom" ..., keep}`, `setLights {property, value, filter: "key" | "smallest", keep?}`, `setParts {property: "CastShadow", value, filter: "large"}`, `addInteriorLights {note}` (manual).

## gate record (`gate.json`, `gate-critic.json`)
```
{ "result": "pass" | "fail" | "skipped", "label": "lighting verified (lighting gate passed)" | "playable prototype, lighting not verified",
  "reasons": ["..."], "failing": [ { "check": "L4", "name": "Post effects in sane ranges", "issues": ["Bloom.Intensity 3 above 1: ..."], "fix": "set {\"target\": \"Bloom.Intensity\", \"value\": 0.5}" } ],
  "counts": { "checks": 12, "pass_": 12, "fail": 0, "waived": 0, "skipped": 0, "unverified": 1, "warnings": 1, "samples": 69, "shots": 0 },
  "scorer": "critic", "captured_at": "...", "genre": "obby", "phase": "day", "platform": "both", "summary": { }, "warnings": [], "unverified": [], "scan": "scan-critic.json" }
```
`visual_gate.py` reads `result`; `verdict.py` evaluates the critic's scan itself and does not trust this file.

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
