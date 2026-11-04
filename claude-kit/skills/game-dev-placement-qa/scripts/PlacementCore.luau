--!strict
-- PlacementCore: the PURE placement checks P1-P7 of game-dev-placement-qa. Plain tables in, a report out, no Roblox API (testable with Lune).
-- Same algorithm as placement_ref.py (Python reference); both are run on tests/fixtures.json and must agree. Edit both together.
-- Data (vectors are {x, y, z}; a rotation `r` is the 9 numbers of CFrame:GetComponents() after the position: R00 R01 R02 R10 R11 R12 R20 R21 R22):
--   snap   = { path, class, pivot = { p, r }, hasPrimaryPart, parts = { { name, p, r, size, anchored, anchoredAssembly, canCollide, canTouch, massless, transparency, hasEffects } } }
--   intent = see references/intent.md (kind, floating, expectedSize, face, yawGrid, randomYaw, surfacePath, bounds, allowOverlap, connect, pair, group, waive, ...)
--   env    = { ground = { samples = { { x, z, y?, n?, path? } } }, neighbours = { part... }, terrainFill?, faceTarget?, connectTargets, pair?, siblings }
-- Core.verify(snap, intent, env, opts) -> report { path, class, kind, status, failed, waived, unverified, checks = { P1 .. P7 = { status, measured, tolerance, issues, fixes, unverified, warnings } } }
local Core = {}

type Dict = { [string]: any }
type Vec = { number }

Core.DEFAULTS = {
	floatTol = 0.1,
	buryTol = 0.25,
	slopeTol = 1.0,
	maxTiltDeg = 3.0,
	faceTolDeg = 15.0,
	yawTolDeg = 1.0,
	defaultYawGrid = 15.0,
	sizeTol = 0.2,
	overlapTol = 0.05,
	zfightDist = 0.005,
	zfightArea = 0.01,
	terrainFillMax = 0.15,
	connectTol = 0.1,
	atTol = 1.0,
	posGridTol = 0.05,
	originRadius = 0.5,
	pairTol = 0.15,
	cloneSizeTol = 0.05,
	maxZfightParts = 300,
	maxSize = 2048.0,
	minSize = 0.05,
} :: Dict

-- Reference scale per object kind. size = ascending [small, mid, large] dimension ranges in studs (pivot-frame extents, any axis order).
Core.KINDS = {
	door = {
		size = { { 0.1, 2 }, { 3, 6 }, { 6, 9 } },
		needsFacing = true,
		yawGrid = 90,
		allowOverlapNames = { "wall", "frame", "doorway" },
	},
	window = {
		size = { { 0.1, 2 }, { 2, 8 }, { 2, 8 } },
		needsFacing = true,
		yawGrid = 90,
		allowOverlapNames = { "wall", "frame" },
	},
	npc = { size = { { 1, 4 }, { 1.5, 4 }, { 4.5, 7 } }, needsFacing = true },
	player = { size = { { 1, 4 }, { 1.5, 4 }, { 4.5, 7 } }, needsFacing = true },
	sign = { size = { { 0.05, 2 }, { 1, 12 }, { 1, 16 } }, needsFacing = true, yawGrid = 90 },
	chair = { size = { { 1.5, 4 }, { 1.5, 4 }, { 2, 5 } }, needsFacing = true },
	table = { size = { { 2, 5 }, { 2, 12 }, { 2, 14 } } },
	lamp = { size = { { 0.5, 4 }, { 0.5, 4 }, { 5, 25 } } },
	crate = { size = { { 1.5, 8 }, { 1.5, 8 }, { 1.5, 8 } } },
	fence = { size = { { 0.2, 2 }, { 2, 10 }, { 2, 20 } } },
	wall = { size = { { 0.2, 4 }, { 4, 60 }, { 4, 300 } }, yawGrid = 90 },
	stairs = { size = { { 1, 60 }, { 2, 40 }, { 3, 40 } } },
	platform = { size = { { 0.2, 6 }, { 4, 400 }, { 4, 400 } } },
	tree = { size = { { 1, 20 }, { 1, 30 }, { 5, 80 } }, randomYaw = true, buryTol = 1.0, terrainFillMax = 0.4 },
	rock = { size = { { 0.5, 20 }, { 0.5, 30 }, { 0.5, 30 } }, randomYaw = true, buryTol = 1.5, terrainFillMax = 0.5 },
	bush = { size = { { 0.5, 8 }, { 0.5, 8 }, { 0.5, 8 } }, randomYaw = true, buryTol = 0.5, terrainFillMax = 0.4 },
	pickup = { size = { { 0.2, 4 }, { 0.5, 4 }, { 0.5, 4 } }, floating = true, canCollide = false },
	ground = { floating = true, randomYaw = true },
	prop = {},
} :: Dict

Core.NAMES = {
	P1 = "Pivot and size",
	P2 = "Grounded",
	P3 = "Upright",
	P4 = "Facing and yaw",
	P5 = "Clearance",
	P6 = "Physics flags",
	P7 = "Connections",
} :: { [string]: string }
Core.ORDER = { "P1", "P2", "P3", "P4", "P5", "P6", "P7" }

local function rnd(x: number): number
	return math.floor(x + 0.5)
end

local function r3(x: number): number
	return math.floor(x * 1000 + 0.5) / 1000
end

local function rv(v: Vec): Vec
	return { r3(v[1]), r3(v[2]), r3(v[3]) }
end

local function add(a: Vec, b: Vec): Vec
	return { a[1] + b[1], a[2] + b[2], a[3] + b[3] }
end

local function sub(a: Vec, b: Vec): Vec
	return { a[1] - b[1], a[2] - b[2], a[3] - b[3] }
end

local function scale(a: Vec, s: number): Vec
	return { a[1] * s, a[2] * s, a[3] * s }
end

local function dot(a: Vec, b: Vec): number
	return a[1] * b[1] + a[2] * b[2] + a[3] * b[3]
end

local function cross(a: Vec, b: Vec): Vec
	return { a[2] * b[3] - a[3] * b[2], a[3] * b[1] - a[1] * b[3], a[1] * b[2] - a[2] * b[1] }
end

local function vlen(a: Vec): number
	return math.sqrt(dot(a, a))
end

local function norm(a: Vec): Vec
	local n = vlen(a)
	if n < 1e-12 then
		return { 0, 0, 0 }
	end
	return { a[1] / n, a[2] / n, a[3] / n }
end

local function axesOf(r: Vec): { Vec }
	return { { r[1], r[4], r[7] }, { r[2], r[5], r[8] }, { r[3], r[6], r[9] } }
end

local function lookOf(r: Vec): Vec
	return { -r[3], -r[6], -r[9] }
end

local function angleDeg(a: Vec, b: Vec): number
	local la, lb = vlen(a), vlen(b)
	if la < 1e-9 or lb < 1e-9 then
		return 0
	end
	local c = dot(a, b) / (la * lb)
	c = math.max(-1, math.min(1, c))
	return math.deg(math.acos(c))
end

local function yawOf(f: Vec): number
	return math.deg(math.atan2(-f[1], -f[3]))
end

local function wrap180(d: number): number
	d = (d + 180) % 360 - 180
	if d == -180 then
		d = 180
	end
	return d
end

local function pathMatches(path: string?, prefix: string?): boolean
	if not path or not prefix or path == "" or prefix == "" then
		return false
	end
	return path == prefix or string.sub(path, 1, #prefix + 1) == prefix .. "."
end

local function contains(s: string, sub_: string): boolean
	return string.find(s, sub_, 1, true) ~= nil
end

-- ------------------------------------------------------------------ geometry
local function corners(part: Dict): { Vec }
	local ax = axesOf(part.r)
	local h = { part.size[1] / 2, part.size[2] / 2, part.size[3] / 2 }
	local out = {}
	for _, sx in { -1, 1 } do
		for _, sy in { -1, 1 } do
			for _, sz in { -1, 1 } do
				local c = part.p
				c = add(c, scale(ax[1], sx * h[1]))
				c = add(c, scale(ax[2], sy * h[2]))
				c = add(c, scale(ax[3], sz * h[3]))
				table.insert(out, c)
			end
		end
	end
	return out
end

local function worldAabb(parts: { Dict }): (Vec, Vec)
	local lo = { math.huge, math.huge, math.huge }
	local hi = { -math.huge, -math.huge, -math.huge }
	for _, pt in parts do
		for _, c in corners(pt) do
			for i = 1, 3 do
				lo[i] = math.min(lo[i], c[i])
				hi[i] = math.max(hi[i], c[i])
			end
		end
	end
	return lo, hi
end

local function modelBox(snap: Dict): Dict
	local piv = snap.pivot
	local ax = axesOf(piv.r)
	local lo = { math.huge, math.huge, math.huge }
	local hi = { -math.huge, -math.huge, -math.huge }
	for _, pt in snap.parts do
		for _, c in corners(pt) do
			local d = sub(c, piv.p)
			for i = 1, 3 do
				local t = dot(d, ax[i])
				lo[i] = math.min(lo[i], t)
				hi[i] = math.max(hi[i], t)
			end
		end
	end
	local dims = { hi[1] - lo[1], hi[2] - lo[2], hi[3] - lo[3] }
	local mid = { (hi[1] + lo[1]) / 2, (hi[2] + lo[2]) / 2, (hi[3] + lo[3]) / 2 }
	local center = piv.p
	for i = 1, 3 do
		center = add(center, scale(ax[i], mid[i]))
	end
	return { lo = lo, hi = hi, dims = dims, mid = mid, center = center, axes = ax }
end

local FACES: { [string]: { number } } = {
	front = { 3, -1 },
	back = { 3, 1 },
	right = { 1, 1 },
	left = { 1, -1 },
	top = { 2, 1 },
	bottom = { 2, -1 },
}

local function facePoint(box: Dict, at: string?): Vec
	if at == nil or at == "center" then
		return box.center
	end
	local f = FACES[at]
	return add(box.center, scale(box.axes[f[1]], f[2] * box.dims[f[1]] / 2))
end

-- Footprint of the model for the ground rays: centre + four corners inset 10% (world axes). The adapter casts one ray per point.
function Core.footprint(snap: Dict): Dict
	local lo, hi = worldAabb(snap.parts)
	local wx, wz = hi[1] - lo[1], hi[3] - lo[3]
	local cx, cz = (lo[1] + hi[1]) / 2, (lo[3] + hi[3]) / 2
	return {
		ymin = lo[2],
		ymax = hi[2],
		points = {
			{ cx, cz },
			{ lo[1] + 0.1 * wx, lo[3] + 0.1 * wz },
			{ hi[1] - 0.1 * wx, lo[3] + 0.1 * wz },
			{ lo[1] + 0.1 * wx, hi[3] - 0.1 * wz },
			{ hi[1] - 0.1 * wx, hi[3] - 0.1 * wz },
		},
		aabbMin = lo,
		aabbMax = hi,
	}
end

-- SAT between two oriented boxes. Returns depth and the translation of box a that separates it from b, or nil when they do not intersect.
local function obbPenetration(a: Dict, b: Dict): (number?, Vec?)
	local axa, axb = axesOf(a.r), axesOf(b.r)
	local ha = { a.size[1] / 2, a.size[2] / 2, a.size[3] / 2 }
	local hb = { b.size[1] / 2, b.size[2] / 2, b.size[3] / 2 }
	local t = sub(b.p, a.p)
	local cand: { Vec } = { axa[1], axa[2], axa[3], axb[1], axb[2], axb[3] }
	for i = 1, 3 do
		for j = 1, 3 do
			local c = cross(axa[i], axb[j])
			if vlen(c) > 1e-6 then
				table.insert(cand, norm(c))
			end
		end
	end
	local best = math.huge
	local bestAxis: Vec = { 0, 0, 0 }
	local bestSign = 1
	for _, L in cand do
		local ra = ha[1] * math.abs(dot(axa[1], L))
			+ ha[2] * math.abs(dot(axa[2], L))
			+ ha[3] * math.abs(dot(axa[3], L))
		local rb = hb[1] * math.abs(dot(axb[1], L))
			+ hb[2] * math.abs(dot(axb[2], L))
			+ hb[3] * math.abs(dot(axb[3], L))
		local d = dot(t, L)
		local ov = ra + rb - math.abs(d)
		if ov <= 0 then
			return nil, nil
		end
		if ov < best then
			best = ov
			bestAxis = L
			bestSign = if d >= 0 then 1 else -1
		end
	end
	return best, scale(bestAxis, -bestSign * best)
end

local function polyArea(p: { Vec }): number
	local s = 0
	local n = #p
	for i = 1, n do
		local x1, y1 = p[i][1], p[i][2]
		local nx = p[i % n + 1]
		s += x1 * nx[2] - nx[1] * y1
	end
	return s / 2
end

local function ccw(p: { Vec }): { Vec }
	if polyArea(p) >= 0 then
		return p
	end
	local out = {}
	for i = #p, 1, -1 do
		table.insert(out, p[i])
	end
	return out
end

local function isect(p1: Vec, p2: Vec, a: Vec, b: Vec): Vec
	local x1, y1, x2, y2 = p1[1], p1[2], p2[1], p2[2]
	local x3, y3, x4, y4 = a[1], a[2], b[1], b[2]
	local den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
	if math.abs(den) < 1e-12 then
		return { x2, y2 }
	end
	local t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
	return { x1 + t * (x2 - x1), y1 + t * (y2 - y1) }
end

local function clip(subject: { Vec }, clipPoly: { Vec }): { Vec }
	local out = subject
	local n = #clipPoly
	for i = 1, n do
		local a, b = clipPoly[i], clipPoly[i % n + 1]
		local inp = out
		out = {}
		if #inp == 0 then
			break
		end
		for k = 1, #inp do
			local cur = inp[k]
			local prev = inp[if k == 1 then #inp else k - 1]
			local sc = (b[1] - a[1]) * (cur[2] - a[2]) - (b[2] - a[2]) * (cur[1] - a[1])
			local sp = (b[1] - a[1]) * (prev[2] - a[2]) - (b[2] - a[2]) * (prev[1] - a[1])
			if sc >= 0 then
				if sp < 0 then
					table.insert(out, isect(prev, cur, a, b))
				end
				table.insert(out, cur)
			elseif sp >= 0 then
				table.insert(out, isect(prev, cur, a, b))
			end
		end
	end
	return out
end

local function faceRect(part: Dict, i: number, s: number): (Vec, Vec, { any }, { any })
	local ax = axesOf(part.r)
	local h = { part.size[1] / 2, part.size[2] / 2, part.size[3] / 2 }
	local n = scale(ax[i], s)
	local c = add(part.p, scale(n, h[i]))
	local j, k = i % 3 + 1, (i + 1) % 3 + 1
	return n, c, { ax[j], h[j] }, { ax[k], h[k] }
end

local SIGNS = { { 1, 1 }, { -1, 1 }, { -1, -1 }, { 1, -1 } }

-- Area of overlap of the largest coplanar, same-facing face pair of parts a and b (0 when none). Downward faces are ignored (they rest on something).
local function coplanarOverlap(a: Dict, b: Dict, distTol: number): number
	local best = 0
	for i = 1, 3 do
		for _, s in { -1, 1 } do
			local n, c, ua, va = faceRect(a, i, s)
			for i2 = 1, 3 do
				for _, s2 in { -1, 1 } do
					local n2, c2, ub, vb = faceRect(b, i2, s2)
					if
						not (dot(n, n2) < 0.99996 or n[2] < -0.99619)
						and math.abs(dot(n, c) - dot(n, c2)) <= distTol
					then
						local e1: Vec = ua[1]
						local e2 = norm(cross(n, e1))
						local ra, rb = {}, {}
						for _, sg in SIGNS do
							local pa = add(add(c, scale(ua[1], sg[1] * ua[2])), scale(va[1], sg[2] * va[2]))
							table.insert(ra, { dot(pa, e1), dot(pa, e2) })
							local pb = add(add(c2, scale(ub[1], sg[1] * ub[2])), scale(vb[1], sg[2] * vb[2]))
							table.insert(rb, { dot(pb, e1), dot(pb, e2) })
						end
						local poly = clip(ccw(rb), ccw(ra))
						if #poly >= 3 then
							best = math.max(best, math.abs(polyArea(poly)))
						end
					end
				end
			end
		end
	end
	return best
end

local function aabbTouch(p1: Dict, p2: Dict, pad: number): boolean
	local lo1, hi1 = worldAabb({ p1 })
	local lo2, hi2 = worldAabb({ p2 })
	for i = 1, 3 do
		if lo1[i] > hi2[i] + pad or lo2[i] > hi1[i] + pad then
			return false
		end
	end
	return true
end

-- ------------------------------------------------------------------ intent helpers
local function kindOf(intent: Dict): Dict
	local k = Core.KINDS[intent.kind or "prop"]
	return (k or Core.KINDS.prop) :: Dict
end

local function pick(intent: Dict, key: string, kind: Dict, opts: Dict, okey: string?): any
	if intent[key] ~= nil then
		return intent[key]
	end
	if kind[key] ~= nil then
		return kind[key]
	end
	return opts[okey or key]
end

local function mk(
	status: string,
	measured: Dict?,
	tolerance: Dict?,
	issues: { string }?,
	fixes: { Dict }?,
	unverified: { string }?,
	warnings: { string }?
): Dict
	return {
		status = status,
		measured = measured or {},
		tolerance = tolerance or {},
		issues = issues or {},
		fixes = fixes or {},
		unverified = unverified or {},
		warnings = warnings or {},
	}
end

local function largestPart(snap: Dict): Dict
	local best, bv = nil, -1
	for _, p in snap.parts do
		local v = p.size[1] * p.size[2] * p.size[3]
		if v > bv then
			best, bv = p, v
		end
	end
	return best :: Dict
end

local function fmt(f: string, ...: any): string
	return string.format(f, ...)
end

local function listStr(v: any): string
	local parts = {}
	for _, x in v do
		table.insert(parts, tostring(x))
	end
	return "[" .. table.concat(parts, ", ") .. "]"
end

local function nstatus(issues: { string }): string
	return if #issues > 0 then "fail" else "pass"
end

-- ------------------------------------------------------------------ checks
local function checkP1(snap: Dict, intent: Dict, _env: Dict, opts: Dict): Dict
	local kind = kindOf(intent)
	local issues: { string }, fixes: { Dict }, unv: { string } = {}, {}, {}
	local parts = snap.parts
	if #parts == 0 then
		return mk("fail", nil, nil, { "model has no parts" })
	end
	local box = modelBox(snap)
	local dims = box.dims
	local meas: Dict = { pivot = rv(snap.pivot.p), size = rv(dims) }
	local tol: Dict = {}
	if snap.class == "Model" and not snap.hasPrimaryPart then
		table.insert(issues, "no PrimaryPart set (the pivot is implicit and fixes/moves cannot rely on it)")
		table.insert(fixes, { action = "setPrimaryPart", part = largestPart(snap).name })
	end
	for i = 1, 3 do
		local slack = 0.5 + 0.1 * dims[i]
		if box.lo[i] - slack > 0 or box.hi[i] + slack < 0 then
			table.insert(
				issues,
				fmt(
					"pivot is outside the model's bounding box on axis %s (offset %.2f studs)",
					string.sub("XYZ", i, i),
					math.min(math.abs(box.lo[i]), math.abs(box.hi[i]))
				)
			)
			break
		end
	end
	local pp = snap.pivot.p
	if vlen(pp) < opts.originRadius and not intent.originOk then
		local at = intent.at
		if not (at and vlen(at) < opts.originRadius) then
			table.insert(
				issues,
				"pivot is at the world origin (0,0,0): moved by accident? set intent.at or intent.originOk"
			)
		end
	end
	tol.originRadius = opts.originRadius
	if intent.at ~= nil then
		local d = sub(intent.at, pp)
		meas.atOffset = rv(d)
		tol.atTol = pick(intent, "atTol", {}, opts)
		if vlen(d) > tol.atTol then
			table.insert(issues, fmt("pivot is %.2f studs from the intended position", vlen(d)))
			table.insert(fixes, { action = "moveBy", d = rv(d) })
		end
	end
	if intent.posGrid and intent.posGrid ~= 0 then
		local g = intent.posGrid
		local o = intent.posGridOrigin or { 0, 0 }
		local dx = (pp[1] - o[1]) % g
		local dz = (pp[3] - o[2]) % g
		dx = math.min(dx, g - dx)
		dz = math.min(dz, g - dz)
		meas.posGridDev = { r3(dx), r3(dz) }
		tol.posGridTol = opts.posGridTol
		if dx > opts.posGridTol or dz > opts.posGridTol then
			local sx = rnd((pp[1] - o[1]) / g) * g + o[1] - pp[1]
			local sz = rnd((pp[3] - o[2]) / g) * g + o[2] - pp[3]
			table.insert(issues, fmt("position is off the %g-stud grid by (%.2f, %.2f)", g, dx, dz))
			table.insert(fixes, { action = "moveBy", d = rv({ sx, 0, sz }) })
		end
	end
	local small = math.min(dims[1], dims[2], dims[3])
	local big = math.max(dims[1], dims[2], dims[3])
	if small < opts.minSize then
		table.insert(issues, fmt("degenerate size: smallest extent %.3f studs", small))
	end
	if big > opts.maxSize then
		table.insert(issues, fmt("size %.0f studs exceeds the %g stud limit", big, opts.maxSize))
	end
	local exp = intent.expectedSize
	local srt = { dims[1], dims[2], dims[3] }
	table.sort(srt)
	if exp then
		local st = pick(intent, "sizeTol", kind, opts)
		tol.sizeTol = st
		local a, b
		if intent.sizeSorted or intent.sizeAxes == false then
			a = { exp[1], exp[2], exp[3] }
			table.sort(a)
			b = srt
		else
			a, b = exp, dims
		end
		local bad = false
		for i = 1, 3 do
			if math.abs(b[i] - a[i]) > st * a[i] + 0.05 then
				bad = true
			end
		end
		meas.expectedSize = rv(exp)
		if bad then
			table.insert(
				issues,
				fmt(
					"size %s differs from the expected %s by more than %d%%",
					listStr(rv(dims)),
					listStr(rv(exp)),
					rnd(st * 100)
				)
			)
		end
	elseif kind.size then
		local rng = kind.size
		meas.kindRange = rng
		local bad = false
		for i = 1, 3 do
			if srt[i] < rng[i][1] or srt[i] > rng[i][2] then
				bad = true
			end
		end
		if bad then
			table.insert(
				issues,
				fmt(
					"size %s is outside the usual %s range (sorted small/mid/large)",
					listStr(rv(srt)),
					tostring(intent.kind)
				)
			)
		end
	else
		table.insert(unv, "size")
	end
	return mk(nstatus(issues), meas, tol, issues, fixes, unv)
end

local function checkP2(snap: Dict, intent: Dict, env: Dict, opts: Dict): Dict
	local kind = kindOf(intent)
	local floating = intent.floating
	if floating == nil then
		floating = kind.floating
	end
	if floating then
		return mk("skip", nil, nil, { "flagged floating (air, hover or decor)" })
	end
	local ft = pick(intent, "floatTol", kind, opts)
	local bt = pick(intent, "buryTol", kind, opts)
	local fp = Core.footprint(snap)
	local samples = if env.ground then env.ground.samples or {} else {}
	local hits = {}
	for _, s in samples do
		if s.y ~= nil then
			table.insert(hits, s)
		end
	end
	local tol: Dict = { floatTol = ft, buryTol = bt }
	if #hits == 0 then
		return mk(
			"fail",
			{ bottomY = r3(fp.ymin), samples = #samples, hits = 0 },
			tol,
			{ "no surface below the model (ray hits nothing): over the void, or the surface is not collidable" }
		)
	end
	local top, low = hits[1], hits[1]
	for _, s in hits do
		if s.y > top.y then
			top = s
		end
		if s.y < low.y then
			low = s
		end
	end
	local gap = fp.ymin - top.y
	local spread = top.y - low.y
	local meas: Dict = {
		bottomY = r3(fp.ymin),
		groundY = r3(top.y),
		gap = r3(gap),
		spread = r3(spread),
		hits = #hits,
		samples = #samples,
	}
	local issues: { string }, fixes: { Dict }, warns: { string } = {}, {}, {}
	if gap > ft then
		table.insert(issues, fmt("floating %.2f studs above the surface (tolerance %.2f)", gap, ft))
		table.insert(fixes, { action = "snapToGround", dy = r3(-gap) })
	elseif gap < -bt then
		table.insert(issues, fmt("buried %.2f studs into the surface (tolerance %.2f)", -gap, bt))
		table.insert(fixes, { action = "snapToGround", dy = r3(-gap) })
	end
	local sp = intent.surfacePath
	if sp then
		meas.restsOn = top.path
		if not pathMatches(top.path or "", sp) then
			table.insert(issues, fmt("rests on %s, not on the intended surface %s", top.path or "?", sp))
		end
	end
	if spread > opts.slopeTol then
		if intent.flatGround then
			table.insert(issues, fmt("ground under the footprint varies by %.2f studs (flatGround declared)", spread))
		else
			table.insert(
				warns,
				fmt("ground varies by %.2f studs under the footprint: check the lower side for a visible gap", spread)
			)
		end
	end
	return mk(nstatus(issues), meas, tol, issues, fixes, {}, warns)
end

local function checkP3(snap: Dict, intent: Dict, env: Dict, opts: Dict): Dict
	if intent.allowTilt then
		return mk("skip", nil, nil, { "tilt allowed by intent" })
	end
	local ax = axesOf(snap.pivot.r)
	local up = ax[2]
	local ref: Vec = { 0, 1, 0 }
	local custom = false
	if intent.alignToSurface and env.ground then
		for _, s in env.ground.samples or {} do
			if s.y ~= nil and s.n then
				ref = s.n
				custom = true
				break
			end
		end
	end
	local ang = angleDeg(up, ref)
	local meas: Dict = { tiltDeg = r3(ang), up = rv(up) }
	local issues: { string }, fixes: { Dict } = {}, {}
	local tol: Dict
	if intent.tilt then
		local want = intent.tilt.deg or 0
		local tl = intent.tilt.tol or 3
		tol = { tiltDeg = want, tol = tl }
		if math.abs(ang - want) > tl then
			table.insert(issues, fmt("tilt %.1f deg, intended %.1f +/- %.1f", ang, want, tl))
			table.insert(fixes, { action = "setUpright", tiltDeg = want })
		end
	else
		local mt = intent.maxTiltDeg
		if mt == nil then
			mt = opts.maxTiltDeg
		end
		tol = { maxTiltDeg = mt }
		if ang > mt then
			table.insert(
				issues,
				fmt(
					"%s: tilted %.1f deg from %s (tolerance %.1f)",
					if ang > 90 then "UPSIDE DOWN" else "leaning",
					ang,
					if custom then "the surface normal" else "world up",
					mt
				)
			)
			table.insert(fixes, { action = "setUpright" })
		end
	end
	return mk(nstatus(issues), meas, tol, issues, fixes)
end

local function checkP4(snap: Dict, intent: Dict, env: Dict, opts: Dict): Dict
	local kind = kindOf(intent)
	local r = snap.pivot.r
	local ax = axesOf(r)
	local fr = intent.front or "Front"
	local fvec: Vec
	if fr == "Front" then
		fvec = lookOf(r)
	elseif fr == "Back" then
		fvec = ax[3]
	elseif fr == "Right" then
		fvec = ax[1]
	else
		fvec = scale(ax[1], -1)
	end
	local fxz: Vec = { fvec[1], 0, fvec[3] }
	local meas: Dict = { front = rv(fvec) }
	local tol: Dict = {}
	local issues: { string }, fixes: { Dict }, unv: { string } = {}, {}, {}
	local face = intent.face
	local randomYaw = intent.randomYaw
	if randomYaw == nil then
		randomYaw = kind.randomYaw
	end
	local needs = kind.needsFacing
	local grid: number? = nil
	local explicitGrid = intent.yawGrid ~= nil or kind.yawGrid ~= nil
	if not randomYaw then
		grid = intent.yawGrid
		if grid == nil then
			grid = kind.yawGrid
		end
		if grid == nil and not face then
			grid = opts.defaultYawGrid
		end
	end
	if intent.yawGrid == 0 then
		grid = nil
	end
	if vlen(fxz) < 0.1 then
		return mk("fail", meas, tol, {
			fmt("the front points up or down (%s lying on its side?); fix P3 first", tostring(intent.kind or "model")),
		}, {})
	end
	local yaw = yawOf(fxz)
	meas.yawDeg = r3(yaw)
	local pos = snap.pivot.p
	if face and not face.any then
		tol.faceTolDeg = if face.tol ~= nil then face.tol else opts.faceTolDeg
		local tgt = if type(face.target) == "table" then face.target else env.faceTarget
		local desired: Vec? = nil
		if face.dir then
			desired = { face.dir[1], 0, face.dir[3] }
		elseif tgt then
			desired = { tgt[1] - pos[1], 0, tgt[3] - pos[3] }
		elseif face.awayFrom or env.faceAwayFrom then
			local af = face.awayFrom or env.faceAwayFrom
			desired = { pos[1] - af[1], 0, pos[3] - af[3] }
		end
		if desired == nil or vlen(desired) < 0.01 then
			table.insert(issues, "facing target missing or on the model's own position: cannot judge the facing")
		else
			local off = angleDeg(fxz, desired)
			local delta = wrap180(yawOf(desired) - yaw)
			meas.facingOffDeg = r3(off)
			meas.yawDeltaDeg = r3(delta)
			if off > tol.faceTolDeg then
				table.insert(
					issues,
					fmt("front faces %.1f deg away from the target (tolerance %.0f)", off, tol.faceTolDeg)
				)
				local final = delta
				if grid and explicitGrid then
					local snapped = rnd((yaw + delta) / grid) * grid
					if math.abs(wrap180(snapped - (yaw + delta))) <= tol.faceTolDeg then
						final = wrap180(snapped - yaw)
					end
				end
				table.insert(fixes, { action = "rotateYaw", deltaDeg = r3(final) })
			end
		end
	elseif needs and not (face and face.any) then
		table.insert(
			issues,
			fmt(
				"%s needs a declared facing (intent.face = {target=..} or {dir=..}, or {any=true} if it truly does not matter)",
				tostring(intent.kind)
			)
		)
	end
	if grid and not (#issues > 0 and #fixes > 0) then
		tol.yawGrid = grid
		tol.yawTolDeg = if intent.yawTolDeg ~= nil then intent.yawTolDeg else opts.yawTolDeg
		local nearest = rnd(yaw / grid) * grid
		local dev = math.abs(wrap180(yaw - nearest))
		meas.yawGridDevDeg = r3(dev)
		if dev > tol.yawTolDeg then
			table.insert(issues, fmt("yaw %.1f deg is %.1f deg off the %g deg grid", yaw, dev, grid))
			table.insert(fixes, { action = "rotateYaw", deltaDeg = r3(wrap180(nearest - yaw)) })
		end
	elseif not grid and not randomYaw and not face then
		table.insert(unv, "yaw grid")
	end
	return mk(nstatus(issues), meas, tol, issues, fixes, unv)
end

local function nameAllowed(pth: string, allow: { string }, names: { string }): boolean
	for _, a in allow do
		if pathMatches(pth, a) then
			return true
		end
	end
	local low = string.lower(pth)
	for _, n in names do
		if contains(low, n) then
			return true
		end
	end
	return false
end

local function checkP5(snap: Dict, intent: Dict, env: Dict, opts: Dict): Dict
	local kind = kindOf(intent)
	local parts = snap.parts
	local issues: { string }, fixes: { Dict }, warns: { string }, unv: { string } = {}, {}, {}, {}
	local lo, hi = worldAabb(parts)
	local meas: Dict = { aabbMin = rv(lo), aabbMax = rv(hi) }
	local tol: Dict = { overlapTol = opts.overlapTol }
	local b = intent.bounds or opts.bounds
	if b then
		local out = {}
		for i = 1, 3 do
			local bmin, bmax = b.min[i], b.max[i]
			if (bmin ~= nil and lo[i] < bmin - 1e-6) or (bmax ~= nil and hi[i] > bmax + 1e-6) then
				table.insert(out, string.sub("XYZ", i, i))
			end
		end
		if #out > 0 then
			table.insert(issues, "outside the map bounds on axis " .. table.concat(out, ","))
		end
	else
		table.insert(unv, "map bounds")
	end
	local allow: { string } = intent.allowOverlap or {}
	local names: { string } = {}
	for _, n in intent.allowOverlapNames or kind.allowOverlapNames or {} do
		table.insert(names, string.lower(n))
	end
	local bt = pick(intent, "buryTol", kind, opts)
	local samples = if env.ground then env.ground.samples or {} else {}
	local surf: { [string]: boolean } = {}
	local ymax, ymin = -math.huge, math.huge
	local nhit = 0
	for _, s in samples do
		if s.y ~= nil then
			nhit += 1
			ymax = math.max(ymax, s.y)
			ymin = math.min(ymin, s.y)
			if s.path then
				surf[s.path] = true
			end
		end
	end
	local spread = if nhit > 0 then ymax - ymin else 0
	local found: { [string]: Dict } = {}
	for _, np in env.neighbours or {} do
		local pth: string = np.path or ""
		if not nameAllowed(pth, allow, names) then
			local lim = opts.overlapTol
			local isSurf = surf[pth] == true
			if not isSurf then
				for sp in surf do
					if pathMatches(pth, sp) then
						isSurf = true
					end
				end
			end
			if isSurf or (intent.surfacePath and pathMatches(pth, intent.surfacePath)) then
				lim = math.max(lim, bt + spread)
			end
			for _, mp in parts do
				local nc = np.canCollide
				if nc == nil then
					nc = true
				end
				if mp.canCollide and nc then
					local depth, mv = obbPenetration(mp, np)
					if depth and mv and depth > lim then
						local cur = found[pth]
						if cur == nil or depth > cur.depth then
							found[pth] = { depth = depth, move = mv }
						end
					end
				end
			end
		end
	end
	local ov = {}
	for k, v in found do
		table.insert(ov, { path = k, depth = v.depth, move = v.move })
	end
	table.sort(ov, function(x, y)
		if x.depth ~= y.depth then
			return x.depth > y.depth
		end
		return x.path < y.path
	end)
	local list = {}
	for i = 1, math.min(5, #ov) do
		table.insert(list, { path = ov[i].path, depth = r3(ov[i].depth), move = rv(ov[i].move) })
		table.insert(issues, fmt("intersects %s by %.2f studs", ov[i].path, ov[i].depth))
	end
	meas.overlaps = list
	if #ov > 0 then
		table.insert(fixes, { action = "nudge", d = rv(ov[1].move) })
	end
	if #parts <= opts.maxZfightParts then
		local zf = {}
		local vis = {}
		for _, p in parts do
			if (p.transparency or 0) < 0.95 then
				table.insert(vis, p)
			end
		end
		for i, a in vis do
			for j = i + 1, #vis do
				local c = vis[j]
				if aabbTouch(a, c, 0.01) then
					local ar = coplanarOverlap(a, c, opts.zfightDist)
					if ar > opts.zfightArea then
						table.insert(zf, { pair = a.name .. "~" .. c.name, area = ar })
					end
				end
			end
			for _, nb in env.neighbours or {} do
				local npth: string = nb.path or ""
				if (nb.transparency or 0) < 0.95 and not nameAllowed(npth, allow, names) then
					if aabbTouch(a, nb, 0.01) then
						local ar = coplanarOverlap(a, nb, opts.zfightDist)
						if ar > opts.zfightArea then
							table.insert(zf, { pair = a.name .. "~" .. npth, area = ar })
						end
					end
				end
			end
		end
		table.sort(zf, function(x, y)
			if x.area ~= y.area then
				return x.area > y.area
			end
			return x.pair < y.pair
		end)
		local zl = {}
		for i = 1, math.min(5, #zf) do
			table.insert(zl, { pair = zf[i].pair, area = r3(zf[i].area) })
			table.insert(issues, fmt("z-fighting: coplanar faces %s overlap %.2f sq studs", zf[i].pair, zf[i].area))
		end
		meas.zfight = zl
		if #zf > 0 then
			table.insert(
				fixes,
				{ action = "offsetFace", note = "move one face 0.05 studs or make one part slightly larger/smaller" }
			)
		end
	else
		table.insert(unv, fmt("z-fight (more than %d parts)", opts.maxZfightParts))
	end
	local tf = env.terrainFill
	if tf ~= nil then
		local mx = pick(intent, "terrainFillMax", kind, opts)
		meas.terrainFill = r3(tf)
		tol.terrainFillMax = mx
		if tf > mx then
			table.insert(
				issues,
				fmt("%d%% of the model volume is inside terrain (limit %d%%)", rnd(tf * 100), rnd(mx * 100))
			)
			table.insert(fixes, { action = "raise", note = "raise the model or carve the terrain" })
		end
	end
	return mk(nstatus(issues), meas, tol, issues, fixes, unv, warns)
end

local function joinN(v: { string }, n: number): string
	local out = {}
	for i = 1, math.min(n, #v) do
		table.insert(out, v[i])
	end
	return table.concat(out, ", ")
end

local function checkP6(snap: Dict, intent: Dict, _env: Dict, _opts: Dict): Dict
	local kind = kindOf(intent)
	local parts = snap.parts
	local issues: { string }, fixes: { Dict }, unv: { string } = {}, {}, {}
	local dynamic = intent.dynamic and true or false
	local loose: { string } = {}
	for _, p in parts do
		if not p.anchored and not p.anchoredAssembly then
			table.insert(loose, p.name)
		end
	end
	local first10 = {}
	for i = 1, math.min(10, #loose) do
		table.insert(first10, loose[i])
	end
	local meas: Dict = { parts = #parts, unanchored = first10 }
	if #loose > 0 and not dynamic then
		table.insert(issues, fmt("%d part(s) not anchored (will fall or drift): %s", #loose, joinN(loose, 5)))
		local lp = {}
		for i = 1, math.min(50, #loose) do
			table.insert(lp, loose[i])
		end
		table.insert(fixes, { action = "anchor", parts = lp })
	end
	local wantCc = intent.canCollide
	if wantCc == nil then
		wantCc = kind.canCollide
	end
	local cc: { string } = {}
	for _, p in parts do
		if p.canCollide then
			table.insert(cc, p.name)
		end
	end
	meas.collidable = #cc
	if wantCc == true and #cc == 0 then
		table.insert(issues, "no part collides (CanCollide false everywhere): players walk through it")
		table.insert(fixes, { action = "setCanCollide", part = largestPart(snap).name, value = true })
	end
	if wantCc == false and #cc > 0 then
		table.insert(issues, fmt("%d part(s) collide but the object should not block: %s", #cc, joinN(cc, 5)))
		local lp = {}
		for i = 1, math.min(50, #cc) do
			table.insert(lp, cc[i])
		end
		table.insert(fixes, { action = "setCanCollide", parts = lp, value = false })
	end
	if intent.canTouch == true then
		local any = false
		for _, p in parts do
			if p.canTouch then
				any = true
			end
		end
		if not any then
			table.insert(issues, "no part has CanTouch true but the object needs touch events")
		end
	end
	if intent.massless ~= nil then
		local bad: { string } = {}
		for _, p in parts do
			if (p.massless and true or false) ~= (intent.massless and true or false) and not p.anchored then
				table.insert(bad, p.name)
			end
		end
		if #bad > 0 then
			table.insert(issues, fmt("Massless should be %s on: %s", tostring(intent.massless), joinN(bad, 5)))
		end
	end
	local junk: { { string } } = {}
	for _, p in parts do
		local mn = math.min(p.size[1], p.size[2], p.size[3])
		if mn < 0.001 then
			table.insert(junk, { p.name, "zero-size" })
		elseif
			(p.transparency or 0) >= 0.99
			and not p.canCollide
			and not p.canTouch
			and not p.hasEffects
			and not intent.allowInvisible
		then
			table.insert(junk, { p.name, "invisible and intangible" })
		end
	end
	local jl = {}
	for i = 1, math.min(10, #junk) do
		table.insert(jl, { part = junk[i][1], why = junk[i][2] })
	end
	meas.junk = jl
	if #junk > 0 then
		local d, names = {}, {}
		for i = 1, math.min(5, #junk) do
			table.insert(d, junk[i][1] .. " (" .. junk[i][2] .. ")")
		end
		for i = 1, math.min(50, #junk) do
			table.insert(names, junk[i][1])
		end
		table.insert(issues, "junk part(s): " .. table.concat(d, ", "))
		table.insert(fixes, { action = "removeParts", parts = names })
	end
	return mk(nstatus(issues), meas, {}, issues, fixes, unv)
end

-- Short description of a model used for clone/group consistency (the adapter sends these for the siblings).
function Core.summary(snap: Dict): Dict
	local box = modelBox(snap)
	local d = { box.dims[1], box.dims[2], box.dims[3] }
	table.sort(d)
	return { dims = rv(d), partCount = #snap.parts, yaw = r3(yawOf(lookOf(snap.pivot.r))), pos = rv(snap.pivot.p) }
end

local function median(v: { number }): number
	local c = table.clone(v)
	table.sort(c)
	return c[#c // 2 + 1]
end

local function checkP7(snap: Dict, intent: Dict, env: Dict, opts: Dict): Dict
	local conns: { Dict } = intent.connect or {}
	local pair = intent.pair
	local group = intent.group
	if #conns == 0 and pair == nil and group == nil then
		return mk("skip", nil, nil, { "no connection, pair or group declared" })
	end
	local issues: { string }, fixes: { Dict } = {}, {}
	local meas: Dict, tol: Dict = {}, {}
	local box = modelBox(snap)
	local targets = env.connectTargets or {}
	local res = {}
	for i, c in conns do
		local pt = c.point
		if pt == nil and targets[i] then
			pt = targets[i].point
		end
		local t = if c.tol ~= nil then c.tol else opts.connectTol
		if pt == nil then
			table.insert(issues, fmt("connection %d: target %s could not be resolved", i, tostring(c.to or "?")))
		else
			local mine = facePoint(box, c.at)
			local d = sub(pt, mine)
			table.insert(res, { at = c.at, offset = rv(d), dist = r3(vlen(d)) })
			tol.connectTol = t
			if vlen(d) > t then
				table.insert(
					issues,
					fmt(
						"connection %d (%s): ends %.2f studs from where the next piece starts (offset %s)",
						i,
						tostring(c.at or "center"),
						vlen(d),
						listStr(rv(d))
					)
				)
				table.insert(fixes, { action = "moveBy", d = rv(d) })
			end
		end
	end
	if #res > 0 then
		meas.connections = res
	end
	if pair ~= nil then
		local other = env.pair
		if not other then
			table.insert(issues, fmt("mirror partner %s not found", tostring(pair.with or "?")))
		else
			local ax = if (pair.axis or "x") == "x" then 1 else 3
			local pp = snap.pivot.p
			local want: Vec = { pp[1], pp[2], pp[3] }
			want[ax] = 2 * pair.at - pp[ax]
			local d = sub(other.pivot.p, want)
			meas.pairOffset = rv(d)
			tol.pairTol = opts.pairTol
			if vlen(d) > opts.pairTol then
				table.insert(issues, fmt("mirror partner is %.2f studs from the mirrored position", vlen(d)))
				table.insert(fixes, {
					action = "moveBy",
					d = rv(sub(want, pp)),
					note = "moves THIS model onto the mirror of the partner; or move the partner instead",
				})
			end
			local a = { box.dims[1], box.dims[2], box.dims[3] }
			local b = modelBox(other).dims
			b = { b[1], b[2], b[3] }
			table.sort(a)
			table.sort(b)
			local diff = false
			for i = 1, 3 do
				if math.abs(a[i] - b[i]) > opts.cloneSizeTol * math.max(a[i], 0.1) then
					diff = true
				end
			end
			if diff then
				table.insert(
					issues,
					fmt("mirror partner has a different size %s vs %s", listStr(rv(a)), listStr(rv(b)))
				)
			end
			local lk = lookOf(snap.pivot.r)
			lk[ax] = -lk[ax]
			if angleDeg(lk, lookOf(other.pivot.r)) > 5 then
				table.insert(issues, "mirror partner does not face the mirrored direction")
			end
		end
	end
	if group ~= nil then
		local sib = env.siblings or {}
		if #sib >= 1 then
			local me = Core.summary(snap)
			local med = {}
			for i = 1, 3 do
				local col = { me.dims[i] }
				for _, s in sib do
					table.insert(col, s.dims[i])
				end
				med[i] = median(col)
			end
			local counts = { me.partCount }
			for _, s in sib do
				table.insert(counts, s.partCount)
			end
			local medc = median(counts)
			meas.groupMedianSize = rv(med)
			tol.cloneSizeTol = opts.cloneSizeTol
			local diff = false
			for i = 1, 3 do
				if math.abs(me.dims[i] - med[i]) > opts.cloneSizeTol * math.max(med[i], 0.1) then
					diff = true
				end
			end
			if diff then
				table.insert(
					issues,
					fmt("size %s differs from the group median %s", listStr(me.dims), listStr(rv(med)))
				)
			end
			if me.partCount ~= medc then
				table.insert(issues, fmt("%d parts, the group median is %d", me.partCount, medc))
			end
			if group.sameYaw then
				local y0 = sib[1].yaw
				if math.abs(wrap180(me.yaw - y0)) > 1.0 then
					table.insert(issues, fmt("yaw %.1f differs from the group yaw %.1f", me.yaw, y0))
				end
			end
		else
			meas.group = "no siblings found"
		end
	end
	return mk(nstatus(issues), meas, tol, issues, fixes)
end

local CHECKS: { [string]: (Dict, Dict, Dict, Dict) -> Dict } = {
	P1 = checkP1,
	P2 = checkP2,
	P3 = checkP3,
	P4 = checkP4,
	P5 = checkP5,
	P6 = checkP6,
	P7 = checkP7,
}

function Core.verify(snap: Dict, intent: Dict?, env: Dict?, opts: Dict?): Dict
	local it: Dict = intent or {}
	local ev: Dict = env or {}
	local o: Dict = table.clone(Core.DEFAULTS)
	local extra: Dict = opts or {}
	for k, v in extra do
		o[k] = v
	end
	local waive: Dict = it.waive or {}
	local checks: Dict = {}
	local failed: { string }, unverified: { string }, waived: { string } = {}, {}, {}
	for _, cid in Core.ORDER do
		local c = CHECKS[cid](snap, it, ev, o)
		if c.status == "fail" and waive[cid] ~= nil then
			c.waived = tostring(waive[cid])
			table.insert(waived, cid)
		elseif c.status == "fail" then
			table.insert(failed, cid)
		end
		for _, u in c.unverified do
			table.insert(unverified, cid .. ":" .. u)
		end
		checks[cid] = c
	end
	return {
		path = snap.path,
		class = snap.class,
		kind = it.kind or "prop",
		status = if #failed > 0 then "fail" else "pass",
		failed = failed,
		waived = waived,
		unverified = unverified,
		checks = checks,
	}
end

-- exposed for the adapter and the tests
Core.modelBox = modelBox
Core.worldAabb = worldAabb
Core.obbPenetration = obbPenetration
Core.facePoint = facePoint
Core.pathMatches = pathMatches
Core.yawOf = yawOf
Core.lookOf = lookOf
Core.wrap180 = wrap180
Core.r3 = r3

return Core
