---
type: research-source
id: gh-elithril-blender-kiln-rel-v1.1.2
title: "elithril/blender-kiln v1.1.2: v1.1.2 — the README contradicted itself about Blender"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v1.1.2"
published: "2026-08-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "common-mistakes-fixes", "other"]
---
# gh-elithril-blender-kiln-rel-v1.1.2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release note for elithril/blender-kiln v1.1.2 (a Blender plugin repo, not Roblox-specific). It corrects the README's Blender version floor to 4.4, based on the layered-actions API used for animation F-curves, and adds a checker harness and a manifest version-consistency check. Little direct Roblox pipeline content.

## Claims
- c1: Stated real Blender floor is 4.4 because animation code reaches F-curves via action.layers[].strips[].channelbag(), which arrived with layered actions in 4.4. *(doc, high; bpy-scripting-headless)*
- c2: Tested only on Blender 5.0 (local) and 5.2.1 LTS (CI); 4.4–4.5 are API-compatible per author but untested, so labelled 'unverified', not 'supported'. *(doc, high; bpy-scripting-headless)*
- c3: README had contradictory version claims (badge 'Blender 4.x+' vs. 'Needs Blender 5.x'); neither was measured on 4.x. *(doc, high; bpy-scripting-headless)*
- c4: A regex checker matching every 'Blender N.N' flagged historical notes (false positive); blacklisting history phrasings then made it pass with no findings; final version whitelists requirement phrasings and fails when none are found. *(experience, medium; common-mistakes-fixes)*
- c5: Test harness now has 18 cases: 15 seeded regressions that must fire and 3 must-stay-silent cases; previously 14 cases only tested firing. Author reports five false positives had shipped. *(data, high; other)*
- c6: plugin.json and marketplace.json both hold the version and are hand-edited; a check now verifies they match, and the version lives in metadata.version in marketplace.json. *(experience, medium; other)*
- c7: Author's view: a check people learn to ignore is worse than no check. *(opinion, medium; other)*

## Numbers
- n1: **Minimum supported Blender version**: 4.4 Layered actions API (channelbag) first available in 4.4; 4.4–4.5 untested
- n2: **Blender versions verified**: 5.0 (local), 5.2.1 LTS (CI) Only versions actually run by the author
- n3: **Checker harness cases**: 18 (15 seeded regressions, 3 must-stay-silent) Up from 14 cases that only asserted firing
- n4: **False positives shipped in checkers**: 5 Motivated adding expect=None silence tests

## Techniques
- t1: **Version-floor verification via API feature**: Identify the Blender release that introduced the API used (layered actions, 4.4), then label versions by what was actually run; mark untested versions as unverified.
- t2: **Negative-control tests for doc checkers**: Add must-stay-silent cases alongside seeded-failure cases so a lint check cannot pass by finding nothing or fire on correct text.

## Quotes (brief, for attribution)
> 4.4–4.5 satisfy the API but are untested, so the README now calls them unverified rather than supported  (elithril)

## Contradictions flagged
- README badge said Blender 4.x+ while the Reproduce section said Needs Blender 5.x (vs Itself (internal README contradiction, resolved in v1.1.2))

## Points to
- https://github.com/elithril/blender-kiln/releases/tag/v1.1.2
