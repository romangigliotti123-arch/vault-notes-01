#!/usr/bin/env python3
"""make_fixtures.py: writes tests/fixtures.json (the lighting cases both cores must agree on).
  python make_fixtures.py           write
  python make_fixtures.py --check   exit 1 when fixtures.json is out of date
Each case: {name, state, cfg, expect: {Lx: status}, status, num: {"L10.measured.cost": 6.75}, fix: {Lx: action}, warn: [substring], unverified: [substring]}.
`expect`, `status`, `num`, `fix` are written by hand below (independent of lighting_ref.py); the test runs both cores and compares them with these AND with each other.
The states are built from the real presets (lighting_ref.resolve) so the 'passing' cases are the shipped presets themselves.
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import lighting_ref as R  # noqa: E402

THEME = {"bg": [24, 32, 56], "panel": [44, 62, 108], "accent": [255, 196, 61], "accent2": [64, 200, 190]}
OUTDOOR = [  # (albedo, normal, lit)
    ((0.36, 0.58, 0.27), (0, 1, 0), True), ((0.36, 0.58, 0.27), (0, 1, 0), False), ((0.78, 0.68, 0.5), (0, 1, 0), True), ((0.55, 0.55, 0.58), (0, 1, 0), True),
    ((0.7, 0.55, 0.4), (0.7, 0, 0.7), True), ((0.7, 0.55, 0.4), (-0.7, 0, -0.7), True), ((0.3, 0.2, 0.12), (0, 1, 0), True), ((0.2, 0.4, 0.85), (0, 1, 0), True),
    ((0.8, 0.2, 0.2), (0, 1, 0), True), ((0.92, 0.92, 0.92), (0, 1, 0), True), ((0.1, 0.1, 0.1), (0, 1, 0), True), ((0.45, 0.45, 0.45), (0, 1, 0), False),
    ((0.6, 0.7, 0.3), (0, 1, 0), True), ((0.5, 0.5, 0.5), (1, 0, 0), True), ((0.5, 0.5, 0.5), (-1, 0, 0), True), ((0.5, 0.5, 0.5), (0, 0, 1), True),
]
INDOOR = [((0.55, 0.4, 0.28), (0, 1, 0)), ((0.7, 0.68, 0.62), (0, 1, 0)), ((0.5, 0.5, 0.52), (1, 0, 0)), ((0.6, 0.45, 0.3), (0, 1, 0)),
          ((0.4, 0.32, 0.25), (-1, 0, 0)), ((0.65, 0.6, 0.55), (0, 1, 0)), ((0.5, 0.42, 0.35), (0, 0, 1)), ((0.58, 0.5, 0.4), (0, 1, 0))]


def samples(indoor=0, light=0.0, lit_every=1):
    out = [dict(albedo=list(a), n=list(n), lit=lit, indoor=False, emissive=False, lightE=0.0) for a, n, lit in OUTDOOR]
    for i, (a, n) in enumerate(INDOOR[:indoor]):
        out.append(dict(albedo=list(a), n=list(n), lit=False, indoor=True, emissive=False, lightE=light if (light and i % lit_every == 0) else 0.0))
    return out


def state_from(res, smp=None, ls=None):
    d = copy.deepcopy(res["desired"])
    st = dict(lighting=d["lighting"], atmospheres=[], skies=[], blooms=[], colorCorrections=[], sunRays=[], dofs=[], blurs=[])
    if d.get("atmosphere"):
        st["atmospheres"] = [dict(d["atmosphere"], path="Lighting.Atmosphere")]
    if d.get("sky"):
        st["skies"] = [dict(R.DATA["sky_default_textures"], **d["sky"], path="Lighting.Sky")]
    for k, key, nm in (("bloom", "blooms", "Bloom"), ("colorCorrection", "colorCorrections", "ColorCorrection"), ("sunRays", "sunRays", "SunRays"), ("depthOfField", "dofs", "DepthOfField")):
        if d.get(k):
            st[key] = [dict(d[k], path="Lighting." + nm, Enabled=True)]
    st["lightStats"] = ls or dict(total=0, shadowed=0, keyTotal=0, keyUnshadowed=0, largeParts=10, largePartsNoShadow=0)
    st["samples"] = smp if smp is not None else samples()
    st["marks"] = dict(preset=res["preset"], time=res["time"], mobile=res["mobile"])
    return st


def base(genre, time=None, mobile=False, **kw):
    return state_from(R.resolve(genre, time, mobile), **kw)


def scan_for(genre, scorer="critic", captured_at="2026-11-04T10:00:00Z", platform="both"):
    """A complete, passing lighting-scan dict for a shipped preset (used by the integration tests of the gates; real scans come from LightingKit.scan)."""
    st = base(genre)
    cfg = dict(genre=genre, platform=platform, theme=THEME)
    return dict(kind="lighting-scan", version=1, game="demo", scorer=scorer, datamodel="Edit", captured_at=captured_at, config=cfg, state=st, report=R.verify(st, cfg))


def case(name, state, cfg=None, expect=None, status=None, num=None, fix=None, warn=None, unverified=None):
    return dict(name=name, state=copy.deepcopy(state), cfg=copy.deepcopy(cfg) if cfg else {}, expect=expect or {}, status=status, num=num or {}, fix=fix or {}, warn=warn or [], unverified=unverified or [])


def build():
    cases = []
    cfgs = lambda g, **kw: dict(genre=g, theme=THEME, **kw)  # noqa: E731
    # ---- every shipped preset passes at every time of day, PC and mobile variant
    for g in R.PRESETS:
        for t in ("day", "golden", "night"):
            for mob in (False, True):
                st = base(g, t, mob)
                cases.append(case("pass: %s preset, %s, %s" % (g, t, "mobile variant" if mob else "PC"), st, cfgs(g, platform="mobile" if mob else "both"), status="pass"))
    # ---- default Roblox lighting
    dflt = dict(lighting=dict(Technology="ShadowMap", Brightness=3, ClockTime=14.5, GeographicLatitude=41.7333, Ambient=[70, 70, 70], OutdoorAmbient=[70, 70, 70], ColorShift_Top=[0, 0, 0],
                              ColorShift_Bottom=[0, 0, 0], EnvironmentDiffuseScale=1, EnvironmentSpecularScale=1, ExposureCompensation=0, GlobalShadows=True, ShadowSoftness=0.2, FogEnd=100000),
                atmospheres=[], skies=[], blooms=[], colorCorrections=[], sunRays=[], dofs=[], blurs=[], lightStats=dict(total=0, shadowed=0, keyTotal=0, keyUnshadowed=0, largeParts=10, largePartsNoShadow=0),
                samples=samples())
    cases.append(case("fail: untouched default Roblox lighting", copy.deepcopy(dflt), cfgs("obby"), expect=dict(L1="fail", L2="fail", L3="fail", L8="skip", L11="pass", L7="pass"), status="fail",
                      num={"L1.measured.changed": 0, "L1.measured.tracked": 9}, fix=dict(L1="applyPreset", L2="applyPreset", L3="applyPreset")))
    st = copy.deepcopy(dflt)
    st["lighting"]["Technology"] = "Voxel"
    cases.append(case("fail: default lighting with Voxel technology and no genre", st, {}, expect=dict(L1="fail"), status="fail", warn=["Technology Voxel"]))
    # ---- bloom blown out
    st = base("obby")
    st["blooms"][0].update(Intensity=3.0, Size=56, Threshold=0.3)
    cases.append(case("fail: blown-out bloom", st, cfgs("obby"), expect=dict(L4="fail", L1="pass", L2="pass", L6="pass"), status="fail", fix=dict(L4="set")))
    st = base("obby")
    st["blooms"][0].update(Intensity=1.1, Size=40, Threshold=0.8)
    cases.append(case("fail: strong bloom index (intensity x size / threshold) above the limit", st, cfgs("obby"), expect=dict(L4="fail"), status="fail", num={"L4.measured.bloom.0.index": 2.292}))
    st = base("obby")
    st["blooms"][0].update(Intensity=0.9, Size=24, Threshold=0.9)
    cases.append(case("pass: bloom at the upper end of sane", st, cfgs("obby"), expect=dict(L4="pass"), status="pass"))
    # ---- crushed dark scene
    st = base("obby", "day")
    st["lighting"].update(ClockTime=0.5, Brightness=0.2, Ambient=[2, 2, 3], OutdoorAmbient=[3, 3, 4], EnvironmentDiffuseScale=0, ExposureCompensation=-1.0)
    cases.append(case("fail: crushed dark scene (night, no ambient, no environment light)", st, cfgs("obby"), expect=dict(L6="fail", L12="fail"), status="fail"))
    st = base("horror", "night")
    st["lighting"].update(Ambient=[0, 0, 0], OutdoorAmbient=[0, 0, 0], EnvironmentDiffuseScale=0, ExposureCompensation=-1.5)
    cases.append(case("fail: pitch-black horror scene", st, cfgs("horror"), expect=dict(L6="fail"), status="fail"))
    # ---- blown scene
    st = base("simulator", "day")
    st["lighting"].update(Brightness=8, ExposureCompensation=1.5)
    st["colorCorrections"][0].update(Brightness=0.12)
    cases.append(case("fail: blown-out bright scene", st, cfgs("simulator"), expect=dict(L6="fail"), status="fail"))
    st = base("simulator", "day")
    st["lighting"].update(Ambient=[200, 200, 200], OutdoorAmbient=[210, 210, 210], ExposureCompensation=1.0)
    cases.append(case("fail: ambient washes out the image (flat and bright)", st, cfgs("simulator"), expect=dict(L6="fail", L12="fail"), status="fail"))
    # ---- missing atmosphere / sky
    st = base("cartoony")
    st["atmospheres"] = []
    cases.append(case("fail: missing Atmosphere", st, cfgs("cartoony"), expect=dict(L2="fail", L8="skip", L1="pass", L3="pass"), status="fail", fix=dict(L2="applyPreset")))
    st = base("cartoony")
    st["skies"] = []
    cases.append(case("fail: missing Sky", st, cfgs("cartoony"), expect=dict(L3="fail", L2="pass"), status="fail", fix=dict(L3="applyPreset")))
    st = base("cartoony")
    st["skies"][0]["SkyboxBk"] = ""
    st["skies"][0]["SkyboxUp"] = ""
    cases.append(case("fail: Sky with empty textures", st, cfgs("cartoony"), expect=dict(L3="fail"), status="fail", num={"L3.measured.default_textures": 4}))
    cases.append(case("warn: default Sky textures are a warning, not a failure", base("cartoony"), cfgs("cartoony"), expect=dict(L3="pass"), status="pass", warn=["default Roblox textures"]))
    st = base("cartoony")
    st["skies"][0].update(SkyboxBk="rbxassetid://1", SkyboxDn="rbxassetid://2", SkyboxFt="rbxassetid://3", SkyboxLf="rbxassetid://4", SkyboxRt="rbxassetid://5", SkyboxUp="rbxassetid://6")
    cases.append(case("pass: custom sky (six textures, fixture ids only)", st, cfgs("cartoony"), expect=dict(L3="pass"), status="pass", num={"L3.measured.default_textures": 0}))
    # ---- extreme post effects
    st = base("obby")
    st["colorCorrections"][0].update(Contrast=0.9, Saturation=1.2, Brightness=0.4)
    cases.append(case("fail: extreme ColorCorrection contrast and saturation", st, cfgs("obby"), expect=dict(L4="fail"), status="fail"))
    st = base("obby")
    st["colorCorrections"][0]["TintColor"] = [255, 120, 120]
    cases.append(case("fail: heavy ColorCorrection tint", st, cfgs("obby"), expect=dict(L4="fail", L5="fail"), status="fail"))
    st = base("obby")
    st["sunRays"][0].update(Intensity=0.9, Spread=1.0)
    cases.append(case("fail: SunRays too strong", st, cfgs("obby"), expect=dict(L4="fail"), status="fail"))
    st = base("tower_defense")
    st["dofs"] = [dict(path="Lighting.DepthOfField", Enabled=True, FarIntensity=0.1, NearIntensity=0, FocusDistance=90, InFocusRadius=60)]
    cases.append(case("fail: depth of field in a tower defense (needs a sharp playfield)", st, cfgs("tower_defense"), expect=dict(L4="fail"), status="fail"))
    st = base("open_world")
    st["dofs"][0].update(FarIntensity=0.9, InFocusRadius=5, FocusDistance=10)
    cases.append(case("fail: depth of field blurs the playfield", st, cfgs("open_world"), expect=dict(L4="fail"), status="fail"))
    st = base("obby")
    st["blurs"] = [dict(path="Lighting.Blur", Enabled=True, Size=24)]
    cases.append(case("fail: menu blur left on during gameplay", st, cfgs("obby"), expect=dict(L4="fail", L10="pass"), status="fail"))
    st = base("obby")
    st["blurs"] = [dict(path="Lighting.Blur", Enabled=False, Size=24)]
    cases.append(case("pass: disabled blur is ignored", st, cfgs("obby"), expect=dict(L4="pass", L11="pass"), status="pass"))
    # ---- palette cohesion
    st = base("cartoony")
    st["atmospheres"][0]["Color"] = [120, 220, 120]
    st["colorCorrections"][0]["TintColor"] = [255, 215, 215]
    cases.append(case("fail: atmosphere green and grading red fight each other", st, cfgs("cartoony"), expect=dict(L5="fail"), status="fail"))
    st = base("cartoony")
    st["atmospheres"][0]["Color"] = [130, 235, 120]
    st["lighting"]["OutdoorAmbient"] = [140, 200, 130]
    st["colorCorrections"][0]["TintColor"] = [235, 255, 235]
    cases.append(case("fail: green world grading clashes with the blue/yellow UI palette", st, cfgs("cartoony"), expect=dict(L5="fail"), status="fail"))
    cases.append(case("note: no theme given, palette fit is unverified but the check passes", base("cartoony"), dict(genre="cartoony"), expect=dict(L5="pass"), status="pass", unverified=["L5: theme"]))
    # ---- shadows
    st = base("obby")
    st["lighting"]["GlobalShadows"] = False
    cases.append(case("fail: GlobalShadows off", st, cfgs("obby"), expect=dict(L7="fail"), status="fail"))
    st = base("obby")
    st["lighting"]["Technology"] = "Compatibility"
    cases.append(case("fail: Compatibility technology has no shadows", st, cfgs("obby"), expect=dict(L7="fail"), status="fail"))
    st = base("obby")
    st["lightStats"] = dict(total=5, shadowed=2, keyTotal=4, keyUnshadowed=2, largeParts=10, largePartsNoShadow=0)
    cases.append(case("fail: key lights without shadows under Future lighting", st, cfgs("obby"), expect=dict(L7="fail"), status="fail", fix=dict(L7="setLights")))
    st = base("obby", "day", True)
    st["lightStats"] = dict(total=8, shadowed=5, keyTotal=5, keyUnshadowed=0, largeParts=10, largePartsNoShadow=0)
    cases.append(case("fail: too many shadow-casting lights on mobile", st, cfgs("obby", platform="mobile"), expect=dict(L7="fail", L10="fail"), status="fail"))
    st = base("obby")
    st["lightStats"] = dict(total=0, shadowed=0, keyTotal=0, keyUnshadowed=0, largeParts=20, largePartsNoShadow=14)
    cases.append(case("fail: most large parts have CastShadow off", st, cfgs("obby"), expect=dict(L7="fail"), status="fail", fix=dict(L7="setParts")))
    st = base("obby")
    st["lighting"]["Technology"] = "Voxel"
    cases.append(case("warn: Voxel technology passes shadows but warns", st, cfgs("obby"), expect=dict(L7="pass"), status="pass", warn=["blocky"]))
    # ---- fog / density per genre
    st = base("horror")
    st["atmospheres"][0].update(Density=0.1, Haze=0.2)
    cases.append(case("fail: thin fog in a horror game", st, cfgs("horror"), expect=dict(L8="fail"), status="fail", fix=dict(L8="set")))
    st = base("cartoony")
    st["atmospheres"][0].update(Density=0.6, Haze=2.5)
    cases.append(case("fail: thick fog in a cartoony game", st, cfgs("cartoony"), expect=dict(L8="fail"), status="fail"))
    st = base("horror")
    cases.append(case("pass: the same horror atmosphere is fine for horror, wrong for obby", st, cfgs("horror"), expect=dict(L8="pass"), status="pass"))
    cases.append(case("fail: horror scene judged as an obby (density too thick, too dark)", st, cfgs("obby"), expect=dict(L8="fail"), status="fail"))
    st = base("obby")
    st.pop("marks")
    st["atmospheres"][0].update(Density=0.9)
    cases.append(case("note: no genre uses generic bands and says so", st, {}, expect=dict(L8="fail"), status="fail", unverified=["L8: genre"]))
    st = base("obby")
    cases.append(case("warn: preset of another genre is flagged", st, cfgs("horror"), expect=dict(L8="fail"), status="fail", warn=["obby preset"]))
    # ---- interiors
    st = base("simulator", smp=samples(indoor=8, light=0.0))
    cases.append(case("fail: dark interiors with no lights", st, cfgs("simulator"), expect=dict(L9="fail"), status="fail", fix=dict(L9="addInteriorLights")))
    st = base("simulator", smp=samples(indoor=8, light=1.5))
    cases.append(case("pass: lit interiors", st, cfgs("simulator"), expect=dict(L9="pass"), status="pass", num={"L9.measured.indoor_lit_fraction": 1.0}))
    st = base("simulator", smp=samples(indoor=2, light=0.0))
    cases.append(case("pass: a closet does not need lights (indoor share under 15%)", st, cfgs("simulator"), expect=dict(L9="pass"), status="pass"))
    st = base("simulator", smp=samples(indoor=8, light=1.5, lit_every=4))
    cases.append(case("fail: only a quarter of the interior is near a light", st, cfgs("simulator"), expect=dict(L9="fail"), status="fail"))
    # ---- performance budget
    st = base("open_world")
    st["blooms"][0]["Size"] = 40
    st["blurs"] = [dict(path="Lighting.Blur", Enabled=True, Size=2)]
    st["lightStats"] = dict(total=40, shadowed=6, keyTotal=6, keyUnshadowed=0, largeParts=10, largePartsNoShadow=0)
    cases.append(case("fail: PC budget exceeded (Future + DOF + SunRays + blur + 6 shadow lights)", st, cfgs("open_world"), expect=dict(L10="fail"), status="fail", fix=dict(L10="applyPreset")))
    st = base("open_world")
    cases.append(case("fail: depth of field and sun rays on a mobile target", st, cfgs("open_world", platform="mobile"), expect=dict(L10="fail"), status="fail"))
    cases.append(case("num: open_world PC cost 8.75, its mobile variant 3.75", base("open_world"), cfgs("open_world"), expect=dict(L10="pass"), status="pass", num={"L10.measured.cost": 8.75, "L10.measured.cost_mobile_variant": 3.75}))
    st = base("obby")
    st["sunRays"] = []
    st["lightStats"] = dict(total=52, shadowed=2, keyTotal=2, keyUnshadowed=0, largeParts=10, largePartsNoShadow=0)
    cases.append(case("warn: heavy light count passes on PC but is reported for phones", st, cfgs("obby"), expect=dict(L10="pass"), status="pass", warn=["on phones"], num={"L10.measured.cost": 11.25, "L10.measured.cost_mobile_variant": 8.25}))
    cases.append(case("pass: obby cost is 6.75 (Future 4 + bloom 1 + colour 0.25 + rays 1 + atmosphere 0.5)", base("obby"), cfgs("obby"), expect=dict(L10="pass"), status="pass", num={"L10.measured.cost": 6.75}))
    # ---- duplicates and conflicts
    st = base("obby")
    st["atmospheres"].append(dict(st["atmospheres"][0], path="Camera.Atmosphere"))
    cases.append(case("fail: two Atmosphere objects", st, cfgs("obby"), expect=dict(L11="fail", L2="fail"), status="fail", fix=dict(L11="remove")))
    st = base("obby")
    st["blooms"].append(dict(st["blooms"][0], path="Camera.Bloom"))
    st["colorCorrections"].append(dict(st["colorCorrections"][0], path="Lighting.ColorCorrection2"))
    cases.append(case("fail: duplicate Bloom and ColorCorrection", st, cfgs("obby"), expect=dict(L11="fail"), status="fail"))
    st = base("obby")
    st["blooms"].append(dict(st["blooms"][0], path="Camera.Bloom", Enabled=False))
    cases.append(case("pass: a disabled duplicate is not a conflict", st, cfgs("obby"), expect=dict(L11="pass"), status="pass"))
    st = base("obby")
    st["lighting"].update(FogEnd=300, FogStart=20)
    cases.append(case("fail: legacy fog with an Atmosphere", st, cfgs("obby"), expect=dict(L11="fail"), status="fail", fix=dict(L11="set")))
    # ---- time of day
    st = base("obby", "day")
    st["lighting"]["ClockTime"] = 23.5
    cases.append(case("fail: midnight with the daytime ambient", st, cfgs("obby"), expect=dict(L12="fail"), status="fail"))
    st = base("obby", "night")
    st["lighting"]["Brightness"] = 5
    cases.append(case("fail: night scene with sun brightness 5", st, cfgs("obby"), expect=dict(L12="fail"), status="fail"))
    st = base("obby", "day")
    st["lighting"]["ExposureCompensation"] = 3
    cases.append(case("fail: exposure compensation +3", st, cfgs("obby"), expect=dict(L12="fail"), status="fail"))
    # ---- screenshots and samples
    st = base("obby")
    st["samples"] = []
    cases.append(case("skip: no samples and no screenshots, brightness cannot be judged", st, cfgs("obby"), expect=dict(L6="skip"), status="pass"))
    st["shots"] = [dict(mean=0.5, crushed=0.02, blown=0.03), dict(mean=0.52, crushed=0.01, blown=0.04)]
    cases.append(case("pass: screenshots alone can carry the brightness check", st, cfgs("obby"), expect=dict(L6="pass"), status="pass", num={"L6.measured.screenshots.count": 2}))
    st["shots"] = [dict(mean=0.06, crushed=0.7, blown=0.0)]
    cases.append(case("fail: dark screenshots", st, cfgs("obby"), expect=dict(L6="fail"), status="fail"))
    st["shots"] = [dict(mean=0.9, crushed=0.0, blown=0.4)]
    cases.append(case("fail: blown screenshots", st, cfgs("obby"), expect=dict(L6="fail"), status="fail"))
    st = base("obby")
    st["samples"] = [dict(albedo=[0.5, 0.5, 0.5], n=[0, 1, 0], lit=True, indoor=False, emissive=False, lightE=0.0)] * 12
    cases.append(case("fail: a flat scene of one grey (no light/shadow separation)", st, cfgs("obby"), expect=dict(L6="fail"), status="fail"))
    # ---- waivers
    st = base("cartoony")
    st["atmospheres"][0]["Color"] = [120, 220, 120]
    st["colorCorrections"][0]["TintColor"] = [255, 215, 215]
    cases.append(case("waived: L5 failure with a real reason passes", st, cfgs("cartoony", waive=dict(L5="deliberate toxic-swamp look, approved in art-direction")), expect=dict(L5="fail"), status="pass"))
    cases.append(case("fail: waiver without a reason is refused", st, cfgs("cartoony", waive=dict(L5="meh")), expect=dict(L5="fail"), status="fail"))
    # ---- partial state must not crash
    cases.append(case("fail: an almost empty state still produces a report", dict(lighting={}), {}, expect=dict(L1="fail", L2="fail", L3="fail"), status="fail"))
    # ---- sun elevation / phase maths
    cases.append(case("num: noon at latitude 25 is day, sun elevation 65", base("obby"), cfgs("obby"), expect=dict(L12="pass"), status="pass", num={"L12.measured.phase": "day"}))
    st = base("obby")
    st["lighting"]["sunDir"] = [0.0, -0.5, 0.8]
    cases.append(case("num: a sun direction below the horizon overrides the clock (night)", st, cfgs("obby"), expect=dict(L12="fail"), num={"L12.measured.phase": "night"}))
    # ---- resolve fixtures
    res = []
    for g in list(R.PRESETS) + list(R.DATA["aliases"]):
        res.append(dict(preset=g))
    for g in R.PRESETS:
        for t in ("day", "golden", "night"):
            for mob in (False, True):
                res.append(dict(preset=g, time=t, mobile=mob))
    res.append(dict(preset="obby", time="night", overrides=dict(bloom=dict(Intensity=0.2), sunRays=False, sky=dict(SkyboxBk="rbxassetid://7"))))
    res.append(dict(preset="Sci-Fi", time="day", mobile=True, overrides=dict(lighting=dict(Brightness=2.2), atmosphere=dict(Color=[10, 20, 30]))))
    res.append(dict(preset="no such preset"))
    res.append(dict(preset="obby", time="noon"))
    return dict(version=1, cases=cases, resolve=res)


def main():
    text = json.dumps(build(), indent=0, sort_keys=True) + "\n"
    p = os.path.join(HERE, "fixtures.json")
    if "--check" in sys.argv:
        cur = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        sys.exit(0 if cur == text else 1)
    open(p, "w", encoding="utf-8", newline="\n").write(text)
    print("wrote", p, len(build()["cases"]), "cases")


if __name__ == "__main__":
    main()
