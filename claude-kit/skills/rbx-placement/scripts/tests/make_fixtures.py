#!/usr/bin/env python3
"""make_fixtures.py: writes fixtures.json, the shared test cases of the placement maths (floating, buried, tilted, wrong facing, overlapping,
misaligned stairs, mirrored pairs, junk, grid, bounds ... and the passing cases).

The EXPECTED results are written by hand below (not computed by the code under test). Both implementations must agree with them:
  python placement_ref.py (Python reference)  and  PlacementCore.luau (run under Lune by Placement.test.luau).
  python make_fixtures.py          rewrite fixtures.json
  python make_fixtures.py --check  exit 1 if fixtures.json is out of date
Case: {name, snap, intent, env, opts?, expect:{P1:"pass",...}, num?:{"P2.gap": 3.5, ...}, fix?:{"P2":"snapToGround"}, status}  (only the checks named in expect are asserted;
status = the overall model status: fail if any expected check is fail unless a waiver says otherwise).
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def rot(yaw=0.0, roll=0.0, pitch=0.0):
    """CFrame.Angles(pitch, yaw, roll) as the 9 components R00..R22 (Roblox YXZ order: yaw applied last)."""
    cy, sy = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))
    cx, sx = math.cos(math.radians(pitch)), math.sin(math.radians(pitch))
    cz, sz = math.cos(math.radians(roll)), math.sin(math.radians(roll))
    ry = [[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]
    rx = [[1, 0, 0], [0, cx, -sx], [0, sx, cx]]
    rz = [[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]]

    def mul(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

    m = mul(mul(ry, rx), rz)
    return [round(m[i][j], 9) for i in range(3) for j in range(3)]


def part(name, p, size, yaw=0.0, roll=0.0, pitch=0.0, anchored=True, collide=True, touch=True, transp=0.0, **kw):
    d = dict(name=name, p=list(p), r=rot(yaw, roll, pitch), size=list(size), anchored=anchored, anchoredAssembly=anchored, canCollide=collide,
             canTouch=touch, massless=False, transparency=transp, hasEffects=False)
    d.update(kw)
    return d


def snap(path, parts, cls="Model", pivot=None, primary=True, yaw=0.0, roll=0.0, pitch=0.0):  # noqa: E501
    piv = pivot or parts[0]["p"]
    return dict(path=path, **{"class": cls}, pivot=dict(p=list(piv), r=rot(yaw, roll, pitch)), hasPrimaryPart=primary, parts=parts)


def ground(y, path="Workspace.Map.Floor", n=(0, 1, 0), samples=5, ys=None):
    out = []
    for i in range(samples):
        yy = y if ys is None else ys[i]
        out.append(dict(x=0, z=0, y=yy, n=list(n), path=path))
    return dict(samples=out)


def nb(path, p, size, yaw=0.0, collide=True, transp=0.0):
    return dict(path=path, p=list(p), r=rot(yaw), size=list(size), canCollide=collide, transparency=transp)


CASES = []


def case(name, s, intent, env, expect, num=None, fix=None, opts=None, status=None):
    CASES.append(dict(name=name, snap=s, intent=intent, env=env, opts=opts or {}, expect=expect, num=num or {}, fix=fix or {},
                      status=status or ("fail" if "fail" in expect.values() else None)))


# ---- passing cases
door = snap("Workspace.Map.House.Door", [part("Panel", (10, 3.5, 0), (4, 7, 0.5))])
case("pass: door facing the walkable side on the 90 deg grid, resting on the floor, hosted by a wall",
     door,
     dict(kind="door", face=dict(target=[10, 3.5, -20]), at=[10, 3.5, 0], surfacePath="Workspace.Map.Floor", bounds=dict(min=[-500, -10, -500], max=[500, 100, 500])),
     dict(ground=ground(0), neighbours=[nb("Workspace.Map.House.WallFront", (10, 5, 0.1), (20, 10, 0.5)), nb("Workspace.Map.Floor", (0, -0.5, 0), (200, 1, 200))]),
     dict(P1="pass", P2="pass", P3="pass", P4="pass", P5="pass", P6="pass", P7="skip"), num={"P2.gap": 0.0, "P4.facingOffDeg": 0.0}, status="pass")

case("pass: tree with random yaw, trunk sunk 0.8 into the ground (kind tolerance 1.0)",
     snap("Workspace.Map.Tree1", [part("Trunk", (5, 9.2, 5), (2, 20, 2), yaw=33), part("Leaves", (5, 22, 5), (10, 8, 10), yaw=33)], pivot=(5, 9.2, 5), yaw=33),
     dict(kind="tree"), dict(ground=ground(0.0)), dict(P1="pass", P2="pass", P3="pass", P4="pass", P5="pass", P6="pass"), num={"P2.gap": -0.8}, status="pass")

case("pass: pickup floats on purpose and has no collision", snap("Workspace.Map.Coin", [part("Coin", (0, 6, 0), (1.5, 1.5, 0.2), collide=False)]),
     dict(kind="pickup"), dict(ground=ground(0)), dict(P1="pass", P2="skip", P3="pass", P6="pass"))

case("pass: crate on a 15 deg grid with expected size", snap("Workspace.Map.Crate1", [part("Box", (0, 1.5, 0), (3, 3, 3), yaw=45)], yaw=45),
     dict(kind="crate", expectedSize=[3, 3, 3], yawGrid=15), dict(ground=ground(0)), dict(P1="pass", P2="pass", P3="pass", P4="pass", P5="pass", P6="pass"), status="pass")

case("pass: the baseplate is a ground kind (not asked to rest on anything, any yaw)", snap("Workspace.Baseplate", [part("Baseplate", (0, -10, 0), (512, 20, 512), yaw=7)], pivot=(0, -10, 0), cls="Part", primary=True, yaw=7),
     dict(kind="ground", originOk=True), dict(), dict(P1="pass", P2="skip", P3="pass", P4="pass"))

# ---- P1
case("fail: pivot at the world origin by accident", snap("Workspace.Map.Lamp", [part("Pole", (0, 7, 0), (1, 14, 1))], pivot=(0, 0, 0)),
     dict(kind="lamp"), dict(ground=ground(0)), dict(P1="fail"))
case("pass: origin allowed when declared", snap("Workspace.Map.Lamp", [part("Pole", (0, 7, 0), (1, 14, 1))], pivot=(0, 7, 0)),
     dict(kind="lamp", originOk=True), dict(ground=ground(0)), dict(P1="pass"))
case("fail: Model without a PrimaryPart", snap("Workspace.Map.Crate2", [part("Box", (0, 1.5, 0), (3, 3, 3))], primary=False),
     dict(kind="crate"), dict(ground=ground(0)), dict(P1="fail"), fix=dict(P1="setPrimaryPart"))
case("fail: pivot far outside the model", snap("Workspace.Map.Crate3", [part("Box", (50, 1.5, 0), (3, 3, 3))], pivot=(0, 1.5, 0)),
     dict(kind="crate"), dict(ground=ground(0)), dict(P1="fail"))
case("fail: door 4x20x1 is far too tall for a door", snap("Workspace.Map.Door2", [part("Panel", (10, 10, 0), (4, 20, 1))]),
     dict(kind="door", face=dict(any=True)), dict(ground=ground(0)), dict(P1="fail"))
case("fail: expected size 4x7x1 but 8x7x1", snap("Workspace.Map.Door3", [part("Panel", (10, 3.5, 5), (8, 7, 1))]),
     dict(kind="door", expectedSize=[4, 7, 1], face=dict(any=True)), dict(ground=ground(0)), dict(P1="fail"))
case("fail: placed 6 studs from the intended position", snap("Workspace.Map.Crate4", [part("Box", (6, 1.5, 0), (3, 3, 3))]),
     dict(kind="crate", at=[0, 1.5, 0]), dict(ground=ground(0)), dict(P1="fail"), fix=dict(P1="moveBy"))
case("fail: off the 4 stud position grid", snap("Workspace.Map.Crate5", [part("Box", (9.5, 1.5, 8), (3, 3, 3))]),
     dict(kind="crate", posGrid=4), dict(ground=ground(0)), dict(P1="fail"), fix=dict(P1="moveBy"))
case("fail: degenerate zero-width model", snap("Workspace.Map.Flat", [part("Sheet", (0, 1, 20), (4, 0.01, 4))]),
     dict(), dict(ground=ground(0.5)), dict(P1="fail"))

# ---- P2
case("fail: floating 3.5 studs", snap("Workspace.Map.Crate6", [part("Box", (0, 5, 0), (3, 3, 3))]), dict(kind="crate"), dict(ground=ground(0)),
     dict(P2="fail"), num={"P2.gap": 3.5}, fix=dict(P2="snapToGround"))
case("fail: buried 1 stud", snap("Workspace.Map.Crate7", [part("Box", (0, 0.5, 0), (3, 3, 3))]), dict(kind="crate"), dict(ground=ground(0)),
     dict(P2="fail"), num={"P2.gap": -1.0}, fix=dict(P2="snapToGround"))
case("pass: floating flag turns the check off", snap("Workspace.Map.Hover", [part("Box", (0, 9, 0), (3, 3, 3))]), dict(kind="crate", floating=True), dict(ground=ground(0)),
     dict(P2="skip"))
case("fail: nothing below (void)", snap("Workspace.Map.Crate8", [part("Box", (0, 1.5, 0), (3, 3, 3))]), dict(kind="crate"),
     dict(ground=dict(samples=[dict(x=0, z=0)] * 5)), dict(P2="fail"))
case("fail: rests on the roof, not on the floor", snap("Workspace.Map.Crate9", [part("Box", (0, 11.5, 0), (3, 3, 3))]), dict(kind="crate", surfacePath="Workspace.Map.Floor"),
     dict(ground=ground(10, path="Workspace.Map.Roof")), dict(P2="fail"))
case("pass: within the 0.1 stud float tolerance", snap("Workspace.Map.Crate10", [part("Box", (0, 1.58, 0), (3, 3, 3))]), dict(kind="crate"), dict(ground=ground(0)),
     dict(P2="pass"))
case("fail: flatGround declared but ground varies 2 studs", snap("Workspace.Map.Crate11", [part("Box", (0, 3.5, 0), (3, 3, 3))]), dict(kind="crate", flatGround=True),
     dict(ground=ground(0, ys=[2, 0, 0, 0, 0])), dict(P2="fail"))
case("pass with warning: uneven ground, resting on the high side", snap("Workspace.Map.Crate12", [part("Box", (0, 3.5, 0), (3, 3, 3))]), dict(kind="crate"),
     dict(ground=ground(0, ys=[2, 0, 0, 0, 0])), dict(P2="pass"), num={"P2.spread": 2.0, "P2.gap": 0.0})

# ---- P3
case("fail: tilted 20 deg", snap("Workspace.Map.Crate13", [part("Box", (0, 1.5, 0), (3, 3, 3), roll=20)], roll=20), dict(kind="crate"), dict(ground=ground(0)),
     dict(P3="fail"), num={"P3.tiltDeg": 20.0}, fix=dict(P3="setUpright"))
case("fail: upside down", snap("Workspace.Map.Crate14", [part("Box", (0, 1.5, 0), (3, 3, 3), roll=180)], roll=180), dict(kind="crate"), dict(ground=ground(0)),
     dict(P3="fail"), num={"P3.tiltDeg": 180.0})
case("pass: intended 15 deg lean", snap("Workspace.Map.Tree2", [part("Trunk", (0, 8, 0), (2, 16, 2), roll=15)], roll=15), dict(kind="tree", tilt=dict(deg=15, tol=3)),
     dict(ground=ground(-2)), dict(P3="pass"))
case("fail: lean does not match the intended 15 deg", snap("Workspace.Map.Tree3", [part("Trunk", (0, 8, 0), (2, 16, 2), roll=30)], roll=30), dict(kind="tree", tilt=dict(deg=15, tol=3)),
     dict(ground=ground(-2)), dict(P3="fail"))
case("pass: rock aligned to a 20 deg slope normal", snap("Workspace.Map.Rock1", [part("Rock", (0, 2, 0), (4, 3, 4), roll=20)], roll=20),
     dict(kind="rock", alignToSurface=True), dict(ground=ground(0, n=(-math.sin(math.radians(20)), math.cos(math.radians(20)), 0))), dict(P3="pass"))
case("pass: tilt allowed", snap("Workspace.Map.Crate15", [part("Box", (0, 1.5, 0), (3, 3, 3), roll=40)], roll=40), dict(kind="crate", allowTilt=True), dict(ground=ground(0)),
     dict(P3="skip"))

# ---- P4
npc = lambda yaw: snap("Workspace.Map.Npc", [part("Root", (0, 3, 0), (2, 6, 1), yaw=yaw)], yaw=yaw)
case("fail: NPC faces away from the player area", npc(0), dict(kind="npc", face=dict(target=[0, 3, 20])), dict(ground=ground(0)), dict(P4="fail"),
     num={"P4.facingOffDeg": 180.0}, fix=dict(P4="rotateYaw"))
case("pass: NPC turned 180 faces +Z", npc(180), dict(kind="npc", face=dict(target=[0, 3, 20])), dict(ground=ground(0)), dict(P4="pass"))
case("fail: NPC with no declared facing", npc(0), dict(kind="npc"), dict(ground=ground(0)), dict(P4="fail"))
case("pass: NPC facing declared irrelevant", npc(0), dict(kind="npc", face=dict(any=True)), dict(ground=ground(0)), dict(P4="pass"))
case("pass: facing via env-resolved target within 15 deg", npc(10), dict(kind="npc", face=dict(target="Workspace.Map.Hub")), dict(ground=ground(0), faceTarget=[0, 3, -20]),
     dict(P4="pass"), num={"P4.facingOffDeg": 10.0})
case("fail: yaw 7 deg off the 15 deg grid", snap("Workspace.Map.Crate16", [part("Box", (0, 1.5, 0), (3, 3, 3), yaw=22)], yaw=22), dict(kind="crate"), dict(ground=ground(0)),
     dict(P4="fail"), num={"P4.yawGridDevDeg": 7.0}, fix=dict(P4="rotateYaw"))
case("pass: 22 deg is fine for a random-yaw rock", snap("Workspace.Map.Rock2", [part("Rock", (0, 1.5, 0), (3, 3, 3), yaw=22)], yaw=22), dict(kind="rock"), dict(ground=ground(0)),
     dict(P4="pass"))
case("fail: door a few degrees off the 90 deg grid", snap("Workspace.Map.Door4", [part("Panel", (10, 3.5, 0), (4, 7, 0.5), yaw=4)], yaw=4),
     dict(kind="door", face=dict(target=[10, 3.5, -20], tol=20)), dict(ground=ground(0)), dict(P4="fail"), fix=dict(P4="rotateYaw"))
case("fail: front vector points up (model lying on its back)", snap("Workspace.Map.Sign1", [part("Board", (0, 1, 0), (4, 3, 0.3), pitch=90)], pitch=90),
     dict(kind="sign", face=dict(any=True)), dict(ground=ground(0)), dict(P4="fail"))
case("pass: custom front face (Back) used for facing", snap("Workspace.Map.Chair1", [part("Seat", (0, 1.5, 0), (3, 3, 3))]),
     dict(kind="chair", front="Back", face=dict(target=[0, 1.5, 20])), dict(ground=ground(0)), dict(P4="pass"))

# ---- P5
case("fail: two crates overlap by 1 stud", snap("Workspace.Map.CrateA", [part("Box", (0, 1.5, 0), (3, 3, 3))]), dict(kind="crate"),
     dict(ground=ground(0), neighbours=[nb("Workspace.Map.CrateB", (2, 2, 0), (3, 4, 3))]), dict(P5="fail"), num={"P5.overlaps.0.depth": 1.0}, fix=dict(P5="nudge"))
case("pass: crates touching face to face", snap("Workspace.Map.CrateA", [part("Box", (0, 1.5, 0), (3, 3, 3))]), dict(kind="crate"),
     dict(ground=ground(0), neighbours=[nb("Workspace.Map.CrateB", (3, 1.5, 0), (3, 3, 3))]), dict(P5="pass"))
case("pass: overlap with a CanCollide=false neighbour is ignored", snap("Workspace.Map.CrateA", [part("Box", (0, 1.5, 0), (3, 3, 3))]), dict(kind="crate"),
     dict(ground=ground(0), neighbours=[nb("Workspace.Map.Trigger", (1, 2, 0), (3, 4, 4), collide=False)]), dict(P5="pass"))
case("pass: allowOverlap prefix", snap("Workspace.Map.CrateA", [part("Box", (0, 1.5, 0), (3, 3, 3))]), dict(kind="crate", allowOverlap=["Workspace.Map.Shelf"]),
     dict(ground=ground(0), neighbours=[nb("Workspace.Map.Shelf.Board", (1, 2, 0), (3, 4, 3))]), dict(P5="pass"))
case("fail: sunk 2 studs into the floor part (overlap with the surface beyond tolerance)", snap("Workspace.Map.Crate17", [part("Box", (0, -0.5, 0), (3, 3, 3))]), dict(kind="crate"),
     dict(ground=ground(1.5, path="Workspace.Map.Floor"), neighbours=[nb("Workspace.Map.Floor", (0, 0.5, 0), (50, 2, 50))]), dict(P5="fail", P2="fail"))
case("fail: rotated crate cuts into a rotated wall (SAT with rotation)", snap("Workspace.Map.Crate18", [part("Box", (0, 1.5, 0), (3, 3, 3), yaw=45)], yaw=45), dict(kind="crate", yawGrid=45),
     dict(ground=ground(0), neighbours=[nb("Workspace.Map.Wall2", (2.2, 1.5, 0), (1, 6, 8), yaw=30)]), dict(P5="fail"))
case("fail: z-fighting coplanar tops inside one model", snap("Workspace.Map.Floor2", [part("Slab", (0, 0, 0), (10, 1, 10)), part("Plate", (0, 0, 0), (4, 1, 4))], pivot=(0, 0, 0)),
     dict(kind="platform", originOk=True, floating=True), dict(), dict(P5="fail"))
case("pass: plate sits 0.2 above the slab (no z-fight)", snap("Workspace.Map.Floor3", [part("Slab", (0, 0, 0), (10, 1, 10)), part("Plate", (0, 0.2, 0), (4, 1, 4))], pivot=(0, 0, 0)),
     dict(kind="platform", originOk=True, floating=True), dict(), dict(P5="pass"))
case("fail: outside the map bounds", snap("Workspace.Map.Crate19", [part("Box", (800, 1.5, 0), (3, 3, 3))]), dict(kind="crate", bounds=dict(min=[-500, -50, -500], max=[500, 200, 500])),
     dict(ground=ground(0)), dict(P5="fail"))
case("fail: 60% of the volume inside terrain", snap("Workspace.Map.Crate20", [part("Box", (0, 3, 0), (6, 6, 6))]), dict(kind="crate"), dict(ground=ground(0), terrainFill=0.6),
     dict(P5="fail"), fix=dict(P5="raise"))

# ---- P6
case("fail: unanchored decor would fall", snap("Workspace.Map.Vase", [part("Body", (0, 1, 0), (1, 2, 1), anchored=False)]), dict(kind="prop"), dict(ground=ground(0)),
     dict(P6="fail"), fix=dict(P6="anchor"))
case("pass: unanchored part welded to an anchored assembly", snap("Workspace.Map.Vase2", [part("Body", (0, 1, 0), (1, 2, 1), anchored=False, anchoredAssembly=True)]), dict(kind="prop"),
     dict(ground=ground(0)), dict(P6="pass"))
case("pass: dynamic object may be unanchored", snap("Workspace.Map.Ball", [part("Body", (0, 1, 0), (2, 2, 2), anchored=False)]), dict(kind="prop", dynamic=True), dict(ground=ground(0)),
     dict(P6="pass"))
case("fail: zero-size and invisible junk parts", snap("Workspace.Map.Hut", [part("Wall", (0, 3, 0), (6, 6, 1)), part("Part", (0, 3, 0), (1, 0, 1)), part("Ghost", (3, 3, 3), (2, 2, 2), transp=1.0, collide=False, touch=False)]),
     dict(kind="prop"), dict(ground=ground(0)), dict(P6="fail"), fix=dict(P6="removeParts"))
case("fail: coin blocks the player (CanCollide true)", snap("Workspace.Map.Coin2", [part("Coin", (0, 3, 0), (1.5, 1.5, 0.2))]), dict(kind="pickup"), dict(ground=ground(0)),
     dict(P6="fail"), fix=dict(P6="setCanCollide"))
case("fail: solid wall with no collision", snap("Workspace.Map.Wall1", [part("Wall", (0, 3, 0), (10, 6, 1), collide=False)]), dict(kind="wall", canCollide=True), dict(ground=ground(0)),
     dict(P6="fail"))
case("fail: trigger needs CanTouch", snap("Workspace.Map.Pad", [part("Pad", (0, 0.5, 0), (6, 1, 6), touch=False)]), dict(kind="prop", canTouch=True), dict(ground=ground(0)),
     dict(P6="fail"))

# ---- P7
stair1 = snap("Workspace.Map.Stairs1", [part("S", (0, 4, 0), (4, 8, 8))])
case("pass: stairs end where the next flight starts", stair1,
     dict(kind="stairs", connect=[dict(at="front", point=[0, 4, -4], to="Workspace.Map.Stairs2")]), dict(ground=ground(0)), dict(P7="pass"))
case("fail: stairs end 0.6 studs short of the next flight", stair1,
     dict(kind="stairs", connect=[dict(at="front", point=[0, 4, -4.6], to="Workspace.Map.Stairs2")]), dict(ground=ground(0)), dict(P7="fail"), fix=dict(P7="moveBy"))
case("fail: connection target not resolved", stair1, dict(kind="stairs", connect=[dict(at="front", to="Workspace.Map.Missing")]), dict(ground=ground(0)), dict(P7="fail"))
left = snap("Workspace.Map.Gate.L", [part("Post", (-10, 4, 0), (2, 8, 2))], yaw=0)
right_ok = snap("Workspace.Map.Gate.R", [part("Post", (10, 4, 0), (2, 8, 2))], yaw=0)
right_bad = snap("Workspace.Map.Gate.R", [part("Post", (11.5, 4, 0), (2, 8, 2))], yaw=0)
right_size = snap("Workspace.Map.Gate.R", [part("Post", (10, 4, 0), (2, 10, 2))], yaw=0)
case("pass: mirrored gate posts", left, dict(kind="prop", pair={"with": "Workspace.Map.Gate.R", "axis": "x", "at": 0}), dict(ground=ground(0), pair=right_ok), dict(P7="pass"))
case("fail: mirrored post 1.5 studs off", left, dict(kind="prop", pair={"with": "Workspace.Map.Gate.R", "axis": "x", "at": 0}), dict(ground=ground(0), pair=right_bad), dict(P7="fail"), fix=dict(P7="moveBy"))
case("fail: mirrored post has a different height", left, dict(kind="prop", pair={"with": "Workspace.Map.Gate.R", "axis": "x", "at": 0}), dict(ground=ground(0), pair=right_size), dict(P7="fail"))
fence = snap("Workspace.Map.Fence5", [part("Post", (20, 3, 0), (1, 6, 1))])
case("pass: fence post matches its siblings", fence, dict(kind="prop", group=dict(sameYaw=True)),
     dict(ground=ground(0), siblings=[dict(dims=[1, 1, 6], partCount=1, yaw=0, pos=[0, 3, 0]), dict(dims=[1, 1, 6], partCount=1, yaw=0, pos=[5, 3, 0])]), dict(P7="pass"))
case("fail: fence post is taller than its siblings", fence, dict(kind="prop", group=dict()),
     dict(ground=ground(0), siblings=[dict(dims=[1, 1, 5], partCount=1, yaw=0, pos=[0, 3, 0]), dict(dims=[1, 1, 5], partCount=1, yaw=0, pos=[5, 3, 0])]), dict(P7="fail"))
case("fail: fence post rotated differently from the group", snap("Workspace.Map.Fence6", [part("Post", (20, 3, 0), (1, 6, 1), yaw=45)], yaw=45), dict(kind="prop", group=dict(sameYaw=True), yawGrid=45),
     dict(ground=ground(0), siblings=[dict(dims=[1, 1, 6], partCount=1, yaw=0, pos=[0, 3, 0])]), dict(P7="fail"))

# ---- waiver
case("waived: a failing check with a reason does not fail the model", snap("Workspace.Map.Crate21", [part("Box", (0, 5, 0), (3, 3, 3))]),
     dict(kind="crate", waive=dict(P2="hangs from the ceiling rope, see decisions.md")), dict(ground=ground(0)), dict(P2="fail"), status="pass")


def build():
    return json.dumps(dict(version=1, note="generated by make_fixtures.py; expectations are hand-written", cases=CASES), indent=1, sort_keys=True) + "\n"


if __name__ == "__main__":
    out = build()
    p = os.path.join(HERE, "fixtures.json")
    if "--check" in sys.argv:
        cur = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        sys.exit(0 if cur == out else 1)
    open(p, "w", encoding="utf-8", newline="\n").write(out)
    print("wrote %s (%d cases)" % (p, len(CASES)))
