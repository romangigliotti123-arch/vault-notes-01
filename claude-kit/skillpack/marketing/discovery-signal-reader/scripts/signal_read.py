#!/usr/bin/env python3
"""signal_read.py - order the fixes for a game's discovery numbers. Stdlib only.

  python signal_read.py --ctr 1.4 --ptr 1.2 --bounce60 38 --bounce180 55 --d1 9 --d7 1.5 --session 8 [--payer 1.2 --likes 78] [--impressions-trend down] [--json]
  python signal_read.py --selftest

Every number is a percentage (session in minutes) read from Creator Hub analytics. The floors below are the vault's rough guides
(ads-stats-monetisation-playbook: D1 10%+, D7 2-3%, PTR over 1% floor, ad CTR drop line 1% and ~2.5% average, session 10+ min, payer
conversion 1-2%, likes ~80% warning line). They are indie or third-party heuristics, NOT Roblox rules; override with --floor name=value
after comparing with your own Analytics "similar experience" benchmarks. First-play bounce has NO published target: pass --bounce-limit
only if you have a benchmark; otherwise the tool only compares the two windows. Output order follows the playbook's decision tree:
packaging -> first-play bounce -> D1 -> D7 -> session -> payer conversion -> likes.
"""
import argparse
import json
import sys

FLOORS = {"ctr": 1.0, "ptr": 1.0, "d1": 10.0, "d7": 2.0, "session": 8.0, "payer": 1.0, "likes": 80.0}

FIX = {
    "ctr": ("packaging", "Thumbnail/icon/title are not earning clicks. Run thumbnail-maker + ctr-ab-test-planner. Do not run ads yet."),
    "ptr": ("packaging", "Impressions are not becoming plays. Test new thumbnails first, then check the title and genre match (ctr-ab-test-planner)."),
    "bounce": ("first minute", "Players leave in the first 60-180 s. Align icon with what they meet, shorten the intro, give an action at once (first-minute-designer)."),
    "d1": ("onboarding", "D1 low: onboarding, first reward, a clear next goal, a return hook such as daily reward or timed event. Do not scale ads."),
    "d7": ("mid-game", "D7 low: progression gap, social features, content cadence (updates-live-ops, event-planner)."),
    "session": ("pace", "Sessions short: add goals and pace; check crashes and load time (retention-diagnoser)."),
    "payer": ("monetisation", "Payer conversion low: cheap entry offer after the first win (price-ladder-planner, gamepass-maker)."),
    "likes": ("sentiment", "Like ratio low: read comments; monetisation pop-ups, bugs or paywalls are the usual cause."),
}


def read(v, floors, bounce_limit=None):
    out = []
    for key in ("ctr", "ptr"):
        if v.get(key) is not None and v[key] < floors[key]:
            out.append((key, "%s %.2f%% under %.2f%%" % (key.upper(), v[key], floors[key])))
    b60, b180 = v.get("bounce60"), v.get("bounce180")
    if bounce_limit is not None:
        for name, val in (("bounce60", b60), ("bounce180", b180)):
            if val is not None and val > bounce_limit:
                out.append(("bounce", "%s %.1f%% over your limit %.1f%%" % (name, val, bounce_limit)))
    for key in ("d1", "d7", "session", "payer", "likes"):
        if v.get(key) is not None and v[key] < floors[key]:
            out.append((key, "%s %.2f under %.2f" % (key, v[key], floors[key])))
    res = []
    for key, why in out:
        area, fix = FIX[key]
        res.append({"signal": key, "area": area, "why": why, "fix": fix})
    notes = []
    if bounce_limit is None and (b60 is not None or b180 is not None):
        notes.append("first-play bounce has no published target: compare it over time and against genre peers, not to a fixed line.")
    if v.get("trend") == "down" and not res:
        notes.append("impressions falling with healthy numbers: competitors may be improving or the Aug-2026 style distribution change is settling; do not judge on one day (weekly seasonality peaks Saturday).")
    if not res and not notes:
        notes.append("nothing under the floors. Re-read against your own similar-experience benchmark before concluding the game is healthy.")
    missing = [k for k in FLOORS if v.get(k) is None]
    if missing:
        notes.append("not provided: " + ", ".join(missing))
    return {"fix_order": res, "notes": notes}


def selftest():
    f = dict(FLOORS)
    r = read(dict(ctr=1.4, ptr=1.2, d1=9, d7=1.5, session=8), f)
    assert [x["signal"] for x in r["fix_order"]] == ["d1", "d7"], r
    r = read(dict(ctr=0.5, d1=5), f)
    assert r["fix_order"][0]["signal"] == "ctr" and r["fix_order"][1]["signal"] == "d1"
    r = read(dict(bounce60=40, bounce180=55), f)
    assert not r["fix_order"] and "no published target" in r["notes"][0]
    r = read(dict(bounce60=40), f, bounce_limit=30)
    assert r["fix_order"][0]["signal"] == "bounce"
    r = read(dict(ctr=3, ptr=3, d1=15, d7=3, session=12, payer=2, likes=90), f)
    assert not r["fix_order"] and "nothing under" in r["notes"][0]
    assert read(dict(trend="down", ctr=3), f)["notes"][0].startswith("impressions falling")
    print("selftest ok (6 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    for k in ("ctr", "ptr", "bounce60", "bounce180", "d1", "d7", "session", "payer", "likes"):
        ap.add_argument("--" + k, type=float)
    ap.add_argument("--impressions-trend", dest="trend", choices=["up", "flat", "down"])
    ap.add_argument("--bounce-limit", dest="bounce_limit", type=float)
    ap.add_argument("--floor", action="append", default=[], help="override a floor, e.g. --floor d1=12")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    floors = dict(FLOORS)
    for kv in a.floor:
        k, _, val = kv.partition("=")
        if k not in floors:
            ap.error("unknown floor %r (have %s)" % (k, ", ".join(floors)))
        floors[k] = float(val)
    v = {k: getattr(a, k) for k in ("ctr", "ptr", "bounce60", "bounce180", "d1", "d7", "session", "payer", "likes", "trend")}
    r = read(v, floors, a.bounce_limit)
    if a.json:
        print(json.dumps(r, indent=1))
    else:
        for i, x in enumerate(r["fix_order"], 1):
            print("%d. [%s] %s\n   -> %s" % (i, x["area"], x["why"], x["fix"]))
        for n in r["notes"]:
            print("note:", n)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
