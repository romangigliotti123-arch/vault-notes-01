#!/usr/bin/env python3
"""ui_design.py: brief -> local HTML/CSS design sheet (tokens, every button in default/hover/pressed/disabled, one layout per screen as phone + desktop frames), optional PNG render.
Stdlib only, no network, no installs. The sheet is the AUTOMATIC DESIGN-FIRST step of rbx-ui-mockup; ui_spec.py exports exact rectangles from it.

  ui_design.py init [--out brief.json]               write a sample brief (palette, fonts, buttons, screens HUD + Shop)
  ui_design.py validate brief.json                   errors (exit 1) and warnings (touch target, text size, contrast, panel share, safe zones)
  ui_design.py build brief.json --out DIR            DIR/index.html + DIR/spec.model.json (the spec the layout declares)
  ui_design.py render DIR [--browser P] [--frames ID,ID] render DIR/png/<frame id>.png with a headless Chrome/Edge already on the machine; none found = HTML only, say so, exit 0
  ui_design.py all brief.json --out DIR              validate + build + render + spec.json (browser export, else the model)

Brief: {"game","style":{"palette":{key:#hex},"fonts":{key:RobloxFontName},"corner":0.18,"stroke":3,"spacing":[4,8,16]},"frames":["phone","desktop"],
 "buttons":[{"name","text","fill":key,"text_color":key,"w":px,"h":px}],
 "screens":[{"name","purpose","elements":[{"name","type":panel|label|button|bar|chip|icon|grid,"rect":[l,t,w,h] (0..1 of the frame),"rect_desktop":[..],"aspect":1,
   "parent","fill":key,"stroke":true,"corner":0..0.5,"text","font":key,"text_color":key,"text_scale":0.5,"variant","value":0..1,"gradient":[key,key],"grid":{"cols","rows","gap"}}]}]}
Frames are drawn at real pixel size: phone 844x390, tablet 1180x820, desktop 1920x1080 (the sizes rbx-visual uses). Element names become the Roblox instance names the built UI must use.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ui_common as C  # noqa: E402

FRAMES = {"phone": (844, 390), "tablet": (1180, 820), "desktop": (1920, 1080)}
STATES = ("default", "hover", "pressed", "disabled")
TYPES = ("panel", "label", "button", "bar", "chip", "icon", "grid")
NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,47}$")
TOPBAR_PX = 36
MIN_TEXT_PX = 14
MIN_TARGET_PX = 44
PANEL_CAP = 0.35

SAMPLE = {
    "game": "sample",
    "style": {
        "palette": {"bg": "#1E2A44", "panel": "#2E4A7D", "accent": "#FFC83D", "text": "#FFFFFF", "warn": "#E5484D"},
        "fonts": {"title": "FredokaOne", "body": "BuilderSansBold"},
        "corner": 0.18, "stroke": 3, "spacing": [4, 8, 16, 24],
    },
    "frames": ["phone", "desktop"],
    "buttons": [
        {"name": "Primary", "text": "Play", "fill": "accent", "text_color": "bg", "w": 160, "h": 48},
        {"name": "Secondary", "text": "Close", "fill": "panel", "text_color": "text", "w": 160, "h": 48},
        {"name": "Danger", "text": "Delete", "fill": "warn", "text_color": "text", "w": 160, "h": 48},
    ],
    "screens": [
        {"name": "HUD", "purpose": "always-on heads-up display", "elements": [
            {"name": "CoinChip", "type": "chip", "rect": [0.02, 0.1, 0.16, 0.12], "text": "0", "font": "body"},
            {"name": "GemChip", "type": "chip", "rect": [0.2, 0.1, 0.16, 0.12], "text": "0", "font": "body"},
            {"name": "ProgressBar", "type": "bar", "rect": [0.3, 0.88, 0.4, 0.05], "value": 0.6},
            {"name": "ShopButton", "type": "button", "variant": "Primary", "rect": [0.84, 0.1, 0.14, 0.14], "text": "Shop"},
        ]},
        {"name": "Shop", "purpose": "buy items with coins", "elements": [
            {"name": "ShopPanel", "type": "panel", "rect": [0.25, 0.14, 0.5, 0.66], "fill": "panel", "stroke": True},
            {"name": "Title", "type": "label", "parent": "ShopPanel", "rect": [0.3, 0.18, 0.4, 0.12], "text": "Shop", "font": "title"},
            {"name": "ItemGrid", "type": "grid", "parent": "ShopPanel", "rect": [0.3, 0.32, 0.4, 0.3], "grid": {"cols": 3, "rows": 1, "gap": 0.02}},
            {"name": "BuyButton", "type": "button", "variant": "Primary", "parent": "ShopPanel", "rect": [0.3, 0.66, 0.18, 0.12], "text": "Buy"},
            {"name": "CloseButton", "type": "button", "variant": "Secondary", "parent": "ShopPanel", "rect": [0.52, 0.66, 0.18, 0.12], "text": "Close"},
        ]},
    ],
}


def font_name(brief, key):
    f = brief["style"]["fonts"]
    return f.get(key, key) if key else f.get("body") or next(iter(f.values()))


def colour(brief, key, default="text"):
    p = brief["style"]["palette"]
    if key is None:
        key = default
    return p[key] if key in p else key


def frame_ids(brief):
    return [f for f in (brief.get("frames") or ["phone", "desktop"]) if f in FRAMES]


def validate(brief):
    errs, warns = [], []
    st = brief.get("style") or {}
    pal, fonts = st.get("palette") or {}, st.get("fonts") or {}
    if not pal:
        errs.append("style.palette is empty")
    for k, v in pal.items():
        if not C.is_hex(v):
            errs.append("palette %s: %r is not a hex colour" % (k, v))
    if not fonts:
        errs.append("style.fonts is empty")
    for k, v in fonts.items():
        if v not in C.FONTS:
            errs.append("font %s: %r is not a Roblox Enum.Font name" % (k, v))
    if len(pal) > 8:
        warns.append("palette has %d colours (3-5 recommended, max 8)" % len(pal))
    for f in brief.get("frames") or []:
        if f not in FRAMES:
            errs.append("unknown frame %r (phone, tablet, desktop)" % f)
    variants = {b.get("name"): b for b in brief.get("buttons") or []}
    for b in variants.values():
        if not NAME_RE.match(str(b.get("name"))):
            errs.append("button variant name %r is not a Roblox-safe name" % b.get("name"))
        for k in ("fill", "text_color"):
            if k in b and b[k] not in pal and not C.is_hex(b[k]):
                errs.append("button %s: %s %r is neither a palette key nor a hex colour" % (b.get("name"), k, b[k]))
    if not brief.get("screens"):
        errs.append("no screens")
    for sc in brief.get("screens") or []:
        names = set()
        if not NAME_RE.match(str(sc.get("name"))):
            errs.append("screen name %r is not a Roblox-safe name" % sc.get("name"))
        for el in sc.get("elements") or []:
            n = el.get("name")
            tag = "%s.%s" % (sc.get("name"), n)
            if not NAME_RE.match(str(n)):
                errs.append("%s: name must match [A-Za-z][A-Za-z0-9_]* (it becomes the Instance name)" % tag)
            if n in names:
                errs.append("%s: duplicate element name" % tag)
            names.add(n)
            if el.get("type") not in TYPES:
                errs.append("%s: type %r not in %s" % (tag, el.get("type"), ", ".join(TYPES)))
            for rk in ("rect", "rect_desktop"):
                r = el.get(rk)
                if rk == "rect" and r is None:
                    errs.append("%s: rect [left, top, width, height] missing" % tag)
                if r is not None and (len(r) != 4 or any(not isinstance(x, (int, float)) for x in r) or r[0] < 0 or r[1] < 0 or r[2] <= 0 or r[3] <= 0 or r[0] + r[2] > 1.0001 or r[1] + r[3] > 1.0001):
                    errs.append("%s: %s %r must be 4 numbers inside 0..1" % (tag, rk, r))
            for k in ("fill", "text_color"):
                if k in el and el[k] not in pal and not C.is_hex(str(el[k])):
                    errs.append("%s: %s %r is neither a palette key nor a hex colour" % (tag, k, el[k]))
            if el.get("font") and el["font"] not in fonts and el["font"] not in C.FONTS:
                errs.append("%s: font %r unknown" % (tag, el["font"]))
            if el.get("type") == "button" and el.get("variant") and el["variant"] not in variants:
                errs.append("%s: variant %r not in brief.buttons" % (tag, el["variant"]))
            if el.get("parent") and el["parent"] not in names and el["parent"] not in [e.get("name") for e in sc.get("elements") or []]:
                errs.append("%s: parent %r not on this screen" % (tag, el["parent"]))
    if errs:
        return errs, warns
    for fid in frame_ids(brief):
        fw, fh = FRAMES[fid]
        for sc in brief["screens"]:
            for el in sc["elements"]:
                x, y, w, h = resolve(el, fid)
                tag = "%s.%s@%s" % (sc["name"], el["name"], fid)
                if el["type"] == "button" and fid == "phone" and h * fh < MIN_TARGET_PX:
                    warns.append("%s: button %.0f px tall, touch target should be >= %d px (about 11%% of 390)" % (tag, h * fh, MIN_TARGET_PX))
                if el["type"] == "panel" and w * h > PANEL_CAP and not (el.get("popup") or "popup" in el["name"].lower()):
                    warns.append("%s: panel covers %.0f%% of the screen (cap %.0f%%)" % (tag, w * h * 100, PANEL_CAP * 100))
                if fid == "phone" and y * fh < TOPBAR_PX and el["type"] != "panel":
                    warns.append("%s: starts inside the Roblox top bar zone (top %d px)" % (tag, TOPBAR_PX))
                if fid == "phone" and el["type"] in ("button", "chip") and y > 0.55 and (x < 0.18 or x + w > 0.82) and y + h > 0.7:
                    warns.append("%s: sits in a thumbstick/jump corner zone" % tag)
                if el.get("text"):
                    fp = font_px(el, fw, fh, fid)
                    if fid == "phone" and fp < MIN_TEXT_PX:
                        warns.append("%s: text %d px < %d px at phone size" % (tag, fp, MIN_TEXT_PX))
                    bg = bg_for_text(brief, el)
                    fg = colour(brief, variant_of(brief, el).get("text_color", "bg")) if el["type"] == "button" else colour(brief, el.get("text_color"), "text")
                    if bg and C.contrast(C.hex2rgb(fg), C.hex2rgb(bg)) < 4.5:
                        warns.append("%s: text contrast %.1f:1 < 4.5:1" % (tag, C.contrast(C.hex2rgb(fg), C.hex2rgb(bg))))
    return errs, warns


def bg_for_text(brief, el):
    if el["type"] == "button":
        v = variant_of(brief, el)
        return colour(brief, v.get("fill", "accent"))
    if el["type"] in ("chip", "panel"):
        return colour(brief, el.get("fill"), "panel")
    return colour(brief, "bg") if "bg" in brief["style"]["palette"] else None


def variant_of(brief, el):
    vs = brief.get("buttons") or []
    for v in vs:
        if v.get("name") == el.get("variant"):
            return v
    return vs[0] if vs else {"name": "Default", "fill": "accent", "text_color": "bg", "w": 160, "h": 48}


def resolve(el, fid):
    """-> (l, t, w, h) fractions of the frame for this element in this frame kind."""
    fw, fh = FRAMES[fid]
    r = list(el.get("rect_" + fid) or el["rect"])
    if el.get("aspect"):
        r[2] = r[3] * fh * float(el["aspect"]) / fw
    return tuple(r)


def font_px(el, fw, fh, fid, rect=None):
    x, y, w, h = rect or resolve(el, fid)
    ts = float(el.get("text_scale", 0.5))
    px = max(MIN_TEXT_PX, int(round(h * fh * ts)))
    est = 0.55 * px * max(1, len(str(el.get("text", ""))))
    avail = w * fw * 0.92
    if est > avail:
        px = max(10, int(avail / (0.55 * max(1, len(str(el.get("text", "")))))))
    return px


class FrameBuilder:
    def __init__(self, fid, kind, w, h, screen, bg):
        self.id, self.kind, self.w, self.h, self.screen, self.bg = fid, kind, w, h, screen, bg
        self.parts, self.model = [], []

    def add(self, name, typ, rect, fill=None, stroke=None, corner=0.0, text=None, font=None, color=None, fpx=0, parent=None, gradient=None, extra=None, state=None, variant=None, value=None):
        l, t, w, h = rect
        px = [round(l * self.w, 2), round(t * self.h, 2), round(w * self.w, 2), round(h * self.h, 2)]
        rad = round(corner * min(px[2], px[3]), 2)
        st = "left:%.4f%%;top:%.4f%%;width:%.4f%%;height:%.4f%%;" % (l * 100, t * 100, w * 100, h * 100)
        if gradient:
            st += "background:linear-gradient(180deg,%s,%s);" % (gradient[0], gradient[1])
        elif fill:
            st += "background-color:%s;" % fill
        if stroke:
            st += "border:%spx solid %s;" % (stroke[0], stroke[1])
        if rad:
            st += "border-radius:%spx;" % rad
        if text is not None:
            fam, wt = C.font_css(font or "BuilderSansBold")
            st += "color:%s;font-size:%dpx;font-weight:%d;font-family:%s;" % (color or "#fff", fpx, wt, fam.replace('"', "'"))
        attrs = ' data-ui="%s" data-type="%s"' % (html.escape(name), typ)
        if parent:
            attrs += ' data-parent="%s"' % html.escape(parent)
        if state:
            attrs += ' data-state="%s"' % state
        if variant:
            attrs += ' data-variant="%s"' % html.escape(variant)
        if text is not None:
            attrs += ' data-text="%s"' % html.escape(str(text), quote=True)
        inner = ""
        if text is not None:
            inner = '<span class="t">%s</span>' % html.escape(str(text))
        if typ == "bar" and value is not None:
            inner = '<i class="fill" style="width:%d%%;background:%s"></i>' % (round(value * 100), extra or "#fff")
        self.parts.append('<div class="el %s"%s style="%s">%s</div>' % (typ, attrs, st, inner))
        self.model.append({
            "name": name, "type": typ, "frame": self.id, "parent": parent, "state": state, "variant": variant,
            "rect": [round(v, 5) for v in (l, t, w, h)], "px": px, "fill": fill if not gradient else None, "gradient": list(gradient) if gradient else None,
            "stroke": {"px": stroke[0], "color": stroke[1]} if stroke else None, "corner": round(corner, 4), "corner_px": rad,
            "text": text, "font": font if text is not None else None, "font_px": fpx if text is not None else None, "color": color if text is not None else None,
        })

    def html(self, extra_cls=""):
        guides = ""
        if self.kind in FRAMES:
            guides += '<div class="guide top" style="height:%dpx"></div>' % TOPBAR_PX
            if self.kind == "phone":
                guides += '<div class="guide stick" style="left:0;bottom:0;width:18%;height:40%"></div><div class="guide stick" style="right:0;bottom:0;width:18%;height:40%"></div>'
        return ('<section class="frame %s" data-id="%s" data-frame="%s" data-screen="%s" style="width:%dpx;height:%dpx;background:%s"><h2 class="cap">%s</h2>%s%s</section>'
                % (extra_cls, html.escape(self.id), self.kind, html.escape(self.screen), self.w, self.h, self.bg, html.escape(self.id), guides, "".join(self.parts)))


def stroke_of(brief, el=None):
    st = brief["style"]
    if el is not None and el.get("stroke") is False:
        return None
    if el is not None and not el.get("stroke") and el.get("type") in ("label", "icon"):
        return None
    return (st.get("stroke", 3), colour(brief, "accent") if "accent" in st["palette"] else "#ffffff")


def draw_element(fb, brief, el, fid):
    fw, fh = FRAMES[fid]
    rect = resolve(el, fid)
    st = brief["style"]
    corner = float(el.get("corner", st.get("corner", 0.18)))
    typ, name = el["type"], el["name"]
    text = el.get("text")
    color = colour(brief, el.get("text_color"), "text")
    fnt = font_name(brief, el.get("font"))
    fpx = font_px(el, fw, fh, fid, rect) if text is not None else 0
    grad = [colour(brief, g) for g in el["gradient"]] if el.get("gradient") else None
    if typ == "panel":
        fb.add(name, typ, rect, fill=colour(brief, el.get("fill"), "panel"), stroke=stroke_of(brief, el) if el.get("stroke") else None, corner=corner, parent=el.get("parent"), gradient=grad)
    elif typ == "label":
        fb.add(name, typ, rect, text=text or "", font=fnt, color=color, fpx=fpx, parent=el.get("parent"))
    elif typ == "button":
        v = variant_of(brief, el)
        fb.add(name, typ, rect, fill=colour(brief, v.get("fill", "accent")), stroke=stroke_of(brief, {"type": "button"}), corner=corner, text=text if text is not None else v.get("text", ""),
               font=fnt, color=colour(brief, v.get("text_color", "bg")), fpx=fpx or font_px({"text": v.get("text", ""), "text_scale": 0.5}, fw, fh, fid, rect), parent=el.get("parent"), state="default", variant=v.get("name"))
    elif typ == "chip":
        fb.add(name, typ, rect, fill=colour(brief, el.get("fill"), "panel"), stroke=stroke_of(brief, {"type": "chip"}), corner=0.5, text=text or "", font=fnt, color=color, fpx=fpx, parent=el.get("parent"))
    elif typ == "bar":
        fb.add(name, typ, rect, fill=colour(brief, "bg"), stroke=stroke_of(brief, {"type": "bar"}), corner=0.5, parent=el.get("parent"), value=float(el.get("value", 0.5)), extra=colour(brief, el.get("fill"), "accent"))
    elif typ == "icon":
        fb.add(name, typ, rect, fill=None, stroke=(2, colour(brief, "text")), corner=0.5, parent=el.get("parent"))
    elif typ == "grid":
        g = el.get("grid") or {"cols": 3, "rows": 1, "gap": 0.02}
        cols, rows, gap = int(g.get("cols", 3)), int(g.get("rows", 1)), float(g.get("gap", 0.02))
        fb.add(name, "panel", rect, fill=None, parent=el.get("parent"))
        x0, y0, w, h = rect
        cw, ch = (w - gap * (cols - 1) * w) / cols, (h - gap * (rows - 1) * h) / rows
        for r in range(rows):
            for c in range(cols):
                cr = (x0 + c * (cw + gap * w), y0 + r * (ch + gap * h), cw, ch)
                fb.add("%sCell%d" % (name, r * cols + c + 1), "panel", cr, fill=colour(brief, "panel"), stroke=stroke_of(brief, {"type": "panel"}), corner=corner, parent=name)


def button_states(brief, v):
    fill, tc = colour(brief, v.get("fill", "accent")), colour(brief, v.get("text_color", "bg"))
    return {"default": (fill, tc, 0), "hover": (C.lighten(fill), tc, 0), "pressed": (C.darken(fill), tc, 2), "disabled": (C.grey(fill), C.grey(tc, 0.6), 0)}


def build_components(brief):
    vs = brief.get("buttons") or [variant_of(brief, {})]
    W = 1100
    rowh, top = 96, 44
    H = top + rowh * (len(vs) + 1) + 20
    fb = FrameBuilder("components", "components", W, H, "components", colour(brief, "bg"))
    st = brief["style"]
    corner = float(st.get("corner", 0.18))
    for i, v in enumerate(vs):
        y = top + i * rowh
        fb.add("Label_" + str(v["name"]), "label", (20 / W, (y + 20) / H, 170 / W, 44 / H), text=str(v["name"]), font=font_name(brief, "body"), color=colour(brief, "text"), fpx=18)
        for j, s in enumerate(STATES):
            fill, tc, off = button_states(brief, v)[s]
            bw, bh = v.get("w", 160), v.get("h", 48)
            x = 220 + j * (bw + 40)
            fb.add("Btn_%s_%s" % (v["name"], s), "button", (x / W, (y + 14 + off) / H, bw / W, bh / H), fill=fill, stroke=(st.get("stroke", 3), colour(brief, "accent") if s != "disabled" else C.grey(colour(brief, "accent"))),
                   corner=corner, text=v.get("text", v["name"]), font=font_name(brief, "body"), color=tc, fpx=max(MIN_TEXT_PX, int(bh * 0.5)), state=s, variant=v["name"])
            fb.add("Cap_%s_%s" % (v["name"], s), "label", (x / W, (y + 14 + bh + 6) / H, bw / W, 18 / H), text=s, font=font_name(brief, "body"), color=colour(brief, "text"), fpx=MIN_TEXT_PX)
    y = top + len(vs) * rowh
    fb.add("Sample_Panel", "panel", (20 / W, (y + 6) / H, 300 / W, 70 / H), fill=colour(brief, "panel"), stroke=(st.get("stroke", 3), colour(brief, "accent")), corner=corner)
    fb.add("Sample_Chip", "chip", (360 / W, (y + 16) / H, 150 / W, 48 / H), fill=colour(brief, "panel"), stroke=(st.get("stroke", 3), colour(brief, "accent")), corner=0.5, text="123", font=font_name(brief, "body"), color=colour(brief, "text"), fpx=20)
    fb.add("Sample_Bar", "bar", (550 / W, (y + 28) / H, 300 / W, 24 / H), fill=colour(brief, "bg"), stroke=(st.get("stroke", 3), colour(brief, "accent")), corner=0.5, value=0.6, extra=colour(brief, "accent"))
    return fb


def build_tokens(brief):
    st = brief["style"]
    pal = st["palette"]
    W = 1100
    H = 340
    fb = FrameBuilder("tokens", "tokens", W, H, "tokens", colour(brief, "bg") if "bg" in pal else "#222222")
    for i, (k, v) in enumerate(pal.items()):
        x = 20 + i * 130
        fb.add("Swatch_" + k, "panel", (x / W, 20 / H, 110 / W, 70 / H), fill=v, stroke=(2, "#ffffff"), corner=0.15)
        fb.add("SwatchName_" + k, "label", (x / W, 94 / H, 110 / W, 22 / H), text="%s %s" % (k, v), font=font_name(brief, "body"), color=colour(brief, "text"), fpx=12)
    y = 130
    for k, f in st["fonts"].items():
        for j, size in enumerate((14, 20, 32)):
            fb.add("Type_%s_%d" % (k, size), "label", ((20 + j * 330) / W, (y) / H, 320 / W, (size + 16) / H), text="%s %s %dpx" % (k, f, size), font=f, color=colour(brief, "text"), fpx=size)
        y += 60
    for i, sp in enumerate(st.get("spacing") or []):
        fb.add("Space_%d" % sp, "panel", ((20 + i * 90) / W, (y + 6) / H, max(sp, 4) / W, 30 / H), fill=colour(brief, "accent") if "accent" in pal else "#ffffff")
        fb.add("SpaceName_%d" % sp, "label", ((20 + i * 90) / W, (y + 40) / H, 80 / W, 20 / H), text="%dpx" % sp, font=font_name(brief, "body"), color=colour(brief, "text"), fpx=12)
    return fb


def build_screens(brief):
    out = []
    pal = brief["style"]["palette"]
    bg = pal.get("bg", "#222222")
    for sc in brief["screens"]:
        for fid in frame_ids(brief):
            fw, fh = FRAMES[fid]
            fb = FrameBuilder("%s.%s" % (sc["name"], fid), fid, fw, fh, sc["name"], bg)
            for el in sc["elements"]:
                draw_element(fb, brief, el, fid)
            out.append(fb)
    return out


CSS = """*{box-sizing:border-box}body{margin:0;padding:16px;background:#101114;color:#ddd;font:14px system-ui,sans-serif}h1{font-size:20px;margin:0 0 4px}p.sub{margin:0 0 16px;color:#999}
.frame{position:relative;overflow:hidden;margin:0 0 28px;outline:1px solid #444}.cap{position:absolute;left:4px;top:-22px;margin:0;font-size:12px;color:#aaa;font-weight:400}
.frame{margin-top:30px}.el{position:absolute;display:flex;align-items:center;justify-content:center;line-height:1;white-space:nowrap;overflow:hidden}
.el.label{justify-content:flex-start}.el .fill{display:block;height:100%}.el.bar{justify-content:flex-start;padding:0}
.guide{position:absolute;pointer-events:none}.guide.top{left:0;top:0;width:100%;background:repeating-linear-gradient(45deg,#00000022,#00000022 6px,#00000044 6px,#00000044 12px)}
.guide.stick{border:2px dashed #ffffff44}
body.only{padding:0;background:#000}body.only .frame{margin:0;outline:none}body.only .cap,body.only h1,body.only p.sub{display:none}"""

JS = """(function(){var q=new URLSearchParams(location.search),only=q.get('frame');
var fs=document.querySelectorAll('.frame');if(only){document.body.classList.add('only');fs.forEach(function(f){if(f.dataset.id!==only)f.style.display='none';});}
function hx(c){var m=/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)(?:,\\s*([\\d.]+))?\\)/.exec(c);if(!m)return null;if(m[4]!==undefined&&parseFloat(m[4])===0)return null;
return '#'+[1,2,3].map(function(i){return ('0'+parseInt(m[i]).toString(16)).slice(-2)}).join('');}
var out={source:'browser',frames:[]};
fs.forEach(function(f){if(f.style.display==='none')return;var fr=f.getBoundingClientRect();var fo={id:f.dataset.id,kind:f.dataset.frame,screen:f.dataset.screen,w:fr.width,h:fr.height,elements:[]};
f.querySelectorAll('[data-ui]').forEach(function(e){var r=e.getBoundingClientRect(),cs=getComputedStyle(e);
fo.elements.push({name:e.dataset.ui,type:e.dataset.type,parent:e.dataset.parent||null,state:e.dataset.state||null,variant:e.dataset.variant||null,
x:r.left-fr.left,y:r.top-fr.top,w:r.width,h:r.height,fill:hx(cs.backgroundColor),stroke_px:parseFloat(cs.borderTopWidth)||0,stroke_color:parseFloat(cs.borderTopWidth)?hx(cs.borderTopColor):null,
corner_px:parseFloat(cs.borderTopLeftRadius)||0,text:e.dataset.text!==undefined?e.dataset.text:null,color:e.dataset.text!==undefined?hx(cs.color):null,
font_px:e.dataset.text!==undefined?parseFloat(cs.fontSize):null,font_family:e.dataset.text!==undefined?cs.fontFamily:null});});out.frames.push(fo);});
var pre=document.createElement('pre');pre.id='ui-spec-out';pre.hidden=true;pre.textContent=JSON.stringify(out);document.body.appendChild(pre);console.log('UISPEC<<'+pre.textContent+'>>UISPEC');})();"""


def build(brief, outdir):
    errs, warns = validate(brief)
    if errs:
        return errs, warns, None
    comps, toks, scr = build_components(brief), build_tokens(brief), build_screens(brief)
    frames = [toks, comps] + scr
    body = ['<h1>UI design sheet: %s</h1><p class="sub">Generated by ui_design.py. Frames are drawn at real pixel size; element names are the Roblox Instance names to build.</p>' % html.escape(str(brief.get("game", "game")))]
    body += [f.html() for f in frames]
    doc = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>UI design sheet</title><meta name="viewport" content="width=device-width,initial-scale=1"><style>%s</style></head><body>\n%s\n<script>%s</script></body></html>\n' % (CSS, "\n".join(body), JS)
    C.write_text(os.path.join(outdir, "index.html"), doc)
    model = model_spec(brief, frames)
    C.write_text(os.path.join(outdir, "spec.model.json"), C.jdump(model))
    C.write_text(os.path.join(outdir, "brief.json"), C.jdump(brief))
    return errs, warns, model


def model_spec(brief, frames):
    st = brief["style"]
    toks = {"palette": st["palette"], "fonts": st["fonts"], "corner": st.get("corner", 0.18), "stroke": st.get("stroke", 3), "spacing": st.get("spacing") or [],
            "buttons": {v["name"]: {s: {"fill": f, "text_color": t, "offset_px": o} for s, (f, t, o) in button_states(brief, v).items()} for v in (brief.get("buttons") or [])}}
    return {"version": 1, "game": brief.get("game", "game"), "source": "model", "tokens": toks,
            "frames": [{"id": f.id, "kind": f.kind, "screen": f.screen, "w": f.w, "h": f.h, "elements": f.model} for f in frames]}


def render(outdir, browser=None, ids=None, timeout=30):
    br = browser or C.find_browser()
    if not br:
        res = {"rendered": [], "browser": None, "note": "no headless Chrome/Edge found: open %s in a browser" % os.path.join(outdir, "index.html")}
        C.write_text(os.path.join(outdir, "render.json"), C.jdump(res))
        return res
    idx = os.path.join(outdir, "index.html")
    model = C.read_json(os.path.join(outdir, "spec.model.json"))
    want = [f for f in model["frames"] if not ids or f["id"] in ids]
    os.makedirs(os.path.join(outdir, "png"), exist_ok=True)
    done, failed = [], []
    for f in want:
        png = os.path.join(outdir, "png", f["id"].replace("/", "_") + ".png")
        if os.path.exists(png):
            os.remove(png)
        w, h = int(f["w"]), int(f["h"])
        try:
            C.run_browser(br, ["--screenshot=" + png, "--window-size=%d,%d" % (w, h), "--virtual-time-budget=2000", C.file_url(idx) + "?frame=" + f["id"]], timeout, wait_file=png)
        except Exception as e:
            failed.append("%s: %s" % (f["id"], type(e).__name__))
            continue
        if os.path.isfile(png) and os.path.getsize(png) > 100:
            crop_png(png, w, h)
            done.append(os.path.relpath(png, outdir).replace("\\", "/"))
        else:
            failed.append("%s: no image written" % f["id"])
    res = {"rendered": done, "failed": failed, "browser": os.path.basename(br)}
    C.write_text(os.path.join(outdir, "render.json"), C.jdump(res))
    return res


def crop_png(path, w, h):
    try:
        iw, ih, ch, rows = C.decode_png(path)
    except Exception:
        return
    if (iw, ih) == (w, h) or iw < w or ih < h:
        return
    rgb = [bytes(r[i] for x in range(w) for i in (x * ch, x * ch + 1, x * ch + 2)) if ch >= 3 else bytes(v for x in range(w) for v in (r[x * ch],) * 3) for r in rows[:h]]
    with open(path, "wb") as f:
        f.write(C.encode_png(w, h, rgb))


def load_brief(p):
    return C.read_json(p)


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd = a[0]

    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else default
    if cmd == "init":
        out = opt("--out")
        if out:
            C.write_text(out, C.jdump(SAMPLE))
            print("wrote " + out)
        else:
            sys.stdout.write(C.jdump(SAMPLE))
        return 0
    if len(a) < 2:
        print("usage: ui_design.py init|validate|build|render|all ...", file=sys.stderr)
        return 2
    if cmd == "validate":
        errs, warns = validate(load_brief(a[1]))
        for e in errs:
            print("ERROR " + e)
        for w in warns:
            print("WARN  " + w)
        print("ui_design validate: %d errors, %d warnings (warnings are advisory)" % (len(errs), len(warns)))
        return 1 if errs else 0
    if cmd in ("build", "all"):
        out = opt("--out") or os.path.join(os.getcwd(), "ui", "design")
        brief = load_brief(a[1])
        errs, warns, model = build(brief, out)
        for e in errs:
            print("ERROR " + e)
        for w in warns:
            print("WARN  " + w)
        if errs:
            return 1
        n = sum(len(f["elements"]) for f in model["frames"])
        print("ui_design: wrote %s (%d frames, %d elements, %d warnings)" % (os.path.join(out, "index.html"), len(model["frames"]), n, len(warns)))
        if cmd == "build":
            return 0
        res = render(out, opt("--browser"), None, int(opt("--timeout", "90")))
        print("ui_design render: %s" % (res.get("note") or "%d png (%s)%s" % (len(res["rendered"]), res["browser"], "; FAILED: " + "; ".join(res["failed"]) if res.get("failed") else "")))
        import ui_spec
        sp = ui_spec.export(os.path.join(out, "index.html"), opt("--browser"), prefer_model=not res.get("browser"))
        C.write_text(os.path.join(out, "spec.json"), C.jdump(sp))
        print("ui_design: spec.json source=%s (%d frames)" % (sp["source"], len(sp["frames"])))
        return 0
    if cmd == "render":
        res = render(a[1], opt("--browser"), opt("--frames").split(",") if opt("--frames") else None, int(opt("--timeout", "90")))
        print("ui_design render: " + (res.get("note") or "%d png (%s)" % (len(res["rendered"]), res["browser"])))
        for f in res.get("failed") or []:
            print("  FAILED " + f)
        return 0
    print("unknown command " + cmd, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
