---
type: research-source
id: yt-yiMGxlRv8h4
title: "Supercharging Blender's Drivers with Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=yiMGxlRv8h4"
published: "2023-06-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes", "other", "procedural-generation"]
---
# yt-yiMGxlRv8h4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender drivers tutorial (Python, no Roblox or Claude content). Shows registering Python functions in bpy.app.driver_namespace so driver expressions can call them. Demonstrates a rotation driver, printing values to the system console, and a noise-based bobbing driver on an icosphere driven by a Follow Path empty. Mostly off-topic for the Roblox/Claude pipeline.

## Claims
- c1: [1:40] Python functions are registered with Blender's driver namespace so a driver expression can call them by the registered name, which can differ from the function name. *(demo, high; bpy-scripting-headless)*
- c2: [2:39] A driver that references a registered function fails until the script has been run; running the script registers it, after which the driver works. *(demo, medium; bpy-scripting-headless)*
- c3: [3:21] Changing the registered function's logic requires re-running the script; the driver then picks up the new value after Update Dependencies. *(demo, medium; bpy-scripting-headless)*
- c4: [4:42] print() output from a driver function appears in the system console; on Windows it is enabled via Window > Toggle System Console. *(demo, medium; bpy-scripting-headless)*
- c5: [6:38] An empty with a Follow Path constraint on a circle curve with Animate Path, with matching 360-frame ranges, gives a seamless loop. *(demo, medium; other)*
- c6: [9:47] mathutils.noise.noise sampled at the object's world-location Vector gives a smooth driver value; on a closed circular path the motion loops seamlessly. *(demo, medium; procedural-generation)*
- c7: [11:08] Scaling the noise driver output by 0.1 reduces motion to a gentle bob; the unscaled version was extreme. *(demo, medium; procedural-generation)*
- c8: [13:54] Passing the raw world location instead of the computed offset location into the noise function caused an error and unexpected behaviour; fixed by using the computed vector. *(demo, medium; common-mistakes-fixes)*
- c9: [14:34] Two ways to pass per-axis values: an optional axis-name argument checked with if statements, or three separate registered functions (custom_driver_a/b/c) with no extra arguments; both gave the same result. *(demo, medium; bpy-scripting-headless)*

## Numbers
- n1: **driver multiplier for rotation speed**: 2 (icosphere spins twice as fast as empty) 
- n2: **animation frame range for path**: 360 frames (start/end and curve path frames) 
- n3: **noise driver scale factor**: 0.1 
- n4: **print rounding**: round(value, 3) 

## Techniques
- t1: **Register driver function in driver_namespace**: import bpy; define function; bpy.app.driver_namespace['name'] = function; run script once. Then use name(var) in the driver expression field and Update Dependencies.
- t2: **Noise driver from world location**: Create driver variables for empty X/Y/Z location; in the function build mathutils.Vector from them, sample mathutils.noise.noise(vector), and return the value as the driver output; multiply by a small factor.
- t3: **Per-axis helper functions**: Write a shared helper taking a base offset vector; wrap in custom_driver_a/b/c with different base vectors; register each and reference in X/Y/Z driver expressions.

## Points to
- Windows system console setup (Window > Toggle System Console)
- Mac/Linux console setup videos (referenced, not linked in transcript)
