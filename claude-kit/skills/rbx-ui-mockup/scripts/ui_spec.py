#!/usr/bin/env python3
"""ui_spec.py: exact UI spec (element rectangles, colours, text, font sizes) from the design sheet's browser layout, normalised to Roblox scale values. Stdlib only, no network.

  ui_spec.py export DIR|index.html [--out spec.json] [--browser P] [--from-model]
        runs the sheet in an already-installed headless Chrome/Edge (--dump-dom: the page script writes getBoundingClientRect / computed style into the DOM); no browser or --from-model
        = the rectangles the layout declares (spec.model.json), marked "source": "model". Text always comes from the brief, never from an image.
  ui_spec.py validate spec.json [--frame ID]       scale 0..1, Roblox-safe unique names, real fonts, touch target, text size, contrast, 35% panel cap, sibling overlap (errors exit 1, rest advisory)
  ui_spec.py roblox spec.json --frame Shop.phone   per element: AnchorPoint / Position / Size as UDim2 scale, UICorner scale, UIStroke, font, text (the build list)
  ui_spec.py check DIR                             browser export vs the declared model: max pixel delta (proves the sheet renders where the spec says)
Element schema: {"name","type","frame","parent","state","variant","rect":[l,t,w,h] scale of the frame,"px":[x,y,w,h],"fill","stroke":{"px","color"},"corner":0..0.5,"text","font","font_px","color"}
"""
import html as H
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ui_common as C  # noqa: E402
import ui_design as D  # noqa: E402

OUT_RE = re.compile(r'<pre id="ui-spec-out"[^>]*>(.*?)</pre>', re.S)


MARK = "UISPEC<<"


def dump_dom(index_html, browser, timeout=40):
    r = C.run_browser(browser, ["--dump-dom", "--virtual-time-budget=2000", C.file_url(index_html)], timeout, marker=(MARK, 'id="ui-spec-out"'))
    m = OUT_RE.search(r["stdout"])
    if m:
        return json.loads(H.unescape(m.group(1)))
    i = r["log"].find(MARK)
    if i >= 0:
        j = r["log"].find(">>UISPEC", i)
        if j > i:
            return json.loads(r["log"][i + len(MARK):j])
    raise RuntimeError("the browser did not return the layout export")


def normalise(raw, model=None):
    fonts_by = {}
    if model:
        for f in model["frames"]:
            for e in f["elements"]:
                fonts_by[(f["id"], e["name"])] = e.get("font")
    frames = []
    for f in raw["frames"]:
        fw, fh = float(f["w"]), float(f["h"])
        els = []
        for e in f["elements"]:
            w, h = float(e["w"]), float(e["h"])
            cp = float(e.get("corner_px") or 0)
            els.append({
                "name": e["name"], "type": e["type"], "frame": f["id"], "parent": e.get("parent"), "state": e.get("state"), "variant": e.get("variant"),
                "rect": [round(e["x"] / fw, 4), round(e["y"] / fh, 4), round(w / fw, 4), round(h / fh, 4)],
                "px": [round(e["x"], 1), round(e["y"], 1), round(w, 1), round(h, 1)],
                "fill": e.get("fill"), "stroke": {"px": e["stroke_px"], "color": e.get("stroke_color")} if e.get("stroke_px") else None,
                "corner": round(min(0.5, cp / max(1.0, min(w, h))), 4), "text": e.get("text"), "font": fonts_by.get((f["id"], e["name"])),
                "font_px": e.get("font_px"), "color": e.get("color"),
            })
        frames.append({"id": f["id"], "kind": f.get("kind"), "screen": f.get("screen"), "w": fw, "h": fh, "elements": els})
    return frames


def export(index_html, browser=None, prefer_model=False, timeout=90):
    if os.path.isdir(index_html):
        index_html = os.path.join(index_html, "index.html")
    base = os.path.dirname(os.path.abspath(index_html))
    model = C.read_json(os.path.join(base, "spec.model.json"))
    br = None if prefer_model else (browser or C.find_browser())
    if br:
        try:
            raw = dump_dom(index_html, br, timeout)
            return {"version": 1, "game": model.get("game"), "source": "browser", "tokens": model["tokens"], "frames": normalise(raw, model)}
        except Exception as e:
            sys.stderr.write("ui_spec: browser export failed (%s), using the declared model\n" % e)
    m = dict(model)
    m["source"] = "model"
    return m


def validate(spec, only=None):
    errs, warns = [], []
    pal_fonts = set(C.FONTS)
    for f in spec["frames"]:
        if only and f["id"] != only:
            continue
        seen = set()
        fw, fh = f["w"], f["h"]
        for e in f["elements"]:
            tag = "%s/%s" % (f["id"], e["name"])
            if not D.NAME_RE.match(e["name"]):
                errs.append("%s: not a Roblox-safe Instance name" % tag)
            if e["name"] in seen:
                errs.append("%s: duplicate name in the frame" % tag)
            seen.add(e["name"])
            l, t, w, h = e["rect"]
            if min(l, t) < -0.0005 or l + w > 1.0005 or t + h > 1.0005 or w <= 0 or h <= 0:
                errs.append("%s: rect %s is outside 0..1" % (tag, e["rect"]))
            if e.get("font") and e["font"] not in pal_fonts:
                errs.append("%s: font %r is not a Roblox Enum.Font name" % (tag, e["font"]))
            if f.get("kind") == "phone":
                if e["type"] == "button" and h * fh < D.MIN_TARGET_PX - 0.5:
                    warns.append("%s: touch target %.0f px < %d" % (tag, h * fh, D.MIN_TARGET_PX))
                if e.get("font_px") and e["font_px"] < D.MIN_TEXT_PX - 0.01:
                    warns.append("%s: text %.0f px < %d at phone size" % (tag, e["font_px"], D.MIN_TEXT_PX))
            if e["type"] == "panel" and not e.get("parent") and w * h > D.PANEL_CAP and "popup" not in e["name"].lower():
                warns.append("%s: panel covers %.0f%% of the frame (cap 35%%)" % (tag, w * h * 100))
            if e.get("text") and e.get("color") and e.get("fill") and C.is_hex(e["color"]) and C.is_hex(e["fill"]):
                cr = C.contrast(C.hex2rgb(e["color"]), C.hex2rgb(e["fill"]))
                if cr < 4.5:
                    warns.append("%s: contrast %.1f:1 < 4.5:1" % (tag, cr))
        tops = [e for e in f["elements"] if e["type"] in ("button", "chip") and not e.get("parent")]
        for i, a in enumerate(tops):
            for b in tops[i + 1:]:
                ox = min(a["rect"][0] + a["rect"][2], b["rect"][0] + b["rect"][2]) - max(a["rect"][0], b["rect"][0])
                oy = min(a["rect"][1] + a["rect"][3], b["rect"][1] + b["rect"][3]) - max(a["rect"][1], b["rect"][1])
                if ox > 0.002 and oy > 0.002:
                    warns.append("%s: %s overlaps %s" % (f["id"], a["name"], b["name"]))
    return errs, warns


def roblox_lines(spec, fid):
    f = next((x for x in spec["frames"] if x["id"] == fid), None)
    if not f:
        raise SystemExit("frame %r not in spec (have: %s)" % (fid, ", ".join(x["id"] for x in spec["frames"])))
    out = []
    for e in f["elements"]:
        l, t, w, h = e["rect"]
        line = "%s [%s] AnchorPoint (0,0) Position UDim2.fromScale(%.4f, %.4f) Size UDim2.fromScale(%.4f, %.4f)" % (e["name"], e["type"], l, t, w, h)
        if e.get("corner"):
            line += " UICorner scale %.3f" % e["corner"]
        if e.get("stroke"):
            line += " UIStroke %spx %s" % (e["stroke"]["px"], e["stroke"].get("color"))
        if e.get("fill"):
            line += " BackgroundColor3 %s" % e["fill"]
        if e.get("text") is not None:
            line += " Text %r Font %s TextColor3 %s font_px %s (TextScaled + UITextSizeConstraint min 14)" % (e["text"], e.get("font"), e.get("color"), e.get("font_px"))
        if e.get("parent"):
            line += " Parent %s (rect above is of the frame, convert to parent scale if nested)" % e["parent"]
        out.append(line)
    return out


def check(dirpath, browser=None):
    base = dirpath if os.path.isdir(dirpath) else os.path.dirname(dirpath)
    model = C.read_json(os.path.join(base, "spec.model.json"))
    br = browser or C.find_browser()
    if not br:
        return None, "no headless browser: nothing to compare"
    spec = export(os.path.join(base, "index.html"), br)
    if spec["source"] != "browser":
        return None, "browser export failed"
    worst, n = 0.0, 0
    bym = {(f["id"], e["name"]): e for f in model["frames"] for e in f["elements"]}
    for f in spec["frames"]:
        for e in f["elements"]:
            m = bym.get((f["id"], e["name"]))
            if not m:
                return 99.0, "element %s/%s is in the browser export but not in the model" % (f["id"], e["name"])
            worst = max(worst, max(abs(a - b) for a, b in zip(e["px"], m["px"])))
            n += 1
    return worst, "%d elements compared" % n


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else default
    cmd = a[0]
    if len(a) < 2:
        print("usage: ui_spec.py export|validate|roblox|check <path>", file=sys.stderr)
        return 2
    if cmd == "export":
        target = a[1]
        sp = export(target, opt("--browser"), "--from-model" in a)
        base = target if os.path.isdir(target) else os.path.dirname(os.path.abspath(target))
        out = opt("--out") or os.path.join(base, "spec.json")
        C.write_text(out, C.jdump(sp))
        print("ui_spec: wrote %s (source %s, %d frames, %d elements)" % (out, sp["source"], len(sp["frames"]), sum(len(f["elements"]) for f in sp["frames"])))
        return 0
    if cmd == "validate":
        errs, warns = validate(C.read_json(a[1]), opt("--frame"))
        for e in errs:
            print("ERROR " + e)
        for w in warns:
            print("WARN  " + w)
        print("ui_spec validate: %d errors, %d warnings (warnings advisory)" % (len(errs), len(warns)))
        return 1 if errs else 0
    if cmd == "roblox":
        for ln in roblox_lines(C.read_json(a[1]), opt("--frame", "phone")):
            print(ln)
        return 0
    if cmd == "check":
        worst, note = check(a[1], opt("--browser"))
        if worst is None:
            print("ui_spec check: skipped (%s)" % note)
            return 0
        print("ui_spec check: max delta %.2f px (%s)" % (worst, note))
        return 0 if worst <= 2.0 else 1
    print("unknown command " + cmd, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
