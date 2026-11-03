---
type: research-source
id: web-ca8d66a253
title: "Blender manual: advanced/command_line/arguments"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/advanced/command_line/arguments.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 2
density: high
tags: ["research-source", "web", "bpy-scripting-headless", "creator-workflows", "other"]
---
# web-ca8d66a253

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender CLI reference: background mode (-b), render flags (-a, -f, -o, -F, -E), Python execution (-P, --python-expr, -- to pass args to sys.argv), logging, and argument order rules. Useful for headless bpy/batch workflows; says nothing about Roblox, MCP, or export settings.

## Claims
- c1: -b/--background runs Blender without UI; audio device disabled by default in background mode, re-enable with -setaudio Default. *(doc, high; bpy-scripting-headless)*
- c2: Arguments execute in the order given; --render-output set after --render-frame has no effect, and placing the output path before the .blend file is overwritten by loading it. *(doc, high; bpy-scripting-headless)*
- c3: Flags must be whitespace-separated; -ba is treated as unknown argument and Blender exits. *(doc, high; bpy-scripting-headless)*
- c4: --python-expr accepts a complete multi-line script, limited only by platform max argument length. *(doc, high; bpy-scripting-headless)*
- c5: Arguments after -- are passed unchanged and accessible via Python sys.argv, for passing custom parameters to headless scripts. *(doc, high; bpy-scripting-headless)*
- c6: -c/--command implies background mode; --python-exit-code sets exit code 0-255 when a script raises an exception (0 disables). *(doc, high; bpy-scripting-headless)*
- c7: Automatic Python script execution (drivers, startup scripts) is disabled by default; enable with -y/--enable-autoexec. *(doc, high; bpy-scripting-headless)*
- c8: In background mode, depsgraph is not built on file load by default (--disable-depsgraph-on-file-load); scripts needing evaluated data must call context.evaluated_depsgraph_get() explicitly. Described as temporary option. *(doc, high; bpy-scripting-headless)*
- c9: Output path with // is relative to the blend file; # characters set zero-padding; without # the suffix #### is appended. *(doc, high; creator-workflows)*
- c10: -X/--factory-startup skips reading user startup.blend, giving reproducible headless runs. *(doc, medium; other)*
- c11: --addons takes comma-separated list with no spaces to enable add-ons in addition to defaults. *(doc, high; bpy-scripting-headless)*

## Numbers
- n1: **--python-exit-code range**: 0-255 (0 disables) 
- n2: **--threads range**: 1-1024; 0 = system processor count 
- n3: **Frame padding example**: animation_##_test.png -> animation_01_test.png 

## Techniques
- t1: **Headless batch render**: Run blender -b file.blend -o //render_ -F PNG -x 1 -a. Set output before -f/-a; loading the blend later overwrites output path.
- t2: **Pass params to bpy script**: blender -b file.blend -P script.py -- arg1 arg2; read args from sys.argv after the -- separator.
- t3: **Inline Python**: Use --python-expr with a multi-line script string, or --python-text for a text block in the .blend.
- t4: **Fail-fast CI scripts**: Set --python-exit-code 1 so an uncaught exception yields a nonzero exit for automation.

### Code: Headless render with output set before frame/anim flags
```sh
blender -b animation.blend -o //render_ -F PNG -x 1 -a
```

### Code: Run a script with custom args passed via sys.argv
```sh
blender -b file.blend -P script.py -- --out /tmp/export
```

### Code: Force depsgraph evaluation inside background script (per manual)
```sh
depsgraph = context.evaluated_depsgraph_get()
```

## Quotes (brief, for attribution)
> ...will not render to /tmp because --render-frame 1 renders before the output path is set.  (docs.blender.org)
> Arguments must be separated by white space.  (docs.blender.org)

## Points to
- https://projects.blender.org/blender/blender/src/branch/main/source/creator/creator_args.cc
