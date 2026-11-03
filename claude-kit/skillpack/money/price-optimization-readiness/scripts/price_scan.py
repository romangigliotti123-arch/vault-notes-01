#!/usr/bin/env python3
"""price_scan.py - find hard-coded Robux prices in a project's Luau so prices can come from the platform instead. Stdlib only.

  python price_scan.py <project-dir> [--json]
  python price_scan.py --selftest

Why: the vault (monetisation-gamepasses.md / pricing.md, Roblox Creator Docs 2026-10) says Price Optimization needs prices scripted through
MarketplaceService (GetProductInfo with Enum.InfoType.Product or GamePass), not hard-coded, so tested and discounted prices display correctly;
the platform's own Dynamic Price Check finds hard-coded prices with test accounts. This is the offline first pass of that.
Flags in *.lua / *.luau (skips Packages, node_modules, .git):
  HARD  a string or number that reads like a price next to the word Robux or R$ (e.g. "Buy for 99 Robux", "R$ 250")
  HARD  an assignment such as `price = 99` / `Price = 99` / `priceInRobux = 99`
Also reports whether GetProductInfo appears anywhere (INFO). A clean scan does NOT prove eligibility: the 30-day transaction minimum, which products are
included, and the current rules are platform-side (live-check price-optimization docs). Exit 1 when any HARD finding exists.
"""
import argparse
import json
import os
import re
import sys
import tempfile

SKIP = {"Packages", "node_modules", ".git", "ServerPackages"}
TEXT_PRICE = re.compile(r"""(?:["'`][^"'`\n]*\b(\d[\d,]*)\s*(?:Robux|R\$)|["'`][^"'`\n]*(?:R\$|Robux)\s*(\d[\d,]*))""", re.I)
ASSIGN_PRICE = re.compile(r"""\b(?:price|priceInRobux|cost|robuxPrice)\s*=\s*(\d+)\b""", re.I)


def scan_text(text, path="<text>"):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        code = "" if line.lstrip().startswith("--") else line
        m = TEXT_PRICE.search(code)
        if m:
            hits.append({"file": path, "line": i, "kind": "HARD", "text": line.strip()[:120], "why": "price written in a string"})
            continue
        m = ASSIGN_PRICE.search(code)
        if m:
            hits.append({"file": path, "line": i, "kind": "HARD", "text": line.strip()[:120], "why": "price assigned as a number"})
    return hits


def scan_dir(root):
    hits, uses_info, files = [], False, 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in fn:
            if f.endswith((".lua", ".luau")):
                p = os.path.join(dp, f)
                files += 1
                with open(p, encoding="utf-8", errors="replace") as fh:
                    t = fh.read()
                if "GetProductInfo" in t:
                    uses_info = True
                hits += scan_text(t, os.path.relpath(p, root))
    return {"files": files, "hard": hits, "uses_get_product_info": uses_info}


def selftest():
    h = scan_text('label.Text = "Buy for 99 Robux"\nlocal price = 150\nlocal ok = info.PriceInRobux\n-- price = 5\n')
    assert [x["line"] for x in h] == [1, 2], h
    assert scan_text('print("R$ 250")')[0]["kind"] == "HARD"
    assert scan_text("local cost = tonumber(x)") == []
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "src"))
        os.makedirs(os.path.join(d, "Packages"))
        with open(os.path.join(d, "src", "a.luau"), "w", encoding="utf-8") as fh:
            fh.write("local info = MarketplaceService:GetProductInfo(id, Enum.InfoType.Product)\nprice = 10\n")
        with open(os.path.join(d, "Packages", "b.luau"), "w", encoding="utf-8") as fh:
            fh.write("price = 77\n")
        r = scan_dir(d)
        assert r["files"] == 1 and len(r["hard"]) == 1 and r["uses_get_product_info"], r
    print("price_scan selftest: 4 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.dir:
        ap.error("project directory required")
    r = scan_dir(a.dir)
    if a.json:
        print(json.dumps(r, indent=2))
    else:
        for h in r["hard"]:
            print("HARD  %s:%d  %s  [%s]" % (h["file"], h["line"], h["text"], h["why"]))
        print("INFO  GetProductInfo %s in %d file(s) scanned" % ("used" if r["uses_get_product_info"] else "NOT found", r["files"]))
        print("%d hard-coded price(s). Clean here is not proof of eligibility: live-check the Price Optimization docs." % len(r["hard"]))
    return 1 if r["hard"] else 0


if __name__ == "__main__":
    sys.exit(main())
