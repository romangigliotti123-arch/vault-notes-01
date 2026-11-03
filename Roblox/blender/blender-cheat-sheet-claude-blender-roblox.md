---
type: research-cheat-sheet
topic: "Claude + Blender + Roblox: do this first"
date: 2026-11-01
status: "v2. Only OFFICIAL or CORROBORATED lines. OFFICIAL = checked against Roblox creator-docs, DevForum staff posts or the tool's own README read in this run. The bpy script has NOT been run in Blender; see its validation note."
tags: [research, blender, roblox, claude, cheat-sheet]
---
# Claude + Blender + Roblox: do this first

Hub: [[blender-README]] (includes "how reliable is this") | long form: [[blender-playbook]] | topics: [[blender-topic-claude-blender-ai]], [[blender-topic-blender-roblox-export-import]], [[blender-topic-mesh-texture-limits]], [[blender-topic-avatar-ugc-accessories]], [[blender-topic-rigging-animation]]

## 1. Connect Claude to Blender (unchanged from v1; all from the tool's own README)
**[OFFICIAL: github.com/ahujasid/mcp-for-blender README]** The tool is `mcp-for-blender` (formerly `blender-mcp`; `uvx blender-mcp` still works). Needs Blender 3.0+, Python 3.10+, `uv`. It is a community plugin, not made by Blender.

Windows
1. **[OFFICIAL]** `winget install --id=astral-sh.uv -e`, then open a NEW terminal (no script is run).
2. **[OFFICIAL]** `uvx mcp-for-blender install-addon`, then in Blender: Edit > Preferences > Add-ons, enable "Interface: MCP for Blender".
3. **[OFFICIAL]** In the 3D viewport press N, open the "MCP for Blender" tab, click Start MCP Server (default socket port 9876).
4. **[OFFICIAL]** Claude Code: `claude mcp add blender uvx mcp-for-blender`. Claude Desktop: Settings > Developer > Edit Config, add `{"mcpServers":{"blender":{"command":"uvx","args":["mcp-for-blender"]}}}`.
5. **[OFFICIAL]** GUI clients that print `spawn uvx ENOENT`: use the full path from `where uvx` as `command`, or `"command":"cmd","args":["/c","uvx","mcp-for-blender"]`.

Mac: **[OFFICIAL]** install uv from the official installer or Homebrew (`brew install uv`), then the same steps 2-4 (use `which uvx` for the full path).

Safety **[OFFICIAL, same README]**: the add-on socket has no authentication or encryption (keep it on localhost); `execute_blender_code` runs arbitrary Python (save the .blend first); `BLENDER_MCP_SAFE_MODE=1` validates scripts before they run and is OFF by default; run only one MCP server instance; for timeouts, break requests into smaller steps.

Headless alternative (no MCP): **[OFFICIAL: Blender manual, command line arguments]** `blender -b file.blend -P script.py -- args` (`-b` background, `-P/--python` run script, everything after `--` is passed to the script via `sys.argv`).

**[CORROBORATED]** Claude-written bpy breaks across Blender 4.0 / 4.4 / 5.0 API changes: check `bpy.app.version_string`, find nodes by type instead of by name, and re-open the exported file to measure it before trusting it.

## 2. bpy export recipe for Roblox (syntax-checked and API-name-checked, NOT run in Blender)
Run: `blender -b model.blend -P export_roblox.py -- C:/out/model.fbx`. It never saves the .blend. Validation done 2026-11-01 without installing Blender: (a) `py_compile` passes; (b) every operator, property and enum name used exists in the Blender `main` source mirror (github.com/blender/blender: `export_scene.fbx` properties and enum values FBX_SCALE_UNITS / COPY / MESH / ARMATURE in scripts/addons_core/io_scene_fbx/__init__.py; Mesh.calc_loop_triangles in rna_mesh_api.cc; Object.to_mesh, to_mesh_clear, hide_get, select_set in rna_object_api.cc; evaluated_get in rna_ID.cc); (c) a mock-`bpy` dry run executed the script logic (12 triangles counted, FBX call received 13 keyword arguments). Names were checked against `main` (Blender 5.x line), not 3.x/4.x; the script filters keywords against the live operator, so older builds silently drop unknown options (read the console). The export settings themselves are OFFICIAL (Roblox art/blender, art/modeling/export-requirements). If you author in meters, also set the importer Scale Unit / Scale Factor (section 3).

```python
import sys, bpy
out = sys.argv[sys.argv.index("--") + 1]
MAX_TRIS = 20000          # OFFICIAL: individual meshes cannot exceed 20,000 triangles (4,000 for rigid and layered accessories; bodies have per-part budgets)

meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH' and not o.hide_get()]
if not meshes: sys.exit("no visible meshes")
bpy.ops.object.select_all(action='DESELECT')
deps = bpy.context.evaluated_depsgraph_get()
tris = 0
for o in meshes:
    me = o.evaluated_get(deps).to_mesh()          # modifiers applied in the evaluated copy
    me.calc_loop_triangles(); tris += len(me.loop_triangles)
    o.evaluated_get(deps).to_mesh_clear()
    o.select_set(True)
    if len(o.data.materials) > 1: print("WARN: one material per mesh is the Roblox limit:", o.name)
    if any(abs(s - 1) > 1e-4 for s in o.scale): print("WARN unapplied scale:", o.name, tuple(o.scale))
print("triangles:", tris)
if tris > MAX_TRIS: sys.exit(f"{tris} triangles > {MAX_TRIS}: reduce first")
bpy.context.view_layer.objects.active = meshes[0]

kw = dict(filepath=out, use_selection=True,            # "Limit to Selected Objects"
          object_types={'MESH', 'ARMATURE'}, use_mesh_modifiers=True,
          apply_scale_options='FBX_SCALE_UNITS',       # Apply Scalings = FBX Unit Scale
          global_scale=1.0, apply_unit_scale=True,     # other scale values 1.0
          axis_forward='Z', axis_up='Y',               # Z Forward, Y Up
          path_mode='COPY', embed_textures=True,       # Path Mode Copy + Embed Textures
          add_leaf_bones=False,                        # Armature: Add Leaf Bones off
          bake_anim=False)                             # on only when exporting keyframed animation
valid = set(bpy.ops.export_scene.fbx.get_rna_type().properties.keys())
bpy.ops.export_scene.fbx(**{k: v for k, v in kw.items() if k in valid})   # silently drops options your Blender lacks: check the console
```
- **[OFFICIAL]** glTF needs none of the FBX scale adjustments (Roblox art/blender). The operator `export_scene.gltf` with `export_format='GLB'` and `use_selection` exists in the Blender source (io_scene_gltf2); not run here.
- **[OFFICIAL]** Scene setup: Unit System = None, Rotation = Degrees. Blender is Z-up, Studio is Y-up. Studio import: World Forward = Front, World Up = Top, Scale Unit = Stud.

## 3. Key numbers (read directly from the page named, 2026-11-01; Roblox creator-docs mirror github.com/Roblox/creator-docs)
| item | value | page |
|---|---|---|
| Triangles, any individual mesh | 20,000 | art/modeling/specifications |
| Triangles, rigid accessory | 4,000 | avatar/rigid-accessories/specifications |
| Triangles, layered accessory | 4,000 | avatar/layered-accessories/specifications |
| Body budgets (Dynamic head / torso / each limb / total) | 4000 / 1750 / 1248 / 10,742 | avatar/character-bodies/specifications (extracted figures) |
| Bone influences per vertex | 4 max, none on Root | art/modeling/specifications |
| Marketplace avatar texture size | 2048x2048 max (raised by DevForum staff post 2026-02-12; low-end mobile under 3.5 GB RAM still gets 1k) | avatar/*/specifications; devforum.roblox.com/t/4358444 |
| Clothing mesh max size | 8 x 8 x 8 studs | avatar/layered-accessories/specifications (extracted) |
| Open Cloud asset upload | 20 MB per create/update call | cloud/guides/usage-assets (extracted) |
| Importer unit conversion | non-Stud units use 25:7 Studs/m since 2026-06-16 (was 20:1); Scale Factor field added; Stud with factor 1.0 unchanged | devforum.roblox.com/t/4644371 |
| Roblox Blender plugin, Blender version | README and docs say "3.2 or greater"; the current release v1.0.5 (2026-04-20) fixes Blender 5.x API breakage and "should now work with 5.0 and 5.1", "may not be compatible with blender v4.x and under" | github.com/Roblox/roblox-blender-plugin README + release v1.0.5 |

Texture limits, resolved by scope (art/modeling/texture-specifications, docs commit 2026-07-22, plus the avatar specification pages): 4096x4096 is the engine's general upload ceiling; 1024x1024 is the maximum of the PBR texture budget table (and of the UV section); 2048x2048 is the cap for Marketplace rigid and layered accessory textures; 256x256 is the maximum budget for non-albedo maps of rigid accessories. These are different scopes, not a conflict, but the docs page does not label the scopes clearly. Detail: [[blender-open-questions]].

## 4. Checklist by stage (labelled research, OFFICIAL/CORROBORATED only)
1. **[OFFICIAL]** If you want Open Cloud upload from Blender, install the Roblox Blender plugin. Click Install Dependencies once in the N-panel Roblox tab, restart Blender, log in via browser OAuth, then pick the creator in the 'Upload to' dropdown. [[sources/off-gh-roblox-blender-plugin-README|off-gh-roblox-blender-plugin-README]] [[sources/off-art_modeling_roblox-blender-plugin|off-art_modeling_roblox-blender-plugin]] [[sources/web-1170ea0231|web-1170ea0231]]
2. **[OFFICIAL]** Match the plugin version to your Blender. v1.0.5 fixes install errors on Blender 5.0 and 5.1 and needs Blender 3.2+. It may not work on 4.x or earlier. [[sources/off-gh-roblox-blender-plugin-rel-v1.0.5|off-gh-roblox-blender-plugin-rel-v1.0.5]] [[sources/gh-Roblox-roblox-blender-plugin-rel-v1.0.5|gh-Roblox-roblox-blender-plugin-rel-v1.0.5]] [[sources/gh-Roblox-roblox-blender-plugin-i8|gh-Roblox-roblox-blender-plugin-i8]]
3. **[OFFICIAL]** If login fails with a DNS error on Windows, delete the bundled aiodns folder. For ModuleNotFoundError, do a clean reinstall. Avoid rapid repeat logins (429). Read the system console for logs. [[sources/gh-Roblox-roblox-blender-plugin-i112|gh-Roblox-roblox-blender-plugin-i112]] [[sources/gh-Roblox-roblox-blender-plugin-i35|gh-Roblox-roblox-blender-plugin-i35]] [[sources/gh-Roblox-roblox-blender-plugin-i75|gh-Roblox-roblox-blender-plugin-i75]]

## 2. Scripting Blender with bpy (headless/batch)
4. **[OFFICIAL]** Run batch scripts with `blender --background --factory-startup --python-exit-code 1 --python script.py -- args`. Then check the exit code and that the output file exists. [[sources/gh-elithril-blender-kiln-f-plugin-references-animation.md|gh-elithril-blender-kiln-f-plugin-references-animation.md]] [[sources/gh-elithril-blender-kiln-f-plugin-references-export-targets.md|gh-elithril-blender-kiln-f-plugin-references-export-targets.md]]

### 3. Model within Roblox limits
5. **[OFFICIAL]** Keep each mesh at or under 20,000 triangles. Rigid accessories must be one mesh at or under 4,000 triangles. Body budgets: head 4000, torso 1750, each arm and leg 1248. Triangles are about 2x quads. [[sources/web-7195087017|web-7195087017]] [[sources/off-dev_3958222|off-dev_3958222]] [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]]
6. **[OFFICIAL]** Make geometry watertight with quads, no N-gons, and non-zero thickness. Use one material per mesh and a single UV set with all UVs inside 0:1. [[sources/off-art_modeling_specifications|off-art_modeling_specifications]] [[sources/web-7195087017|web-7195087017]] [[sources/off-dev_4950522|off-dev_4950522]]
7. **[OFFICIAL]** Size textures to the item. Basic guidance: 5x5 studs 256, 10x10 512, 20x20 1024. Marketplace avatar textures are capped at 2048. [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] [[sources/off-dev_4358444|off-dev_4358444]] [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]]
8. **[OFFICIAL]** For PBR use SurfaceAppearance maps: OpenGL tangent-space normals, metalness workflow only, albedo with no baked lighting. For accessories, cap Normal/Roughness/Metalness at 256 and Color at 1024. [[sources/off-dev_3816937|off-dev_3816937]] [[sources/off-art_modeling_texture-specifications|off-art_modeling_texture-specifications]] [[sources/off-art_modeling_surface-appearance|off-art_modeling_surface-appearance]]

### 4. Rig and animate
9. **[CORROBORATED]** Before rigging, apply scale and rotation, weld duplicate vertices and remove loose parts. Disconnected islands make automatic weights fail. [[sources/gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-rigging.md|gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-rigging.md]] [[sources/gh-elithril-blender-kiln-f-plugin-references-characters.md|gh-elithril-blender-kiln-f-plugin-references-characters.md]]
10. **[OFFICIAL]** Use the standard R15 hierarchy and Roblox's Rig_and_Attachments_Template.blend. Put Root and LowerTorso at 0,0,0 and parent all 15 meshes to one armature. [[sources/off-avatar_character-bodies_specifications|off-avatar_character-bodies_specifications]] [[sources/web-2a50b96cb8|web-2a50b96cb8]] [[sources/off-art_modeling_rig-a-humanoid-model|off-art_modeling_rig-a-humanoid-model]]
11. **[OFFICIAL]** Respect the skinning limits: at most 4 influences per vertex, none on Root or HumanoidRootNode, and bones frozen at scale 1 and rotation 0. [[sources/off-art_modeling_skin-a-humanoid-model|off-art_modeling_skin-a-humanoid-model]] [[sources/off-art_modeling_specifications|off-art_modeling_specifications]] [[sources/off-studio_importer|off-studio_importer]]
12. **[OFFICIAL]** Paint weights with the armature shown as Sticks and Auto Normalize on. Use X-Axis Mirror, test in Pose mode and reset with Alt+R. [[sources/web-1cc5c97477|web-1cc5c97477]] [[sources/off-art_modeling_skin-a-humanoid-model|off-art_modeling_skin-a-humanoid-model]] [[sources/off-art_modeling_rig-a-humanoid-model|off-art_modeling_rig-a-humanoid-model]]
13. **[OFFICIAL]** Export FBX with Add Leaf Bones off. Enable Bake Animation only for keyframed content, and export one animation track per file. [[sources/web-3a1e35acf3|web-3a1e35acf3]] [[sources/off-art_modeling_specifications|off-art_modeling_specifications]] [[sources/web-7195087017|web-7195087017]]
14. **[OFFICIAL]** Import animations through the Animation Clip Editor importer (Rig Type, Rig Scale, Rest Pose Source). Use Joint Upgrade constraints for multi-bone rigs. Expect AnimationConstraint rather than Motor6D under the Avatar Joint Upgrade. [[sources/off-dev_4775593|off-dev_4775593]] [[sources/off-dev_4260501|off-dev_4260501]] [[sources/web-af064b2633|web-af064b2633]]

### 5. Export from Blender
15. **[OFFICIAL]** Export FBX with Apply Scalings = FBX Unit Scale, Path Mode = Copy with Embed Textures, Add Leaf Bones off, selected objects only, and lights and cameras removed. [[sources/off-art_accessories_creating_exporting|off-art_accessories_creating_exporting]] [[sources/off-art_blender|off-art_blender]] [[sources/off-art_modeling_export-requirements|off-art_modeling_export-requirements]]
16. **[CORROBORATED]** Apply modifiers before export, including Geometry Nodes results. Do not rename meshes or move pivots if you plan to Reimport. [[sources/gh-elithril-blender-kiln-f-plugin-references-batch-mode.md|gh-elithril-blender-kiln-f-plugin-references-batch-mode.md]] [[sources/off-art_accessories_creating_exporting|off-art_accessories_creating_exporting]] [[sources/off-dev_4068650|off-dev_4068650]]
17. **[OFFICIAL]** Connect the colour map to alpha in the Blender PBR material and export glTF/FBX, so the importer auto-sets DoubleSided and Transparency. [[sources/off-dev_4137281|off-dev_4137281]]
18. **[OFFICIAL]** For avatar items, include cages named <Mesh>_InnerCage and <Mesh>_OuterCage from Roblox's templates. Never delete cage vertices or alter cage UVs. [[sources/off-art_modeling_specifications|off-art_modeling_specifications]] [[sources/off-avatar_layered-accessories_specifications|off-avatar_layered-accessories_specifications]] [[sources/web-04cef4e0ee|web-04cef4e0ee]]

### 6. Import into Studio and iterate
19. **[OFFICIAL]** Import via the Studio Importer. Pick the scale approach deliberately: Scale Unit Stud, or a real-world unit plus the Scale Factor field. Enable 'Uses Cages' when cages are present. [[sources/off-art_blender|off-art_blender]] [[sources/off-dev_4644371|off-dev_4644371]] [[sources/off-art_modeling_cage-meshes_index|off-art_modeling_cage-meshes_index]]
20. **[OFFICIAL]** For bulk imports use the import queue presets and Apply settings to all. Use the Upload to Roblox toggle during test iteration. [[sources/off-studio_importer|off-studio_importer]] [[sources/web-5d5513d689|web-5d5513d689]]
21. **[OFFICIAL]** Iterate with Reimport (right-click or Alt+Shift+R). It matches meshes by name. Use Quick Import (Alt+M) for single files. [[sources/off-dev_4068650|off-dev_4068650]] [[sources/off-dev_4112031|off-dev_4112031]] [[sources/off-dev_3958222|off-dev_3958222]]
22. **[OFFICIAL]** For layered accessories, import as a Model and then use the Accessory Fitting Tool (Generate MeshPart Accessory). Check Marketplace requirements: Material Plastic, Transparency 0, VertexColor 1,1,1, no extra Scripts or Parts. [[sources/off-avatar_layered-accessories_import|off-avatar_layered-accessories_import]] [[sources/web-5d5513d689|web-5d5513d689]] [[sources/web-0d333c4d57|web-0d333c4d57]]
23. **[OFFICIAL]** Validate with the UGC Validation visualization plugin (red for errors, yellow for warnings). [[sources/off-dev_4709282|off-dev_4709282]] [[sources/off-dev_4950522|off-dev_4950522]]

### 7. Upload and automate
24. **[OFFICIAL]** Upload from the Blender plugin and check Toolbox > Inventory > My Packages. Re-uploading updates the same package. Deleting the 'Roblox Package ID' custom property creates a new asset. [[sources/off-gh-roblox-blender-plugin-README|off-gh-roblox-blender-plugin-README]]
25. **[OFFICIAL]** For HTTP automation, use the Open Cloud Assets API: an x-api-key, up to 20 MB per call, then poll the returned operation for the assetId. It accepts .rbxm, animations and Roblox meshes since 2025-10-23. Docs still recommend the Studio Importer for custom 3D models. [[sources/off-cloud_guides_usage-assets|off-cloud_guides_usage-assets]] [[sources/web-57279f4b4c|web-57279f4b4c]] [[sources/off-dev_4022082|off-dev_4022082]]

