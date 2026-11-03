#!/usr/bin/env python3
"""image_specs.py - check thumbnail/icon files against specs YOU pass in (taken from the live Creator Docs check). Stdlib only.

  python image_specs.py FILE [FILE ...] [--expect 1920x1080] [--aspect 16:9] [--max-mb 5] [--min-width 640] [--json]
  python image_specs.py --selftest

Reads PNG and JPEG headers only (no pixels): width, height, bytes, aspect ratio, PNG colour type/alpha. No spec numbers are built in on
purpose: Roblox's requirements change, so the skill live-checks them and passes them here. Exit 1 when a file fails a given spec.
"""
import argparse
import json
import os
import struct
import sys
import zlib


def png_info(b):
    if b[:8] != b"\x89PNG\r\n\x1a\n" or b[12:16] != b"IHDR":
        return None
    w, h, depth, ctype = struct.unpack(">IIBB", b[16:26])
    return dict(format="png", width=w, height=h, alpha=ctype in (4, 6), bit_depth=depth)


def jpeg_info(b):
    if b[:2] != b"\xff\xd8":
        return None
    i = 2
    while i + 9 < len(b):
        if b[i] != 0xFF:
            i += 1
            continue
        m = b[i + 1]
        if m in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", b[i + 5:i + 9])
            return dict(format="jpeg", width=w, height=h, alpha=False, bit_depth=8)
        if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
            i += 2
            continue
        i += 2 + struct.unpack(">H", b[i + 2:i + 4])[0]
    return None


def inspect(path):
    with open(path, "rb") as f:
        b = f.read()
    info = png_info(b) or jpeg_info(b)
    if not info:
        return dict(path=path, error="not a PNG or JPEG")
    info.update(path=path, bytes=len(b))
    return info


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def evaluate(info, expect, aspect, max_mb, min_width):
    if "error" in info:
        return [info["error"]]
    fails = []
    w, h = info["width"], info["height"]
    if expect and (w, h) != expect:
        fails.append("size %dx%d, expected %dx%d" % (w, h, expect[0], expect[1]))
    if aspect and abs(w / h - aspect[0] / aspect[1]) > 0.01:
        fails.append("aspect %.3f, expected %d:%d" % (w / h, aspect[0], aspect[1]))
    if max_mb and info["bytes"] > max_mb * 1024 * 1024:
        fails.append("%.2f MB, over %s MB" % (info["bytes"] / 1048576, max_mb))
    if min_width and w < min_width:
        fails.append("width %d, under %d" % (w, min_width))
    return fails


def pair(s, sep):
    a, b = s.lower().split(sep)
    return int(a), int(b)


def selftest():
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d))
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1920, 1080, 8, 6, 0, 0, 0)) + chunk(b"IEND", b"")
    i = png_info(png)
    assert (i["width"], i["height"], i["alpha"]) == (1920, 1080, True)
    jpg = b"\xff\xd8" + b"\xff\xe0\x00\x04ab" + b"\xff\xc0\x00\x0b\x08" + struct.pack(">HH", 512, 512) + b"\x01\x01\x11\x00" + b"\xff\xd9"
    j = jpeg_info(jpg)
    assert (j["width"], j["height"]) == (512, 512)
    info = dict(png_info(png), bytes=2 * 1048576, path="x")
    assert evaluate(info, (1920, 1080), (16, 9), 5, 640) == []
    assert len(evaluate(info, (1280, 720), (1, 1), 1, 4000)) == 4
    print("selftest ok")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--expect")
    ap.add_argument("--aspect")
    ap.add_argument("--max-mb", type=float)
    ap.add_argument("--min-width", type=int)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.files:
        ap.error("give at least one image file")
    expect = pair(a.expect, "x") if a.expect else None
    aspect = pair(a.aspect, ":") if a.aspect else None
    bad = 0
    res = []
    for p in a.files:
        info = inspect(p) if os.path.isfile(p) else dict(path=p, error="file not found")
        fails = evaluate(info, expect, aspect, a.max_mb, a.min_width)
        info["fails"] = fails
        bad += bool(fails)
        res.append(info)
        if not a.json:
            if "error" in info:
                print("FAIL %s: %s" % (p, info["error"]))
            else:
                g = gcd(info["width"], info["height"])
                print("%s %s: %s %dx%d (%d:%d) %.2f MB alpha=%s%s" % ("FAIL" if fails else "ok  ", os.path.basename(p), info["format"], info["width"], info["height"],
                      info["width"] // g, info["height"] // g, info["bytes"] / 1048576, info["alpha"], ("  <- " + "; ".join(fails)) if fails else ""))
    if a.json:
        print(json.dumps(res))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
