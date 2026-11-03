---
type: research-source
id: yt-5T0sSKH2_0o
title: "Blender Python Tutorial : Lists - Create, Append and Remove [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=5T0sSKH2_0o"
published: "2020-11-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-5T0sSKH2_0o

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial on Python list basics (create, append, extend, remove, clear) run in the Blender Python console, then applied inside a bpy addon panel with an enum-driven operator. Covers duplicate prevention with "not in" checks and a StringProperty input. Does not cover Claude, blender-mcp, Roblox export, or mesh/rig limits.

## Claims
- c1: Tutorial uses bpy addon scaffolding (property group, panel, operator) and Window > Toggle System Console to print debug output. *(demo, medium; claude-blender-ai)*
- c2: [8:42] Pressing an append button twice duplicates items unless guarded with an 'if a and b are not in list' check. *(demo, high; claude-blender-ai)*
- c3: [10:41] In property definitions, newer Blender versions require colon annotation syntax (name: StringProperty) instead of '=', which gives a warning otherwise. *(demo, medium; claude-blender-ai)*
- c4: [5:13] EnumProperty accepts expand=True to render options as button row instead of dropdown in the panel. *(demo, high; claude-blender-ai)*
- c5: Non-Roblox general Python: list.extend(iterable) appends multiple items, list.clear() empties list, list.remove(x) deletes first match. *(demo, high; other)*

## Techniques
- t1: **Guard list append against duplicates**: Wrap list.append in 'if a and b not in list:' so repeated button presses do not add items again.
- t2: **Convenience variable for pointer property**: Assign my_tool.my_list to a local name like list to shorten repeated access in operator code.

### Code: Branch operator logic on EnumProperty identifier
```python
if enum == 'OP1':
    if a not in list and b not in list:
        list.extend([a, b])
else:
    list.clear()
```

## Points to
- Darkfall blog template download (linked in description, not fetched)
- Darkfall list-search tutorial (linked in description)
