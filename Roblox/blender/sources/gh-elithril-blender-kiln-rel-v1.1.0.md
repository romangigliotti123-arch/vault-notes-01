---
type: research-source
id: gh-elithril-blender-kiln-rel-v1.1.0
title: "elithril/blender-kiln v1.1.0: v1.1.0 — audited against a live Blender"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v1.1.0"
published: "2026-08-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "open-cloud-automation", "procedural-generation", "rigging-animation", "roblox-export-settings", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-rel-v1.1.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for blender-kiln v1.1.0, a Claude plugin pipeline for Blender assets. Covers bugs found by running phases live (SOURCE addon integrations off by default, batch runner clearing integration flags, texture map loss, geometry-nodes exports missing modifier results, PEP 668 pip failures, over-dense rigs), a rig-selection phase by vertex count, pose conversion on import, 31 iron rules, and CI checks. Mostly a changelog; little on Roblox-specific import/export.

## Claims
- c1: SOURCE phase fails on default install: all four addon integrations ship off, so addon does not register commands; search returns 'Unknown command type: search_polyhaven_assets', misleading as version mismatch. *(doc, high; claude-blender-mcp)*
- c2: Sketchfab API-key setup step is needed for SOURCE phase and is surfaced only by the status tools. *(doc, medium; claude-blender-mcp)*
- c3: Batch runner scene-clear via read_homefile(use_empty=True) reset addon integration flags stored as scene properties; asset 1 succeeded and all later assets failed silently. *(doc, high; bpy-scripting-headless)*
- c4: Texturing dropped 4 of 7 downloaded maps: AO dropped despite glTF occlusionTexture slot; displacement has no slot; compatibility table covered only BSDF properties. *(doc, high; texturing-baking-uv)*
- c5: Geometry-nodes exports produced 2 triangles instead of 2,688 because output exists only as modifier result and export_apply=False writes base mesh. *(doc, high; common-mistakes-fixes)*
- c6: All six pip install commands failed on PEP 668 Pythons (Homebrew, most Linux distros). *(doc, high; common-mistakes-fixes)*
- c7: Rigging picked a rig 12x too dense: 370-vertex figure on Rigify human left 107 of 160 deform bones influencing nothing and detached head from neck. *(data, high; rigging-animation)*
- c8: Rig tiers measured on Blender 5.0.1: hand-built below 700 vertices, basic_human (35 deform bones) to 3,000 vertices, full human (160 bones) above; Rigify human worth it at ~3,200 vertices. *(data, high; rigging-animation)*
- c9: No free library ships a T-posed humanoid; measured rest poses were -26.8, -28.2 and -70.8 degrees, so conversion to T-pose is the documented path. *(data, medium; rigging-animation)*
- c10: Skill reimplemented capabilities its dependency already ships: local ~25GB Hunyuan3D install replaced by native addon command; hand-built node graph replaced by set_texture; external USDZ tools replaced by native Blender USDZ export. *(opinion, medium; claude-blender-mcp)*
- c11: Author's stated lesson: documentation written by looking at ecosystem instead of at the dependency causes errors; project rule is claims must be measured, not reasoned. *(opinion, medium; creator-workflows)*
- c12: Fifteen reference assets across three themes, reproducible via run_gallery.sh: 21,879 triangles, 1,456 kB reduced to 133 kB after dedup/weld/Draco. *(data, high; procedural-generation)*
- c13: CI: verify.yml runs ten text checks per push and a 12/12 regression suite; blender.yml re-checks nine Blender-dependent findings weekly and fails on Blender deprecations such as Material.use_nodes. *(doc, medium; open-cloud-automation)*
- c14: Blender deprecation Material.use_nodes was caught by blender.yml on first run. *(data, high; common-mistakes-fixes)*
- c15: Release notes contain no Roblox-specific scale, axis, or import settings; Roblox is not the focus of this source. *(doc, high; roblox-export-settings)*

## Numbers
- n1: **triangles in geometry-nodes export**: 2 of 2,688 Modifier-only output lost when export_apply=False
- n2: **texture maps kept**: 3 of 7 AO dropped; displacement has no slot
- n3: **deform bones unused on wrong rig**: 107 of 160 370-vertex figure on Rigify human
- n4: **rig over-density factor**: 12x Rig chosen too dense for mesh
- n5: **hand-built rig threshold**: <700 vertices Blender 5.0.1 tiers
- n6: **basic_human deform bones**: 35 bones up to 3,000 vertices Blender 5.0.1 tiers
- n7: **full human deform bones**: 160 bones above 3,000 vertices Blender 5.0.1 tiers
- n8: **Rigify human worth-it vertex count**: ~3,200 Stated threshold
- n9: **measured rest-pose angles of free humanoids**: -26.8, -28.2, -70.8 degrees Three free T-posed library checks
- n10: **reference asset triangles**: 21,879 Fifteen reference assets, three themes
- n11: **reference asset size**: 1,456 kB to 133 kB After dedup/weld/Draco
- n12: **pip commands failing on PEP 668**: 6 of 6 All pip install commands on PEP 668 Python
- n13: **local Hunyuan3D install size**: ~25 GB Replaced by addon-native command
- n14: **iron rules**: 31 (up from 26) v1.1.0 pipeline rules
- n15: **verify.yml text checks**: 10 per push Plus 12/12 seeded regression suite
- n16: **bugs found by running pipeline**: 15 Found only when phases were executed

## Techniques
- t1: **Vertex-count rig selection**: Measure mesh vertex count, route to hand-built rig below 700, basic_human (35 bones) up to 3,000, full 160-bone human above. Avoid Rigify human below ~3,200 vertices.
- t2: **Batch scene reset without losing addon flags**: Do not use read_homefile(use_empty=True) between assets when addon integration flags are scene properties; they get wiped. Re-enable or preserve them after reset.
- t3: **Use set_texture for multi-map materials**: Use the addon's set_texture command rather than hand-building node graphs; it produces 16 nodes covering seven maps in the author's test.
- t4: **Apply modifiers before export for geometry nodes**: Geometry-nodes output exists only as modifier result; export with modifiers applied, otherwise base mesh (2 tris) is written.
- t5: **Use venv or pipx for pip on PEP 668 Python**: System Python rejects pip install under PEP 668; create a virtual environment before installing dependencies.
- t6: **Check status tools for addon setup**: Run addon status tools to find disabled integrations and required API keys (e.g., Sketchfab) before running SOURCE phase.
- t7: **Regression check of checker itself**: Seed each known regression into the docs and assert the checker flags it (12/12 in verify.yml); run Blender-dependent checks on a weekly schedule to catch deprecations.

### Code: Plugin install commands from release notes
```text
/plugin marketplace add elithril/blender-kiln
/plugin install blender-kiln@blender-kiln

Then `/kiln setup`.
```

## Quotes (brief, for attribution)
> claims must be measured, not reasoned  (elithril)
> Each time the documentation had been written by looking at the ecosystem instead of at the dependency.  (elithril)

## Contradictions flagged
- Texturing via glTF keeps all seven downloaded maps (vs Release notes: AO dropped and displacement has no slot, so only 3 of 7 kept)
- Batch runner clears scene between assets safely (vs Release notes: read_homefile(use_empty=True) disabled integrations after asset 1, silently failing later assets)

## Points to
- https://github.com/elithril/blender-kiln
- https://github.com/elithril/blender-kiln/blob/main/CHANGELOG.md
- https://github.com/elithril/blender-kiln/blob/main/CONTRIBUTING.md
- Blender 5.0.1
- Rigify
- Hunyuan3D
- Polyhaven addon
- Sketchfab addon
- Draco
