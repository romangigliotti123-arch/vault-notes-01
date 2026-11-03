#!/usr/bin/env python3
"""tasks.py - validate a task table and print the work in waves. Stdlib only.

  python tasks.py tasks.csv [--max-hours 4]
  python tasks.py --selftest

CSV columns: id,title,deps,owns,verify,est_h   (deps and owns: ';' separated; owns = paths the task may write)
Checks: unique ids; deps exist; no dependency cycle; every task has a verify check that is not vague; est_h <= --max-hours
(bigger tasks must be split); owns not empty; two tasks in the SAME wave must not own overlapping paths (one writer per path).
Output: waves (tasks that can run in parallel), the critical path in hours. Exit 0 ok, 1 on any error.
"""
import argparse
import csv
import io
import sys

VAGUE = ("works", "looks good", "is good", "done", "fine", "ok", "correct")


def overlap(a, b):
    a, b = a.rstrip("/"), b.rstrip("/")
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def plan(rows, max_hours=4.0):
    errs, tasks = [], {}
    for r in rows:
        i = (r.get("id") or "").strip()
        if not i or i in tasks:
            errs.append("bad or duplicate id: %r" % i)
            continue
        try:
            est = float(r.get("est_h") or 0)
        except ValueError:
            est = 0
        t = dict(id=i, title=r.get("title", ""), deps=[d.strip() for d in (r.get("deps") or "").split(";") if d.strip()],
                 owns=[o.strip() for o in (r.get("owns") or "").split(";") if o.strip()], verify=(r.get("verify") or "").strip(), est=est)
        tasks[i] = t
        v = t["verify"].lower()
        if not v or v in VAGUE or (len(v) < 12 and "`" not in v):
            errs.append("%s: verify is empty or vague (%r); name a command, file or observable" % (i, t["verify"]))
        if est <= 0:
            errs.append("%s: est_h missing" % i)
        elif est > max_hours:
            errs.append("%s: est_h %.1f > %.1f, split it" % (i, est, max_hours))
        if not t["owns"]:
            errs.append("%s: owns is empty (what may it write?)" % i)
    for t in tasks.values():
        for d in t["deps"]:
            if d not in tasks:
                errs.append("%s: unknown dependency %s" % (t["id"], d))
    wave, left, waves = {}, set(tasks), []
    while left:
        ready = sorted(i for i in left if all(d in wave for d in tasks[i]["deps"] if d in tasks))
        if not ready:
            errs.append("dependency cycle among: " + ", ".join(sorted(left)))
            break
        n = len(waves)
        for i in ready:
            wave[i] = n
        waves.append(ready)
        left -= set(ready)
    for n, w in enumerate(waves):
        for x in range(len(w)):
            for y in range(x + 1, len(w)):
                for a in tasks[w[x]]["owns"]:
                    for b in tasks[w[y]]["owns"]:
                        if overlap(a, b):
                            errs.append("wave %d: %s and %s both own %s (serialise or split the path)" % (n + 1, w[x], w[y], a))
    finish = {}
    for w in waves:
        for i in w:
            finish[i] = tasks[i]["est"] + max([finish[d] for d in tasks[i]["deps"] if d in finish] or [0])
    return errs, waves, (max(finish.values()) if finish else 0.0)


def selftest():
    ok = "id,title,deps,owns,verify,est_h\nA,data,,src/server/Data.luau,`luau-check.sh src/server/Data.luau` exits 0,2\nB,shop,A,src/server/Shop.luau,`lune run Shop.spec.luau` prints PASS,3\nC,ui,A,src/client/,screenshot shows the shop,2\n"
    e, w, cp = plan(list(csv.DictReader(io.StringIO(ok))))
    assert not e and w == [["A"], ["B", "C"]] and cp == 5.0, (e, w, cp)
    cyc = ok.replace("A,data,,", "A,data,B,")
    assert any("cycle" in x for x in plan(list(csv.DictReader(io.StringIO(cyc))))[0])
    vague = ok.replace("screenshot shows the shop", "works")
    assert any("vague" in x for x in plan(list(csv.DictReader(io.StringIO(vague))))[0])
    big = ok.replace(",2\n", ",9\n", 1)
    assert any("split it" in x for x in plan(list(csv.DictReader(io.StringIO(big))))[0])
    clash = ok.replace("src/client/", "src/server/")
    assert any("both own" in x for x in plan(list(csv.DictReader(io.StringIO(clash))))[0])
    assert any("unknown dependency" in x for x in plan(list(csv.DictReader(io.StringIO(ok.replace("B,shop,A", "B,shop,Z")))))[0])
    print("selftest ok (6 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--max-hours", type=float, default=4.0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    with open(a.file, encoding="utf-8", newline="") as f:
        errs, waves, cp = plan(list(csv.DictReader(f)), a.max_hours)
    for n, w in enumerate(waves, 1):
        print("wave %d (parallel ok): %s" % (n, ", ".join(w)))
    print("critical path: %.1f h" % cp)
    for e in errs:
        print("ERROR:", e)
    print("PASS" if not errs else "FAIL (%d)" % len(errs))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
