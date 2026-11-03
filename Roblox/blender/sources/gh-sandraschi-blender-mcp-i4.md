---
type: research-source
id: gh-sandraschi-blender-mcp-i4
title: "sandraschi/blender-mcp#4 Just some thoughts"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/issues/4"
published: "2026-07-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# gh-sandraschi-blender-mcp-i4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on sandraschi/blender-mcp about install-doc friction. Reporter says the bridge addon .py was hidden under docs/ and prerequisites were front-loaded. Maintainer's reply says fixes shipped: addon is a first-class download (addon/blender_bridge_addon.py, attached to v0.11.1), download links sit atop README/INSTALL, and headless mode is the default. No Roblox export or asset-pipeline content.

## Claims
- c1: blender-mcp headless mode is the default; the bridge addon is only needed for a live Blender viewport while the agent works. *(doc, high; claude-blender-ai)*
- c2: Bridge addon lives at addon/blender_bridge_addon.py and is attached to the v0.11.1 release assets (maintainer reply, verified 2026-10-09). *(doc, high; claude-blender-ai)*
- c3: Install path is two downloads (.mcpb and the Blender addon) plus one prompt, documented in docs/ONBOARDING.md, with a 6-step quickstart in README and INSTALL. *(doc, high; automation-and-creator-workflows)*
- c4: Reporter's opinion: burying the addon in docs and front-loading prerequisites raised the barrier to install. *(opinion, medium; automation-and-creator-workflows)*
- c5: Issue contains no Roblox Studio, FBX/glTF export, MeshPart, or Roblox pipeline details. *(data, high; other)*

## Numbers
- n1: **release version**: v0.11.1 release where bridge addon is attached as asset
- n2: **quickstart steps**: 6 quickstart right after download links in README and INSTALL

## Quotes (brief, for attribution)
> the bridge addon is only required if you want a live Blender viewport while the agent works. Most tools run headless  (sandraschi)

## Points to
- https://github.com/sandraschi/blender-mcp/issues/4
- addon/blender_bridge_addon.py
- docs/ONBOARDING.md
