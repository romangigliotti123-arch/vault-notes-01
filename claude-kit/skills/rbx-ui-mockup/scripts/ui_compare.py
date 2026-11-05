#!/usr/bin/env python3
"""ui_compare.py: spec rectangles vs the BUILT UI (numeric, advisory) plus downscaled luminance / edge / palette region flags. Stdlib only, no network.

  ui_compare.py rects  --spec spec.json --frame Shop.phone --built built.(json|txt) [--tol 0.02] [--json]
        built = the console output of rbx-visual/scripts/ui_overlap.luau (lines `UI-RECTS <viewport> [json]`) or a JSON file {"phone": [{path,kind,x,y,w,h,text}]}.
        Elements match by Instance name (last path segment, `[n]` stripped). Per element: dx/dy/dw/dh as a fraction of the frame, text equal, missing, extra built elements.
  ui_compare.py images --spec spec.json --frame Shop.phone --design design.png --shot built.png [--json]
        48x24 luminance grid inside the union of spec rectangles: mean abs diff, 6x3 heat grid, edge-map correlation, palette distance, per-element region flags. PNG only (8-bit).
  ui_compare.py gate   --spec spec.json --frame Shop.phone --built built.txt [--design d.png --shot s.png] --mode auto|figma|manual [--scorer builder|critic] [--round N] --write Games/<slug>
        writes Games/<slug>/ui-design-qa/gate.json (scorecard.py discovers it) and prints the line `UI design: done (auto|figma|manual)`.
  ui_compare.py skip   --reason TEXT [--mode auto|figma|manual] --write Games/<slug>      records `UI design: skipped: <reason>`
  ui_compare.py line   Games/<slug>                                                      prints the gate line from the record (`UI design: skipped: not run` when none)
Thresholds (position/size 0.02 of the frame, edge correlation >= 0.6, luminance MAD < 0.12, palette distance < 0.12, region 0.18) are UNVALIDATED guesses: advisory, they flag regions
for a closer look and never pass or fail a game alone. Cap the fix loop at 3 rounds shared with rbx-visual.
"""
import datetime
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ui_common as C  # noqa: E402

TOL = 0.02
EDGE_MIN, MAD_MAX, PAL_MAX, REGION_MAX = 0.6, 0.12, 0.12, 0.18
MODES = ("auto", "figma", "manual")
GATE_DIR = "ui-design-qa"


def seg_name(path):
    last = str(path).split(".")[-1]
    return re.sub(r"\[\d+\]$", "", last)


def load_built(p, viewport):
    t = open(p, encoding="utf-8-sig", errors="replace").read()
    items = None
    try:
        j = json.loads(t)
        items = j.get(viewport) if isinstance(j, dict) else j
    except ValueError:
        for m in re.finditer(r"UI-RECTS\s+(\w+)\s+(\[.*\])\s*$", t, re.M):
            if m.group(1) == viewport:
                items = json.loads(m.group(2))
    if items is None:
        raise SystemExit("no built rectangles for viewport %r in %s (run ui_overlap.luau and keep its UI-RECTS lines)" % (viewport, p))
    return items


def frame_of(spec, fid):
    f = next((x for x in spec["frames"] if x["id"] == fid), None)
    if not f:
        raise SystemExit("frame %r not in the spec (have: %s)" % (fid, ", ".join(x["id"] for x in spec["frames"])))
    return f


def compare_rects(frame, built, tol=TOL):
    fw, fh = float(frame["w"]), float(frame["h"])
    byname = {}
    for b in built:
        if b.get("kind") == "skip":
            continue
        byname.setdefault(seg_name(b["path"]), []).append(b)
    rows, used = [], set()
    for e in frame["elements"]:
        cands = byname.get(e["name"], [])
        sx, sy, sw, sh = e["px"]
        if not cands:
            rows.append({"name": e["name"], "status": "missing"})
            continue
        b = min(cands, key=lambda c: abs(c["x"] - sx) + abs(c["y"] - sy) + abs(c["w"] - sw) + abs(c["h"] - sh))
        used.add(id(b))
        d = [round((b["x"] - sx) / fw, 4), round((b["y"] - sy) / fh, 4), round((b["w"] - sw) / fw, 4), round((b["h"] - sh) / fh, 4)]
        ok = all(abs(v) <= tol for v in d)
        row = {"name": e["name"], "status": "ok" if ok else "off", "d": d}
        if e.get("text") not in (None, "") and b.get("text") is not None:
            row["text_ok"] = str(b["text"]).strip() == str(e["text"]).strip()
        rows.append(row)
    extra = sorted({seg_name(b["path"]) for b in built if b.get("kind") != "skip" and id(b) not in used and seg_name(b["path"]) not in {e["name"] for e in frame["elements"]}})
    return rows, extra


def summarise_rects(rows, extra):
    total = len(rows)
    found = [r for r in rows if r["status"] != "missing"]
    ok = [r for r in found if r["status"] == "ok"]
    tx = [r for r in found if "text_ok" in r]
    return {"total": total, "found": len(found), "within_tol": len(ok), "text_compared": len(tx), "text_equal": sum(1 for r in tx if r["text_ok"]),
            "missing": [r["name"] for r in rows if r["status"] == "missing"], "off": [(r["name"], r["d"]) for r in found if r["status"] == "off"], "extra": extra[:20], "extra_count": len(extra)}


def lum_grid(img, gw, gh):
    g = C.to_rgb_grid(img, gw, gh)
    return [[(0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]) / 255.0 for c in row] for row in g]


def edge_map(L):
    h, w = len(L), len(L[0])
    return [[abs(L[y][min(w - 1, x + 1)] - L[y][x]) + abs(L[min(h - 1, y + 1)][x] - L[y][x]) for x in range(w)] for y in range(h)]


def pearson(a, b):
    n = len(a)
    if n < 2:
        return 0.0
    ma, mb = sum(a) / n, sum(b) / n
    va = sum((x - ma) ** 2 for x in a)
    vb = sum((y - mb) ** 2 for y in b)
    if va < 1e-9 or vb < 1e-9:
        return 1.0 if va < 1e-9 and vb < 1e-9 else 0.0
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(va * vb)


def top_colours(cells, k=5):
    cnt = {}
    for c in cells:
        key = tuple(int(v) // 16 for v in c)
        cnt[key] = cnt.get(key, 0) + 1
    return [tuple(v * 16 + 8 for v in key) for key, _ in sorted(cnt.items(), key=lambda kv: -kv[1])[:k]]


def palette_distance(a, b):
    def one(x, y):
        return sum(min(math.dist(p, q) for q in y) for p in x) / len(x) / 441.67
    return (one(a, b) + one(b, a)) / 2 if a and b else 1.0


def compare_images(frame, design_png, shot_png):
    d, s = C.decode_png(design_png), C.decode_png(shot_png)
    gw, gh = 48, 24
    Ld, Ls = lum_grid(d, gw, gh), lum_grid(s, gw, gh)
    rects = [e["rect"] for e in frame["elements"]]
    mask = []
    for y in range(gh):
        for x in range(gw):
            cx, cy = (x + 0.5) / gw, (y + 0.5) / gh
            if any(r[0] <= cx <= r[0] + r[2] and r[1] <= cy <= r[1] + r[3] for r in rects):
                mask.append((x, y))
    cells = mask or [(x, y) for y in range(gh) for x in range(gw)]
    mad_cells = {(x, y): abs(Ld[y][x] - Ls[y][x]) for x, y in [(x, y) for y in range(gh) for x in range(gw)]}
    mad = sum(mad_cells[c] for c in cells) / len(cells)
    heat = []
    for by in range(3):
        row = []
        for bx in range(6):
            vals = [mad_cells[(x, y)] for y in range(by * 8, by * 8 + 8) for x in range(bx * 8, bx * 8 + 8)]
            row.append(sum(vals) / len(vals))
        heat.append(row)
    Ed, Es = edge_map(Ld), edge_map(Ls)
    corr = pearson([Ed[y][x] for x, y in cells], [Es[y][x] for x, y in cells])
    gd, gs = C.to_rgb_grid(d, 64, 32), C.to_rgb_grid(s, 64, 32)
    pc = [(x, y) for y in range(32) for x in range(64) if not mask or any(r[0] <= (x + .5) / 64 <= r[0] + r[2] and r[1] <= (y + .5) / 32 <= r[1] + r[3] for r in rects)]
    pal = palette_distance(top_colours([gd[y][x] for x, y in pc]), top_colours([gs[y][x] for x, y in pc]))
    parents = {e.get("parent") for e in frame["elements"]}
    flags = []
    for e in frame["elements"]:
        if e["name"] in parents:
            continue
        r = e["rect"]
        box = (r[0], r[1], r[0] + r[2], r[1] + r[3])
        a, b = C.to_rgb_grid(d, 8, 4, box), C.to_rgb_grid(s, 8, 4, box)
        ds = [math.dist(a[j][i], b[j][i]) / 441.67 for j in range(4) for i in range(8)]
        ld = [abs((0.299 * a[j][i][0] + 0.587 * a[j][i][1] + 0.114 * a[j][i][2]) - (0.299 * b[j][i][0] + 0.587 * b[j][i][1] + 0.114 * b[j][i][2])) / 255.0 for j in range(4) for i in range(8)]
        v = max(sum(ds) / len(ds), sum(ld) / len(ld))
        if v > REGION_MAX:
            flags.append({"name": e["name"], "diff": round(v, 3)})
    return {"mad": round(mad, 4), "edge_corr": round(corr, 4), "palette_distance": round(pal, 4), "heat": [[round(v, 3) for v in row] for row in heat], "region_flags": flags,
            "masked_cells": len(mask), "note": "advisory, thresholds untested guesses (edge >= %.1f, mad < %.2f, palette < %.2f, region %.2f)" % (EDGE_MIN, MAD_MAX, PAL_MAX, REGION_MAX)}


def heat_text(heat):
    return "\n".join("  " + " ".join(" .:*#"[min(4, int(v / 0.1))] for v in row) for row in heat)


def score_checks(rs, im):
    ch = {}
    ch["U1"] = round(10.0 * rs["found"] / rs["total"], 1) if rs["total"] else 0.0
    ch["U2"] = round(10.0 * rs["within_tol"] / rs["found"], 1) if rs["found"] else 0.0
    ch["U3"] = round(10.0 * rs["text_equal"] / rs["text_compared"], 1) if rs["text_compared"] else 10.0
    if im:
        ch["U4"] = round(max(0.0, min(10.0, 10.0 * (1 - im["palette_distance"] / (PAL_MAX * 3)))), 1)
        ch["U5"] = round(max(0.0, min(10.0, 10.0 * max(0.0, im["edge_corr"]) / EDGE_MIN)), 1)
    return ch


def write_gate(dest, rec):
    d = os.path.join(dest, GATE_DIR)
    C.write_text(os.path.join(d, "gate.json"), C.jdump(rec))
    return os.path.join(d, "gate.json")


def gate_line(rec):
    if not rec:
        return "UI design: skipped: not run"
    if rec.get("done"):
        return "UI design: done (%s)" % rec.get("mode", "auto")
    return "UI design: skipped: %s" % rec.get("reason", "no reason given")


def read_gate(dest):
    p = os.path.join(dest, GATE_DIR, "gate.json")
    return C.read_json(p) if os.path.isfile(p) else None


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd = a[0]

    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else default
    if cmd == "line":
        print(gate_line(read_gate(a[1])))
        return 0
    if cmd == "skip":
        why = opt("--reason")
        mode = opt("--mode", "auto")
        dest = opt("--write")
        if not why or not dest or mode not in MODES:
            print("usage: ui_compare.py skip --reason TEXT [--mode auto|figma|manual] --write Games/<slug>", file=sys.stderr)
            return 2
        rec = {"gate": "ui-design", "done": False, "reason": why[:200], "mode": mode, "result": "skipped", "status": "skipped", "advisory": True, "date": datetime.date.today().isoformat()}
        write_gate(dest, rec)
        print(gate_line(rec))
        return 0
    if cmd not in ("rects", "images", "gate"):
        print("unknown command " + cmd, file=sys.stderr)
        return 2
    spec = C.read_json(opt("--spec"))
    fid = opt("--frame", "phone")
    frame = frame_of(spec, fid)
    tol = float(opt("--tol", str(TOL)))
    out = {}
    if cmd in ("rects", "gate"):
        built = load_built(opt("--built"), frame.get("kind") or fid.split(".")[-1])
        rows, extra = compare_rects(frame, built, tol)
        out["rects"] = summarise_rects(rows, extra)
        out["rows"] = rows
    if cmd == "images" or (cmd == "gate" and opt("--design") and opt("--shot")):
        try:
            out["images"] = compare_images(frame, opt("--design"), opt("--shot"))
        except (ValueError, OSError, SystemExit) as e:
            out["images_error"] = str(e)
    rs, im = out.get("rects"), out.get("images")
    if cmd == "gate":
        mode = opt("--mode", "auto")
        if mode not in MODES:
            print("--mode must be auto|figma|manual", file=sys.stderr)
            return 2
        ch = score_checks(rs, im)
        reasons = []
        if rs["missing"]:
            reasons.append("missing in the build: " + ", ".join(rs["missing"][:8]))
        if rs["off"]:
            reasons.append("off by more than %.2f: " % tol + ", ".join("%s %s" % (n, d) for n, d in rs["off"][:5]))
        if im:
            for f in im["region_flags"][:5]:
                reasons.append("region differs: %s (%.2f)" % (f["name"], f["diff"]))
        mean = sum(ch.values()) / len(ch)
        rec = {"gate": "ui-design", "done": True, "mode": mode, "scorer": opt("--scorer", "builder"), "result": "pass" if mean >= 7.0 else "fail", "checks": ch, "reasons": reasons,
               "rounds": int(opt("--round", "1")), "frame": fid, "advisory": True, "spec": os.path.basename(opt("--spec")), "spec_source": spec.get("source"), "date": datetime.date.today().isoformat()}
        p = write_gate(opt("--write"), rec)
        print(gate_line(rec))
        print("UI COMPARE %s frame %s: %d/%d elements found, %d within %.2f, text %d/%d equal, %d extra built elements; mean %.1f (advisory)" %
              (rec["result"].upper(), fid, rs["found"], rs["total"], rs["within_tol"], tol, rs["text_equal"], rs["text_compared"], rs["extra_count"], mean))
        for r in reasons:
            print("  - " + r)
        print("wrote " + p)
        return 0
    if "--json" in a:
        print(json.dumps(out, indent=1))
        return 0
    if rs:
        print("UI RECTS frame %s: %d/%d found, %d within %.2f, text %d/%d equal, %d missing, %d extra (advisory)" % (fid, rs["found"], rs["total"], rs["within_tol"], tol, rs["text_equal"], rs["text_compared"], len(rs["missing"]), rs["extra_count"]))
        for n in rs["missing"][:10]:
            print("  missing " + n)
        for n, d in rs["off"][:10]:
            print("  off %s dx,dy,dw,dh = %s" % (n, d))
        for n in rs["extra"][:5]:
            print("  extra built element " + n)
    if im:
        print("UI IMAGES mad %.3f (< %.2f) edge corr %.2f (>= %.1f) palette distance %.3f (< %.2f)  [advisory, untested thresholds]" % (im["mad"], MAD_MAX, im["edge_corr"], EDGE_MIN, im["palette_distance"], PAL_MAX))
        print(heat_text(im["heat"]))
        for f in im["region_flags"][:8]:
            print("  region differs: %s %.2f" % (f["name"], f["diff"]))
    if out.get("images_error"):
        print("UI IMAGES skipped: " + out["images_error"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
