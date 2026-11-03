---
type: research-source
id: yt-WQ6SPNt0Dpg
title: "An Automated Pipeline for Construction 4D Reporting — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=WQ6SPNt0Dpg"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-WQ6SPNt0Dpg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Construction talk (BCON26) on an automated Blender 4D reporting pipeline for a UK nuclear build (Hinkley Point C, then Sizewell C). Uses Blender in background mode running Python plus Bonsai/IFC, schedule CSVs, and PowerPoint export. Not about Roblox, blender-mcp, Claude, or Roblox export. Relevance to the topic is minimal.

## Claims
- c1: [3:57] Blender run in background mode (blender -b style) executes Python 4D logic, reading config, CSV schedules and IFC model, then exports images. *(demo, medium; claude-blender-ai)*
- c2: [12:47] Standardized the tool across 17 planner laptops with pinned Blender and Python versions and GitHub-based version control; over 3,300 runs logged since October, about four per day. *(data, medium; automation-and-creator-workflows)*
- c3: [17:17] Speaker's opinion: Blender runs Python on modest hardware, easy to deploy, and fits the need better than heavy 4D software. *(opinion, medium; automation-and-creator-workflows)*
- c4: [17:58] Model and schedule must match precisely or automation only automates mistakes; IFC files are manipulated with Python and IfcOpenShell (via Bonsai) to fix common model problems before 4D runs. *(experience, medium; other)*
- c5: [17:58] Multiprocessing of Blender for repeated buildings cut work that took two days to minutes. *(data, low; automation-and-creator-workflows)*
- c6: [13:51] Version 2 stores the Blender file as an output and keeps the schedule inside Blender, allowing day/week/month/year switching by dynamic aggregation without regenerating. *(demo, medium; other)*
- c7: [8:11] Blender built-in edges and ambient occlusion/shadows replaced SketchUp/DWG wireframe workarounds for contour lines between construction joints. *(experience, medium; other)*

## Numbers
- n1: **Blender 2.8 release year**: 2019 
- n2: **Switch to Blender for 4D**: 2023, from monthly to weekly reporting 
- n3: **Laptops deployed**: 17 
- n4: **Locked runs**: more than 3,300 (~4 per day) 
- n5: **Project scale**: 50 buildings, 55 tower cranes, 25 planners, 400 concrete models, 7,200 rooms, 35,000 concrete parts 
- n6: **Time saved on repeated buildings**: two days of work reduced to minutes 
- n7: **Version 1 build time**: one week 

## Techniques
- t1: **Headless Blender 4D batch**: Run Blender in background mode with a Python script. Read a config file and per-building CSVs converted from schedule exports. Join with IFC geometry, export images, and assemble a PowerPoint.
- t2: **Runtime pinning and tracing**: Ship one tool version to every laptop, pinning Blender and Python versions and libraries. Log input files, parameters, machine, user and process ID to replicate runs when debugging.
- t3: **On-the-fly time aggregation**: Group active tasks by day, week, month or year at animation time instead of pre-rendering each timestep.

## Points to
- Bonsai (IFC add-on for Blender)
- IfcOpenShell
- IFC (Industry Foundation Classes)
- Blender 2.8
- SketchUp
- Primavera-style schedule export (XER/XML, named only as PX program)
