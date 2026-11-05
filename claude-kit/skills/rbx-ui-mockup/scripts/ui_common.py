#!/usr/bin/env python3
"""ui_common.py: shared helpers of the rbx-ui-mockup tools. Stdlib only, no network.

  fonts       FONTS (real Roblox Enum.Font names, read 2026-11-05 from create.roblox.com/docs/reference/engine/enums/Font) and font_css()
  colours     hex2rgb / rgb2hex / lum / contrast / lighten / darken
  browser     find_browser() (env UI_BROWSER wins; else an installed Chrome/Edge/Chromium), run_browser()
  png         decode_png() 8-bit non-interlaced gray/RGB/RGBA/gray+alpha, encode_png(), resample()
"""
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib

FONTS = """Legacy Arial SourceSans SourceSansBold SourceSansLight SourceSansItalic SourceSansSemibold Bodoni Garamond Cartoon Code Highway SciFi Arcade Fantasy Antique
Gotham GothamMedium GothamBold GothamBlack AmaticSC Bangers Creepster DenkOne Fondamento FredokaOne GrenzeGotisch IndieFlower JosefinSans Jura Kalam LuckiestGuy Merriweather
Michroma Nunito Oswald PatrickHand PermanentMarker Roboto RobotoCondensed RobotoMono Sarpanch SpecialElite TitilliumWeb Ubuntu BuilderSans BuilderSansMedium BuilderSansBold
BuilderSansExtraBold Arimo ArimoBold""".split()

_CSS = {
    "FredokaOne": '"Fredoka One","Fredoka",system-ui,sans-serif', "Nunito": '"Nunito",system-ui,sans-serif', "LuckiestGuy": '"Luckiest Guy","Impact",sans-serif',
    "BuilderSans": '"Builder Sans","Gotham",system-ui,sans-serif', "BuilderSansMedium": '"Builder Sans","Gotham",system-ui,sans-serif',
    "BuilderSansBold": '"Builder Sans","Gotham",system-ui,sans-serif', "BuilderSansExtraBold": '"Builder Sans","Gotham",system-ui,sans-serif',
    "GothamBold": '"Gotham","Montserrat","Segoe UI",sans-serif', "Gotham": '"Gotham","Montserrat","Segoe UI",sans-serif', "GothamMedium": '"Gotham","Montserrat","Segoe UI",sans-serif',
    "GothamBlack": '"Gotham","Montserrat","Segoe UI",sans-serif', "SourceSans": '"Source Sans Pro","Segoe UI",sans-serif', "SourceSansBold": '"Source Sans Pro","Segoe UI",sans-serif',
    "Michroma": '"Michroma","Eurostile",sans-serif', "Jura": '"Jura",sans-serif', "SciFi": '"Orbitron","Michroma",sans-serif', "Roboto": '"Roboto","Segoe UI",sans-serif',
    "Oswald": '"Oswald","Impact",sans-serif', "Ubuntu": '"Ubuntu",sans-serif', "Arial": 'Arial,sans-serif', "Arimo": '"Arimo",Arial,sans-serif', "ArimoBold": '"Arimo",Arial,sans-serif',
    "Code": '"Consolas","Courier New",monospace', "RobotoMono": '"Roboto Mono",monospace',
}
_BOLD = ("Bold", "Black", "ExtraBold", "Semibold", "LuckiestGuy", "FredokaOne", "Bangers")


def font_css(name):
    fam = _CSS.get(name)
    if fam is None:
        fam = '"%s",system-ui,sans-serif' % re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)
    weight = 700 if any(b in name for b in _BOLD) else 400
    return fam, weight


def hex2rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb2hex(c):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(v)))) for v in c[:3])


def is_hex(s):
    return isinstance(s, str) and re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", s) is not None


def _chan(v):
    v = v / 255.0
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def lum(c):
    return 0.2126 * _chan(c[0]) + 0.7152 * _chan(c[1]) + 0.0722 * _chan(c[2])


def contrast(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def mix(c, t, k):
    return tuple(c[i] + (t[i] - c[i]) * k for i in range(3))


def lighten(h, k=0.14):
    return rgb2hex(mix(hex2rgb(h), (255, 255, 255), k))


def darken(h, k=0.16):
    return rgb2hex(mix(hex2rgb(h), (0, 0, 0), k))


def grey(h, k=0.75):
    c = hex2rgb(h)
    g = 0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2]
    return rgb2hex(mix(c, (g, g, g), k))


def fexists(p):
    return bool(p) and os.path.isfile(p)


def find_browser(env=None):
    env = os.environ if env is None else env
    p = env.get("UI_BROWSER")
    if p:
        return p if os.path.isfile(p) else None
    cands = []
    if os.name == "nt":
        for base in (env.get("ProgramFiles"), env.get("ProgramFiles(x86)"), env.get("LOCALAPPDATA")):
            if base:
                cands += [os.path.join(base, "Microsoft", "Edge", "Application", "msedge.exe"), os.path.join(base, "Google", "Chrome", "Application", "chrome.exe")]
    elif sys.platform == "darwin":
        cands += ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge", "/Applications/Chromium.app/Contents/MacOS/Chromium"]
    for c in cands:
        if os.path.isfile(c):
            return c
    for n in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "microsoft-edge-stable", "chrome", "msedge"):
        w = shutil.which(n)
        if w:
            return w
    return None


def file_url(p):
    p = os.path.abspath(p).replace("\\", "/")
    return "file:///" + p.lstrip("/") if re.match(r"^[A-Za-z]:", p) else "file://" + p


def run_browser(browser, args, timeout=60, wait_file=None, marker=None):
    """Run a headless browser. Chrome/Edge on Windows hand the page to a detached process, so stdout is useless there: the caller either waits for a file
    (--screenshot) or for a console marker in the browser log (--dump-dom + --enable-logging). Returns {"stdout": str, "log": str, "ok": bool}."""
    import time
    prof = os.path.join(tempfile.gettempdir(), "uibrowser-%d-%s" % (os.getpid(), os.urandom(4).hex()))
    os.makedirs(prof)
    log, so = os.path.join(prof, "b.log"), os.path.join(prof, "stdout.txt")
    stub = browser.lower().endswith(".py")
    marks = (marker,) if isinstance(marker, str) else tuple(marker or ())
    cmd = [sys.executable, browser] if stub else [browser]
    cmd += ["--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check", "--disable-extensions", "--hide-scrollbars", "--user-data-dir=" + prof]
    if marker:
        cmd += ["--enable-logging", "--v=1", "--log-file=" + log]
    cmd += list(args)
    res = {"stdout": "", "log": "", "ok": False}
    fh = open(so, "wb")
    try:
        p = subprocess.Popen(cmd, stdout=fh, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        end = time.time() + timeout
        while time.time() < end:
            time.sleep(0.25)
            fh.flush()
            if wait_file and os.path.isfile(wait_file) and os.path.getsize(wait_file) > 100:
                time.sleep(0.4)
                res["ok"] = True
                break
            if marker:
                if os.path.isfile(log):
                    try:
                        t = open(log, encoding="utf-8", errors="replace").read()
                    except OSError:
                        t = ""
                    if any(m in t for m in marks):
                        res["log"], res["ok"] = t, True
                        break
                if os.path.getsize(so) > 0 and p.poll() is not None:
                    res["stdout"] = open(so, encoding="utf-8", errors="replace").read()
                    if any(m in res["stdout"] for m in marks):
                        res["ok"] = True
                        break
            if stub and p.poll() is not None:
                break
        if stub or not res["ok"]:
            p.poll() is None and p.kill()
        res["stdout"] = res["stdout"] or open(so, encoding="utf-8", errors="replace").read()
    finally:
        fh.close()
        for _ in range(8):
            try:
                shutil.rmtree(prof)
                break
            except OSError:
                time.sleep(0.5)
    return res


def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if pa <= pb and pa <= pc else (b if pb <= pc else c)


def decode_png(path):
    """-> (w, h, channels, rows) rows = list of bytearray (w*channels). Raises ValueError for unsupported files."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG: %s" % os.path.basename(path))
    pos, idat, hdr, pal = 8, [], None, None
    while pos < len(data):
        ln, typ = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + ln]
        pos += 12 + ln
        if typ == b"IHDR":
            hdr = struct.unpack(">IIBBBBB", body)
        elif typ == b"PLTE":
            pal = body
        elif typ == b"IDAT":
            idat.append(body)
        elif typ == b"IEND":
            break
    if not hdr:
        raise ValueError("PNG without header")
    w, h, depth, ctype, _, _, inter = hdr
    if depth != 8 or inter != 0 or ctype not in (0, 2, 3, 4, 6):
        raise ValueError("unsupported PNG (need 8-bit, non-interlaced gray/RGB/RGBA/palette)")
    ch = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ctype]
    raw = zlib.decompress(b"".join(idat))
    stride = w * ch
    rows, prev = [], bytearray(stride)
    p = 0
    for _ in range(h):
        ft = raw[p]
        line = bytearray(raw[p + 1:p + 1 + stride])
        p += 1 + stride
        if ft == 1:
            for i in range(ch, stride):
                line[i] = (line[i] + line[i - ch]) & 255
        elif ft == 2:
            line = bytearray((x + y) & 255 for x, y in zip(line, prev))
        elif ft == 3:
            for i in range(stride):
                a = line[i - ch] if i >= ch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif ft == 4:
            for i in range(stride):
                a = line[i - ch] if i >= ch else 0
                c = prev[i - ch] if i >= ch else 0
                line[i] = (line[i] + _paeth(a, prev[i], c)) & 255
        elif ft != 0:
            raise ValueError("bad PNG filter %d" % ft)
        rows.append(line)
        prev = line
    if ctype == 3:
        if not pal:
            raise ValueError("palette PNG without PLTE")
        rows = [bytearray(b for v in r for b in pal[v * 3:v * 3 + 3]) for r in rows]
        ch = 3
    return w, h, ch, rows


def encode_png(w, h, rgb_rows):
    """rgb_rows: list of h sequences of w*3 ints."""
    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    raw = b"".join(b"\x00" + bytes(r) for r in rgb_rows)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 6)) + chunk(b"IEND", b"")


def to_rgb_grid(img, gw, gh, box=None):
    """Box-average the image (or the fractional box (l,t,r,b)) into a gw x gh grid -> list of gh rows of gw (r,g,b) floats. Samples at most 6x6 pixels per cell."""
    w, h, ch, rows = img
    l, t, r, b = box if box else (0.0, 0.0, 1.0, 1.0)
    x0, x1, y0, y1 = l * w, r * w, t * h, b * h
    out = []
    for gy in range(gh):
        row = []
        ya, yb = y0 + (y1 - y0) * gy / gh, y0 + (y1 - y0) * (gy + 1) / gh
        ys = max(1, min(6, int(yb - ya)))
        for gx in range(gw):
            xa, xb = x0 + (x1 - x0) * gx / gw, x0 + (x1 - x0) * (gx + 1) / gw
            xs = max(1, min(6, int(xb - xa)))
            sr = sg = sb = n = 0
            for j in range(ys):
                yy = min(h - 1, max(0, int(ya + (yb - ya) * (j + 0.5) / ys)))
                line = rows[yy]
                for i in range(xs):
                    xx = min(w - 1, max(0, int(xa + (xb - xa) * (i + 0.5) / xs)))
                    if ch >= 3:
                        o = xx * ch
                        sr += line[o]; sg += line[o + 1]; sb += line[o + 2]
                    else:
                        v = line[xx * ch]
                        sr += v; sg += v; sb += v
                    n += 1
            row.append((sr / n, sg / n, sb / n))
        out.append(row)
    return out


def jdump(o):
    import json
    return json.dumps(o, indent=1, ensure_ascii=False, sort_keys=False) + "\n"


def write_text(p, t):
    d = os.path.dirname(os.path.abspath(p))
    os.makedirs(d, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return p


def read_json(p):
    import json
    with open(p, encoding="utf-8-sig") as f:
        return json.load(f)
