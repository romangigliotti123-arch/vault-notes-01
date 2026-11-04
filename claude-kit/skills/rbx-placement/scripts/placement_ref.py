#!/usr/bin/env python3
"""placement_ref.py: Python reference implementation of PlacementCore.luau (the pure checks P1-P7 of rbx-placement).

The shipped checker is Luau (Placement.luau, runs inside Roblox Studio). This file is the same algorithm over the same plain data, in Python, so that:
  - the maths can be unit-tested with fixtures without Studio (tests/fixtures.json; the Luau core is run on the SAME fixtures under Lune and must agree),
  - placement_gate.py can RE-CHECK a stored report that carries its inputs (snapshot + environment + intent) instead of trusting its status field.
Keep it identical to PlacementCore.luau: change both, then run netlify-site/tools/test_placement.py (it compares them).

Data (all plain JSON; vectors are [x,y,z]; a rotation r is the 9 numbers of CFrame:GetComponents() after the position: R00 R01 R02 R10 R11 R12 R20 R21 R22):
  snap   = {path, class, pivot:{p,r}, hasPrimaryPart, parts:[{name,p,r,size,anchored,anchoredAssembly,canCollide,canTouch,massless,transparency,hasEffects}]}
  intent = see references/intent.md (kind, floating, expectedSize, face, yawGrid, randomYaw, surfacePath, bounds, allowOverlap, connect, pair, ...)
  env    = {ground:{samples:[{x,z,y?,n?,path?}]}, neighbours:[part...], terrainFill?, faceTarget?, connectTargets:[{point}], pair?:snap, siblings:[summary]}
Entry point: verify(snap, intent, env, opts) -> report {path, class, kind, status, failed, unverified, checks:{P1..P7:{status, measured, tolerance, issues, fixes}}}.
"""
import math

DEFAULTS = dict(floatTol=0.1, buryTol=0.25, slopeTol=1.0, maxTiltDeg=3.0, faceTolDeg=15.0, yawTolDeg=1.0, defaultYawGrid=15.0,
                sizeTol=0.2, overlapTol=0.05, zfightDist=0.005, zfightArea=0.01, terrainFillMax=0.15, connectTol=0.1, atTol=1.0,
                posGridTol=0.05, originRadius=0.5, pairTol=0.15, cloneSizeTol=0.05, maxZfightParts=300, maxSize=2048.0, minSize=0.05)

# Reference scale per object kind. size = sorted ascending [small, mid, large] dimension ranges in studs (pivot-frame extents, any axis order).
KINDS = {
    "door": dict(size=[[0.1, 2], [3, 6], [6, 9]], needsFacing=True, yawGrid=90, allowOverlapNames=["wall", "frame", "doorway"]),
    "window": dict(size=[[0.1, 2], [2, 8], [2, 8]], needsFacing=True, yawGrid=90, allowOverlapNames=["wall", "frame"]),
    "npc": dict(size=[[1, 4], [1.5, 4], [4.5, 7]], needsFacing=True),
    "player": dict(size=[[1, 4], [1.5, 4], [4.5, 7]], needsFacing=True),
    "sign": dict(size=[[0.05, 2], [1, 12], [1, 16]], needsFacing=True, yawGrid=90),
    "chair": dict(size=[[1.5, 4], [1.5, 4], [2, 5]], needsFacing=True),
    "table": dict(size=[[2, 5], [2, 12], [2, 14]]),
    "lamp": dict(size=[[0.5, 4], [0.5, 4], [5, 25]]),
    "crate": dict(size=[[1.5, 8], [1.5, 8], [1.5, 8]]),
    "fence": dict(size=[[0.2, 2], [2, 10], [2, 20]]),
    "wall": dict(size=[[0.2, 4], [4, 60], [4, 300]], yawGrid=90),
    "stairs": dict(size=[[1, 60], [2, 40], [3, 40]]),
    "platform": dict(size=[[0.2, 6], [4, 400], [4, 400]]),
    "tree": dict(size=[[1, 20], [1, 30], [5, 80]], randomYaw=True, buryTol=1.0, terrainFillMax=0.4),
    "rock": dict(size=[[0.5, 20], [0.5, 30], [0.5, 30]], randomYaw=True, buryTol=1.5, terrainFillMax=0.5),
    "bush": dict(size=[[0.5, 8], [0.5, 8], [0.5, 8]], randomYaw=True, buryTol=0.5, terrainFillMax=0.4),
    "pickup": dict(size=[[0.2, 4], [0.5, 4], [0.5, 4]], floating=True, canCollide=False),
    "ground": dict(floating=True, randomYaw=True),
    "prop": dict(),
}
PARTS_CAP = 300


def rnd(x):
    """round half up (the Luau side uses math.floor(x + 0.5); Python round() is banker's rounding)"""
    return math.floor(x + 0.5)


def r3(x):
    return math.floor(x * 1000 + 0.5) / 1000


def rv(v):
    return [r3(x) for x in v]


def sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]


def scale(a, s):
    return [a[0] * s, a[1] * s, a[2] * s]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def vlen(a):
    return math.sqrt(dot(a, a))


def norm(a):
    n = vlen(a)
    if n < 1e-12:
        return [0.0, 0.0, 0.0]
    return [a[0] / n, a[1] / n, a[2] / n]


def axes_of(r):
    """right, up, back (= -look) columns of the rotation."""
    return [[r[0], r[3], r[6]], [r[1], r[4], r[7]], [r[2], r[5], r[8]]]


def look_of(r):
    return [-r[2], -r[5], -r[8]]


def angle_deg(a, b):
    la, lb = vlen(a), vlen(b)
    if la < 1e-9 or lb < 1e-9:
        return 0.0
    c = dot(a, b) / (la * lb)
    c = max(-1.0, min(1.0, c))
    return math.degrees(math.acos(c))


def yaw_of(f):
    return math.degrees(math.atan2(-f[0], -f[2]))


def wrap180(d):
    d = (d + 180.0) % 360.0 - 180.0
    if d == -180.0:
        d = 180.0
    return d


def path_matches(path, prefix):
    if not path or not prefix:
        return False
    return path == prefix or path.startswith(prefix + ".")


# ------------------------------------------------------------------ geometry
def corners(part):
    ax = axes_of(part["r"])
    h = [part["size"][0] / 2, part["size"][1] / 2, part["size"][2] / 2]
    out = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            for sz in (-1, 1):
                c = part["p"]
                c = add(c, scale(ax[0], sx * h[0]))
                c = add(c, scale(ax[1], sy * h[1]))
                c = add(c, scale(ax[2], sz * h[2]))
                out.append(c)
    return out


def world_aabb(parts):
    lo = [math.inf] * 3
    hi = [-math.inf] * 3
    for pt in parts:
        for c in corners(pt):
            for i in range(3):
                lo[i] = min(lo[i], c[i])
                hi[i] = max(hi[i], c[i])
    return lo, hi


def model_box(snap):
    piv = snap["pivot"]
    ax = axes_of(piv["r"])
    lo = [math.inf] * 3
    hi = [-math.inf] * 3
    for pt in snap["parts"]:
        for c in corners(pt):
            d = sub(c, piv["p"])
            for i in range(3):
                t = dot(d, ax[i])
                lo[i] = min(lo[i], t)
                hi[i] = max(hi[i], t)
    dims = [hi[i] - lo[i] for i in range(3)]
    mid = [(hi[i] + lo[i]) / 2 for i in range(3)]
    center = piv["p"]
    for i in range(3):
        center = add(center, scale(ax[i], mid[i]))
    return dict(lo=lo, hi=hi, dims=dims, mid=mid, center=center, axes=ax)


def face_point(box, at):
    if at == "center" or at is None:
        return box["center"]
    table = {"front": (2, -1), "back": (2, 1), "right": (0, 1), "left": (0, -1), "top": (1, 1), "bottom": (1, -1)}
    i, s = table[at]
    return add(box["center"], scale(box["axes"][i], s * box["dims"][i] / 2))


def footprint(snap):
    lo, hi = world_aabb(snap["parts"])
    wx, wz = hi[0] - lo[0], hi[2] - lo[2]
    cx, cz = (lo[0] + hi[0]) / 2, (lo[2] + hi[2]) / 2
    pts = [[cx, cz], [lo[0] + 0.1 * wx, lo[2] + 0.1 * wz], [hi[0] - 0.1 * wx, lo[2] + 0.1 * wz],
           [lo[0] + 0.1 * wx, hi[2] - 0.1 * wz], [hi[0] - 0.1 * wx, hi[2] - 0.1 * wz]]
    return dict(ymin=lo[1], ymax=hi[1], points=pts, aabbMin=lo, aabbMax=hi)


def obb_penetration(a, b):
    """-> (depth, move) or None. depth = smallest overlap over the 15 SAT axes; move = translation of box a that separates it from b."""
    axa, axb = axes_of(a["r"]), axes_of(b["r"])
    ha = [a["size"][0] / 2, a["size"][1] / 2, a["size"][2] / 2]
    hb = [b["size"][0] / 2, b["size"][1] / 2, b["size"][2] / 2]
    t = sub(b["p"], a["p"])
    cand = [axa[0], axa[1], axa[2], axb[0], axb[1], axb[2]]
    for i in range(3):
        for j in range(3):
            c = cross(axa[i], axb[j])
            if vlen(c) > 1e-6:
                cand.append(norm(c))
    best = math.inf
    best_axis = None
    best_sign = 1.0
    for L in cand:
        ra = ha[0] * abs(dot(axa[0], L)) + ha[1] * abs(dot(axa[1], L)) + ha[2] * abs(dot(axa[2], L))
        rb = hb[0] * abs(dot(axb[0], L)) + hb[1] * abs(dot(axb[1], L)) + hb[2] * abs(dot(axb[2], L))
        d = dot(t, L)
        ov = ra + rb - abs(d)
        if ov <= 0:
            return None
        if ov < best:
            best = ov
            best_axis = L
            best_sign = 1.0 if d >= 0 else -1.0
    return best, scale(best_axis, -best_sign * best)


def _poly_area(p):
    s = 0.0
    n = len(p)
    for i in range(n):
        x1, y1 = p[i]
        x2, y2 = p[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2


def _ccw(p):
    return p if _poly_area(p) >= 0 else list(reversed(p))


def _clip(subject, clip):
    out = subject
    n = len(clip)
    for i in range(n):
        a, b = clip[i], clip[(i + 1) % n]
        inp = out
        out = []
        if not inp:
            break
        for k in range(len(inp)):
            cur, prev = inp[k], inp[k - 1]

            def side(pt):
                return (b[0] - a[0]) * (pt[1] - a[1]) - (b[1] - a[1]) * (pt[0] - a[0])

            sc, sp = side(cur), side(prev)
            if sc >= 0:
                if sp < 0:
                    out.append(_isect(prev, cur, a, b))
                out.append(cur)
            elif sp >= 0:
                out.append(_isect(prev, cur, a, b))
    return out


def _isect(p1, p2, a, b):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    x3, y3, x4, y4 = a[0], a[1], b[0], b[1]
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-12:
        return [x2, y2]
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return [x1 + t * (x2 - x1), y1 + t * (y2 - y1)]


def face_rect(part, i, s):
    ax = axes_of(part["r"])
    h = [part["size"][0] / 2, part["size"][1] / 2, part["size"][2] / 2]
    n = scale(ax[i], s)
    c = add(part["p"], scale(n, h[i]))
    j, k = (i + 1) % 3, (i + 2) % 3
    return n, c, [ax[j], h[j]], [ax[k], h[k]]


def coplanar_overlap(a, b, dist_tol):
    """Area of overlap of the largest coplanar, same-facing face pair of parts a and b (0 when none)."""
    best = 0.0
    for i in range(3):
        for s in (-1, 1):
            n, c, ua, va = face_rect(a, i, s)
            for i2 in range(3):
                for s2 in (-1, 1):
                    n2, c2, ub, vb = face_rect(b, i2, s2)
                    if dot(n, n2) < 0.99996 or n[1] < -0.99619:
                        continue  # not the same facing, or a downward face (bottom faces rest on something and are not visible)
                    if abs(dot(n, c) - dot(n, c2)) > dist_tol:
                        continue
                    e1 = ua[0]
                    e2 = norm(cross(n, e1))

                    def to2(pt):
                        return [dot(pt, e1), dot(pt, e2)]

                    ra = []
                    for su, sv in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
                        ra.append(to2(add(add(c, scale(ua[0], su * ua[1])), scale(va[0], sv * va[1]))))
                    rb = []
                    for su, sv in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
                        rb.append(to2(add(add(c2, scale(ub[0], su * ub[1])), scale(vb[0], sv * vb[1]))))
                    poly = _clip(_ccw(rb), _ccw(ra))
                    if len(poly) >= 3:
                        best = max(best, abs(_poly_area(poly)))
    return best


def aabb_touch(p1, p2, pad):
    lo1, hi1 = world_aabb([p1])
    lo2, hi2 = world_aabb([p2])
    for i in range(3):
        if lo1[i] > hi2[i] + pad or lo2[i] > hi1[i] + pad:
            return False
    return True


# ------------------------------------------------------------------ intent helpers
def kind_of(intent):
    return KINDS.get(intent.get("kind") or "prop") or KINDS["prop"]


def pick(intent, key, kind, opts, okey=None):
    if intent.get(key) is not None:
        return intent[key]
    if kind.get(key) is not None:
        return kind[key]
    return opts[okey or key]


def mk(status, measured=None, tolerance=None, issues=None, fixes=None, unverified=None, warnings=None):
    return dict(status=status, measured=measured or {}, tolerance=tolerance or {}, issues=issues or [], fixes=fixes or [],
                unverified=unverified or [], warnings=warnings or [])


def largest_part(snap):
    best, bv = None, -1.0
    for p in snap["parts"]:
        v = p["size"][0] * p["size"][1] * p["size"][2]
        if v > bv:
            best, bv = p, v
    return best


# ------------------------------------------------------------------ checks
def check_p1(snap, intent, env, opts):
    kind = kind_of(intent)
    issues, fixes, unv = [], [], []
    parts = snap["parts"]
    if not parts:
        return mk("fail", issues=["model has no parts"])
    box = model_box(snap)
    dims = box["dims"]
    meas = dict(pivot=rv(snap["pivot"]["p"]), size=rv(dims))
    tol = {}
    if snap.get("class") == "Model" and not snap.get("hasPrimaryPart"):
        issues.append("no PrimaryPart set (the pivot is implicit and fixes/moves cannot rely on it)")
        lp = largest_part(snap)
        fixes.append(dict(action="setPrimaryPart", part=lp["name"]))
    for i in range(3):
        slack = 0.5 + 0.1 * dims[i]
        if box["lo"][i] - slack > 0 or box["hi"][i] + slack < 0:
            issues.append("pivot is outside the model's bounding box on axis %s (offset %.2f studs)" % ("XYZ"[i], min(abs(box["lo"][i]), abs(box["hi"][i]))))
            break
    pp = snap["pivot"]["p"]
    if vlen(pp) < opts["originRadius"] and not intent.get("originOk"):
        at = intent.get("at")
        if not (at and vlen(at) < opts["originRadius"]):
            issues.append("pivot is at the world origin (0,0,0): moved by accident? set intent.at or intent.originOk")
    tol["originRadius"] = opts["originRadius"]
    if intent.get("at") is not None:
        d = sub(intent["at"], pp)
        meas["atOffset"] = rv(d)
        tol["atTol"] = pick(intent, "atTol", {}, opts)
        if vlen(d) > tol["atTol"]:
            issues.append("pivot is %.2f studs from the intended position" % vlen(d))
            fixes.append(dict(action="moveBy", d=rv(d)))
    if intent.get("posGrid"):
        g = float(intent["posGrid"])
        o = intent.get("posGridOrigin") or [0, 0]
        dx = (pp[0] - o[0]) % g
        dz = (pp[2] - o[1]) % g
        dx = min(dx, g - dx)
        dz = min(dz, g - dz)
        meas["posGridDev"] = [r3(dx), r3(dz)]
        tol["posGridTol"] = opts["posGridTol"]
        if dx > opts["posGridTol"] or dz > opts["posGridTol"]:
            sx = rnd((pp[0] - o[0]) / g) * g + o[0] - pp[0]
            sz = rnd((pp[2] - o[1]) / g) * g + o[1] - pp[2]
            issues.append("position is off the %g-stud grid by (%.2f, %.2f)" % (g, dx, dz))
            fixes.append(dict(action="moveBy", d=rv([sx, 0, sz])))
    # size
    small = min(dims)
    big = max(dims)
    if small < opts["minSize"]:
        issues.append("degenerate size: smallest extent %.3f studs" % small)
    if big > opts["maxSize"]:
        issues.append("size %.0f studs exceeds the %g stud limit" % (big, opts["maxSize"]))
    exp = intent.get("expectedSize")
    srt = sorted(dims)
    if exp:
        st = pick(intent, "sizeTol", kind, opts)
        tol["sizeTol"] = st
        if intent.get("sizeSorted") or not intent.get("sizeAxes", True):
            a, b = sorted(exp), srt
        else:
            a, b = exp, dims
        bad = [i for i in range(3) if abs(b[i] - a[i]) > st * a[i] + 0.05]
        meas["expectedSize"] = rv(exp)
        if bad:
            issues.append("size %s differs from the expected %s by more than %d%%" % (rv(dims), rv(exp), rnd(st * 100)))
    elif kind.get("size"):
        rng = kind["size"]
        meas["kindRange"] = rng
        bad = [i for i in range(3) if srt[i] < rng[i][0] or srt[i] > rng[i][1]]
        if bad:
            issues.append("size %s is outside the usual %s range %s (sorted small/mid/large)" % (rv(srt), intent.get("kind"), rng))
    else:
        unv.append("size")
    return mk("fail" if issues else "pass", meas, tol, issues, fixes, unv)


def check_p2(snap, intent, env, opts):
    kind = kind_of(intent)
    floating = intent.get("floating") if intent.get("floating") is not None else kind.get("floating")
    if floating:
        return mk("skip", issues=["flagged floating (air, hover or decor)"])
    ft = pick(intent, "floatTol", kind, opts)
    bt = pick(intent, "buryTol", kind, opts)
    fp = footprint(snap)
    samples = (env.get("ground") or {}).get("samples") or []
    hits = [s for s in samples if s.get("y") is not None]
    tol = dict(floatTol=ft, buryTol=bt)
    if not hits:
        return mk("fail", dict(bottomY=r3(fp["ymin"]), samples=len(samples), hits=0), tol,
                  ["no surface below the model (ray hits nothing): over the void, or the surface is not collidable"])
    top = hits[0]
    low = hits[0]
    for s in hits:
        if s["y"] > top["y"]:
            top = s
        if s["y"] < low["y"]:
            low = s
    gap = fp["ymin"] - top["y"]
    spread = top["y"] - low["y"]
    meas = dict(bottomY=r3(fp["ymin"]), groundY=r3(top["y"]), gap=r3(gap), spread=r3(spread), hits=len(hits), samples=len(samples))
    issues, fixes, warns = [], [], []
    if gap > ft:
        issues.append("floating %.2f studs above the surface (tolerance %.2f)" % (gap, ft))
        fixes.append(dict(action="snapToGround", dy=r3(-gap)))
    elif gap < -bt:
        issues.append("buried %.2f studs into the surface (tolerance %.2f)" % (-gap, bt))
        fixes.append(dict(action="snapToGround", dy=r3(-gap)))
    sp = intent.get("surfacePath")
    if sp:
        meas["restsOn"] = top.get("path")
        if not path_matches(top.get("path") or "", sp):
            issues.append("rests on %s, not on the intended surface %s" % (top.get("path") or "?", sp))
    if spread > opts["slopeTol"]:
        if intent.get("flatGround"):
            issues.append("ground under the footprint varies by %.2f studs (flatGround declared)" % spread)
        else:
            warns.append("ground varies by %.2f studs under the footprint: check the lower side for a visible gap" % spread)
    return mk("fail" if issues else "pass", meas, tol, issues, fixes, [], warns)


def check_p3(snap, intent, env, opts):
    if intent.get("allowTilt"):
        return mk("skip", issues=["tilt allowed by intent"])
    ax = axes_of(snap["pivot"]["r"])
    up = ax[1]
    ref = [0.0, 1.0, 0.0]
    if intent.get("alignToSurface"):
        for s in (env.get("ground") or {}).get("samples") or []:
            if s.get("y") is not None and s.get("n"):
                ref = s["n"]
                break
    ang = angle_deg(up, ref)
    meas = dict(tiltDeg=r3(ang), up=rv(up))
    issues, fixes = [], []
    if intent.get("tilt"):
        want = float(intent["tilt"].get("deg", 0))
        tl = float(intent["tilt"].get("tol", 3))
        tol = dict(tiltDeg=want, tol=tl)
        if abs(ang - want) > tl:
            issues.append("tilt %.1f deg, intended %.1f +/- %.1f" % (ang, want, tl))
            fixes.append(dict(action="setUpright", tiltDeg=want))
    else:
        mt = intent.get("maxTiltDeg") if intent.get("maxTiltDeg") is not None else opts["maxTiltDeg"]
        tol = dict(maxTiltDeg=mt)
        if ang > mt:
            issues.append("%s: tilted %.1f deg from %s (tolerance %.1f)" % ("UPSIDE DOWN" if ang > 90 else "leaning", ang, "the surface normal" if ref != [0.0, 1.0, 0.0] else "world up", mt))
            fixes.append(dict(action="setUpright"))
    return mk("fail" if issues else "pass", meas, tol, issues, fixes)


def check_p4(snap, intent, env, opts):
    kind = kind_of(intent)
    r = snap["pivot"]["r"]
    ax = axes_of(r)
    fr = intent.get("front") or "Front"
    fvec = {"Front": look_of(r), "Back": ax[2], "Right": ax[0], "Left": scale(ax[0], -1)}[fr]
    fxz = [fvec[0], 0.0, fvec[2]]
    meas = dict(front=rv(fvec))
    tol = {}
    issues, fixes, unv = [], [], []
    face = intent.get("face")
    random_yaw = intent.get("randomYaw") if intent.get("randomYaw") is not None else kind.get("randomYaw")
    needs = kind.get("needsFacing")
    grid = None
    explicit_grid = intent.get("yawGrid") is not None or kind.get("yawGrid") is not None
    if not random_yaw:
        grid = intent.get("yawGrid") if intent.get("yawGrid") is not None else kind.get("yawGrid")
        if grid is None and not face:
            grid = opts["defaultYawGrid"]
    if intent.get("yawGrid") == 0:
        grid = None
    if vlen(fxz) < 0.1:
        return mk("fail", meas, tol, ["the front points up or down (%s lying on its side?); fix P3 first" % intent.get("kind", "model")], [])
    yaw = yaw_of(fxz)
    meas["yawDeg"] = r3(yaw)
    desired = None
    pos = snap["pivot"]["p"]
    if face and not face.get("any"):
        tol["faceTolDeg"] = face.get("tol") if face.get("tol") is not None else opts["faceTolDeg"]
        tgt = face["target"] if isinstance(face.get("target"), list) else env.get("faceTarget")
        if face.get("dir"):
            desired = [face["dir"][0], 0.0, face["dir"][2]]
        elif tgt:
            desired = [tgt[0] - pos[0], 0.0, tgt[2] - pos[2]]
        elif face.get("awayFrom") or env.get("faceAwayFrom"):
            af = face.get("awayFrom") or env.get("faceAwayFrom")
            desired = [pos[0] - af[0], 0.0, pos[2] - af[2]]
        if desired is None or vlen(desired) < 0.01:
            issues.append("facing target missing or on the model's own position: cannot judge the facing")
        else:
            off = angle_deg(fxz, desired)
            delta = wrap180(yaw_of(desired) - yaw)
            meas["facingOffDeg"] = r3(off)
            meas["yawDeltaDeg"] = r3(delta)
            if off > tol["faceTolDeg"]:
                issues.append("front faces %.1f deg away from the target (tolerance %.0f)" % (off, tol["faceTolDeg"]))
                final = delta
                if grid and explicit_grid:
                    snapped = rnd((yaw + delta) / grid) * grid
                    if abs(wrap180(snapped - (yaw + delta))) <= tol["faceTolDeg"]:
                        final = wrap180(snapped - yaw)
                fixes.append(dict(action="rotateYaw", deltaDeg=r3(final)))
    elif needs and not (face and face.get("any")):
        issues.append("%s needs a declared facing (intent.face = {target=..} or {dir=..}, or {any=true} if it truly does not matter)" % intent.get("kind"))
    if grid and not (issues and fixes):
        tol["yawGrid"] = grid
        tol["yawTolDeg"] = opts["yawTolDeg"] if intent.get("yawTolDeg") is None else intent["yawTolDeg"]
        nearest = rnd(yaw / grid) * grid
        dev = abs(wrap180(yaw - nearest))
        meas["yawGridDevDeg"] = r3(dev)
        if dev > tol["yawTolDeg"]:
            issues.append("yaw %.1f deg is %.1f deg off the %g deg grid" % (yaw, dev, grid))
            fixes.append(dict(action="rotateYaw", deltaDeg=r3(wrap180(nearest - yaw))))
    elif not grid and not random_yaw and not face:
        unv.append("yaw grid")
    return mk("fail" if issues else "pass", meas, tol, issues, fixes, unv)


def check_p5(snap, intent, env, opts):
    kind = kind_of(intent)
    parts = snap["parts"]
    issues, fixes, warns, unv = [], [], [], []
    lo, hi = world_aabb(parts)
    meas = dict(aabbMin=rv(lo), aabbMax=rv(hi))
    tol = dict(overlapTol=opts["overlapTol"])
    b = intent.get("bounds") or opts.get("bounds")
    if b:
        out = []
        for i in range(3):
            if (b["min"][i] is not None and lo[i] < b["min"][i] - 1e-6) or (b["max"][i] is not None and hi[i] > b["max"][i] + 1e-6):
                out.append(i)
        if out:
            issues.append("outside the map bounds on axis %s" % ",".join("XYZ"[i] for i in out))
    else:
        unv.append("map bounds")
    # overlap with neighbours
    allow = list(intent.get("allowOverlap") or [])
    names = [n.lower() for n in (intent.get("allowOverlapNames") or kind.get("allowOverlapNames") or [])]
    bt = pick(intent, "buryTol", kind, opts)
    samples = (env.get("ground") or {}).get("samples") or []
    hits = [s for s in samples if s.get("y") is not None]
    surf_paths = set(s.get("path") for s in hits if s.get("path"))
    spread = (max(s["y"] for s in hits) - min(s["y"] for s in hits)) if hits else 0.0
    found = {}
    for np_ in env.get("neighbours") or []:
        pth = np_.get("path") or ""
        if any(path_matches(pth, a) for a in allow) or any(n in pth.lower() for n in names):
            continue
        lim = opts["overlapTol"]
        if pth in surf_paths or any(path_matches(pth, s) for s in surf_paths) or (intent.get("surfacePath") and path_matches(pth, intent["surfacePath"])):
            lim = max(lim, bt + spread)
        for mp in parts:
            if not (mp.get("canCollide") and np_.get("canCollide", True)):
                continue
            res = obb_penetration(mp, np_)
            if res and res[0] > lim:
                cur = found.get(pth)
                if cur is None or res[0] > cur[0]:
                    found[pth] = (res[0], res[1])
    ov = sorted(found.items(), key=lambda kv: (-kv[1][0], kv[0]))
    meas["overlaps"] = [dict(path=k, depth=r3(v[0]), move=rv(v[1])) for k, v in ov[:5]]
    for k, v in ov[:5]:
        issues.append("intersects %s by %.2f studs" % (k, v[0]))
    if ov:
        fixes.append(dict(action="nudge", d=rv(ov[0][1][1])))
    # z-fighting
    if len(parts) <= opts["maxZfightParts"]:
        zf = []
        vis = [p for p in parts if p.get("transparency", 0) < 0.95]
        for i, a in enumerate(vis):
            for j in range(i + 1, len(vis)):
                c = vis[j]
                if aabb_touch(a, c, 0.01):
                    ar = coplanar_overlap(a, c, opts["zfightDist"])
                    if ar > opts["zfightArea"]:
                        zf.append(("%s~%s" % (a["name"], c["name"]), ar))
            for nb in env.get("neighbours") or []:
                if nb.get("transparency", 0) >= 0.95:
                    continue
                npth = nb.get("path") or ""
                if any(path_matches(npth, al) for al in allow) or any(n in npth.lower() for n in names):
                    continue
                if aabb_touch(a, nb, 0.01):
                    ar = coplanar_overlap(a, nb, opts["zfightDist"])
                    if ar > opts["zfightArea"]:
                        zf.append(("%s~%s" % (a["name"], nb.get("path")), ar))
        zf.sort(key=lambda kv: (-kv[1], kv[0]))
        meas["zfight"] = [dict(pair=k, area=r3(v)) for k, v in zf[:5]]
        for k, v in zf[:5]:
            issues.append("z-fighting: coplanar faces %s overlap %.2f sq studs" % (k, v))
        if zf:
            fixes.append(dict(action="offsetFace", note="move one face 0.05 studs or make one part slightly larger/smaller"))
    else:
        unv.append("z-fight (more than %d parts)" % opts["maxZfightParts"])
    tf = env.get("terrainFill")
    if tf is not None:
        mx = pick(intent, "terrainFillMax", kind, opts)
        meas["terrainFill"] = r3(tf)
        tol["terrainFillMax"] = mx
        if tf > mx:
            issues.append("%d%% of the model volume is inside terrain (limit %d%%)" % (rnd(tf * 100), rnd(mx * 100)))
            fixes.append(dict(action="raise", note="raise the model or carve the terrain"))
    return mk("fail" if issues else "pass", meas, tol, issues, fixes, unv, warns)


def check_p6(snap, intent, env, opts):
    kind = kind_of(intent)
    parts = snap["parts"]
    issues, fixes, unv = [], [], []
    dynamic = bool(intent.get("dynamic"))
    loose = [p["name"] for p in parts if not p.get("anchored") and not p.get("anchoredAssembly")]
    meas = dict(parts=len(parts), unanchored=loose[:10])
    if loose and not dynamic:
        issues.append("%d part(s) not anchored (will fall or drift): %s" % (len(loose), ", ".join(loose[:5])))
        fixes.append(dict(action="anchor", parts=loose[:50]))
    want_cc = intent.get("canCollide") if intent.get("canCollide") is not None else kind.get("canCollide")
    cc = [p["name"] for p in parts if p.get("canCollide")]
    meas["collidable"] = len(cc)
    if want_cc is True and not cc:
        issues.append("no part collides (CanCollide false everywhere): players walk through it")
        fixes.append(dict(action="setCanCollide", part=largest_part(snap)["name"], value=True))
    if want_cc is False and cc:
        issues.append("%d part(s) collide but the object should not block: %s" % (len(cc), ", ".join(cc[:5])))
        fixes.append(dict(action="setCanCollide", parts=cc[:50], value=False))
    if intent.get("canTouch") is True and not any(p.get("canTouch") for p in parts):
        issues.append("no part has CanTouch true but the object needs touch events")
    if intent.get("massless") is not None:
        bad = [p["name"] for p in parts if bool(p.get("massless")) != bool(intent["massless"]) and not p.get("anchored")]
        if bad:
            issues.append("Massless should be %s on: %s" % (intent["massless"], ", ".join(bad[:5])))
    junk = []
    for p in parts:
        if min(p["size"]) < 0.001:
            junk.append((p["name"], "zero-size"))
        elif p.get("transparency", 0) >= 0.99 and not p.get("canCollide") and not p.get("canTouch") and not p.get("hasEffects") and not intent.get("allowInvisible"):
            junk.append((p["name"], "invisible and intangible"))
    meas["junk"] = [dict(part=n, why=w) for n, w in junk[:10]]
    if junk:
        issues.append("junk part(s): " + ", ".join("%s (%s)" % j for j in junk[:5]))
        fixes.append(dict(action="removeParts", parts=[n for n, _ in junk[:50]]))
    return mk("fail" if issues else "pass", meas, {}, issues, fixes, unv)


def summary(snap):
    box = model_box(snap)
    return dict(dims=rv(sorted(box["dims"])), partCount=len(snap["parts"]), yaw=r3(yaw_of(look_of(snap["pivot"]["r"]))), pos=rv(snap["pivot"]["p"]))


def check_p7(snap, intent, env, opts):
    conns = intent.get("connect") or []
    pair = intent.get("pair")
    group = intent.get("group")
    if not conns and pair is None and group is None:
        return mk("skip", issues=["no connection, pair or group declared"])
    issues, fixes, meas, tol = [], [], {}, {}
    box = model_box(snap)
    targets = env.get("connectTargets") or []
    res = []
    for i, c in enumerate(conns):
        pt = c.get("point") or (targets[i].get("point") if i < len(targets) and targets[i] else None)
        t = c["tol"] if c.get("tol") is not None else opts["connectTol"]
        if pt is None:
            issues.append("connection %d: target %s could not be resolved" % (i + 1, c.get("to", "?")))
            continue
        mine = face_point(box, c.get("at"))
        d = sub(pt, mine)
        res.append(dict(at=c.get("at"), offset=rv(d), dist=r3(vlen(d))))
        tol["connectTol"] = t
        if vlen(d) > t:
            issues.append("connection %d (%s): ends %.2f studs from where the next piece starts (offset %s)" % (i + 1, c.get("at") or "center", vlen(d), rv(d)))
            fixes.append(dict(action="moveBy", d=rv(d)))
    if res:
        meas["connections"] = res
    if pair is not None:
        other = env.get("pair")
        if not other:
            issues.append("mirror partner %s not found" % pair.get("with", "?"))
        else:
            ax = 0 if pair.get("axis", "x") == "x" else 2
            pp = snap["pivot"]["p"]
            want = list(pp)
            want[ax] = 2 * pair["at"] - pp[ax]
            op = other["pivot"]["p"]
            d = sub(op, want)
            meas["pairOffset"] = rv(d)
            tol["pairTol"] = opts["pairTol"]
            if vlen(d) > opts["pairTol"]:
                issues.append("mirror partner is %.2f studs from the mirrored position" % vlen(d))
                fixes.append(dict(action="moveBy", d=rv(sub(want, pp)), note="moves THIS model onto the mirror of the partner; or move the partner instead"))
            a, b = sorted(box["dims"]), sorted(model_box(other)["dims"])
            if any(abs(a[i] - b[i]) > opts["cloneSizeTol"] * max(a[i], 0.1) for i in range(3)):
                issues.append("mirror partner has a different size %s vs %s" % (rv(a), rv(b)))
            lk = look_of(snap["pivot"]["r"])
            lk[ax] = -lk[ax]
            if angle_deg(lk, look_of(other["pivot"]["r"])) > 5:
                issues.append("mirror partner does not face the mirrored direction")
    if group is not None:
        sib = env.get("siblings") or []
        if len(sib) >= 1:
            me = summary(snap)
            dims_list = [s["dims"] for s in sib] + [me["dims"]]
            med = [sorted(d[i] for d in dims_list)[len(dims_list) // 2] for i in range(3)]
            counts = sorted([s["partCount"] for s in sib] + [me["partCount"]])
            medc = counts[len(counts) // 2]
            meas["groupMedianSize"] = rv(med)
            tol["cloneSizeTol"] = opts["cloneSizeTol"]
            if any(abs(me["dims"][i] - med[i]) > opts["cloneSizeTol"] * max(med[i], 0.1) for i in range(3)):
                issues.append("size %s differs from the group median %s" % (me["dims"], rv(med)))
            if me["partCount"] != medc:
                issues.append("%d parts, the group median is %d" % (me["partCount"], medc))
            if group.get("sameYaw"):
                y0 = sib[0]["yaw"]
                if abs(wrap180(me["yaw"] - y0)) > 1.0:
                    issues.append("yaw %.1f differs from the group yaw %.1f" % (me["yaw"], y0))
        else:
            meas["group"] = "no siblings found"
    return mk("fail" if issues else "pass", meas, tol, issues, fixes)


CHECKS = [("P1", check_p1), ("P2", check_p2), ("P3", check_p3), ("P4", check_p4), ("P5", check_p5), ("P6", check_p6), ("P7", check_p7)]
NAMES = {"P1": "Pivot and size", "P2": "Grounded", "P3": "Upright", "P4": "Facing and yaw", "P5": "Clearance", "P6": "Physics flags", "P7": "Connections"}


def verify(snap, intent=None, env=None, opts=None):
    intent = intent or {}
    env = env or {}
    o = dict(DEFAULTS)
    o.update(opts or {})
    waive = intent.get("waive") or {}
    checks = {}
    failed, unverified, waived = [], [], []
    for cid, fn in CHECKS:
        c = fn(snap, intent, env, o)
        if c["status"] == "fail" and cid in waive:
            c["waived"] = str(waive[cid])
            waived.append(cid)
        elif c["status"] == "fail":
            failed.append(cid)
        for u in c["unverified"]:
            unverified.append("%s:%s" % (cid, u))
        checks[cid] = c
    return dict(path=snap.get("path"), **{"class": snap.get("class")}, kind=intent.get("kind") or "prop",
                status="fail" if failed else "pass", failed=failed, waived=waived, unverified=unverified, checks=checks)
