#!/usr/bin/env python3
"""changelog.py - turn commit subjects into a changelog section. Stdlib only.

  git log v1.2..HEAD --pretty=%s | python changelog.py --version 1.3 --date 2026-11-02
  python changelog.py commits.txt --version 1.3
  python changelog.py --selftest

Groups conventional subjects (feat, fix, perf, refactor, docs, chore, test, exp) into Added / Fixed / Changed / Internal.
Subjects that are not conventional go to "Unsorted" so nothing is silently dropped. The output is the DEVELOPER changelog;
the player-facing text is written by hand from the Added/Fixed lists (update-announcement-writer owns that). Exit 0.
"""
import argparse
import re
import sys

SUBJ = re.compile(r"^(feat|fix|perf|refactor|docs|chore|test|exp)(?:\(([^)]+)\))?(!)?:\s*(.+)$")
SECTION = {"feat": "Added", "fix": "Fixed", "perf": "Changed", "refactor": "Internal", "docs": "Internal", "chore": "Internal", "test": "Internal", "exp": "Internal"}
ORDER = ["Added", "Fixed", "Changed", "Internal", "Unsorted"]


def build(lines, version, date):
    groups = {k: [] for k in ORDER}
    breaking = []
    for ln in lines:
        ln = ln.strip()
        if not ln or ln.startswith("Merge "):
            continue
        m = SUBJ.match(ln)
        if not m:
            groups["Unsorted"].append(ln)
            continue
        typ, scope, bang, text = m.groups()
        item = ("%s: %s" % (scope, text)) if scope else text
        groups[SECTION[typ]].append(item)
        if bang:
            breaking.append(item)
    out = ["## %s - %s" % (version, date)]
    if breaking:
        out += ["", "### Breaking"] + ["- " + b for b in breaking]
    for k in ORDER:
        if groups[k]:
            out += ["", "### " + k] + ["- " + i for i in groups[k]]
    return "\n".join(out) + "\n", groups


def selftest():
    text, g = build(["feat(shop): add limit", "fix: stop dupe", "wip stuff", "chore: bump rojo", "feat(data)!: new schema", "Merge branch x", ""], "1.3", "2026-11-02")
    assert g["Added"] == ["shop: add limit", "data: new schema"] and g["Fixed"] == ["stop dupe"], g
    assert g["Unsorted"] == ["wip stuff"] and g["Internal"] == ["bump rojo"]
    assert text.startswith("## 1.3 - 2026-11-02") and "### Breaking\n- data: new schema" in text
    assert "Merge" not in text
    print("selftest ok (4 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--version", default="Unreleased")
    ap.add_argument("--date", default="")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    src = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    sys.stdout.write(build(src.splitlines(), a.version, a.date or "undated")[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
