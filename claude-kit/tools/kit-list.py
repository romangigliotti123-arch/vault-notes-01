#!/usr/bin/env python3
"""kit-list.py: list everything the kit installed (Skills / Agents / Mods), markdown for chat, one bullet per item. Read-only, stdlib; Windows, macOS, Linux.
Reads <config>/claude-kit/installed.tsv, the SKILL.md / agent frontmatter descriptions, and mods/.claude-plugin/marketplace.json
(installed state of mods from `claude plugin list --json`, else "installed: unknown").
Usage: kit-list.py [--config DIR] [--mods DIR] [--width N]"""
import argparse, json, os, re, shutil, subprocess, sys

MARKET = "roblox-vault-kit-mods"
# Used only when the SKILL.md has no `summary:` and the description is trigger text with no usable first clause.
FALLBACK = {
    "rbx-make": "Designs and builds a Roblox game end to end from the vault, skills and assets",
    "rbx-research": "Deep multi-source research on a topic with every claim labelled by evidence level",
    "rbx-ailib": "How Claude finds and uses skills, agents and notes in the AI Library Vault",
    "rbx-use": "How Claude should use the claudes-vault Obsidian vault",
}


def frontmatter_field(path, name):
    try:
        t = open(path, encoding="utf-8", errors="replace").read(8000)
    except OSError:
        return ""
    m = re.match(r"---\s*\n(.*?)\n---", t, re.S)
    fm = m.group(1) if m else ""
    d = re.search(r"^%s:\s*(.*)$" % name, fm, re.M)
    if not d:
        return ""
    v = d.group(1).strip()
    if v[:1] in "\"'" and v[-1:] == v[:1] and len(v) > 1:
        v = v[1:-1]
    elif v in (">", "|", ">-", "|-"):
        m2 = re.search(r"^%s:\s*[>|]-?\s*\n((?:[ \t]+.*\n?)+)" % name, fm, re.M)
        v = " ".join(x.strip() for x in m2.group(1).splitlines()) if m2 else ""
    return v.replace('\\"', '"')


def desc(path):
    """summary: first, else description."""
    return frontmatter_field(path, "summary") or frontmatter_field(path, "description")


def one_line(s, w=90):
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s*Kit skill: wins over similar installed skills\.?", "", s).strip()
    s = re.sub(r"\s*\([^()]*\)", "", s)      # drop parentheticals
    s = re.sub(r"\s*\([^()]*$", "", s)       # unclosed paren
    s = re.sub(r"^(Run|Type) /[\w-]+ (to|for) ", "", s)
    s = re.sub(r"^/[\w-]+ (?=[a-z])", "", s)
    if re.match(r"(Use|Invoke|Trigger)\b.{0,40}?\b(when|whenever|if|for)\b", s, re.I):
        m = re.search(r"[:\u2014] (.+)$", s) or re.search(r", (.+)$", s)
        if m:
            s = m.group(1)
    m = re.search(r"^(.{12,}?[.!?])(\s+[A-Z/]|$)", s)   # first sentence
    if m:
        s = m.group(1)
    s = s.rstrip(".").strip()
    if s[:1].islower():
        s = s[0].upper() + s[1:]
    if len(s) > w:
        m = re.search(r"^(.{40,}?)(?:;| \u2014 | - ) ", s)
        if m and len(m.group(1)) <= w:
            return m.group(1).rstrip(" ,;:")
        cut = s[:w]
        cut = cut[: cut.rfind(" ")] if " " in cut else cut
        s = cut.rstrip(" ,;:-") + "\u2026"
    return s


def find_mods(arg, config):
    here = os.path.dirname(os.path.abspath(__file__))
    cands = [arg, os.environ.get("CLAUDES_VAULT") and os.path.join(os.environ["CLAUDES_VAULT"], "claude-kit", "mods"),
             os.path.join(os.path.expanduser("~"), "Obsidian", "claudes-vault", "claude-kit", "mods"),
             os.path.join(here, "..", "mods"), os.path.join(config, "claude-kit", "mods")]
    for c in cands:
        if c and os.path.isfile(os.path.join(c, ".claude-plugin", "marketplace.json")):
            return os.path.abspath(c)
    return None


def plugin_state(config):
    exe = shutil.which("claude")
    if not exe:
        return None
    try:
        r = subprocess.run([exe, "plugin", "list", "--json"], capture_output=True, text=True, timeout=30,
                           env=dict(os.environ, CLAUDE_CONFIG_DIR=config), stdin=subprocess.DEVNULL)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--config"); ap.add_argument("--mods"); ap.add_argument("--width", type=int, default=110)
    a = ap.parse_args()
    config = a.config or os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    man = os.path.join(config, "claude-kit", "installed.tsv")
    if not os.path.isfile(man):
        print("rbx-list: no kit manifest at %s (kit not installed here; run /rbx-update)." % man)
        return 1
    rels = [l.split("\t")[0] for l in open(man, encoding="utf-8", errors="replace").read().splitlines() if l.strip()]
    SM = "claude-kit/vault-mode/.claude/"
    always = sorted({r.split("/")[1] for r in rels if r.startswith("skills/") and r.endswith("/SKILL.md")})
    stored = sorted({r[len(SM + "skills/"):].split("/")[0] for r in rels if r.startswith(SM + "skills/") and r.endswith("/SKILL.md")})
    skills = always + stored
    agents = sorted({r[len(SM + "agents/"):-3] for r in rels if r.startswith(SM + "agents/") and r.endswith(".md")} | {r[len("agents/"):-3] for r in rels if r.startswith("agents/") and r.endswith(".md")})
    def skill_path(s):
        sp = os.path.join(config, "skills", s, "SKILL.md")
        return sp if os.path.isfile(sp) else os.path.join(config, "claude-kit", "vault-mode", ".claude", "skills", s, "SKILL.md")
    def agent_path(g):
        ap_ = os.path.join(config, "agents", g + ".md")
        return ap_ if os.path.isfile(ap_) else os.path.join(config, "claude-kit", "vault-mode", ".claude", "agents", g + ".md")
    w = min(a.width, 90)
    dash = "—"

    def W(name):  # keep whole line <= ~110 chars
        return max(45, min(w, 110 - len(name) - 8))

    out = ["Installed from the Roblox Dev Mastery Vault kit.", ""]
    out += ["Everything except the always-on commands is OFF in normal Claude sessions: type /rbx-load in a project folder to turn on Roblox dev mode (/rbx-unload turns it off).", ""]
    out += ["## Always-on commands (%d)" % len(always), ""]
    for s in always:
        sp = skill_path(s)
        d = one_line(frontmatter_field(sp, "summary"), W(s)) or FALLBACK.get(s) or one_line(desc(sp), W(s)) or "(no description)"
        out += ["- **/%s** %s %s" % (s, dash, d), ""]
    out += ["## Skills in Roblox dev mode (%d; usable after /rbx-load)" % len(stored), ""]
    for s in stored:
        sp = skill_path(s)
        d = one_line(frontmatter_field(sp, "summary"), W(s)) or FALLBACK.get(s) or one_line(desc(sp), W(s)) or "(no description)"
        out += ["- **/%s** %s %s" % (s, dash, d), ""]
    out += ["## Agents in Roblox dev mode (%d)" % len(agents), ""]
    for g in agents:
        out += ["- **%s** %s %s" % (g, dash, one_line(desc(agent_path(g)), W(g)) or "(no description)"), ""]
    mods = find_mods(a.mods, config)
    cnt = 0
    lines = []
    if mods:
        data = json.load(open(os.path.join(mods, ".claude-plugin", "marketplace.json"), encoding="utf-8"))
        state = plugin_state(config)
        cmd = {"rbx-subagent-hud": "/rbx-subagent-hud", "rbx-graph": "/rbx-graph"}
        for p in sorted(data.get("plugins", []), key=lambda x: x["name"]):
            n = p["name"]
            inst = "unknown" if state is None else ("yes" if ("%s@%s" % (n, data.get("name", MARKET))) in state else "no")
            lines += ["- **%s**%s %s %s (installed: %s)" % (n, (" (%s)" % cmd[n]) if n in cmd else "", dash, one_line(p.get("description", ""), max(45, w - 25 - len(n))), inst), ""]
            cnt += 1
    out += ["## Mods (%d)" % cnt, ""]
    out += lines or ["- None found (the kit's mods folder is not in the vault clone yet)", ""]
    cold = [r for r in rels if r.startswith("claude-kit/vault-mode/cold/")]
    out += ["## Cold area (%d files in %d topics)" % (len(cold), len({r.split("/")[3] for r in cold})), "", "- Bulk that skills point to ([cold:topic/file]); not loaded into projects. `python claude-kit/tools/vault-mode.py cold` lists it.", ""]
    pack = os.path.join(config, "claude-kit", "skillpack")
    n = sum(1 for d, _, f in os.walk(pack) if "SKILL.md" in f) if os.path.isdir(pack) else 0
    out += ["## Roblox pack skills (%s)" % (n or "?"), "", "- Run `/rbx list` to browse them, or `/rbx find <words>` to search.", ""]
    print("\n".join(out).rstrip("\n"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
