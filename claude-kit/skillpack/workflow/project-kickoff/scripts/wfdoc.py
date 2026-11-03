#!/usr/bin/env python3
"""wfdoc.py - structure check for the documents the workflow skills write. Stdlib only.

  python wfdoc.py docs/kickoff.md --kind kickoff
  python wfdoc.py x.md --require "Goal,Owner" --max-lines 80 [--need-evidence]
  python wfdoc.py --selftest

Checks: required headings present (case-insensitive substring of a '#' heading), no TODO/TBD/lorem/XXX placeholders,
length cap, minimum length, and with --need-evidence at least one evidence mark (a backtick span, '::' or 'evidence:').
It checks STRUCTURE only; whether the content is true is the worker-verifier's and the critic's job. Exit 0 pass, 1 fail.
"""
import argparse
import re
import sys

KINDS = {
    "kickoff": dict(req=["Goal", "Scope", "Toolchain", "Milestones", "First tasks"], max=90),
    "handoff": dict(req=["State", "Done", "Next", "Open", "Run"], max=80, ev=True),
    "decision": dict(req=["Decision", "Options", "Evidence", "Revisit"], max=70),
    "postmortem": dict(req=["Timeline", "Cause", "What worked", "Actions"], max=110, ev=True),
    "onboarding": dict(req=["Day one", "Setup", "First task", "Rules"], max=100),
    "release": dict(req=["Gate", "Rollback", "Sign-off"], max=90),
    "style": dict(req=["Naming", "Tools", "Enforce"], max=100),
    "roles": dict(req=["Roles", "Owns", "Collab", "Backup"], max=90),
    "mcpsession": dict(req=["Connection", "Checkpoint", "Serial", "Rollback"], max=90),
    "playtestlog": dict(req=["Build", "Mode", "Result", "Evidence"], max=80, ev=True),
    "kblookup": dict(req=["Question", "Sources", "Trust"], max=60),
    "devlog": dict(req=["Shipped", "Numbers", "Next"], max=70),
    "assets": dict(req=["Sources", "Naming", "Upload", "Registry"], max=100),
    "docs": dict(req=["Purpose", "API", "Example"], max=120),
    "sprint": dict(req=["Capacity", "Plan", "Overflow"], max=80),
    "debt": dict(req=["Item", "Fix", "Rank"], max=100),
    "gitflow": dict(req=["Branch", "Commit", "Ignore", "Rollback"], max=90),
    "ci": dict(req=["Hook", "Checks", "Skipped"], max=80),
    "pins": dict(req=["Tool", "Version", "Upgrade"], max=70),
    "folders": dict(req=["Repo", "Explorer", "Ownership"], max=90),
    "scopeguard": dict(req=["Frozen", "Swap", "Rule"], max=70),
    "milestone": dict(req=["Criteria", "Verdict", "Gaps"], max=80, ev=True),
    "budget": dict(req=["Routing", "Cap", "Total"], max=80),
}
PLACEHOLDER = re.compile(r"\b(TODO|TBD|lorem ipsum|XXX)\b", re.I)
EVIDENCE = re.compile(r"`[^`\n]+`|::|evidence:", re.I)


def check(text, require, max_lines, need_ev=False):
    errs = []
    heads = [h.lower() for h in re.findall(r"^#+\s*(.+)$", text, re.M)]
    for r in require:
        if not any(r.lower() in h for h in heads):
            errs.append("missing heading: " + r)
    if PLACEHOLDER.search(text):
        errs.append("placeholder text (TODO/TBD/XXX)")
    n = len([ln for ln in text.splitlines() if ln.strip()])
    if max_lines and n > max_lines:
        errs.append("too long: %d non-blank lines > %d" % (n, max_lines))
    if len(text.split()) < 25:
        errs.append("too short (<25 words)")
    if need_ev and not EVIDENCE.search(text):
        errs.append("no evidence mark (backtick command, '::' or 'evidence:')")
    return errs


def selftest():
    good = "# Handoff\n## State\nplace builds `rojo build` ok\n## Done\nitem one two three four five six\n## Next\nfix the shop remote check\n## Open questions\nnone known yet\n## Run\n`rojo serve`\n"
    assert check(good, KINDS["handoff"]["req"], 80, True) == [], check(good, KINDS["handoff"]["req"], 80, True)
    bad = good.replace("## Next", "## Later").replace("fix", "TODO fix")
    errs = check(bad, KINDS["handoff"]["req"], 80, True)
    assert any("Next" in e for e in errs) and any("placeholder" in e for e in errs), errs
    noev = "# A\n## Goal\n" + "word " * 30
    assert any("evidence" in e for e in check(noev, ["Goal"], 50, True))
    assert any("too long" in e for e in check("# A\n## Goal\n" + "word word\n" * 60, ["Goal"], 20))
    assert any("too short" in e for e in check("# A\n## Goal\nx", ["Goal"], 20))
    print("selftest ok (5 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--kind")
    ap.add_argument("--require", default="")
    ap.add_argument("--max-lines", type=int, default=0)
    ap.add_argument("--need-evidence", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    req = [r.strip() for r in a.require.split(",") if r.strip()]
    mx, ev = a.max_lines, a.need_evidence
    if a.kind:
        if a.kind not in KINDS:
            print("unknown kind; known: " + ", ".join(sorted(KINDS)))
            return 1
        k = KINDS[a.kind]
        req = req or k["req"]
        mx = mx or k["max"]
        ev = ev or k.get("ev", False)
    errs = check(open(a.file, encoding="utf-8").read(), req, mx, ev)
    print("PASS" if not errs else "FAIL: " + "; ".join(errs))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
