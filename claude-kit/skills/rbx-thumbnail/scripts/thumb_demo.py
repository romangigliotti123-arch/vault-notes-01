#!/usr/bin/env python3
"""thumb_demo.py: sample layers and three composition concepts for thumb_compose.py (`thumb_compose.py demo --out DIR`).
Everything is drawn here from scratch (an invented blocky hero, a block tower, lava and a lava drop for an invented game called Lava Climb):
no real person, no other game's art, no copied thumbnail. It shows the workflow: pick the hook, build three DIFFERENT compositions, look at the 100 px strips.
"""
import json
import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter

S = 2  # supersample


def _rr(d, box, r, fill, outline=None, width=0):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def hero(path):
    W, H = 700 * S, 900 * S
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    k = S
    # arms thrown up (behind the head)
    for sgn in (-1, 1):
        cx = 350 * k + sgn * 235 * k
        d.line((350 * k + sgn * 140 * k, 640 * k, cx + sgn * 40 * k, 330 * k), fill=(46, 125, 250), width=90 * k)
        d.ellipse((cx + sgn * 40 * k - 62 * k, 330 * k - 80 * k, cx + sgn * 40 * k + 62 * k, 330 * k + 44 * k), fill=(255, 205, 60))
    # torso
    _rr(d, (190 * k, 590 * k, 510 * k, 900 * k), 36 * k, (46, 125, 250))
    d.rectangle((190 * k, 700 * k, 510 * k, 735 * k), fill=(255, 255, 255))
    # head
    _rr(d, (110 * k, 150 * k, 590 * k, 640 * k), 90 * k, (255, 209, 64))
    _rr(d, (130 * k, 160 * k, 570 * k, 330 * k), 80 * k, (255, 224, 110))  # soft highlight
    # hair block
    _rr(d, (100 * k, 90 * k, 600 * k, 270 * k), 70 * k, (88, 52, 30))
    d.polygon([(140 * k, 270 * k), (560 * k, 270 * k), (520 * k, 340 * k), (180 * k, 340 * k)], fill=(88, 52, 30))
    # face: huge scared eyes, raised brows, open mouth
    for ex in (255, 445):
        d.ellipse(((ex - 70) * k, 345 * k, (ex + 70) * k, 520 * k), fill=(255, 255, 255), outline=(20, 20, 30), width=8 * k)
        px = ex + (14 if ex < 350 else -14)
        d.ellipse(((px - 30) * k, 410 * k, (px + 30) * k, 485 * k), fill=(20, 20, 30))
        d.ellipse(((px - 12) * k, 420 * k, (px + 2) * k, 436 * k), fill=(255, 255, 255))
    d.line((190 * k, 330 * k, 300 * k, 300 * k), fill=(40, 24, 14), width=22 * k)
    d.line((510 * k, 330 * k, 400 * k, 300 * k), fill=(40, 24, 14), width=22 * k)
    d.ellipse((290 * k, 545 * k, 410 * k, 625 * k), fill=(60, 15, 20))
    d.rectangle((310 * k, 548 * k, 390 * k, 565 * k), fill=(255, 255, 255))
    d.ellipse((315 * k, 590 * k, 385 * k, 625 * k), fill=(240, 110, 130))
    for bx in (190, 510):
        d.ellipse(((bx - 34) * k, 520 * k, (bx + 34) * k, 560 * k), fill=(255, 140, 90, 170))
    im = im.resize((W // S, H // S), Image.LANCZOS)
    im.save(path)


def tower(path):
    W, H = 520 * S, 1000 * S
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cols = [(255, 99, 99), (255, 190, 60), (110, 220, 110), (70, 170, 255), (180, 110, 255), (255, 120, 200)]
    rnd = random.Random(7)
    y = H - 4 * S
    bh = 76 * S
    i = 0
    while y - bh > 70 * S:
        off = rnd.randint(-22, 22) * S
        w = (400 - 6 * i) * S
        x0 = (W - w) // 2 + off
        _rr(d, (x0, y - bh, x0 + w, y), 16 * S, cols[i % len(cols)], (30, 20, 50), 6 * S)
        d.rectangle((x0 + 18 * S, y - bh + 14 * S, x0 + w - 18 * S, y - bh + 26 * S), fill=(255, 255, 255, 90))
        y -= bh - 6 * S
        i += 1
    d.line((W // 2, y, W // 2, 20 * S), fill=(60, 40, 40), width=8 * S)
    d.polygon([(W // 2, 20 * S), (W // 2 + 110 * S, 52 * S), (W // 2, 84 * S)], fill=(255, 235, 0), outline=(30, 20, 50))
    im.resize((W // S, H // S), Image.LANCZOS).save(path)


def lava(path):
    W, H = 1920, 330
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = im.load()
    for y in range(H):
        t = y / H
        c = (255, int(210 - 150 * t), int(40 - 30 * t))
        for x in range(W):
            px[x, y] = c + (255,)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    pts = [(0, H)]
    for x in range(0, W + 40, 40):
        pts.append((x, 70 + 34 * math.sin(x / 140.0) + 18 * math.sin(x / 47.0)))
    pts.append((W, H))
    md.polygon(pts, fill=255)
    im.putalpha(mask)
    d = ImageDraw.Draw(im)
    rnd = random.Random(3)
    for _ in range(26):
        x, y, r = rnd.randint(0, W), rnd.randint(110, H - 10), rnd.randint(8, 26)
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 245, 140, 200))
    for _ in range(14):
        x, y, r = rnd.randint(0, W), rnd.randint(150, H - 10), rnd.randint(18, 40)
        d.ellipse((x - r, y - r // 2, x + r, y + r // 2), fill=(120, 20, 10, 230))
    im.save(path)


def drop(path):
    W, H = 600 * S, 760 * S
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = W // 2
    d.polygon([(cx, 30 * S), (cx + 240 * S, 400 * S), (cx - 240 * S, 400 * S)], fill=(255, 120, 20))
    d.ellipse((cx - 250 * S, 250 * S, cx + 250 * S, 720 * S), fill=(255, 120, 20))
    d.ellipse((cx - 190 * S, 330 * S, cx + 190 * S, 680 * S), fill=(255, 190, 40))
    d.ellipse((cx - 120 * S, 420 * S, cx + 120 * S, 620 * S), fill=(255, 240, 130))
    d.ellipse((cx - 170 * S, 330 * S, cx - 90 * S, 410 * S), fill=(255, 255, 255, 230))
    im.resize((W // S, H // S), Image.LANCZOS).save(path)


def _concept(name, desc, spec, base):
    d = os.path.join(base, name)
    os.makedirs(d, exist_ok=True)
    spec["name"] = name
    sp = os.path.join(d, "spec.json")
    json.dump(spec, open(sp, "w", encoding="utf8"), indent=1)
    return sp


def run(out, tc):
    import argparse
    base = os.path.abspath(out)
    layers = os.path.join(base, "layers")
    os.makedirs(layers, exist_ok=True)
    hero(os.path.join(layers, "hero.png"))
    tower(os.path.join(layers, "tower.png"))
    lava(os.path.join(layers, "lava.png"))
    drop(os.path.join(layers, "drop.png"))
    rel = "../layers/"
    outline = {"px": 16, "color": "#14102a"}
    concepts = {
        "concept-a-face-left": {
            "template": "face-left-prize-right",
            "background": {"gradient": ["#6a3cc9", "#2b1470", "#120833"], "angle": 80},
            "burst": {"color": "#ffffff", "alpha": 30, "cx": 0.27, "cy": 0.45, "rays": 20},
            "layers": [
                {"file": rel + "lava.png", "role": "scene", "glow": {"px": 50, "color": "#ff7a00", "strength": 1.2}},
                {"file": rel + "tower.png", "role": "prize", "cx": 0.74, "cy": 0.65, "h": 0.66, "outline": outline, "shadow": True},
                {"file": rel + "hero.png", "role": "hero", "outline": outline, "glow": {"px": 46, "color": "#fff176"}, "shadow": True}],
            "texts": [{"text": "RUN!", "slot": "tr", "size": 0.22, "fill": "#ffe600", "stroke": "#14102a", "rotate": -4}]},
        "concept-b-tiny-hero": {
            "template": "tiny-hero-huge-scene",
            "background": {"gradient": ["#2a5bd7", "#162a8a", "#0b1240"], "angle": 90},
            "burst": {"color": "#8fd8ff", "alpha": 34, "cx": 0.72, "cy": 0.3, "rays": 14},
            "layers": [
                {"file": rel + "tower.png", "role": "prize", "cx": 0.72, "cy": 0.62, "h": 0.84, "outline": outline, "shadow": True},
                {"file": rel + "hero.png", "role": "hero", "cx": 0.72, "cy": 0.16, "h": 0.26, "outline": outline, "glow": {"px": 36, "color": "#ffffff"}},
                {"file": rel + "lava.png", "role": "scene", "glow": {"px": 50, "color": "#ff7a00", "strength": 1.2}}],
            "texts": [{"text": "50 FLOORS", "slot": "tl", "size": 0.21, "fill": "#ffffff", "stroke": "#14102a", "max_width": 0.52}]},
        "concept-c-object": {
            "template": "object-only",
            "background": {"gradient": ["#6a11cb", "#2a0845"], "angle": 100},
            "burst": {"color": "#ffb347", "alpha": 40, "cx": 0.5, "cy": 0.52, "rays": 24},
            "layers": [
                {"file": rel + "drop.png", "role": "prize", "outline": outline, "glow": {"px": 70, "color": "#ff9a3c", "strength": 1.8}},
                {"file": rel + "hero.png", "role": "hero", "icon": False, "h": 0.5, "cx": 0.13, "cy": 0.72, "outline": outline}],
            "texts": []},
    }
    results = {}
    for name, spec in concepts.items():
        sp = _concept(name, "", spec, base)
        print("== %s" % name)
        tc.cmd_compose(argparse.Namespace(spec=sp, out=os.path.join(base, name), jpg=False, font=None))
        results[name] = os.path.join(base, name)
    # contact sheet: three thumbnails and three icons, labelled
    cw, ch, ic = 600, 338, 338
    sheet = Image.new("RGB", (cw * 3 + 40, ch + ic + 90), (36, 36, 44))
    d = ImageDraw.Draw(sheet)
    for i, (name, dirp) in enumerate(results.items()):
        t = Image.open(os.path.join(dirp, "thumbnail-1920x1080.png")).resize((cw, ch), Image.LANCZOS)
        ico = Image.open(os.path.join(dirp, "icon-512.png")).resize((ic, ic), Image.LANCZOS)
        x = 10 + i * (cw + 10)
        sheet.paste(t, (x, 40))
        sheet.paste(ico, (x, 40 + ch + 30))
        d.text((x, 12), name, fill=(255, 220, 120), font=tc.get_font(18))
    sheet.save(os.path.join(base, "contact-sheet.png"))
    print("wrote %s" % os.path.join(base, "contact-sheet.png"))
    return 0
