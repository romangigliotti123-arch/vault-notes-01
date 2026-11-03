---
type: research-source
id: yt-RZUExdcP1q0
title: "Blender Python Tutorial: Application Timers [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=RZUExdcP1q0"
published: "2021-02-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-RZUExdcP1q0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial on bpy.app.timers. Shows registering a function to run once after a delay (first_interval) and a repeating timer that returns a float to reschedule and returns None to stop. Demo adds cubes to the scene via the Scripting workspace and Window > Toggle System Console. No Roblox, Claude, or blender-mcp content.

## Claims
- c1: [2:07] bpy.app.timers.register(func, first_interval=5) runs a function once after 5 seconds, e.g. adding a cube to the scene. *(demo, high; claude-blender-ai)*
- c2: [2:52] A timer function returning None unregisters itself; returning a float reschedules it after that many seconds. *(demo, high; claude-blender-ai)*
- c3: [3:33] Timer callbacks that modify module-level globals must declare 'global counter' inside the function before changing it. *(demo, high; claude-blender-ai)*
- c4: [4:58] Repeating timer demo: a cube is added every 0.5 s, moved 2 units on Y each tick, and the timer stops after 10 runs. *(demo, high; claude-blender-ai)*
- c5: [4:16] Narration says the timer returns 1 (one-second interval) while counter < 10, yet the final run is described as every half second; the code and narration are inconsistent. *(demo, medium; claude-blender-ai)*

## Numbers
- n1: **one-shot timer delay**: 5 s first_interval for a single delayed call
- n2: **repeat count**: 10 counter stops timer when equal to 10
- n3: **repeat interval**: 0.5 s stated as achievable by returning a float; demo runs every half second
- n4: **Y offset per tick**: 2 location variable increased per cube

## Techniques
- t1: **One-shot delayed call via bpy.app.timers**: Define a function with no args, then call bpy.app.timers.register(func, first_interval=N). Function runs once after N seconds in Blender's main loop.
- t2: **Repeating timer with stop condition**: Use a global counter; each call increments it and does work; return a float interval to repeat, or None when counter reaches the limit.
- t3: **Debug via system console**: Enable Window > Toggle System Console and print() values to check timer progress.

### Code: Reconstructed from narration: one-shot delayed call (spoken code, not verbatim source)
```python
import bpy

def _5_seconds():
    bpy.ops.mesh.primitive_cube_add()

bpy.app.timers.register(_5_seconds, first_interval=5)
```

### Code: Reconstructed from narration: repeating timer with global counter and stop condition
```python
import bpy

counter = 0
location = 0

def run_10_times():
    global counter
    global location
    bpy.ops.mesh.primitive_cube_add(location=(0, location, 0))
    counter += 1
    print(counter)
    if counter == 10:
        return None
    return 0.5

bpy.app.timers.register(run_10_times)
```

## Quotes (brief, for attribution)
> we should see a cube now appear we can also see the message in the system console  (at 2:07, Darkfall)
> if counter is equal to 10 then add a colon then we want to return none  (at 4:16, Darkfall)

## Contradictions flagged
- Timer returns 1 (1-second interval) when counter < 10 (vs Same video says the cube is added every half second in the final demo)

## Points to
- Official Blender bpy timers documentation (linked by the author, not included in transcript)
- Darkfall blog post (referenced, not named)
