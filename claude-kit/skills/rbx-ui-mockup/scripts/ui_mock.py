#!/usr/bin/env python3
"""ui_mock.py: the MANUAL Nano Banana 2.1 package (preference on). Builds <project>/ui-mockup/ with ready-to-paste prompts (style sheet first, then each screen; text placeholders only),
the reference images to upload, numbered steps for the Gemini website, a checklist and a status that picks up images the user drops into results/. Stdlib only, no network, never blocks.

  ui_mock.py package (--brief brief.json | --spec spec.json) --project DIR [--design DIR] [--refs IMG ...]
        --design = the automatic design sheet folder (its png/ frames become layout references); --refs = the user's own screenshots / reference frames (copied, never altered)
  ui_mock.py status DIR [--write Games/<slug>]    which images arrived in DIR/ui-mockup/results/ (png/jpg/webp), aspect warnings, the next step; --write records the pending state as a skip reason
  ui_mock.py gen --project DIR [--go --yes]       quiet advanced path: only when GEMINI_API_KEY or GOOGLE_API_KEY is ALREADY in your environment; runs rbx-thumbnail/scripts/gen_image.py
        (the only Gemini client); dry-run unless --go AND --yes; never prints the key; no price is hard-coded: check your own plan before --yes
The pipeline keeps working without the images: layout, spec, build and compare come from the automatic design sheet; the images only guide style (colours, icon style, decoration). Spec wins on any conflict.
"""
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ui_common as C  # noqa: E402

PHONE = (844, 390)
FEEL = (("rounded", ("FredokaOne", "Nunito", "LuckiestGuy", "Bangers", "Cartoon")), ("techno", ("SciFi", "Michroma", "Jura", "Sarpanch", "TitilliumWeb")),
        ("clean geometric", ("BuilderSans", "Gotham", "SourceSans", "Roboto", "Arimo", "Ubuntu")))
PLACEHOLDER = {"label": "[TITLE]", "button": "[BUTTON]", "chip": "[NUMBER]"}
RESULT_EXT = (".png", ".jpg", ".jpeg", ".webp")


def font_feel(names):
    for feel, keys in FEEL:
        if any(any(k in n for k in keys) for n in names):
            return feel + " bold sans-serif"
    return "bold sans-serif"


def load_model(brief_p, spec_p):
    if brief_p:
        b = C.read_json(brief_p)
        st = b["style"]
        screens = [{"name": s["name"], "purpose": s.get("purpose", ""), "elements": [{"name": e["name"], "type": e["type"], "rect": e["rect"]} for e in s["elements"]]} for s in b["screens"]]
        return {"game": b.get("game", "game"), "palette": st["palette"], "fonts": list(st["fonts"].values()), "corner": st.get("corner", 0.18), "stroke": st.get("stroke", 3), "screens": screens}
    sp = C.read_json(spec_p)
    t = sp["tokens"]
    screens = []
    for f in sp["frames"]:
        if f.get("kind") == "phone":
            screens.append({"name": f["screen"], "purpose": "", "elements": [{"name": e["name"], "type": e["type"], "rect": e["rect"]} for e in f["elements"]]})
    return {"game": sp.get("game", "game"), "palette": t["palette"], "fonts": list(t["fonts"].values()), "corner": t.get("corner", 0.18), "stroke": t.get("stroke", 3), "screens": screens}


def style_block(m):
    pal = ", ".join("%s %s" % (k, v) for k, v in list(m["palette"].items())[:5])
    return ("Flat game UI mockup for a mobile-first Roblox game. Palette (max 5 colours): %s. Rounded panels with corner radius about %d%% of the panel height, uniform %dpx outline, "
            "flat fill or a simple two-colour gradient, one icon style (simple filled glyphs), one font feel (%s). No photographs, no real-world brands, no existing game's UI, no watermark, "
            "no drop shadows or bevels that a Roblox UIStroke/UICorner/UIGradient cannot draw." % (pal, round(m["corner"] * 100), m["stroke"], font_feel(m["fonts"])))


def style_prompt(m):
    return (style_block(m) + "\n\nMake ONE style sheet image: a button in four states (default, hover, pressed, disabled), a panel with a title bar, a currency chip, a progress bar, "
            "six simple icons, the palette swatches and one line of sample text. Plain neutral background. Text is placeholder only (Aa, 123). Wide landscape layout.")


def screen_prompt(m, sc):
    lines = []
    for e in sc["elements"]:
        l, t, w, h = e["rect"]
        ph = PLACEHOLDER.get(e["type"])
        lines.append("- %s (%s): left %d%%, top %d%%, width %d%%, height %d%%%s" % (e["name"], e["type"], round(l * 100), round(t * 100), round(w * 100), round(h * 100), "; text %s" % ph if ph else ""))
    return (style_block(m) + "\n\nMatch the attached style sheet exactly (same colours, corner radius, outline, icon style) and use the attached layout image as the position reference.\n"
            "Canvas: wide landscape, about 2.16:1 (844 x 390, a phone held sideways). Screen: %s. Show a plain neutral blurred game background so the panels do not float on a fake scene.\n"
            "Elements, positions and sizes as fractions of the screen:\n%s\n"
            "Leave the bottom-left and bottom-right 18%% empty (thumbstick and jump) and the top 6%% empty (Roblox top bar). Buttons at least 11%% of the screen height. "
            "All text is a placeholder in square brackets: do not invent words or numbers. Do not add elements that are not listed." % (sc["name"], "\n".join(lines)))


def files_for(m):
    out = [{"id": "00", "name": "style-sheet", "file": "style-sheet.png", "kind": "style", "prompt": style_prompt(m), "aspect": [16, 9]}]
    for i, sc in enumerate(m["screens"], 1):
        out.append({"id": "%02d" % i, "name": sc["name"], "file": "%s.png" % re.sub(r"[^A-Za-z0-9_-]", "", sc["name"]).lower(), "kind": "screen", "prompt": screen_prompt(m, sc), "aspect": list(PHONE)})
    return out


def instructions(items, refs_by):
    n = len(items)
    steps = [
        "Open https://gemini.google.com in your browser and sign in with your Google account (Google's help says you must be signed in to generate images).",
        "Start a new chat. In the left sidebar choose Images (Google's help names this entry), or ask for an image in the chat. Pick the Nano Banana image model: Google's help page for the Gemini app "
        "calls the current one Nano Banana 2; if the model picker shows Nano Banana 2.1 or newer, choose that one.",
        "Limits: image generation uses your Gemini usage limit and the limits depend on your Gemini plan and can change. You can see what is left in Gemini under Settings > Usage Limits.",
    ]
    for it in items:
        refs = refs_by.get(it["id"], [])
        what = "Upload " + (", ".join("references/" + r for r in refs) if refs else "no reference images (none were found; the prompt is enough)") + " with the + (add files) button in the prompt box"
        if it["kind"] == "style":
            steps.append("STYLE SHEET. %s. Open prompts/%s-%s.md, copy the text inside the code block, paste it, send." % (what, it["id"], it["name"]))
            steps.append("Check the style sheet against CHECKLIST.md (palette, four button states, no photo, no brand). If it is wrong, ask for a redo ONCE with the fix written in words. Then download it "
                         "(download icon on the image) and save it as results/%s." % it["file"])
        else:
            steps.append("SCREEN %s. Start from the same chat or a new one. %s, and also upload results/style-sheet.png. Open prompts/%s-%s.md, copy the text in the code block, paste, send." % (it["name"], what, it["id"], it["name"]))
            steps.append("Check screen %s against CHECKLIST.md (positions close to the layout reference, no extra elements, empty corners). One redo at most. Download it and save it as results/%s." % (it["name"], it["file"]))
    steps.append("Tell Claude the images are in results/ (or just continue): Claude picks them up with `ui_mock.py status`, keeps the spec rectangles as the layout truth, takes colours and icon style from the images, and never copies text from an image. To click through it first, say: prototype this mockup (rbx-ui-prototype makes one HTML page you open in your browser).")
    return "# Manual UI mockups with Nano Banana 2.1 on the Gemini website\n\n" + "\n".join("%d. %s" % (i, s) for i, s in enumerate(steps, 1)) + "\n\nYou can skip all of this at any time: `/rbx-mockup off` returns to the automatic design-first mode. Nothing waits for these images.\n"


CHECKLIST = """# Checklist for every generated image
- [ ] The palette matches the style block (at most 5 colours, no surprise colours).
- [ ] Panels have a uniform outline and flat or simple-gradient fill (no ornament that varies along an edge: it cannot be a Roblox 9-slice).
- [ ] Buttons show clear states; touch targets look at least 11% of the screen height.
- [ ] Only the listed elements exist; no extra gem counters, banners or logos.
- [ ] The bottom corners (thumbstick, jump) and the top bar are empty.
- [ ] All text is placeholder or garbled: that is fine, the real text comes from the spec.
- [ ] No real brand, character, watermark or another game's UI.
- [ ] The file is saved in results/ with the exact expected name.
"""


def package(a, opt):
    m = load_model(opt("--brief"), opt("--spec"))
    proj = opt("--project")
    if not proj:
        print("usage: ui_mock.py package (--brief F | --spec F) --project DIR [--design DIR] [--refs IMG ...]", file=sys.stderr)
        return 2
    root = os.path.join(proj, "ui-mockup")
    for d in ("prompts", "references", "results"):
        os.makedirs(os.path.join(root, d), exist_ok=True)
    items = files_for(m)
    user_refs = []
    if "--refs" in a:
        for x in a[a.index("--refs") + 1:]:
            if x.startswith("--"):
                break
            user_refs.append(x)
    design = opt("--design")
    refs_by, copied = {}, []

    def put(src, label):
        if not os.path.isfile(src):
            return None
        dest = "%02d-%s" % (len(copied) + 1, re.sub(r"[^A-Za-z0-9._-]", "_", label))
        shutil.copyfile(src, os.path.join(root, "references", dest))
        copied.append(dest)
        return dest
    style_refs = [r for r in (put(p, "mine-" + os.path.basename(p)) for p in user_refs) if r]
    if design:
        for nm in ("components",):
            r = put(os.path.join(design, "png", nm + ".png"), "layout-" + nm + ".png")
            if r and nm == "components":
                style_refs.append(r)
    refs_by["00"] = style_refs
    for it in items[1:]:
        refs = list(style_refs[:len(user_refs)])
        if design:
            r = put(os.path.join(design, "png", "%s.phone.png" % it["name"]), "layout-%s.png" % it["name"])
            if r:
                refs.append(r)
        refs_by[it["id"]] = refs
    for it in items:
        head = "# Prompt %s: %s\n\nAspect: %s\nUpload: %s\nSave the result as: results/%s\n\nPaste this text (everything inside the code block):\n\n" % (
            it["id"], it["name"], "wide landscape, about 2.16:1 (844 x 390)" if it["kind"] == "screen" else "wide landscape", ", ".join("references/" + r for r in refs_by.get(it["id"], [])) or "nothing", it["file"])
        C.write_text(os.path.join(root, "prompts", "%s-%s.md" % (it["id"], it["name"])), head + "```\n" + it["prompt"] + "\n```\n")
    C.write_text(os.path.join(root, "INSTRUCTIONS.md"), instructions(items, refs_by))
    C.write_text(os.path.join(root, "CHECKLIST.md"), CHECKLIST)
    C.write_text(os.path.join(root, "README.md"), "# ui-mockup\nManual Nano Banana 2.1 package made by ui_mock.py. Start with INSTRUCTIONS.md. Drop finished images into results/ with the names in status.json. Nothing here is needed to build the UI.\n")
    C.write_text(os.path.join(root, "status.json"), C.jdump({"version": 1, "game": m["game"], "expected": [{"id": i["id"], "name": i["name"], "file": i["file"], "aspect": i["aspect"], "refs": refs_by.get(i["id"], [])} for i in items]}))
    nsteps = len(re.findall(r"(?m)^\d+\. ", open(os.path.join(root, "INSTRUCTIONS.md"), encoding="utf-8").read()))
    print("ui_mock: wrote %s: %d prompts (style sheet + %d screens), %d reference images, %d numbered steps, checklist; waiting for %d images in results/" % (root, len(items), len(items) - 1, len(copied), nsteps, len(items)))
    return 0


def find_result(root, stem):
    for ext in RESULT_EXT:
        p = os.path.join(root, "results", stem + ext)
        if os.path.isfile(p):
            return p
    return None


def status(proj, write=None):
    root = os.path.join(proj, "ui-mockup")
    sp = os.path.join(root, "status.json")
    if not os.path.isfile(sp):
        print("ui_mock: no ui-mockup package here (run package first)")
        return 1
    st = C.read_json(sp)
    got, waiting, warns = [], [], []
    for e in st["expected"]:
        p = find_result(root, os.path.splitext(e["file"])[0])
        if not p:
            waiting.append(e["name"])
            continue
        got.append(e["name"])
        if p.lower().endswith(".png"):
            try:
                w, h, _, _ = C.decode_png(p)
                ew, eh = e["aspect"]
                if abs(w / h - ew / eh) / (ew / eh) > 0.15:
                    warns.append("%s is %dx%d (aspect %.2f), the screen wants about %.2f: crop it or ask for a wider image" % (e["file"], w, h, w / h, ew / eh))
            except (ValueError, OSError):
                warns.append("%s could not be read as an 8-bit PNG: it still counts, look at it by eye" % e["file"])
    print("UI mockup (manual): %d of %d images received%s" % (len(got), len(st["expected"]), "; waiting for: " + ", ".join(waiting) if waiting else ""))
    for w in warns:
        print("  WARN " + w)
    if waiting:
        print("  next: keep building from the design sheet spec; images are picked up here when they arrive (INSTRUCTIONS.md step list)")
    else:
        print("  all images received: take colours and icon style from them, keep the spec rectangles, build, then ui_compare.py gate --mode manual (or say: prototype this mockup, for a clickable HTML page first)")
    if write and waiting:
        import ui_compare
        rec = {"gate": "ui-design", "done": False, "reason": "manual mockups pending: %s" % ", ".join(waiting), "mode": "manual", "result": "skipped", "status": "skipped", "advisory": True}
        ui_compare.write_gate(write, rec)
        print(ui_compare.gate_line(rec))
    return 0


def gen_image_path():
    p = os.environ.get("UI_MOCK_GEN_IMAGE")
    if p:
        return p
    return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "rbx-thumbnail", "scripts", "gen_image.py"))


def gen(a, opt):
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        print("ui_mock gen: no Gemini key in your environment; nothing to do (the manual package works without one)")
        return 3
    proj = opt("--project")
    root = os.path.join(proj or "", "ui-mockup")
    sp = os.path.join(root, "status.json")
    if not proj or not os.path.isfile(sp):
        print("ui_mock gen: run package first (--project DIR)", file=sys.stderr)
        return 2
    st = C.read_json(sp)
    jobs = []
    for e in st["expected"]:
        text = open(os.path.join(root, "prompts", "%s-%s.md" % (e["id"], e["name"])), encoding="utf-8").read()
        m = re.search(r"```\n(.*?)\n```", text, re.S)
        asp = "16:9" if e["name"] == "style-sheet" else "21:9"
        jobs.append({"name": os.path.splitext(e["file"])[0], "prompt": m.group(1) if m else text, "aspect": asp, "refs": [os.path.join(root, "references", r) for r in e["refs"]]})
    pf = os.path.join(root, "prompts.json")
    C.write_text(pf, C.jdump(jobs))
    real = "--go" in a and "--yes" in a
    cmd = [sys.executable, "-I", gen_image_path(), "batch", "--prompts-file", pf, "--out", os.path.join(root, "results")] + ([] if real else ["--dry-run"])
    print("ui_mock gen: %d images through gen_image.py (%s). Price depends on your Gemini plan or API pricing: check it first; a real run needs --go --yes." % (len(jobs), "REAL" if real else "dry run"))
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
    out = (r.stdout + r.stderr)
    if key:
        out = out.replace(key, "***")
    print(out.strip()[-1500:])
    return r.returncode


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a and a.index(n) + 1 < len(a) else d
    c = a[0]
    if c == "package":
        return package(a, opt)
    if c == "status":
        return status(a[1] if len(a) > 1 else ".", opt("--write"))
    if c == "gen":
        return gen(a, opt)
    print("unknown command " + c, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
