#!/usr/bin/env python3
"""audio_check.py manifest.csv [--scan <project>] [--max-seconds N] [--max-mb N] | --selftest

Audio provenance check. manifest.csv columns: asset_id, title, owner, permission, length_s, size_mb, evidence.
permission is one of: owned, roblox, licensed, granted, unknown (granted = the owner granted this experience use; Creator Docs: imported
audio is private until permission is granted to specific friends/experiences, live-check).
Checks: permission unknown/blank is FAIL; licensed or granted without evidence (link, file, receipt id) is FAIL; duplicate ids; non-numeric ids;
length/size over the limits YOU pass (the live Creator Docs audio limits are not built in; the 2026-10-28 note said 20 MB, 7 minutes for imports).
With --scan: every rbxassetid in Sound/AudioPlayer/SoundId/Asset lines of the project must appear in the manifest (missing = FAIL).
Exit 1 on FAIL, 2 on bad input.
"""
import csv
import os
import re
import sys
import tempfile

PERMS = {"owned", "roblox", "licensed", "granted", "unknown"}
AUD = re.compile(r"(Sound|AudioPlayer|SoundId|\.Asset\b|AudioAsset)", re.I)
ID = re.compile(r"rbxassetid://(\d+)")


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def check(rows, scanned=None, max_s=None, max_mb=None):
    out, seen = [], set()
    for i, r in enumerate(rows, 2):
        aid = (r.get("asset_id") or "").strip()
        perm = (r.get("permission") or "").strip().lower()
        who = "row %d (%s)" % (i, aid or "no id")
        if not aid.isdigit():
            out.append(("FAIL", who + ": asset_id must be digits"))
        if aid in seen:
            out.append(("FAIL", who + ": duplicate asset id"))
        seen.add(aid)
        if perm not in PERMS or perm == "unknown":
            out.append(("FAIL", who + ": permission %r is not established" % perm))
        if perm in ("licensed", "granted") and not (r.get("evidence") or "").strip():
            out.append(("FAIL", who + ": %s without evidence" % perm))
        if not (r.get("owner") or "").strip():
            out.append(("WARN", who + ": owner blank"))
        L, S = num(r.get("length_s")), num(r.get("size_mb"))
        if max_s is not None and L is not None and L > max_s:
            out.append(("FAIL", who + ": %.0fs over your %.0fs limit" % (L, max_s)))
        if max_mb is not None and S is not None and S > max_mb:
            out.append(("FAIL", who + ": %.1f MB over your %.1f MB limit" % (S, max_mb)))
    for a in sorted(scanned or []):
        if a not in seen:
            out.append(("FAIL", "asset %s is used in code but not in the manifest" % a))
    if not any(lv == "FAIL" for lv, _ in out):
        out.append(("OK", "every audio asset has an established permission"))
    return out


def scan_ids(root):
    ids = set()
    for d, _, names in os.walk(root):
        if any(x in d.replace("\\", "/") for x in ("/.git", "/Packages")):
            continue
        for n in names:
            if n.endswith((".luau", ".lua")):
                for line in open(os.path.join(d, n), encoding="utf-8", errors="replace").read().splitlines():
                    if not line.strip().startswith("--") and AUD.search(line):
                        ids.update(ID.findall(line))
    return ids


def selftest():
    rows = [{"asset_id": "1", "owner": "me", "permission": "owned", "length_s": "30"},
            {"asset_id": "2", "owner": "x", "permission": "licensed", "evidence": "receipt 77", "length_s": "500"},
            {"asset_id": "3", "owner": "", "permission": "unknown"},
            {"asset_id": "2", "owner": "x", "permission": "granted"}]
    r = check(rows, scanned={"1", "9"}, max_s=420)
    f = [m for lv, m in r if lv == "FAIL"]
    assert len(f) == 5, f
    assert check(rows[:1], scanned={"1"})[0][0] == "OK"
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "a.luau"), "w").write('s.SoundId = "rbxassetid://123"\nlocal img = "rbxassetid://999"\n-- Sound rbxassetid://5\n')
        assert scan_ids(d) == {"123"}
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    rest = list(argv)
    opts = {}
    for flag in ("--scan", "--max-seconds", "--max-mb"):
        if flag in rest:
            i = rest.index(flag)
            opts[flag] = rest[i + 1] if i + 1 < len(rest) else None
            del rest[i:i + 2]
    if len(rest) != 1:
        print(__doc__)
        return 2
    try:
        rows = list(csv.DictReader(open(rest[0], encoding="utf-8-sig")))
        scanned = scan_ids(opts["--scan"]) if opts.get("--scan") else None
        ms = float(opts["--max-seconds"]) if opts.get("--max-seconds") else None
        mm = float(opts["--max-mb"]) if opts.get("--max-mb") else None
    except (OSError, ValueError, TypeError) as e:
        print("bad input: %s" % e)
        return 2
    out = check(rows, scanned, ms, mm)
    for lv, m in out:
        print("[%s] %s" % (lv, m))
    return 1 if any(x[0] == "FAIL" for x in out) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
