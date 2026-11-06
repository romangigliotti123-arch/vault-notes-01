#!/usr/bin/env python3
"""spark.py: real-entropy seeds for game ideas + a tiny de-dupe history (stdlib only; run with `py -I` / pyrun).

LLMs cannot be random, so the seeds are drawn here with random.SystemRandom (OS entropy), never by the model.

  spark.py draw [--n N] [--lane single|open|any]   N numbered seed sets (default 3, max 12), each:
        Odd domain: / Core verb: / Feeling: / Constraint: / Setting twist: (the twist is optional, drawn ~2 times in 3)
        --lane single  drops entries that need other players (tag mp)
        --lane open    drops entries that need a closed/linear space (tag linear) and multiplayer-only ones are kept
        --lane any     (default) no filtering
        --seed S       deterministic draw, for tests only
  spark.py hist add "<title>" "<one-line pitch>"   remember an idea (state/ideas-history.tsv, newest last, capped at 200 lines)
  spark.py hist check "<one-line pitch>"           prints NEW (exit 0) or SIMILAR: <title> (exit 1, best match) when token Jaccard >= 0.5
  spark.py hist list                               date, title, pitch of every remembered idea
Data: data/spark-lists.json next to this file. History lives in <claude config dir>/claude-kit/state/ (kit_state.py); vault-managed, tiny.
"""
import datetime
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit_state  # noqa: E402

CAP = 200
THRESH = 0.5
STOP = set("a an the of to and or in on for with is are be it its that this you your they their as at by from into who what when then than but not no can will just".split())
LABELS = (("domain", "Odd domain"), ("verb", "Core verb"), ("feeling", "Feeling"), ("constraint", "Constraint"), ("twist", "Setting twist"))
DROP = {"single": {"mp"}, "open": {"linear"}, "any": set()}


def load_lists():
    with open(os.path.join(HERE, "data", "spark-lists.json"), encoding="utf-8") as f:
        return json.load(f)


def pool(items, lane):
    out = []
    for e in items:
        text, tag = (e, "") if isinstance(e, str) else (e[0], e[1])
        if tag and tag in DROP[lane]:
            continue
        out.append(text)
    return out


def cmd_draw(args):
    n, lane, seed = 3, "any", None
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--n" and i + 1 < len(args):
            n = int(args[i + 1]); i += 2
        elif a == "--lane" and i + 1 < len(args):
            lane = args[i + 1]; i += 2
        elif a == "--seed" and i + 1 < len(args):
            seed = args[i + 1]; i += 2
        else:
            print(__doc__); return 2
    if lane not in DROP or not 1 <= n <= 12:
        print(__doc__); return 2
    rng = random.Random(seed) if seed is not None else random.SystemRandom()
    data = load_lists()
    pools = {k: pool(data[k], lane) for k, _ in LABELS}
    picks = {k: rng.sample(pools[k], n) for k, _ in LABELS}   # distinct across the N sets
    for j in range(n):
        print("SEED SET %d" % (j + 1))
        for k, label in LABELS:
            if k == "twist" and rng.random() >= 2 / 3:
                continue
            print("  %s: %s" % (label, picks[k][j]))
        print()
    return 0


def tokens(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 2 and w not in STOP}


def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def hist_path():
    return kit_state.path("ideas-history.tsv")


def read_hist():
    p = hist_path()
    if not os.path.isfile(p):
        return []
    rows = []
    for line in open(p, encoding="utf-8", errors="replace").read().splitlines():
        parts = line.split("\t")
        if len(parts) >= 3:
            rows.append(parts[:3])
    return rows


def clean(s):
    return " ".join(s.replace("\t", " ").replace("\r", " ").replace("\n", " ").split())


def cmd_hist(args):
    if args[:1] == ["add"] and len(args) == 3:
        rows = read_hist()
        rows.append([datetime.date.today().isoformat(), clean(args[1]), clean(args[2])])
        rows = rows[-CAP:]
        p = hist_path()
        os.makedirs(os.path.dirname(p), exist_ok=True)
        tmp = p + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write("".join("\t".join(r) + "\n" for r in rows))
        os.replace(tmp, p)
        print("added (%d kept)" % len(rows))
        return 0
    if args[:1] == ["check"] and len(args) == 2:
        t = tokens(args[1])
        best = None
        for d, title, pitch in read_hist():
            j = jaccard(t, tokens(pitch))
            if j >= THRESH and (best is None or j > best[0]):
                best = (j, title)
        if best:
            print("SIMILAR: %s" % best[1])
            return 1
        print("NEW")
        return 0
    if args[:1] == ["list"] and len(args) == 1:
        for d, title, pitch in read_hist():
            print("%s | %s | %s" % (d, title, pitch))
        return 0
    print(__doc__)
    return 2


def main(argv):
    if argv[:1] == ["draw"]:
        return cmd_draw(argv[1:])
    if argv[:1] == ["hist"]:
        return cmd_hist(argv[1:])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
