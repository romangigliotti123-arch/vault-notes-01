--!strict
-- InventoryView: filter, sort, page and selection for an item grid. Pure over plain item tables, so the UI only renders the
-- returned page. Ownership truth stays on the server (kit PlayerData); this is the client view model.
--   local page = InventoryView.view(items, { category = "weapon", search = "sw", sort = "rarity", page = 1, pageSize = 20 })
--   selection = InventoryView.toggle(selection, id, true)     -- multi-select; false = single select
--   selection = InventoryView.reconcile(selection, items)     -- drop ids that no longer exist (sold, traded)
local InventoryView = {}

export type Item = { id: string, name: string, category: string, rarity: number, qty: number, acquired: number }
export type Query = {
	category: string?,
	search: string?,
	minRarity: number?,
	sort: string?, -- "name" | "rarity" | "qty" | "newest"
	page: number?,
	pageSize: number?,
}
export type Page = { items: { Item }, total: number, pages: number, page: number }

local function lessFor(sort: string): (Item, Item) -> boolean
	if sort == "rarity" then
		return function(a, b)
			if a.rarity ~= b.rarity then
				return a.rarity > b.rarity
			end
			return a.name < b.name
		end
	elseif sort == "qty" then
		return function(a, b)
			if a.qty ~= b.qty then
				return a.qty > b.qty
			end
			return a.name < b.name
		end
	elseif sort == "newest" then
		return function(a, b)
			if a.acquired ~= b.acquired then
				return a.acquired > b.acquired
			end
			return a.id < b.id
		end
	end
	return function(a, b)
		if a.name ~= b.name then
			return a.name < b.name
		end
		return a.id < b.id
	end
end

function InventoryView.view(items: { Item }, query: Query?): Page
	local q: Query = query or {}
	local needle = if q.search then string.lower(q.search) else nil
	local matched: { Item } = {}
	for _, it in items do
		local ok = it.qty > 0
		if ok and q.category and it.category ~= q.category then
			ok = false
		end
		if ok and q.minRarity and it.rarity < q.minRarity then
			ok = false
		end
		if ok and needle and not string.find(string.lower(it.name), needle, 1, true) then
			ok = false
		end
		if ok then
			table.insert(matched, it)
		end
	end
	table.sort(matched, lessFor(q.sort or "name"))
	local size = math.max(1, q.pageSize or 20)
	local pages = math.max(1, math.ceil(#matched / size))
	local page = math.clamp(q.page or 1, 1, pages)
	local out: { Item } = {}
	for i = (page - 1) * size + 1, math.min(#matched, page * size) do
		table.insert(out, matched[i])
	end
	return { items = out, total = #matched, pages = pages, page = page }
end

function InventoryView.toggle(selection: { string }, id: string, multi: boolean): { string }
	for i, s in selection do
		if s == id then
			local copy = table.clone(selection)
			table.remove(copy, i)
			return copy
		end
	end
	if multi then
		local copy = table.clone(selection)
		table.insert(copy, id)
		return copy
	end
	return { id }
end

function InventoryView.reconcile(selection: { string }, items: { Item }): { string }
	local have: { [string]: boolean } = {}
	for _, it in items do
		if it.qty > 0 then
			have[it.id] = true
		end
	end
	local out = {}
	for _, s in selection do
		if have[s] then
			table.insert(out, s)
		end
	end
	return out
end

return InventoryView
