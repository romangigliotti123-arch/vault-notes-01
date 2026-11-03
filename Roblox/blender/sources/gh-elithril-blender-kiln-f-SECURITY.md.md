---
type: research-source
id: gh-elithril-blender-kiln-f-SECURITY.md
title: "elithril/blender-kiln/SECURITY.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/SECURITY.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 2
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "open-cloud-automation"]
---
# gh-elithril-blender-kiln-f-SECURITY.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
SECURITY.md of elithril/blender-kiln, a documentation-and-prompt skill for Claude Code (no service, no binary). Covers the security surface: execute_blender_code runs arbitrary Python in Blender with user privileges; pipeline downloads from PolyHaven and Sketchfab; tools/ scripts run in CI and locally. Gives reporting process and scope exclusions. Marginal relevance to Roblox pipeline.

## Claims
- c1: execute_blender_code runs arbitrary Python inside Blender; anything the skill tells a model to execute runs with the user's privileges. *(doc, high; claude-blender-mcp)*
- c2: Blender-side code execution from generated code is intended behaviour, not a vulnerability, per the project's own scope note. *(doc, high; claude-blender-mcp)*
- c3: The pipeline downloads assets from PolyHaven and Sketchfab and can fetch generation results from remote services. *(doc, high; bpy-scripting-headless)*
- c4: Marketplace/downloaded assets should be treated as untrusted; verify licences and geometry before shipping. Project logs record licences for this reason (iron rule 17). *(doc, high; creator-workflows)*
- c5: tools/ scripts run in CI and locally, so they form part of the security surface. *(doc, medium; open-cloud-automation)*

## Numbers
- n1: **iron rule referenced**: 17 (licence logging) 

## Techniques
- t1: **Security advisory reporting**: Report via GitHub security advisory, not a public issue. Include version/commit, Blender version, and smallest reproducing input. Describe the class of problem and affected path; omit working exploits in initial report.

## Quotes (brief, for attribution)
> execute_blender_code runs arbitrary Python inside Blender. Anything the skill tells a model to execute runs with your user's privileges.  (elithril)

## Points to
- https://github.com/elithril/blender-kiln/security/advisories/new
- PolyHaven
- Sketchfab
