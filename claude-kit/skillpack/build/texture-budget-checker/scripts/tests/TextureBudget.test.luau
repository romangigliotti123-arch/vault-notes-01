--!nocheck
local t = require("../../../../../systems/_check/harness")
local TB = require("../TextureBudget")

t.test("a 1024 square RGBA texture with mips is about 5.3 MB", function()
	local mb = TB.bytes(1024, 1024) / (1024 * 1024)
	t.truthy(math.abs(mb - 5.333) < 0.01, "got " .. mb)
	t.eq(TB.bytes(1024, 1024, 4, false), 4 * 1024 * 1024)
end)

t.test("same id is counted once and uses are added", function()
	local rep = TB.report({
		{ id = "rbxassetid://1", width = 512, height = 512, uses = 3 },
		{ id = "rbxassetid://1", width = 512, height = 512 },
		{ id = "rbxassetid://2", width = 256, height = 256 },
	})
	t.eq(rep.unique, 2)
	t.eq(rep.rows[1].uses, 4)
end)

t.test("rows are sorted by memory and oversize ones are flagged with a 75 percent saving", function()
	local rep = TB.report({
		{ id = "small", width = 128, height = 128 },
		{ id = "big", width = 2048, height = 2048 },
	})
	t.eq(rep.rows[1].id, "big")
	t.truthy(rep.rows[1].flag ~= nil)
	t.falsy(rep.rows[2].flag)
	t.truthy(math.abs(rep.potentialSaveMB - rep.rows[1].mb * 0.75) < 1e-9)
end)

t.test("overBudget follows the budget option", function()
	local items = { { id = "a", width = 2048, height = 2048 } }
	t.truthy(TB.report(items, { budgetMB = 10 }).overBudget)
	t.falsy(TB.report(items, { budgetMB = 100 }).overBudget)
end)

t.test("format mentions the worst texture and the saving", function()
	local text = TB.format(TB.report({ { id = "wall.png", width = 2048, height = 2048 } }))
	t.truthy(string.find(text, "wall.png", 1, true))
	t.truthy(string.find(text, "potential saving", 1, true))
end)

t.done()
