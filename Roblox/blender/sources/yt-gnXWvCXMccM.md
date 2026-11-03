---
type: research-source
id: yt-gnXWvCXMccM
title: "Blender Python Tutorial : How to make a Random Word Generator [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=gnXWvCXMccM"
published: "2021-01-21"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-gnXWvCXMccM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender bpy tutorial: builds a random word generator add-on with a property group, operator, and UI panel. Uses random.randint over Python lists, len() to size ranges, and the system console for debugging. Contains nothing on Claude, blender-mcp, Roblox export, FBX/glTF, triangle limits, rigging, or accessories.

## Claims
- c1: [0:43] Blender add-on pattern in the tutorial needs three parts: a panel, an operator, and a property group, using a template from the Scripting workspace. *(demo, high; claude-blender-ai)*
- c2: [3:55] Operator generates random index with random randint(a, b) where a=0 and b=len(list)-1, since Python indexing starts at zero. *(demo, high; claude-blender-ai)*
- c3: [7:56] Printed list lengths appear only in the system console (Window > Toggle System Console); list A=6, list B=217, list C=104 items. *(demo, high; claude-blender-ai)*
- c4: [8:37] Debugging counts with len() was used instead of manual counting; ranges set to 0-5, 0-216, 0-103. *(demo, medium; claude-blender-ai)*
- c5: [5:38] Panel displays the chosen word via layout.label(text=mytool.list_a[mytool.number_1]) with integer properties updated by the operator. *(demo, medium; claude-blender-ai)*
- c6: [0:00] Tutorial states the word generator can produce random names, street names, or places; no Roblox or Claude content is present. *(opinion, low; other)*

## Numbers
- n1: **list A item count**: 6 Counted via len() and printed to system console
- n2: **list B item count**: 217 Range set to 0-216 after subtracting one
- n3: **list C item count**: 104 Range set to 0-103 after subtracting one

## Techniques
- t1: **Random index from list length**: Use len(list) to get item count. Set a=0 and b=len-1. Call random randint(a,b). Store result in an IntProperty and display list[index] in the panel label.
- t2: **Property group for UI state**: Define lists and IntProperty defaults in a PropertyGroup. Operator writes random results to those properties. Panel reads them via mytool.property to show text.

### Code: Random index generation in operator (as narrated, Blender bpy add-on context)
```python
a = 0
b = len(mytool.list_a) - 1
r1 = randint(a, b)
mytool.number_1 = r1
```

### Code: Panel label showing selected word
```python
layout.label(text=mytool.list_a[mytool.number_1])
```

## Quotes (brief, for attribution)
> we're going to need a panel an operator and a property group  (at 0:43, Darkfall)
> list A has six items list B has 217 list C has 104  (at 8:37, Darkfall)
