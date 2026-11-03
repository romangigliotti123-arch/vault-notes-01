#!/usr/bin/env python3
"""pincheck.py - check that tool and package versions are pinned exactly. Stdlib only.

  python pincheck.py rokit.toml [wally.toml ...] [--against template/rokit.toml]
  python pincheck.py --selftest

Reads simple `name = "owner/repo@1.2.3"` (rokit.toml, aftman.toml) and `Name = "scope/name@1.2.3"` (wally.toml
[dependencies]) lines. FAIL for: no @version, @latest, '*', '^', '~', '>=', '<' ranges. With --against, WARN for tools present
in one file and not the other and for different versions (drift). It does not fetch the network: whether a pinned version is the
newest or still safe is a live check on the tool's release page. Exit 0 pass (drift is a warning), 1 on an unpinned entry.
"""
import argparse
import re
import sys

LINE = re.compile(r'^\s*([A-Za-z0-9_.-]+)\s*=\s*"([^"]+)"\s*(?:#.*)?$')
EXACT = re.compile(r"@\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def parse(text):
    out, section = {}, ""
    for ln in text.splitlines():
        s = ln.strip()
        if s.startswith("["):
            section = s.strip("[]").lower()
            continue
        if section not in ("tools", "dependencies", "server-dependencies", "dev-dependencies"):
            continue
        m = LINE.match(ln)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def check(pins):
    errs = []
    for name, spec in pins.items():
        if "@" not in spec:
            errs.append("%s: no @version in %r" % (name, spec))
        elif not EXACT.search(spec):
            errs.append("%s: %r is not an exact x.y.z pin" % (name, spec))
    return errs


def drift(a, b):
    w = []
    for k in sorted(set(a) | set(b)):
        if k not in a:
            w.append("%s only in template" % k)
        elif k not in b:
            w.append("%s only in project" % k)
        elif a[k] != b[k]:
            w.append("%s differs: project %s vs template %s" % (k, a[k], b[k]))
    return w


def selftest():
    good = '[tools]\nrojo = "rojo-rbx/rojo@7.7.1"\nstylua = "JohnnyMorganz/StyLua@2.3.1"  # fmt\n'
    assert check(parse(good)) == []
    bad = good + 'selene = "Kampfkarren/selene"\nlune = "lune-org/lune@latest"\nwally = "UpliftGames/wally@^0.3"\n'
    e = check(parse(bad))
    assert len(e) == 3, e
    w = 'Promise = "evaera/promise@4.0.0"\n'
    assert parse("[package]\nname = \"x\"\n[dependencies]\n" + w) == {"Promise": "evaera/promise@4.0.0"}
    d = drift(parse(good), parse(good.replace("7.7.1", "7.6.0") + 'lune = "lune-org/lune@0.10.4"\n'))
    assert len(d) == 2 and any("differs" in x for x in d) and any("only in template" in x for x in d), d
    print("selftest ok (4 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--against")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.files:
        ap.error("file required")
    bad = 0
    allpins = {}
    for f in a.files:
        pins = parse(open(f, encoding="utf-8").read())
        allpins.update(pins)
        for e in check(pins):
            print("FAIL %s: %s" % (f, e))
            bad += 1
        print("%s: %d entries" % (f, len(pins)))
    if a.against:
        for w in drift(allpins, parse(open(a.against, encoding="utf-8").read())):
            print("WARN:", w)
    print("PASS" if not bad else "FAIL (%d)" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
