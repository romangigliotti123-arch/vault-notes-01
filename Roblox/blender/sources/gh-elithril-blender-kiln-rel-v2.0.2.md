---
type: research-source
id: gh-elithril-blender-kiln-rel-v2.0.2
title: "elithril/blender-kiln v2.0.2: blender-kiln 2.0.2 — a lighter install"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/releases/tag/v2.0.2"
published: "2026-10-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 1
density: low
tags: ["research-source", "github", "other"]
---
# gh-elithril-blender-kiln-rel-v2.0.2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release note for elithril/blender-kiln v2.0.2, a Claude Code plugin/skill around Blender. Reduces install download from about 46 MB to about 9 MB by shipping the plugin from plugin/ (316 KB) and moving benchmark results to a separate bench-results branch. No change to skill behaviour. Little direct Roblox or bpy content.

## Claims
- c1: Install of kiln 2.0.2 downloads about 9 MB, down from 46 MB in 2.0.1, measured in a clean Claude Code profile. *(data, high; other)*
- c2: In 2.0.1 the install held the whole repo twice: a 30 MB marketplace clone plus a 16 MB plugin copy, mostly benchmark results. *(data, high; other)*
- c3: Plugin now ships from plugin/ (316 KB: SKILL.md, references/, tools/, licence); marketplace source points there. *(doc, high; other)*
- c4: Benchmark results moved to the bench-results branch with history kept; docs/benchmarks.md links there. *(doc, high; other)*
- c5: Standalone clone uses root symlinks; on Windows, enable core.symlinks in git or install as a plugin. *(doc, high; other)*
- c6: Upgrade from 2.0.1 to 2.0.2 via the /plugin menu was tested; same two install commands as before. *(experience, medium; other)*
- c7: Contributor checks now run as python3 plugin/tools/verify_docs.py (path moved under plugin/). *(doc, high; other)*

## Numbers
- n1: **install download size**: 46 MB -> ~9 MB kiln 2.0.1 vs 2.0.2 in clean Claude Code profile
- n2: **marketplace clone size (2.0.1)**: 30 MB whole repo cloned, mostly benchmark results
- n3: **plugin copy size (2.0.1)**: 16 MB duplicate of repo in plugin install
- n4: **plugin/ directory size (2.0.2)**: 316 KB SKILL.md, references/, tools/, licence

## Techniques
- t1: **Ship plugin from subdirectory**: Keep the installable plugin in plugin/ and point the marketplace source there; move bulky benchmark data to an orphan-style branch to shrink clone and install size.
- t2: **Root symlinks for standalone clone**: Repo root symlinks into plugin/ so standalone clones work; on Windows enable git core.symlinks or install as plugin instead.

## Quotes (brief, for attribution)
> Installing kiln now downloads about 9 MB instead of 46 MB.  (elithril)

## Points to
- https://github.com/elithril/blender-kiln/releases/tag/v2.0.2
- https://github.com/elithril/blender-kiln/tree/bench-results
- https://github.com/elithril/blender-kiln/blob/v2.0.2/docs/benchmarks.md
- https://github.com/elithril/blender-kiln/compare/v2.0.1...v2.0.2
