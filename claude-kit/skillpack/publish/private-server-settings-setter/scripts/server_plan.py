#!/usr/bin/env python3
"""server_plan.py <plan.json> [--scan <project>] | --template | --selftest

Checks a private-server / teleport plan for the conflicts the Creator Docs private-servers and teleport pages describe (2026-10-28
snapshot; live-check, policies and prices change). Plan JSON:
  {"access": "public", "private_servers": {"enabled": true, "price_robux": 100, "previous_price_robux": 100, "ack_price_change_cancels_subs": false},
   "paid_access": false, "max_players": 20, "reserved_servers": true}
Checks: private servers need a public experience; paid access and private servers cannot both be on; changing a non-zero price cancels
active subscriptions and needs the explicit ack; price must be a non-negative integer you set from the live dashboard (never invented);
max_players >= 1. With --scan: client-side TeleportService:Teleport( calls (deprecated per the docs), SetTeleportData lines mentioning
currency/inventory/token/secret (teleport data is client-visible), and ReservedServerId built without GenerateGUID. Exit 1 on FAIL, 2 on bad input.
"""
import json
import os
import re
import sys
import tempfile


def check(p):
    out = []
    ps = p.get("private_servers") or {}
    if ps.get("enabled") and p.get("access") not in (None, "public"):
        out.append(("FAIL", "private servers need a public experience (access=%r)" % p.get("access")))
    if ps.get("enabled") and p.get("paid_access"):
        out.append(("FAIL", "paid access and private servers cannot be on together"))
    if ps.get("enabled"):
        price, prev = ps.get("price_robux"), ps.get("previous_price_robux")
        if price is not None and (not isinstance(price, int) or price < 0):
            out.append(("FAIL", "price_robux must be a non-negative integer read from the dashboard"))
        elif price is None:
            out.append(("WARN", "private server price undecided"))
        if isinstance(price, int) and isinstance(prev, int) and prev > 0 and price != prev:
            if ps.get("ack_price_change_cancels_subs"):
                out.append(("WARN", "price change %d -> %d cancels active subscriptions (acknowledged; players get an inbox message)" % (prev, price)))
            else:
                out.append(("FAIL", "price change %d -> %d cancels active subscriptions: set ack_price_change_cancels_subs only if intended" % (prev, price)))
    mp = p.get("max_players")
    if mp is not None and (not isinstance(mp, int) or mp < 1):
        out.append(("FAIL", "max_players must be an integer >= 1"))
    if not any(lv == "FAIL" for lv, _ in out):
        out.append(("OK", "plan has no internal conflicts"))
    return out


def scan(root):
    out = []
    for d, _, names in os.walk(root):
        if any(x in d.replace("\\", "/") for x in ("/.git", "/Packages")):
            continue
        for n in names:
            if not n.endswith((".luau", ".lua")):
                continue
            rel = os.path.relpath(os.path.join(d, n), root).replace("\\", "/")
            for i, line in enumerate(open(os.path.join(d, n), encoding="utf-8", errors="replace").read().splitlines(), 1):
                if line.strip().startswith("--"):
                    continue
                if re.search(r"TeleportService[:.]Teleport\(", line):
                    out.append(("WARN", "legacy TeleportService:Teleport( (docs: use server-side TeleportAsync)", "%s:%d" % (rel, i)))
                if re.search(r"SetTeleportData", line) and re.search(r"(coin|cash|gem|robux|inventory|token|secret|currency|data)", line, re.I):
                    out.append(("FAIL", "SetTeleportData with value-bearing names: teleport data is client-visible, persist with DataStores", "%s:%d" % (rel, i)))
                if re.search(r"ReserveServer\(", line) and "GenerateGUID" in line:
                    out.append(("WARN", "GenerateGUID near ReserveServer: confirm it is for ReservedServerId in TeleportOptions, not the ReserveServer code", "%s:%d" % (rel, i)))
    return out


def selftest():
    ok = {"access": "public", "private_servers": {"enabled": True, "price_robux": 50, "previous_price_robux": 50}, "max_players": 12}
    assert [x[0] for x in check(ok)] == ["OK"]
    bad = {"access": "friends", "paid_access": True, "private_servers": {"enabled": True, "price_robux": 60, "previous_price_robux": 50}, "max_players": 0}
    assert [x[0] for x in check(bad)].count("FAIL") == 4, check(bad)
    ack = {"access": "public", "private_servers": {"enabled": True, "price_robux": 60, "previous_price_robux": 50, "ack_price_change_cancels_subs": True}}
    assert [x[0] for x in check(ack)] == ["WARN", "OK"], check(ack)
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write("TeleportService:Teleport(1, p)\nopts:SetTeleportData({coins = 5})\n-- SetTeleportData(token)\n")
        s = scan(d)
        assert [x[0] for x in s] == ["WARN", "FAIL"], s
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--template" in argv:
        print(json.dumps({"access": "", "private_servers": {"enabled": False, "price_robux": None, "previous_price_robux": None,
                                                           "ack_price_change_cancels_subs": False}, "paid_access": False, "max_players": None,
                          "reserved_servers": False}, indent=2))
        return 0
    rest = list(argv)
    proj = None
    if "--scan" in rest:
        i = rest.index("--scan")
        proj = rest[i + 1] if i + 1 < len(rest) else None
        del rest[i:i + 2]
    if len(rest) != 1:
        print(__doc__)
        return 2
    try:
        plan = json.load(open(rest[0], encoding="utf-8"))
        assert isinstance(plan, dict)
        if proj is not None:
            assert os.path.isdir(proj)
    except Exception as e:
        print("bad input: %s" % e)
        return 2
    rows = [(a, b, "") for a, b in check(plan)] + (scan(proj) if proj else [])
    for lv, m, at in rows:
        print("[%s] %s%s" % (lv, m, "  <- " + at if at else ""))
    print("2026-10-28 docs snapshot: live-check private server and teleport pages")
    return 1 if any(r[0] == "FAIL" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
