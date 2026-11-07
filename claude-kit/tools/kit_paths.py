#!/usr/bin/env python3
"""kit_paths.py: where the vault and the kit live (ONE folder). Standard library only; other tools import it (sys.path-inserted, python -I safe) and the 3 stub skills carry a copy named where.py.

Everything of the kit lives in ONE folder, the vault folder (default ~/Obsidian/rbx-dev-vault; an existing claudes-vault folder keeps its name):
    <vault>/                      the vault clone (notes, Games/, Models/, My-Skills/, My-Agents/, START-HERE.md)
    <vault>/.rbx/claude-kit/      the installed kit (tools, systems, skillpack, vault-mode store, state, backup, roblox-reference, installed.tsv); hidden from git
Outside it only: ~/.claude/skills/{rbx-update,rbx-check,rbx-uninstall}/ (thin stubs + this file as where.py) and ~/.claude/rbx-dev-vault.path (one line: the vault folder).
Moving the folder moves everything. A moved folder is found again by /rbx-update (the stub runs where.py, which looks in this order and rewrites the pointer):
    1. the folder this file lives in (<vault>/.rbx/claude-kit/tools or <vault>/claude-kit/tools)   2. env RBX_DEV_VAULT / CLAUDES_VAULT   3. the pointer file
    4. the current folder and its parents (a loaded vault folder)   5. ~/Obsidian/rbx-dev-vault, ~/Obsidian/claudes-vault
KIT HOME (the folder that holds claude-kit/): <vault>/.rbx when the one-folder layout exists; else the Claude config folder (legacy layout: tests, kit-only installs).

  where.py [--set FOLDER]       print VAULT / KIT / SKILL (the full text of the stub skill this file sits in) and refresh the pointer
  kit_paths.py kit-home         print the kit home
  kit_paths.py vault [--config DIR]   print the vault folder (empty when there is none): used by the installers
"""
import os
import sys

VAULT_NAMES = ("rbx-dev-vault", "claudes-vault")
POINTER = "rbx-dev-vault.path"
RBX = ".rbx"


def user_home():
    return os.path.abspath(os.path.expanduser(os.environ.get("CLAUDE_KIT_HOME") or "~"))


def config_dir(explicit=None):
    if explicit:
        return os.path.abspath(os.path.expanduser(explicit))
    d = os.environ.get("CLAUDE_CONFIG_DIR")
    if d:
        return os.path.abspath(os.path.expanduser(d))
    return os.path.join(user_home(), ".claude")


def pointer_file(config):
    return os.path.join(config, POINTER)


def is_vault(d):
    return bool(d) and os.path.isdir(d) and os.path.exists(os.path.join(d, ".git"))


def has_layout(d):
    return bool(d) and os.path.isdir(os.path.join(d, RBX, "claude-kit"))


def from_script(script):
    """the vault that holds this tool: <vault>/.rbx/claude-kit/tools/x (installed copy) or <vault>/claude-kit/tools/x (the kit source inside the vault clone)"""
    if not script:
        return None
    d = os.path.dirname(os.path.realpath(script))
    for _ in range(7):
        par = os.path.dirname(d)
        if os.path.basename(d) == "claude-kit" and par != d:
            if os.path.basename(par) == RBX:
                v = os.path.dirname(par)
                return v if os.path.isdir(v) else None
            if is_vault(par) and os.path.exists(os.path.join(par, "vault-update.sh")):
                return par
        if par == d:
            break
        d = par
    return None


def read_pointer(config):
    try:
        with open(pointer_file(config), encoding="utf-8") as f:
            ln = f.read().splitlines()[0].strip()
        return ln or None
    except (OSError, IndexError):
        return None


def write_pointer(config, vault):
    """one line; only rewritten when it differs; never raises"""
    try:
        if read_pointer(config) == vault:
            return False
        os.makedirs(config, exist_ok=True)
        tmp = pointer_file(config) + ".%d.tmp" % os.getpid()
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(vault + "\n")
        os.replace(tmp, pointer_file(config))
        return True
    except OSError:
        return False


def from_cwd(cwd=None):
    d = os.path.abspath(cwd or os.getcwd())
    home = os.path.realpath(user_home())
    for _ in range(25):
        if os.path.realpath(d) != home and is_vault(d) and (os.path.isfile(os.path.join(d, ".claude", "vault-mode.json")) or has_layout(d)):
            return d
        par = os.path.dirname(d)
        if par == d:
            break
        d = par
    return None


def defaults():
    base = os.path.join(user_home(), "Obsidian")
    return [os.path.join(base, n) for n in VAULT_NAMES]


def find_vault(config=None, script=None, cwd=None):
    """the vault folder or None (order: script location, env, pointer, cwd, defaults)"""
    v = from_script(script)
    if v:
        return v
    for k in ("RBX_DEV_VAULT", "CLAUDES_VAULT"):
        e = os.environ.get(k)
        if e and is_vault(os.path.expanduser(e)):
            return os.path.abspath(os.path.expanduser(e))
    p = read_pointer(config_dir(config))
    if p and is_vault(p):
        return os.path.abspath(p)
    v = from_cwd(cwd)
    if v:
        return v
    for d in defaults():
        if is_vault(d):
            return d
    return None


def kit_home(config=None, script=None):
    """the folder that holds claude-kit/: <vault>/.rbx (one-folder layout) else the config folder (legacy)"""
    if os.environ.get("RBX_LAYOUT") == "legacy":      # tests and kit-only installs: the old layout (claude-kit/ in the config folder)
        return config_dir(config)
    e = os.environ.get("RBX_KIT_HOME")
    if e:
        return os.path.abspath(os.path.expanduser(e))
    v = from_script(script)
    if v:
        return os.path.join(v, RBX)
    v = find_vault(config, None)
    if v and has_layout(v):
        return os.path.join(v, RBX)
    return config_dir(config)


def install_home(vault, config=None):
    """where an installer puts the kit: inside the vault when there is one, else the config folder (kit-only install)"""
    return os.path.join(vault, RBX) if vault else config_dir(config)


def stub_name(script):
    d = os.path.dirname(os.path.abspath(script))
    if os.path.basename(os.path.dirname(d)) == "skills" and os.path.basename(d).startswith("rbx-"):
        return os.path.basename(d)
    return None


def where_main(argv):
    me = os.path.abspath(__file__)
    stub = stub_name(me)
    config = os.path.dirname(os.path.dirname(os.path.dirname(me))) if stub else config_dir()
    if argv[:1] == ["--set"] and len(argv) > 1:
        v = os.path.abspath(os.path.expanduser(argv[1]))
        if not is_vault(v):
            print("NOT A VAULT FOLDER (no .git): %s" % v)
            return 1
        write_pointer(config, v)
    v = find_vault(config, None if stub else me)
    if not v:
        print("VAULT NOT FOUND. Ask the user where the rbx-dev-vault folder is (it may have been moved), then run this again with --set <folder>. If there is none yet, follow https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main/SETUP-FOR-CLAUDE.md")
        return 1
    write_pointer(config, v)
    kit = os.path.join(v, RBX, "claude-kit")
    print("VAULT " + v)
    print("KIT " + kit)
    if stub:
        sk = os.path.join(kit, "vault-mode", ".claude", "skills", stub, "SKILL.md")
        print("SKILL " + sk + ("" if os.path.isfile(sk) else "   (MISSING: run the setup runbook SETUP-FOR-CLAUDE.md)"))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    a = sys.argv[1:]
    if a[:1] == ["kit-home"]:
        print(kit_home(script=os.path.abspath(__file__)))
        sys.exit(0)
    if a[:1] == ["vault"]:
        cfg = a[a.index("--config") + 1] if "--config" in a and a.index("--config") + 1 < len(a) else None
        v = find_vault(cfg, os.path.abspath(__file__))
        if v:
            print(v)
        sys.exit(0)
    sys.exit(where_main(a))
