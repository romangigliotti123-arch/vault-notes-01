#!/usr/bin/env python3
"""shot_check.py - check a video shot list CSV against the mode's structure. Stdlib only.

  python shot_check.py shots.csv --mode external|page|ad [--min-total 60 --max-total 90 --hook-max 10]
  python shot_check.py --selftest

CSV columns: start, end, scene, in_game (yes/no), text_overlay (yes/no), voiceover (yes/no). start/end are seconds or m:ss.
Checks:
  exists      every shot has in_game=yes (never show a feature the game does not have today)
  contiguous  shots are in order, no overlaps, no gaps over 0.5 s
  total       external: total within --min-total..--max-total (vault: 60-90 s, rasdev, indie); page/ad: no total rule here
  hook        external: the first shot ends within --hook-max seconds (vault: 5-10 s high-action hook)
  page-rules  page mode: no text overlay and no voiceover on any shot (vault: official page-video guidelines). The tool
              cannot see cinematic style, lyrics or real-life footage: those stay human checks.
Limits are arguments because Roblox's video rules and your platform's limits change: pass the live values.
"""
import argparse
import csv
import sys


def secs(v):
    v = str(v).strip()
    if ":" in v:
        m, s = v.split(":", 1)
        return int(m) * 60 + float(s)
    return float(v)


def check(rows, mode, min_total=60.0, max_total=90.0, hook_max=10.0):
    out = []
    shots = []
    for i, r in enumerate(rows, 1):
        shots.append((i, secs(r["start"]), secs(r["end"]), r))
    bad = [i for i, a, b, r in shots if (r.get("in_game") or "").strip().lower() != "yes"]
    out.append(("exists", "FAIL" if bad else "PASS", "shots not in the game today: %s" % bad if bad else "all shots exist"))
    prob = []
    prev_end = None
    for i, a, b, r in shots:
        if b <= a:
            prob.append("shot %d ends before it starts" % i)
        if prev_end is not None and a < prev_end - 1e-9:
            prob.append("shot %d overlaps the previous" % i)
        if prev_end is not None and a - prev_end > 0.5:
            prob.append("gap before shot %d" % i)
        prev_end = b
    out.append(("contiguous", "FAIL" if prob else "PASS", "; ".join(prob) if prob else "in order, no gaps"))
    total = (shots[-1][2] - shots[0][1]) if shots else 0.0
    if mode == "external":
        ok = min_total <= total <= max_total
        out.append(("total", "PASS" if ok else "FAIL", "%.1f s (want %.0f-%.0f)" % (total, min_total, max_total)))
        hook_end = shots[0][2] - shots[0][1] if shots else 0
        out.append(("hook", "PASS" if hook_end <= hook_max else "FAIL", "first shot %.1f s (hook max %.0f)" % (hook_end, hook_max)))
    else:
        out.append(("total", "PASS", "%.1f s (no total rule applied in %s mode: check the live limit)" % (total, mode)))
    if mode == "page":
        flagged = [i for i, a, b, r in shots if (r.get("text_overlay") or "").strip().lower() == "yes" or (r.get("voiceover") or "").strip().lower() == "yes"]
        out.append(("page-rules", "FAIL" if flagged else "PASS", "overlay or voiceover on shots %s" % flagged if flagged else "no overlay or voiceover"))
    return out


def selftest():
    good = [
        {"start": "0", "end": "8", "scene": "hook", "in_game": "yes", "text_overlay": "no", "voiceover": "no"},
        {"start": "8", "end": "40", "scene": "features", "in_game": "yes", "text_overlay": "no", "voiceover": "no"},
        {"start": "0:40", "end": "1:15", "scene": "more", "in_game": "yes", "text_overlay": "no", "voiceover": "no"},
    ]
    r = {n: s for n, s, m in check(good, "external")}
    assert all(v == "PASS" for v in r.values()), r
    bad = [dict(x) for x in good]
    bad[1]["in_game"] = "no"
    assert {n: s for n, s, m in check(bad, "external")}["exists"] == "FAIL"
    gap = [dict(x) for x in good]
    gap[2]["start"] = "0:50"
    assert {n: s for n, s, m in check(gap, "external")}["contiguous"] == "FAIL"
    short = good[:2]
    assert {n: s for n, s, m in check(short, "external")}["total"] == "FAIL"
    slow = [dict(x) for x in good]
    slow[0]["end"] = "20"
    slow[1]["start"] = "20"
    assert {n: s for n, s, m in check(slow, "external")}["hook"] == "FAIL"
    pg = [dict(x) for x in good]
    pg[0]["voiceover"] = "yes"
    assert {n: s for n, s, m in check(pg, "page")}["page-rules"] == "FAIL"
    assert {n: s for n, s, m in check(good, "page")}["page-rules"] == "PASS"
    print("selftest ok (8 assertions)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--mode", choices=["external", "page", "ad"])
    ap.add_argument("--min-total", type=float, default=60.0, dest="min_total")
    ap.add_argument("--max-total", type=float, default=90.0, dest="max_total")
    ap.add_argument("--hook-max", type=float, default=10.0, dest="hook_max")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv or not a.mode:
        ap.error("csv and --mode are required")
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    res = check(rows, a.mode, a.min_total, a.max_total, a.hook_max)
    for n, s, m in res:
        print("%-4s %-11s %s" % (s, n, m))
    return 1 if any(s == "FAIL" for n, s, m in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
