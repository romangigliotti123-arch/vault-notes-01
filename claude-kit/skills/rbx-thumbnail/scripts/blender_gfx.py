#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later
"""blender_gfx.py: optional headless Blender renders for Roblox icons and thumbnails (stdlib only; never installs, downloads or enables add-ons).

  blender_gfx.py detect
  blender_gfx.py gen --recipe icon|portrait|action|scene|variants [--subject primitive:cube|FILE.obj|fbx|glb] [--name N] [--project DIR] [--size icon|thumb|WxH]
                     [--palette warm|cool|comp] [--hero-color RRGGBB] [--flat-color RRGGBB] [--outline] [--glow] [--pose part=rx,ry,rz] [--focal MM]
                     [--blender-version X.Y] [--brief brief.json]     (flags and brief keys are the same; flags win)
  blender_gfx.py check SCRIPT [--project DIR]
  blender_gfx.py run SCRIPT [--project DIR] [--engine eevee|cycles] [--samples N] [--allow-high] [--subject FILE] [--timeout S] [--blender PATH]

Everything is written under <project>/renders/ (scripts in renders/_scripts/). `run` refuses any script that fails `check`. The generated bpy scripts are GPL-2.0-or-later
(blender.org: published scripts using the Blender API must be GPL-compatible); the renders you make are yours. Recipes come from the vault note on Blender GFX and are UNTESTED LIVE.
"""
import argparse
import ast
import glob
import hashlib
import json
import os
import re
import struct
import subprocess
import sys
import time

MISSING = "Blender not found: thumbnails/icons use the checklist and prompts only (optional: install Blender for rendered GFX)"
TIMEOUT = {"eevee": 180, "cycles": 420}
CAPS = {"eevee": 64, "cycles": 128}
HARD_CAP = 256
SIZES = {"icon": (1024, 1024), "thumb": (1920, 1080), "portrait": (1024, 1280)}
MODEL_EXT = ("obj", "fbx", "glb", "gltf")
PRIMS = ("cube", "sphere", "cone", "cylinder", "torus", "gem")
NAME_RX = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,39}$")
HEX_RX = re.compile(r"^#?[0-9A-Fa-f]{6}$")
ENV_KEEP = ("PATH", "PATHEXT", "COMSPEC", "SYSTEMROOT", "SYSTEMDRIVE", "WINDIR", "TEMP", "TMP", "HOME", "USERPROFILE", "APPDATA", "LOCALAPPDATA", "DISPLAY",
            "WAYLAND_DISPLAY", "XDG_RUNTIME_DIR", "XDG_CONFIG_HOME", "XDG_DATA_HOME", "LANG", "LD_LIBRARY_PATH")


def inside(base, p):
    b, q = os.path.normcase(os.path.realpath(base)), os.path.normcase(os.path.realpath(p))
    return q == b or q.startswith(b + os.sep)


def render_dir(project):
    return os.path.join(os.path.realpath(project or os.getcwd()), "renders")


def parse_version(text):
    m = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", text or "")
    return tuple(int(x or 0) for x in m.groups()) if m else None


def candidates():
    out = []
    if os.name == "nt":
        roots = [os.environ.get(k) for k in ("ProgramFiles", "ProgramFiles(x86)")]
        for r in filter(None, roots):
            out += glob.glob(os.path.join(r, "Blender Foundation", "Blender *", "blender.exe"))
            out += glob.glob(os.path.join(r, "Steam", "steamapps", "common", "Blender", "blender.exe"))
        la = os.environ.get("LOCALAPPDATA")
        if la:
            out += glob.glob(os.path.join(la, "Programs", "Blender Foundation", "Blender *", "blender.exe"))
    elif sys.platform == "darwin":
        out += ["/Applications/Blender.app/Contents/MacOS/Blender", os.path.expanduser("~/Applications/Blender.app/Contents/MacOS/Blender")]
    else:
        out += ["/usr/bin/blender", "/usr/local/bin/blender", "/snap/bin/blender"] + glob.glob("/opt/blender*/blender")
    out = [p for p in out if os.path.isfile(p)]
    out.sort(key=lambda p: parse_version(os.path.basename(os.path.dirname(p))) or (0,), reverse=True)
    return out


def find_blender(explicit=None):
    envp = explicit or os.environ.get("BLENDER_BIN")
    if envp and os.path.isfile(envp):
        return envp
    from shutil import which
    return which("blender") or (candidates() or [None])[0]


def clean_env():
    return {k: v for k, v in os.environ.items() if k in ENV_KEEP or k.startswith("BLENDER_")}


def blender_version(exe):
    try:
        r = subprocess.run([exe, "--version"], capture_output=True, text=True, timeout=60, env=clean_env())
        return parse_version(r.stdout)
    except (OSError, subprocess.SubprocessError):
        return None


def cmd_detect(a):
    exe = find_blender(getattr(a, "blender", None))
    if not exe:
        print(MISSING)
        return 3
    v = blender_version(exe)
    print("Blender %s at %s" % (".".join(map(str, v)) if v else "(version unknown)", exe))
    return 0


# ---------------------------------------------------------------- safety check
ALLOWED_IMPORTS = {"bpy", "bmesh", "mathutils", "math", "random", "sys", "colorsys", "bpy_extras"}
BAD_NAMES = {"eval", "exec", "compile", "open", "__import__", "getattr", "setattr", "delattr", "globals", "locals", "vars", "input", "breakpoint", "exit", "quit", "memoryview"}
BAD_ATTRS = {"save_render", "save", "write", "save_as_mainfile", "system", "popen", "unlink", "remove_files"}
BAD_PREFIX = ("bpy.utils", "bpy.ops.script", "bpy.ops.preferences", "bpy.ops.file", "bpy.ops.text", "bpy.ops.export", "bpy.ops.image.save", "bpy.ops.image.open",
              "bpy.data.libraries", "bpy.data.texts", "bpy.app.handlers", "bpy.app.timers", "bpy.context.preferences", "bpy.app.binary_path", "addon_utils")
WM_OK = ("read_factory_settings", "obj_import")
PATHISH = re.compile(r"^(/|\\|[A-Za-z]:[\\/])|\.\.[\\/]|^//")


def dotted(n):
    parts = []
    while isinstance(n, ast.Attribute):
        parts.append(n.attr)
        n = n.value
    if isinstance(n, ast.Name):
        parts.append(n.id)
        return ".".join(reversed(parts))
    return None


def check_source(src, rdir=None):
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return ["line %s: syntax error: %s" % (e.lineno, e.msg)]
    bad = []
    for n in ast.walk(tree):
        ln = getattr(n, "lineno", 0)
        if isinstance(n, ast.Import):
            for al in n.names:
                if al.name.split(".")[0] not in ALLOWED_IMPORTS:
                    bad.append("line %d: import %s is not allowed" % (ln, al.name))
        elif isinstance(n, ast.ImportFrom):
            if n.level or (n.module or "").split(".")[0] not in ALLOWED_IMPORTS or (n.module or "").split(".")[0] == "sys":
                bad.append("line %d: from %s import is not allowed" % (ln, n.module))
        elif isinstance(n, ast.Name) and (n.id in BAD_NAMES or n.id == "__builtins__"):
            bad.append("line %d: name %s is not allowed" % (ln, n.id))
        elif isinstance(n, ast.Attribute):
            d = dotted(n)
            if n.attr.startswith("__"):
                bad.append("line %d: dunder attribute %s" % (ln, n.attr))
            elif n.attr in BAD_ATTRS:
                bad.append("line %d: attribute .%s can write or run outside the render folder" % (ln, n.attr))
            elif d and d.startswith("sys.") and d != "sys.argv":
                bad.append("line %d: only sys.argv may be used from sys (%s)" % (ln, d))
            elif d and (d.startswith(BAD_PREFIX) or d.startswith("bpy.ops.wm.") and d.split(".")[3] not in WM_OK):
                bad.append("line %d: %s is not allowed" % (ln, d))
        elif isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 1 and PATHISH.search(n.value):
            if not (rdir and os.path.isabs(n.value) and inside(rdir, n.value)):
                bad.append("line %d: path-like string %r (paths come from --out-dir/--subject only)" % (ln, n.value[:60]))
    return sorted(set(bad), key=lambda s: int(re.search(r"line (\d+)", s).group(1)))


def cmd_check(a):
    p = a.script
    if not os.path.isfile(p):
        print("no such script: %s" % p)
        return 2
    bad = check_source(open(p, encoding="utf-8").read(), render_dir(a.project))
    if bad:
        print("REFUSED %s" % p)
        for b in bad[:30]:
            print("  " + b)
        return 2
    print("OK %s (allowed imports only, no exec/eval/open, no paths outside the render folder)" % p)
    return 0


# ---------------------------------------------------------------- generator
PALETTES = {  # hero, rim, key, bg top, bg bottom (linear RGB)
    "warm": ((0.90, 0.42, 0.08), (0.25, 0.55, 1.0), (1.0, 0.92, 0.80), (0.10, 0.15, 0.32), (0.015, 0.025, 0.07)),
    "cool": ((0.08, 0.55, 0.90), (1.0, 0.50, 0.15), (0.90, 0.95, 1.0), (0.30, 0.10, 0.28), (0.05, 0.02, 0.07)),
    "comp": ((0.85, 0.18, 0.22), (0.15, 0.90, 0.55), (1.0, 0.95, 0.90), (0.04, 0.22, 0.22), (0.01, 0.04, 0.05)),
}
RECIPES = {  # size, focal, margin, az, el, tilt, shift_x, shift_y, dof_fstop, face_light, secondary, ground, variants
    "icon": dict(size="icon", focal=55, margin=1.15, az=30, el=18, tilt=0, sx=0, sy=0, dof=0, face=False, second=False, ground=False, variants=["transparent", "gradient", "comp"]),
    "portrait": dict(size="portrait", focal=80, margin=1.3, az=15, el=3, tilt=0, sx=0, sy=0, dof=4.0, face=True, second=False, ground=False, variants=["gradient"]),
    "action": dict(size="thumb", focal=28, margin=1.5, az=20, el=-10, tilt=10, sx=0.17, sy=-0.08, dof=0, face=False, second=False, ground=True, variants=["gradient"]),
    "scene": dict(size="thumb", focal=40, margin=1.5, az=25, el=8, tilt=0, sx=0.17, sy=-0.08, dof=0, face=False, second=True, ground=True, variants=["gradient"]),
    "variants": dict(size="thumb", focal=40, margin=1.5, az=25, el=8, tilt=0, sx=0.17, sy=-0.08, dof=0, face=False, second=True, ground=True, variants=["warm", "cool", "comp"]),
}

HEADER = '''# SPDX-License-Identifier: GPL-2.0-or-later
# Roblox Dev Mastery Vault, rbx-thumbnail/scripts/blender_gfx.py: generated Blender script (recipe %(recipe)s). Licence: GPL-2.0-or-later, as blender.org
# requires for published scripts that use the Blender API. Renders you make with it are yours. Written from the Blender manual, UNTESTED LIVE.
# Run only through blender_gfx.py run (headless, factory settings, output limited to the render folder).
'''

BODY = r'''
import bpy
import sys
import math
from mathutils import Vector

TARGET = %(target)r
EEVEE_IDS = %(eevee)r
COMP_GROUP = %(group)r
OBJ_OLD = %(objold)r
P = %(params)s


def args():
    a = sys.argv
    t = a[a.index("--") + 1:] if "--" in a else []
    d = {}
    i = 0
    while i < len(t):
        if t[i].startswith("--") and i + 1 < len(t):
            d[t[i][2:]] = t[i + 1]
            i += 2
        else:
            i += 1
    return d


def set_engine(sc, want):
    names = {"EEVEE": EEVEE_IDS, "CYCLES": ("CYCLES",)}[want]
    for n in names:
        try:
            sc.render.engine = n
            break
        except TypeError:
            continue
    return sc.render.engine


def quality(sc, n, limit):
    n = max(1, min(int(n), 256))
    if sc.render.engine == "CYCLES":
        sc.cycles.device = "CPU"
        sc.cycles.samples = n
        sc.cycles.use_denoising = True
        sc.cycles.time_limit = int(limit)
    else:
        sc.eevee.taa_render_samples = n


def bounds(objs):
    pts = [o.matrix_world @ Vector(c) for o in objs if o.type == "MESH" for c in o.bound_box]
    lo = Vector(map(min, zip(*pts)))
    hi = Vector(map(max, zip(*pts)))
    return (lo + hi) / 2, (hi - lo).length / 2


def material(name, color, rough=0.45, emit=0.0):
    m = bpy.data.materials.new(name)
    if TARGET[0] < 5:
        m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (color[0], color[1], color[2], 1)
    b.inputs["Roughness"].default_value = rough
    if emit:
        sk = "Emission Color" if "Emission Color" in b.inputs else "Emission"
        b.inputs[sk].default_value = (color[0], color[1], color[2], 1)
        b.inputs["Emission Strength"].default_value = emit
    return m


def paint(objs, color, flat):
    parts = flat if flat else None
    for i, o in enumerate(objs):
        if o.type != "MESH":
            continue
        c = parts[i %% len(parts)] if parts else color
        o.data.materials.clear()
        o.data.materials.append(material("hero_mat_%%d" %% i, c))


def outline(o, thick=0.02):
    mod = o.modifiers.new("ol", "SOLIDIFY")
    mod.thickness = -thick
    mod.offset = 1
    mod.use_flip_normals = True
    mod.material_offset = 1
    m = material("ol_mat", (0.0, 0.0, 0.0), emit=1.0)
    try:
        m.use_backface_culling = True
    except AttributeError:
        pass
    o.data.materials.append(m)


def world_gradient(sc, top, bottom):
    w = bpy.data.worlds.new("w")
    sc.world = w
    if TARGET[0] < 5:
        w.use_nodes = True
    n, l = w.node_tree.nodes, w.node_tree.links
    n.clear()
    tc = n.new("ShaderNodeTexCoord")
    sep = n.new("ShaderNodeSeparateXYZ")
    ramp = n.new("ShaderNodeValToRGB")
    bg = n.new("ShaderNodeBackground")
    out = n.new("ShaderNodeOutputWorld")
    ramp.color_ramp.elements[0].color = (bottom[0], bottom[1], bottom[2], 1)
    ramp.color_ramp.elements[1].color = (top[0], top[1], top[2], 1)
    l.new(tc.outputs["Window"], sep.inputs["Vector"])
    l.new(sep.outputs["Y"], ramp.inputs["Fac"])
    l.new(ramp.outputs["Color"], bg.inputs["Color"])
    l.new(bg.outputs["Background"], out.inputs["Surface"])


def glow(sc):
    try:
        if COMP_GROUP:
            tree = bpy.data.node_groups.new("c", "CompositorNodeTree")
            sc.compositing_node_group = tree
        else:
            sc.use_nodes = True
            tree = sc.node_tree
            tree.nodes.clear()
        n, l = tree.nodes, tree.links
        rl = n.new("CompositorNodeRLayers")
        gl = n.new("CompositorNodeGlare")
        co = n.new("CompositorNodeComposite")
        l.new(rl.outputs["Image"], gl.inputs["Image"])
        l.new(gl.outputs["Image"], co.inputs["Image"])
        print("GLOW on")
    except Exception as e:
        print("GLOW skipped: %%s" %% e)


def import_model(path):
    ext = path.lower().rsplit(".", 1)[-1]
    if ext == "obj":
        if OBJ_OLD:
            bpy.ops.import_scene.obj(filepath=path)
        else:
            bpy.ops.wm.obj_import(filepath=path)
    elif ext == "fbx":
        bpy.ops.import_scene.fbx(filepath=path)
    else:
        bpy.ops.import_scene.gltf(filepath=path)
    return [o for o in bpy.context.selected_objects if o.type == "MESH"]


def primitive(kind):
    r = 1.0
    if kind == "sphere":
        bpy.ops.mesh.primitive_uv_sphere_add(radius=r, segments=48, ring_count=24)
    elif kind == "cone":
        bpy.ops.mesh.primitive_cone_add(radius1=r, depth=2 * r, vertices=48)
    elif kind == "cylinder":
        bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=2 * r, vertices=48)
    elif kind == "torus":
        bpy.ops.mesh.primitive_torus_add(major_radius=r, minor_radius=0.35 * r)
    elif kind == "gem":
        bpy.ops.mesh.primitive_ico_sphere_add(radius=r, subdivisions=1)
    else:
        bpy.ops.mesh.primitive_cube_add(size=1.6 * r)
    o = bpy.context.active_object
    if kind in ("cube", "gem"):
        mod = o.modifiers.new("bv", "BEVEL")
        mod.width = 0.08
        mod.segments = 3
    o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
    return o


def build_subject(a):
    if P["subject"] == "model":
        objs = import_model(a["subject"])
        if not objs:
            raise RuntimeError("no mesh objects in the imported model")
        c, r = bounds(objs)
        s = 1.0 / max(r, 1e-6)
        root = bpy.data.objects.new("hero_root", None)
        bpy.context.scene.collection.objects.link(root)
        for o in objs:
            if o.parent is None:
                o.parent = root
        root.scale = (s, s, s)
        root.location = -c * s
        bpy.context.view_layer.update()
    else:
        objs = [primitive(P["subject"])]
    for i, o in enumerate(objs):
        o.name = "hero_%%d" %% i
    return objs


def drop(prefixes):
    for o in list(bpy.data.objects):
        if o.name.split("_")[0] in prefixes:
            bpy.data.objects.remove(o, do_unlink=True)


def light(sc, kind, name, loc, target, energy, size, color):
    ld = bpy.data.lights.new(name, kind)
    ld.energy = energy
    ld.color = color
    if kind == "AREA":
        ld.size = size
    else:
        ld.shadow_soft_size = size
    o = bpy.data.objects.new("lt_" + name, ld)
    o.location = loc
    sc.collection.objects.link(o)
    o.rotation_euler = (target - Vector(loc)).to_track_quat("-Z", "Y").to_euler()


def rig(sc, centre, radius, key, rim, face):
    d = radius * 3.0
    E = lambda base: base * d * d
    light(sc, "AREA", "key", centre + Vector((-d * .7, -d * .8, d * .6)), centre, E(60), radius * 2, key)
    light(sc, "AREA", "fill", centre + Vector((d * .9, -d * .6, d * .1)), centre, E(20), radius * 3, (1, 1, 1))
    light(sc, "AREA", "rim", centre + Vector((d * .4, d * .9, d * .5)), centre, E(90), radius * 1.5, rim)
    if face:
        light(sc, "POINT", "face", centre + Vector((-d * .3, -d * .9, d * .1)), centre, E(30), 0.5, key)


def camera(sc, centre, radius, R, w, h, az_add):
    cd = bpy.data.cameras.new("cam")
    cd.lens = P["focal"]
    cd.shift_x, cd.shift_y = R["sx"], R["sy"]
    cam = bpy.data.objects.new("cam_main", cd)
    sc.collection.objects.link(cam)
    sc.camera = cam
    fov = 2 * math.atan(cd.sensor_width / (2 * cd.lens))
    if h > w:
        fov = 2 * math.atan(math.tan(fov / 2) * w / h)
    elif h < w:
        fov = 2 * math.atan(math.tan(fov / 2) * h / w)
    dist = radius * R["margin"] / math.sin(fov / 2)
    a, e = math.radians(R["az"] + az_add), math.radians(R["el"])
    cam.location = centre + Vector((math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e))) * dist
    cam.rotation_euler = (centre - cam.location).to_track_quat("-Z", "Y").to_euler()
    cam.rotation_euler.rotate_axis("Z", math.radians(R["tilt"]))
    return cam


def extras(sc, hero, cam, centre, radius, R, color):
    if R["ground"]:
        bpy.ops.mesh.primitive_plane_add(size=radius * 40, location=(centre.x, centre.y, centre.z - radius))
        bpy.context.active_object.name = "bg_ground"
        bpy.context.active_object.data.materials.append(material("ground", (color[0] * .25, color[1] * .25, color[2] * .25), rough=0.8))
    if R["second"]:
        right = cam.matrix_world.to_quaternion() @ Vector((1, 0, 0))
        bpy.ops.mesh.primitive_uv_sphere_add(radius=radius * .45, location=centre + right * radius * 2.6 + Vector((0, 0, -radius * .4)))
        bpy.context.active_object.name = "bg_second"
        bpy.context.active_object.data.materials.append(material("second", (color[2] * .3 + .3, .3, .3), emit=1.5))


def pose():
    for k, v in P["pose"].items():
        for o in bpy.data.objects:
            if o.name.startswith(k):
                o.rotation_euler = (o.rotation_euler[0] + math.radians(v[0]), o.rotation_euler[1] + math.radians(v[1]), o.rotation_euler[2] + math.radians(v[2]))


def main():
    a = args()
    out_dir = a.get("out-dir")
    if not out_dir:
        raise RuntimeError("--out-dir is required")
    R = P["recipe_cfg"]
    w, h = P["size"]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    want = "CYCLES" if a.get("engine", "eevee").lower() == "cycles" else "EEVEE"
    set_engine(sc, want)
    quality(sc, a.get("samples", 64), a.get("time-limit", 120))
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = w, h, 100
    sc.render.image_settings.file_format = "PNG"
    if P["glow"]:
        glow(sc)
    hero = build_subject(a)
    if P["flat"] or P["subject"] != "model":
        paint(hero, P["hero_color"], P["flat"])
    if P["outline"]:
        for o in hero:
            outline(o)
    pose()
    centre, radius = bounds(hero)
    print("SCENE heroes=%%d radius=%%.3f engine=%%s version=%%s" %% (len(hero), radius, sc.render.engine, ".".join(map(str, bpy.app.version))))
    for v in P["variants"]:
        drop(("lt", "cam", "bg"))
        pal = PAL[v] if v in PAL else PAL[P["palette"]]
        if v in PAL and not P["flat"] and not P["hero_set"] and P["subject"] != "model":
            paint(hero, pal[0], None)
        transparent = v == "transparent"
        sc.render.film_transparent = transparent
        sc.render.image_settings.color_mode = "RGBA" if transparent else "RGB"
        if not transparent:
            world_gradient(sc, pal[3], pal[4])
        cam = camera(sc, centre, radius, R, w, h, 0 if v != "variants" else 0)
        if R["dof"]:
            cam.data.dof.use_dof = True
            cam.data.dof.focus_object = hero[0]
            cam.data.dof.aperture_fstop = R["dof"]
        rig(sc, centre, radius, pal[2], pal[1], R["face"])
        extras(sc, hero, cam, centre, radius, R, pal[0])
        path = "%%s/%%s_%%s.png" %% (out_dir, P["name"], v)
        sc.render.filepath = path
        bpy.ops.render.render(write_still=True)
        print("RESULT %%s %%d %%d" %% (path, w, h))
    if w > h:
        print("SAFE_ZONE bottom 15 percent of the frame is kept free of key content (player-count overlay)")


PAL = %(pal)s
main()
'''


def parse_hex(s):
    s = s.lstrip("#")
    srgb = [int(s[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [round(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4, 4) for c in srgb]


def build_script(cfg, ver):
    target = (ver[0], ver[1])
    if (4, 2) <= target < (5, 0):
        eevee = ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE")
    else:
        eevee = ("BLENDER_EEVEE", "BLENDER_EEVEE_NEXT")
    R = RECIPES[cfg["recipe"]]
    w, h = cfg["size_wh"]
    params = dict(subject="model" if cfg["subject_path"] else cfg["subject"].split(":", 1)[-1], name=cfg["name"], size=[w, h], focal=cfg["focal"] or R["focal"],
                  palette=cfg["palette"], hero_color=cfg["hero_color"], hero_set=cfg["hero_set"], flat=cfg["flat"], outline=cfg["outline"], glow=cfg["glow"], pose=cfg["pose"],
                  variants=cfg["variants"], recipe_cfg=dict(R))
    pal = {k: [list(x) for x in v] for k, v in PALETTES.items()}
    pal["transparent"] = pal[cfg["palette"]]
    pal["gradient"] = pal[cfg["palette"]]
    src = HEADER % {"recipe": cfg["recipe"]} + BODY % dict(target=target, eevee=eevee, group=target >= (5, 0), objold=target < (3, 2),
                                                       params=repr(params), pal=repr(pal))
    return src


def load_brief(a):
    cfg = {}
    if a.brief:
        cfg = json.load(open(a.brief, encoding="utf-8"))
    for k in ("recipe", "subject", "name", "project", "size", "palette", "hero_color", "flat_color", "focal", "blender_version"):
        v = getattr(a, k, None)
        if v not in (None, ""):
            cfg[k] = v
    for k in ("outline", "glow"):
        if getattr(a, k, False):
            cfg[k] = True
    if a.pose:
        cfg["pose"] = a.pose
    return cfg


def cmd_gen(a):
    c = load_brief(a)
    recipe = c.get("recipe", "icon")
    if recipe not in RECIPES:
        print("unknown recipe %r (icon, portrait, action, scene, variants)" % recipe)
        return 2
    name = str(c.get("name") or "gfx")
    if not NAME_RX.match(name):
        print("--name must be letters, digits, - or _ (max 40)")
        return 2
    project = os.path.realpath(c.get("project") or os.getcwd())
    rdir = render_dir(project)
    R = RECIPES[recipe]
    size = c.get("size") or R["size"]
    if size in SIZES:
        w, h = SIZES[size]
    else:
        m = re.match(r"^(\d{3,4})x(\d{3,4})$", str(size))
        if not m:
            print("--size must be icon, thumb, portrait or WxH")
            return 2
        w, h = int(m.group(1)), int(m.group(2))
    if not (512 <= w <= 4096 and 512 <= h <= 4096):
        print("size %dx%d is outside 512..4096 per side (icons need at least 512)" % (w, h))
        return 2
    subj = str(c.get("subject") or "primitive:gem")
    spath = None
    if subj.startswith("primitive:"):
        if subj.split(":", 1)[1] not in PRIMS:
            print("primitive must be one of: " + ", ".join(PRIMS))
            return 2
    else:
        spath = os.path.realpath(subj)
        if not os.path.isfile(spath) or spath.rsplit(".", 1)[-1].lower() not in MODEL_EXT:
            print("subject must be an existing .obj, .fbx, .glb or .gltf file")
            return 2
        if not inside(project, spath):
            print("copy the model into the project folder first (models are read only from inside the project): " + spath)
            return 2
    pal = c.get("palette") or "warm"
    if pal not in PALETTES:
        print("palette must be warm, cool or comp")
        return 2
    for k in ("hero_color", "flat_color"):
        if c.get(k) and not all(HEX_RX.match(x) for x in str(c[k]).split(",")):
            print("--%s must be RRGGBB (flat-color: comma list)" % k.replace("_", "-"))
            return 2
    hero = parse_hex(c["hero_color"]) if c.get("hero_color") else list(PALETTES[pal][0])
    flat = [parse_hex(x) for x in str(c["flat_color"]).split(",")] if c.get("flat_color") else None
    pose = {}
    for item in ([c["pose"]] if isinstance(c.get("pose"), str) else c.get("pose") or []):
        m = re.match(r"^([A-Za-z0-9_]+)=(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)$", item)
        if not m:
            print("--pose part=rx,ry,rz (degrees)")
            return 2
        pose[m.group(1)] = [float(m.group(i)) for i in (2, 3, 4)]
    ver = parse_version(str(c.get("blender_version") or "")) or None
    if not ver:
        exe = find_blender()
        ver = (blender_version(exe) if exe else None) or (4, 5, 0)
    cfg = dict(recipe=recipe, subject=subj, subject_path=spath, name=name, size_wh=(w, h), palette=pal, hero_color=hero, hero_set=bool(c.get("hero_color")), flat=flat, focal=float(c["focal"]) if c.get("focal") else 0,
               outline=bool(c.get("outline")), glow=bool(c.get("glow")), pose=pose, variants=list(R["variants"]))
    src = build_script(cfg, ver)
    bad = check_source(src, rdir)
    if bad:
        print("internal error: generated script fails check: " + "; ".join(bad[:3]))
        return 1
    sdir = os.path.join(rdir, "_scripts")
    os.makedirs(sdir, exist_ok=True)
    sp = os.path.join(sdir, "%s_%s.py" % (name, recipe))
    open(sp, "w", encoding="utf-8", newline="\n").write(src)
    side = dict(recipe=recipe, name=name, size=[w, h], subject=subj, subject_path=spath, target_version=list(ver[:2]), variants=cfg["variants"], engine="eevee", samples=CAPS["eevee"],
                outputs=["%s_%s.png" % (name, v) for v in cfg["variants"]], safe_zone="bottom 15 percent free" if w > h else "n/a (square)",
                script_sha256=hashlib.sha256(src.encode()).hexdigest())
    json.dump(side, open(sp[:-3] + ".json", "w", encoding="utf-8"), indent=1)
    print("script: " + sp)
    print("next: blender_gfx.py run \"%s\" --project \"%s\"" % (sp, project))
    return 0


# ---------------------------------------------------------------- runner
def png_info(p):
    try:
        with open(p, "rb") as f:
            head = f.read(33)
        if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
            return None
        return struct.unpack(">II", head[16:24])
    except OSError:
        return None


def kill_tree(proc):
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True)
    else:
        try:
            os.killpg(proc.pid, 9)
        except OSError:
            proc.kill()


def attempt(exe, script, rdir, engine, samples, subject, timeout, offline):
    cmd = [exe, "-b", "--factory-startup"] + (["--offline-mode"] if offline else []) + ["--python-exit-code", "1", "-P", script, "--",
           "--out-dir", rdir, "--engine", engine, "--samples", str(samples), "--time-limit", "120"] + (["--subject", subject] if subject else [])
    kw = {} if os.name == "nt" else {"start_new_session": True}
    proc = subprocess.Popen(cmd, cwd=rdir, env=clean_env(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace", **kw)
    try:
        out, err = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        kill_tree(proc)
        try:
            proc.communicate(timeout=10)
        except subprocess.SubprocessError:
            pass
        return False, [], "timed out after %d s" % timeout, cmd
    if proc.returncode != 0:
        return False, [], "exit code %s: %s" % (proc.returncode, (err or out).strip()[-300:]), cmd
    res, notes = [], []
    for ln in out.splitlines():
        m = re.match(r"^RESULT (.+) (\d+) (\d+)$", ln)
        if not m:
            continue
        p = m.group(1)
        info = png_info(p) if inside(rdir, p) else None
        if info and info == (int(m.group(2)), int(m.group(3))) and os.path.getsize(p) > 1024:
            res.append((p, info))
        else:
            notes.append("rejected output " + p)
    if not res:
        return False, [], "no valid PNG written (%s)" % ("; ".join(notes) or "no RESULT line"), cmd
    return True, res, "", cmd


def cmd_run(a):
    script = os.path.realpath(a.script)
    if not os.path.isfile(script):
        print("no such script: " + a.script)
        return 2
    rdir = render_dir(a.project)
    bad = check_source(open(script, encoding="utf-8").read(), rdir)
    if bad:
        print("REFUSED: script fails the safety check, nothing was run")
        for b in bad[:10]:
            print("  " + b)
        return 2
    exe = find_blender(a.blender)
    if not exe:
        print(MISSING)
        return 3
    side = {}
    try:
        side = json.load(open(script[:-3] + ".json", encoding="utf-8"))
    except (OSError, ValueError):
        pass
    engine = (a.engine or side.get("engine") or "eevee").lower()
    cap = HARD_CAP if a.allow_high else CAPS[engine]
    samples = max(1, min(a.samples or CAPS[engine], cap, HARD_CAP))
    subject = a.subject or side.get("subject_path")
    project = os.path.realpath(a.project or os.getcwd())
    if subject:
        subject = os.path.realpath(subject)
        if not inside(project, subject) or not os.path.isfile(subject) or subject.rsplit(".", 1)[-1].lower() not in MODEL_EXT:
            print("subject must be an existing obj/fbx/glb/gltf file inside the project: " + subject)
            return 2
    os.makedirs(rdir, exist_ok=True)
    try:
        h = subprocess.run([exe, "--help"], capture_output=True, text=True, timeout=60, env=clean_env())
        offline = "--offline-mode" in (h.stdout or "")
    except (OSError, subprocess.SubprocessError):
        offline = False
    ladder = [(engine, samples)] + ([("cycles", 64)] if engine == "eevee" else [])
    last = ""
    for eng, spl in ladder:
        to = min(a.timeout, TIMEOUT[eng]) if a.timeout else TIMEOUT[eng]
        t0 = time.time()
        ok, res, err, cmd = attempt(exe, script, rdir, eng, spl, subject, to, offline)
        if ok:
            for p, (w, hh) in res:
                print("OUTPUT %s %dx%d %d bytes (%s, %d samples, %.0f s)" % (p, w, hh, os.path.getsize(p), eng, spl, time.time() - t0))
                json.dump(dict(script=script, blender=exe, engine=eng, samples=spl, size=[w, hh], when=time.strftime("%Y-%m-%d")), open(p[:-4] + ".json", "w"), indent=1)
            print("next: thumb_score.py inspect <png>, then score each candidate by looking (checklist 'Score and test'); 2-5 variants for personalization")
            return 0
        last = err
        print("%s render failed: %s" % (eng, err))
    print("render failed (no further fallback): " + last)
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("detect")
    d.add_argument("--blender")
    g = sub.add_parser("gen")
    g.add_argument("--recipe")
    g.add_argument("--subject")
    g.add_argument("--name")
    g.add_argument("--project")
    g.add_argument("--size")
    g.add_argument("--palette")
    g.add_argument("--hero-color", dest="hero_color")
    g.add_argument("--flat-color", dest="flat_color")
    g.add_argument("--outline", action="store_true")
    g.add_argument("--glow", action="store_true")
    g.add_argument("--pose", action="append")
    g.add_argument("--focal")
    g.add_argument("--blender-version", dest="blender_version")
    g.add_argument("--brief")
    c = sub.add_parser("check")
    c.add_argument("script")
    c.add_argument("--project")
    r = sub.add_parser("run")
    r.add_argument("script")
    r.add_argument("--project")
    r.add_argument("--engine", choices=("eevee", "cycles"))
    r.add_argument("--samples", type=int)
    r.add_argument("--allow-high", action="store_true")
    r.add_argument("--subject")
    r.add_argument("--timeout", type=int)
    r.add_argument("--blender")
    a = ap.parse_args()
    return {"detect": cmd_detect, "gen": cmd_gen, "check": cmd_check, "run": cmd_run}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
