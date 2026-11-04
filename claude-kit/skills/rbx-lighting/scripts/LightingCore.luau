--!strict
local Data = require("./LightingData")

local Core = {}

type Dict = { [string]: any }

Core.DATA = Data
local M: Dict = Data.model
local COSTS: Dict = Data.costs
local PRESETS: Dict = Data.presets

Core.ORDER = { "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "L11", "L12" }
Core.NAMES = {
	L1 = "Not the default Roblox lighting",
	L2 = "Atmosphere present and sane",
	L3 = "Sky set",
	L4 = "Post effects in sane ranges",
	L5 = "Colour grading cohesive with the palette",
	L6 = "Scene brightness not crushed or blown",
	L7 = "Shadows on for the key lights",
	L8 = "Fog and haze density suit the genre",
	L9 = "Interiors lit",
	L10 = "Performance budget (mobile and PC)",
	L11 = "No conflicting duplicate effects",
	L12 = "Time of day and exposure coherent",
}
local PHASE_KEYS = { luma_mean = true, crushed_max = true, blown_max = true, spread_min = true, amb_outdoor = true }
local MIN_WAIVER = 10

local function rnd(x: number): number
	return math.floor(x * 1000 + 0.5) / 1000
end

local function clamp(x: number, lo: number, hi: number): number
	return math.max(lo, math.min(hi, x))
end

local function deepcopy(v: any): any
	if type(v) == "table" then
		local out = {}
		for k, x in v :: Dict do
			out[k] = deepcopy(x)
		end
		return out
	end
	return v
end

local function isDict(v: any): boolean
	return type(v) == "table" and (next(v :: Dict)) ~= nil and (v :: { any })[1] == nil
end

function Core.canon(name: any): string?
	if name == nil then
		return nil
	end
	local s = string.lower(tostring(name))
	s = string.gsub(s, "[^a-z0-9]+", "_")
	s = string.gsub(s, "^_+", "")
	s = string.gsub(s, "_+$", "")
	if PRESETS[s] then
		return s
	end
	return Data.aliases[s]
end
local canon = Core.canon

local function merge(base: Dict, patch: Dict): Dict
	local out: Dict = deepcopy(base)
	for k, v in patch do
		if v == false then
			out[k] = false
		elseif isDict(v) and isDict(out[k]) then
			out[k] = merge(out[k], v)
		else
			out[k] = deepcopy(v)
		end
	end
	return out
end
Core.merge = merge

function Core.resolve(preset: any, time: string?, mobile: boolean?, overrides: Dict?): Dict?
	local g = canon(preset)
	if not g then
		return nil
	end
	local p: Dict = PRESETS[g]
	local t = string.lower(time or p.default_time)
	if t ~= "day" and t ~= "golden" and t ~= "night" then
		return nil
	end
	local cfg: Dict = deepcopy(p.base)
	if t ~= p.default_time then
		cfg = merge(cfg, Data.global_times[t] or {})
	end
	cfg = merge(cfg, (p.times and p.times[t]) or {})
	if mobile then
		local mp: Dict = {}
		for k, v in Data.mobile :: Dict do
			if k ~= "note" then
				mp[k] = v
			end
		end
		cfg = merge(cfg, mp)
	end
	if overrides then
		cfg = merge(cfg, overrides)
	end
	return { preset = g, time = t, mobile = if mobile then true else false, desired = cfg }
end

function Core.bands(genre: any, phase: string): Dict
	local b: Dict = deepcopy(Data.bands.generic)
	b = merge(b, Data.bands.phases[phase] or {})
	local g = canon(genre)
	if g then
		local gb: Dict = PRESETS[g].bands or {}
		for k, v in gb do
			if phase == "day" or not PHASE_KEYS[k] then
				b[k] = deepcopy(v)
			end
		end
		local pb: Dict = (PRESETS[g].phase_bands and PRESETS[g].phase_bands[phase]) or {}
		b = merge(b, pb)
	end
	return b
end

local function luma255(c: { number }): number
	return (0.2126 * c[1] + 0.7152 * c[2] + 0.0722 * c[3]) / 255.0
end

local function lumaLin(c: { number }): number
	local g = M.albedo_gamma
	return 0.2126 * (c[1] ^ g) + 0.7152 * (c[2] ^ g) + 0.0722 * (c[3] ^ g)
end

local function hsv(c: { number }): (number, number, number)
	local r, g, b = c[1] / 255.0, c[2] / 255.0, c[3] / 255.0
	local mx, mn = math.max(r, g, b), math.min(r, g, b)
	local d = mx - mn
	local h = 0.0
	if d <= 1e-9 then
		h = 0.0
	elseif mx == r then
		h = 60.0 * (((g - b) / d) % 6)
	elseif mx == g then
		h = 60.0 * ((b - r) / d + 2)
	else
		h = 60.0 * ((r - g) / d + 4)
	end
	local s = if mx <= 1e-9 then 0.0 else d / mx
	return h % 360.0, s, mx
end

local function hueDist(a: number, b: number): number
	local d = math.abs(a - b) % 360.0
	return if d > 180.0 then 360.0 - d else d
end

local function sunInfo(lt: Dict): (number, { number })
	local sd = lt.sunDir
	if sd then
		local n = math.sqrt(sd[1] ^ 2 + sd[2] ^ 2 + sd[3] ^ 2)
		if n == 0 then
			n = 1.0
		end
		local v = { sd[1] / n, sd[2] / n, sd[3] / n }
		return math.deg(math.asin(clamp(v[2], -1, 1))), v
	end
	local lat = math.rad(lt.GeographicLatitude or 41.7333)
	local h = math.rad(((lt.ClockTime or 14.5) - 12.0) * 15.0)
	local up = math.cos(lat) * math.cos(h)
	local v = { -math.sin(h), up, -math.sin(lat) * math.cos(h) }
	return math.deg(math.asin(clamp(up, -1, 1))), v
end

local function phaseOf(elev: number): string
	if elev >= M.day_elev then
		return "day"
	end
	if elev < M.night_elev then
		return "night"
	end
	return "dusk"
end

local function sunUp(elev: number): number
	return clamp((elev - M.sun_ramp_lo) / M.sun_ramp_span, 0.0, 1.0)
end

local function enabled(lst: any): { Dict }
	local out = {}
	for _, x in (lst or {}) :: { Dict } do
		if x.Enabled ~= false then
			table.insert(out, x)
		end
	end
	return out
end

local function firstEnabled(lst: any): Dict?
	return enabled(lst)[1]
end

local function pct(sorted: { number }, q: number): number
	return sorted[math.floor(q * (#sorted - 1)) + 1]
end

local function sampleLuma(smp: Dict, lt: Dict, elev: number, sunv: { number }, sup: number, cc: Dict?): number
	local albL = lumaLin(smp.albedo)
	local indoor = smp.indoor == true
	local lit = smp.lit ~= false
	local n = smp.n or { 0, 1, 0 }
	local nd = 0.0
	if sup > 0 then
		nd = math.max(0.0, n[1] * sunv[1] + n[2] * sunv[2] + n[3] * sunv[3])
	end
	local amb = luma255(if indoor then lt.Ambient else lt.OutdoorAmbient)
	local envd = lt.EnvironmentDiffuseScale or 1
	local sky = (M.sky_amb_base + M.sky_amb_day * sup) * envd * (if indoor then M.indoor_sky_share else 1.0)
	local ambE = amb * M.ambient_gain + sky
	local strength = sup
		* clamp((lt.Brightness or 3) / 3.0, 0.0, 4.0)
		* (0.5 + 0.5 * math.min(1.0, math.max(math.sin(math.rad(elev)), 0.0) * 1.6))
	local sunE = if indoor or not lit then 0.0 else strength * nd * M.sun_gain
	local E = albL * (ambE + sunE)
	if smp.emissive then
		E += M.emissive_gain * (0.4 + albL)
	end
	E += (smp.lightE or 0.0) * albL * M.light_gain
	E *= 2.0 ^ (lt.ExposureCompensation or 0)
	local v = E / (1.0 + M.tone_k * E)
	local out = v ^ (1.0 / M.out_gamma)
	if cc then
		out = (out - 0.5) * (1.0 + (cc.Contrast or 0)) + 0.5 + (cc.Brightness or 0)
	end
	return clamp(out, 0.0, 1.0)
end

local function sceneStats(state: Dict): Dict
	local lt: Dict = state.lighting
	local elev, sunv = sunInfo(lt)
	local sup = sunUp(elev)
	local cc = firstEnabled(state.colorCorrections)
	local vals: { number }, indoorVals: { number } = {}, {}
	local indoorLit = 0
	for _, s in (state.samples or {}) :: { Dict } do
		local L = sampleLuma(s, lt, elev, sunv, sup, cc)
		table.insert(vals, L)
		if s.indoor then
			table.insert(indoorVals, L)
			if (s.lightE or 0) > 0 then
				indoorLit += 1
			end
		end
	end
	local n = #vals
	local out: Dict =
		{ n = n, indoor_n = #indoorVals, indoor_fraction = 0.0, indoor_mean = nil, indoor_lit_fraction = 0.0 }
	if n > 0 then
		local sv = table.clone(vals)
		table.sort(sv)
		local sum, crushed, blown = 0.0, 0, 0
		for _, v in vals do
			sum += v
			if v < M.crushed_luma then
				crushed += 1
			end
			if v > M.blown_luma then
				blown += 1
			end
		end
		out.mean = sum / n
		out.p10 = pct(sv, 0.1)
		out.p50 = pct(sv, 0.5)
		out.p90 = pct(sv, 0.9)
		out.crushed = crushed / n
		out.blown = blown / n
		out.indoor_fraction = #indoorVals / n
		out.spread = out.p90 - out.p10
	end
	if #indoorVals > 0 then
		local s2 = 0.0
		for _, v in indoorVals do
			s2 += v
		end
		out.indoor_mean = s2 / #indoorVals
		out.indoor_lit_fraction = indoorLit / #indoorVals
	end
	return out
end

local function mk(): Dict
	return { status = "pass", measured = {}, tolerance = {}, issues = {}, fixes = {}, unverified = {}, warnings = {} }
end

local function fail(c: Dict, msg: string, fix: Dict?)
	c.status = "fail"
	table.insert(c.issues, msg)
	if fix then
		table.insert(c.fixes, fix)
	end
end

local function setfix(target: string, value: any, note: string?): Dict
	local f: Dict = { action = "set", target = target, value = value }
	if note then
		f.note = note
	end
	return f
end

local function presetFix(ctx: Dict, why: string): Dict
	local g = ctx.genre
	if not g then
		return { action = "applyPreset", preset = "(choose a genre)", note = why }
	end
	return { action = "applyPreset", preset = g, time = ctx.time, mobile = ctx.platform == "mobile", note = why }
end

local function fmt(x: any): string
	if type(x) == "number" then
		if x == math.floor(x) and math.abs(x) < 1e15 then
			return string.format("%d", x)
		end
		local s = string.format("%.3f", x)
		s = string.gsub(s, "0+$", "")
		s = string.gsub(s, "%.$", "")
		return s
	end
	return tostring(x)
end

local function outside(x: number, lo: number, hi: number): boolean
	return x < lo or x > hi
end

local function num(v: any, d: number): number
	return if type(v) == "number" then v else d
end

local function l1(state: Dict, ctx: Dict): Dict
	local c = mk()
	local lt: Dict, D: Dict = state.lighting, Data.roblox_default
	local unchanged: { string } = {}
	local function near(v: number, lst: { number }, tol: number): boolean
		for _, x in lst do
			if math.abs(v - x) <= tol then
				return true
			end
		end
		return false
	end
	local function nearCol(v: { number }, lst: { { number } }): boolean
		for _, x in lst do
			if math.max(math.abs(v[1] - x[1]), math.abs(v[2] - x[2]), math.abs(v[3] - x[3])) <= D.tol_color then
				return true
			end
		end
		return false
	end
	local tracked = 0
	for _, k in { "Brightness", "ClockTime", "ExposureCompensation", "ShadowSoftness" } do
		tracked += 1
		if lt[k] ~= nil and near(lt[k], D[k], D.tol) then
			table.insert(unchanged, k)
		end
	end
	tracked += 1
	if lt.GeographicLatitude ~= nil and near(lt.GeographicLatitude, D.GeographicLatitude, D.tol_lat) then
		table.insert(unchanged, "GeographicLatitude")
	end
	for _, k in { "Ambient", "OutdoorAmbient", "ColorShift_Top", "ColorShift_Bottom" } do
		tracked += 1
		if lt[k] ~= nil and nearCol(lt[k], D[k]) then
			table.insert(unchanged, k)
		end
	end
	local changed = tracked - #unchanged
	local tuned: { string } = {}
	for _, pair in
		{
			{ "Atmosphere", "atmospheres" },
			{ "Bloom", "blooms" },
			{ "ColorCorrection", "colorCorrections" },
			{ "SunRays", "sunRays" },
		}
	do
		if #enabled(state[pair[2]]) > 0 then
			table.insert(tuned, pair[1])
		end
	end
	local marks: Dict = state.marks or {}
	c.measured =
		{ changed = changed, tracked = tracked, unchanged = unchanged, tuned_objects = tuned, preset = marks.preset }
	c.tolerance = { min_changed = D.min_changed, min_tuned_objects = 1 }
	if changed < D.min_changed then
		fail(
			c,
			string.format(
				"only %d of %d lighting properties differ from the Roblox defaults (unchanged: %s): this is the default Roblox look",
				changed,
				tracked,
				table.concat(unchanged, ", ")
			),
			presetFix(ctx, "L1 default lighting")
		)
	end
	if #tuned == 0 then
		fail(
			c,
			"no enabled Atmosphere, Bloom, ColorCorrection or SunRays: nothing shapes the image beyond engine defaults",
			presetFix(ctx, "L1 no post effects")
		)
	end
	local tech = lt.Technology
	if tech == "Voxel" or tech == "Compatibility" or tech == "Legacy" then
		table.insert(
			c.warnings,
			string.format(
				"Technology %s: Future (PC) or ShadowMap (mobile-safe) gives real shadows and lighting",
				tostring(tech)
			)
		)
	end
	return c
end

local function l2(state: Dict, ctx: Dict): Dict
	local c = mk()
	local b: Dict = ctx.bands
	local atm: { Dict } = state.atmospheres or {}
	c.measured = { count = #atm }
	c.tolerance = { count = 1, offset = { 0, 1 }, haze = b.haze, glare = b.glare }
	if #atm == 0 then
		fail(c, "no Atmosphere in Lighting: no depth haze, flat horizon", presetFix(ctx, "L2 add Atmosphere"))
		return c
	end
	local a = atm[1]
	c.measured.Density, c.measured.Offset, c.measured.Haze, c.measured.Glare, c.measured.Color =
		a.Density, a.Offset, a.Haze, a.Glare, a.Color
	if #atm > 1 then
		fail(
			c,
			string.format("%d Atmosphere objects (only one is used; the others fight it)", #atm),
			{ action = "remove", target = "Atmosphere", keep = 1 }
		)
	end
	if num(a.Density, 0) <= 0 then
		fail(
			c,
			string.format("Atmosphere.Density is %s (0 = no atmosphere)", fmt(num(a.Density, 0))),
			presetFix(ctx, "L2 density")
		)
	end
	if outside(num(a.Offset, 0), 0, 1) then
		fail(
			c,
			string.format("Atmosphere.Offset %s outside 0-1", fmt(a.Offset)),
			setfix("Atmosphere.Offset", clamp(num(a.Offset, 0), 0, 1))
		)
	end
	if outside(num(a.Haze, 0), b.haze[1], b.haze[2]) then
		fail(
			c,
			string.format("Atmosphere.Haze %s outside %s-%s", fmt(a.Haze), fmt(b.haze[1]), fmt(b.haze[2])),
			setfix("Atmosphere.Haze", clamp(num(a.Haze, 0), b.haze[1], b.haze[2]))
		)
	end
	if outside(num(a.Glare, 0), b.glare[1], b.glare[2]) then
		fail(
			c,
			string.format("Atmosphere.Glare %s outside %s-%s", fmt(a.Glare), fmt(b.glare[1]), fmt(b.glare[2])),
			setfix("Atmosphere.Glare", clamp(num(a.Glare, 0), b.glare[1], b.glare[2]))
		)
	end
	local col = a.Color
	if col and math.max(col[1], col[2], col[3]) < 8 then
		fail(c, "Atmosphere.Color is black: the haze would swallow the scene", presetFix(ctx, "L2 colour"))
	end
	return c
end

local function l3(state: Dict, ctx: Dict): Dict
	local c = mk()
	local skies: { Dict } = state.skies or {}
	local keys = { "SkyboxBk", "SkyboxDn", "SkyboxFt", "SkyboxLf", "SkyboxRt", "SkyboxUp" }
	c.measured = { count = #skies }
	c.tolerance = { count = 1, textures = 6, sun_size = { 1, 60 } }
	if #skies == 0 then
		fail(c, "no Sky object: the engine falls back to a bare default sky", presetFix(ctx, "L3 add Sky"))
		return c
	end
	local s = skies[1]
	if #skies > 1 then
		fail(
			c,
			string.format("%d Sky objects (only one is used)", #skies),
			{ action = "remove", target = "Sky", keep = 1 }
		)
	end
	local missing: { string } = {}
	local dflt = 0
	for _, k in keys do
		local v = s[k]
		if v == nil or v == "" then
			table.insert(missing, k)
		elseif v == Data.sky_default_textures[k] then
			dflt += 1
		end
	end
	c.measured.missing, c.measured.default_textures, c.measured.StarCount, c.measured.SunAngularSize =
		missing, dflt, s.StarCount, s.SunAngularSize
	if #missing > 0 then
		fail(c, "Sky texture(s) empty: " .. table.concat(missing, ", "), presetFix(ctx, "L3 textures"))
	elseif dflt == 6 then
		table.insert(
			c.warnings,
			"Sky uses the six default Roblox textures: find a sky that matches the art direction (search_asset) and pass it as an override; never invent asset ids"
		)
	end
	local sun = num(s.SunAngularSize, 21)
	if outside(sun, 1, 60) then
		fail(
			c,
			string.format("Sky.SunAngularSize %s outside 1-60", fmt(s.SunAngularSize)),
			setfix("Sky.SunAngularSize", clamp(sun, 1, 60))
		)
	end
	if ctx.phase == "night" and s.CelestialBodiesShown ~= false and num(s.StarCount, 3000) < 500 then
		table.insert(
			c.warnings,
			string.format("night scene with StarCount %s: the sky will look empty", fmt(num(s.StarCount, 0)))
		)
	end
	return c
end

local function l4(state: Dict, ctx: Dict): Dict
	local c = mk()
	local b: Dict = ctx.bands
	local m: Dict = { bloom = {}, colorCorrection = {}, sunRays = {}, depthOfField = {}, blur = {} }
	for _, e in enabled(state.blooms) do
		local thr, size, inten = num(e.Threshold, 2), num(e.Size, 24), num(e.Intensity, 1)
		local idx = inten * (size / 24.0) / math.max(thr, 0.1)
		table.insert(m.bloom, { Intensity = e.Intensity, Size = e.Size, Threshold = e.Threshold, index = rnd(idx) })
		if inten > b.bloom_int_max then
			fail(
				c,
				string.format(
					"Bloom.Intensity %s above %s: highlights bleed over everything",
					fmt(inten),
					fmt(b.bloom_int_max)
				),
				setfix("Bloom.Intensity", b.bloom_int_max * 0.5)
			)
		end
		if thr < b.bloom_thr_min then
			fail(
				c,
				string.format("Bloom.Threshold %s below %s: everything blooms", fmt(thr), fmt(b.bloom_thr_min)),
				setfix("Bloom.Threshold", 1.0)
			)
		end
		if size > b.bloom_size_max then
			fail(
				c,
				string.format("Bloom.Size %s above %s: smeared glow", fmt(size), fmt(b.bloom_size_max)),
				setfix("Bloom.Size", 24)
			)
		end
		if idx > b.bloom_index_max then
			fail(
				c,
				string.format(
					"bloom strength index %s above %s (Intensity x Size/24 / Threshold): blown out",
					fmt(rnd(idx)),
					fmt(b.bloom_index_max)
				),
				setfix("Bloom.Intensity", rnd(b.bloom_index_max * 0.4 * math.max(thr, 0.1) * 24.0 / math.max(size, 1)))
			)
		end
	end
	for _, e in enabled(state.colorCorrections) do
		local tint = e.TintColor or { 255, 255, 255 }
		local _, ts, _ = hsv(tint)
		table.insert(
			m.colorCorrection,
			{ Brightness = e.Brightness, Contrast = e.Contrast, Saturation = e.Saturation, tint_saturation = rnd(ts) }
		)
		local specs: { { any } } =
			{ { "Brightness", b.cc_brightness }, { "Contrast", b.cc_contrast }, { "Saturation", b.cc_saturation } }
		for _, spec in specs do
			local key, lh = spec[1], spec[2]
			local v = num(e[key], 0)
			if outside(v, lh[1], lh[2]) then
				fail(
					c,
					string.format("ColorCorrection.%s %s outside %s to %s", key, fmt(v), fmt(lh[1]), fmt(lh[2])),
					setfix("ColorCorrection." .. key, clamp(v, lh[1], lh[2]))
				)
			end
		end
		if ts > b.cc_tint_sat_max then
			fail(
				c,
				string.format(
					"ColorCorrection.TintColor saturation %s above %s: the whole screen is one colour",
					fmt(rnd(ts)),
					fmt(b.cc_tint_sat_max)
				),
				setfix("ColorCorrection.TintColor", { 255, 255, 255 })
			)
		end
		if num(e.Contrast, 0) > 0.3 and num(e.Saturation, 0) > 0.45 then
			table.insert(
				c.warnings,
				string.format(
					"ColorCorrection Contrast %s and Saturation %s both high: harsh, check the result in Studio",
					fmt(num(e.Contrast, 0)),
					fmt(num(e.Saturation, 0))
				)
			)
		end
	end
	for _, e in enabled(state.sunRays) do
		table.insert(m.sunRays, { Intensity = e.Intensity, Spread = e.Spread })
		if num(e.Intensity, 0.25) > b.sunrays_int_max then
			fail(
				c,
				string.format(
					"SunRays.Intensity %s above %s: white fog around the sun",
					fmt(num(e.Intensity, 0.25)),
					fmt(b.sunrays_int_max)
				),
				setfix("SunRays.Intensity", b.sunrays_int_max * 0.5)
			)
		end
		if num(e.Spread, 1) > b.sunrays_spread_max then
			fail(
				c,
				string.format("SunRays.Spread %s above %s", fmt(num(e.Spread, 1)), fmt(b.sunrays_spread_max)),
				setfix("SunRays.Spread", b.sunrays_spread_max * 0.7)
			)
		end
	end
	for _, e in enabled(state.dofs) do
		table.insert(m.depthOfField, {
			FarIntensity = e.FarIntensity,
			NearIntensity = e.NearIntensity,
			FocusDistance = e.FocusDistance,
			InFocusRadius = e.InFocusRadius,
		})
		if not b.dof_allowed then
			fail(
				c,
				"DepthOfField is enabled but this genre needs a sharp playfield",
				{ action = "remove", target = "DepthOfField" }
			)
			continue
		end
		if num(e.FarIntensity, 0.75) > b.dof_far_max then
			fail(
				c,
				string.format(
					"DepthOfField.FarIntensity %s above %s: blurry gameplay",
					fmt(num(e.FarIntensity, 0.75)),
					fmt(b.dof_far_max)
				),
				setfix("DepthOfField.FarIntensity", b.dof_far_max * 0.4)
			)
		end
		if num(e.NearIntensity, 0.75) > b.dof_near_max then
			fail(
				c,
				string.format(
					"DepthOfField.NearIntensity %s above %s: the avatar blurs",
					fmt(num(e.NearIntensity, 0.75)),
					fmt(b.dof_near_max)
				),
				setfix("DepthOfField.NearIntensity", 0)
			)
		end
		if num(e.InFocusRadius, 30) < b.dof_radius_min then
			fail(
				c,
				string.format(
					"DepthOfField.InFocusRadius %s below %s: the playfield is out of focus",
					fmt(num(e.InFocusRadius, 30)),
					fmt(b.dof_radius_min)
				),
				setfix("DepthOfField.InFocusRadius", 60)
			)
		end
		if num(e.FocusDistance, 0) < b.dof_focus_min then
			fail(
				c,
				string.format(
					"DepthOfField.FocusDistance %s below %s",
					fmt(num(e.FocusDistance, 0)),
					fmt(b.dof_focus_min)
				),
				setfix("DepthOfField.FocusDistance", 90)
			)
		end
	end
	for _, e in enabled(state.blurs) do
		table.insert(m.blur, { Size = e.Size })
		if num(e.Size, 0) > b.blur_max then
			fail(
				c,
				string.format(
					"BlurEffect.Size %s above %s: a menu blur left on during gameplay",
					fmt(num(e.Size, 0)),
					fmt(b.blur_max)
				),
				setfix("Blur.Size", 0)
			)
		end
	end
	c.measured = m
	c.tolerance = {
		bloom_int_max = b.bloom_int_max,
		bloom_thr_min = b.bloom_thr_min,
		bloom_size_max = b.bloom_size_max,
		bloom_index_max = b.bloom_index_max,
		cc_brightness = b.cc_brightness,
		cc_contrast = b.cc_contrast,
		cc_saturation = b.cc_saturation,
		cc_tint_sat_max = b.cc_tint_sat_max,
		sunrays_int_max = b.sunrays_int_max,
		dof_allowed = b.dof_allowed,
		blur_max = b.blur_max,
	}
	return c
end

local function l5(state: Dict, ctx: Dict): Dict
	local c = mk()
	local b: Dict = ctx.bands
	local lt: Dict = state.lighting
	local parts: { { any } } = {}
	local atm = (state.atmospheres or {})[1]
	if atm and atm.Color then
		table.insert(parts, { "Atmosphere.Color", atm.Color })
	end
	local cc = firstEnabled(state.colorCorrections)
	if cc and cc.TintColor then
		table.insert(parts, { "ColorCorrection.TintColor", cc.TintColor })
	end
	if num(lt.FogEnd, 100000) < 100000 and lt.FogColor then
		table.insert(parts, { "Lighting.FogColor", lt.FogColor })
	end
	if lt.OutdoorAmbient then
		table.insert(parts, { "Lighting.OutdoorAmbient", lt.OutdoorAmbient })
	end
	local tints: { { any } } = {}
	for _, p in parts do
		local h, s, v = hsv(p[2])
		if s >= 0.12 and v >= 0.15 then
			table.insert(tints, { p[1], h, s })
		end
	end
	local worst, wa, wb = 0.0, "", ""
	for i = 1, #tints do
		for j = i + 1, #tints do
			local d = hueDist(tints[i][2], tints[j][2])
			if d > worst then
				worst, wa, wb = d, tints[i][1], tints[j][1]
			end
		end
	end
	local meanHue: number? = nil
	if #tints > 0 then
		local sx, sy = 0.0, 0.0
		for _, t in tints do
			sx += math.cos(math.rad(t[2])) * t[3]
			sy += math.sin(math.rad(t[2])) * t[3]
		end
		meanHue = math.deg(math.atan2(sy, sx)) % 360.0
	end
	local names: { string } = {}
	for _, t in tints do
		table.insert(names, t[1])
	end
	c.measured = { tinted = names, max_hue_spread = rnd(worst), mean_hue = if meanHue then rnd(meanHue) else nil }
	c.tolerance = { hue_cohesion_deg = b.hue_cohesion_deg, theme_hue_deg = b.theme_hue_deg }
	if worst > b.hue_cohesion_deg then
		fail(
			c,
			string.format(
				"grading colours fight each other: %s and %s are %s degrees apart in hue (limit %s)",
				wa,
				wb,
				fmt(rnd(worst)),
				fmt(b.hue_cohesion_deg)
			),
			presetFix(ctx, "L5 cohesion")
		)
	end
	local theme: Dict = ctx.theme or {}
	local tkeys: { string } = {}
	for k in theme do
		table.insert(tkeys, k)
	end
	table.sort(tkeys)
	local thues: { { any } } = {}
	for _, k in tkeys do
		local h, s, v = hsv(theme[k])
		if s >= 0.15 and v >= 0.15 then
			table.insert(thues, { k, h } :: { any })
		end
	end
	local th: { { any } } = {}
	for _, t in thues do
		table.insert(th, { t[1], rnd(t[2]) })
	end
	c.measured.theme_hues = th
	if #tkeys == 0 then
		table.insert(c.unverified, "theme (no StyleKit Theme given: palette fit not checked, only internal cohesion)")
	elseif meanHue ~= nil and #thues > 0 then
		local best, comp = 1e9, 1e9
		for _, t in thues do
			best = math.min(best, hueDist(meanHue, t[2]))
			comp = math.min(comp, hueDist(meanHue, (t[2] + 180.0) % 360.0))
		end
		c.measured.nearest_theme_hue_distance = rnd(best)
		c.measured.nearest_complement_distance = rnd(comp)
		if best > b.theme_hue_deg and comp > 30.0 then
			fail(
				c,
				string.format(
					"world grading hue %s is %s degrees from every palette hue and not a complement: it clashes with the UI/art palette",
					fmt(rnd(meanHue)),
					fmt(rnd(best))
				),
				presetFix(ctx, "L5 palette")
			)
		end
	end
	return c
end

local function l6(state: Dict, ctx: Dict): Dict
	local c = mk()
	local b: Dict = ctx.bands
	local st: Dict = ctx.stats
	local shots: { Dict } = state.shots or {}
	c.tolerance = {
		luma_mean = b.luma_mean,
		crushed_max = b.crushed_max,
		blown_max = b.blown_max,
		spread_min = b.spread_min,
		min_samples = M.min_samples,
	}
	local meas: Dict = { n = st.n, method = "estimate" }
	if st.n >= M.min_samples then
		meas.mean, meas.p10, meas.p50, meas.p90 = rnd(st.mean), rnd(st.p10), rnd(st.p50), rnd(st.p90)
		meas.spread, meas.crushed, meas.blown = rnd(st.spread), rnd(st.crushed), rnd(st.blown)
	end
	if #shots > 0 then
		local sm, sc, sb = 0.0, 0.0, 0.0
		for _, s in shots do
			sm += num(s.mean, 0)
			sc += num(s.crushed, 0)
			sb += num(s.blown, 0)
		end
		meas.screenshots =
			{ count = #shots, mean = rnd(sm / #shots), crushed = rnd(sc / #shots), blown = rnd(sb / #shots) }
	end
	c.measured = meas
	if st.n < M.min_samples and #shots == 0 then
		c.status = "skip"
		table.insert(
			c.issues,
			string.format(
				"only %d scene sample(s) (need %d) and no screenshots: brightness cannot be judged",
				st.n,
				M.min_samples
			)
		)
		return c
	end
	local lo, hi = b.luma_mean[1], b.luma_mean[2]
	local lt: Dict = state.lighting
	local ec = num(lt.ExposureCompensation, 0)
	local mid = (lo + hi) / 2.0
	if st.n >= M.min_samples then
		local mean = st.mean
		if mean < lo or mean > hi then
			local stops = clamp(2.2 * math.log(math.max(mid, 0.01) / math.max(mean, 0.01), 2) * 0.8, -2.0, 2.0)
			fail(
				c,
				string.format(
					"estimated mean brightness %s is %s (band %s-%s)",
					fmt(rnd(mean)),
					if mean < lo then "crushed/too dark" else "blown/too bright",
					fmt(lo),
					fmt(hi)
				),
				setfix(
					"Lighting.ExposureCompensation",
					rnd(clamp(ec + stops, -1.5, 1.5)),
					string.format("about %s stops", fmt(rnd(stops)))
				)
			)
		end
		if st.crushed > b.crushed_max then
			fail(
				c,
				string.format(
					"%s%% of the sampled surfaces are crushed black (limit %s%%)",
					fmt(rnd(st.crushed * 100)),
					fmt(rnd(b.crushed_max * 100))
				),
				presetFix(ctx, "L6 crushed shadows: raise Ambient/OutdoorAmbient or add lights")
			)
		end
		if st.blown > b.blown_max then
			fail(
				c,
				string.format(
					"%s%% of the sampled surfaces are blown white (limit %s%%)",
					fmt(rnd(st.blown * 100)),
					fmt(rnd(b.blown_max * 100))
				),
				setfix("Lighting.Brightness", rnd(clamp(num(lt.Brightness, 3) * 0.7, 0.5, 4)), "lower sun brightness")
			)
		end
		if st.spread < b.spread_min then
			fail(
				c,
				string.format(
					"flat image: p90 - p10 = %s (needs %s): no light/shadow separation",
					fmt(rnd(st.spread)),
					fmt(b.spread_min)
				),
				presetFix(ctx, "L6 flat")
			)
		end
	end
	if #shots > 0 then
		local sm: Dict = meas.screenshots
		if sm.mean < lo - 0.04 or sm.mean > hi + 0.04 then
			local stops = clamp(2.2 * math.log(math.max(mid, 0.01) / math.max(sm.mean, 0.01), 2) * 0.8, -2.0, 2.0)
			fail(
				c,
				string.format("screenshot mean luma %s outside %s-%s", fmt(sm.mean), fmt(lo - 0.04), fmt(hi + 0.04)),
				setfix("Lighting.ExposureCompensation", rnd(clamp(ec + stops, -1.5, 1.5)))
			)
		end
		if sm.crushed > b.crushed_max then
			fail(
				c,
				string.format(
					"screenshots: %s%% crushed pixels (limit %s%%)",
					fmt(rnd(sm.crushed * 100)),
					fmt(rnd(b.crushed_max * 100))
				),
				presetFix(ctx, "L6 shots crushed")
			)
		end
		if sm.blown > b.blown_max + 0.05 then
			fail(
				c,
				string.format(
					"screenshots: %s%% blown pixels (limit %s%%)",
					fmt(rnd(sm.blown * 100)),
					fmt(rnd((b.blown_max + 0.05) * 100))
				),
				presetFix(ctx, "L6 shots blown")
			)
		end
	end
	return c
end

local function l7(state: Dict, ctx: Dict): Dict
	local c = mk()
	local lt: Dict = state.lighting
	local ls: Dict = state.lightStats or {}
	local tech = lt.Technology
	local plat = ctx.platform
	local maxs = if plat == "mobile" then COSTS.shadow_lights_mobile else COSTS.shadow_lights_pc
	local large, nocast = num(ls.largeParts, 0), num(ls.largePartsNoShadow, 0)
	local frac = if large > 0 then nocast / large else 0.0
	c.measured = {
		GlobalShadows = lt.GlobalShadows,
		Technology = tech,
		shadow_lights = num(ls.shadowed, 0),
		key_lights = num(ls.keyTotal, 0),
		key_unshadowed = num(ls.keyUnshadowed, 0),
		large_parts = large,
		large_parts_no_cast = nocast,
		large_no_cast_fraction = rnd(frac),
	}
	c.tolerance = { GlobalShadows = true, max_shadow_lights = maxs, large_nocast_max = ctx.bands.large_nocast_max }
	if lt.GlobalShadows == false then
		fail(
			c,
			"Lighting.GlobalShadows is off: no sun shadows, the world looks flat",
			setfix("Lighting.GlobalShadows", true)
		)
	end
	if tech == "Compatibility" or tech == "Legacy" then
		fail(
			c,
			string.format("Technology %s has no dynamic shadows", tostring(tech)),
			setfix("Lighting.Technology", if plat == "mobile" then "ShadowMap" else "Future")
		)
	end
	if tech == "Voxel" then
		table.insert(c.warnings, "Technology Voxel: shadows are blocky; use Future (PC) or ShadowMap")
	end
	if tech == "Future" and num(ls.keyUnshadowed, 0) > 0 then
		fail(
			c,
			string.format("%d key light(s) (Range >= 16, Brightness >= 1) have Shadows off", ls.keyUnshadowed),
			{ action = "setLights", property = "Shadows", value = true, filter = "key" }
		)
	end
	if num(ls.shadowed, 0) > maxs then
		fail(
			c,
			string.format(
				"%d shadow-casting lights (budget %d on %s): turn Shadows off on the least important",
				ls.shadowed,
				maxs,
				plat
			),
			{ action = "setLights", property = "Shadows", value = false, filter = "smallest", keep = maxs }
		)
	end
	if frac > ctx.bands.large_nocast_max then
		fail(
			c,
			string.format(
				"%s%% of large parts have CastShadow off (limit %s%%)",
				fmt(rnd(frac * 100)),
				fmt(rnd(ctx.bands.large_nocast_max * 100))
			),
			{ action = "setParts", property = "CastShadow", value = true, filter = "large" }
		)
	end
	return c
end

local function l8(state: Dict, ctx: Dict): Dict
	local c = mk()
	local b: Dict = ctx.bands
	local atm = (state.atmospheres or {})[1]
	local marks: Dict = state.marks or {}
	if not atm then
		c.status = "skip"
		table.insert(c.issues, "no Atmosphere to judge (see L2)")
		return c
	end
	c.measured = {
		genre = ctx.genre,
		Density = atm.Density,
		Haze = atm.Haze,
		Offset = atm.Offset,
		legacy_FogEnd = state.lighting.FogEnd,
	}
	c.tolerance = { density = b.density, haze = b.haze }
	local d, h = num(atm.Density, 0), num(atm.Haze, 0)
	if not ctx.genre then
		table.insert(c.unverified, "genre (not given, generic bands used)")
	end
	if outside(d, b.density[1], b.density[2]) then
		fail(
			c,
			string.format(
				"Atmosphere.Density %s outside %s-%s for %s: %s",
				fmt(d),
				fmt(b.density[1]),
				fmt(b.density[2]),
				ctx.genre or "generic",
				if d < b.density[1] then "too thin, no depth" else "too thick, the playfield disappears"
			),
			setfix("Atmosphere.Density", rnd((b.density[1] + b.density[2]) / 2.0))
		)
	end
	if outside(h, b.haze[1], b.haze[2]) then
		fail(
			c,
			string.format(
				"Atmosphere.Haze %s outside %s-%s for %s",
				fmt(h),
				fmt(b.haze[1]),
				fmt(b.haze[2]),
				ctx.genre or "generic"
			),
			setfix("Atmosphere.Haze", clamp(h, b.haze[1], b.haze[2]))
		)
	end
	local mp = canon(marks.preset)
	if mp and ctx.genre and mp ~= ctx.genre then
		table.insert(
			c.warnings,
			string.format("scene was set up with the %s preset but the game genre is %s", mp, tostring(ctx.genre))
		)
	end
	return c
end

local function l9(_state: Dict, ctx: Dict): Dict
	local c = mk()
	local b: Dict = ctx.bands
	local st: Dict = ctx.stats
	local f = st.indoor_fraction
	c.measured = {
		indoor_fraction = rnd(f),
		indoor_samples = st.indoor_n,
		indoor_mean = if st.indoor_mean ~= nil then rnd(st.indoor_mean) else nil,
		indoor_lit_fraction = rnd(st.indoor_lit_fraction),
	}
	c.tolerance =
		{ applies_from_indoor_fraction = 0.15, indoor_mean_min = b.interior_luma_min, indoor_lit_fraction_min = 0.3 }
	if f < 0.15 then
		return c
	end
	if st.indoor_mean < b.interior_luma_min then
		fail(
			c,
			string.format(
				"interiors are too dark: mean estimated brightness %s (min %s)",
				fmt(rnd(st.indoor_mean)),
				fmt(b.interior_luma_min)
			),
			{
				action = "addInteriorLights",
				note = "PointLight/SpotLight/SurfaceLight in every room; raise Lighting.Ambient",
			}
		)
	end
	if st.indoor_lit_fraction < 0.3 then
		fail(
			c,
			string.format(
				"only %s%% of interior samples are near a light source: rooms look flat",
				fmt(rnd(st.indoor_lit_fraction * 100))
			),
			{ action = "addInteriorLights", note = "a warm PointLight (Range 16-24, Shadows on) per room" }
		)
	end
	return c
end

local function costOf(state: Dict): number
	local lt: Dict = state.lighting
	local ls: Dict = state.lightStats or {}
	local cost: number = COSTS.technology[lt.Technology] or 0
	for _, pair in
		{
			{ "blooms", "bloom" },
			{ "colorCorrections", "colorCorrection" },
			{ "sunRays", "sunRays" },
			{ "dofs", "depthOfField" },
			{ "blurs", "blur" },
		}
	do
		for _, e in enabled(state[pair[1]]) do
			cost += COSTS[pair[2]]
			if pair[2] == "bloom" and num(e.Size, 24) > COSTS.bloom_big_size then
				cost += COSTS.bloom_big
			end
		end
	end
	if state.atmospheres and #state.atmospheres > 0 then
		cost += COSTS.atmosphere
	end
	local sh = num(ls.shadowed, 0)
	local plain = math.max(0, num(ls.total, 0) - sh)
	cost += sh * (if lt.Technology == "Future" then COSTS.shadow_light_future else COSTS.shadow_light) + plain * COSTS.plain_light
	return cost
end

local function mobileState(state: Dict): Dict
	local s: Dict = deepcopy(state)
	if s.lighting.Technology == "Future" then
		s.lighting.Technology = "ShadowMap"
	end
	s.dofs = {}
	s.sunRays = {}
	return s
end

local function l10(state: Dict, ctx: Dict): Dict
	local c = mk()
	local plat = ctx.platform
	local ls: Dict = state.lightStats or {}
	local cost = costOf(state)
	local mcost = costOf(mobileState(state))
	local budget = if plat == "mobile" then COSTS.budget_mobile else COSTS.budget_pc
	c.measured = {
		platform = plat,
		cost = rnd(cost),
		cost_mobile_variant = rnd(mcost),
		shadow_lights = num(ls.shadowed, 0),
		lights = num(ls.total, 0),
		effects_on = #enabled(state.blooms) + #enabled(state.colorCorrections) + #enabled(state.sunRays) + #enabled(
			state.dofs
		) + #enabled(state.blurs),
	}
	c.tolerance = {
		budget = budget,
		budget_mobile = COSTS.budget_mobile,
		budget_pc = COSTS.budget_pc,
		max_shadow_lights_mobile = COSTS.shadow_lights_mobile,
	}
	if cost > budget then
		fail(
			c,
			string.format(
				"lighting cost %s above the %s budget %s (Technology + effects + lights)",
				fmt(rnd(cost)),
				plat,
				fmt(budget)
			),
			{
				action = "applyPreset",
				preset = ctx.genre or "(choose a genre)",
				time = ctx.time,
				mobile = true,
				note = "mobile-safe variant",
			}
		)
	end
	if plat == "mobile" then
		if #enabled(state.dofs) > 0 then
			fail(c, "DepthOfField on a mobile target", { action = "remove", target = "DepthOfField" })
		end
		if #enabled(state.sunRays) > 0 then
			fail(c, "SunRays on a mobile target", { action = "remove", target = "SunRays" })
		end
		if num(ls.shadowed, 0) > COSTS.shadow_lights_mobile then
			fail(
				c,
				string.format(
					"%d shadow-casting lights on a mobile target (max %d)",
					ls.shadowed,
					COSTS.shadow_lights_mobile
				),
				{
					action = "setLights",
					property = "Shadows",
					value = false,
					filter = "smallest",
					keep = COSTS.shadow_lights_mobile,
				}
			)
		end
	elseif mcost > COSTS.budget_mobile then
		table.insert(
			c.warnings,
			string.format(
				"on phones this scene costs %s (mobile budget %s): offer LightingKit.apply(preset, {mobile = true}) to low-end clients",
				fmt(rnd(mcost)),
				fmt(COSTS.budget_mobile)
			)
		)
	end
	return c
end

local function l11(state: Dict, _ctx: Dict): Dict
	local c = mk()
	local groups: { { any } } = {
		{ "Atmosphere", "atmospheres", false },
		{ "Sky", "skies", false },
		{ "Bloom", "blooms", true },
		{ "ColorCorrection", "colorCorrections", true },
		{ "SunRays", "sunRays", true },
		{ "DepthOfField", "dofs", true },
		{ "Blur", "blurs", true },
	}
	local counts: Dict = {}
	for _, g in groups do
		local lst: { Dict } = if g[3] then enabled(state[g[2]]) else (state[g[2]] or {})
		counts[g[1]] = #lst
		if #lst > 1 then
			local paths: { string } = {}
			for _, x in lst do
				table.insert(paths, tostring(x.path or "?"))
			end
			fail(
				c,
				string.format(
					"%d %s objects%s: only one should exist (paths: %s)",
					#lst,
					g[1],
					if g[3] then " enabled" else "",
					table.concat(paths, ", ")
				),
				{ action = "remove", target = g[1], keep = 1 }
			)
		end
	end
	local lt: Dict = state.lighting
	if state.atmospheres and #state.atmospheres > 0 and num(lt.FogEnd, 100000) < 5000 then
		fail(
			c,
			string.format(
				"Lighting.FogEnd %s (legacy fog) is set while an Atmosphere exists: two haze systems fight",
				fmt(lt.FogEnd)
			),
			setfix("Lighting.FogEnd", 100000)
		)
	end
	c.measured = { counts = counts, FogEnd = num(lt.FogEnd, 100000) }
	c.tolerance = { max_per_class = 1, legacy_fog_with_atmosphere = false }
	return c
end

local function l12(state: Dict, ctx: Dict): Dict
	local c = mk()
	local b: Dict = ctx.bands
	local lt: Dict = state.lighting
	local amb = luma255(lt.OutdoorAmbient)
	local ex = num(lt.ExposureCompensation, 0)
	c.measured = {
		ClockTime = lt.ClockTime,
		sun_elevation = rnd(ctx.elev),
		phase = ctx.phase,
		outdoor_ambient_luma = rnd(amb),
		ExposureCompensation = ex,
		Brightness = lt.Brightness,
	}
	c.tolerance = { amb_outdoor = b.amb_outdoor, exposure = b.exposure }
	if outside(amb, b.amb_outdoor[1], b.amb_outdoor[2]) then
		local why = if amb > b.amb_outdoor[2] then "too bright for " .. ctx.phase else "too dark for " .. ctx.phase
		fail(
			c,
			string.format(
				"OutdoorAmbient luma %s is %s (band %s-%s): time of day and ambient disagree",
				fmt(rnd(amb)),
				why,
				fmt(b.amb_outdoor[1]),
				fmt(b.amb_outdoor[2])
			),
			presetFix(ctx, "L12 ambient vs time")
		)
	end
	if outside(ex, b.exposure[1], b.exposure[2]) then
		fail(
			c,
			string.format("ExposureCompensation %s outside %s to %s", fmt(ex), fmt(b.exposure[1]), fmt(b.exposure[2])),
			setfix("Lighting.ExposureCompensation", clamp(ex, b.exposure[1], b.exposure[2]))
		)
	end
	if ctx.phase == "night" and num(lt.Brightness, 3) > 3.5 then
		fail(
			c,
			string.format(
				"Brightness %s on a night scene: the moon would light it like noon",
				fmt(num(lt.Brightness, 3))
			),
			setfix("Lighting.Brightness", 1.5)
		)
	end
	return c
end

local CHECK_FUNCS = { l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12 }

local function normalizeState(state: Dict): Dict
	local s: Dict = deepcopy(state)
	if not s.lighting then
		s.lighting = {}
	end
	local lt: Dict = s.lighting
	local defaults: { { any } } = {
		{ "Technology", "ShadowMap" },
		{ "Brightness", 3 },
		{ "ClockTime", 14.5 },
		{ "GeographicLatitude", 41.7333 },
		{ "Ambient", { 70, 70, 70 } },
		{ "OutdoorAmbient", { 70, 70, 70 } },
		{ "ColorShift_Top", { 0, 0, 0 } },
		{ "ColorShift_Bottom", { 0, 0, 0 } },
		{ "EnvironmentDiffuseScale", 1 },
		{ "EnvironmentSpecularScale", 1 },
		{ "ExposureCompensation", 0 },
		{ "GlobalShadows", true },
		{ "ShadowSoftness", 0.2 },
		{ "FogEnd", 100000 },
	}
	for _, kv in defaults do
		if lt[kv[1]] == nil then
			lt[kv[1]] = kv[2]
		end
	end
	return s
end

function Core.phaseTime(phase: string): string
	if phase == "day" then
		return "day"
	elseif phase == "dusk" then
		return "golden"
	end
	return "night"
end

function Core.verify(stateIn: Dict, cfgIn: Dict?): Dict
	local cfg: Dict = cfgIn or {}
	local state = normalizeState(stateIn)
	local marks: Dict = state.marks or {}
	local genre = canon(cfg.genre) or canon(marks.preset)
	local elev = sunInfo(state.lighting)
	local phase = phaseOf(elev)
	local platform = cfg.platform or "both"
	local ctx: Dict = {
		genre = genre,
		time = cfg.time or Core.phaseTime(phase),
		phase = phase,
		elev = elev,
		platform = platform,
		bands = Core.bands(genre, phase),
		theme = cfg.theme,
		stats = sceneStats(state),
	}
	for k, v in (cfg.bands or {}) :: Dict do
		ctx.bands[k] = v
	end
	local checks: Dict = {}
	for i, fn in CHECK_FUNCS do
		local cid = Core.ORDER[i]
		local r = fn(state, ctx)
		r.name = Core.NAMES[cid]
		checks[cid] = r
	end
	local waive: Dict = cfg.waive or {}
	local failed: { string }, waived: { string }, unverified: { string }, warnings: { string } = {}, {}, {}, {}
	for _, cid in Core.ORDER do
		local c = checks[cid]
		local skipThis = false
		if c.status == "fail" and waive[cid] ~= nil then
			local reason = string.gsub(tostring(waive[cid]), "^%s+", "")
			reason = string.gsub(reason, "%s+$", "")
			if #reason >= MIN_WAIVER then
				c.waived = reason
				table.insert(waived, cid)
				skipThis = true
			else
				table.insert(
					c.issues,
					string.format("waiver of %s has no real reason (>= %d characters)", cid, MIN_WAIVER)
				)
			end
		end
		if not skipThis then
			if c.status == "fail" then
				table.insert(failed, cid)
			end
			for _, u in c.unverified do
				table.insert(unverified, cid .. ": " .. u)
			end
			for _, w in c.warnings do
				table.insert(warnings, cid .. ": " .. w)
			end
		end
	end
	local skipped: { string } = {}
	for _, cid in Core.ORDER do
		if checks[cid].status == "skip" then
			table.insert(skipped, cid)
		end
	end
	return {
		kind = "lighting-report",
		version = 1,
		genre = genre,
		time = ctx.time,
		phase = phase,
		platform = platform,
		status = if #failed > 0 then "fail" else "pass",
		failed = failed,
		waived = waived,
		skipped = skipped,
		unverified = unverified,
		warnings = warnings,
		checks = checks,
		summary = {
			sun_elevation = rnd(elev),
			cost = checks.L10.measured.cost,
			cost_mobile_variant = checks.L10.measured.cost_mobile_variant,
		},
	}
end

return Core
