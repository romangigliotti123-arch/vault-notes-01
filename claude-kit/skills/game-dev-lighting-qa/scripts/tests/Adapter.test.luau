--!nocheck
local roblox = require("@lune/roblox")
local serde = require("@lune/serde")
local t = require("../../../../systems/_check/harness")
local LightingKit = require("../LightingKit")

local Instance, Color3, Vector3 = roblox.Instance, roblox.Color3, roblox.Vector3

local boxes = {
	{ min = { -100, -1, -100 }, max = { 100, 0, 100 }, color = { 0.36, 0.58, 0.27 } },
	{ min = { 20, 0, 20 }, max = { 40, 12, 22 }, color = { 0.7, 0.55, 0.4 } },
	{ min = { 20, 0, 38 }, max = { 40, 12, 40 }, color = { 0.7, 0.55, 0.4 } },
	{ min = { 20, 0, 22 }, max = { 22, 12, 38 }, color = { 0.7, 0.55, 0.4 } },
	{ min = { 38, 0, 22 }, max = { 40, 12, 38 }, color = { 0.7, 0.55, 0.4 } },
	{ min = { 20, 12, 20 }, max = { 40, 14, 40 }, color = { 0.45, 0.3, 0.2 } },
	{ min = { -30, 0, -30 }, max = { -26, 20, -26 }, color = { 0.5, 0.5, 0.55 } },
}
local propColors = {
	{ 0.8, 0.2, 0.2 },
	{ 0.2, 0.4, 0.85 },
	{ 0.9, 0.85, 0.3 },
	{ 0.15, 0.15, 0.18 },
	{ 0.78, 0.68, 0.5 },
	{ 0.92, 0.92, 0.92 },
	{ 0.3, 0.2, 0.12 },
}
for i = 0, 6 do
	for j = 0, 6 do
		local x, z = -95 + i * 28, -95 + j * 28
		if not (x + 18 > 15 and x < 45 and z + 18 > 15 and z < 45) and not (i == 2 and j == 2) then
			local h = 4 + ((i * 7 + j * 5) % 14)
			table.insert(
				boxes,
				{ min = { x, 0, z }, max = { x + 18, h, z + 18 }, color = propColors[((i * 3 + j) % #propColors) + 1] }
			)
		end
	end
end
local function approx(a, b, msg)
	t.truthy(math.abs(a - b) < 1e-4, (msg or "approx") .. ": expected " .. tostring(b) .. ", got " .. tostring(a))
end

local function rayBox(o, d, b)
	local tmin, tmax = 0, math.huge
	local n = nil
	for axis = 1, 3 do
		if math.abs(d[axis]) < 1e-9 then
			if o[axis] < b.min[axis] or o[axis] > b.max[axis] then
				return nil
			end
		else
			local t1, t2 = (b.min[axis] - o[axis]) / d[axis], (b.max[axis] - o[axis]) / d[axis]
			local sign = -1
			if t1 > t2 then
				t1, t2 = t2, t1
				sign = 1
			end
			if t1 > tmin then
				tmin = t1
				n = { 0, 0, 0 }
				n[axis] = sign
			end
			tmax = math.min(tmax, t2)
			if tmin > tmax then
				return nil
			end
		end
	end
	if not n then
		return nil
	end
	return tmin, n
end

local root = Instance.new("Folder")
local lighting = Instance.new("Lighting")
local lampPart = Instance.new("Part")
lampPart.Position = Vector3.new(30, 8, 30)
lampPart.Parent = root
local lamp = Instance.new("PointLight")
lamp.Brightness, lamp.Range, lamp.Shadows, lamp.Enabled = 2, 24, true, true
lamp.Parent = lampPart
local technology = "Voxel"
local techWritable = true
local sun = { 0.35, 0.8, 0.5 }
local sl = math.sqrt(sun[1] ^ 2 + sun[2] ^ 2 + sun[3] ^ 2)
sun = { sun[1] / sl, sun[2] / sl, sun[3] / sl }

local function resetLighting()
	for _, c in lighting:GetChildren() do
		c:Destroy()
	end
	lighting.Brightness = 3
	lighting.ClockTime = 14.5
	lighting.GeographicLatitude = 41.7333
	lighting.Ambient = Color3.fromRGB(70, 70, 70)
	lighting.OutdoorAmbient = Color3.fromRGB(70, 70, 70)
	lighting.ColorShift_Top = Color3.fromRGB(0, 0, 0)
	lighting.ColorShift_Bottom = Color3.fromRGB(0, 0, 0)
	lighting.EnvironmentDiffuseScale = 0
	lighting.EnvironmentSpecularScale = 0
	lighting.ExposureCompensation = 0
	lighting.GlobalShadows = true
	lighting.ShadowSoftness = 0.2
	lighting.FogColor = Color3.fromRGB(192, 192, 192)
	lighting.FogStart = 0
	lighting.FogEnd = 100000
	lighting:SetAttribute("LightingKitPreset", nil)
	technology = "Voxel"
end
resetLighting()

local world = {
	lighting = function()
		return lighting
	end,
	camera = function()
		return nil
	end,
	sunDirection = function()
		return sun
	end,
	raycast = function(ox, oy, oz, dx, dy, dz, length)
		local len = math.sqrt(dx * dx + dy * dy + dz * dz)
		local d = { dx / len, dy / len, dz / len }
		local best, bestN, bestBox = math.huge, nil, nil
		for _, b in boxes do
			local tt, n = rayBox({ ox, oy, oz }, d, b)
			if tt and tt > 1e-4 and tt < best and tt <= length then
				best, bestN, bestBox = tt, n, b
			end
		end
		if not bestBox then
			return nil
		end
		return {
			pos = { ox + d[1] * best, oy + d[2] * best, oz + d[3] * best },
			n = bestN,
			color = bestBox.color,
			emissive = bestBox.emissive == true,
		}
	end,
	lights = function()
		local out = {}
		for _, d in root:GetDescendants() do
			if d:IsA("PointLight") then
				local p = d.Parent.Position
				table.insert(out, {
					inst = d,
					class = "PointLight",
					pos = { p.X, p.Y, p.Z },
					Enabled = d.Enabled,
					Brightness = d.Brightness,
					Range = d.Range,
					Shadows = d.Shadows,
				})
			end
		end
		return out
	end,
	stats = function()
		return {
			largeParts = 6,
			largePartsNoShadow = 0,
			bounds = { minX = -100, maxX = 100, minZ = -100, maxZ = 100, top = 20, bottom = -1 },
			spawns = { { 0, 3, 0 } },
		}
	end,
	largeParts = function()
		return {}
	end,
	toColor = function(c)
		return Color3.fromRGB(c[1], c[2], c[3])
	end,
	fromColor = function(c)
		return { math.floor(c.R * 255 + 0.5), math.floor(c.G * 255 + 0.5), math.floor(c.B * 255 + 0.5) }
	end,
	setTechnology = function(_, name)
		if techWritable then
			technology = name
		end
		return techWritable
	end,
	getTechnology = function()
		return technology
	end,
	theme = function()
		return { bg = { 24, 32, 56 }, panel = { 44, 62, 108 }, accent = { 255, 196, 61 }, accent2 = { 64, 200, 190 } }
	end,
	isMobileClient = function()
		return false
	end,
	newInstance = function(class)
		return Instance.new(class)
	end,
	jsonEncode = function(v)
		return serde.encode("json", v)
	end,
	jsonDecode = function(s)
		return serde.decode("json", s)
	end,
	now = function()
		return "2026-11-04T10:00:00Z"
	end,
	datamodel = function()
		return "Edit"
	end,
}
LightingKit.world = world

local function count(class)
	local n = 0
	for _, c in lighting:GetChildren() do
		if c.ClassName == class then
			n += 1
		end
	end
	return n
end

local function why(scan)
	local out = {}
	for _, id in scan.report.failed do
		table.insert(out, id .. ": " .. table.concat(scan.report.checks[id].issues, "; "))
	end
	return table.concat(out, " | ")
end

local function captured(fn)
	local lines = {}
	LightingKit.output = function(s)
		table.insert(lines, s)
	end
	local ok, r = pcall(fn)
	LightingKit.output = print
	if not ok then
		error(r)
	end
	return r, lines
end

t.test("apply obby: the Lighting service and the effect objects match the preset", function()
	resetLighting()
	local r = LightingKit.apply("obby")
	t.eq(r.preset, "obby")
	t.eq(r.time, "day")
	approx(lighting.Brightness, 3.2)
	t.eq(world.fromColor(lighting.OutdoorAmbient)[3], 162)
	t.eq(technology, "Future")
	t.eq(count("Atmosphere"), 1)
	t.eq(count("Sky"), 1)
	t.eq(count("BloomEffect"), 1)
	t.eq(count("ColorCorrectionEffect"), 1)
	t.eq(count("SunRaysEffect"), 1)
	t.eq(count("DepthOfFieldEffect"), 0)
	approx(lighting:FindFirstChildOfClass("Atmosphere").Density, 0.27)
	t.eq(lighting:GetAttribute("LightingKitPreset"), "obby:day")
end)

t.test("apply twice does not duplicate objects; applying another preset replaces the look", function()
	LightingKit.apply("obby")
	LightingKit.apply("open_world")
	t.eq(count("Atmosphere"), 1)
	t.eq(count("BloomEffect"), 1)
	t.eq(count("DepthOfFieldEffect"), 1)
	t.eq(lighting:GetAttribute("LightingKitPreset"), "open_world:day")
	LightingKit.apply("horror", { time = "night", mobile = true })
	t.eq(count("DepthOfFieldEffect"), 0)
	t.eq(count("SunRaysEffect"), 0)
	t.eq(technology, "ShadowMap")
	t.eq(lighting:GetAttribute("LightingKitPreset"), "horror:night:mobile")
end)

t.test("overrides and aliases", function()
	LightingKit.apply(
		"tycoon",
		{ bloom = { Intensity = 0.15 }, sunRays = false, sky = { SkyboxBk = "rbxassetid://7" } }
	)
	t.eq(lighting:GetAttribute("LightingKitPreset"), "simulator:day")
	approx(lighting:FindFirstChildOfClass("BloomEffect").Intensity, 0.15)
	t.eq(count("SunRaysEffect"), 0)
	t.eq(lighting:FindFirstChildOfClass("Sky").SkyboxBk, "rbxassetid://7")
end)

t.test("apply with an unknown preset or time is an error", function()
	t.truthy(not pcall(LightingKit.apply, "nope"))
	t.truthy(not pcall(LightingKit.apply, "obby", { time = "noon" }))
end)

t.test("Technology that cannot be written is reported, not fatal", function()
	techWritable = false
	local r = LightingKit.apply("obby")
	techWritable = true
	local found = false
	for _, s in r.skipped do
		if string.find(s, "Technology", 1, true) then
			found = true
		end
	end
	t.truthy(found, "skipped lists Technology")
end)

t.test("snapshot reads the lighting, effects, lights and samples", function()
	resetLighting()
	LightingKit.apply("obby")
	local st = LightingKit.snapshot()
	t.eq(st.lighting.Technology, "Future")
	approx(st.lighting.Brightness, 3.2)
	t.eq(#st.atmospheres, 1)
	t.eq(#st.blooms, 1)
	t.eq(st.marks.preset, "obby")
	t.eq(st.lightStats.total, 1)
	t.eq(st.lightStats.shadowed, 1)
	t.truthy(#st.samples >= 40, "samples " .. #st.samples)
	local indoor, lit = 0, 0
	for _, s in st.samples do
		if s.indoor then
			indoor += 1
			if s.lightE > 0 then
				lit += 1
			end
		end
	end
	t.truthy(indoor >= 1, "interior samples found under the roof (" .. indoor .. ")")
	t.truthy(lit >= 1, "the lamp lights an interior sample")
end)

t.test("scan of an applied preset passes and emits chunked output that decodes", function()
	resetLighting()
	LightingKit.apply("obby")
	local scan, lines = captured(function()
		return LightingKit.scan({ genre = "obby", game = "demo", scorer = "critic" })
	end)
	t.eq(scan.kind, "lighting-scan")
	t.eq(scan.report.status, "pass", why(scan))
	t.eq(scan.scorer, "critic")
	t.truthy(scan.config.theme ~= nil)
	local parts, total = {}, 0
	local last
	for _, ln in lines do
		local i, n, chunk = string.match(ln, "^LIGHTING_SCAN_PART (%d+)/(%d+) (.*)$")
		if i then
			parts[tonumber(i)] = chunk
			total = tonumber(n)
		end
		last = ln
	end
	t.eq(#parts, total)
	local back = serde.decode("json", table.concat(parts))
	t.eq(back.kind, "lighting-scan")
	t.eq(back.report.status, "pass")
	t.truthy(string.find(last, "LIGHTING: PASS", 1, true), last)
end)

t.test("a default-lighting scene fails L1 L2 L3 and the fixes apply the preset", function()
	resetLighting()
	local scan = LightingKit.scan({ genre = "obby", emit = false })
	t.eq(scan.report.status, "fail")
	t.truthy(table.find(scan.report.failed, "L1") ~= nil)
	t.truthy(table.find(scan.report.failed, "L2") ~= nil)
	local r = LightingKit.applyFixes(scan.report)
	t.truthy(r.rescan)
	t.eq(lighting:GetAttribute("LightingKitPreset"), "obby:day")
	local again = LightingKit.scan({ genre = "obby", emit = false })
	t.eq(again.report.status, "pass", why(again))
end)

t.test("fix(): duplicate effects and a blown bloom are repaired in the loop", function()
	resetLighting()
	LightingKit.apply("obby")
	local extra = Instance.new("BloomEffect")
	extra.Parent = lighting
	lighting:FindFirstChildOfClass("BloomEffect").Intensity = 3
	lighting:FindFirstChildOfClass("BloomEffect").Threshold = 0.3
	local before = LightingKit.scan({ genre = "obby", emit = false })
	t.eq(before.report.status, "fail")
	t.truthy(table.find(before.report.failed, "L11") ~= nil, "L11 duplicates")
	local scan = captured(function()
		return LightingKit.fix({ genre = "obby" })
	end)
	t.eq(scan.report.status, "pass", why(scan))
	t.eq(count("BloomEffect"), 1)
	t.truthy(lighting:FindFirstChildOfClass("BloomEffect").Intensity <= 1.0)
end)

t.test("an unshadowed key light is switched on by the fix", function()
	resetLighting()
	LightingKit.apply("obby")
	lamp.Shadows = false
	local scan = LightingKit.scan({ genre = "obby", emit = false })
	t.truthy(table.find(scan.report.failed, "L7") ~= nil, "L7 fails: " .. table.concat(scan.report.failed, ","))
	LightingKit.applyFixes(scan.report)
	t.eq(lamp.Shadows, true)
	lamp.Shadows = true
end)

t.test("the mobile variant scans clean on a mobile target", function()
	resetLighting()
	LightingKit.apply("sci_fi", { mobile = true })
	local scan = LightingKit.scan({ genre = "sci_fi", platform = "mobile", emit = false })
	t.eq(scan.report.status, "pass", why(scan))
	t.truthy(scan.report.summary.cost <= 7)
end)

t.test("a cold start (no preset mark, no genre) uses generic bands and says so", function()
	resetLighting()
	LightingKit.apply("cartoony")
	lighting:SetAttribute("LightingKitPreset", nil)
	local scan = LightingKit.scan({ emit = false })
	t.eq(scan.report.genre, nil)
	local found = false
	for _, u in scan.report.unverified do
		if string.find(u, "genre", 1, true) then
			found = true
		end
	end
	t.truthy(found)
end)

t.done()
