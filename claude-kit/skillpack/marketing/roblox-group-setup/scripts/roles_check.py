#!/usr/bin/env python3
"""roles_check.py - lint a group role plan for least privilege. Stdlib only.

  python roles_check.py roles.csv [--max-money-holders 2]
  python roles_check.py --selftest

CSV columns: person, role, permissions (semicolon list), twosv (yes/no). Money permissions are the words payouts, revenue,
ad_account, ad_invoices, analytics, ownership (the names are yours; the live Roblox permission names change, so map them first).
Checks:
  money-holders  more than --max-money-holders people hold any money permission (vault: restrict payouts, analytics and ad invoices to trusted roles)
  twosv          anyone with a money permission without twosv=yes (vault: sensitive permissions need two-step verification)
  ownership      more than one person holds ownership; a non-owner holds ownership
  collaborator   a role literally named collaborator, member or tester holding a money permission
Exit 1 on FAIL. It checks the plan, not the real group: the owner verifies in Roblox.
"""
import argparse
import csv
import sys

MONEY = {"payouts", "revenue", "ad_account", "ad_invoices", "analytics", "ownership"}


def check(rows, max_money=2):
    out = []
    holders = {}
    for r in rows:
        perms = {p.strip().lower() for p in (r.get("permissions") or "").split(";") if p.strip()}
        r["_perms"] = perms
        if perms & MONEY:
            holders[r["person"]] = r
    out.append(("money-holders", "FAIL" if len(holders) > max_money else "PASS", "%d people with money permissions (max %d): %s" % (len(holders), max_money, ", ".join(sorted(holders)) or "none")))
    no2 = [p for p, r in holders.items() if (r.get("twosv") or "").strip().lower() != "yes"]
    out.append(("twosv", "FAIL" if no2 else "PASS", "no 2SV: %s" % ", ".join(no2) if no2 else "all money holders have 2SV"))
    owners = [r["person"] for r in rows if "ownership" in r["_perms"]]
    own_bad = len(owners) > 1 or any((r.get("role") or "").strip().lower() != "owner" for r in rows if "ownership" in r["_perms"])
    out.append(("ownership", "FAIL" if own_bad else "PASS", "ownership: %s" % (", ".join(owners) or "nobody")))
    weak = [r["person"] for r in rows if (r.get("role") or "").strip().lower() in ("collaborator", "member", "tester") and r["_perms"] & MONEY]
    out.append(("collaborator", "FAIL" if weak else "PASS", "low roles with money permissions: %s" % ", ".join(weak) if weak else "none"))
    return out


def selftest():
    ok = [
        {"person": "ann", "role": "Owner", "permissions": "ownership;payouts;analytics", "twosv": "yes"},
        {"person": "bob", "role": "Developer", "permissions": "analytics", "twosv": "yes"},
        {"person": "cy", "role": "Moderator", "permissions": "wall;kick", "twosv": "no"},
    ]
    assert all(s == "PASS" for n, s, m in check([dict(r) for r in ok])), check([dict(r) for r in ok])
    bad = [dict(r) for r in ok]
    bad[1]["twosv"] = "no"
    assert {n: s for n, s, m in check(bad)}["twosv"] == "FAIL"
    many = [dict(r) for r in ok] + [{"person": "di", "role": "Developer", "permissions": "revenue", "twosv": "yes"}]
    assert {n: s for n, s, m in check(many)}["money-holders"] == "FAIL"
    own = [dict(r) for r in ok]
    own[1]["permissions"] = "ownership"
    assert {n: s for n, s, m in check(own)}["ownership"] == "FAIL"
    low = [dict(r) for r in ok]
    low[2]["role"] = "Tester"
    low[2]["permissions"] = "payouts"
    assert {n: s for n, s, m in check(low)}["collaborator"] == "FAIL"
    print("selftest ok (5 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--max-money-holders", type=int, default=2, dest="max_money")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv:
        ap.error("give the roles csv")
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        res = check(list(csv.DictReader(f)), a.max_money)
    for n, s, m in res:
        print("%-4s %-14s %s" % (s, n, m))
    return 1 if any(s == "FAIL" for n, s, m in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
