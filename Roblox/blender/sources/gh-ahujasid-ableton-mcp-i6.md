---
type: research-source
id: gh-ahujasid-ableton-mcp-i6
title: "ahujasid/ableton-mcp#6 I can not see the AbletonMCP as Control Surface"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/ableton-mcp/issues/6"
published: "2025-03-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# gh-ahujasid-ableton-mcp-i6

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #6 on ahujasid/ableton-mcp (Mar 2025): users cannot see AbletonMCP in Ableton Live's Control Surface dropdown. Causes found in thread: wrong __init__.py copied (from MCP_Server instead of AbletonMCP_Remote_Script), HTML saved instead of raw file, wrong install folder. Working fix: place folder under Live's MIDI Remote Scripts dir. Ableton 10 needs Python 2.7-compatible script. Not Blender-related.

## Claims
- c1: The ableton-mcp project is an Ableton Live MCP bridge, not a Blender MCP; issue concerns Live Control Surface setup only. *(doc, high; claude-blender-ai)*
- c2: Common install failure: saving GitHub page HTML as __init__.py produces HTML contents; use the RAW file instead. *(experience, high; automation-and-creator-workflows)*
- c3: Copying __init__.py from MCP_Server instead of AbletonMCP_Remote_Script caused the server to fail. *(experience, high; automation-and-creator-workflows)*
- c4: Script placed in MIDI Remote Scripts folder under Live install dir showed as selectable control surface and Live listened on port 9877 for one user. *(experience, medium; automation-and-creator-workflows)*
- c5: Ableton 10 requires Python 2.7-compatible script (commenter's opinion/workaround), not Python 3. *(opinion, low; other)*

## Numbers
- n1: **TCP port**: 9877 

## Techniques
- t1: **Install remote script to MIDI Remote Scripts**: Create AbletonMCP folder with __init__.py under Live's Resources/MIDI Remote Scripts (not User Remote Scripts in AppData), restart Live, select AbletonMCP in Control Surface dropdown.
- t2: **Download raw file**: Use GitHub Raw view to save __init__.py; right-click save of rendered page yields HTML.

## Quotes (brief, for attribution)
> I downloaded the html of the __ini.py by right clicking it on the Github page and saving. It named it __ini.py but the contents were HTML.  (ahujasid)

## Contradictions flagged
- Placing folder in User Remote Scripts (AppData) is the expected location (vs CsRic and dancohen81 report success only with Resources/MIDI Remote Scripts)

## Points to
- https://github.com/ahujasid/ableton-mcp/issues/6
