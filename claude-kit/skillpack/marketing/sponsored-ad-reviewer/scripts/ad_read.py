#!/usr/bin/env python3
"""ad_read.py - turn one ad campaign's numbers into the metrics and a first-pass verdict. Stdlib only.

  python ad_read.py --spend 70 --impressions 90000 --clicks 2250 --plays 2000 --hours 168 [--earnings 80] [--cohort-d1 0.11 --organic-d1 0.13]
                    [--ctr-drop 1.0 --ctr-good 2.5 --cpp-good 0.008 --roas-floor 100 --learning-hours 48] [--json]
  python ad_read.py --selftest

Money is in ONE unit of your choice (the playbook's CPP benchmarks are USD; pass USD to compare). Defaults come from the vault's
ads-stats-monetisation-playbook (CTR drop 1%, day-one target about 2.5%, CPP benchmark $0.008, ROAS 100% = break-even, learning 24-48 h).
They are knobs, not facts: the skill live-checks Ads Manager and passes current values. Earnings lag up to 30 days, so ROAS is only
final after the attribution window; this tool says so rather than guessing.
"""
import argparse
import json
import sys


def read(a):
    m = {}
    m["ctr_pct"] = 100.0 * a.clicks / a.impressions if a.impressions else None
    m["cost_per_click"] = a.spend / a.clicks if a.clicks else None
    m["cost_per_play"] = a.spend / a.plays if a.plays else None
    m["click_to_play_pct"] = 100.0 * a.plays / a.clicks if a.clicks else None
    m["cpm"] = 1000.0 * a.spend / a.impressions if a.impressions else None
    m["roas_pct"] = 100.0 * a.earnings / a.spend if (a.earnings is not None and a.spend) else None
    notes = []
    verdict = []
    if a.hours < a.learning_hours:
        verdict.append("TOO EARLY: %.0f h of data, the learning period is about %.0f h and restarts on each pause or edit. Change nothing." % (a.hours, a.learning_hours))
    ctr = m["ctr_pct"]
    cpp = m["cost_per_play"]
    if ctr is None:
        notes.append("no impressions: nothing to read")
    elif ctr < a.ctr_drop:
        verdict.append("CTR %.2f%% under %.1f%%: packaging problem. Replace the weakest thumbnails (ctr-ab-test-planner, thumbnail-maker)." % (ctr, a.ctr_drop))
    elif ctr < a.ctr_good:
        verdict.append("CTR %.2f%% between %.1f%% and %.1f%%: usable; test one new thumbnail variable." % (ctr, a.ctr_drop, a.ctr_good))
    else:
        verdict.append("CTR %.2f%% at or above %.1f%%: packaging is not the bottleneck." % (ctr, a.ctr_good))
    if cpp is not None and ctr is not None:
        if cpp > 2 * a.cpp_good and ctr >= a.ctr_drop:
            verdict.append("CPP %.4f is over twice the %.4f benchmark with CTR fine: clicks are not becoming plays. Check thumbnail/game mismatch and join friction." % (cpp, a.cpp_good))
        elif cpp > a.cpp_good:
            verdict.append("CPP %.4f above the %.4f benchmark: watch it and compare with Ads Manager." % (cpp, a.cpp_good))
        else:
            verdict.append("CPP %.4f at or under the %.4f benchmark." % (cpp, a.cpp_good))
    if m["click_to_play_pct"] is not None and m["click_to_play_pct"] < 50:
        notes.append("click-to-play %.0f%%: many clicks never start a session (loading, device, age gate)." % m["click_to_play_pct"])
    if m["roas_pct"] is None:
        notes.append("no earnings given: ROAS unknown. Plays and earnings finalise up to 30 days after the click.")
    elif m["roas_pct"] < a.roas_floor:
        verdict.append("ROAS %.0f%% under %.0f%%: do not scale. Fix retention or monetisation first; stop if still under after the attribution window." % (m["roas_pct"], a.roas_floor))
    else:
        verdict.append("ROAS %.0f%% at or over %.0f%%: may scale in modest steps while ad-cohort retention holds." % (m["roas_pct"], a.roas_floor))
    if a.cohort_d1 is not None and a.organic_d1 is not None:
        if a.cohort_d1 < 0.8 * a.organic_d1:
            verdict.append("Ad-cohort D1 %.1f%% is under 80%% of organic %.1f%% (heuristic, unsourced): paid players are not sticking; fix the game, not the budget." % (100 * a.cohort_d1, 100 * a.organic_d1))
        else:
            verdict.append("Ad-cohort D1 %.1f%% is close to organic %.1f%%." % (100 * a.cohort_d1, 100 * a.organic_d1))
    m["verdict"] = verdict
    m["notes"] = notes
    return m


class _A:
    pass


def _mk(**k):
    a = _A()
    d = dict(spend=70.0, impressions=90000, clicks=2250, plays=2000, hours=168.0, earnings=None, cohort_d1=None, organic_d1=None,
             ctr_drop=1.0, ctr_good=2.5, cpp_good=0.008, roas_floor=100.0, learning_hours=48.0)
    d.update(k)
    for kk, v in d.items():
        setattr(a, kk, v)
    return a


def selftest():
    m = read(_mk())
    assert abs(m["ctr_pct"] - 2.5) < 1e-9 and abs(m["cost_per_play"] - 0.035) < 1e-9, m
    assert any("CPP" in v and "twice" in v for v in m["verdict"]), m["verdict"]
    assert read(_mk(hours=10))["verdict"][0].startswith("TOO EARLY")
    assert any("packaging problem" in v for v in read(_mk(clicks=500))["verdict"])
    assert abs(read(_mk(earnings=140.0))["roas_pct"] - 200.0) < 1e-9
    assert any("do not scale" in v for v in read(_mk(earnings=35.0))["verdict"])
    assert any("not sticking" in v for v in read(_mk(cohort_d1=0.05, organic_d1=0.13))["verdict"])
    assert read(_mk(impressions=0, clicks=0, plays=0))["ctr_pct"] is None
    print("selftest ok (8 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--spend", type=float)
    ap.add_argument("--impressions", type=int)
    ap.add_argument("--clicks", type=int)
    ap.add_argument("--plays", type=int)
    ap.add_argument("--hours", type=float, help="hours the campaign has run")
    ap.add_argument("--earnings", type=float, help="attributed earnings in the same unit as spend")
    ap.add_argument("--cohort-d1", type=float, dest="cohort_d1", help="ad cohort D1 as a fraction, e.g. 0.11")
    ap.add_argument("--organic-d1", type=float, dest="organic_d1")
    ap.add_argument("--ctr-drop", type=float, dest="ctr_drop", default=1.0)
    ap.add_argument("--ctr-good", type=float, dest="ctr_good", default=2.5)
    ap.add_argument("--cpp-good", type=float, dest="cpp_good", default=0.008)
    ap.add_argument("--roas-floor", type=float, dest="roas_floor", default=100.0)
    ap.add_argument("--learning-hours", type=float, dest="learning_hours", default=48.0)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    for k in ("spend", "impressions", "clicks", "plays", "hours"):
        if getattr(a, k) is None:
            ap.error("--%s is required" % k)
    m = read(a)
    if a.json:
        print(json.dumps(m, indent=1))
    else:
        for k in ("ctr_pct", "cost_per_click", "cost_per_play", "click_to_play_pct", "cpm", "roas_pct"):
            print("%-18s %s" % (k, "n/a" if m[k] is None else "%.4f" % m[k]))
        for v in m["verdict"]:
            print("-", v)
        for n in m["notes"]:
            print("note:", n)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
