#!/usr/bin/env python3
"""rbx-quick.py: deterministic output for the small toggle/list/status skills (no model judgment). Stdlib; Windows, macOS, Linux.
The skill body runs this through dynamic shell injection and prints the result as is.
  list                  everything the kit installed (runs kit-list.py, same text)
  light on|off          Obsidian light / full view of the claudes-vault (runs the vault's update script with --set-view; no update, offline)
  check                 is a newer vault or kit available (update-check.py, read-only) + the vault-folder status line (is this folder the loaded vault, where the vault is)
Always exits 0 so the injected command never aborts the skill; failures are printed as one line."""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(args, timeout=300):
    try:
        p = subprocess.run([sys.executable, "-I"] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError) as e:
        return 127, "", type(e).__name__
    return p.returncode, (p.stdout or "").rstrip("\n"), (p.stderr or "").strip()


def find_vault():
    home = os.path.expanduser("~")
    for c in (os.environ.get("CLAUDES_VAULT"), os.path.join(home, "Obsidian", "claudes-vault")):
        if c and os.path.isdir(c):
            return c
    return None


def cmd_list():
    rc, out, err = run([os.path.join(HERE, "kit-list.py")])
    print(out if out else "rbx-list: no output (%s). Run /rbx-update." % (err.splitlines()[-1] if err else "kit-list.py failed"))


def cmd_light(mode):
    view = {"on": "light", "off": "full"}.get(mode)
    if not view:
        print("rbx-light: use `on` or `off`.")
        return
    v = find_vault()
    if not v:
        print("rbx-light: no claudes-vault found (set CLAUDES_VAULT or clone it to ~/Obsidian/claudes-vault).")
        return
    if os.name == "nt":
        script = os.path.join(v, "vault-update.ps1")
        cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", script, "-SetView", view]
    else:
        script = os.path.join(v, "vault-update.sh")
        cmd = ["bash", script, "--set-view", view]
    if not os.path.isfile(script):
        print("rbx-light: %s not found in the vault. Run /rbx-update first." % os.path.basename(script))
        return
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300, cwd=v, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError) as e:
        print("rbx-light: could not run the vault script (%s)." % type(e).__name__)
        return
    out = ((p.stdout or "") + (p.stderr or "")).strip()
    print(out if out else "rbx-light: the vault script printed nothing (exit %d)." % p.returncode)


def cmd_check():
    rc, out, err = run([os.path.join(HERE, "update-check.py")], 300)
    print(out if out else "rbx-check: no output (%s)." % (err.splitlines()[-1] if err else "update-check.py failed"))
    rc, out, err = run([os.path.join(HERE, "vault-mode.py"), "status"], 60)
    if out:
        print(out.splitlines()[0])


def main(argv):
    a = argv[1:]
    if a[:1] == ["list"]:
        cmd_list()
    elif a[:1] == ["light"]:
        cmd_light(a[1] if len(a) > 1 else "")
    elif a[:1] == ["check"]:
        cmd_check()
    else:
        print("rbx-quick: use list | light on|off | check")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
