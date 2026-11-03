#!/usr/bin/env python3
"""backup_check.py make <out-manifest.json> <file-or-folder> [...] | verify <manifest.json> | --selftest

Backup manifest for place exports (.rbxl/.rbxlx), project folders and asset lists. `make` records path, size and sha256 for every file;
`verify` recomputes them and reports missing, changed and new-size files, so a restore copy is proven intact rather than assumed.
Warns when a .rbxl/.rbxlx is over --place-limit bytes (default 104857600 = the Creator Docs place size limit at 2026-10-28: live-check).
It does not talk to Roblox: the cloud version history is separate (version-history-keeper). Exit 1 on any verify difference, 2 on bad input.
"""
import hashlib
import json
import os
import sys
import tempfile

LIMIT = 104857600


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for d, _, names in os.walk(p):
                if any(x in d.replace("\\", "/") for x in ("/.git", "/node_modules")):
                    continue
                files += [os.path.join(d, n) for n in sorted(names)]
        elif os.path.isfile(p):
            files.append(p)
        else:
            raise FileNotFoundError(p)
    return files


def make(out, paths, limit=LIMIT):
    rows, warns = [], []
    for f in collect(paths):
        sz = os.path.getsize(f)
        rows.append({"path": os.path.abspath(f).replace("\\", "/"), "bytes": sz, "sha256": sha(f)})
        if f.lower().endswith((".rbxl", ".rbxlx")) and sz > limit:
            warns.append("%s is %d bytes, over the %d place limit" % (f, sz, limit))
    json.dump({"files": rows}, open(out, "w", encoding="utf-8"), indent=1)
    return rows, warns


def verify(manifest):
    bad = []
    for r in json.load(open(manifest, encoding="utf-8"))["files"]:
        p = r["path"]
        if not os.path.isfile(p):
            bad.append("MISSING " + p)
        elif os.path.getsize(p) != r["bytes"] or sha(p) != r["sha256"]:
            bad.append("CHANGED " + p)
    return bad


def selftest():
    with tempfile.TemporaryDirectory() as d:
        a = os.path.join(d, "a.rbxlx")
        open(a, "w").write("hello")
        m = os.path.join(d, "m.json")
        rows, warns = make(m, [a], limit=3)
        assert len(rows) == 1 and warns, (rows, warns)
        assert verify(m) == []
        open(a, "w").write("hellp")
        assert verify(m) == ["CHANGED " + os.path.abspath(a).replace("\\", "/")]
        os.remove(a)
        assert verify(m)[0].startswith("MISSING")
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    try:
        if len(argv) >= 3 and argv[0] == "make":
            rows, warns = make(argv[1], argv[2:])
            print("manifest %s: %d file(s), %d bytes" % (argv[1], len(rows), sum(r["bytes"] for r in rows)))
            for w in warns:
                print("WARN " + w)
            return 0
        if len(argv) == 2 and argv[0] == "verify":
            bad = verify(argv[1])
            for b in bad:
                print(b)
            print("verify ok" if not bad else "%d difference(s)" % len(bad))
            return 1 if bad else 0
    except (OSError, ValueError, KeyError) as e:
        print("bad input: %s" % e)
        return 2
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
