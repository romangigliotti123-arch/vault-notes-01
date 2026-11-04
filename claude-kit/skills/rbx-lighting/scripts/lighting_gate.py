#!/usr/bin/env python3
"""lighting_gate.py: deterministic pass/fail of the lighting gate (checks L1-L12 in references/checks.md). Nobody eyeballs the result.

  python lighting_gate.py <scan.json> [--project DIR] [--write Games/<slug>] [--scorer critic] [--genre G] [--platform both|pc|mobile] [--shots-from-visual Games/<slug>] [--shots a.png b.png]
  python lighting_gate.py ingest <console-output.txt> --write Games/<slug> [--scorer builder|critic] [--game SLUG] [--genre G] [--platform P] [--shots ...] [--shots-from-visual DIR] [--name scan-builder]
  python lighting_gate.py recheck <scan.json>                       re-run L1-L12 from the stored state (lighting_ref.py) and compare with the stored report
  python lighting_gate.py image-stats <a.png> [b.png ...]            mean / crushed / blown luma of screenshots (PNG only, standard library decoder)

scan.json (written by LightingKit.scan, or built by `ingest` from the LIGHTING_SCAN_PART console lines): see references/gate-format.md.
  {"kind": "lighting-scan", "version": 1, "game": "slug", "scorer": "builder" | "critic", "datamodel": "Edit", "captured_at": "2026-11-04T10:00:00Z",
   "config": {"genre": "obby", "platform": "both", "theme": {...}, "waive": {...}}, "state": {...snapshot...}, "report": {...checks...}, "shots": [{"path", "mean", "crushed", "blown"}]?}

PASS needs ALL of: a scan of kind lighting-scan; the checks recomputed here from the stored state (the stored report is never trusted; a differing stored report is
reported) are pass or waived with a reason of >= 10 characters (at most 2 waivers); L6 (brightness) judged from >= 8 scene samples or from screenshots (a scan with
neither fails unless it states a `no_world` reason); a scan not older than the newest Luau source (--project). --scorer critic additionally demands scorer == critic (the
critic's own fresh scan decides; a builder's scan is evidence only). --genre and --platform (from GAME.md) override the config recorded in the scan.
Importable: evaluate(scan, base_dir, project, require_scorer, genre, platform) -> dict(status, reasons, failing, label, counts, report).
"""
import datetime
import json
import os
import re
import struct
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lighting_ref  # noqa: E402

NOT_VERIFIED = "playable prototype, lighting not verified"
VERIFIED = "lighting verified (lighting gate passed)"
MIN_WAIVER = 10
MAX_WAIVERS = 2
PART = re.compile(r"LIGHTING_SCAN_PART\s+(\d+)/(\d+)\s+(\S.*?)\s*$")
SKIP_OK = {"L8"}  # L8 skips when there is no Atmosphere, which L2 already fails


def _newest_source(project):
    newest = 0.0
    for root, dirs, files in os.walk(project):
        dirs[:] = [d for d in dirs if d.lower() not in ("packages", "vendor", "node_modules", ".git", "build", "docs")]
        for f in files:
            if f.endswith((".luau", ".lua")):
                newest = max(newest, os.path.getmtime(os.path.join(root, f)))
    return newest


def _ts(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc).timestamp()
    except Exception:
        return None


# ------------------------------------------------------------------ PNG luma (standard library)
def png_stats(path, max_pixels=400000):
    """-> dict(mean, crushed, blown, w, h) of a PNG (8-bit gray, gray+alpha, RGB, RGBA, palette; not interlaced), luma in display space 0-1. Raises ValueError otherwise."""
    data = open(path, "rb").read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    pos, idat, plte = 8, [], None
    w = h = depth = ctype = interlace = None
    while pos < len(data):
        n, typ = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + n]
        pos += 12 + n
        if typ == b"IHDR":
            w, h, depth, ctype, _, _, interlace = struct.unpack(">IIBBBBB", body)
        elif typ == b"PLTE":
            plte = body
        elif typ == b"IDAT":
            idat.append(body)
        elif typ == b"IEND":
            break
    if depth != 8 or interlace != 0 or ctype not in (0, 2, 3, 4, 6):
        raise ValueError("unsupported PNG (need 8-bit, not interlaced): depth %s colour type %s interlace %s" % (depth, ctype, interlace))
    bpp = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ctype]
    raw = zlib.decompress(b"".join(idat))
    stride = w * bpp
    prev = bytearray(stride)
    rows = []
    off = 0
    step = max(1, int((w * h / float(max_pixels)) ** 0.5))
    for y in range(h):
        f = raw[off]
        cur = bytearray(raw[off + 1:off + 1 + stride])
        off += 1 + stride
        if f == 1:
            for i in range(bpp, stride):
                cur[i] = (cur[i] + cur[i - bpp]) & 255
        elif f == 2:
            for i in range(stride):
                cur[i] = (cur[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride):
                left = cur[i - bpp] if i >= bpp else 0
                cur[i] = (cur[i] + ((left + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(stride):
                a = cur[i - bpp] if i >= bpp else 0
                b = prev[i]
                c = prev[i - bpp] if i >= bpp else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                cur[i] = (cur[i] + pr) & 255
        elif f != 0:
            raise ValueError("bad PNG filter %d" % f)
        prev = cur
        if y % step == 0:
            rows.append(cur)
    tot = crushed = blown = 0
    acc = 0.0
    for cur in rows:
        for x in range(0, w, step):
            i = x * bpp
            if ctype == 0 or ctype == 4:
                lum = cur[i] / 255.0
            elif ctype == 3:
                j = cur[i] * 3
                lum = (0.2126 * plte[j] + 0.7152 * plte[j + 1] + 0.0722 * plte[j + 2]) / 255.0
            else:
                lum = (0.2126 * cur[i] + 0.7152 * cur[i + 1] + 0.0722 * cur[i + 2]) / 255.0
            acc += lum
            tot += 1
            if lum < lighting_ref.M["crushed_luma"]:
                crushed += 1
            if lum > lighting_ref.M["blown_luma"]:
                blown += 1
    return dict(mean=round(acc / tot, 4), crushed=round(crushed / tot, 4), blown=round(blown / tot, 4), w=w, h=h)


def shots_from(paths, base=None):
    out, bad = [], []
    for p in paths:
        full = p if os.path.isabs(p) or not base else os.path.join(base, p)
        try:
            s = png_stats(full)
            s["path"] = p
            out.append(s)
        except Exception as e:
            bad.append("%s (%s)" % (p, e))
    return out, bad


def visual_shot_paths(game_dir):
    """The screenshots the visual gate used (visual-qa/gate-critic.json, else gate.json): PNG paths relative to the game folder."""
    for name in ("gate-critic.json", "gate.json"):
        p = os.path.join(game_dir, "visual-qa", name)
        if os.path.isfile(p):
            try:
                g = json.load(open(p, encoding="utf-8-sig"))
            except Exception:
                continue
            paths = []
            for s in g.get("screenshots") or []:
                q = s.get("path", "") if isinstance(s, dict) else str(s)
                if q.lower().endswith(".png"):
                    paths.append(q)
            return paths
    return []


# ------------------------------------------------------------------ gate maths
def _first_fix(c):
    fx = c.get("fixes") or []
    if fx:
        f = fx[0]
        return "%s %s" % (f.get("action"), json.dumps({k: v for k, v in f.items() if k not in ("action", "note")}))
    return ""


def evaluate(scan, base_dir=".", project=None, require_scorer=None, genre=None, platform=None):
    reasons, failing = [], []
    counts = dict(checks=0, pass_=0, fail=0, waived=0, skipped=0, unverified=0, warnings=0, samples=0, shots=0)
    if not isinstance(scan, dict) or scan.get("kind") != "lighting-scan":
        return dict(status="skipped", reasons=["no lighting scan recorded (run rbx-lighting: LightingKit.scan on the whole place)"], failing=[], label=NOT_VERIFIED, counts=counts, report=None)
    if scan.get("version") != 1:
        reasons.append("unknown scan version %r" % scan.get("version"))
    if require_scorer and scan.get("scorer") != require_scorer:
        reasons.append("scan was made by %r, the verdict needs a fresh scan made by %r" % (scan.get("scorer"), require_scorer))
    state = scan.get("state")
    cfg = dict(scan.get("config") or {})
    if not isinstance(state, dict) or not isinstance(state.get("lighting"), dict):
        reasons.append("the scan carries no state snapshot: the checks cannot be recomputed")
        return dict(status="fail", reasons=reasons, failing=failing, label=NOT_VERIFIED, counts=counts, report=None)
    if genre:
        cfg["genre"] = genre
    if platform:
        cfg["platform"] = platform
    if scan.get("shots"):
        state = dict(state, shots=scan["shots"])
    rep = lighting_ref.verify(state, cfg)
    counts["samples"] = len(state.get("samples") or [])
    counts["shots"] = len(state.get("shots") or [])
    stored = scan.get("report")
    if isinstance(stored, dict) and not genre and not platform and not scan.get("shots"):
        if stored.get("status") != rep["status"] or sorted(stored.get("failed") or []) != sorted(rep["failed"]):
            reasons.append("the stored report (%s, failed %s) differs from a fresh run of the checks on the stored state (%s, failed %s): the scan was edited or made by an older kit" %
                           (stored.get("status"), stored.get("failed"), rep["status"], rep["failed"]))
    if len(rep["waived"]) > MAX_WAIVERS:
        reasons.append("%d checks are waived (limit %d): fix them instead" % (len(rep["waived"]), MAX_WAIVERS))
    no_world = scan.get("no_world")
    no_world_ok = isinstance(no_world, str) and len(no_world.strip()) >= MIN_WAIVER
    for cid in lighting_ref.ORDER:
        c = rep["checks"][cid]
        counts["checks"] += 1
        counts["unverified"] += len(c["unverified"])
        counts["warnings"] += len(c["warnings"])
        if c.get("waived"):
            counts["waived"] += 1
            counts["pass_"] += 1
            continue
        if c["status"] == "pass":
            counts["pass_"] += 1
        elif c["status"] == "skip":
            counts["skipped"] += 1
            if cid in SKIP_OK or (cid == "L6" and no_world_ok):
                counts["pass_"] += 1
            else:
                counts["fail"] += 1
                failing.append(dict(check=cid, name=c["name"], issues=c["issues"][:3], fix="run LightingKit.scan inside the built place (it samples the map), or pass screenshots with --shots-from-visual"))
        else:
            counts["fail"] += 1
            failing.append(dict(check=cid, name=c["name"], issues=c["issues"][:4], fix=_first_fix(c)))
    if failing:
        reasons.append("%d of %d lighting check(s) fail" % (len(failing), counts["checks"]))
    cap = _ts(scan.get("captured_at") or "")
    if project:
        src = _newest_source(project)
        if src and cap is not None and cap < src - 1:
            reasons.append("stale scan: a Luau source changed after the scan was captured; run the scan again")
    status = "pass" if not reasons else "fail"
    return dict(status=status, reasons=reasons, failing=failing, label=VERIFIED if status == "pass" else NOT_VERIFIED, counts=counts, report=rep)


# ------------------------------------------------------------------ console parsing
def parse_console(text):
    """-> scan dict from LIGHTING_SCAN_PART i/n chunks (timestamps or prefixes before the tag are ignored), or None."""
    parts, total = {}, 0
    for ln in text.splitlines():
        m = PART.search(ln)
        if m:
            parts[int(m.group(1))] = m.group(3)
            total = int(m.group(2))
    if not parts:
        return None
    if sorted(parts) != list(range(1, total + 1)):
        raise ValueError("LIGHTING_SCAN_PART chunks are incomplete: have %s of %d" % (sorted(parts), total))
    return json.loads("".join(parts[i] for i in range(1, total + 1)))


def print_result(r, scan):
    rep = r.get("report") or {}
    print("LIGHTING GATE: %s | scorer %s | genre %s | phase %s | platform %s | %d/%d checks pass" % (
        r["status"].upper(), scan.get("scorer", "?") if isinstance(scan, dict) else "?", rep.get("genre"), rep.get("phase"), rep.get("platform"), r["counts"]["pass_"], r["counts"]["checks"]))
    print("STATUS LABEL: " + r["label"])
    for x in r["reasons"]:
        print("  - " + x)
    for f in r["failing"][:30]:
        print("  FAIL %s %s :: %s" % (f["check"], f["name"], " | ".join(f["issues"])))
        if f["fix"]:
            print("       suggested fix: " + f["fix"])
    c = r["counts"]
    print("  waived: %d | skipped: %d | unverified items: %d | warnings: %d | scene samples: %d | screenshots: %d" % (c["waived"], c["skipped"], c["unverified"], c["warnings"], c["samples"], c["shots"]))
    for w in (rep.get("warnings") or [])[:6]:
        print("  note: " + w)
    for u in (rep.get("unverified") or [])[:4]:
        print("  unverified: " + u)


def write_gate(out_dir, scan, r, src):
    d = os.path.join(out_dir, "lighting-qa")
    os.makedirs(d, exist_ok=True)
    rep = r.get("report") or {}
    rec = dict(result=r["status"], label=r["label"], reasons=r["reasons"], failing=r["failing"], counts=r["counts"], scorer=scan.get("scorer"), captured_at=scan.get("captured_at"),
               genre=rep.get("genre"), phase=rep.get("phase"), platform=rep.get("platform"), summary=rep.get("summary"), warnings=rep.get("warnings"), unverified=rep.get("unverified"),
               scan=os.path.basename(src) if src else None)
    p = os.path.join(d, "gate-critic.json" if scan.get("scorer") == "critic" else "gate.json")
    json.dump(rec, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
    print("WROTE " + p)


def _opt(a, name):
    return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else None


def _opt_list(a, name):
    if name not in a:
        return []
    out = []
    for x in a[a.index(name) + 1:]:
        if x.startswith("--"):
            break
        out.append(x)
    return out


def _attach_shots(scan, a, out_dir):
    shots, bad = [], []
    explicit = _opt_list(a, "--shots")
    if explicit:
        s, b = shots_from(explicit)
        shots += s
        bad += b
    vdir = _opt(a, "--shots-from-visual")
    if vdir:
        paths = visual_shot_paths(vdir)
        s, b = shots_from(paths, vdir)
        shots += s
        bad += b
        if not paths:
            bad.append("no PNG screenshots found in %s/visual-qa/gate*.json" % vdir)
    if shots:
        scan["shots"] = shots
    for b in bad:
        print("note: screenshot not used: " + b)
    return scan


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        sys.exit(__doc__)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    out_dir = _opt(a, "--write")
    if a[0] == "image-stats":
        bad = 0
        for p in a[1:]:
            try:
                print(json.dumps(dict(path=p, **png_stats(p))))
            except Exception as e:
                bad += 1
                print("ERROR %s: %s" % (p, e))
        sys.exit(1 if bad else 0)
    if a[0] == "ingest":
        if len(a) < 2:
            sys.exit("ingest: console output file required")
        text = open(a[1], encoding="utf-8-sig", errors="replace").read() if a[1] != "-" else sys.stdin.read()
        try:
            scan = parse_console(text)
        except ValueError as e:
            sys.exit("ingest: %s" % e)
        if not scan:
            sys.exit("ingest: no LIGHTING_SCAN_PART lines found in " + a[1])
        if _opt(a, "--scorer"):
            scan["scorer"] = _opt(a, "--scorer")
        if _opt(a, "--game"):
            scan["game"] = _opt(a, "--game")
        scan.setdefault("scorer", "builder")
        scan.setdefault("captured_at", datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
        _attach_shots(scan, a, out_dir)
        if not out_dir:
            json.dump(scan, sys.stdout, indent=1)
            return
        d = os.path.join(out_dir, "lighting-qa")
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, (_opt(a, "--name") or "scan-%s" % scan["scorer"]) + ".json")
        json.dump(scan, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
        print("WROTE " + p)
        r = evaluate(scan, out_dir, _opt(a, "--project"), "critic" if scan["scorer"] == "critic" else None, _opt(a, "--genre"), _opt(a, "--platform"))
        print_result(r, scan)
        write_gate(out_dir, scan, r, p)
        sys.exit(0 if r["status"] == "pass" else 1)
    if a[0] == "recheck":
        scan = json.load(open(a[1], encoding="utf-8-sig"))
        rep = lighting_ref.verify(scan["state"], scan.get("config"))
        st = scan.get("report") or {}
        if st.get("status") == rep["status"] and sorted(st.get("failed") or []) == sorted(rep["failed"]):
            print("SAME %s (%s, failed %s)" % (a[1], rep["status"], rep["failed"]))
            sys.exit(0)
        print("DIFF %s: stored %s %s, re-check %s %s" % (a[1], st.get("status"), st.get("failed"), rep["status"], rep["failed"]))
        sys.exit(1)
    scan = json.load(open(a[0], encoding="utf-8-sig"))
    _attach_shots(scan, a, out_dir)
    gdir = os.path.dirname(os.path.abspath(a[0]))
    base = out_dir or (os.path.dirname(gdir) if os.path.basename(gdir) == "lighting-qa" else gdir)
    r = evaluate(scan, base, _opt(a, "--project"), _opt(a, "--scorer"), _opt(a, "--genre"), _opt(a, "--platform"))
    print_result(r, scan)
    if out_dir:
        write_gate(out_dir, scan, r, a[0])
    sys.exit(0 if r["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
