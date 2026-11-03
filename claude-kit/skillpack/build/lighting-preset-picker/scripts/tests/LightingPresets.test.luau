--!nocheck
-- Run: lune run LightingPresets.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local LP = require("../LightingPresets")

t.test("every mood validates on both device tiers", function()
	for _, mood in LP.moods() do
		for _, device in { "pc", "mobile" } do
			t.eq(LP.validate(LP.pick(mood, device)), {}, mood .. "/" .. device)
		end
	end
	t.eq(#LP.moods(), 5)
end)

t.test("mobile strips haze, sun rays and blur and caps bloom", function()
	local pc = LP.pick("bright_cartoon", "pc")
	local mobile = LP.pick("bright_cartoon", "mobile")
	t.truthy(pc.atmosphere.Haze > 0)
	t.eq(mobile.atmosphere.Haze, 0)
	t.eq(mobile.sunRays, nil)
	t.eq(mobile.blur, nil)
	t.truthy(pc.sunRays ~= nil and pc.blur ~= nil)
	t.truthy(LP.pick("warm_sunset", "mobile").bloom.Intensity <= 0.5)
end)

t.test("pick returns a copy, not the shared table", function()
	local a = LP.pick("night", "pc")
	a.lighting.Brightness = 9
	t.eq(LP.pick("night", "pc").lighting.Brightness, 0.5)
end)

t.test("unknown mood or device throws", function()
	t.eq(pcall(LP.pick, "disco", "pc"), false)
	t.eq(pcall(LP.pick, "night", "console"), false)
end)

t.test("validate catches out-of-range values", function()
	local p = LP.pick("night", "pc")
	p.lighting.ClockTime = 30
	p.atmosphere.Density = 2
	t.eq(#LP.validate(p), 2)
end)

t.test("toLuau output is loadable text containing the values", function()
	local text = LP.toLuau(LP.pick("overcast", "mobile"))
	t.truthy(string.find(text, "ClockTime = 12", 1, true))
	t.truthy(string.find(text, "Ambient = { 110, 112, 118 }", 1, true))
	t.eq(string.find(text, "sunRays", 1, true), nil)
end)

t.done()
