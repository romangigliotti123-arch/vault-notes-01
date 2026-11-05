#!/usr/bin/env python3
"""thumb_score.py: the arithmetic and the objective file checks of the THUMBNAIL SCORE RUBRIC (rbx-thumbnail). Stdlib only, no network, no image libraries.

The agent LOOKS at each candidate image and scores it (3 gates, 13 checks, 0-2 each); this tool adds the weights, the gates, pass/fail, the ranking of 2-5 variants,
header-level facts about the file, and writes the advisory gate record the verdict and scorecard read. Rubric text and anchors: [cold:rbx-thumbnail/rubric.md].

  thumb_score.py rubric                         the gates and checks with weights and how-to-check lines
  thumb_score.py template [--kind thumbnail|icon] [--variants N]    a blank scores file (null = not scored yet)
  thumb_score.py inspect IMAGE [--kind thumbnail|icon]              file exists, PNG/JPEG/GIF/BMP header size, aspect, byte limits, bottom-edge note
  thumb_score.py score SCORES.json [--write Games/<slug>] [--scorer builder|critic] [--json]
        ranks the variants; with --write also writes Games/<slug>/thumb-score/gate.json and prints the line `thumbnail: scored <score>/<max> (variants N)`
  thumb_score.py skip --reason TEXT --write Games/<slug>            records `thumbnail: skipped: <reason>`
  thumb_score.py line Games/<slug>                                  prints the proof-of-use line from the record (`thumbnail: skipped: not run` when none)

SCORES.json: {"game": "slug", "genre": "obby", "kind": "thumbnail", "variants": [{"id": "A", "image": "art/a.png", "control": true,
  "gates": {"G1": "pass", "G2": "pass", "G3": "pass"}, "scores": {"1": 2, "2": 1, ... "13": 2}}]}   (image and control optional)
Weights (3/2/1), the pass bar 32 of 46 and the file limits are the vault's ASSUMPTIONS from evidence grades, not fitted to data; the result ledger (tools/thumb_record.py) is meant to replace them.
"""
import datetime
import json
import os
import struct
import sys

GATES = [
    ("G1", "Promise is real", "Compare with the first-minute screenshot or GAME.md; list every shown element as in game yes/no. Anything absent or enhanced = fail."),
    ("G2", "Rule-safe", "Run the Roblox section of references/checklist.md: no free-Robux hint, real people or brands, copied art, gore, fake UI."),
    ("G3", "Original vs competitors", "Place it beside 5-10 genre competitors; a near-copy of another experience's key art or composition = fail."),
]
CHECKS = [
    ("1", "One clear focal subject", 3, "Squint or blur: name the hero in one noun; none or competing = 0."),
    ("2", "Subject/background value contrast", 3, "View in greyscale: does the hero still separate from the background?"),
    ("3", "Small-size legibility", 3, "Shrink to about 150 px (icon) or 320 px wide (thumbnail) and look again."),
    ("4", "Element count", 2, "Count distinct focal items: 1-2 = 2, three = 1, four or more = 0."),
    ("5", "Genre legibility", 2, "Cover the title and ask what genre it is; one second = 2."),
    ("6", "Emotion or stakes cue", 2, "Describe the feeling in one word; clear expression, threat or reward = 2."),
    ("7", "Curiosity the game answers", 2, "Name the question the image raises and where the first minute answers it."),
    ("8", "Text discipline", 1, "Read the text at small size; check the bottom 15% is free; none or 1-3 big words = 2."),
    ("9", "Colour fit", 1, "Palette matches the genre mood and supports contrast; clashing or muddy = 0."),
    ("10", "Action or implied motion", 1, "Is there a pose or diagonal that implies something is happening?"),
    ("11", "Novelty twist", 1, "State the one thing only this game has; generic = 0."),
    ("12", "Cross-asset consistency", 1, "Compare with the icon and the other thumbnails: shared palette and character."),
    ("13", "Artifact check", 1, "Zoom to 100%: broken hands, garbled text, extra limbs = 0."),
]
WEIGHT = {c[0]: c[2] for c in CHECKS}
MAX_SCORE = 2 * sum(WEIGHT.values())
PASS_SCORE = 32
THUMB_MAX_BYTES = 3000000
ICON_MIN = 512
ASPECT_TOL = 0.005
GATE_DIR = "thumb-score"
KINDS = ("thumbnail", "icon")
PASS_WORDS = ("pass", "passed", "ok", "yes", "true", "1")
FAIL_WORDS = ("fail", "failed", "no", "false", "0")


def read_header(path):
    with open(path, "rb") as f:
        b = f.read(65536)
    if b[:8] == b"\x89PNG\r\n\x1a\n" and len(b) >= 24:
        w, h = struct.unpack(">II", b[16:24])
        return "png", w, h
    if b[:6] in (b"GIF87a", b"GIF89a") and len(b) >= 10:
        w, h = struct.unpack("<HH", b[6:10])
        return "gif", w, h
    if b[:2] == b"BM" and len(b) >= 26:
        w, h = struct.unpack("<ii", b[18:26])
        return "bmp", abs(w), abs(h)
    if b[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(b):
            if b[i] != 0xFF:
                i += 1
                continue
            m = b[i + 1]
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7 or m == 0xFF:
                i += 1 if m == 0xFF else 2
                continue
            if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack(">HH", b[i + 5:i + 9])
                return "jpeg", w, h
            i += 2 + struct.unpack(">H", b[i + 2:i + 4])[0]
    return None, 0, 0


def inspect(path, kind="thumbnail"):
    """-> (facts dict, [{id, status ok|warn|fail|note, note}]); a fail means the file is not usable as is"""
    out = []

    def add(i, s, n):
        out.append({"id": i, "status": s, "note": n})
    facts = {"path": path, "kind": kind}
    if not os.path.isfile(path):
        add("file", "fail", "file not found")
        return facts, out
    size = os.path.getsize(path)
    facts["bytes"] = size
    if size == 0:
        add("file", "fail", "file is empty")
        return facts, out
    add("file", "ok", "%d bytes" % size)
    try:
        fmt, w, h = read_header(path)
    except (OSError, struct.error) as e:
        fmt, w, h = None, 0, 0
        add("format", "warn", "header unreadable: %s" % e)
    if not fmt:
        if not out or out[-1]["id"] != "format":
            add("format", "warn", "not PNG/JPEG/GIF/BMP by header (Roblox also takes .tga): size and aspect not checked")
    else:
        facts.update(format=fmt, width=w, height=h)
        add("format", "ok", "%s %dx%d" % (fmt, w, h))
        if w <= 0 or h <= 0:
            add("size", "fail", "zero width or height")
        elif kind == "thumbnail":
            r = w / float(h)
            if abs(r - 16 / 9.0) / (16 / 9.0) <= ASPECT_TOL:
                add("aspect", "ok", "16:9")
                if (w, h) != (1920, 1080):
                    add("size", "warn", "%dx%d; 1920x1080 is the recommended size" % (w, h))
                else:
                    add("size", "ok", "1920x1080")
            else:
                add("aspect", "fail", "%.3f:1 is not 16:9; Roblox stretches non-16:9 images to 16:9" % r)
        else:
            if w != h:
                add("aspect", "fail", "icon must be square (got %dx%d)" % (w, h))
            else:
                add("aspect", "ok", "square")
            if min(w, h) < ICON_MIN:
                add("size", "fail", "icon needs at least %dx%d (got %dx%d)" % (ICON_MIN, ICON_MIN, w, h))
            else:
                add("size", "ok", "%dx%d, at least %d" % (w, h, ICON_MIN))
    if kind == "thumbnail":
        if size >= THUMB_MAX_BYTES:
            add("bytes", "fail", "%d bytes; thumbnail personalization takes files under 3 MB (read as 3,000,000 bytes: stricter than needed)" % size)
        else:
            add("bytes", "ok", "under 3 MB")
        add("safe-zone", "note", "keep essential text and elements out of the bottom edge (player-count overlay): check the bottom 15% by eye (rubric check 8)")
    else:
        add("bytes", "note", "icon file-size limit not stated on the Roblox pages read: not checked")
        add("safe-zone", "note", "icons render down to about 150 px: check legibility at that size (rubric check 3)")
    return facts, out


def objective_ok(rows):
    return not any(r["status"] == "fail" for r in rows)


def flag(v):
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in PASS_WORDS:
        return True
    if s in FAIL_WORDS:
        return False
    return None


def score_variant(v, kind, base):
    """-> result dict; raises ValueError with a usable message on bad input"""
    vid = str(v.get("id", "")).strip()
    if not vid:
        raise ValueError("a variant has no id")
    g = v.get("gates") or {}
    gates = {}
    for gid, _n, _h in GATES:
        f = flag(g.get(gid))
        if f is None:
            raise ValueError("variant %s: gate %s must be pass or fail (look at the image and decide)" % (vid, gid))
        gates[gid] = f
    sc = {}
    for k, val in (v.get("scores") or {}).items():
        k = str(k).strip().lstrip("Cc")
        if k not in WEIGHT:
            raise ValueError("variant %s: unknown check %r (checks are 1-13)" % (vid, k))
        if isinstance(val, bool) or val not in (0, 1, 2) or isinstance(val, float) and val != int(val):
            raise ValueError("variant %s: check %s must be 0, 1 or 2 (got %r)" % (vid, k, val))
        sc[k] = int(val)
    missing = [c[0] for c in CHECKS if c[0] not in sc]
    if missing:
        raise ValueError("variant %s: not scored: check %s (score all 13 by looking at the image)" % (vid, ", ".join(missing)))
    total = sum(WEIGHT[k] * sc[k] for k in WEIGHT)
    names = {c[0]: c[1] for c in CHECKS}
    losses = sorted(((WEIGHT[k] * (2 - sc[k]), -int(k), k) for k in WEIGHT if sc[k] < 2), reverse=True)
    fixes = [{"check": k, "name": names[k], "score": sc[k], "loses": loss} for loss, _o, k in losses[:3]]
    rows, facts = None, None
    img = v.get("image")
    if img:
        p = img if os.path.isabs(img) else os.path.join(base, img)
        facts, rows = inspect(p, kind)
    obj_ok = True if rows is None else objective_ok(rows)
    gates_ok = all(gates.values())
    return {"id": vid, "total": total, "max": MAX_SCORE, "gates": gates, "gates_ok": gates_ok, "scores": sc, "fix_first": fixes, "image": img, "objective": rows,
            "objective_ok": obj_ok, "control": bool(v.get("control")), "pass": gates_ok and obj_ok and total >= PASS_SCORE}


def rank(results):
    return sorted(results, key=lambda r: (not r["pass"], not r["gates_ok"], -r["total"], r["id"]))


def load_scores(path):
    with open(path, encoding="utf-8-sig") as f:
        d = json.load(f)
    if not isinstance(d, dict) or not isinstance(d.get("variants"), list) or not d["variants"]:
        raise ValueError('SCORES.json needs {"variants": [ {id, gates, scores}, ... ]}')
    kind = d.get("kind", "thumbnail")
    if kind not in KINDS:
        raise ValueError("kind must be thumbnail or icon")
    ids = [str(v.get("id")) for v in d["variants"] if isinstance(v, dict)]
    if len(ids) != len(d["variants"]) or len(set(ids)) != len(ids):
        raise ValueError("every variant needs a unique id")
    return d, kind


def evaluate(d, kind, base="."):
    return rank([score_variant(v, kind, base) for v in d["variants"]])


def line_of(rec):
    if not rec:
        return "thumbnail: skipped: not run"
    if rec.get("done"):
        return "thumbnail: scored %d/%d (variants %d)" % (rec["score"], rec["max"], rec["variants"])
    return "thumbnail: skipped: %s" % rec.get("reason", "no reason given")


def gate_path(dest):
    return os.path.join(dest, GATE_DIR, "gate.json")


def read_gate(dest):
    try:
        with open(gate_path(dest), encoding="utf-8-sig") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def write_gate(dest, rec):
    os.makedirs(os.path.join(dest, GATE_DIR), exist_ok=True)
    with open(gate_path(dest), "w", encoding="utf-8", newline="\n") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    return gate_path(dest)


def gate_record(d, kind, ranked, scorer):
    best = ranked[0]
    reasons = []
    for gid, ok in best["gates"].items():
        if not ok:
            reasons.append("gate %s failed (%s)" % (gid, next(g[1] for g in GATES if g[0] == gid)))
    for r in best["objective"] or []:
        if r["status"] == "fail":
            reasons.append("file: %s: %s" % (r["id"], r["note"]))
    if best["total"] < PASS_SCORE:
        reasons.append("score %d is under the pass bar %d (assumption)" % (best["total"], PASS_SCORE))
    reasons += ["fix first: check %s %s (%d/2)" % (f["check"], f["name"], f["score"]) for f in best["fix_first"]]
    return {"gate": "thumb-score", "done": True, "advisory": True, "scorer": scorer, "kind": kind, "game": d.get("game"), "genre": d.get("genre"),
            "result": "pass" if best["pass"] else "fail", "status": "pass" if best["pass"] else "fail",
            "checks": {("C" + k): round(best["scores"][k] * 5.0, 1) for k in WEIGHT}, "gates": best["gates"], "score": best["total"], "max": MAX_SCORE, "pass_score": PASS_SCORE,
            "variants": len(ranked), "best": best["id"], "ranking": [{"id": r["id"], "total": r["total"], "pass": r["pass"]} for r in ranked], "reasons": reasons,
            "assumptions": "weights 3/2/1, pass bar 32 of 46 and the file limits are vault assumptions, not fitted to data",
            "date": datetime.date.today().isoformat()}


def table(ranked, kind):
    ctl = next((r for r in ranked if r["control"]), None)
    lines = ["THUMBNAIL SCORE (%s; max %d, pass %d with no failed gate; weights and pass bar are assumptions)" % (kind, MAX_SCORE, PASS_SCORE),
             "rank  id        total   gates  file     result   vs control"]
    for i, r in enumerate(ranked, 1):
        fl = "n/a" if r["objective"] is None else ("ok" if r["objective_ok"] else "FAIL")
        dv = "" if not ctl or r is ctl else "%+d" % (r["total"] - ctl["total"])
        lines.append("%-5d %-9s %2d/%-4d %-6s %-8s %-8s %s" % (i, r["id"][:9], r["total"], r["max"], "ok" if r["gates_ok"] else "FAIL", fl, "PASS" if r["pass"] else "FAIL", dv + (" (control)" if r is ctl else "")))
    return lines


def cmd_rubric():
    print("THUMBNAIL SCORE RUBRIC: gates (pass/fail) and 13 checks scored 0/1/2; weight x score; max %d, pass %d (assumptions; anchors in rubric.md)" % (MAX_SCORE, PASS_SCORE))
    for gid, n, h in GATES:
        print("  %-3s gate   %s: %s" % (gid, n, h))
    for cid, n, w, h in CHECKS:
        print("  %-3s x%d     %s: %s" % (cid, w, n, h))
    return 0


def cmd_template(a, opt):
    n = int(opt("--variants", "3"))
    kind = opt("--kind", "thumbnail")
    if kind not in KINDS or not 1 <= n <= 10:
        print("usage: thumb_score.py template [--kind thumbnail|icon] [--variants 1-10]", file=sys.stderr)
        return 2
    vs = [{"id": chr(65 + i), "image": "art/%s-%s.png" % (kind, chr(97 + i)), "control": i == 0, "gates": {g[0]: None for g in GATES}, "scores": {c[0]: None for c in CHECKS}} for i in range(n)]
    print(json.dumps({"game": "slug", "genre": "genre", "kind": kind, "variants": vs}, indent=1))
    return 0


def cmd_inspect(a, opt):
    kind = opt("--kind", "thumbnail")
    path = next((x for x in a[1:] if not x.startswith("--") and x != kind), None)
    if not path or kind not in KINDS:
        print("usage: thumb_score.py inspect IMAGE [--kind thumbnail|icon]", file=sys.stderr)
        return 2
    _f, rows = inspect(path, kind)
    for r in rows:
        print("  %-9s %-5s %s" % (r["id"], r["status"].upper(), r["note"]))
    ok = objective_ok(rows)
    print("FILE CHECKS: %s" % ("ok" if ok else "FAIL"))
    return 0 if ok else 1


def cmd_score(a, opt):
    src = a[1] if len(a) > 1 and not a[1].startswith("--") else None
    if not src:
        print("usage: thumb_score.py score SCORES.json [--write Games/<slug>] [--scorer builder|critic] [--json]", file=sys.stderr)
        return 2
    scorer = opt("--scorer", "builder")
    if scorer not in ("builder", "critic"):
        print("--scorer must be builder or critic", file=sys.stderr)
        return 2
    try:
        d, kind = load_scores(src)
        ranked = evaluate(d, kind, os.path.dirname(os.path.abspath(src)))
    except (OSError, ValueError) as e:
        print("thumb_score: %s" % e, file=sys.stderr)
        return 2
    if "--json" in a:
        print(json.dumps({"kind": kind, "ranking": ranked}, indent=1))
    else:
        for ln in table(ranked, kind):
            print(ln)
        b = ranked[0]
        for r in b["objective"] or []:
            if r["status"] in ("fail", "warn"):
                print("  file %s %s: %s" % (b["id"], r["status"].upper(), r["note"]))
        print("best %s: %d/%d, %s" % (b["id"], b["total"], b["max"], "PASS" if b["pass"] else "NOT YET (fix the lowest checks, then score again)"))
        for f in b["fix_first"]:
            print("  fix first: check %s %s scored %d/2 (loses %d points)" % (f["check"], f["name"], f["score"], f["loses"]))
        if len(ranked) == 1:
            print("note: one variant scored; Roblox thumbnail personalization needs 2-5 active thumbnails")
        elif len(ranked) > 5:
            print("note: only 5 thumbnails can be active at once; pick the top 5 for the test")
    rec = gate_record(d, kind, ranked, scorer)
    if opt("--write"):
        p = write_gate(opt("--write"), rec)
        print(line_of(rec))
        print("wrote " + p)
    else:
        print(line_of(rec) + "   (not recorded: add --write Games/<slug>)")
    return 0


def cmd_skip(a, opt):
    why, dest = opt("--reason"), opt("--write")
    if not why or not dest:
        print("usage: thumb_score.py skip --reason TEXT --write Games/<slug>", file=sys.stderr)
        return 2
    rec = {"gate": "thumb-score", "done": False, "reason": why[:200], "result": "skipped", "status": "skipped", "advisory": True, "date": datetime.date.today().isoformat()}
    write_gate(dest, rec)
    print(line_of(rec))
    return 0


def main(argv=None):
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(errors="replace")
        except Exception:
            pass
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else default
    cmd = a[0]
    if cmd == "rubric":
        return cmd_rubric()
    if cmd == "template":
        return cmd_template(a, opt)
    if cmd == "inspect":
        return cmd_inspect(a, opt)
    if cmd == "score":
        return cmd_score(a, opt)
    if cmd == "skip":
        return cmd_skip(a, opt)
    if cmd == "line" and len(a) > 1:
        print(line_of(read_gate(a[1])))
        return 0
    print("unknown command %s (rubric|template|inspect|score|skip|line)" % cmd, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
