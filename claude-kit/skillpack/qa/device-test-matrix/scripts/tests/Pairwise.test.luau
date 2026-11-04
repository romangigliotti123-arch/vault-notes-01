--!nocheck
local t = require("../../../../../systems/_check/harness")
local Pairwise = require("../Pairwise")

local PARAMS = {
	{ name = "Platform", values = { "Phone", "Tablet", "Desktop", "Console" } },
	{ name = "Input", values = { "Touch", "Keyboard", "Gamepad" } },
	{ name = "Graphics", values = { "Low", "Auto", "High" } },
	{ name = "Network", values = { "Good", "Slow", "Lossy" } },
	{ name = "Server", values = { "Solo", "Full" } },
}

print("Pairwise")

t.test("every pair is covered with far fewer rows than the full product", function()
	local r = Pairwise.generate(PARAMS)
	local covered, total = Pairwise.coverage(PARAMS, r.rows)
	t.eq(covered, total)
	t.eq(#r.uncoverable, 0)
	t.truthy(#r.rows < 4 * 3 * 3 * 3 * 2 / 3, "rows " .. #r.rows)
end)

t.test("output is deterministic", function()
	local a = Pairwise.generate(PARAMS)
	local b = Pairwise.generate(PARAMS)
	t.eq(a.rows, b.rows)
end)

t.test("excluded combinations never appear and impossible pairs are reported", function()
	local function exclude(row)
		return (row.Platform == "Console" and row.Input ~= "Gamepad")
			or (row.Platform == "Phone" and row.Input == "Gamepad" and false)
	end
	local r = Pairwise.generate(PARAMS, exclude)
	for _, row in r.rows do
		t.falsy(exclude(row))
	end
	t.eq(#r.uncoverable, 2)
	t.truthy(string.find(r.uncoverable[1], "Console", 1, true))
end)

t.test("two parameters degenerate to the full product", function()
	local p = { { name = "A", values = { "1", "2" } }, { name = "B", values = { "x", "y", "z" } } }
	t.eq(#Pairwise.generate(p).rows, 6)
end)

t.test("coverage reports missing pairs for a hand-picked short list", function()
	local covered, total = Pairwise.coverage(
		PARAMS,
		{ { Platform = "Phone", Input = "Touch", Graphics = "Low", Network = "Good", Server = "Solo" } }
	)
	t.eq(covered, 10)
	t.truthy(total > 10)
end)

t.test("markdown table has a header and one line per row", function()
	local r = Pairwise.generate(PARAMS)
	local md = Pairwise.format(PARAMS, r.rows)
	local lines = 0
	for _ in string.gmatch(md, "[^\n]+") do
		lines += 1
	end
	t.eq(lines, #r.rows + 2)
end)

t.test("a huge product is refused", function()
	local big = {}
	for i = 1, 8 do
		table.insert(big, { name = "P" .. i, values = { "1", "2", "3", "4", "5", "6" } })
	end
	t.falsy(pcall(Pairwise.generate, big))
end)

t.done()
