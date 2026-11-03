#!/usr/bin/env python3
"""release_log.py add|next|check <release/release-log.jsonl> ...   |   --selftest

Append-only release log with restore points. One JSON object per line:
  {"version": "1.4.2", "date": "2026-11-02", "place_version": 57, "notes": "what changed for players", "restore_point": "path or Studio version note",
   "gate": "release/gates.json verdict: GO"}
  add  LOG --version 1.4.2 --place-version 57 --notes "..." --restore "..." [--gate "..."] [--date YYYY-MM-DD]
       refuses a version that is not greater than the last, empty notes, or a missing restore point.
  next LOG --bump major|minor|patch      prints the next version (1.0.0 when the log is empty)
  check LOG   verifies: JSON valid, versions strictly increasing, place_version non-decreasing, notes and restore_point present.
The place_version number comes from Studio/Creator Hub Version History (never guessed). Exit 1 on failure, 2 on bad input.
"""
import argparse
import datetime
import json
import os
import re
import sys
import tempfile

SEM = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def parse(v):
    m = SEM.match(v or "")
    return tuple(int(x) for x in m.groups()) if m else None


def load(path):
    rows = []
    if os.path.isfile(path):
        for n, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    raise ValueError("line %d is not JSON" % n)
    return rows


def problems(rows):
    out, prev, pv = [], None, None
    for i, r in enumerate(rows, 1):
        v = parse(r.get("version"))
        if v is None:
            out.append("entry %d: version %r is not MAJOR.MINOR.PATCH" % (i, r.get("version")))
            continue
        if prev and v <= prev:
            out.append("entry %d: version %s not greater than the previous" % (i, r["version"]))
        prev = v
        if not str(r.get("notes", "")).strip():
            out.append("entry %d: notes empty" % i)
        if not str(r.get("restore_point", "")).strip():
            out.append("entry %d: no restore_point" % i)
        p = r.get("place_version")
        if not isinstance(p, int) or p < 1:
            out.append("entry %d: place_version must be a positive integer from Version History" % i)
        else:
            if pv is not None and p < pv:
                out.append("entry %d: place_version %d went backwards from %d (record a rollback as a new entry)" % (i, p, pv))
            pv = p
    return out


def bump(rows, kind):
    if not rows:
        return "1.0.0"
    a, b, c = parse(rows[-1]["version"])
    return {"major": "%d.0.0" % (a + 1), "minor": "%d.%d.0" % (a, b + 1), "patch": "%d.%d.%d" % (a, b, c + 1)}[kind]


def add(path, a):
    rows = load(path)
    e = {"version": a.version, "date": a.date or datetime.date.today().isoformat(), "place_version": a.place_version, "notes": a.notes,
         "restore_point": a.restore, "gate": a.gate or ""}
    p = problems(rows + [e])
    if p:
        print("refused: " + "; ".join(p[-3:]))
        return 1
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print("added %s" % a.version)
    return 0


def selftest():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "log.jsonl")
        ns = argparse.Namespace
        assert bump(load(p), "patch") == "1.0.0"
        assert add(p, ns(version="1.0.0", place_version=3, notes="first", restore="vh#3", gate="GO", date="2026-01-01")) == 0
        assert add(p, ns(version="1.0.0", place_version=4, notes="dup", restore="x", gate="", date=None)) == 1
        assert add(p, ns(version="1.1.0", place_version=2, notes="back", restore="x", gate="", date=None)) == 1
        assert add(p, ns(version="1.1.0", place_version=9, notes="", restore="x", gate="", date=None)) == 1
        assert add(p, ns(version="1.1.0", place_version=9, notes="n", restore="", gate="", date=None)) == 1
        assert add(p, ns(version="1.1.0", place_version=9, notes="second", restore="vh#9", gate="", date=None)) == 0
        rows = load(p)
        assert bump(rows, "patch") == "1.1.1" and bump(rows, "minor") == "1.2.0" and bump(rows, "major") == "2.0.0"
        assert problems(rows) == []
        open(p, "a").write('{"version":"1.0.5","notes":"x"}\n')
        assert len(problems(load(p))) >= 2
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if len(argv) < 2 or argv[0] not in ("add", "next", "check"):
        print(__doc__)
        return 2
    cmd, path = argv[0], argv[1]
    try:
        if cmd == "check":
            p = problems(load(path))
            for x in p:
                print("FAIL " + x)
            print("log ok (%d entries)" % len(load(path)) if not p else "%d problem(s)" % len(p))
            return 1 if p else 0
        if cmd == "next":
            ap = argparse.ArgumentParser()
            ap.add_argument("--bump", choices=("major", "minor", "patch"), required=True)
            print(bump(load(path), ap.parse_args(argv[2:]).bump))
            return 0
        ap = argparse.ArgumentParser()
        ap.add_argument("--version", required=True)
        ap.add_argument("--place-version", type=int, required=True)
        ap.add_argument("--notes", required=True)
        ap.add_argument("--restore", required=True)
        ap.add_argument("--gate")
        ap.add_argument("--date")
        return add(path, ap.parse_args(argv[2:]))
    except ValueError as e:
        print("bad input: %s" % e)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
