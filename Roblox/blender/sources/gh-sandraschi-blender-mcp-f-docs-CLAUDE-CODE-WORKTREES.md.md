---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-CLAUDE-CODE-WORKTREES.md
title: "sandraschi/blender-mcp/docs/CLAUDE-CODE-WORKTREES.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/CLAUDE-CODE-WORKTREES.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0411
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# gh-sandraschi-blender-mcp-f-docs-CLAUDE-CODE-WORKTREES.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
A guide to developing the sandraschi/blender-mcp server with Claude Code git worktrees, one per domain (modeling, animation, rendering, materials, scripting, import/export, testing). It gives per-domain prompts and bpy API pointers. It has nothing on Roblox, and no concrete export settings, limits or code. The performance claims are unsupported.

## Claims
- c1: The guide splits blender-mcp development across 7 git worktrees (modeling, animation, rendering, materials, scripting, io, testing). Each runs its own Claude Code session with a domain-specific prompt. *(doc, high; claude-blender-ai)*
- c2: The scripting-domain prompt lists dynamic bpy script generation and execution, a safe execution sandbox, operator registration, and Blender 2.8x–4.x version compatibility via bpy.app.version. *(doc, medium; claude-blender-ai)*
- c3: The import/export worktree prompt targets FBX, OBJ, GLTF, STL and PLY via bpy.ops.import_scene / export_scene, plus batch conversion and metadata preservation. It gives no Roblox-specific settings (scale, axes, apply transforms). *(doc, high; blender-roblox-export-import)*
- c4: The testing worktree calls for automated Blender headless testing, mesh integrity validation, performance benchmarks, and cross-version checks. It gives no concrete commands. *(doc, medium; claude-blender-ai)*
- c5: Each worktree can carry its own CLAUDE.md. The example for modeling lists key bpy modules (meshes, objects, bmesh, mathutils) and advises using bmesh for complex mesh operations and batching operations. *(doc, medium; automation-and-creator-workflows)*
- c6: The guide asserts '10x faster' development and 'days instead of weeks' with parallel Claude instances. It gives no measurement, so this is opinion. *(opinion, low; claude-blender-ai)*
- c7: The animation prompt points to bpy.data.actions, bpy.data.armatures, keyframe_insert(), fcurves, and scene.frame_set() as the key APIs for keyframes and rigs. It has no Roblox rig (R15/Motor6D) content. *(doc, medium; rigging-animation)*

## Numbers
- n1: **worktrees/Claude sessions**: 7 modeling, animation, rendering, materials, scripting, io, testing
- n2: **supported Blender versions**: 2.8x–4.x compatibility target in the prompts

## Techniques
- t1: **Domain-based git worktrees for Claude Code**: From the repo, run `git worktree add ../blender-<domain> -b feature/<name>` for each domain. cd into each worktree and run `claude` with a domain-specific prompt. Optionally add a per-worktree CLAUDE.md listing the key bpy modules.
- t2: **Compatibility worktrees per Blender version**: Create worktrees such as compat/blender-2.8x, 3.x and 4.x to test the MCP server against several Blender versions in parallel.

### Code: Create per-domain worktrees for parallel Claude Code sessions
```bash
git worktree add ../blender-modeling -b feature/3d-modeling
git worktree add ../blender-animation -b feature/animation-tools
git worktree add ../blender-io -b feature/import-export
git worktree add ../blender-testing -b improve/comprehensive-testing
```

## Points to
- sandraschi/blender-mcp
- Claude Code git worktrees
- Claude Desktop (MCP client)
