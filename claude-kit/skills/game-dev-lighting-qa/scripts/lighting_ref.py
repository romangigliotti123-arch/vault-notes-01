#!/usr/bin/env python3
"""lighting_ref.py: Python reference of LightingCore.luau (checks L1-L12 of game-dev-lighting-qa + preset resolution).
Same algorithm as the Luau core; both run on tests/fixtures.json and must agree field by field. Edit both together. Constants live in presets.json.

  verify(state, cfg) -> report         the 12 checks on a plain-table lighting state (see references/api.md)
  resolve(preset, time, mobile, overrides) -> {preset, time, mobile, desired}   the property set a preset produces
  bands(genre, phase) -> tolerance bands used for that genre and time of day
"""
import copy
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "presets.json"), encoding="utf-8"))
M = DATA["model"]
COSTS = DATA["costs"]
PRESETS = DATA["presets"]
ORDER = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "L11", "L12"]
NAMES = {
    "L1": "Not the default Roblox lighting", "L2": "Atmosphere present and sane", "L3": "Sky set", "L4": "Post effects in sane ranges",
    "L5": "Colour grading cohesive with the palette", "L6": "Scene brightness not crushed or blown", "L7": "Shadows on for the key lights",
    "L8": "Fog and haze density suit the genre", "L9": "Interiors lit", "L10": "Performance budget (mobile and PC)",
    "L11": "No conflicting duplicate effects", "L12": "Time of day and exposure coherent",
}
PHASE_KEYS = ("luma_mean", "crushed_max", "blown_max", "spread_min", "amb_outdoor")
MIN_WAIVER = 10


def rnd(x):
    return math.floor(x * 1000 + 0.5) / 1000


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


# ------------------------------------------------------------------ names, merge, presets
def canon(name):
    if name is None:
        return None
    s = re.sub(r"[^a-z0-9]+", "_", str(name).lower()).strip("_")
    if s in PRESETS:
        return s
    return DATA["aliases"].get(s)


def merge(base, patch):
    out = copy.deepcopy(base)
    for k, v in patch.items():
        if v is False:
            out[k] = False
        elif isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def resolve(preset, time=None, mobile=False, overrides=None):
    g = canon(preset)
    if not g:
        return None
    p = PRESETS[g]
    t = (time or p["default_time"]).lower()
    if t not in ("day", "golden", "night"):
        return None
    cfg = copy.deepcopy(p["base"])
    if t != p["default_time"]:
        cfg = merge(cfg, DATA["global_times"].get(t, {}))
    cfg = merge(cfg, p.get("times", {}).get(t, {}))
    if mobile:
        cfg = merge(cfg, {k: v for k, v in DATA["mobile"].items() if k != "note"})
    if overrides:
        cfg = merge(cfg, overrides)
    return dict(preset=g, time=t, mobile=bool(mobile), desired=cfg)


def bands(genre, phase):
    b = copy.deepcopy(DATA["bands"]["generic"])
    b = merge(b, DATA["bands"]["phases"].get(phase, {}))
    g = canon(genre)
    if g:
        gb = PRESETS[g].get("bands", {})
        for k, v in gb.items():
            if phase == "day" or k not in PHASE_KEYS:
                b[k] = copy.deepcopy(v)
        b = merge(b, PRESETS[g].get("phase_bands", {}).get(phase, {}))
    return b


# ------------------------------------------------------------------ colour and sun maths
def luma255(c):
    return (0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]) / 255.0


def luma_lin(c):
    g = M["albedo_gamma"]
    return 0.2126 * (c[0] ** g) + 0.7152 * (c[1] ** g) + 0.0722 * (c[2] ** g)


def hsv(c):
    r, g, b = c[0] / 255.0, c[1] / 255.0, c[2] / 255.0
    mx, mn = max(r, g, b), min(r, g, b)
    d = mx - mn
    if d <= 1e-9:
        h = 0.0
    elif mx == r:
        h = 60.0 * (((g - b) / d) % 6)
    elif mx == g:
        h = 60.0 * ((b - r) / d + 2)
    else:
        h = 60.0 * ((r - g) / d + 4)
    s = 0.0 if mx <= 1e-9 else d / mx
    return h % 360.0, s, mx


def hue_dist(a, b):
    d = abs(a - b) % 360.0
    return 360.0 - d if d > 180.0 else d


def sun_info(lt):
    """-> (elevation_deg, sun vector [x, y, z])"""
    sd = lt.get("sunDir")
    if sd:
        n = math.sqrt(sd[0] ** 2 + sd[1] ** 2 + sd[2] ** 2) or 1.0
        v = [sd[0] / n, sd[1] / n, sd[2] / n]
        return math.degrees(math.asin(clamp(v[1], -1, 1))), v
    lat = math.radians(lt.get("GeographicLatitude", 41.7333))
    h = math.radians((lt.get("ClockTime", 14.5) - 12.0) * 15.0)
    up = math.cos(lat) * math.cos(h)
    v = [-math.sin(h), up, -math.sin(lat) * math.cos(h)]
    return math.degrees(math.asin(clamp(up, -1, 1))), v


def phase_of(elev):
    if elev >= M["day_elev"]:
        return "day"
    if elev < M["night_elev"]:
        return "night"
    return "dusk"


def sun_up(elev):
    return clamp((elev - M["sun_ramp_lo"]) / M["sun_ramp_span"], 0.0, 1.0)


def first_enabled(lst):
    for x in lst or []:
        if x.get("Enabled", True) is not False:
            return x
    return None


def enabled(lst):
    return [x for x in (lst or []) if x.get("Enabled", True) is not False]


def pct(sorted_vals, q):
    n = len(sorted_vals)
    return sorted_vals[int(math.floor(q * (n - 1)))]


def sample_luma(smp, lt, elev, sunv, sup, cc):
    alb = [c for c in smp["albedo"]]
    albL = luma_lin(alb)
    indoor = bool(smp.get("indoor"))
    lit = smp.get("lit", True) is not False
    n = smp.get("n") or [0, 1, 0]
    nd = max(0.0, n[0] * sunv[0] + n[1] * sunv[1] + n[2] * sunv[2]) if sup > 0 else 0.0
    amb = luma255(lt["Ambient"] if indoor else lt["OutdoorAmbient"])
    envd = lt.get("EnvironmentDiffuseScale", 1)
    sky = (M["sky_amb_base"] + M["sky_amb_day"] * sup) * envd * (M["indoor_sky_share"] if indoor else 1.0)
    ambE = amb * M["ambient_gain"] + sky
    strength = sup * clamp(lt.get("Brightness", 3) / 3.0, 0.0, 4.0) * (0.5 + 0.5 * min(1.0, max(math.sin(math.radians(elev)), 0.0) * 1.6))
    sunE = 0.0 if (indoor or not lit) else strength * nd * M["sun_gain"]
    E = albL * (ambE + sunE)
    if smp.get("emissive"):
        E += M["emissive_gain"] * (0.4 + albL)
    E += (smp.get("lightE") or 0.0) * albL * M["light_gain"]
    E *= 2.0 ** lt.get("ExposureCompensation", 0)
    v = E / (1.0 + M["tone_k"] * E)
    out = v ** (1.0 / M["out_gamma"])
    if cc:
        out = (out - 0.5) * (1.0 + cc.get("Contrast", 0)) + 0.5 + cc.get("Brightness", 0)
    return clamp(out, 0.0, 1.0)


def scene_stats(state):
    lt = state["lighting"]
    elev, sunv = sun_info(lt)
    sup = sun_up(elev)
    cc = first_enabled(state.get("colorCorrections"))
    vals, indoor_vals, indoor_lit = [], [], 0
    for s in state.get("samples") or []:
        L = sample_luma(s, lt, elev, sunv, sup, cc)
        vals.append(L)
        if s.get("indoor"):
            indoor_vals.append(L)
            if (s.get("lightE") or 0) > 0:
                indoor_lit += 1
    n = len(vals)
    out = dict(n=n, indoor_n=len(indoor_vals), indoor_fraction=0.0, indoor_mean=None, indoor_lit_fraction=0.0)
    if n:
        sv = sorted(vals)
        out.update(mean=sum(vals) / n, p10=pct(sv, 0.1), p50=pct(sv, 0.5), p90=pct(sv, 0.9),
                   crushed=len([v for v in vals if v < M["crushed_luma"]]) / n, blown=len([v for v in vals if v > M["blown_luma"]]) / n,
                   indoor_fraction=len(indoor_vals) / n)
        out["spread"] = out["p90"] - out["p10"]
    if indoor_vals:
        out["indoor_mean"] = sum(indoor_vals) / len(indoor_vals)
        out["indoor_lit_fraction"] = indoor_lit / len(indoor_vals)
    return out


# ------------------------------------------------------------------ report helpers
def mk(status="pass"):
    return dict(status=status, measured={}, tolerance={}, issues=[], fixes=[], unverified=[], warnings=[])


def fail(c, msg, fix=None):
    c["status"] = "fail"
    c["issues"].append(msg)
    if fix:
        c["fixes"].append(fix)


def setfix(target, value, note=None):
    f = dict(action="set", target=target, value=value)
    if note:
        f["note"] = note
    return f


def preset_fix(ctx, why):
    g = ctx["genre"]
    if not g:
        return dict(action="applyPreset", preset="(choose a genre)", note=why)
    return dict(action="applyPreset", preset=g, time=ctx["time"], mobile=ctx["platform"] == "mobile", note=why)


def fmt(x):
    if isinstance(x, float):
        return ("%.3f" % x).rstrip("0").rstrip(".")
    return str(x)


def rng(v, lo, hi):
    return v < lo or v > hi


# ------------------------------------------------------------------ the checks
def l1(state, ctx):
    c = mk()
    lt, D = state["lighting"], DATA["roblox_default"]
    unchanged = []

    def near(v, lst, tol):
        return any(abs(v - x) <= tol for x in lst)

    def near_col(v, lst):
        return any(max(abs(v[i] - x[i]) for i in range(3)) <= D["tol_color"] for x in lst)

    tracked = 0
    for k in ("Brightness", "ClockTime", "ExposureCompensation", "ShadowSoftness"):
        tracked += 1
        if k in lt and near(lt[k], D[k], D["tol"]):
            unchanged.append(k)
    tracked += 1
    if "GeographicLatitude" in lt and near(lt["GeographicLatitude"], D["GeographicLatitude"], D["tol_lat"]):
        unchanged.append("GeographicLatitude")
    for k in ("Ambient", "OutdoorAmbient", "ColorShift_Top", "ColorShift_Bottom"):
        tracked += 1
        if k in lt and near_col(lt[k], D[k]):
            unchanged.append(k)
    changed = tracked - len(unchanged)
    tuned = [n for n, key in (("Atmosphere", "atmospheres"), ("Bloom", "blooms"), ("ColorCorrection", "colorCorrections"), ("SunRays", "sunRays")) if enabled(state.get(key))]
    c["measured"] = dict(changed=changed, tracked=tracked, unchanged=unchanged, tuned_objects=tuned, preset=(state.get("marks") or {}).get("preset"))
    c["tolerance"] = dict(min_changed=D["min_changed"], min_tuned_objects=1)
    if changed < D["min_changed"]:
        fail(c, "only %d of %d lighting properties differ from the Roblox defaults (unchanged: %s): this is the default Roblox look" % (changed, tracked, ", ".join(unchanged)),
             preset_fix(ctx, "L1 default lighting"))
    if not tuned:
        fail(c, "no enabled Atmosphere, Bloom, ColorCorrection or SunRays: nothing shapes the image beyond engine defaults", preset_fix(ctx, "L1 no post effects"))
    if lt.get("Technology") in ("Voxel", "Compatibility", "Legacy"):
        c["warnings"].append("Technology %s: Future (PC) or ShadowMap (mobile-safe) gives real shadows and lighting" % lt.get("Technology"))
    return c


def l2(state, ctx):
    c = mk()
    b = ctx["bands"]
    atm = state.get("atmospheres") or []
    c["measured"] = dict(count=len(atm))
    c["tolerance"] = dict(count=1, offset=[0, 1], haze=b["haze"], glare=b["glare"])
    if not atm:
        fail(c, "no Atmosphere in Lighting: no depth haze, flat horizon", preset_fix(ctx, "L2 add Atmosphere"))
        return c
    a = atm[0]
    c["measured"].update(Density=a.get("Density"), Offset=a.get("Offset"), Haze=a.get("Haze"), Glare=a.get("Glare"), Color=a.get("Color"))
    if len(atm) > 1:
        fail(c, "%d Atmosphere objects (only one is used; the others fight it)" % len(atm), dict(action="remove", target="Atmosphere", keep=1))
    if a.get("Density", 0) <= 0:
        fail(c, "Atmosphere.Density is %s (0 = no atmosphere)" % fmt(a.get("Density", 0)), preset_fix(ctx, "L2 density"))
    if rng(a.get("Offset", 0), 0, 1):
        fail(c, "Atmosphere.Offset %s outside 0-1" % fmt(a.get("Offset")), setfix("Atmosphere.Offset", clamp(a.get("Offset", 0), 0, 1)))
    if rng(a.get("Haze", 0), b["haze"][0], b["haze"][1]):
        fail(c, "Atmosphere.Haze %s outside %s-%s" % (fmt(a.get("Haze")), fmt(b["haze"][0]), fmt(b["haze"][1])), setfix("Atmosphere.Haze", clamp(a.get("Haze", 0), b["haze"][0], b["haze"][1])))
    if rng(a.get("Glare", 0), b["glare"][0], b["glare"][1]):
        fail(c, "Atmosphere.Glare %s outside %s-%s" % (fmt(a.get("Glare")), fmt(b["glare"][0]), fmt(b["glare"][1])), setfix("Atmosphere.Glare", clamp(a.get("Glare", 0), b["glare"][0], b["glare"][1])))
    col = a.get("Color")
    if col and max(col) < 8:
        fail(c, "Atmosphere.Color is black: the haze would swallow the scene", preset_fix(ctx, "L2 colour"))
    return c


def l3(state, ctx):
    c = mk()
    skies = state.get("skies") or []
    keys = ("SkyboxBk", "SkyboxDn", "SkyboxFt", "SkyboxLf", "SkyboxRt", "SkyboxUp")
    c["measured"] = dict(count=len(skies))
    c["tolerance"] = dict(count=1, textures=6, sun_size=[1, 60])
    if not skies:
        fail(c, "no Sky object: the engine falls back to a bare default sky", preset_fix(ctx, "L3 add Sky"))
        return c
    s = skies[0]
    if len(skies) > 1:
        fail(c, "%d Sky objects (only one is used)" % len(skies), dict(action="remove", target="Sky", keep=1))
    missing = [k for k in keys if not s.get(k)]
    dflt = [k for k in keys if s.get(k) and s.get(k) == DATA["sky_default_textures"][k]]
    c["measured"].update(missing=missing, default_textures=len(dflt), StarCount=s.get("StarCount"), SunAngularSize=s.get("SunAngularSize"))
    if missing:
        fail(c, "Sky texture(s) empty: %s" % ", ".join(missing), preset_fix(ctx, "L3 textures"))
    elif len(dflt) == 6:
        c["warnings"].append("Sky uses the six default Roblox textures: find a sky that matches the art direction (search_asset) and pass it as an override; never invent asset ids")
    if rng(s.get("SunAngularSize", 21), 1, 60):
        fail(c, "Sky.SunAngularSize %s outside 1-60" % fmt(s.get("SunAngularSize")), setfix("Sky.SunAngularSize", clamp(s.get("SunAngularSize", 21), 1, 60)))
    if ctx["phase"] == "night" and s.get("CelestialBodiesShown", True) and s.get("StarCount", 3000) < 500:
        c["warnings"].append("night scene with StarCount %s: the sky will look empty" % fmt(s.get("StarCount", 0)))
    return c


def l4(state, ctx):
    c = mk()
    b = ctx["bands"]
    m = dict(bloom=[], colorCorrection=[], sunRays=[], depthOfField=[], blur=[])
    for i, e in enumerate(enabled(state.get("blooms"))):
        idx = e.get("Intensity", 1) * (e.get("Size", 24) / 24.0) / max(e.get("Threshold", 2), 0.1)
        m["bloom"].append(dict(Intensity=e.get("Intensity"), Size=e.get("Size"), Threshold=e.get("Threshold"), index=rnd(idx)))
        if e.get("Intensity", 1) > b["bloom_int_max"]:
            fail(c, "Bloom.Intensity %s above %s: highlights bleed over everything" % (fmt(e.get("Intensity")), fmt(b["bloom_int_max"])), setfix("Bloom.Intensity", b["bloom_int_max"] * 0.5))
        if e.get("Threshold", 2) < b["bloom_thr_min"]:
            fail(c, "Bloom.Threshold %s below %s: everything blooms" % (fmt(e.get("Threshold")), fmt(b["bloom_thr_min"])), setfix("Bloom.Threshold", 1.0))
        if e.get("Size", 24) > b["bloom_size_max"]:
            fail(c, "Bloom.Size %s above %s: smeared glow" % (fmt(e.get("Size")), fmt(b["bloom_size_max"])), setfix("Bloom.Size", 24))
        if idx > b["bloom_index_max"]:
            fail(c, "bloom strength index %s above %s (Intensity x Size/24 / Threshold): blown out" % (fmt(rnd(idx)), fmt(b["bloom_index_max"])), setfix("Bloom.Intensity", rnd(b["bloom_index_max"] * 0.4 * max(e.get("Threshold", 1), 0.1) * 24.0 / max(e.get("Size", 24), 1))))
    for e in enabled(state.get("colorCorrections")):
        tint = e.get("TintColor", [255, 255, 255])
        _, ts, _ = hsv(tint)
        m["colorCorrection"].append(dict(Brightness=e.get("Brightness"), Contrast=e.get("Contrast"), Saturation=e.get("Saturation"), tint_saturation=rnd(ts)))
        for key, lo_hi, fixv in (("Brightness", b["cc_brightness"], 0.0), ("Contrast", b["cc_contrast"], 0.15), ("Saturation", b["cc_saturation"], 0.2)):
            v = e.get(key, 0)
            if rng(v, lo_hi[0], lo_hi[1]):
                fail(c, "ColorCorrection.%s %s outside %s to %s" % (key, fmt(v), fmt(lo_hi[0]), fmt(lo_hi[1])), setfix("ColorCorrection." + key, clamp(v, lo_hi[0], lo_hi[1])))
        if ts > b["cc_tint_sat_max"]:
            fail(c, "ColorCorrection.TintColor saturation %s above %s: the whole screen is one colour" % (fmt(rnd(ts)), fmt(b["cc_tint_sat_max"])), setfix("ColorCorrection.TintColor", [255, 255, 255]))
        if e.get("Contrast", 0) > 0.3 and e.get("Saturation", 0) > 0.45:
            c["warnings"].append("ColorCorrection Contrast %s and Saturation %s both high: harsh, check the result in Studio" % (fmt(e.get("Contrast")), fmt(e.get("Saturation"))))
    for e in enabled(state.get("sunRays")):
        m["sunRays"].append(dict(Intensity=e.get("Intensity"), Spread=e.get("Spread")))
        if e.get("Intensity", 0.25) > b["sunrays_int_max"]:
            fail(c, "SunRays.Intensity %s above %s: white fog around the sun" % (fmt(e.get("Intensity")), fmt(b["sunrays_int_max"])), setfix("SunRays.Intensity", b["sunrays_int_max"] * 0.5))
        if e.get("Spread", 1) > b["sunrays_spread_max"]:
            fail(c, "SunRays.Spread %s above %s" % (fmt(e.get("Spread")), fmt(b["sunrays_spread_max"])), setfix("SunRays.Spread", b["sunrays_spread_max"] * 0.7))
    for e in enabled(state.get("dofs")):
        m["depthOfField"].append(dict(FarIntensity=e.get("FarIntensity"), NearIntensity=e.get("NearIntensity"), FocusDistance=e.get("FocusDistance"), InFocusRadius=e.get("InFocusRadius")))
        if not b["dof_allowed"]:
            fail(c, "DepthOfField is enabled but this genre needs a sharp playfield", dict(action="remove", target="DepthOfField"))
            continue
        if e.get("FarIntensity", 0.75) > b["dof_far_max"]:
            fail(c, "DepthOfField.FarIntensity %s above %s: blurry gameplay" % (fmt(e.get("FarIntensity")), fmt(b["dof_far_max"])), setfix("DepthOfField.FarIntensity", b["dof_far_max"] * 0.4))
        if e.get("NearIntensity", 0.75) > b["dof_near_max"]:
            fail(c, "DepthOfField.NearIntensity %s above %s: the avatar blurs" % (fmt(e.get("NearIntensity")), fmt(b["dof_near_max"])), setfix("DepthOfField.NearIntensity", 0))
        if e.get("InFocusRadius", 30) < b["dof_radius_min"]:
            fail(c, "DepthOfField.InFocusRadius %s below %s: the playfield is out of focus" % (fmt(e.get("InFocusRadius")), fmt(b["dof_radius_min"])), setfix("DepthOfField.InFocusRadius", 60))
        if e.get("FocusDistance", 0) < b["dof_focus_min"]:
            fail(c, "DepthOfField.FocusDistance %s below %s" % (fmt(e.get("FocusDistance")), fmt(b["dof_focus_min"])), setfix("DepthOfField.FocusDistance", 90))
    for e in enabled(state.get("blurs")):
        m["blur"].append(dict(Size=e.get("Size")))
        if e.get("Size", 0) > b["blur_max"]:
            fail(c, "BlurEffect.Size %s above %s: a menu blur left on during gameplay" % (fmt(e.get("Size")), fmt(b["blur_max"])), setfix("Blur.Size", 0))
    c["measured"] = m
    c["tolerance"] = dict(bloom_int_max=b["bloom_int_max"], bloom_thr_min=b["bloom_thr_min"], bloom_size_max=b["bloom_size_max"], bloom_index_max=b["bloom_index_max"],
                          cc_brightness=b["cc_brightness"], cc_contrast=b["cc_contrast"], cc_saturation=b["cc_saturation"], cc_tint_sat_max=b["cc_tint_sat_max"],
                          sunrays_int_max=b["sunrays_int_max"], dof_allowed=b["dof_allowed"], blur_max=b["blur_max"])
    return c


def l5(state, ctx):
    c = mk()
    b = ctx["bands"]
    lt = state["lighting"]
    parts = []
    atm = (state.get("atmospheres") or [None])[0]
    if atm and atm.get("Color"):
        parts.append(("Atmosphere.Color", atm["Color"]))
    cc = first_enabled(state.get("colorCorrections"))
    if cc and cc.get("TintColor"):
        parts.append(("ColorCorrection.TintColor", cc["TintColor"]))
    if lt.get("FogEnd", 100000) < 100000 and lt.get("FogColor"):
        parts.append(("Lighting.FogColor", lt["FogColor"]))
    if lt.get("OutdoorAmbient"):
        parts.append(("Lighting.OutdoorAmbient", lt["OutdoorAmbient"]))
    tints = []
    for name, col in parts:
        h, s, v = hsv(col)
        if s >= 0.12 and v >= 0.15:
            tints.append((name, h, s))
    worst, wa, wb = 0.0, None, None
    for i in range(len(tints)):
        for j in range(i + 1, len(tints)):
            d = hue_dist(tints[i][1], tints[j][1])
            if d > worst:
                worst, wa, wb = d, tints[i][0], tints[j][0]
    mean_hue = None
    if tints:
        sx = sum(math.cos(math.radians(h)) * s for _, h, s in tints)
        sy = sum(math.sin(math.radians(h)) * s for _, h, s in tints)
        mean_hue = math.degrees(math.atan2(sy, sx)) % 360.0
    c["measured"] = dict(tinted=[t[0] for t in tints], max_hue_spread=rnd(worst), mean_hue=None if mean_hue is None else rnd(mean_hue))
    c["tolerance"] = dict(hue_cohesion_deg=b["hue_cohesion_deg"], theme_hue_deg=b["theme_hue_deg"])
    if worst > b["hue_cohesion_deg"]:
        fail(c, "grading colours fight each other: %s and %s are %s degrees apart in hue (limit %s)" % (wa, wb, fmt(rnd(worst)), fmt(b["hue_cohesion_deg"])), preset_fix(ctx, "L5 cohesion"))
    theme = ctx.get("theme") or {}
    thues = []
    for k in sorted(theme.keys()):
        h, s, v = hsv(theme[k])
        if s >= 0.15 and v >= 0.15:
            thues.append((k, h))
    c["measured"]["theme_hues"] = [[k, rnd(h)] for k, h in thues]
    if not theme:
        c["unverified"].append("theme (no StyleKit Theme given: palette fit not checked, only internal cohesion)")
    elif mean_hue is not None and thues:
        best = min(hue_dist(mean_hue, h) for _, h in thues)
        comp = min(hue_dist(mean_hue, (h + 180.0) % 360.0) for _, h in thues)
        c["measured"]["nearest_theme_hue_distance"] = rnd(best)
        c["measured"]["nearest_complement_distance"] = rnd(comp)
        if best > b["theme_hue_deg"] and comp > 30.0:
            fail(c, "world grading hue %s is %s degrees from every palette hue and not a complement: it clashes with the UI/art palette" % (fmt(rnd(mean_hue)), fmt(rnd(best))), preset_fix(ctx, "L5 palette"))
    return c


def l6(state, ctx):
    c = mk()
    b = ctx["bands"]
    st = ctx["stats"]
    shots = state.get("shots") or []
    c["tolerance"] = dict(luma_mean=b["luma_mean"], crushed_max=b["crushed_max"], blown_max=b["blown_max"], spread_min=b["spread_min"], min_samples=M["min_samples"])
    meas = dict(n=st["n"], method="estimate")
    if st["n"] >= M["min_samples"]:
        meas.update(mean=rnd(st["mean"]), p10=rnd(st["p10"]), p50=rnd(st["p50"]), p90=rnd(st["p90"]), spread=rnd(st["spread"]), crushed=rnd(st["crushed"]), blown=rnd(st["blown"]))
    if shots:
        sm = sum(s.get("mean", 0) for s in shots) / len(shots)
        sc = sum(s.get("crushed", 0) for s in shots) / len(shots)
        sb = sum(s.get("blown", 0) for s in shots) / len(shots)
        meas["screenshots"] = dict(count=len(shots), mean=rnd(sm), crushed=rnd(sc), blown=rnd(sb))
    c["measured"] = meas
    if st["n"] < M["min_samples"] and not shots:
        c["status"] = "skip"
        c["issues"].append("only %d scene sample(s) (need %d) and no screenshots: brightness cannot be judged" % (st["n"], M["min_samples"]))
        return c
    lo, hi = b["luma_mean"]
    ec = state["lighting"].get("ExposureCompensation", 0)
    mid = (lo + hi) / 2.0
    if st["n"] >= M["min_samples"]:
        mean = st["mean"]
        if mean < lo or mean > hi:
            stops = clamp(2.2 * math.log2(max(mid, 0.01) / max(mean, 0.01)) * 0.8, -2.0, 2.0)
            fail(c, "estimated mean brightness %s is %s (band %s-%s)" % (fmt(rnd(mean)), "crushed/too dark" if mean < lo else "blown/too bright", fmt(lo), fmt(hi)),
                 setfix("Lighting.ExposureCompensation", rnd(clamp(ec + stops, -1.5, 1.5)), "about %s stops" % fmt(rnd(stops))))
        if st["crushed"] > b["crushed_max"]:
            fail(c, "%s%% of the sampled surfaces are crushed black (limit %s%%)" % (fmt(rnd(st["crushed"] * 100)), fmt(rnd(b["crushed_max"] * 100))), preset_fix(ctx, "L6 crushed shadows: raise Ambient/OutdoorAmbient or add lights"))
        if st["blown"] > b["blown_max"]:
            fail(c, "%s%% of the sampled surfaces are blown white (limit %s%%)" % (fmt(rnd(st["blown"] * 100)), fmt(rnd(b["blown_max"] * 100))), setfix("Lighting.Brightness", rnd(clamp(state["lighting"].get("Brightness", 3) * 0.7, 0.5, 4)), "lower sun brightness"))
        if st["spread"] < b["spread_min"]:
            fail(c, "flat image: p90 - p10 = %s (needs %s): no light/shadow separation" % (fmt(rnd(st["spread"])), fmt(b["spread_min"])), preset_fix(ctx, "L6 flat"))
    if shots:
        sm = c["measured"]["screenshots"]
        if sm["mean"] < lo - 0.04 or sm["mean"] > hi + 0.04:
            fail(c, "screenshot mean luma %s outside %s-%s" % (fmt(sm["mean"]), fmt(lo - 0.04), fmt(hi + 0.04)), setfix("Lighting.ExposureCompensation", rnd(clamp(ec + clamp(2.2 * math.log2(max(mid, 0.01) / max(sm["mean"], 0.01)) * 0.8, -2.0, 2.0), -1.5, 1.5))))
        if sm["crushed"] > b["crushed_max"]:
            fail(c, "screenshots: %s%% crushed pixels (limit %s%%)" % (fmt(rnd(sm["crushed"] * 100)), fmt(rnd(b["crushed_max"] * 100))), preset_fix(ctx, "L6 shots crushed"))
        if sm["blown"] > b["blown_max"] + 0.05:
            fail(c, "screenshots: %s%% blown pixels (limit %s%%)" % (fmt(rnd(sm["blown"] * 100)), fmt(rnd((b["blown_max"] + 0.05) * 100))), preset_fix(ctx, "L6 shots blown"))
    return c


def l7(state, ctx):
    c = mk()
    lt = state["lighting"]
    ls = state.get("lightStats") or {}
    tech = lt.get("Technology")
    plat = ctx["platform"]
    maxs = COSTS["shadow_lights_mobile"] if plat == "mobile" else COSTS["shadow_lights_pc"]
    large, nocast = ls.get("largeParts", 0), ls.get("largePartsNoShadow", 0)
    frac = (nocast / large) if large else 0.0
    c["measured"] = dict(GlobalShadows=lt.get("GlobalShadows"), Technology=tech, shadow_lights=ls.get("shadowed", 0), key_lights=ls.get("keyTotal", 0),
                         key_unshadowed=ls.get("keyUnshadowed", 0), large_parts=large, large_parts_no_cast=nocast, large_no_cast_fraction=rnd(frac))
    c["tolerance"] = dict(GlobalShadows=True, max_shadow_lights=maxs, large_nocast_max=ctx["bands"]["large_nocast_max"])
    if lt.get("GlobalShadows") is False:
        fail(c, "Lighting.GlobalShadows is off: no sun shadows, the world looks flat", setfix("Lighting.GlobalShadows", True))
    if tech in ("Compatibility", "Legacy"):
        fail(c, "Technology %s has no dynamic shadows" % tech, setfix("Lighting.Technology", "ShadowMap" if plat == "mobile" else "Future"))
    if tech == "Voxel":
        c["warnings"].append("Technology Voxel: shadows are blocky; use Future (PC) or ShadowMap")
    if tech == "Future" and ls.get("keyUnshadowed", 0) > 0:
        fail(c, "%d key light(s) (Range >= 16, Brightness >= 1) have Shadows off" % ls["keyUnshadowed"], dict(action="setLights", property="Shadows", value=True, filter="key"))
    if ls.get("shadowed", 0) > maxs:
        fail(c, "%d shadow-casting lights (budget %d on %s): turn Shadows off on the least important" % (ls["shadowed"], maxs, plat), dict(action="setLights", property="Shadows", value=False, filter="smallest", keep=maxs))
    if frac > ctx["bands"]["large_nocast_max"]:
        fail(c, "%s%% of large parts have CastShadow off (limit %s%%)" % (fmt(rnd(frac * 100)), fmt(rnd(ctx["bands"]["large_nocast_max"] * 100))), dict(action="setParts", property="CastShadow", value=True, filter="large"))
    return c


def l8(state, ctx):
    c = mk()
    b = ctx["bands"]
    atm = (state.get("atmospheres") or [None])[0]
    marks = state.get("marks") or {}
    if not atm:
        c["status"] = "skip"
        c["issues"].append("no Atmosphere to judge (see L2)")
        return c
    c["measured"] = dict(genre=ctx["genre"], Density=atm.get("Density"), Haze=atm.get("Haze"), Offset=atm.get("Offset"), legacy_FogEnd=state["lighting"].get("FogEnd"))
    c["tolerance"] = dict(density=b["density"], haze=b["haze"])
    d, h = atm.get("Density", 0), atm.get("Haze", 0)
    if not ctx["genre"]:
        c["unverified"].append("genre (not given, generic bands used)")
    if rng(d, b["density"][0], b["density"][1]):
        fail(c, "Atmosphere.Density %s outside %s-%s for %s: %s" % (fmt(d), fmt(b["density"][0]), fmt(b["density"][1]), ctx["genre"] or "generic", "too thin, no depth" if d < b["density"][0] else "too thick, the playfield disappears"),
             setfix("Atmosphere.Density", rnd((b["density"][0] + b["density"][1]) / 2.0)))
    if rng(h, b["haze"][0], b["haze"][1]):
        fail(c, "Atmosphere.Haze %s outside %s-%s for %s" % (fmt(h), fmt(b["haze"][0]), fmt(b["haze"][1]), ctx["genre"] or "generic"), setfix("Atmosphere.Haze", clamp(h, b["haze"][0], b["haze"][1])))
    mp = canon(marks.get("preset"))
    if mp and ctx["genre"] and mp != ctx["genre"]:
        c["warnings"].append("scene was set up with the %s preset but the game genre is %s" % (mp, ctx["genre"]))
    return c


def l9(state, ctx):
    c = mk()
    b = ctx["bands"]
    st = ctx["stats"]
    f = st["indoor_fraction"]
    c["measured"] = dict(indoor_fraction=rnd(f), indoor_samples=st["indoor_n"], indoor_mean=None if st["indoor_mean"] is None else rnd(st["indoor_mean"]), indoor_lit_fraction=rnd(st["indoor_lit_fraction"]))
    c["tolerance"] = dict(applies_from_indoor_fraction=0.15, indoor_mean_min=b["interior_luma_min"], indoor_lit_fraction_min=0.3)
    if f < 0.15:
        return c
    if st["indoor_mean"] < b["interior_luma_min"]:
        fail(c, "interiors are too dark: mean estimated brightness %s (min %s)" % (fmt(rnd(st["indoor_mean"])), fmt(b["interior_luma_min"])), dict(action="addInteriorLights", note="PointLight/SpotLight/SurfaceLight in every room; raise Lighting.Ambient"))
    if st["indoor_lit_fraction"] < 0.3:
        fail(c, "only %s%% of interior samples are near a light source: rooms look flat" % fmt(rnd(st["indoor_lit_fraction"] * 100)), dict(action="addInteriorLights", note="a warm PointLight (Range 16-24, Shadows on) per room"))
    return c


def cost_of(state, platform_mobile=False):
    lt = state["lighting"]
    ls = state.get("lightStats") or {}
    cost = COSTS["technology"].get(lt.get("Technology"), 0)
    if platform_mobile and lt.get("Technology") == "Future":
        pass
    for key, ck in (("blooms", "bloom"), ("colorCorrections", "colorCorrection"), ("sunRays", "sunRays"), ("dofs", "depthOfField"), ("blurs", "blur")):
        for e in enabled(state.get(key)):
            cost += COSTS[ck]
            if ck == "bloom" and e.get("Size", 24) > COSTS["bloom_big_size"]:
                cost += COSTS["bloom_big"]
    if state.get("atmospheres"):
        cost += COSTS["atmosphere"]
    sh = ls.get("shadowed", 0)
    plain = max(0, ls.get("total", 0) - sh)
    cost += sh * (COSTS["shadow_light_future"] if lt.get("Technology") == "Future" else COSTS["shadow_light"]) + plain * COSTS["plain_light"]
    return cost


def mobile_state(state):
    """What the same scene costs with the mobile-safe variant of the engine settings (Future -> ShadowMap, no DOF, no SunRays)."""
    s = copy.deepcopy(state)
    if s["lighting"].get("Technology") == "Future":
        s["lighting"]["Technology"] = "ShadowMap"
    s["dofs"] = []
    s["sunRays"] = []
    return s


def l10(state, ctx):
    c = mk()
    plat = ctx["platform"]
    ls = state.get("lightStats") or {}
    cost = cost_of(state)
    mcost = cost_of(mobile_state(state))
    budget = COSTS["budget_mobile"] if plat == "mobile" else COSTS["budget_pc"]
    c["measured"] = dict(platform=plat, cost=rnd(cost), cost_mobile_variant=rnd(mcost), shadow_lights=ls.get("shadowed", 0), lights=ls.get("total", 0),
                         effects_on=len(enabled(state.get("blooms"))) + len(enabled(state.get("colorCorrections"))) + len(enabled(state.get("sunRays"))) + len(enabled(state.get("dofs"))) + len(enabled(state.get("blurs"))))
    c["tolerance"] = dict(budget=budget, budget_mobile=COSTS["budget_mobile"], budget_pc=COSTS["budget_pc"], max_shadow_lights_mobile=COSTS["shadow_lights_mobile"])
    if cost > budget:
        fail(c, "lighting cost %s above the %s budget %s (Technology + effects + lights)" % (fmt(rnd(cost)), plat, fmt(budget)), dict(action="applyPreset", preset=ctx["genre"] or "(choose a genre)", time=ctx["time"], mobile=True, note="mobile-safe variant"))
    if plat == "mobile":
        if enabled(state.get("dofs")):
            fail(c, "DepthOfField on a mobile target", dict(action="remove", target="DepthOfField"))
        if enabled(state.get("sunRays")):
            fail(c, "SunRays on a mobile target", dict(action="remove", target="SunRays"))
        if ls.get("shadowed", 0) > COSTS["shadow_lights_mobile"]:
            fail(c, "%d shadow-casting lights on a mobile target (max %d)" % (ls["shadowed"], COSTS["shadow_lights_mobile"]), dict(action="setLights", property="Shadows", value=False, filter="smallest", keep=COSTS["shadow_lights_mobile"]))
    elif mcost > COSTS["budget_mobile"]:
        c["warnings"].append("on phones this scene costs %s (mobile budget %s): offer LightingKit.apply(preset, {mobile = true}) to low-end clients" % (fmt(rnd(mcost)), fmt(COSTS["budget_mobile"])))
    return c


def l11(state, ctx):
    c = mk()
    groups = (("Atmosphere", "atmospheres", False), ("Sky", "skies", False), ("Bloom", "blooms", True), ("ColorCorrection", "colorCorrections", True),
              ("SunRays", "sunRays", True), ("DepthOfField", "dofs", True), ("Blur", "blurs", True))
    counts = {}
    for name, key, only_enabled in groups:
        lst = enabled(state.get(key)) if only_enabled else (state.get(key) or [])
        counts[name] = len(lst)
        if len(lst) > 1:
            fail(c, "%d %s objects%s: only one should exist (paths: %s)" % (len(lst), name, " enabled" if only_enabled else "", ", ".join(str(x.get("path", "?")) for x in lst)), dict(action="remove", target=name, keep=1))
    lt = state["lighting"]
    if state.get("atmospheres") and lt.get("FogEnd", 100000) < 5000:
        fail(c, "Lighting.FogEnd %s (legacy fog) is set while an Atmosphere exists: two haze systems fight" % fmt(lt.get("FogEnd")), setfix("Lighting.FogEnd", 100000))
    c["measured"] = dict(counts=counts, FogEnd=lt.get("FogEnd", 100000))
    c["tolerance"] = dict(max_per_class=1, legacy_fog_with_atmosphere=False)
    return c


def l12(state, ctx):
    c = mk()
    b = ctx["bands"]
    lt = state["lighting"]
    amb = luma255(lt["OutdoorAmbient"])
    ex = lt.get("ExposureCompensation", 0)
    c["measured"] = dict(ClockTime=lt.get("ClockTime"), sun_elevation=rnd(ctx["elev"]), phase=ctx["phase"], outdoor_ambient_luma=rnd(amb), ExposureCompensation=ex, Brightness=lt.get("Brightness"))
    c["tolerance"] = dict(amb_outdoor=b["amb_outdoor"], exposure=b["exposure"])
    if rng(amb, b["amb_outdoor"][0], b["amb_outdoor"][1]):
        why = "too bright for %s" % ctx["phase"] if amb > b["amb_outdoor"][1] else "too dark for %s" % ctx["phase"]
        fail(c, "OutdoorAmbient luma %s is %s (band %s-%s): time of day and ambient disagree" % (fmt(rnd(amb)), why, fmt(b["amb_outdoor"][0]), fmt(b["amb_outdoor"][1])), preset_fix(ctx, "L12 ambient vs time"))
    if rng(ex, b["exposure"][0], b["exposure"][1]):
        fail(c, "ExposureCompensation %s outside %s to %s" % (fmt(ex), fmt(b["exposure"][0]), fmt(b["exposure"][1])), setfix("Lighting.ExposureCompensation", clamp(ex, b["exposure"][0], b["exposure"][1])))
    if ctx["phase"] == "night" and lt.get("Brightness", 3) > 3.5:
        fail(c, "Brightness %s on a night scene: the moon would light it like noon" % fmt(lt.get("Brightness")), setfix("Lighting.Brightness", 1.5))
    return c


CHECK_FUNCS = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]


def normalize_state(state):
    """Fill the required lighting properties with the Roblox defaults so a partial state cannot crash a check."""
    s = copy.deepcopy(state)
    lt = s.setdefault("lighting", {})
    for k, v in (("Technology", "ShadowMap"), ("Brightness", 3), ("ClockTime", 14.5), ("GeographicLatitude", 41.7333), ("Ambient", [70, 70, 70]), ("OutdoorAmbient", [70, 70, 70]),
                 ("ColorShift_Top", [0, 0, 0]), ("ColorShift_Bottom", [0, 0, 0]), ("EnvironmentDiffuseScale", 1), ("EnvironmentSpecularScale", 1),
                 ("ExposureCompensation", 0), ("GlobalShadows", True), ("ShadowSoftness", 0.2), ("FogEnd", 100000)):
        if k not in lt:
            lt[k] = v
    return s


def verify(state, cfg=None):
    cfg = cfg or {}
    state = normalize_state(state)
    marks = state.get("marks") or {}
    genre = canon(cfg.get("genre")) or canon(marks.get("preset"))
    elev, _ = sun_info(state["lighting"])
    phase = phase_of(elev)
    platform = cfg.get("platform") or "both"
    ctx = dict(genre=genre, time=cfg.get("time") or phase_time(phase), phase=phase, elev=elev, platform=platform, bands=bands(genre, phase), theme=cfg.get("theme"), stats=scene_stats(state))
    for k, v in (cfg.get("bands") or {}).items():
        ctx["bands"][k] = v
    checks = {}
    for fn, cid in zip(CHECK_FUNCS, ORDER):
        r = fn(state, ctx)
        r["name"] = NAMES[cid]
        checks[cid] = r
    waive = cfg.get("waive") or {}
    failed, waived, unverified, warnings = [], [], [], []
    for cid in ORDER:
        c = checks[cid]
        if c["status"] == "fail" and cid in waive:
            reason = str(waive[cid]).strip()
            if len(reason) >= MIN_WAIVER:
                c["waived"] = reason
                waived.append(cid)
                continue
            c["issues"].append("waiver of %s has no real reason (>= %d characters)" % (cid, MIN_WAIVER))
        if c["status"] == "fail":
            failed.append(cid)
        for u in c["unverified"]:
            unverified.append("%s: %s" % (cid, u))
        for w in c["warnings"]:
            warnings.append("%s: %s" % (cid, w))
    skipped = [cid for cid in ORDER if checks[cid]["status"] == "skip"]
    rep = dict(kind="lighting-report", version=1, genre=genre, time=ctx["time"], phase=phase, platform=platform,
               status="fail" if failed else "pass", failed=failed, waived=waived, skipped=skipped, unverified=unverified, warnings=warnings, checks=checks,
               summary=dict(sun_elevation=rnd(elev), cost=checks["L10"]["measured"]["cost"], cost_mobile_variant=checks["L10"]["measured"]["cost_mobile_variant"]))
    return rep


def phase_time(phase):
    return {"day": "day", "dusk": "golden", "night": "night"}[phase]


if __name__ == "__main__":
    import sys
    d = json.load(open(sys.argv[1], encoding="utf-8-sig"))
    print(json.dumps(verify(d["state"], d.get("cfg")), indent=1))
