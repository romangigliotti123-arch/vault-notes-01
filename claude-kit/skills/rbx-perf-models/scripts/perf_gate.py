#!/usr/bin/env python3
"""perf_gate.py: deterministic analyzer of rbx-perf-models. Reads the PERF_* lines printed by perf_run.luau (or a scan .json made from them).

  python perf_gate.py analyze <console.txt | scan.json> [--game NAME] [--write DIR] [--approve RV-SHADOW,RV-ANCHOR]
      DRY RUN. Classifies every part (SAFE / REVIEW / cannot improve), writes DIR/perf-qa/{scan-before.json, plan.json, report.md, perf_apply.luau,
      perf_revert.luau}. SAFE items only change collision/query/touch flags, collision fidelity or remove provably invisible or duplicate parts.
      REVIEW items are only written into the plan when approved by id with --approve.
  python perf_gate.py verify <before scan.json|console.txt> <after console.txt|json> --plan plan.json [--write DIR]
      Appearance diff: every rendering property of every surviving part must be identical (PASS/FAIL per class); behaviour changes must be exactly
      the planned ones; removed parts must be invisible or have an identical twin. Exit 1 on FAIL.
  python perf_gate.py diff   (same as verify)
Python 3 stdlib only. Run with python -I.
"""
import datetime
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNNER = os.path.join(HERE, "perf_run.luau")

DECOR_CLASSES = {"Part", "MeshPart", "UnionOperation", "NegateOperation", "WedgePart", "CornerWedgePart"}
ALLOWED_KIDS = {"Decal", "Texture", "SurfaceAppearance", "SpecialMesh", "BlockMesh", "CylinderMesh", "FileMesh", "PointLight", "SpotLight",
                "SurfaceLight", "ParticleEmitter", "Fire", "Smoke", "Sparkles", "Sound"}
SCRIPT_KIDS = {"Script", "LocalScript", "ModuleScript"}
HOLDER_CLASSES = {"Tool", "Accessory", "Hat", "BackpackItem"}
SPECIAL_PARTS = {"Seat", "VehicleSeat", "SpawnLocation", "TrussPart"}
INTERACTIVE = ("kill", "lava", "damage", "hurt", "trap", "spawn", "checkpoint", "trigger", "zone", "region", "door", "gate", "ladder", "climb", "seat",
               "vehicle", "wheel", "button", "lever", "switch", "pickup", "coin", "collect", "portal", "teleport", "goal", "finish", "hitbox", "sensor",
               "pad", "platform", "elevator", "conveyor", "bounce", "barrier", "wall_invis", "boundary", "npc", "enemy", "target", "shop", "prompt", "click")
PROP_FIELD = {"CanQuery": "cq", "CanTouch": "ct", "CanCollide": "cc", "Anchored": "anch", "CastShadow": "cs", "CollisionFidelity": "cfid", "RenderFidelity": "rfid"}
BOOL_PROPS = {"CanQuery", "CanTouch", "CanCollide", "Anchored", "CastShadow"}
VISUAL_FIELDS = ["cls", "name", "pid", "tr", "rf", "mat", "mv", "col", "shape", "sx", "sy", "sz", "cf", "rfid", "meshid", "texid", "kids", "tags", "attrs", "ksig", "cs"]
BEHAVIOUR_FIELDS = ["anch", "cc", "cq", "ct", "ml", "cfid"]
VISUAL_PROP_NAMES = {"CastShadow", "RenderFidelity"}
UNDO = "Undo in one step: press Ctrl+Z in Studio (Edit > Undo 'PerfPass: applied'), or run perf_revert.luau from the same folder."


# ---------------------------------------------------------------- parsing
LINE = re.compile(r"(PERF_SCAN|PERF_P|PERF_C|PERF_END|PERF_APPLY|PERF_REVERT)\s+(\{.*\})\s*$")


def parse_console(text):
    """-> dict phase -> dump {head, parts, containers, complete}; plus 'apply' (PERF_APPLY object) and 'appearance' (lines)."""
    dumps, cur, apply_info, appearance, revert = {}, None, None, [], None
    for ln in text.splitlines():
        if re.search(r"APPEARANCE (DIFF|\w+) ?(PASS|FAIL)", ln):
            appearance.append(ln.strip())
        m = LINE.search(ln)
        if not m:
            continue
        try:
            obj = json.loads(m.group(2))
        except ValueError:
            continue
        tag = m.group(1)
        if tag == "PERF_SCAN":
            cur = dict(head=obj, parts=[], containers=[], complete=False)
            dumps[obj.get("phase", "before")] = cur
        elif tag in ("PERF_P", "PERF_C") and cur is not None:
            f = cur["head"]["fieldsP" if tag == "PERF_P" else "fieldsC"]
            for row in obj["rows"]:
                (cur["parts"] if tag == "PERF_P" else cur["containers"]).append(dict(zip(f, row)))
        elif tag == "PERF_END" and cur is not None:
            cur["complete"] = obj.get("nparts") == len(cur["parts"]) == cur["head"].get("nparts") and obj.get("ncontainers") == len(cur["containers"])
        elif tag == "PERF_APPLY":
            apply_info = obj
        elif tag == "PERF_REVERT":
            revert = obj
    dumps["apply"], dumps["appearance"], dumps["revert"] = apply_info, appearance, revert
    return dumps


def load_scan(path, phase="before"):
    text = open(path, encoding="utf-8-sig", errors="replace").read()
    if text.lstrip().startswith("{"):
        try:
            obj = json.loads(text)
            if isinstance(obj, dict) and obj.get("kind") == "perf-scan":
                return obj
        except ValueError:
            pass
    d = parse_console(text)
    if phase not in d or not isinstance(d[phase], dict):
        sys.exit("no PERF_SCAN (%s) block found in %s (did you save the whole Output text?)" % (phase, path))
    x = d[phase]
    if not x["complete"]:
        sys.exit("the %s scan in %s is incomplete (PERF_END missing or row counts differ): the Output was truncated; save the full Output and retry" % (phase, path))
    return dict(kind="perf-scan", head=x["head"], parts=x["parts"], containers=x["containers"], apply=d["apply"], appearance=d["appearance"], revert=d["revert"])


# ---------------------------------------------------------------- model of the scanned game
def aslist(x):
    """An empty Lua table may arrive as {} (some JSON encoders): treat it as an empty list."""
    return x if isinstance(x, list) else []


class World:
    def __init__(self, scan):
        self.head = scan["head"]
        self.parts = {p["id"]: p for p in scan["parts"]}
        self.nodes = dict(self.parts)
        for c in scan["containers"]:
            self.nodes[c["id"]] = c
        self.kids = {i: set(filter(None, (n.get("kids") or "").split(","))) for i, n in self.nodes.items()}
        self.children = {}
        for i, n in self.nodes.items():
            self.children.setdefault(n["pid"], []).append(i)
        self.refnames = set(aslist(self.head.get("refnames")))
        self.joint = set(aslist(self.head.get("jointRefs")))
        sc = self.head.get("scripts") or {"n": 0, "unreadable": 0}
        self.scripts_ok = sc.get("unreadable", 0) == 0
        self.complete = not self.head.get("capped")
        self.ex = set()
        self._build_exclusions()

    def ancestors(self, i):
        out, seen = [], set()
        p = self.nodes[i]["pid"]
        while p and p in self.nodes and p not in seen:
            seen.add(p)
            out.append(p)
            p = self.nodes[p]["pid"]
        return out

    def path(self, i):
        names = [self.nodes[a]["name"] for a in reversed(self.ancestors(i))] + [self.nodes[i]["name"]]
        return "/".join(names)

    def subtree(self, i):
        out, stack = [], [i]
        while stack:
            x = stack.pop()
            out.append(x)
            stack.extend(self.children.get(x, []))
        return out

    def _build_exclusions(self):
        for i, n in self.nodes.items():
            k = self.kids[i]
            if (k & SCRIPT_KIDS) or "Humanoid" in k or n["cls"] in HOLDER_CLASSES or n.get("tags", 0) or n.get("attrs", 0) and i not in self.parts:
                self.ex.update(self.subtree(i))
            if n["cls"] in SPECIAL_PARTS:
                par = n["pid"]
                self.ex.update(self.subtree(par) if par in self.nodes else [i])
                self.ex.add(i)
            if "Humanoid" in k:
                self.ex.update(self.subtree(i))

    def referenced(self, i):
        names = [self.nodes[i]["name"]] + [self.nodes[a]["name"] for a in self.ancestors(i)]
        return any(n in self.refnames for n in names)

    def decor(self, i):
        """-> (ok, reason). The exact decorative rule (references/rules.md, D1-D8)."""
        n = self.parts[i]
        if not self.complete:
            return False, "scan was capped"
        if not self.scripts_ok:
            return False, "scripts could not be read"
        if n["cls"] not in DECOR_CLASSES:
            return False, "class " + n["cls"]
        if not self.kids[i] <= ALLOWED_KIDS:
            return False, "has children " + ",".join(sorted(self.kids[i] - ALLOWED_KIDS))
        if n.get("tags") or n.get("attrs"):
            return False, "tagged or has attributes"
        if i in self.joint:
            return False, "referenced by a weld, constraint, PrimaryPart or value"
        if i in self.ex:
            return False, "inside a scripted, character, tool, seat or tagged container"
        if self.referenced(i):
            return False, "name used by a script"
        low = " ".join([n["name"]] + [self.nodes[a]["name"] for a in self.ancestors(i)]).lower()
        hit = [w for w in INTERACTIVE if w in low]
        if hit:
            return False, "interactive-looking name (%s)" % hit[0]
        return True, ""


# ---------------------------------------------------------------- geometry
def _rot(cf):
    return [cf[3:6], cf[6:9], cf[9:12]]


def contained(b, a, eps=0.01):
    """True when every corner of b's bounding box lies inside a's box (a: Block Part)."""
    ca, cb = a["cf"], b["cf"]
    ra, rb = _rot(ca), _rot(cb)
    ha = (a["sx"] / 2, a["sy"] / 2, a["sz"] / 2)
    hb = (b["sx"] / 2, b["sy"] / 2, b["sz"] / 2)
    for sx in (-1, 1):
        for sy in (-1, 1):
            for sz in (-1, 1):
                loc = (sx * hb[0], sy * hb[1], sz * hb[2])
                w = [cb[k] + sum(rb[k][j] * loc[j] for j in range(3)) for k in range(3)]
                d = [w[k] - ca[k] for k in range(3)]
                for j in range(3):
                    t = sum(ra[k][j] * d[k] for k in range(3))
                    if abs(t) > ha[j] - eps:
                        return False
    return True


# ---------------------------------------------------------------- cost estimate (relative units, ESTIMATE)
FID_COST = {"Box": 1, "Hull": 2, "Default": 4, "Precise": 8, "": 1}


def estimate(world, state, removed):
    phys = mem = 0.0
    draw = set()
    vis = shadows = 0
    for i, p in world.parts.items():
        if i in removed:
            continue
        s = state.get(i, p)
        phys += (1 if s["cc"] else 0) + (0.5 if s["cq"] else 0) + (0.25 if s["ct"] else 0) + (0 if s["anch"] else 4)
        mem += FID_COST.get(s["cfid"], 2) if s["cls"] in ("MeshPart", "UnionOperation", "NegateOperation") else 1
        if p["tr"] < 1:
            vis += 1
            shadows += 1 if s["cs"] else 0
            draw.add((p["mat"], p["mv"], p["meshid"], p["texid"], bool(p["kids"]), p["cls"] == "MeshPart"))
    return dict(parts=len(world.parts) - len(removed), physicsUnits=round(phys, 1), collisionMemUnits=round(mem, 1), drawBatchesProxy=len(draw), visibleParts=vis, shadowCasters=shadows)


# ---------------------------------------------------------------- classification
def classify(world, approve=()):
    P = world.parts
    state = {i: dict(p) for i, p in P.items()}  # effective state after SAFE
    changes = []  # (rule, id, prop, from, to)
    removed = {}  # id -> rule
    dec = {i: world.decor(i) for i in P}
    blocked = {}  # reason -> count

    def setp(rule, i, prop, new):
        f = PROP_FIELD[prop]
        old = state[i][f]
        if prop in BOOL_PROPS:
            frm, to = bool(old), bool(new)
        else:
            frm, to = old, new
        changes.append((rule, i, prop, frm, to))
        state[i][f] = int(new) if prop in BOOL_PROPS else new

    for i in P:
        ok, why = dec[i]
        if not ok:
            blocked[why] = blocked.get(why, 0) + 1
    # S5 invisible leftovers
    for i, p in P.items():
        if dec[i][0] and not world.kids[i] and p["tr"] >= 0.999 and not p["cc"] and (not p["ct"] or not world.head.get("bulkTouch")) and (not p["cq"] or not world.head.get("queryApi")):
            removed[i] = "S5"
    # S6 identical coincident opaque duplicates
    groups = {}
    for i, p in P.items():
        if i in removed or not dec[i][0] or world.kids[i] or p["tr"] != 0 or not p["anch"]:
            continue
        key = (p["cls"], p["shape"], p["sx"], p["sy"], p["sz"], tuple(round(v, 3) for v in p["cf"]), p["mat"], p["mv"], p["col"], p["rf"], p["cs"], p["ml"],
               p["anch"], p["cc"], p["cq"], p["ct"], p["cfid"], p["rfid"], p["meshid"], p["texid"])
        groups.setdefault(key, []).append(i)
    for ids in groups.values():
        for i in sorted(ids)[1:]:
            removed[i] = "S6"
    # S4 hidden inside a bigger solid block
    cell = 32.0
    grid = {}
    for i, p in P.items():
        if i in removed or p["cls"] != "Part" or p["shape"] != "Block" or not p["anch"] or not p["cc"] or not dec[i][0]:
            continue
        r = 0.5 * math.sqrt(p["sx"] ** 2 + p["sy"] ** 2 + p["sz"] ** 2)
        x, y, z = p["cf"][0], p["cf"][1], p["cf"][2]
        for cx in range(int((x - r) // cell), int((x + r) // cell) + 1):
            for cy in range(int((y - r) // cell), int((y + r) // cell) + 1):
                for cz in range(int((z - r) // cell), int((z + r) // cell) + 1):
                    grid.setdefault((cx, cy, cz), []).append(i)
    for i in sorted(P):
        p = P[i]
        if i in removed or not p["anch"] or not state[i]["cc"] or not dec[i][0]:
            continue
        key = (int(p["cf"][0] // cell), int(p["cf"][1] // cell), int(p["cf"][2] // cell))
        for a in grid.get(key, []):
            if a != i and state[a]["cc"] and a not in removed and contained(p, P[a]):
                setp("S4", i, "CanCollide", False)
                break
    # S2 / S3 / S7
    for i, p in P.items():
        if i in removed or not dec[i][0]:
            continue
        s = state[i]
        if not p["anch"]:
            continue
        if s["cc"] == 0 and s["cq"] == 1:
            if not world.head.get("queryApi"):
                setp("S2", i, "CanQuery", False)
        if s["ct"] == 1:
            if not world.head.get("bulkTouch"):
                setp("S3", i, "CanTouch", False)
        if p["cls"] in ("MeshPart", "UnionOperation", "NegateOperation") and s["cfid"] not in ("Box", "") and not s["cc"] and not s["cq"] and not s["ct"]:
            setp("S7", i, "CollisionFidelity", "Box")
    safe_state = {i: dict(s) for i, s in state.items()}

    # ---- REVIEW (never applied without --approve)
    review = []

    def maxdim(p):
        return max(p["sx"], p["sy"], p["sz"])

    def add(code, title, risk, ids_props, note, auto=True):
        review.append(dict(id="RV-" + code, title=title, risk=risk, count=len(ids_props), items=ids_props, note=note, auto=auto))

    live = [i for i in P if i not in removed]
    sh = [(i, "CastShadow", True, False) for i in live if state[i]["cs"] and P[i]["tr"] < 1 and maxdim(P[i]) <= 2]
    if sh:
        add("SHADOW", "Turn off CastShadow on small parts (largest dimension 2 studs or less)", "visual: those parts stop casting shadows", sh,
            "Roblox docs: may leave visual artifacts on shadows; judge it in the view the player sees.")
    an = [(i, "Anchored", False, True) for i in live if not state[i]["anch"] and i not in world.joint and i not in world.ex and not world.kids[i] - ALLOWED_KIDS
          and not P[i]["tags"] and not P[i]["attrs"] and not world.referenced(i)]
    if an:
        add("ANCHOR", "Anchor parts that are not anchored and have no joints, scripts or tags", "gameplay: they no longer fall, slide or can be pushed", an,
            "Cannot be proven static from edit-time data: a part that rests on the floor may still be a pushable crate or fall at runtime.")
    co = [(i, "CanCollide", True, False) for i in live if dec[i][0] and state[i]["anch"] and state[i]["cc"] and maxdim(P[i]) <= 4]
    if co:
        add("COLLIDE", "Turn off CanCollide on small anchored decorative parts", "gameplay: players walk through them", co,
            "Walk-through foliage and trim are the usual candidates; walls, steps and rails are not.")
    fb, fh, rn = [], [], []
    for i in live:
        s, p = state[i], P[i]
        if p["cls"] in ("MeshPart", "UnionOperation", "NegateOperation") and s["cfid"] in ("Precise", "Default") and s["cc"] and i not in world.ex:
            if s["anch"] and maxdim(p) <= 6:
                fb.append((i, "CollisionFidelity", s["cfid"], "Box"))
            elif s["cfid"] == "Precise":
                fh.append((i, "CollisionFidelity", "Precise", "Hull"))
        if p["cls"] == "MeshPart" and p["rfid"] == "Precise":
            rn.append((i, "RenderFidelity", "Precise", "Automatic"))
    if fb:
        add("FIDELITY-BOX", "Collision shape Box on small anchored meshes and unions", "gameplay: the collision outline gets coarser (docs: generally safe for small anchored parts)", fb, "Box has the lowest memory cost.")
    if fh:
        add("FIDELITY-HULL", "Collision shape Hull instead of Precise on larger meshes", "gameplay: concave shapes (arches, bowls) become filled", fh, "Precise is the most expensive mode.")
    if rn:
        add("RENDER", "RenderFidelity Automatic instead of Precise", "visual: far-away meshes may drop detail sooner", rn, "Official default is Automatic; the detail drop starts at 250 studs.")
    if world.head.get("queryApi"):
        q = [(i, "CanQuery", True, False) for i in live if dec[i][0] and not state[i]["cc"] and state[i]["cq"]]
        if q:
            add("QUERY", "CanQuery off on non-colliding decorative parts (blocked because a script uses raycasts or spatial queries)", "gameplay: rays pass through them", q, "A script in this game queries the world; whether it should see these parts is your call.")
    if world.head.get("bulkTouch"):
        t = [(i, "CanTouch", True, False) for i in live if dec[i][0] and state[i]["ct"]]
        if t:
            add("TOUCH", "CanTouch off on decorative parts (blocked because a script listens to touches broadly)", "gameplay: a broad Touched listener would no longer see them", t, "A script connects Touched on the character or iterates descendants.")
    # manual notes (no automatic action)
    c = world.head.get("counts") or {}
    manual = []
    if c.get("surfaceAppearance") or c.get("textures") or c.get("decals"):
        manual.append(("TEXTURES", "%d SurfaceAppearance, %d Texture, %d Decal" % (c.get("surfaceAppearance", 0), c.get("textures", 0), c.get("decals", 0)),
                       "Downsizing images changes how surfaces look; open the largest ones in the Asset Manager and judge."))
    if c.get("lights"):
        manual.append(("LIGHTS", "%d lights (%d with Shadows on)" % (c["lights"], c.get("lightsShadow", 0)), "Range, Brightness and Shadows are look decisions; each Shadows light is a real GPU cost."))
    if c.get("emitters") or c.get("beams") or c.get("trails") or c.get("fx"):
        manual.append(("PARTICLES", "%d ParticleEmitters (total Rate %s), %d Beams, %d Trails, %d Fire/Smoke/Sparkles" % (c.get("emitters", 0), c.get("emitterRate", 0), c.get("beams", 0), c.get("trails", 0), c.get("fx", 0)),
                       "Lower Rate or Lifetime changes the effect; far-away emitters are the cheapest to cut."))
    st = world.head.get("stats") or {}
    if st.get("streamingEnabled") is False and len(P) >= 2000:
        manual.append(("STREAMING", "StreamingEnabled is off with %d parts" % len(P), "Turning on instance streaming reduces memory on phones but changes when far objects exist: scripts must cope."))
    clusters = {}
    for i in live:
        p = P[i]
        if p["anch"] and p["tr"] < 1 and maxdim(p) <= 4 and p["cls"] == "Part":
            clusters.setdefault((p["mat"], p["col"], p["shape"]), []).append(i)
    big = sorted(((len(v), k) for k, v in clusters.items() if len(v) >= 50), reverse=True)[:3]
    if big:
        manual.append(("MERGE", "; ".join("%d small anchored %s %s parts" % (n, k[0], k[1]) for n, k in big),
                       "Merging into a union or mesh in a modelling tool cuts instance count; it changes how you edit them, not how they look if done right."))
    if c.get("transparent"):
        manual.append(("TRANSPARENT", "%d partly transparent parts" % c["transparent"], "Overdraw cost; changing Transparency changes the look."))
    # cannot improve
    cannot = []
    if c.get("meshParts"):
        top = ", ".join("%s x%d" % (m or "(none)", n) for m, n in aslist(c.get("topMeshIds"))[:3])
        cannot.append("%d MeshParts (%d distinct meshes; most used: %s). Triangle counts are not readable from Luau in Studio: check heavy ones in the Developer Console, simplify them in your modelling tool." % (c["meshParts"], c.get("distinctMeshIds", 0), top or "n/a"))
    if c.get("unions"):
        cannot.append("%d union/negate parts: their render mesh cannot be simplified without rebuilding the shape." % c["unions"])
    if c.get("lights"):
        cannot.append("%d lights stay as they are (every change is a visible change)." % c["lights"])
    if c.get("emitters"):
        cannot.append("%d particle emitters stay as they are." % c["emitters"])
    return dict(changes=changes, removed=removed, review=review, manual=manual, cannot=cannot, blocked=blocked, safe_state=safe_state,
                est_before=estimate(world, {}, set()), est_after=estimate(world, safe_state, set(removed)))


# ---------------------------------------------------------------- plan
def build_plan(world, res, approve):
    groups = {}
    for rule, i, prop, frm, to in res["changes"]:
        groups.setdefault((rule, prop, frm, to, "safe"), []).append(i)
    rem = {}
    for i, rule in res["removed"].items():
        rem.setdefault(rule, []).append(i)
    approved, allow = [], set()
    for rv in res["review"]:
        if rv["id"] in approve and rv["auto"]:
            approved.append(rv["id"])
            for i, prop, frm, to in rv["items"]:
                groups.setdefault((rv["id"], prop, frm, to, "review"), []).append(i)
                if prop in VISUAL_PROP_NAMES:
                    allow.add(prop)
    items = [dict(rule=k[0], prop=k[1], **{"from": k[2], "to": k[3]}, tier=k[4], ids=sorted(v)) for k, v in sorted(groups.items(), key=lambda kv: (kv[0][4] != "safe", kv[0][0], kv[0][1]))]
    n_safe = len([i for i in items if i["tier"] == "safe"])
    removals = [dict(rule=rule, prop="Remove", tier="safe", **{"from": None, "to": None}, ids=sorted(ids)) for rule, ids in sorted(rem.items())]
    items = items[:n_safe] + removals + items[n_safe:]
    return dict(version=1, game=world.head.get("game"), root=world.head.get("root"), fingerprint=world.head.get("fingerprint"), nparts=world.head.get("nparts"),
                approved=approved, allowVisual=sorted(allow), removed=sorted(i for ids in rem.values() for i in ids), items=items)


def lua(v):
    if v is None:
        return "nil"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, str):
        return json.dumps(v)
    if isinstance(v, list):
        return "{" + ",".join(lua(x) for x in v) + "}"
    return "{" + ",".join("[%s]=%s" % (json.dumps(k), lua(x)) for k, x in v.items()) + "}"


def runner_with(plan, mode):
    src = open(RUNNER, encoding="utf-8").read()
    a, b = src.index("-- PLAN-BEGIN"), src.index("-- PLAN-END")
    src = src[:a] + "-- PLAN-BEGIN\nlocal PLAN = " + lua(plan) + "\n" + src[b:]
    src, n = re.subn(r'mode = "scan"', 'mode = "%s"' % mode, src, count=1)
    assert n == 1
    return "-- GENERATED by perf_gate.py from perf_run.luau (mode %s). Run in Studio's command bar or with execute_luau (Edit).\n" % mode + src


def revert_plan(plan, world):
    """Inverse plan. After the apply the removed parts are gone from the tree, so a part with scan id k now sits at k minus the number of removed ids below k;
    the runner does that arithmetic and checks the Class:Name guard of every part instead of the fingerprint."""
    inv = []
    for it in plan["items"]:
        if it["prop"] != "Remove":
            inv.append(dict(rule=it["rule"], prop=it["prop"], tier=it["tier"], ids=it["ids"], **{"from": it["to"], "to": it["from"]}))
    names = {}
    for it in inv:
        for i in it["ids"]:
            n = world.parts[i]
            names[str(i)] = n["cls"] + ":" + n["name"]
    return dict(plan, items=inv, names=names)


# ---------------------------------------------------------------- report
def pct(a, b):
    return "0%" if a == 0 else "%.0f%%" % (100.0 * (a - b) / a)


def gain_of(world, res, rv):
    st = {i: dict(s) for i, s in res["safe_state"].items()}
    for i, prop, frm, to in rv["items"]:
        f = PROP_FIELD[prop]
        st[i][f] = int(to) if prop in BOOL_PROPS else to
    a = estimate(world, res["safe_state"], set(res["removed"]))
    b = estimate(world, st, set(res["removed"]))
    return round(a["physicsUnits"] - b["physicsUnits"] + a["collisionMemUnits"] - b["collisionMemUnits"] + 0.5 * (a["shadowCasters"] - b["shadowCasters"]), 1)


RULES = {"S2": "CanQuery off on decorative non-colliding parts", "S3": "CanTouch off on decorative parts", "S4": "CanCollide off on parts fully hidden inside a bigger solid block",
         "S5": "Move invisible, non-colliding, unreferenced leftover parts to ServerStorage.PerfPass_Removed", "S6": "Move identical opaque duplicates (same place, same everything) to ServerStorage.PerfPass_Removed",
         "S7": "CollisionFidelity Box on meshes/unions that no longer collide, get queried or touched"}


def report(world, res, plan, game, now=None):
    h = world.head
    b, a = res["est_before"], res["est_after"]
    L = []
    L.append("# Performance pass (models): %s" % game)
    L.append("")
    L.append("Dry run. Nothing in your game was changed. Scan of `%s` taken %s: %d parts, %d containers, %s scripts (%s unreadable)." % (
        h.get("root"), h.get("capturedAt", "?"), h["nparts"], h["ncontainers"], (h.get("scripts") or {}).get("n", 0), (h.get("scripts") or {}).get("unreadable", 0)))
    L.append("")
    L.append("## Estimated effect of the SAFE tier (ESTIMATE in relative units, not milliseconds; measure with the MicroProfiler)")
    L.append("")
    L.append("| metric | before | after SAFE | change |")
    L.append("|---|---|---|---|")
    for k, lab in (("parts", "parts in scan"), ("physicsUnits", "physics/query/touch cost units"), ("collisionMemUnits", "collision memory units"), ("drawBatchesProxy", "draw batches proxy (distinct material/mesh/texture combos)"), ("visibleParts", "visible parts"), ("shadowCasters", "shadow-casting visible parts")):
        L.append("| %s | %s | %s | %s |" % (lab, b[k], a[k], pct(b[k], a[k])))
    st = h.get("stats") or {}
    if st:
        L.append("")
        L.append("Studio Stats at scan time: " + ", ".join("%s=%s" % (k, v) for k, v in st.items() if v is not None) + ".")
    L.append("")
    L.append("## SAFE tier (proven: no rendering property and no gameplay behaviour changes)")
    L.append("")
    if not res["changes"] and not res["removed"]:
        L.append("Nothing in this game can be proven safe to change. See the blocked reasons below.")
    else:
        L.append("| rule | what | parts |")
        L.append("|---|---|---|")
        cnt = {}
        for r, *_ in res["changes"]:
            cnt[r] = cnt.get(r, 0) + 1
        for r in res["removed"].values():
            cnt[r] = cnt.get(r, 0) + 1
        for r in sorted(cnt):
            L.append("| %s | %s | %d |" % (r, RULES[r], cnt[r]))
    L.append("")
    if res["blocked"]:
        L.append("Kept as they are (not provably decorative): " + "; ".join("%s: %d" % (k, v) for k, v in sorted(res["blocked"].items(), key=lambda kv: -kv[1])[:6]) + ".")
        L.append("")
    L.append("## REVIEW tier (might change the look or behaviour; never applied unless you approve each id)")
    L.append("")
    ranked = sorted(res["review"], key=lambda r: -gain_of(world, res, r))
    if not ranked and not res["manual"]:
        L.append("No suggestions.")
    for rv in ranked:
        g = gain_of(world, res, rv)
        L.append("- **%s** (%d parts, estimated gain %s units): %s. Risk: %s. %s" % (rv["id"], rv["count"], g, rv["title"], rv["risk"], rv["note"]))
        ex = [world.path(i) for i, *_ in rv["items"][:3]]
        L.append("  e.g. " + "; ".join("`%s`" % e for e in ex))
    for code, what, note in res["manual"]:
        L.append("- **RV-%s** (manual, no automatic change): %s. %s" % (code, what, note))
    L.append("")
    L.append("## Cannot be improved without changing how it looks")
    L.append("")
    for x in res["cannot"] or ["Nothing notable found."]:
        L.append("- " + x)
    L.append("")
    L.append("## How to apply")
    L.append("")
    L.append("1. Say yes to the SAFE tier. `perf_apply.luau` (next to this report) applies it, checks every rendering property again and puts everything back by itself if one differs.")
    L.append("2. Approve REVIEW items one by one by id (for example `--approve RV-FIDELITY-BOX`); each one is then included in a new `perf_apply.luau`.")
    L.append("3. " + UNDO)
    L.append("")
    L.append("## Limits")
    L.append("")
    L.append("- References from scripts are found by name (own name or any parent's name, also `Name1`/`Name2` style families). A script that finds parts some other way (by position, by child order, by string built at runtime) is only caught through the tag, attribute, joint and script-folder rules.")
    L.append("- If any script cannot be read, nothing is SAFE. If the scan was cut off (maxParts), nothing is SAFE.")
    L.append("- Runtime-created parts and parts in other services (ReplicatedStorage models spawned later) are not scanned; scan the Server datamodel during a playtest to cover spawned objects.")
    L.append("- Cost numbers are a relative proxy, not milliseconds. Real gain: compare MicroProfiler before and after.")
    L.append("- Removed parts are moved to ServerStorage.PerfPass_Removed, not destroyed; delete that folder when you are happy.")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- appearance diff
def vis_key(p):
    return tuple(json.dumps(p.get(f), sort_keys=True) for f in VISUAL_FIELDS)


def appearance_diff(before, after, plan):
    """-> dict(status, byClass{cls:[checked, failing]}, failures[], warnings[])."""
    bp = {p["id"]: p for p in before["parts"]}
    ap = {p["id"]: p for p in after["parts"]}
    planned = {}
    removes = {}
    allow = set(plan.get("allowVisual") or [])
    for it in plan["items"]:
        for i in it["ids"]:
            if it["prop"] == "Remove":
                removes[i] = it["rule"]
            else:
                planned.setdefault(i, {})[PROP_FIELD[it["prop"]]] = (it["to"], it["prop"])
    fails, warns, by = [], [], {}

    def tick(cls, bad):
        c = by.setdefault(cls, [0, 0])
        c[0] += 1
        c[1] += 1 if bad else 0

    for i, p in bp.items():
        q = ap.get(i)
        if q is None:
            ok = False
            if i not in removes:
                fails.append("part %d (%s) disappeared without being in the plan" % (i, p["name"]))
            elif p["tr"] >= 0.999:
                ok = True
            else:
                same = [x for x in after["parts"] if x["id"] != i and x["cls"] == p["cls"] and vis_key(x)[2:] == vis_key(p)[2:] and x["tr"] == 0 and x["cf"] == p["cf"]]
                ok = bool(same)
                if not ok:
                    fails.append("removed part %d (%s) is visible and has no identical twin" % (i, p["name"]))
            tick(p["cls"], not ok)
            continue
        bad = False
        for f in VISUAL_FIELDS:
            if p[f] != q[f]:
                pl = planned.get(i, {}).get(f)
                if pl and pl[1] in allow and q[f] == pl[0]:
                    continue
                bad = True
                fails.append("part %d (%s): %s %r -> %r" % (i, p["name"], f, p[f], q[f]))
        for f in BEHAVIOUR_FIELDS:
            if p[f] != q[f]:
                pl = planned.get(i, {}).get(f)
                want = (int(pl[0]) if isinstance(pl[0], bool) else pl[0]) if pl else None
                if pl is None or q[f] != want:
                    bad = True
                    fails.append("part %d (%s): unplanned change %s %r -> %r" % (i, p["name"], f, p[f], q[f]))
        tick(p["cls"], bad)
    for i, q in ap.items():
        if i not in bp:
            fails.append("part %d (%s) exists after but not before" % (i, q["name"]))
            tick(q["cls"], True)
    for i, ch in planned.items():
        if i in ap:
            for f, (to, prop) in ch.items():
                if ap[i][f] != (int(to) if isinstance(to, bool) else to):
                    warns.append("part %d: planned %s not applied (the runner skipped it)" % (i, prop))
    bc = {c["id"]: c for c in before["containers"]}
    ac = {c["id"]: c for c in after["containers"]}
    for i, c in bc.items():
        if i in ac and (ac[i]["name"], ac[i]["cls"]) != (c["name"], c["cls"]):
            fails.append("container %d changed name or class" % i)
    return dict(status="FAIL" if fails else "PASS", byClass={k: v for k, v in sorted(by.items())}, failures=fails, warnings=warns)


def print_diff(d):
    for cls, (n, bad) in d["byClass"].items():
        print("APPEARANCE %s %s (%d checked, %d differ)" % (cls, "PASS" if not bad else "FAIL", n, bad))
    for f in d["failures"][:30]:
        print("  FAIL " + f)
    for w in d["warnings"][:10]:
        print("  warn " + w)
    print("APPEARANCE DIFF: " + d["status"])


# ---------------------------------------------------------------- CLI
def wr(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8", newline="\n").write(text)
    print("WROTE " + path)


def opt(a, name, default=None):
    return a[a.index(name) + 1] if name in a else default


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        sys.exit(__doc__)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    cmd = a[0]
    out = opt(a, "--write")
    if cmd == "analyze":
        scan = load_scan(a[1], "before")
        game = opt(a, "--game") or scan["head"].get("game") or "game"
        base = os.path.join(out or os.path.join("Games", re.sub(r"[^A-Za-z0-9_.-]+", "_", game)), "perf-qa")
        approve = set(filter(None, (opt(a, "--approve") or "").split(",")))
        w = World(scan)
        res = classify(w, approve)
        known = {r["id"] for r in res["review"] if r["auto"]}
        if approve - known:
            sys.exit("unknown or non-automatic REVIEW id(s): %s (known: %s)" % (",".join(sorted(approve - known)), ",".join(sorted(known)) or "none"))
        plan = build_plan(w, res, approve)
        wr(os.path.join(base, "scan-before.json"), json.dumps(dict(scan, kind="perf-scan"), separators=(",", ":")))
        wr(os.path.join(base, "plan.json"), json.dumps(plan, indent=1))
        wr(os.path.join(base, "report.md"), report(w, res, plan, game))
        wr(os.path.join(base, "perf_apply.luau"), runner_with(plan, "apply"))
        wr(os.path.join(base, "perf_revert.luau"), runner_with(revert_plan(plan, w), "revert"))
        n = sum(len(i["ids"]) for i in plan["items"])
        print("PERF ANALYSIS (dry run): %d parts | SAFE: %d changes/removals planned | REVIEW suggestions: %d (approved: %d)" % (
            w.head["nparts"], sum(len(i["ids"]) for i in plan["items"] if i["tier"] == "safe"), len(res["review"]) + len(res["manual"]), len(plan["approved"])))
        print("ESTIMATE physics cost units %s -> %s (%s), collision memory units %s -> %s (%s)" % (
            res["est_before"]["physicsUnits"], res["est_after"]["physicsUnits"], pct(res["est_before"]["physicsUnits"], res["est_after"]["physicsUnits"]),
            res["est_before"]["collisionMemUnits"], res["est_after"]["collisionMemUnits"], pct(res["est_before"]["collisionMemUnits"], res["est_after"]["collisionMemUnits"])))
        print(UNDO)
        return
    if cmd in ("verify", "diff"):
        before = load_scan(a[1], "before")
        after = load_scan(a[2], "after")
        plan = json.load(open(opt(a, "--plan"), encoding="utf-8-sig")) if opt(a, "--plan") else dict(items=[], allowVisual=[])
        d = appearance_diff(before, after, plan)
        if (after.get("apply") or {}).get("status") == "REVERTED":
            d["warnings"] = ["the runner reverted all of its edits (REVERTED): the planned changes are not in the game"]
        print_diff(d)
        if out:
            wr(os.path.join(out, "perf-qa", "appearance-diff.json"), json.dumps(d, indent=1))
            wr(os.path.join(out, "perf-qa", "scan-after.json"), json.dumps(dict(after, kind="perf-scan"), separators=(",", ":")))
        info = after.get("apply") or {}
        if info:
            print("runner reported: %s" % json.dumps(info))
        sys.exit(0 if d["status"] == "PASS" else 1)
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
