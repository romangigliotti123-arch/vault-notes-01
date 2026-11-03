#!/usr/bin/env python3
"""reportcheck.py - triage a worker report before the manager relays it. Stdlib only.

  python reportcheck.py report.md [--brief brief.md] [--root DIR] [--max-words 350]
  python reportcheck.py --selftest

Reads the report's CRITERIA lines ([met|unmet|untested] <criterion> :: evidence: <...>), then:
  - every [met] needs evidence that is not narration ('looks good', 'should work', 'verified manually');
  - the count of CRITERIA lines should equal the brief's DONE WHEN items (when --brief is given);
  - paths named in the report must exist under --root (or be absolute); a 'sha256:<hex>' after a path must match the file;
  - report length over --max-words is flagged; the first line should be RESULT.
Prints a verdict (ACCEPT / SPOT-CHECK / REJECT) and one command to run per [met] line. A pass here proves the report is
well-formed, NOT that it is true: run the printed spot-checks. Exit 0 ACCEPT or SPOT-CHECK, 1 REJECT.
"""
import argparse
import hashlib
import os
import re
import sys

NARRATION = re.compile(r"looks (?:good|fine|correct)|should work|appears to|verified manually|reviewed the code|i checked|seems", re.I)
LINE = re.compile(r"^\s*(?:[-*]\s*)?\[(met|unmet|untested)\]\s*(.+)$", re.I)


def triage(report, brief="", root=".", max_words=350):
    rej, warn, checks = [], [], []
    first = next((ln for ln in report.splitlines() if ln.strip()), "")
    if not first.upper().startswith("RESULT"):
        warn.append("first line is not RESULT")
    if len(report.split()) > max_words:
        warn.append("long report: %d words > %d" % (len(report.split()), max_words))
    crit = [LINE.match(ln) for ln in report.splitlines()]
    crit = [m for m in crit if m]
    if not crit:
        rej.append("no CRITERIA lines")
    for m in crit:
        status, rest = m.group(1).lower(), m.group(2)
        ev = rest.split("::", 1)[1].strip() if "::" in rest else ""
        ev = re.sub(r"^evidence:\s*", "", ev, flags=re.I)
        if status == "met":
            if len(ev) < 12:
                rej.append("[met] without evidence: " + rest[:50])
            elif NARRATION.search(ev) and not re.search(r"`|\d|/|\\", ev):
                rej.append("[met] evidence is narration: " + ev[:50])
            else:
                cmd = re.search(r"`([^`]+)`", ev)
                checks.append("re-run: " + cmd.group(1) if cmd else "re-check: " + rest.split("::")[0].strip()[:60])
        elif status == "untested" and not re.search(r"not run|missing|cannot|no studio|no tool|needs", ev, re.I):
            warn.append("[untested] without a reason: " + rest[:40])
    if brief:
        n = 0
        mm = re.search(r"DONE WHEN[^\n]*\n((?:\s*\d+[.)].*\n?)+)", brief, re.I)
        if mm:
            n = len([x for x in mm.group(1).splitlines() if x.strip()])
        if n and n != len(crit):
            rej.append("brief has %d DONE WHEN items, report has %d CRITERIA lines" % (n, len(crit)))
    for p in sorted(set(re.findall(r"(?:[A-Za-z]:[\\/][^\s,;`]+|[\w./-]+\.(?:luau|lua|py|md|json|toml|csv|sh|ps1|txt))", report))):
        full = p if os.path.isabs(p) else os.path.join(root, p)
        if not os.path.exists(full):
            warn.append("path not found: " + p)
    for p, h in re.findall(r"(\S+)\s+sha256:([0-9a-fA-F]{16,64})", report):
        full = p if os.path.isabs(p) else os.path.join(root, p)
        if os.path.isfile(full):
            got = hashlib.sha256(open(full, "rb").read()).hexdigest()
            if not got.startswith(h.lower()):
                rej.append("hash mismatch for " + p)
    verdict = "REJECT" if rej else ("SPOT-CHECK" if warn or checks else "ACCEPT")
    return verdict, rej, warn, checks


def selftest():
    good = "RESULT: done\nCRITERIA:\n[met] lint clean :: evidence: `luau-check.sh x` -> exit 0\n[untested] studio run :: evidence: no Studio, not run\n"
    v, rej, warn, chk = triage(good, "DONE WHEN:\n1. lint\n2. run\n")
    assert v == "SPOT-CHECK" and not rej and chk == ["re-run: luau-check.sh x"], (v, rej, chk)
    v, rej, *_ = triage("RESULT: done\n[met] it works :: evidence: looks good, trust me\n")
    assert v == "REJECT" and rej, rej
    v, rej, *_ = triage("RESULT: done\n[met] x :: evidence: ok\n")
    assert v == "REJECT"
    v, rej, *_ = triage(good, "DONE WHEN:\n1. a\n2. b\n3. c\n")
    assert v == "REJECT" and "3 DONE WHEN" in rej[0], rej
    v, rej, *_ = triage("RESULT: done\nnothing else\n")
    assert v == "REJECT"
    import tempfile

    d = tempfile.mkdtemp()
    with open(os.path.join(d, "a.txt"), "wb") as f:
        f.write(b"hi")
    h = hashlib.sha256(b"hi").hexdigest()[:16]
    ok = "RESULT: done\n[met] file :: evidence: a.txt sha256:%s size 2\n" % h
    assert triage(ok, root=d)[0] != "REJECT"
    assert triage(ok.replace(h, "0" * 16), root=d)[0] == "REJECT"
    assert any("path not found" in w for w in triage("RESULT: done\n[met] f :: evidence: made nope.md ok 123\n", root=d)[2])
    print("selftest ok (8 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--brief")
    ap.add_argument("--root", default=".")
    ap.add_argument("--max-words", type=int, default=350)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    brief = open(a.brief, encoding="utf-8").read() if a.brief else ""
    v, rej, warn, chk = triage(open(a.file, encoding="utf-8").read(), brief, a.root, a.max_words)
    print("VERDICT:", v)
    for x in rej:
        print("REJECT:", x)
    for x in warn:
        print("WARN:", x)
    for x in chk:
        print("CHECK:", x)
    return 1 if v == "REJECT" else 0


if __name__ == "__main__":
    sys.exit(main())
