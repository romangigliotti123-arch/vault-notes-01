#!/usr/bin/env python3
"""faq_cluster.py - group real player questions and rank them for the FAQ. Stdlib only.

  python faq_cluster.py questions.txt [--sim 0.5] [--top 15]
  python faq_cluster.py --selftest

One question per line (from Discord, comments, tickets, in-game feedback). Questions whose content words overlap by --sim (Jaccard)
become one cluster; clusters are ranked by size. The FAQ answers the biggest clusters first, in the players' own words (the shortest
question in the cluster is shown as the heading candidate). Handles and names are not read or kept: strip them before you paste.
Exit 2 on unreadable input.
"""
import argparse
import re
import sys

STOP = set("a an the is are was be do does did how what when where why who can could i you my me we it this that to of in on for and or with at as if not there any".split())


def toks(q):
    ws = (w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w for w in re.findall(r"[a-z0-9]+", q.lower()))
    return {w for w in ws if w not in STOP and len(w) > 1}


def cluster(lines, sim=0.5):
    groups = []
    for q in (l.strip() for l in lines):
        if not q:
            continue
        t = toks(q)
        for g in groups:
            u = t | g["toks"]
            if u and len(t & g["toks"]) / len(u) >= sim:
                g["qs"].append(q)
                g["toks"] |= t
                break
        else:
            groups.append({"toks": set(t), "qs": [q]})
    return sorted(({"count": len(g["qs"]), "heading": min(g["qs"], key=len), "all": g["qs"]} for g in groups), key=lambda x: (-x["count"], x["heading"]))


def selftest():
    qs = ["How do I get pets?", "how to get pets", "where do I get a pet?", "Is there a Discord", "how do i get pets fast", "Why did my coins reset?"]
    c = cluster(qs, 0.4)
    assert c[0]["count"] == 4 and "pet" in c[0]["heading"].lower(), c
    assert sum(x["count"] for x in c) == 6
    assert any("Discord" in x["heading"] for x in c)
    assert cluster(["", "  "]) == []
    print("selftest ok (4 asserts)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--sim", type=float, default=0.5)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("give the questions file")
    try:
        lines = open(a.file, encoding="utf-8-sig").read().splitlines()
    except OSError as e:
        print("error:", e)
        return 2
    for x in cluster(lines, a.sim)[: a.top]:
        print("x%-3d %s" % (x["count"], x["heading"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
