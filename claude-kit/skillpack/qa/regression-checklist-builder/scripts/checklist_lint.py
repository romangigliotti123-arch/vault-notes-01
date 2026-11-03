#!/usr/bin/env python3
"""checklist_lint.py: check a regression checklist (Markdown table or list) is runnable by someone who did not write it.

usage: python checklist_lint.py <checklist.md>
       python checklist_lint.py --selftest

A checklist ROW is a Markdown table row or a '- [ ]' list line. Each row needs:
  id        a short id like R-001 (unique)
  action    what to do or run (a command, a menu path, a bot name)
  expected  an observable result (a number, a log line, a visible state), not 'works' or 'looks fine'
  area      the system it protects (save, shop, combat, ui, ...)
Table columns are matched by header name (id, area, check|action, expected|result). Exit 1 if any row fails or there are fewer
than 5 rows. Heuristic text checks only: it cannot tell whether a check is a GOOD check.
"""
import re
import sys

VAGUE = re.compile(r"^(works?|ok|fine|looks? (fine|good|ok)|no (issues|problems)|good|correct|as expected)\.?$", re.I)


def parse_table(lines):
    rows, header = [], None
    for ln in lines:
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        low = [c.lower() for c in cells]
        if header is None and "id" in low:
            header = low
            continue
        if header:
            rows.append(dict(zip(header, cells)))
    return rows


def lint(text):
    problems, ids = [], set()
    rows = parse_table(text.splitlines())
    if not rows:
        problems.append("no table rows found (need a header with id | area | check | expected)")
    for n, r in enumerate(rows, 1):
        rid = r.get("id", "")
        label = rid or "row %d" % n
        if not re.fullmatch(r"[A-Za-z]{1,6}-?\d{1,4}", rid):
            problems.append("%s: id missing or not like R-001" % label)
        elif rid in ids:
            problems.append("%s: duplicate id" % label)
        ids.add(rid)
        action = r.get("check") or r.get("action") or ""
        if len(action) < 8:
            problems.append("%s: action too short" % label)
        exp = r.get("expected") or r.get("result") or ""
        if len(exp) < 5 or VAGUE.match(exp):
            problems.append("%s: expected result is vague or missing: %r" % (label, exp))
        if not r.get("area"):
            problems.append("%s: no area" % label)
    if 0 < len(rows) < 5:
        problems.append("only %d rows: a regression list for a release needs at least 5" % len(rows))
    return rows, problems


GOOD = """| id | area | check | expected |
|---|---|---|---|
| R-001 | save | Join, buy test item, leave, rejoin | Inventory shows the item; Output has no DataStore errors |
| R-002 | shop | Run purchase-flow-tester scenarios | PURCHASE FLOW: 7/7 scenarios passed |
| R-003 | ui | Open shop on the smallest phone profile | Buy button fully on screen, no overlap |
| R-004 | combat | Hit a dummy 10 times | Dummy health drops by 10 x damage; no server errors |
| R-005 | loading | Join with Network Simulator slow | Spawns within 30 s, no infinite yield warning |
"""
BAD = """| id | area | check | expected |
|---|---|---|---|
| R-001 | save | test | works |
| R-001 | shop | open shop | looks fine |
"""


def selftest():
    rows, p = lint(GOOD)
    assert len(rows) == 5 and not p, p
    rows, p = lint(BAD)
    assert any("duplicate" in x for x in p) and any("vague" in x for x in p) and any("only 2 rows" in x for x in p), p
    assert lint("just prose")[1]
    print("checklist_lint selftest: ok (good list 0 problems, bad list %d problems)" % len(p))
    return 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--selftest":
        return selftest()
    rows, problems = lint(open(argv[0], encoding="utf-8").read())
    for p in problems:
        print("FAIL", p)
    print("CHECKLIST: %d rows, %s" % (len(rows), "ready" if not problems else "%d problems" % len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
