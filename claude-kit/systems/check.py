#!/usr/bin/env python3
"""Run every static check and headless test of the kit's drop-in systems.

  python check.py                 all systems
  python check.py PlayerData Shop only these
  python check.py --no-tests      static checks only

Per system: stylua --check, selene (src with the Roblox std, tests with selene-tests.toml),
luau-lsp analyze on src (the Luau type checker with Roblox definitions; strict where the file says --!strict),
and every tests/*.test.luau under Lune. Tools come from Rokit (rokit.toml next to this file; run `rokit install`).
A missing tool is reported as SKIPPED and makes the run exit 2, never a silent pass.
Exit: 0 all passed, 1 a check failed, 2 a tool was missing (nothing failed).
"""
import glob
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFS = os.path.join(HERE, "..", "tools", "roblox-project-template", "globalTypes.d.luau")


def tool(name):
    p = shutil.which(name)
    if not p:
        rk = os.path.join(os.path.expanduser("~"), ".rokit", "bin", name + (".exe" if os.name == "nt" else ""))
        p = rk if os.path.exists(rk) else None
    return p


def run(cmd, **kw):
    r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    no_tests = "--no-tests" in sys.argv
    systems = args or sorted(d for d in os.listdir(HERE) if os.path.isdir(os.path.join(HERE, d, "src")))
    missing, failed = [], []
    t = {n: tool(n) for n in ("stylua", "selene", "luau-lsp", "lune", "rojo")}
    for n, p in t.items():
        if not p:
            missing.append(n)
            print("SKIPPED %s: not installed (run `rokit install` in %s)" % (n, HERE))
    sm = None
    if t["rojo"]:
        sm = os.path.join(HERE, "_check", "sourcemap.json")
        rc, out = run([t["rojo"], "sourcemap", os.path.join("_check", "check.project.json"), "-o", sm, "--absolute"])
        if rc != 0:
            print("rojo sourcemap failed:\n" + out)
            sm = None
            failed.append("rojo sourcemap")
    for s in systems:
        print("== %s" % s)
        if t["stylua"]:
            rc, out = run([t["stylua"], "--check", s])
            print("  stylua   %s" % ("ok" if rc == 0 else "FAIL\n" + out))
            if rc:
                failed.append(s + " stylua")
        if t["selene"]:
            rc, out = run([t["selene"], os.path.join(s, "src")])
            print("  selene   %s" % ("ok (src)" if rc == 0 else "FAIL\n" + out))
            if rc:
                failed.append(s + " selene")
            if os.path.isdir(os.path.join(HERE, s, "tests")):
                rc, out = run([t["selene"], "--config", "selene-tests.toml", os.path.join(s, "tests")])
                print("  selene   %s" % ("ok (tests)" if rc == 0 else "FAIL\n" + out))
                if rc:
                    failed.append(s + " selene tests")
        if t["luau-lsp"]:
            cmd = [t["luau-lsp"], "analyze", "--definitions=" + DEFS]
            if sm:
                cmd.append("--sourcemap=" + sm)
            cmd.append(os.path.join(s, "src"))
            rc, out = run(cmd)
            lines = [l for l in out.splitlines() if not l.startswith("[INFO]")]
            summary = [l for l in lines if l.endswith("errors") or l.endswith("warnings")]
            ok = rc == 0 and not any(not l.startswith("0 ") for l in summary)
            print("  analyze  %s (%s)" % ("ok" if ok else "FAIL", ", ".join(summary)))
            if not ok:
                print("\n".join(lines))
                failed.append(s + " analyze")
        if t["lune"] and not no_tests:
            for f in sorted(glob.glob(os.path.join(HERE, s, "tests", "*.test.luau"))):
                rc, out = run([t["lune"], "run", os.path.relpath(f, HERE)])
                last = out.splitlines()[-1] if out else ""
                print("  lune     %s: %s" % (os.path.basename(f), last if rc == 0 else "FAIL\n" + out))
                if rc:
                    failed.append(s + " tests")
    if os.path.exists(os.path.join(HERE, "_check", "sourcemap.json")):
        os.remove(os.path.join(HERE, "_check", "sourcemap.json"))
    if failed:
        print("FAILED: " + "; ".join(failed))
        return 1
    if missing:
        print("INCOMPLETE: missing tools: " + ", ".join(missing))
        return 2
    print("ALL PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
