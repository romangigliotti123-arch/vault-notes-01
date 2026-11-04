<!-- cold: rbx-placement/report-shape.md | read when: read only to see the full JSON shape of a per-model report or a scan file. -->

## From skills/rbx-placement/references/api.md :: Report (per model)

```json
{"path": "Workspace.Map.House.Door", "class": "Model", "kind": "door", "status": "fail", "failed": ["P4"], "waived": [], "unverified": ["P5:map bounds"],
 "intent": {"kind": "door", "face": {"target": [10, 3.5, 20]}}, "intentSource": "argument", "datamodel": "Edit", "at": "2026-11-04T10:00:00Z",
 "fixesApplied": [{"action": "snapToGround", "dy": -0.3}], "passes": 2,
 "checks": {"P1": {"status": "pass", "measured": {"size": [4, 7, 0.5]}, "tolerance": {"originRadius": 0.5}, "issues": [], "fixes": []},
            "P4": {"status": "fail", "measured": {"facingOffDeg": 180, "yawDeg": 0}, "tolerance": {"faceTolDeg": 15}, "issues": ["front faces 180.0 deg away from the target (tolerance 15)"],
                   "fixes": [{"action": "rotateYaw", "deltaDeg": 180}]}}}
```
Scan: `{"kind": "placement-scan", "version": 1, "game", "scorer", "datamodel", "captured_at", "root", "models_total", "summary": {pass, fail, waived}, "skipped": [{path, reason}], "fingerprint", "models": [...]}`.
