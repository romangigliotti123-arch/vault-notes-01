---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-reference-fidelity.md
title: "elithril/blender-kiln/plugin/references/reference-fidelity.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/reference-fidelity.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0764
relevance: 2
density: high
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-reference-fidelity.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Reference-image fidelity procedure for script-built (bpy, headless blender -b) assets in the blender-kiln plugin: inventory details, measure silhouette/profile from image or template, BVH attachment checks, palette-based materials with Poly Haven scans, sRGB bake conversion for glTF export, and measured review of the shipped GLB. Not Roblox-specific; glTF export pitfalls and bpy snippets are transferable.

## Claims
- c1: For script-built assets from a reference image, measure the image (silhouette, palette) rather than eyeballing; effort scales by tier (lightweight prop: inventory, attachment, one measure; balanced: all steps, two correction rounds). *(doc, high; claude-blender-ai)*
- c2: Inventory identity-defining details and the owning part before writing geometry, noting how parts meet (inserted, hooked, welded, resting); inventory from 3x enlarged crops. *(doc, high; claude-blender-ai)*
- c3: A photo has no scale: ask for real size or log an assumed size; also read camera elevation from rim ellipses (minor/major = sin θ) and azimuth for 3/4 views. *(doc, high; claude-blender-ai)*
- c4: Measured on Blender 5.2.2, the glTF exporter writes a linear float base-colour image to PNG without the sRGB transfer: linear 0.2 lands as byte 51 instead of 124 and reads back ~0.03 (ships near-black). Convert to sRGB byte image first. *(data, high; blender-roblox-export-import)*
- c5: glTF carries textures, not node trees, so procedural/box-projected shaders must be baked to the asset's UVs before export; pack all images (bpy.ops.file.pack_all()) or unpacked textures render black. *(doc, high; blender-roblox-export-import)*
- c6: Bake colour through an Emission shader into a float image; a DIFFUSE bake of a metallic surface comes out near-black. Relief ships as a NORMAL bake (tangent space, Non-Color float) via a Normal Map node; glTF has no bump. *(doc, high; mesh-texture-limits)*
- c7: Use 16+ sides around tubes, 32+ around turned bodies, 64+ segments for curved glass in one smooth shell; use 16-32 samples and 512 px bakes in review, 1024 only for final bake. *(doc, medium; mesh-texture-limits)*
- c8: Use one material per physical material; texture sets may be per major part (a single atlas starves large parts) but baked from one shader. Metal base colour cannot be dark; tarnish stays metal, only crusts are non-metal. *(doc, medium; mesh-texture-limits)*
- c9: Poly Haven CC0 textures are reachable without a key via api.polyhaven.com; requires unique User-Agent (ToS 2.4) and credit in asset log (ToS 2.5). Preview thumbnails should be compared to the photo crop before choosing. *(doc, high; automation-and-creator-workflows)*
- c10: Attachment check: BVH surface-to-surface distance; any part >0.5 mm from every other part floats. Contact is not insertion: joining parts should enter by at least their own radius; render joints in isolation and look at them. *(doc, high; claude-blender-ai)*
- c11: Review: fidelity_check.py renders ortho silhouette and HDRI-lit view, prints IoU and per-band width gaps; fix gaps >8% band width, not the score. Max two correction rounds (three measures), one material problem per round, correct half-way, measure the shipped _final.glb. *(doc, high; claude-blender-ai)*
- c12: Luminance and highlight values depend on unknown photo lighting: treat as alarms, fix the material not the number. Openwork objects and thin wires are judged by proportions/overlay, not IoU. *(doc, medium; claude-blender-ai)*
- c13: When a generated 3D template (e.g. TRELLIS.2) exists, extract profile from it with template_profile.py at real height (generated mesh is always 1 m tall); model from measures, not template surface, which is faceted and breaks when decimated. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **floating-part tolerance**: 0.5 mm BVH distance above which a part counts as floating
- n2: **glass segments**: ≥64 curved glass smooth shell
- n3: **sides**: 16+ tube, 32+ turned body stay round up close
- n4: **sRGB export bug**: 0.2 linear -> byte 51 vs correct 124 Blender 5.2.2 glTF exporter, float base colour
- n5: **band width gap threshold**: 8% fix gaps above this in fidelity review
- n6: **bake resolution**: 512 px review, 1024 px final 16-32 samples in review

## Techniques
- t1: **Core-width lathe profile from alpha image**: Load RGBA image in bpy, mask alpha>0.5, find vertical axis by median of opaque columns, scale height to real metres, per row take the opaque run through the axis; use as lathe profile.
- t2: **Wire centre-line tracing**: Per row between two height fractions, take outermost thin run on one side of axis, average it, thin to every ~10th point, feed NURBS order 3-4 or Bezier AUTO handles with bevel to measured thickness; never poly spline.
- t3: **Headless batch run**: blender -b --factory-startup --python-exit-code 1 --python script.py -- args, used for template_profile.py and fidelity_check.py.
- t4: **Bake-then-convert for glTF**: Build shader with box-projected textures, bake via Emission into float image, convert with to_srgb_byte, swap into Image Texture feeding Base Color, pack images, export GLB, then measure the GLB.
- t5: **Curvature-based wear**: Bake Pointiness, use part's 90th and 99th percentiles as ramp ends, multiply by noise; bare metal as one soft-edged region, not thresholded noise.
- t6: **Palette sampling**: Take 10th/50th/90th luminance percentile colours of a crop region, convert sRGB to linear, use as base colour palette.
- t7: **Fetch Poly Haven texture set**: GET api.polyhaven.com/files/<id> with custom User-Agent, download Diffuse, Rough, nor_gl, AO jpg at 1k; Non-Color for data maps.

### Code: BVH floating-part check
```python
def floating_parts(objs, tol=0.0005):
    dg = bpy.context.evaluated_depsgraph_get(); data = {}
    for o in objs:
        bm = bmesh.new(); bm.from_object(o, dg); bm.transform(o.matrix_world)
        data[o.name] = (BVHTree.FromBMesh(bm), [v.co.copy() for v in bm.verts]); bm.free()
    out = []
    for n, (_, pts) in data.items():
        d, m = min((min(t.find_nearest(p)[3] for p in pts), k) for k, (t, _) in data.items() if k != n)
        if d > tol:
            out.append((n, m, round(d * 1000, 2)))
```

### Code: Linear float to sRGB byte image before glTF export
```python
enc = np.where(rgb <= 0.0031308, rgb * 12.92, 1.055 * np.power(rgb, 1 / 2.4) - 0.055)
out = bpy.data.images.new(float_img.name + "_sRGB", w, h, alpha=True, float_buffer=False)
out.colorspace_settings.name = "sRGB"
out.pixels = np.concatenate([enc, lin[:, 3:4]], 1).ravel().tolist()
out.pack()
```

## Points to
- Poly Haven API (api.polyhaven.com)
- TRELLIS.2 (ai-generation.md)
- tools/template_profile.py
- tools/fidelity_check.py
- elithril/blender-kiln
