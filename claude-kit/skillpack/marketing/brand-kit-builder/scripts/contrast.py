#!/usr/bin/env python3
"""contrast.py - WCAG contrast ratios for a brand palette. Stdlib only.

  python contrast.py --pair text=#FFFFFF,bg=#1B2A49 --pair accent=#FFD23F,bg=#1B2A49 [--large] [--json]
  python contrast.py --palette brand.json        # {"bg": "#1B2A49", "text": "#FFFFFF", "accent": "#FFD23F"}; checks every colour against bg
  python contrast.py --selftest

Ratio = (L1 + 0.05) / (L2 + 0.05) with WCAG 2.x relative luminance. Pass levels: 4.5 for normal text, 3.0 for large text and UI shapes.
The vault says to check text and UI colour contrast against WCAG or a contrast calculator and to avoid combinations such as white on
yellow (thumbnails-icons: "Verify text and UI contrast before shipping"). This tool is that calculator; it judges numbers, not taste.
Exit 1 when a pair is under its level.
"""
import argparse
import json
import re
import sys


def parse(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError("not a hex colour: %r" % h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = lum(parse(a)), lum(parse(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def judge(r, large):
    need = 3.0 if large else 4.5
    return ("PASS" if r >= need else "FAIL"), need


def selftest():
    assert abs(ratio("#000000", "#FFFFFF") - 21.0) < 1e-6
    assert abs(ratio("#fff", "#fff") - 1.0) < 1e-9
    assert judge(ratio("#FFFFFF", "#FFD23F"), False)[0] == "FAIL"  # white on yellow, the vault's named bad pair
    assert judge(ratio("#FFD23F", "#1B2A49"), False)[0] == "PASS"
    assert judge(2.9, False)[0] == "FAIL" and judge(3.0, True)[0] == "PASS"
    try:
        parse("blue")
        raise SystemExit("bad hex accepted")
    except ValueError:
        pass
    print("selftest ok (6 checks)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", action="append", default=[], help="fg_name=#hex,bg_name=#hex")
    ap.add_argument("--palette")
    ap.add_argument("--large", action="store_true", help="large text or UI shapes (3.0 level)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    pairs = []
    for p in a.pair:
        parts = dict(x.split("=", 1) for x in p.split(","))
        (fn, fv), (bn, bv) = list(parts.items())[0], list(parts.items())[1]
        pairs.append((fn, fv, bn, bv))
    if a.palette:
        pal = json.load(open(a.palette, encoding="utf-8"))
        bg = pal.get("bg")
        if not bg:
            ap.error("palette needs a 'bg' colour")
        for k, v in pal.items():
            if k != "bg":
                pairs.append((k, v, "bg", bg))
    if not pairs:
        ap.error("give --pair or --palette")
    out = []
    bad = 0
    for fn, fv, bn, bv in pairs:
        r = ratio(fv, bv)
        verdict, need = judge(r, a.large)
        bad += verdict == "FAIL"
        out.append({"fg": fn, "bg": bn, "ratio": round(r, 2), "need": need, "verdict": verdict})
    if a.json:
        print(json.dumps(out, indent=1))
    else:
        for o in out:
            print("%-4s %-10s on %-6s %5.2f:1 (need %.1f)" % (o["verdict"], o["fg"], o["bg"], o["ratio"], o["need"]))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
