--!nocheck
-- Run: lune run InventoryView.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local V = require("../InventoryView")

local items = {
	{ id = "1", name = "Wood Sword", category = "weapon", rarity = 1, qty = 1, acquired = 10 },
	{ id = "2", name = "Fire Sword", category = "weapon", rarity = 4, qty = 1, acquired = 30 },
	{ id = "3", name = "Apple", category = "food", rarity = 1, qty = 12, acquired = 20 },
	{ id = "4", name = "Gone", category = "food", rarity = 1, qty = 0, acquired = 5 },
}
local function ids(list)
	local out = {}
	for _, i in list do
		table.insert(out, i.id)
	end
	return out
end

t.test("zero-quantity items never show", function()
	t.eq(V.view(items).total, 3)
end)
t.test("category, search and rarity filters combine", function()
	t.eq(ids(V.view(items, { category = "weapon", search = "SWORD", minRarity = 2 }).items), { "2" })
end)
t.test("sort modes", function()
	t.eq(ids(V.view(items, { sort = "rarity" }).items), { "2", "3", "1" })
	t.eq(ids(V.view(items, { sort = "qty" }).items), { "3", "2", "1" })
	t.eq(ids(V.view(items, { sort = "newest" }).items), { "2", "3", "1" })
	t.eq(ids(V.view(items, {}).items), { "3", "2", "1" })
end)
t.test("paging clamps the page number", function()
	local p = V.view(items, { pageSize = 2, page = 9 })
	t.eq(p.pages, 2)
	t.eq(p.page, 2)
	t.eq(#p.items, 1)
end)
t.test("toggle: single select replaces, multi adds, same id removes", function()
	t.eq(V.toggle({ "1" }, "2", false), { "2" })
	t.eq(V.toggle({ "1" }, "2", true), { "1", "2" })
	t.eq(V.toggle({ "1", "2" }, "1", true), { "2" })
end)
t.test("reconcile drops sold items", function()
	t.eq(V.reconcile({ "1", "4", "zzz" }, items), { "1" })
end)
t.done()
