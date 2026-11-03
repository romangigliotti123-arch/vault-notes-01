---
type: research-source
id: yt-okuDHQyCySk
title: "How to stay on top of Blender's Breaking Changes"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=okuDHQyCySk"
published: "2025-01-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "other"]
---
# yt-okuDHQyCySk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video by Victor Stenov on tracking Blender Python API breaking changes between releases. Notes that release notes list a breaking-changes section in each of the prior four releases (4.0-4.3). Recommends testing add-ons/scripts against daily or experimental builds, and introduces the "Blender Launcher" tool for downloading stable, daily and experimental builds. No Roblox, Claude or MCP content.

## Claims
- c1: [0:00] Blender Python API releases often include breaking changes that can break add-ons and scripts on new releases. *(doc, high; bpy-scripting-headless)*
- c2: [0:41] Release notes for 4.0, 4.1, 4.2 and 4.3 each have a Python API breaking-changes section (as stated by the speaker). *(doc, medium; bpy-scripting-headless)*
- c3: [1:23] Recommended mitigation: install upcoming alpha/beta or daily build and run a feature checklist of your add-on or script against it. *(opinion, medium; bpy-scripting-headless)*
- c4: [2:06] Blender Launcher tool lists installed builds and downloads stable, daily and experimental Blender builds from one UI. *(demo, medium; other)*
- c5: [2:46] Blender Launcher is available for Windows, Linux and Mac; a macOS arm64 build is in the GitHub releases assets. *(doc, medium; other)*
- c6: [3:27] Keep a written checklist of add-on features and how to test each one before testing a new Blender release. *(opinion, medium; bpy-scripting-headless)*

## Numbers
- n1: **Example LTS build downloaded**: 4.2 LTS 

## Techniques
- t1: **Pre-release regression testing**: Install daily or alpha/beta build of the upcoming Blender release. Run a written checklist of each add-on or script feature with a test for each. Use the build for real work to surface issues.

## Quotes (brief, for attribution)
> there's potentially some breaking changes in the python API that you would need to address  (at 0:00, CG Python)

## Points to
- Blender Launcher (GitHub releases, link in video description)
- blender.org experimental and daily builds page
