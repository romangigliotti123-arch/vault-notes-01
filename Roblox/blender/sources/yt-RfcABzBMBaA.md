---
type: research-source
id: yt-RfcABzBMBaA
title: "Blender Python Tutorial : How to Generate Random Numbers [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=RfcABzBMBaA"
published: "2020-10-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-RfcABzBMBaA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial on generating random numbers in bpy. Shows random.uniform for floats and random.choice(range()) for integers, then wires them into a UI panel via a property group, bpy.props.IntProperty, and an operator. Uses the random value to index a text or icon list. Does not cover Claude, blender-mcp, Roblox, or export. Relevance to the topic is low.

## Claims
- c1: [0:41] random.uniform(0,1) returns a float; random.choice(range(0,10)) returns an integer in Blender's Python console. *(demo, high; claude-blender-ai)*
- c2: [6:54] random.choice(range(0,11)) excludes the end value, so 11 never appears and the max is 10; the author recommends adding one to the end value. *(demo, high; claude-blender-ai)*
- c3: [2:21] bpy.props.IntProperty(name=..., default=0) defines a panel property; the author imports it via 'from bpy.props import ...' to avoid typing bpy.props each time. *(demo, high; claude-blender-ai)*
- c4: [9:40] layout.label(text=...) rejects a list and raises a TypeError saying a string is expected; the fix is to index the list with a string-valued value. *(demo, medium; claude-blender-ai)*
- c5: [10:20] Indexing a 3-item list with a random number 0-11 raises IndexError; the range must be limited to 0-2 for a 3-item list. *(demo, high; claude-blender-ai)*
- c6: [13:05] layout.label(icon=...) displays an icon by name; icon names are copied from the Developer Extras icon viewer (Ctrl+T) after enabling developer tools in Preferences. *(demo, medium; claude-blender-ai)*
- c7: [5:31] Debugging by print() shows output only after enabling Window > Toggle System Console. *(demo, high; claude-blender-ai)*

## Numbers
- n1: **range end value**: 11 (yields 0-10) random.choice(range(0,11)) used to show 0-10 inclusive
- n2: **list length for index**: 3 items (indexes 0-2) text list a,b,c; random range set to 0-2 to avoid IndexError

## Techniques
- t1: **Random int property via bpy.props**: Add IntProperty(name, default=0) to a PropertyGroup, draw it on the panel, and set it from the operator with x = random.choice(range(0,N)) then tool.random_number = x.
- t2: **Index list by random property**: Define text_list=['a','b','c']; draw layout.label(text=tool.text_list[tool.random_number]) with range limited to len(list).

### Code: Float and integer random generation in Blender Python console
```python
import random
random.uniform(0, 1)
random.choice(range(0, 10))
```

### Code: Panel property declaration
```python
from bpy.props import IntProperty
random_number: IntProperty(name="", default=0)
```

## Contradictions flagged
- Integer random values are produced with random.choice(range(a,b)) and the range end must be one past the max. (vs Common Python practice uses random.randint(a,b), which is inclusive of both ends; the tutorial does not mention it.)
