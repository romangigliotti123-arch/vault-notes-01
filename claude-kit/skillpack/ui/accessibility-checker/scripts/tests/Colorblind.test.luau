--!nocheck
-- Run: lune run Colorblind.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local C = require("../Colorblind")

t.test("greys are unchanged by simulation (rows sum to ~1)", function()
	for _, kind in { "protan", "deutan", "tritan" } do
		local g = C.simulate({ 128, 128, 128 }, kind)
		t.truthy(math.abs(g[1] - 128) < 2 and math.abs(g[2] - 128) < 2 and math.abs(g[3] - 128) < 2, kind)
	end
end)
t.test("red and green get much closer under deutan/protan", function()
	local red, green = { 220, 40, 40 }, { 40, 160, 40 }
	local normal = C.distance(red, green)
	local deut = C.distance(C.simulate(red, "deutan"), C.simulate(green, "deutan"))
	local prot = C.distance(C.simulate(red, "protan"), C.simulate(green, "protan"))
	t.truthy(deut < normal * 0.6, `deut {deut} vs normal {normal}`)
	t.truthy(prot < normal * 0.6, `prot {prot} vs normal {normal}`)
end)
t.test("collisions reports a red/green team pair but not red/blue", function()
	local hits = C.collisions({
		{ name = "red team", color = { 200, 60, 60 } },
		{ name = "green team", color = { 60, 140, 60 } },
		{ name = "blue team", color = { 40, 60, 220 } },
	})
	local pairsHit = {}
	for _, h in hits do
		pairsHit[h.a .. "/" .. h.b] = true
		t.truthy(h.kind == "protan" or h.kind == "deutan" or h.kind == "tritan")
	end
	t.truthy(pairsHit["red team/green team"])
	t.falsy(pairsHit["red team/blue team"])
end)
t.test("identical-looking pairs are not blamed on colour blindness", function()
	t.eq(C.collisions({ { name = "a", color = { 100, 100, 100 } }, { name = "b", color = { 102, 100, 100 } } }), {})
end)
t.test("colourOnly lists indicators with no second cue", function()
	t.eq(
		C.colourOnly({
			{ name = "team", colors = 2, hasSecondaryCue = false },
			{ name = "rarity", colors = 5, hasSecondaryCue = true },
			{ name = "plain", colors = 1, hasSecondaryCue = false },
		}),
		{ "team" }
	)
end)
t.done()
