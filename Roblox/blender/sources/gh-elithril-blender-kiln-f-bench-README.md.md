---
type: research-source
id: gh-elithril-blender-kiln-f-bench-README.md
title: "elithril/blender-kiln/bench/README.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/bench/README.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0041
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "open-cloud-automation", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-f-bench-README.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for a quality bench that measures an end-to-end Claude /kiln Blender skill on six fixed briefs, one per pipeline path. It re-imports the shipped GLB and checks tris, topology, dimensions, textures, rigs and deformation, logs session cost, and publishes results. A measurement harness, not a Roblox guide.

## Claims
- c1: Every Blender call in the bench passes --python-exit-code 1 because Blender exits 0 when a Python script raises. *(doc, high; bpy-scripting-headless)*
- c2: glTF importer keeps vertices split at every UV and normal seam; a closed barrel showed 4,112 boundary edges, so topology is judged after welding coincident points. *(doc, high; common-mistakes-fixes)*
- c3: glTF importer adds an Icosphere object as bone display shape; counting it as geometry put an arm standing at z = -1.0. *(doc, high; common-mistakes-fixes)*
- c4: glTF exporter binds unweighted vertices to a synthetic neutral_bone so the file still validates; a vertex driven only by that bone counts as unweighted. *(doc, high; rigging-animation)*
- c5: glTF exporter drops loose edges by default, so a shipped GLB cannot contain one. *(doc, high; common-mistakes-fixes)*
- c6: Deformation probe bends every deform bone 25 degrees and measures edge stretch (stretch_p99, stretch_max) to catch rigs that validate but deform badly. *(doc, medium; rigging-animation)*
- c7: Material check records images and max px of textures surviving export, plus empty_material_slots, to detect silent texture loss. *(doc, medium; texturing-baking-uv)*
- c8: Pinned setup: blender-mcp 2.0.0 with bundled addon 1.7, installed into a throwaway Blender profile; Blender version is whatever the machine has. *(doc, high; claude-blender-mcp)*
- c9: Session runs in auto mode with bypassPermissions and no user settings, so a human never answers the skill's prompt-before-destroy rule. *(doc, high; claude-blender-mcp)*
- c10: gradio_client uses the locally saved Hugging Face token by default, so Space calls count against a free logged-in account's ZeroGPU quota (3.5 min/day). *(doc, high; open-cloud-automation)*
- c11: Text-to-3D generation runs through Hugging Face Spaces via gradio_client; generation backend is one variable the bench is meant to compare. *(doc, medium; procedural-generation)*
- c12: Publish step copies proof files to a bench-results git worktree (about 0.5-1 MB per label), listing GLBs over 1 MB by size and sha256 instead of including them; export fails if a username or e-mail survives. *(doc, high; creator-workflows)*
- c13: Published labels are immutable records; a new run must use a new label instead of republishing over an old one. *(doc, high; creator-workflows)*
- c14: Author's view: one run per brief is not deterministic enough, so a single difference between two labels is a lead, not a verdict. *(opinion, high; creator-workflows)*
- c15: Session cost is taken as CLI equivalent-API cost, which is not billed on subscription but is the only comparable quota measure. *(doc, medium; bpy-scripting-headless)*

## Numbers
- n1: **briefs**: 6 fixed, one per pipeline path 
- n2: **seeded instrument tests**: 10/10 expected 
- n3: **boundary edges on unwelded closed barrel**: 4,112 
- n4: **arm z position from Icosphere bug**: -1.0 m 
- n5: **deform bone bend for probe**: 25 degrees 
- n6: **ZeroGPU free quota per day**: 3.5 min 
- n7: **published size per label**: about 0.5-1 MB 
- n8: **GLB size threshold for publishing file**: under 1 MB 
- n9: **blender-mcp version / addon**: 2.0.0 / addon 1.7 
- n10: **bench runs size, git-ignored**: hundreds of MB 

## Techniques
- t1: **Fail-loud Blender runs**: Pass --python-exit-code 1 to every Blender call so script exceptions give nonzero exit. Explicit sys.exit(1) also propagates.
- t2: **Weld before topology check**: After glTF import, weld coincident vertices across UV/normal seams, then count non_manifold, boundary and degenerate edges.
- t3: **Deformation probe**: Bend each deform bone 25 degrees, measure edge stretch p99 and max to detect rigs that validate but deform badly.
- t4: **Measure the file, not the log**: Re-import the exported GLB and measure it, since the production log is written by the session under judgement.

### Code: Run the instrument self-test and the six-brief bench under a label
```bash
python3 bench/test_measure.py          # the instrument first: seeded defects, 10/10 expected
python3 bench/run.py baseline          # all six briefs
python3 bench/run.py lot2 ai-mushrooms # one brief under a new label
```

### Code: Create the bench-results worktree once, then publish a label
```bash
git worktree add bench/results bench-results
python3 bench/publish.py <label>
```

## Quotes (brief, for attribution)
> Nothing proved the skill: no end-to-end session driven by /kiln had ever been measured.  (elithril)
> Blender exits 0 when a Python script raises, unless given --python-exit-code 1.  (elithril)
> A published label is a record: never republish it over a different run — measure under a new label instead.  (elithril)

## Contradictions flagged
- Blender reports success (exit 0) even when a bpy script raises an exception. (vs Common assumption that a failed Blender script yields a failing exit code)
- A GLB that validates can still have unweighted vertices, because the exporter reassigns them to neutral_bone. (vs Assumption that a validating GLB has no unweighted vertices)

## Points to
- elithril/blender-kiln
- blender-mcp 2.0.0
- gradio_client
- Hugging Face ZeroGPU
- bench-results branch
- references/characters.md
