#!/usr/bin/env python3
"""loc_check.py - check translated store/UI strings before they go into Creator Hub. Stdlib only.

  python loc_check.py strings.csv --lang es [--name "Steal an Egg"] [--max-ratio 1.5] [--limit title=50 --limit description=1000]
  python loc_check.py --selftest

CSV columns: key, source, <lang> (header names; extra columns ignored). Checks per row:
  missing      translation empty (an empty entry tells Roblox you do not want it translated; better to know)
  same         translation identical to the source for text longer than 3 words (probably never translated)
  placeholder  {Name}-style placeholders must match the source exactly (vault: keep parameter names identical across locales)
  name         the game name must appear unchanged where the source has it (vault: keep the game name the same across languages)
  ratio        translation longer than --max-ratio x source (vault: Spanish about 30% longer, German more; design UI for longer text)
  limit        length over a per-key limit you pass (the real limits are NOT built in: live-check Creator Docs)
Exit 1 when any FAIL. WARN rows are judgement calls for a human translator.
"""
import argparse
import csv
import re
import sys

PH = re.compile(r"\{[^{}]+\}")


def check_rows(rows, lang, name=None, max_ratio=1.5, limits=None):
    limits = limits or {}
    out = []
    for r in rows:
        key, src, tr = r.get("key", ""), (r.get("source") or "").strip(), (r.get(lang) or "").strip()
        if not tr:
            out.append((key, "FAIL", "missing", "no %s translation" % lang))
            continue
        if len(src.split()) > 3 and tr == src:
            out.append((key, "WARN", "same", "identical to source"))
        if sorted(PH.findall(src)) != sorted(PH.findall(tr)):
            out.append((key, "FAIL", "placeholder", "source %s vs translation %s" % (PH.findall(src), PH.findall(tr))))
        if name and name in src and name not in tr:
            out.append((key, "FAIL", "name", "game name %r must stay unchanged" % name))
        if src and len(tr) > max_ratio * len(src) and len(tr) > 12:
            out.append((key, "WARN", "ratio", "%d chars vs %d source (x%.2f)" % (len(tr), len(src), len(tr) / len(src))))
        lim = limits.get(key)
        if lim and len(tr) > lim:
            out.append((key, "FAIL", "limit", "%d chars over limit %d" % (len(tr), lim)))
    return out


def selftest():
    rows = [
        {"key": "title", "source": "Steal an Egg", "es": "Roba un Huevo"},
        {"key": "a", "source": "Hello {Player_Name}, welcome back", "es": "Hola {Player_Name}, bienvenido"},
        {"key": "b", "source": "Hello {Player_Name}, welcome back", "es": "Hola {Jugador}, bienvenido"},
        {"key": "c", "source": "Play Steal an Egg today", "es": "Juega Roba un Huevo hoy"},
        {"key": "d", "source": "Collect eggs and trade", "es": ""},
        {"key": "e", "source": "Collect eggs and trade", "es": "Collect eggs and trade"},
        {"key": "f", "source": "Buy", "es": "Comprar ahora mismo en la tienda"},
        {"key": "description", "source": "x", "es": "y" * 20},
    ]
    res = check_rows(rows, "es", name="Steal an Egg", limits={"description": 10})
    got = {(k, c) for k, s, c, m in res}
    assert ("b", "placeholder") in got and ("a", "placeholder") not in got
    assert ("c", "name") in got and ("title", "name") in got
    assert ("d", "missing") in got and ("e", "same") in got and ("f", "ratio") in got and ("description", "limit") in got
    print("selftest ok (6 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--lang")
    ap.add_argument("--name")
    ap.add_argument("--max-ratio", type=float, default=1.5, dest="max_ratio")
    ap.add_argument("--limit", action="append", default=[], help="key=chars")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv or not a.lang:
        ap.error("csv path and --lang are required")
    limits = {}
    for kv in a.limit:
        k, _, v = kv.partition("=")
        limits[k] = int(v)
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if rows and a.lang not in rows[0]:
        ap.error("column %r not in CSV (have %s)" % (a.lang, ", ".join(rows[0].keys())))
    res = check_rows(rows, a.lang, a.name, a.max_ratio, limits)
    for k, s, c, m in res:
        print("%-5s %-14s %-11s %s" % (s, k, c, m))
    fails = sum(1 for r in res if r[1] == "FAIL")
    print("%d rows, %d FAIL, %d WARN" % (len(rows), fails, len(res) - fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
