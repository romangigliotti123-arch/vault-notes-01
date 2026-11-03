--!strict
-- TextureBudget: estimate texture memory from an inventory and rank the biggest wins. Pure logic, unit-tested under Lune.
-- Studio cannot read image sizes from an asset id, so the inventory (scripts/texture_inventory.luau) lists ids and where they are used,
-- and the owner supplies width/height (Asset Manager, the image file, or the Developer Console texture memory tab).
-- The byte model is an ESTIMATE: width * height * bytesPerPixel * 4/3 for mip maps. Vault: a 1024x1024 texture is "about 5 MB"
-- regardless of PNG file size (2018 DevForum figure), one resident 1024 SurfaceAppearance set about 2.8 MB. Confirm with the
-- Developer Console (Place memory, graphics texture) before acting on a number.
local TextureBudget = {}

export type Item = { id: string, width: number, height: number, uses: number?, kind: string? }
export type Row = {
	id: string,
	kind: string,
	width: number,
	height: number,
	uses: number,
	mb: number,
	flag: string?,
	saveMB: number,
}
export type Report = { totalMB: number, unique: number, rows: { Row }, overBudget: boolean, potentialSaveMB: number }

export type Options = { bytesPerPixel: number?, mips: boolean?, maxSide: number?, budgetMB: number? }

function TextureBudget.bytes(width: number, height: number, bytesPerPixel: number?, mips: boolean?): number
	local bpp = bytesPerPixel or 4
	local factor = if mips == false then 1 else 4 / 3
	return width * height * bpp * factor
end

-- Items with the same id are one texture in memory: merged, uses added up, largest size kept.
function TextureBudget.report(items: { Item }, opts: Options?): Report
	local o: Options = opts or {}
	local maxSide = o.maxSide or 1024
	local budgetMB = o.budgetMB or 200 -- the skill's own default, not a platform number
	local merged: { [string]: Row } = {}
	local order: { string } = {}
	for _, it in items do
		local mb = TextureBudget.bytes(it.width, it.height, o.bytesPerPixel, o.mips) / (1024 * 1024)
		local row = merged[it.id]
		if not row then
			row = {
				id = it.id,
				kind = it.kind or "texture",
				width = it.width,
				height = it.height,
				uses = 0,
				mb = mb,
				saveMB = 0,
			}
			merged[it.id] = row
			table.insert(order, it.id)
		end
		row.uses += it.uses or 1
		if mb > row.mb then
			row.mb, row.width, row.height = mb, it.width, it.height
		end
	end
	local rows: { Row } = {}
	local total, save = 0, 0
	for _, id in order do
		local row = merged[id]
		total += row.mb
		if math.max(row.width, row.height) > maxSide then
			-- halving both sides keeps a quarter of the memory
			row.flag = `{row.width}x{row.height} above {maxSide}: halve it if it is not seen up close`
			row.saveMB = row.mb * 0.75
			save += row.saveMB
		end
		table.insert(rows, row)
	end
	table.sort(rows, function(a, b)
		if a.mb ~= b.mb then
			return a.mb > b.mb
		end
		return a.id < b.id
	end)
	return {
		totalMB = total,
		unique = #rows,
		rows = rows,
		overBudget = total > budgetMB,
		potentialSaveMB = save,
	}
end

function TextureBudget.format(rep: Report, top: number?): string
	local lines = {
		string.format(
			"TEXTURE BUDGET: %d unique, ~%.1f MB estimated%s",
			rep.unique,
			rep.totalMB,
			rep.overBudget and " (OVER BUDGET)" or ""
		),
	}
	for i, r in rep.rows do
		if i > (top or 10) then
			break
		end
		table.insert(
			lines,
			string.format(
				"  %6.2f MB  %-9s %dx%d x%d uses  %s%s",
				r.mb,
				r.kind,
				r.width,
				r.height,
				r.uses,
				r.id,
				r.flag and ("  <- " .. r.flag) or ""
			)
		)
	end
	table.insert(lines, string.format("potential saving from oversize textures: ~%.1f MB", rep.potentialSaveMB))
	return table.concat(lines, "\n")
end

return TextureBudget
