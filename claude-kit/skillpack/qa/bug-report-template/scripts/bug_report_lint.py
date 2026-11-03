#!/usr/bin/env python3
"""bug_report_lint.py: check that a bug report (Markdown) has what a fixer needs.

usage: python bug_report_lint.py <report.md> [--json]
       python bug_report_lint.py --selftest

Checks (each is a pass/fail line; exit 1 if any REQUIRED check fails):
  title        one-line title under 100 chars, not 'bug' or 'broken'
  expected     an 'Expected' section with text
  actual       an 'Actual' section with text
  steps        a 'Steps' section with at least 2 numbered steps, each under 200 chars
  where        says Server, Client or Both (where it happens)
  build        a build/version/place version or date
  frequency    how often (always, sometimes N of M, once)
  environment  device/platform (RECOMMENDED, not required)
  evidence     Output excerpt, screenshot or video reference (RECOMMENDED)
Heuristic text checks only: it cannot tell whether the steps are true. Reproduce them (repro-step-writer) before filing.
"""
import json
import re
import sys

REQUIRED = ["title", "expected", "actual", "steps", "where", "build", "frequency"]


def section(text, name):
    m = re.search(r"^#{1,4}\s*" + name + r"[^\n]*\n(.*?)(?=^#{1,4}\s|\Z)", text, re.M | re.S | re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"^\**" + name + r"\**\s*:\s*(.+)$", text, re.M | re.I)
    return m.group(1).strip() if m else ""


def lint(text):
    res = {}
    first = next((ln for ln in text.splitlines() if ln.strip()), "")
    title = re.sub(r"^#+\s*|^title\s*:\s*", "", first.strip(), flags=re.I).strip()
    res["title"] = (0 < len(title) < 100 and title.lower() not in ("bug", "broken", "bug report", "it is broken"), title or "(none)")
    exp, act = section(text, "expected"), section(text, "actual")
    res["expected"] = (len(exp) >= 5, exp[:60] or "(missing)")
    res["actual"] = (len(act) >= 5, act[:60] or "(missing)")
    steps_text = section(text, "steps")
    steps = re.findall(r"^\s*\d+[.)]\s*(.+)$", steps_text, re.M)
    long_ = [s for s in steps if len(s) > 200]
    res["steps"] = (len(steps) >= 2 and not long_, f"{len(steps)} numbered steps" + (f", {len(long_)} too long" if long_ else ""))
    where = re.search(r"\b(server|client|both|studio|edit mode)\b", text, re.I)
    res["where"] = (bool(where), where.group(1) if where else "(no Server/Client/Both)")
    build = re.search(r"\b(build|version|v\d+(\.\d+)*|place version|commit|date)\b\s*[:#=]?\s*\S+", text, re.I)
    res["build"] = (bool(build), build.group(0)[:40] if build else "(no build/version)")
    freq = re.search(r"\b(always|every time|sometimes|intermittent|once|rarely|\d+\s*(/|of|out of)\s*\d+)\b", text, re.I)
    res["frequency"] = (bool(freq), freq.group(0) if freq else "(no frequency)")
    env = re.search(r"\b(phone|tablet|desktop|console|ios|android|windows|mac|xbox|pc|device)\b", text, re.I)
    res["environment"] = (bool(env), env.group(1) if env else "(no device/platform)")
    ev = re.search(r"(```|\.png|\.jpg|\.gif|\.mp4|screenshot|video|output)", text, re.I)
    res["evidence"] = (bool(ev), "present" if ev else "(no output/screenshot/video)")
    return res


def render(res):
    lines = []
    failed = 0
    for k, (ok, detail) in res.items():
        req = k in REQUIRED
        if not ok and req:
            failed += 1
        lines.append("%s %-11s %s%s" % ("PASS" if ok else ("FAIL" if req else "WARN"), k, detail, "" if req else "  (recommended)"))
    lines.append("BUG REPORT: %s" % ("ready to file" if failed == 0 else "%d required checks failed" % failed))
    return "\n".join(lines), failed


GOOD = """# Shop buy button does nothing after respawn

## Expected
Pressing Buy after respawning opens the confirm dialog.

## Actual
Nothing happens; Output shows `Shop:31: attempt to index nil with 'coins'` (Server).

## Steps
1. Join the test place on a phone.
2. Reset the character from the menu.
3. Walk to the shop and press Buy.

Build: place version 112. Happens 3 of 3 times. Device: Android phone.
Screenshot: shop-buy.png
"""
BAD = """bug

it is broken, please fix
"""


def selftest():
    g, gf = render(lint(GOOD))
    b, bf = render(lint(BAD))
    assert gf == 0, g
    assert bf >= 5, b
    assert "FAIL title" in b and "FAIL steps" in b
    only_one_step = GOOD.replace("2. Reset the character from the menu.\n3. Walk to the shop and press Buy.\n", "")
    assert not lint(only_one_step)["steps"][0]
    assert lint(GOOD.replace("Build: place version 112.", ""))["build"][0] is False
    print("bug_report_lint selftest: ok (good report 0 failures, bad report %d failures)" % bf)
    return 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--selftest":
        return selftest()
    text = open(argv[0], encoding="utf-8").read()
    res = lint(text)
    if "--json" in argv:
        print(json.dumps({k: {"ok": v[0], "detail": v[1]} for k, v in res.items()}, indent=2))
        return 0 if all(res[k][0] for k in REQUIRED) else 1
    out, failed = render(res)
    print(out)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
