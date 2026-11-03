#!/usr/bin/env python3
"""ad_plan.py - check a rewarded-video plan against the vault's targets and estimate daily volume. Stdlib only.

  python ad_plan.py --dau 150000 --optin 0.12 --views 3.5 --reward-rate 0.92 --length 20 --placement lobby,death,results
  python ad_plan.py --selftest

Vault targets (monetisation-other.md "Rewarded video: placement, rewards, eligibility", Roblox Creator Docs 2026-10; fast-moving, live-check):
  reward rate >= 90%, opt-in >= 10%, views per opted-in player per day >= 3, video length 6-30 s,
  placements at natural breaks (lobby, death, results) and never mid-fight, eligibility roughly 100k DAU during the beta.
  Reported uplift for context only: up to 3% of revenue early, 5-10% long term (Driving Empire about 7%).
The tool judges the numbers you give it; it cannot see your UI. Exit 1 when any target fails.
"""
import argparse
import sys

GOOD_PLACEMENTS = {"lobby", "death", "results", "respawn", "menu", "between_rounds"}
BAD_PLACEMENTS = {"midfight", "mid_fight", "combat", "midrun", "mid_run", "join"}


def plan(dau, optin, views, reward_rate, length, placements, dau_floor=100000):
    checks = []

    def add(name, ok, detail):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    add("DAU near the beta floor", dau >= dau_floor, "%d DAU vs about %d (live-check eligibility)" % (dau, dau_floor))
    add("opt-in >= 10%", optin >= 0.10, "%.1f%%" % (optin * 100))
    add("views per opted-in player >= 3/day", views >= 3, "%.1f" % views)
    add("reward rate >= 90%", reward_rate >= 0.90, "%.1f%%" % (reward_rate * 100))
    add("video length 6-30 s", 6 <= length <= 30, "%d s" % length)
    bad = [p for p in placements if p in BAD_PLACEMENTS]
    unknown = [p for p in placements if p not in GOOD_PLACEMENTS and p not in BAD_PLACEMENTS]
    add("no placement mid-fight/run/join", not bad, ", ".join(bad) or "none")
    add("placements are natural breaks", bool(placements) and not unknown and not bad,
        "unrecognised: " + ", ".join(unknown) if unknown else "ok")
    daily_views = dau * optin * views
    return {"daily_views": round(daily_views), "checks": checks, "ok": all(c["ok"] for c in checks)}


def selftest():
    r = plan(150000, 0.12, 3.5, 0.92, 20, ["lobby", "death"])
    assert r["ok"] and r["daily_views"] == 63000, r
    r = plan(50000, 0.05, 1, 0.8, 45, ["midfight"])
    assert not r["ok"] and sum(1 for c in r["checks"] if not c["ok"]) == 7, r
    r = plan(150000, 0.12, 3.5, 0.92, 20, ["settings_tab"])
    assert [c["ok"] for c in r["checks"]][-1] is False
    r = plan(150000, 0.12, 3.5, 0.92, 20, [])
    assert not r["ok"]
    print("ad_plan selftest: 4 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dau", type=int)
    ap.add_argument("--optin", type=float, help="share of players who opt in, 0-1")
    ap.add_argument("--views", type=float, help="views per opted-in player per day")
    ap.add_argument("--reward-rate", type=float, help="share of started videos that finish and reward, 0-1")
    ap.add_argument("--length", type=int, help="video length in seconds")
    ap.add_argument("--placement", default="", help="comma list: lobby,death,results,...")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    for k in ("dau", "optin", "views", "reward_rate", "length"):
        if getattr(a, k) is None:
            ap.error("--%s is required" % k.replace("_", "-"))
    r = plan(a.dau, a.optin, a.views, a.reward_rate, a.length, [p for p in a.placement.split(",") if p])
    for c in r["checks"]:
        print("%-4s %-38s %s" % ("ok" if c["ok"] else "FAIL", c["check"], c["detail"]))
    print("Expected rewarded views per day: %d (dau x opt-in x views)" % r["daily_views"])
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
