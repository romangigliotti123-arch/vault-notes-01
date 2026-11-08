#!/usr/bin/env python3
"""thumb_compose.py: compose a Roblox thumbnail (1920x1080) and icon (512x512) from supplied image layers, with outline, glow, big short text,
safe-zone guides and a downscale-legibility strip. Part of rbx-thumbnail. Pillow (PIL) does the pixels; without Pillow it writes an SVG composite only.
No network, no API key, never uploads. Input layers are YOUR OWN files (a transparent PNG cut-out of your character, your screenshot, your art):
never a real person's photo, another game's art, or a copied thumbnail (see references/roblox-mapping.md).

  thumb_compose.py templates                         list the composition templates and their roles
  thumb_compose.py compose SPEC.json --out DIR [--jpg]
        writes thumbnail-1920x1080.png, icon-512.png, guides-thumbnail.png, guides-icon.png, strip-thumbnail.png, strip-icon.png, report.json
        and prints PASS/WARN lines plus `SUMMARY: N PASS, M WARN` (exit 0; exit 2 on bad input)
  thumb_compose.py strip IMAGE --out strip.png [--widths 100,200,400]
        true-size downscales of any image in colour and in greyscale (use it on every candidate, also AI-made ones)
  thumb_compose.py demo --out DIR                    draws original sample layers and composes three concepts (A/B/C), a contact sheet and the reports

SPEC.json (every path relative to the spec file; fractions are of the canvas):
 {"name": "lava-climb", "template": "face-left-prize-right",
  "background": {"gradient": ["#ff9a3c", "#7b2cbf"], "angle": 100} | {"color": "#222"} | {"file": "bg.png"},   optional "burst": {"color": "#ffffff", "alpha": 40, "cx": 0.3, "cy": 0.4, "rays": 18}
  "layers": [{"file": "hero.png", "role": "hero", "outline": {"px": 14, "color": "#111"}, "glow": {"px": 40, "color": "#ffe600"}, "shadow": true,
              "cx": 0.28, "cy": 0.55, "h": 0.95, "flip": false, "rotate": 0, "opacity": 1.0, "box": [x0, y0, x1, y1]}, ...],   cx/cy/h/box override the template; roles: hero hero2 prize extra scene scene2
  "texts": [{"text": "DAY 6", "slot": "tr", "size": 0.17, "fill": "#ffffff", "stroke": "#000000", "stroke_frac": 0.09, "rotate": -3}],
  "icon_layers": [...optional, same form: otherwise the thumbnail layers are re-laid-out with the template's icon positions],
  "icon_texts": [...optional, none by default]}
Thresholds printed as WARN are assumptions from references/text-colour-cheatsheet.md, not Roblox rules; the Roblox spec comes from the live check.
"""
import argparse
import base64
import colorsys
import json
import math
import os
import struct
import sys

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont
    HAVE_PIL = True
except Exception:  # pragma: no cover
    HAVE_PIL = False

TW, TH, IS = 1920, 1080, 512
BOTTOM_ZONE = 0.15
MAX_BYTES = 3 * 1024 * 1024
STRIP_THUMB = [100, 200, 400]
STRIP_ICON = [64, 100, 150]

# role -> ("c", cx, cy, h) centre and height fractions, or ("box", x0, y0, x1, y1) cover-fit boxes. Thumbnail then icon.
TEMPLATES = {
    "face-left-prize-right": {
        "desc": "hero close-up on the left third looking toward a prize/scene filling the right; most character games",
        "thumbnail": {"hero": ("c", 0.27, 0.56, 1.02), "prize": ("c", 0.72, 0.52, 0.80), "extra": ("c", 0.50, 0.85, 0.30), "scene": ("box", 0, 0.70, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"hero": ("c", 0.5, 0.58, 0.96), "prize": ("c", 0.80, 0.30, 0.42), "extra": ("c", 0.18, 0.80, 0.25), "scene": ("box", 0, 0.78, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tr", "icon": "tr"}},
    "tiny-hero-huge-scene": {
        "desc": "small hero in the lower third, giant tower/boss/map fills the frame: scale and danger",
        "thumbnail": {"prize": ("c", 0.60, 0.50, 1.00), "hero": ("c", 0.60, 0.20, 0.26), "extra": ("c", 0.15, 0.55, 0.50), "scene": ("box", 0, 0.76, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"prize": ("c", 0.5, 0.52, 0.95), "hero": ("c", 0.5, 0.22, 0.32), "extra": ("c", 0.15, 0.55, 0.40), "scene": ("box", 0, 0.82, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tr", "icon": "tr"}},
    "versus-duel": {
        "desc": "hero and rival at the edges, equal size, prize between: PvP, race, boss",
        "thumbnail": {"hero": ("c", 0.22, 0.58, 0.98), "hero2": ("c", 0.78, 0.58, 0.98), "prize": ("c", 0.50, 0.55, 0.45), "scene": ("box", 0, 0.78, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"hero": ("c", 0.27, 0.58, 0.85), "hero2": ("c", 0.73, 0.58, 0.85), "prize": ("c", 0.50, 0.30, 0.34), "scene": ("box", 0, 0.82, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tc", "icon": "tc"}},
    "before-after-split": {
        "desc": "two halves, same pose, thin divider: progression, pets, bases, skins, updates",
        "thumbnail": {"scene": ("box", 0, 0, 0.5, 1), "scene2": ("box", 0.5, 0, 1, 1), "hero": ("c", 0.25, 0.58, 0.92), "hero2": ("c", 0.75, 0.58, 0.92), "prize": ("c", 0.5, 0.5, 0.0)},
        "icon": {"scene": ("box", 0, 0, 0.5, 1), "scene2": ("box", 0.5, 0, 1, 1), "hero": ("c", 0.25, 0.58, 0.80), "hero2": ("c", 0.75, 0.58, 0.80), "prize": ("c", 0.5, 0.5, 0.0)},
        "text": {"thumbnail": "tc", "icon": "tc"}},
    "object-only": {
        "desc": "one giant prize or button centred on a flat colour with glow; the strongest icon type for a single reward",
        "thumbnail": {"prize": ("c", 0.5, 0.52, 0.86), "hero": ("c", 0.14, 0.64, 0.50), "extra": ("c", 0.86, 0.64, 0.42), "scene": ("box", 0, 0.8, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"prize": ("c", 0.5, 0.52, 0.88), "hero": ("c", 0.18, 0.78, 0.36), "extra": ("c", 0.82, 0.78, 0.30), "scene": ("box", 0, 0.82, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tr", "icon": "tr"}},
    "crowd-in-shape": {
        "desc": "many small characters packed in one bold shape (ring, box) with the hero at the edge: last-to-leave, events",
        "thumbnail": {"prize": ("c", 0.64, 0.54, 0.92), "hero": ("c", 0.16, 0.58, 0.96), "extra": ("c", 0.50, 0.50, 0.40), "scene": ("box", 0, 0.8, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"prize": ("c", 0.5, 0.40, 0.70), "hero": ("c", 0.5, 0.78, 0.70), "extra": ("c", 0.5, 0.5, 0.30), "scene": ("box", 0, 0.82, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tr", "icon": "tr"}},
    "pile-and-hero": {
        "desc": "hero partly buried in a huge pile of currency, pets or items: collectors, simulators",
        "thumbnail": {"hero": ("c", 0.50, 0.46, 0.90), "prize": ("c", 0.50, 0.90, 0.46), "extra": ("c", 0.12, 0.70, 0.36), "scene": ("box", 0, 0.62, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"hero": ("c", 0.5, 0.44, 0.84), "prize": ("c", 0.5, 0.90, 0.42), "extra": ("c", 0.15, 0.72, 0.28), "scene": ("box", 0, 0.7, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tr", "icon": "tr"}},
    "reach-to-camera": {
        "desc": "a hand, claw or tool reaching toward the viewer, prize behind: action, scarcity, sports",
        "thumbnail": {"hero": ("c", 0.62, 0.60, 1.0), "prize": ("c", 0.22, 0.45, 0.60), "extra": ("c", 0.85, 0.20, 0.30), "scene": ("box", 0, 0.8, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"hero": ("c", 0.6, 0.62, 0.95), "prize": ("c", 0.25, 0.30, 0.45), "extra": ("c", 0.85, 0.2, 0.25), "scene": ("box", 0, 0.82, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tl", "icon": "tl"}},
    "color-isolation": {
        "desc": "scene in one limited palette (or grey), the hero or prize the single saturated element: horror, mystery, crowded genres",
        "thumbnail": {"hero": ("c", 0.5, 0.58, 0.96), "prize": ("c", 0.80, 0.55, 0.60), "extra": ("c", 0.15, 0.55, 0.50), "scene": ("box", 0, 0.8, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"hero": ("c", 0.5, 0.58, 0.96), "prize": ("c", 0.8, 0.3, 0.40), "extra": ("c", 0.2, 0.3, 0.30), "scene": ("box", 0, 0.82, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tc", "icon": "tc"}},
    "vanishing-line": {
        "desc": "a row of identical enemies/cars/props converging on a point, hero in the foreground: chase, waves, tower defence",
        "thumbnail": {"hero": ("c", 0.22, 0.56, 1.0), "prize": ("c", 0.72, 0.50, 0.74), "extra": ("c", 0.85, 0.25, 0.30), "scene": ("box", 0, 0.78, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "icon": {"hero": ("c", 0.28, 0.60, 0.92), "prize": ("c", 0.75, 0.40, 0.55), "extra": ("c", 0.85, 0.2, 0.25), "scene": ("box", 0, 0.82, 1, 1.0), "scene2": ("box", 0, 0, 1, 1)},
        "text": {"thumbnail": "tr", "icon": "tr"}},
}
SLOTS = {"tr": ("r", 0.965, 0.045), "tl": ("l", 0.035, 0.045), "tc": ("c", 0.5, 0.045), "c": ("c", 0.5, 0.42)}
ICON_SLOTS = {"tr": ("r", 0.92, 0.07), "tl": ("l", 0.08, 0.07), "tc": ("c", 0.5, 0.07), "c": ("c", 0.5, 0.40)}
FONTS = ["C:/Windows/Fonts/impact.ttf", "C:/Windows/Fonts/ariblk.ttf", "C:/Windows/Fonts/arialbd.ttf",
         "/System/Library/Fonts/Supplemental/Impact.ttf", "/System/Library/Fonts/Supplemental/Arial Black.ttf", "/System/Library/Fonts/Helvetica.ttc",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"]

RES = None
if HAVE_PIL:
    RES = getattr(getattr(Image, "Resampling", Image), "LANCZOS")


def die(msg, code=2):
    print("ERROR: " + msg)
    sys.exit(code)


def hexrgb(c, default=(255, 255, 255)):
    if not c:
        return default
    c = c.lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    try:
        return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))
    except Exception:
        die("bad colour %r (use #rrggbb)" % c)


def lum(rgb):
    def ch(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb[:3]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def get_font(size, path=None):
    for p in ([path] if path else []) + FONTS:
        if p and os.path.exists(p):
            try:
                return ImageFont.truetype(p, int(size))
            except Exception:
                pass
    try:
        return ImageFont.load_default(int(size))
    except Exception:
        return ImageFont.load_default()


# ---------- pixel helpers ----------
def gradient(w, h, colours, angle):
    cols = [hexrgb(c) for c in colours] if colours else [(40, 40, 60), (10, 10, 20)]
    if len(cols) == 1:
        cols = cols * 2
    a = math.radians(angle)
    dx, dy = math.cos(a), math.sin(a)
    # build a 1-D ramp then map by projected position, at reduced size for speed
    sw, sh = max(w // 4, 2), max(h // 4, 2)
    img = Image.new("RGB", (sw, sh))
    px = img.load()
    ext = abs(dx) * sw + abs(dy) * sh
    for y in range(sh):
        for x in range(sw):
            t = ((x - sw / 2) * dx + (y - sh / 2) * dy) / ext + 0.5
            t = min(max(t, 0.0), 1.0) * (len(cols) - 1)
            i = min(int(t), len(cols) - 2)
            f = t - i
            px[x, y] = tuple(int(cols[i][k] * (1 - f) + cols[i + 1][k] * f) for k in range(3))
    return img.resize((w, h), RES)


def cover(img, w, h):
    iw, ih = img.size
    s = max(w / iw, h / ih)
    nw, nh = max(int(iw * s + 0.5), 1), max(int(ih * s + 0.5), 1)
    img = img.resize((nw, nh), RES)
    x, y = (nw - w) // 2, (nh - h) // 2
    return img.crop((x, y, x + w, y + h))


def dilate(alpha, px):
    px = int(px)
    for _ in range(max(px, 0)):
        alpha = alpha.filter(ImageFilter.MaxFilter(3))
    if px > 0:
        alpha = alpha.filter(ImageFilter.GaussianBlur(max(px / 10.0, 0.6))).point(lambda v: 255 if v > 110 else int(v * 2.2))
    return alpha


def tint(alpha, rgb):
    out = Image.new("RGBA", alpha.size, rgb + (0,))
    out.putalpha(alpha)
    return out


def paste_rgba(base, layer, xy):
    """alpha-composite layer onto the RGBA base at xy, clipping to the base"""
    x, y = xy
    bw, bh = base.size
    lw, lh = layer.size
    sx, sy = max(0, -x), max(0, -y)
    ex, ey = min(lw, bw - x), min(lh, bh - y)
    if ex <= sx or ey <= sy:
        return
    part = layer.crop((sx, sy, ex, ey))
    region = base.crop((x + sx, y + sy, x + ex, y + ey))
    base.paste(Image.alpha_composite(region, part), (x + sx, y + sy))


def add_burst(base, spec, W, H):
    if not spec:
        return
    cx, cy = spec.get("cx", 0.3) * W, spec.get("cy", 0.4) * H
    rays = int(spec.get("rays", 16))
    col = hexrgb(spec.get("color"), (255, 255, 255))
    alpha = int(spec.get("alpha", 40))
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    R = math.hypot(W, H) * 1.2
    step = 2 * math.pi / rays
    for i in range(rays):
        a0 = i * step
        a1 = a0 + step / 2
        d.polygon([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))], fill=col + (alpha,))
    base.alpha_composite(ov)


def vignette(base, strength=0.35):
    W, H = base.size
    mask = Image.radial_gradient("L").resize((W, H), RES)  # 0 centre -> 255 edge
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    dark.putalpha(mask.point(lambda v: int(max(0, v - 90) * strength * 1.6)))
    base.alpha_composite(dark)


def make_background(spec, W, H, base_dir):
    bg = (spec or {}).get("background") or {}
    if bg.get("file"):
        p = os.path.join(base_dir, bg["file"])
        if not os.path.exists(p):
            die("background file not found: " + p)
        im = cover(Image.open(p).convert("RGB"), W, H)
    elif bg.get("gradient"):
        im = gradient(W, H, bg["gradient"], bg.get("angle", 90))
    else:
        im = Image.new("RGB", (W, H), hexrgb(bg.get("color"), (30, 30, 46)))
    im = im.convert("RGBA")
    add_burst(im, (spec or {}).get("burst"), W, H)
    if (spec or {}).get("vignette", True):
        vignette(im)
    return im


def load_layer(path):
    if not os.path.exists(path):
        die("layer file not found: " + path)
    return Image.open(path).convert("RGBA")


def place_layer(canvas, layer_spec, role_layout, base_dir, W, H, scale_px):
    """returns (bbox, hero_mask_info) and draws the layer onto canvas"""
    im = load_layer(os.path.join(base_dir, layer_spec["file"]))
    if layer_spec.get("flip"):
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if layer_spec.get("rotate"):
        im = im.rotate(layer_spec["rotate"], expand=True, resample=Image.BICUBIC)
    box = layer_spec.get("box") or (role_layout if role_layout and role_layout[0] == "box" else None)
    if box and box[0] == "box":
        box = box[1:]
    if box:
        x0, y0, x1, y1 = int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)
        im = cover(im, max(x1 - x0, 1), max(y1 - y0, 1))
        pos = (x0, y0)
    else:
        if role_layout and role_layout[0] == "c":
            cx, cy, h = role_layout[1:]
        else:
            cx, cy, h = 0.5, 0.5, 0.8
        cx, cy, h = layer_spec.get("cx", cx), layer_spec.get("cy", cy), layer_spec.get("h", h)
        if h <= 0:
            return None
        th = max(int(h * H), 2)
        tw = max(int(im.width * th / im.height), 2)
        if tw > W * 0.98:
            tw = int(W * 0.98)
            th = max(int(im.height * tw / im.width), 2)
        im = im.resize((tw, th), RES)
        pos = (int(cx * W - tw / 2), int(cy * H - th / 2))
    if layer_spec.get("opacity", 1.0) < 1.0:
        a = im.getchannel("A").point(lambda v: int(v * layer_spec["opacity"]))
        im.putalpha(a)
    alpha = im.getchannel("A")
    pad = int(max((layer_spec.get("glow") or {}).get("px", 0), (layer_spec.get("outline") or {}).get("px", 0)) * scale_px * 2 + 8)
    big = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    big.paste(im, (pad, pad))
    balpha = big.getchannel("A")
    stack = Image.new("RGBA", big.size, (0, 0, 0, 0))
    if layer_spec.get("shadow"):
        sh = tint(balpha.filter(ImageFilter.GaussianBlur(max(H * 0.012, 2))).point(lambda v: int(v * 0.55)), (0, 0, 0))
        off = int(H * 0.012)
        tmp = Image.new("RGBA", big.size, (0, 0, 0, 0))
        tmp.paste(sh, (off, off))
        stack.alpha_composite(tmp)
    g = layer_spec.get("glow")
    if g:
        gpx = max(int(g.get("px", 30) * scale_px), 2)
        ga = dilate(balpha, max(gpx // 6, 1)).filter(ImageFilter.GaussianBlur(gpx / 2.0)).point(lambda v: min(255, int(v * g.get("strength", 1.6))))
        stack.alpha_composite(tint(ga, hexrgb(g.get("color"), (255, 230, 0))))
    o = layer_spec.get("outline")
    if o:
        opx = max(int(o.get("px", 10) * scale_px), 1)
        stack.alpha_composite(tint(dilate(balpha, opx), hexrgb(o.get("color"), (0, 0, 0))))
    stack.alpha_composite(big)
    paste_rgba(canvas, stack, (pos[0] - pad, pos[1] - pad))
    bbox = (pos[0], pos[1], pos[0] + im.width, pos[1] + im.height)
    return {"bbox": bbox, "alpha": alpha, "pos": pos, "img": im}


def draw_text(canvas, t, W, H, slots, font_path, scale):
    text = str(t.get("text", "")).strip()
    if not text:
        return None
    size = max(int(t.get("size", 0.17) * H), 8)
    sfrac = t.get("stroke_frac", 0.09)
    fill, stroke = hexrgb(t.get("fill"), (255, 255, 255)), hexrgb(t.get("stroke"), (0, 0, 0))
    maxw = t.get("max_width", 0.55) * W
    anchor, sx, sy = (t["x_anchor"], t["x"], t["y"]) if "x" in t else slots.get(t.get("slot", "tr"), slots["tr"])
    while True:
        font = get_font(size, t.get("font") or font_path)
        sw = max(int(size * sfrac), 1)
        d = ImageDraw.Draw(Image.new("RGBA", (4, 4)))
        bb = d.textbbox((0, 0), text, font=font, stroke_width=sw)
        if bb[2] - bb[0] <= maxw or size <= 12:
            break
        size = int(size * 0.92)
    pad = sw * 2 + int(size * 0.1)
    lay = Image.new("RGBA", (bb[2] - bb[0] + 2 * pad, bb[3] - bb[1] + 2 * pad), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ld.text((pad - bb[0], pad - bb[1]), text, font=font, fill=fill + (255,), stroke_width=sw, stroke_fill=stroke + (255,))
    if t.get("shadow", True):
        sh = tint(lay.getchannel("A").filter(ImageFilter.GaussianBlur(max(size * 0.04, 1))).point(lambda v: int(v * 0.6)), (0, 0, 0))
        base = Image.new("RGBA", lay.size, (0, 0, 0, 0))
        o = max(int(size * 0.04), 2)
        base.paste(sh, (o, o))
        base.alpha_composite(lay)
        lay = base
    if t.get("rotate"):
        lay = lay.rotate(t["rotate"], expand=True, resample=Image.BICUBIC)
    lw, lh = lay.size
    x = int(sx * W - (lw if anchor == "r" else lw / 2 if anchor == "c" else 0))
    y = int(sy * H)
    x = min(max(x, 0), W - lw)
    y = min(max(y, 0), H - lh)
    pre = canvas.convert("RGB").crop((x, y, x + lw, y + lh))
    bgmean = tuple(int(v) for v in ImageStat_mean(pre))
    paste_rgba(canvas, lay, (x, y))
    glyph_h = size * 0.72  # approximate cap height
    return {"text": text, "bbox": (x, y, x + lw, y + lh), "size_px": size, "cap_px": glyph_h, "fill": fill, "stroke": stroke, "bg_mean": bgmean,
            "contrast_fill_stroke": round(contrast(fill, stroke), 2), "contrast_fill_bg": round(contrast(fill, bgmean), 2), "words": len(text.split())}


def _pix(img):
    return list(img.get_flattened_data()) if hasattr(img, "get_flattened_data") else list(img.getdata())


def ImageStat_mean(img):
    small = img.resize((8, 8), RES)
    px = _pix(small)
    n = len(px)
    return tuple(sum(p[i] for p in px) / n for i in range(3))


def compose_one(spec, base_dir, kind, font_path):
    W, H = (TW, TH) if kind == "thumbnail" else (IS, IS)
    scale_px = H / 1080.0
    tmpl = TEMPLATES.get(spec.get("template") or "face-left-prize-right")
    if tmpl is None:
        die("unknown template %r (run: thumb_compose.py templates)" % spec.get("template"))
    layout = tmpl[kind]
    canvas = make_background(spec, W, H, base_dir)
    layers = spec.get("icon_layers") if kind == "icon" and spec.get("icon_layers") else spec.get("layers", [])
    infos, hero_contrast, hero_count = [], None, 0
    for ls in layers:
        role = ls.get("role", "extra")
        if not ls.get("file"):
            die("each layer needs a file")
        if kind == "icon" and not spec.get("icon_layers") and ls.get("icon") is False:
            continue
        ls = dict(ls)
        if kind == "icon" and not spec.get("icon_layers"):
            ls.pop("cx", None); ls.pop("cy", None); ls.pop("h", None); ls.pop("box", None)
        want = role == "hero" or (role == "prize" and not any(l.get("role") == "hero" and not (kind == "icon" and l.get("icon") is False) for l in layers))
        pre = canvas.copy() if want else None
        info = place_layer(canvas, ls, layout.get(role), base_dir, W, H, scale_px)
        if info is None:
            continue
        info["role"] = role
        infos.append(info)
        if want and pre is not None and hero_contrast is None:
            full = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            paste_rgba(full, info["img"], info["pos"])
            hero_contrast = hero_value_contrast(full, full.getchannel("A"), pre)
        if role in ("hero", "hero2", "prize", "extra"):
            hero_count += 1
    texts_spec = spec.get("texts", []) if kind == "thumbnail" else spec.get("icon_texts", [])
    slots = SLOTS if kind == "thumbnail" else ICON_SLOTS
    tinfos = []
    for t in texts_spec:
        r = draw_text(canvas, t, W, H, slots, font_path, scale_px)
        if r:
            tinfos.append(r)
    return canvas.convert("RGB"), {"kind": kind, "size": [W, H], "layers": infos, "texts": tinfos, "hero_value_contrast": hero_contrast, "elements": hero_count}


def hero_value_contrast(hero_rgba, mask, behind_rgba):
    """absolute difference of mean luminance (0..1) between hero pixels and the background behind them"""
    hp, bp, mp = hero_rgba.convert("RGB").resize((48, 27), RES), behind_rgba.convert("RGB").resize((48, 27), RES), mask.resize((48, 27), RES)
    num_h = num_b = den = 0.0
    for (h, b, m) in zip(_pix(hp), _pix(bp), _pix(mp)):
        w = m / 255.0
        num_h += w * lum(h)
        num_b += w * lum(b)
        den += w
    if den <= 0:
        return None
    return round(abs(num_h - num_b) / den, 3)


# ---------- guides and strip ----------
def guides(img, kind, info):
    W, H = img.size
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    f = get_font(max(H // 45, 11))
    if kind == "thumbnail":
        d.rectangle((0, int(H * (1 - BOTTOM_ZONE)), W, H), fill=(255, 40, 40, 90))
        d.text((12, int(H * (1 - BOTTOM_ZONE)) + 8), "bottom 15%: player-count area may cover this", fill=(255, 255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 255))
        m = int(W * 0.04)
        d.rectangle((m, int(H * 0.04), W - m, int(H * (1 - BOTTOM_ZONE))), outline=(0, 255, 255, 230), width=3)
        for k in (1, 2):
            d.line((W * k // 3, 0, W * k // 3, H), fill=(255, 255, 0, 150), width=2)
            d.line((0, H * k // 3, W, H * k // 3), fill=(255, 255, 0, 150), width=2)
    else:
        m = int(W * 0.08)
        d.rectangle((m, m, W - m, H - m), outline=(0, 255, 255, 230), width=3)
        d.rounded_rectangle((0, 0, W - 1, H - 1), radius=int(W * 0.12), outline=(255, 40, 40, 230), width=4)
        d.line((W // 2, 0, W // 2, H), fill=(255, 255, 0, 120), width=1)
        d.line((0, H // 2, W, H // 2), fill=(255, 255, 0, 120), width=1)
        d.text((m + 4, m + 2), "icon: keep detail inside", fill=(255, 255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 255))
    for t in info.get("texts", []):
        d.rectangle(t["bbox"], outline=(255, 0, 255, 255), width=3)
    for l in info.get("layers", []):
        if l["role"] in ("hero", "hero2"):
            d.rectangle(l["bbox"], outline=(0, 255, 0, 200), width=2)
    out = img.convert("RGBA")
    out.alpha_composite(ov)
    return out.convert("RGB")


def strip(img, widths, label=None):
    W, H = img.size
    gap, cap = 24, 26
    sizes = []
    for w in widths:
        w = min(w, W)
        sizes.append((w, max(int(H * w / W), 1)))
    tw = sum(s[0] for s in sizes) + gap * (len(sizes) + 1)
    th = cap + 2 * max(s[1] for s in sizes) + cap + gap * 3
    out = Image.new("RGB", (max(tw, 300), th), (48, 48, 54))
    d = ImageDraw.Draw(out)
    f = get_font(14)
    x = gap
    y1 = cap + gap // 2
    y2 = y1 + max(s[1] for s in sizes) + cap + gap // 2
    d.text((gap, 4), (label or "true size, colour (top) and greyscale (bottom)"), fill=(230, 230, 230), font=f)
    for (w, h) in sizes:
        small = img.resize((w, h), RES).convert("RGB")
        out.paste(small, (x, y1))
        out.paste(small.convert("L").convert("RGB"), (x, y2))
        d.text((x, y1 - 18 + 2), "%d px" % w, fill=(255, 220, 120), font=f)
        x += w + gap
    return out


# ---------- checks ----------
def checks(info_thumb, info_icon, files):
    res = []

    def ck(level, msg):
        res.append((level, msg))
    for info in (info_thumb, info_icon):
        kind, (W, H) = info["kind"], info["size"]
        pre = kind
        ck("PASS" if info["elements"] <= 3 else "WARN", "%s: %d subject elements (hero/prize/extra; 1-3 reads best, assumption)" % (pre, info["elements"]))
        hc = info["hero_value_contrast"]
        if hc is None:
            ck("WARN", "%s: no hero or prize layer, so value contrast was not measured" % pre)
        else:
            ck("PASS" if hc >= 0.18 else "WARN", "%s: main subject (hero, else prize) vs background luminance difference %.2f (>= 0.18 wanted, assumption; check the greyscale row)" % (pre, hc))
        big = max([(l["bbox"][3] - l["bbox"][1]) / H for l in info["layers"] if l["role"] in ("hero", "hero2", "prize")] or [0])
        ck("PASS" if big >= 0.35 else "WARN", "%s: biggest subject is %.0f%% of the frame height (>= 35%% wanted, assumption)" % (pre, big * 100))
        limit = 3 if kind == "thumbnail" else 1
        for t in info["texts"]:
            ck("PASS" if t["words"] <= limit else "WARN", "%s: text %r has %d word(s) (max %d, assumption)" % (pre, t["text"], t["words"], limit))
            px100 = t["cap_px"] * (100.0 / W)
            ck("PASS" if px100 >= 8 else "WARN", "%s: text %r is about %.1f px tall at 100 px width (>= 8 wanted, assumption)" % (pre, t["text"], px100))
            c = max(t["contrast_fill_stroke"], t["contrast_fill_bg"])
            ck("PASS" if c >= 3 else "WARN", "%s: text %r contrast %.1f:1 (fill vs outline %.1f, vs background %.1f; >= 3 wanted)" % (pre, t["text"], c, t["contrast_fill_stroke"], t["contrast_fill_bg"]))
            if kind == "thumbnail":
                ck("PASS" if t["bbox"][3] <= H * (1 - BOTTOM_ZONE) else "WARN", "%s: text %r stays above the bottom 15%% player-count area" % (pre, t["text"]))
            m = 0.04 * W
            ck("PASS" if t["bbox"][0] >= m * 0.5 and t["bbox"][2] <= W - m * 0.5 else "WARN", "%s: text %r keeps a margin from the sides" % (pre, t["text"]))
    for name, size in files.items():
        if name.startswith("thumbnail"):
            ck("PASS" if size <= MAX_BYTES else "WARN", "%s is %.2f MB (Roblox thumbnail limit is under 3 MB; use --jpg or re-export)" % (name, size / 1048576.0))
    return res


def write_svg(spec, base_dir, outdir):
    """fallback without Pillow: an SVG composite; no strips, no checks"""
    def png_size(p):
        with open(p, "rb") as fh:
            h = fh.read(24)
        return struct.unpack(">II", h[16:24]) if h[:8] == b"\x89PNG\r\n\x1a\n" else (1000, 1000)
    bg = (spec.get("background") or {})
    stops = bg.get("gradient") or [bg.get("color", "#1e1e2e")] * 2
    tmpl = TEMPLATES.get(spec.get("template") or "face-left-prize-right")
    for kind, (W, H) in (("thumbnail", (TW, TH)), ("icon", (IS, IS))):
        parts = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="%d" height="%d" viewBox="0 0 %d %d">' % (W, H, W, H),
                 '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (stops[0], stops[-1]),
                 '<rect width="100%" height="100%" fill="url(#g)"/>']
        for ls in spec.get("layers", []):
            lay = tmpl[kind].get(ls.get("role", "extra"))
            if not lay or lay[0] != "c":
                continue
            cx, cy, h = ls.get("cx", lay[1]), ls.get("cy", lay[2]), ls.get("h", lay[3])
            p = os.path.join(base_dir, ls["file"])
            iw, ih = png_size(p)
            th = h * H
            tw = iw * th / ih
            data = base64.b64encode(open(p, "rb").read()).decode()
            parts.append('<image x="%d" y="%d" width="%d" height="%d" href="data:image/png;base64,%s"/>' % (cx * W - tw / 2, cy * H - th / 2, tw, th, data))
        for t in (spec.get("texts", []) if kind == "thumbnail" else spec.get("icon_texts", [])):
            anchor, sx, sy = SLOTS.get(t.get("slot", "tr"), SLOTS["tr"]) if kind == "thumbnail" else ICON_SLOTS.get(t.get("slot", "tr"), ICON_SLOTS["tr"])
            size = t.get("size", 0.17) * H
            ta = {"r": "end", "l": "start", "c": "middle"}[anchor]
            parts.append('<text x="%d" y="%d" font-family="Impact, Arial Black, sans-serif" font-weight="900" font-size="%d" text-anchor="%s" fill="%s" stroke="%s" stroke-width="%d" paint-order="stroke" stroke-linejoin="round">%s</text>'
                         % (sx * W, sy * H + size * 0.85, size, ta, t.get("fill", "#fff"), t.get("stroke", "#000"), size * 0.12, t.get("text", "")))
        parts.append("</svg>")
        open(os.path.join(outdir, "thumbnail.svg" if kind == "thumbnail" else "icon.svg"), "w", encoding="utf8").write("\n".join(parts))


# ---------- commands ----------
def cmd_templates(_a):
    for name, t in TEMPLATES.items():
        print("%-24s %s" % (name, t["desc"]))
        print("%-24s roles: %s" % ("", ", ".join(sorted(t["thumbnail"].keys()))))
    print("\ntext slots: " + ", ".join(sorted(SLOTS)))


def cmd_compose(a):
    spec_path = os.path.abspath(a.spec)
    if not os.path.exists(spec_path):
        die("spec not found: " + spec_path)
    spec = json.load(open(spec_path, encoding="utf8"))
    base_dir = os.path.dirname(spec_path)
    outdir = os.path.abspath(a.out)
    os.makedirs(outdir, exist_ok=True)
    if not HAVE_PIL:
        write_svg(spec, base_dir, outdir)
        print("WARN Pillow is not installed: wrote thumbnail.svg and icon.svg only (no PNG, strips or checks). Install it with: pip install pillow")
        print("SUMMARY: 0 PASS, 1 WARN")
        return 0
    thumb, ti = compose_one(spec, base_dir, "thumbnail", a.font)
    icon, ii = compose_one(spec, base_dir, "icon", a.font)
    files = {}
    p = os.path.join(outdir, "thumbnail-1920x1080.png")
    thumb.save(p, optimize=True)
    files["thumbnail-1920x1080.png"] = os.path.getsize(p)
    if a.jpg or files["thumbnail-1920x1080.png"] > MAX_BYTES:
        thumb.save(os.path.join(outdir, "thumbnail-1920x1080.jpg"), quality=92, optimize=True)
    icon.save(os.path.join(outdir, "icon-512.png"), optimize=True)
    guides(thumb, "thumbnail", ti).save(os.path.join(outdir, "guides-thumbnail.png"))
    guides(icon, "icon", ii).save(os.path.join(outdir, "guides-icon.png"))
    strip(thumb, STRIP_THUMB).save(os.path.join(outdir, "strip-thumbnail.png"))
    strip(icon, STRIP_ICON).save(os.path.join(outdir, "strip-icon.png"))
    res = checks(ti, ii, files)
    for lv, msg in res:
        print("%s %s" % (lv, msg))
    npass, nwarn = sum(1 for r in res if r[0] == "PASS"), sum(1 for r in res if r[0] == "WARN")
    rep = {"name": spec.get("name"), "template": spec.get("template"), "results": [{"level": l, "message": m} for l, m in res],
           "thumbnail": {k: v for k, v in ti.items() if k not in ("layers",)}, "icon": {k: v for k, v in ii.items() if k not in ("layers",)}, "files": files}
    json.dump(rep, open(os.path.join(outdir, "report.json"), "w", encoding="utf8"), indent=1, default=str)
    print("wrote %s" % outdir)
    print("SUMMARY: %d PASS, %d WARN" % (npass, nwarn))
    return 0


def cmd_strip(a):
    if not HAVE_PIL:
        die("strip needs Pillow (pip install pillow)")
    if not os.path.exists(a.image):
        die("image not found: " + a.image)
    img = Image.open(a.image).convert("RGB")
    widths = [int(x) for x in a.widths.split(",")] if a.widths else (STRIP_ICON if abs(img.width - img.height) < 4 else STRIP_THUMB)
    out = strip(img, widths)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    out.save(a.out)
    print("wrote %s (%s px wide, true size, colour and greyscale)" % (a.out, "/".join(str(w) for w in widths)))
    return 0


def cmd_demo(a):
    if not HAVE_PIL:
        die("demo needs Pillow (pip install pillow)")
    import importlib.util
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thumb_demo.py")
    spec = importlib.util.spec_from_file_location("thumb_demo", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.run(a.out, sys.modules[__name__])


def main(argv):
    ap = argparse.ArgumentParser(description="compose Roblox thumbnails and icons, with legibility strips (rbx-thumbnail)")
    ap.add_argument("--font", help="path to a bold .ttf (default: Impact, Arial Black, DejaVu Bold)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("templates").set_defaults(fn=cmd_templates)
    c = sub.add_parser("compose")
    c.add_argument("spec")
    c.add_argument("--out", required=True)
    c.add_argument("--jpg", action="store_true")
    c.set_defaults(fn=cmd_compose)
    s = sub.add_parser("strip")
    s.add_argument("image")
    s.add_argument("--out", required=True)
    s.add_argument("--widths")
    s.set_defaults(fn=cmd_strip)
    dm = sub.add_parser("demo")
    dm.add_argument("--out", required=True)
    dm.set_defaults(fn=cmd_demo)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
