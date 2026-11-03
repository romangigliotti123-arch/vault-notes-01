---
type: research-source
id: gh-HoldMyBeer-gg-blenderwright-rel-v1.2.2
title: "HoldMyBeer-gg/blenderwright v1.2.2: v1.2.2"
source_type: "github"
creator: "HoldMyBeer-gg"
url: "https://github.com/HoldMyBeer-gg/blenderwright/releases/tag/v1.2.2"
published: "2026-04-19"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# gh-HoldMyBeer-gg-blenderwright-rel-v1.2.2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for HoldMyBeer-gg/blenderwright v1.2.2 (2026-04-19) listing three PRs: version bump to v1.2.1, removal of a PyPI publish workflow, and a fix so the installer's Done button exits instead of reinstalling. Says nothing about Roblox, bpy, MCP tool behavior, or export settings. Links point to a repo named blend-ai, not blenderwright.

## Claims
- c1: blenderwright v1.2.2 is a Blender-related tool with an installer and a PyPI publish workflow (since removed); the release notes do not say it is an MCP server or uses Claude. *(doc, low; claude-blender-ai)*
- c2: Release removed the PyPI publish workflow (PR #10), so the project no longer auto-publishes to PyPI from CI, per this release. *(doc, medium; automation-and-creator-workflows)*
- c3: Installer bug fixed in PR #11: the Done button exited instead of reinstalling. *(doc, high; automation-and-creator-workflows)*
- c4: Release contains only three PR items and a version bump to v1.2.1; no feature or Roblox-specific changes are listed. *(doc, high; other)*
- c5: Release notes name the repo blenderwright, but the changelog and PR links point to HoldMyBeer-gg/blend-ai, suggesting a rename or mismatch. *(doc, medium; other)*

## Numbers
- n1: **version**: v1.2.2 (previous v1.2.1) Release tag date 2026-04-19
- n2: **PRs listed**: 3 (#9, #10, #11) Chore and fix items in this release

## Contradictions flagged
- Repo is named blenderwright (vs Changelog and PR links point to HoldMyBeer-gg/blend-ai)

## Points to
- https://github.com/HoldMyBeer-gg/blend-ai/pull/9
- https://github.com/HoldMyBeer-gg/blend-ai/pull/10
- https://github.com/HoldMyBeer-gg/blend-ai/pull/11
- https://github.com/HoldMyBeer-gg/blend-ai/compare/v1.2.1...v1.2.2
