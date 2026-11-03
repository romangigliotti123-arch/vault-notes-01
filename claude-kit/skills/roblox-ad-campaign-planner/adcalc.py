#!/usr/bin/env python3
"""adcalc.py - deterministic budget/schedule arithmetic for a Roblox ad test. Everything it prints is an ESTIMATE from your assumptions.

  python adcalc.py --daily 10 --days 10 [--cost-per-play 0.010] [--ctr 2.5] [--d1 12] [--payer 1.5 --arppu 300 --robux-usd 0.0035]
  python adcalc.py --total 100 --days 10          (derives the daily budget)
  python adcalc.py --total 100 --daily 10         (derives the duration)

Defaults come from the KB (indie, self-reported): cost per play ~$0.008-0.013 (Roblox says as low as ~1 cent), CTR 2.5% average.
Outputs: budget table, expected clicks/plays at three cost-per-play scenarios, expected D1 returners, a day-by-day checkpoint schedule with go/no-go rules,
and break-even Robux per player if you give a payout rate. Re-check numbers against the live Ads Manager before spending anything.
"""
import argparse
import math
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--daily", type=float)
    ap.add_argument("--days", type=float)
    ap.add_argument("--total", type=float)
    ap.add_argument("--cost-per-play", type=float, default=0.010, help="USD per play (KB indie ~0.008-0.013)")
    ap.add_argument("--ctr", type=float, default=2.5, help="percent (KB: <1 replace, ~2.5 average, 3.5+ exceptional)")
    ap.add_argument("--d1", type=float, default=12.0, help="D1 retention percent of ad cohort (KB indie 10-16)")
    ap.add_argument("--payer", type=float, default=None, help="payer conversion percent")
    ap.add_argument("--arppu", type=float, default=None, help="Robux per paying user")
    ap.add_argument("--robux-usd", type=float, default=0.0035, help="USD per Earned Robux via DevEx: KB (official, 2026-10) legacy 0.0035; higher 0.0054 for US 18+ verified purchases")
    ap.add_argument("--creator-share", type=float, default=0.70, help="share of the sale price you earn (KB: creator earns 70 on 100 Robux)")
    a = ap.parse_args()

    if a.daily and a.days:
        daily, days = a.daily, a.days
        total = daily * days
    elif a.total and a.days:
        total, days = a.total, a.days
        daily = total / days
    elif a.total and a.daily:
        total, daily = a.total, a.daily
        days = math.ceil(total / daily)
    else:
        ap.error("give two of --daily --days --total")

    print("## Budget (ESTIMATE from your assumptions)\n")
    print("| Item | Value |\n|---|---|")
    print("| Daily budget | $%.2f |" % daily)
    print("| Days | %g |" % days)
    print("| Total spend | $%.2f |" % total)
    print()
    print("## Scenarios\n")
    print("| Scenario | Cost per play | Plays | Impressions needed at CTR %.1f%% | D1 returners (D1 %.0f%%) |" % (a.ctr, a.d1))
    print("|---|---|---|---|---|")
    for name, cpp in (("Good (Roblox cold-start claim ~1c or better)", 0.008), ("Base (your input)", a.cost_per_play), ("Poor", max(a.cost_per_play * 2, 0.02))):
        plays = total / cpp
        impressions = plays / (a.ctr / 100.0)
        print("| %s | $%.4f | %s | %s | %s |" % (name, cpp, "{:,.0f}".format(plays), "{:,.0f}".format(impressions), "{:,.0f}".format(plays * a.d1 / 100.0)))
    print("\nNote: impressions = plays / CTR assumes every click becomes a play (upper bound on clicks per play); real funnels leak, so treat plays as optimistic.")
    if a.payer and a.arppu:
        plays = total / a.cost_per_play
        payers = plays * a.payer / 100.0
        robux = payers * a.arppu * a.creator_share
        usd = robux * a.robux_usd
        print("\n## Break-even check (ESTIMATE; ARPPU is per payer over the period you measure, usually far lower for a brand-new cohort)\n")
        print("- Payers: %s; Earned Robux (spend x %.0f%% share): %s; USD at $%.4f/Earned Robux: $%.2f vs ad spend $%.2f -> ROAS %.0f%%" % ("{:,.0f}".format(payers), 100 * a.creator_share, "{:,.0f}".format(robux), a.robux_usd, usd, total, 100 * usd / total))
        print("- Official ads data (KB) says ROAS above 100% is reachable for earnings-objective campaigns reinvesting a small share of daily earnings; do not expect this from a brand-new game.")
    print("\n## Checkpoints (go/no-go rules from the KB; adjust to your thresholds)\n")
    cps = sorted(set([1, 3, 5, 7, int(days)]))
    print("| Day | Check | Go | No-go |\n|---|---|---|---|")
    for d in cps:
        if d > days:
            continue
        if d == 1:
            chk, go, no = "CTR, impressions delivered, cost per play", "CTR >= 1.5%, spend on pace", "CTR < 1%: replace the creative (do not raise budget)"
        elif d == 3:
            chk, go, no = "Cohort D1 of day-1 players (Analytics > Retention by first-play date), cost per play", "D1 within 10-16% or improving; cost per play <= ~$0.013", "D1 below ~6%: pause ads and fix the game (ads cannot rescue weak retention)"
        elif d == 5:
            chk, go, no = "Acquisition tab: Home recommendations vs sponsored impressions", "Home impressions growing", "Zero organic uplift after 5 days: keep fixing retention/PTR before extending"
        elif d == 7:
            chk, go, no = "PTR, first-play bounce, session length, favourites", "Bounce falling, session >= ~7 min", "Bounce high / session < 5 min: fix first session"
        else:
            chk, go, no = "Overall: organic vs sponsored, payer conversion, ROAS", "Organic Home impressions exceed sponsored: stop ads", "Still mostly sponsored: pause, iterate, retest later (no repeated restarts)"
        print("| %d | %s | %s | %s |" % (d, chk, go, no))
    print("\nSources for the thresholds: run `kbq.py find \"ad budget per day duration stop\" -t ads-and-sponsored-experiences` and cite what it returns. Roblox guidance in the KB: run at least 1-2 weeks, judge after 3-5 days minimum.")


if __name__ == "__main__":
    main()
