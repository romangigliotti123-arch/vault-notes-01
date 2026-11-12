#!/usr/bin/env python3
"""design_gate.py - the design-pack gate of /rbx-workflow, /rbx-plan, /rbx-make and /rbx-manager. Stdlib only, no network, no secrets.

A NEW game may not get game code until Games/<slug>/design-pack/APPROVED.md shows the five design steps approved (or skipped by the user on purpose), in this order:
  refs   reference collection from similar top games (refs.md)
  style  style test: 3-8 hero props shown and approved (style-test.md)
  ui     UI examples, several versions per key screen, phone frames first (ui.md)
  map    map layout with stud scale (map.md)
  plan   one-page plan approved (plan.md)

  design_gate.py init <slug>                       create design-pack/ and APPROVED.md (idempotent, never overwrites)
  design_gate.py status <slug>                     print the part lines, then DESIGN GATE: PASS or DESIGN GATE: STOP - next: <part> (exit 0 / 1)
  design_gate.py approve <slug> <part> [--note T]  mark a part approved with today's date; refuses when design-pack/<part file> is missing or empty
  design_gate.py skip <slug> <part|all> --reason T log a user override (skip one part or the whole pack) in APPROVED.md; the reason is the user's own words
  design_gate.py extra <slug> <name> [--note T]    record an optional extra design part (thumbnail, cutscene, ...) as approved
  design_gate.py figma <slug> --stage S --tools LIST|-   the Figma check: connected = any tool name contains "figma"; prints the connect prompt ONCE per stage S
                                                   (start, style, ui, map, approve, redesign-<n>, ...), then only a one-line reminder. Never asks for or stores a token, never installs anything.
<slug> may also be a game folder path. Games root: --games DIR, else env GAMES_ROOT, else <vault folder>/Games (nearest folder with .claude/vault-mode.json).
APPROVED.md line format (the one place the gate reads):   - [x] ui | approved 2026-11-12 | note      - [ ] map      - [skip] ui | skipped 2026-11-12 | user said: ...
"""
import argparse, datetime, os, re, sys

sys.dont_write_bytecode = True
PARTS = [
    ("refs", "refs.md", "collect reference screenshots and notes from 3-6 similar top games (rbx-design-pack, part 1)"),
    ("style", "style-test.md", "style test: 3-8 hero props built and shown, user picks the look (part 2)"),
    ("ui", "ui.md", "UI examples: 3 versions of each key screen, phone frames first, user picks (part 3)"),
    ("map", "map.md", "map layout with stud scale, zones, flow, landmarks (part 4)"),
    ("plan", "plan.md", "one-page plan that pulls the approved parts together (part 5)"),
]
NAMES = [p[0] for p in PARTS]
LINE = re.compile(r"^\s*-\s*\[(x|X| |skip)\]\s*([a-z0-9_-]+)\s*(?:\|(.*))?$")
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{0,48}$")


def today():
    return datetime.date.today().isoformat()


def vault_root(start=None):
    d = os.path.abspath(start or os.getcwd())
    home = os.path.realpath(os.path.expanduser("~"))
    while True:
        if os.path.isfile(os.path.join(d, ".claude", "vault-mode.json")) and os.path.realpath(d) != home:
            return d
        up = os.path.dirname(d)
        if up == d:
            return None
        d = up


def game_dir(a):
    s = a.slug
    if os.path.isdir(s) and (os.sep in s or "/" in s or s.startswith(".")):
        return os.path.abspath(s)
    if not SLUG.match(s):
        sys.exit("design_gate: bad slug %r (kebab-case) or folder path not found" % s)
    root = a.games or os.environ.get("GAMES_ROOT")
    if not root:
        v = vault_root()
        if not v:
            sys.exit("design_gate: this is not the vault folder; start the session in the vault folder or pass --games DIR")
        root = os.path.join(v, "Games")
    return os.path.join(os.path.abspath(root), s)


def pack_dir(g):
    return os.path.join(g, "design-pack")


def approved_path(g):
    return os.path.join(pack_dir(g), "APPROVED.md")


def skeleton(slug):
    out = ["# Design pack approvals: %s" % slug, "",
           "The gate (`design_gate.py status`) reads only the `- [x] part | ...` lines. New games get no game code until all five are `[x]` or `[skip]`.",
           "Order: refs, style, ui, map, plan. The user can skip the whole pack or one part by saying so; the skill then logs it under Overrides.", "", "## Parts", ""]
    for n, f, what in PARTS:
        out.append("- [ ] %s | %s -> %s" % (n, f, what))
    out += ["", "## Extra parts (optional: thumbnails, animations, cutscenes, ...)", "", "## Overrides", ""]
    return "\n".join(out) + "\n"


def parse(text):
    st = {}
    for ln in text.splitlines():
        m = LINE.match(ln)
        if m and m.group(2) in NAMES:
            st[m.group(2)] = (m.group(1).lower() if m.group(1).strip() else " ", (m.group(3) or "").strip())
    return st


def read(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def write(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def overall_skip(text):
    return re.search(r"^\s*-\s*OVERRIDE all\b", text, re.M) is not None


def replace_part(text, part, newline):
    out, done = [], False
    for ln in text.splitlines():
        m = LINE.match(ln)
        if m and m.group(2) == part and not done:
            out.append(newline)
            done = True
        else:
            out.append(ln)
    return "\n".join(out) + "\n"


def append_section(text, header, line):
    lines = text.splitlines()
    if header in lines:
        i = lines.index(header)
        j = i + 1
        while j < len(lines) and not lines[j].startswith("## "):
            j += 1
        k = j
        while k > i + 1 and not lines[k - 1].strip():
            k -= 1
        lines.insert(k, line)
        return "\n".join(lines) + "\n"
    return text.rstrip("\n") + "\n\n" + header + "\n\n" + line + "\n"


def cmd_init(a):
    g = game_dir(a)
    p = approved_path(g)
    os.makedirs(pack_dir(g), exist_ok=True)
    if os.path.isfile(p):
        print("design-pack exists: %s" % p)
    else:
        write(p, skeleton(os.path.basename(g)))
        print("created %s" % p)
    return 0


def cmd_status(a):
    g = game_dir(a)
    text = read(approved_path(g))
    if not text:
        print("no design-pack yet (%s)" % approved_path(g))
        print("DESIGN GATE: STOP - next: refs (%s); run: design_gate.py init %s" % (PARTS[0][2], os.path.basename(g)))
        return 1
    st = parse(text)
    skip_all = overall_skip(text)
    nxt = None
    for n, f, what in PARTS:
        s, note = st.get(n, (" ", ""))
        mark = {"x": "approved", "skip": "skipped", " ": "MISSING"}.get(s, "MISSING")
        if skip_all and s == " ":
            mark = "skipped (whole pack)"
        print("%-6s %-22s %s" % (n, mark, note))
        if s == " " and not skip_all and nxt is None:
            nxt = (n, what)
    if nxt:
        print("DESIGN GATE: STOP - next: %s (%s)" % nxt)
        return 1
    print("DESIGN GATE: PASS%s" % (" (override logged)" if skip_all or any(v[0] == "skip" for v in st.values()) else ""))
    return 0


def need_part(p):
    if p not in NAMES:
        sys.exit("design_gate: part must be one of %s" % ", ".join(NAMES))


def cmd_approve(a):
    g = game_dir(a)
    need_part(a.part)
    p = approved_path(g)
    if not os.path.isfile(p):
        write(p, skeleton(os.path.basename(g)))
    f = dict((n, x) for n, x, _ in PARTS)[a.part]
    body = read(os.path.join(pack_dir(g), f)).strip()
    if len(body) < 40:
        print("REFUSED: design-pack/%s is missing or empty; write the part first (it must say what was shown and what the user picked)" % f)
        return 1
    idx = NAMES.index(a.part)
    st = parse(read(p))
    for earlier in NAMES[:idx]:
        if st.get(earlier, (" ",))[0] == " " and not overall_skip(read(p)):
            print("REFUSED: %s comes before %s and is not approved or skipped yet" % (earlier, a.part))
            return 1
    line = "- [x] %s | approved %s | %s" % (a.part, today(), (a.note or "user picked").strip())
    write(p, replace_part(read(p), a.part, line))
    print("approved %s" % a.part)
    return 0


def cmd_skip(a):
    g = game_dir(a)
    p = approved_path(g)
    if not a.reason or len(a.reason.strip()) < 3:
        print("REFUSED: --reason is required (the user's own words)")
        return 1
    if not os.path.isfile(p):
        write(p, skeleton(os.path.basename(g)))
    text = read(p)
    if a.part == "all":
        text = append_section(text, "## Overrides", "- OVERRIDE all %s: user skipped the design pack: %s" % (today(), a.reason.strip()))
    else:
        need_part(a.part)
        text = replace_part(text, a.part, "- [skip] %s | skipped %s | %s" % (a.part, today(), a.reason.strip()))
        text = append_section(text, "## Overrides", "- OVERRIDE %s %s: %s" % (a.part, today(), a.reason.strip()))
    write(p, text)
    print("override logged: %s" % a.part)
    return 0


def cmd_extra(a):
    g = game_dir(a)
    p = approved_path(g)
    if not os.path.isfile(p):
        write(p, skeleton(os.path.basename(g)))
    if not re.match(r"^[a-z0-9][a-z0-9-]{0,30}$", a.name):
        sys.exit("design_gate: extra name must be kebab-case")
    write(p, append_section(read(p), "## Extra parts (optional: thumbnails, animations, cutscenes, ...)",
                            "- [x] extra-%s | approved %s | %s" % (a.name, today(), (a.note or "user picked").strip())))
    print("extra recorded: %s" % a.name)
    return 0


FIGMA_DOCS = "https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/"
FIGMA_PROMPT = [
    "FIGMA: not connected. Why it helps: you see and edit real frames (UI screens, map layout, boards) before any code is written, and I can read your edits back.",
    "Connect (about 2 minutes, you run it, I change nothing): in a normal terminal run  claude plugin install figma@claude-plugins-official  then restart Claude Code, type /plugin, open the Installed tab, select figma, press Enter to sign in, click Allow access.",
    "Or without the plugin:  claude mcp add --transport http figma https://mcp.figma.com/mcp  then start a new session, type /mcp, select figma, Authenticate, Allow access.",
    "Seats: writing to the canvas needs a Full seat (free during the beta); Starter plans have very low tool-call limits, Professional 200 calls/day. Docs: " + FIGMA_DOCS,
    "Say 'connected' when done, or 'no Figma' and I draw with HTML/SVG instead (rbx-ui-prototype and the specialist skills).",
]


def cmd_figma(a):
    g = game_dir(a)
    names = []
    t = a.tools
    if t == "-":
        t = sys.stdin.read()
    for n in re.split(r"[,\n]", t or ""):
        n = n.strip()
        if n and n.lower() != "none":
            names.append(n)
    connected = any("figma" in n.lower() for n in names)
    if connected:
        print("FIGMA: connected (%d tools). Draw this stage in Figma/FigJam; the HTML/SVG route is only the fallback." % sum(1 for n in names if "figma" in n.lower()))
        return 0
    import json
    mp = os.path.join(pack_dir(g), ".figma-prompted.json")
    try:
        done = json.loads(read(mp) or "{}")
    except ValueError:
        done = {}
    if not isinstance(done, dict):
        done = {}
    if a.stage in done:
        print("FIGMA: not connected (already offered for stage %s; continuing with the HTML/SVG fallback, one reminder at the next stage)." % a.stage)
        return 0
    done[a.stage] = today()
    write(mp, json.dumps(done, sort_keys=True) + "\n")
    print("\n".join(FIGMA_PROMPT))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="design_gate.py")
    ap.add_argument("--games")
    sp = ap.add_subparsers(dest="cmd", required=True)
    for c in ("init", "status"):
        p = sp.add_parser(c); p.add_argument("slug")
    p = sp.add_parser("approve"); p.add_argument("slug"); p.add_argument("part"); p.add_argument("--note")
    p = sp.add_parser("skip"); p.add_argument("slug"); p.add_argument("part"); p.add_argument("--reason")
    p = sp.add_parser("extra"); p.add_argument("slug"); p.add_argument("name"); p.add_argument("--note")
    p = sp.add_parser("figma"); p.add_argument("slug"); p.add_argument("--stage", required=True); p.add_argument("--tools", default="-")
    a = ap.parse_args(argv)
    return {"init": cmd_init, "status": cmd_status, "approve": cmd_approve, "skip": cmd_skip, "extra": cmd_extra, "figma": cmd_figma}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
