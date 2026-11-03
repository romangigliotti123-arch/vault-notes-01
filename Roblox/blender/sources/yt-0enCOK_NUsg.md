---
type: research-source
id: yt-0enCOK_NUsg
title: "Blender Python Tutorial : Why is it not Working? : Episode 1 [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=0enCOK_NUsg"
published: "2020-12-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes"]
---
# yt-0enCOK_NUsg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner video fixing a Blender bpy script copied from a tutorial (node editor / node group creation). Fixes: add missing keyword argument (text=), correct an AttributeError spelling mistake, replace parentheses with square brackets. Advises reading the Info window for error line numbers. No Roblox, Claude, MCP, or export content.

## Claims
- c1: [0:42] Blender's Info window shows the Python error and line number after running a script; use it to locate the failing line. *(demo, high; bpy-scripting-headless)*
- c2: [1:23] A missing keyword argument (e.g. text=) in a bpy call raises an error; fix by adding 'name=' style keyword and value. *(demo, high; common-mistakes-fixes)*
- c3: [1:55] An AttributeError on a bpy call was caused by a simple spelling mistake in the attribute name. *(demo, high; common-mistakes-fixes)*
- c4: [2:04] Wrong bracket type (parentheses instead of square brackets) caused a error on a line that otherwise looked correct; the reported line number was not the true cause. *(demo, medium; common-mistakes-fixes)*
- c5: [2:44] Presenter's opinion: most script problems are spelling mistakes, wrong symbols, or small typos. *(opinion, medium; common-mistakes-fixes)*

## Numbers
- n1: **Error sources fixed**: 3 (missing keyword arg, attribute spelling, brackets) Script ran in Blender scripting workspace; fixes made iteratively

## Techniques
- t1: **Read Info window for errors**: Run script in Blender scripting workspace, scroll Info editor to see traceback; it points to the offending line. Fix, rerun, repeat until the button/node group appears.

## Contradictions flagged
- Reported error line (63) was itself correct; the real problem was on a different line. (vs Interpreter error line numbers taken at face value)
