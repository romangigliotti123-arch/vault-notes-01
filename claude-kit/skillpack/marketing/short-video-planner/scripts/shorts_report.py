#!/usr/bin/env python3
"""shorts_report.py - read the short-form tracker and say which format to repeat. Stdlib only.

  python shorts_report.py shorts-log.csv [--hit 1000] [--min-posts 3]
  python shorts_report.py --selftest

CSV columns: date, format, hook, views_7d, plays (plays attributed to the clip via tracked link; may be empty). Output:
  * your channel average views and each clip's ratio to it (vault: benchmark each short against your own average)
  * clips at or above --hit views (vault: find the over-1,000-view pattern; the 1,000 line is one creator's, change it with --hit)
  * per format: posts, average views, hit rate, plays per 1,000 views; a format is only ranked once it has --min-posts posts
No growth numbers are promised or inferred; with fewer than 10 clips the report says the sample is too small to decide.
"""
import argparse
import csv
import sys


def num(v):
    v = (v or "").strip().replace(",", "")
    return float(v) if v else None


def report(rows, hit=1000, min_posts=3):
    clips = []
    for r in rows:
        views = num(r.get("views_7d"))
        if views is None:
            continue
        clips.append({"format": (r.get("format") or "?").strip(), "hook": (r.get("hook") or "").strip(), "views": views, "plays": num(r.get("plays")), "date": r.get("date", "")})
    out = {"n": len(clips), "notes": [], "formats": [], "hits": []}
    if not clips:
        out["notes"].append("no clips with views_7d filled yet")
        return out
    avg = sum(c["views"] for c in clips) / len(clips)
    out["avg_views"] = avg
    out["hits"] = [c for c in clips if c["views"] >= hit]
    fm = {}
    for c in clips:
        fm.setdefault(c["format"], []).append(c)
    for name, cs in fm.items():
        v = sum(c["views"] for c in cs)
        p = [c["plays"] for c in cs if c["plays"] is not None]
        out["formats"].append({
            "format": name,
            "posts": len(cs),
            "avg_views": v / len(cs),
            "hit_rate": sum(1 for c in cs if c["views"] >= hit) / len(cs),
            "plays_per_1000_views": (1000.0 * sum(p) / sum(c["views"] for c in cs if c["plays"] is not None)) if p else None,
            "ranked": len(cs) >= min_posts,
        })
    out["formats"].sort(key=lambda f: (not f["ranked"], -f["avg_views"]))
    if len(clips) < 10:
        out["notes"].append("only %d clips: too small a sample to decide; keep posting and judge after 30-60 days." % len(clips))
    unranked = [f["format"] for f in out["formats"] if not f["ranked"]]
    if unranked:
        out["notes"].append("not ranked yet (under %d posts): %s" % (min_posts, ", ".join(unranked)))
    if not any(f["plays_per_1000_views"] is not None for f in out["formats"]):
        out["notes"].append("no attributed plays yet: add tracked links; views alone do not show players.")
    return out


def selftest():
    rows = [
        {"date": "d1", "format": "loop", "hook": "a", "views_7d": "2000", "plays": "40"},
        {"date": "d2", "format": "loop", "hook": "b", "views_7d": "500", "plays": "5"},
        {"date": "d3", "format": "loop", "hook": "c", "views_7d": "1,500", "plays": ""},
        {"date": "d4", "format": "fail", "hook": "d", "views_7d": "300", "plays": "1"},
        {"date": "d5", "format": "devlog", "hook": "e", "views_7d": "", "plays": ""},
    ]
    r = report(rows)
    assert r["n"] == 4 and abs(r["avg_views"] - 1075.0) < 1e-9, r
    assert len(r["hits"]) == 2
    f = {x["format"]: x for x in r["formats"]}
    assert f["loop"]["ranked"] and not f["fail"]["ranked"] and abs(f["loop"]["hit_rate"] - 2 / 3) < 1e-9
    assert abs(f["loop"]["plays_per_1000_views"] - 1000.0 * 45 / 2500) < 1e-9
    assert any("too small" in n for n in r["notes"])
    assert report([])["notes"][0].startswith("no clips")
    print("selftest ok (7 assertions)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--hit", type=float, default=1000)
    ap.add_argument("--min-posts", type=int, default=3, dest="min_posts")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv:
        ap.error("give the tracker csv")
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        r = report(list(csv.DictReader(f)), a.hit, a.min_posts)
    print("clips with views:", r["n"], "| average views: %.0f" % r.get("avg_views", 0))
    print("hits (>= %.0f views): %d" % (a.hit, len(r["hits"])))
    for h in r["hits"]:
        print("  - %s [%s] %.0f views: %s" % (h["date"], h["format"], h["views"], h["hook"]))
    for fmt in r["formats"]:
        print("format %-12s posts %-3d avg %.0f hit-rate %.0f%% plays/1000 views %s%s" % (
            fmt["format"], fmt["posts"], fmt["avg_views"], 100 * fmt["hit_rate"],
            "n/a" if fmt["plays_per_1000_views"] is None else "%.1f" % fmt["plays_per_1000_views"],
            "" if fmt["ranked"] else "  (not ranked)"))
    for n in r["notes"]:
        print("note:", n)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
