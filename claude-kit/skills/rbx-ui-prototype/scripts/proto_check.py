#!/usr/bin/env python3
"""proto_check.py: validate a Claude-written UI prototype (rbx-ui-prototype). Stdlib only, no network.
Usage: python -I proto_check.py <ui/prototype dir | path/to/index.html> [--no-handoff]
Prints PASS/FAIL/WARN lines and a summary; exit 1 when any FAIL."""
import io, json, os, re, shutil, subprocess, sys, tempfile

RISKY = ("backdrop-filter", "filter:", "mix-blend-mode", "clip-path", "mask-image", "conic-gradient", "radial-gradient", "text-shadow")
DEVICES = ("phone", "tablet", "desktop")
res = []


def ck(name, cond, detail="", warn=False):
    res.append(("PASS" if cond else ("WARN" if warn else "FAIL"), name, "" if cond else str(detail)[:300]))


def rd(p):
    return io.open(p, encoding="utf-8", errors="replace").read()


def blocks(html, tag):
    return re.findall(r"<%s\b[^>]*>(.*?)</%s>" % (tag, tag), html, re.S | re.I)


def split_top(s, ch):
    out, depth, cur = [], 0, ""
    for c in s:
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        if c == ch and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += c
    return out + [cur]


def soft_shadows(css):
    bad = []
    for m in re.finditer(r"box-shadow\s*:\s*([^;}]+)", css):
        for one in split_top(m.group(1), ","):
            toks = [t for t in split_top(one.strip().replace("\n", " "), " ") if t and t != "inset"]
            lens = [t for t in toks if re.match(r"^-?[\d.]|^calc\(", t)]
            if len(lens) >= 3 and not re.match(r"^-?0(\.0+)?[a-z%]*$", lens[2]):
                bad.append(one.strip()[:60])
    return bad


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    need_handoff = "--no-handoff" not in argv
    if not args:
        print("usage: proto_check.py <ui/prototype dir | index.html> [--no-handoff]")
        return 2
    p = os.path.abspath(args[0])
    d = p if os.path.isdir(p) else os.path.dirname(p)
    f = os.path.join(d, "index.html") if os.path.isdir(p) else p
    if not os.path.isfile(f):
        print("FAIL index.html exists :: %s" % f)
        return 1
    html = rd(f)
    css = re.sub(r"/\*.*?\*/", "", "\n".join(blocks(html, "style")), flags=re.S)
    js = "\n".join(b for m, b in re.findall(r"<script\b([^>]*)>(.*?)</script>", html, re.S | re.I) if "src=" not in m)
    nb = re.search(r'id=["\']notbuildable["\'].*?</section>', html, re.S | re.I)
    nbtxt = (nb.group(0) if nb else "").lower()
    ck("single file: only index.html is referenced (no src/href files, no link tags)", not re.search(r"<link\b|<script[^>]+src=|<img[^>]+src=[\"'](?!data:)|<iframe|@import", html, re.I), "found external reference")
    urls = [u for u in re.findall(r"(?:https?:)?//[\w.-]+\.[a-z]{2,}[^\s\"'<>)]*", html, re.I) if "www.w3.org/2000/svg" not in u]
    ck("no external URLs (no CDN, no fonts, no network)", not urls, urls[:3])
    ck("no network or storage APIs (fetch, XHR, WebSocket, sendBeacon, import())", not re.search(r"\bfetch\s*\(|XMLHttpRequest|WebSocket|EventSource|sendBeacon|\bimport\s*\(", js), "network API in script")
    ck("size sane (<= 400 KB, <= 900 lines)", len(html) <= 400000 and html.count("\n") <= 900, "%d bytes, %d lines" % (len(html), html.count("\n")), warn=True)
    ck("has <title> and viewport meta", bool(re.search(r"<title>[^<]+</title>", html)) and "name=\"viewport\"" in html)
    ck("visible 'prototype, not the game' notice", bool(re.search(r"prototype[^<]{0,40}not the game", html, re.I)))
    m = re.search(r"const\s+SCREENS\s*=\s*\[(.*?)\];", js, re.S)
    ck("screens array with >= 3 screens (const SCREENS = [{id:...}])", bool(m) and len(re.findall(r"\bid\s*:", m.group(1))) >= 3, "SCREENS missing or < 3")
    ck("state object (const/let state)", bool(re.search(r"\b(const|let|var)\s+state\s*=", js)))
    ck("single render function", len(re.findall(r"function\s+render\s*\(", js)) == 1)
    miss = [x for x in DEVICES if not re.search(r"\bid\s*:\s*['\"]%s['\"]" % x, js)]
    ck("device switcher with phone, tablet and desktop", not miss and "devices" in html, miss)
    rot = [
        bool(re.search(r"id=[\"']rotate[\"']", html)),
        "portrait" in js and "landscape" in js,
        bool(re.search(r"===\s*['\"]r['\"]", js)),
        bool(re.search(r"rotate\s*:\s*(true|1)\b", js)) and bool(re.search(r"rotate\s*:\s*(false|0)\b", js)),
    ]
    ck("rotate control (id=rotate) with portrait and landscape, key R, desktop does not rotate", all(rot), "missing: " + ", ".join(n for n, ok in zip(("id=rotate button", "portrait+landscape", "R key", "rotate flags (phone/tablet true, desktop false)"), rot) if not ok))
    ck("orientation kept in page state, not localStorage", "localStorage" not in js, "localStorage used", warn=True)
    ck("safe-area overlay toggle", bool(re.search(r"safe", js + html, re.I)) and bool(re.search(r"type=\"checkbox\"|safe-toggle|showsafe", html)))
    ck("hover state in CSS (:hover)", ":hover" in css)
    ck("prefers-reduced-motion media query present (reduce effects for players who ask)", "prefers-reduced-motion" in css, "no reduced-motion rule", warn=True)
    ck("press handlers (pointerdown + pointerup, or mouse/touch)", bool(re.search(r"pointerdown|mousedown|touchstart", js)) and bool(re.search(r"pointerup|mouseup|touchend", js)))
    ck("disabled state (:disabled, .disabled or aria-disabled)", bool(re.search(r":disabled|\.disabled|aria-disabled", css + js)))
    ck("press 0.08 s and release 0.15 s timings present", bool(re.search(r"\b(0?\.08|80)\b", js + css)) and bool(re.search(r"\b(0?\.15|150)\b", js + css)))
    ck("click handling", bool(re.search(r"addEventListener\(\s*['\"]click|onclick", js + html)))
    ck("keyboard shortcuts (keydown)", "keydown" in js)
    ck("Roblox constraints badge list (id=constraints)", bool(re.search(r'id=["\']constraints["\']', html)) and "UICorner" in html)
    ck("'not buildable as-is' note (id=notbuildable)", bool(nb))
    ck("fidelity panel (id=fidelity)", bool(re.search(r'id=["\']fidelity["\']', html)))
    low = css.lower()
    bad = [t for t in RISKY if t in low and t.rstrip(":") not in nbtxt]
    ck("risky CSS (blur, filter, blend, clip-path, mask, gradients other than linear, text-shadow) only when named in the not-buildable note", not bad, bad)
    ss = soft_shadows(low)
    ck("box-shadow only hard (blur 0) or flagged as soft shadow in the note", not ss or "box-shadow" in nbtxt or "soft shadow" in nbtxt, ss[:2])
    node = shutil.which("node")
    if node and js.strip():
        t = os.path.join(tempfile.mkdtemp(prefix="protochk-"), "a.js")
        io.open(t, "w", encoding="utf-8").write(js)
        r = subprocess.run([node, "--check", t], capture_output=True, text=True)
        shutil.rmtree(os.path.dirname(t), ignore_errors=True)
        ck("script syntax (node --check)", r.returncode == 0, r.stderr[:200])
    else:
        res.append(("WARN", "script syntax not checked (no node on PATH)", ""))
    sp = os.path.join(d, "spec.json")
    try:
        sj = json.loads(rd(sp))
        ok = isinstance(sj.get("screens"), list) and len(sj["screens"]) >= 1 and all(s.get("elements") for s in sj["screens"]) and "style" in sj
    except Exception as e:
        ok = False
        sj = str(e)
    ck("spec.json valid (style + screens with elements)", ok, sj if isinstance(sj, str) else "missing style or screens")
    if need_handoff:
        hp = os.path.join(d, "handoff.md")
        h = rd(hp) if os.path.isfile(hp) else ""
        ck("handoff.md exists with Roblox instance trees (Frame, UICorner, UIStroke, Scale)", len(h) > 500 and all(x in h for x in ("Frame", "UICorner", "UIStroke", "Scale")), "missing or thin")
        ck("handoff.md names the next step /rbx-ui and says it is not the game", "/rbx-ui" in h and "not the game" in h.lower())
    for st, n, dt in res:
        print("%s %s%s" % (st, n, (" :: " + dt) if dt else ""))
    nf = sum(1 for r in res if r[0] == "FAIL")
    print("proto_check: %d pass, %d warn, %d fail  (%s)" % (sum(1 for r in res if r[0] == "PASS"), sum(1 for r in res if r[0] == "WARN"), nf, f))
    return 1 if nf else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
