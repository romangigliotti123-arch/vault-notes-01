--!nocheck
-- Run (from the kit's systems folder, where rokit.toml pins lune):
--   lune run ../skills/game-dev-lighting-qa/scripts/tests/Lighting.test.luau [fixtures.json] [--dump out.json]
-- Runs every case of fixtures.json through LightingCore and asserts the hand-written expectations; resolves every preset case. --dump writes all reports and
-- resolved presets as JSON so the Python reference (lighting_ref.py) can be compared field by field (netlify-site/tools/test_lighting.py does that).
local fs = require("@lune/fs")
local process = require("@lune/process")
local serde = require("@lune/serde")
local t = require("../../../../systems/_check/harness")
local Core = require("../LightingCore")

local fixturePath = "../skills/game-dev-lighting-qa/scripts/tests/fixtures.json"
local dumpPath = nil
local args = process.args
local i = 1
while i <= #args do
	if args[i] == "--dump" then
		dumpPath = args[i + 1]
		i += 1
	else
		fixturePath = args[i]
	end
	i += 1
end

local fx = serde.decode("json", fs.readFile(fixturePath))
local dump = { reports = {}, resolved = {} }

local function getNum(rep, key)
	local parts = string.split(key, ".")
	local v = rep.checks[parts[1]]
	for k = 2, #parts do
		local p = parts[k]
		if type(v) == "table" and v[1] ~= nil then
			v = v[tonumber(p) + 1]
		else
			v = v[p]
		end
	end
	return v
end

local function contains(list, needle)
	for _, s in list do
		if string.find(s, needle, 1, true) then
			return true
		end
	end
	return false
end

for _, c in fx.cases do
	t.test(c.name, function()
		local rep = Core.verify(c.state, c.cfg)
		dump.reports[c.name] = rep
		for k, v in c.expect do
			t.eq(rep.checks[k].status, v, k .. " status (" .. table.concat(rep.checks[k].issues, "; ") .. ")")
		end
		if c.status ~= nil then
			t.eq(rep.status, c.status, "overall status, failed: " .. table.concat(rep.failed, ","))
		end
		for k, v in c.num do
			t.eq(getNum(rep, k), v, k)
		end
		for k, a in c.fix do
			local found = false
			for _, f in rep.checks[k].fixes do
				if f.action == a then
					found = true
				end
			end
			t.truthy(found, "fix " .. k .. " should include " .. a)
		end
		for _, w in c.warn do
			t.truthy(contains(rep.warnings, w), "warning " .. w)
		end
		for _, w in c.unverified do
			t.truthy(contains(rep.unverified, w), "unverified " .. w)
		end
	end)
end

for idx, r in fx.resolve do
	t.test("resolve " .. idx .. " " .. tostring(r.preset) .. " " .. tostring(r.time), function()
		local res = Core.resolve(r.preset, r.time, r.mobile, r.overrides)
		dump.resolved[tostring(idx)] = res or "nil"
		if r.preset == "no such preset" or r.time == "noon" then
			t.eq(res, nil)
		else
			t.truthy(res ~= nil, "resolves")
			t.truthy(res.desired.lighting.Technology ~= nil)
			if r.mobile then
				t.eq(res.desired.lighting.Technology, "ShadowMap")
				t.eq(res.desired.depthOfField, false)
				t.eq(res.desired.sunRays, false)
			end
		end
	end)
end

t.test("every check id has a name", function()
	for _, id in Core.ORDER do
		t.truthy(Core.NAMES[id], id)
	end
	t.eq(#Core.ORDER, 12)
end)

t.test("overrides win over the preset and a section can be removed", function()
	local res = Core.resolve(
		"obby",
		"night",
		false,
		{ bloom = { Intensity = 0.2 }, sunRays = false, lighting = { Brightness = 0.9 } }
	)
	t.eq(res.desired.bloom.Intensity, 0.2)
	t.eq(res.desired.sunRays, false)
	t.eq(res.desired.lighting.Brightness, 0.9)
	t.eq(res.time, "night")
end)

t.test("aliases resolve to the canonical genre", function()
	t.eq(Core.canon("Tycoon"), "simulator")
	t.eq(Core.canon("sci-fi"), "sci_fi")
	t.eq(Core.canon("Open World"), "open_world")
	t.eq(Core.canon("nonsense"), nil)
end)

if dumpPath then
	fs.writeFile(dumpPath, serde.encode("json", dump))
end
t.done()
