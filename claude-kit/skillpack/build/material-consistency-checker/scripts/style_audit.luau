--!strict
-- style_audit.luau: read-only census of materials and colours in a place, with the rare ones listed as candidate outliers.
-- Paste into the Studio command bar or send through the Studio MCP `execute_luau` tool (datamodel_type Edit).
-- Statistics logic mirrors scripts/StyleStats.luau (tested under Lune). A rare material is a CANDIDATE, not a mistake: check each
-- one against the art bible before changing it. Never edits anything.
local ROOT: Instance? = nil -- nil = Workspace
local MIN_SHARE = 0.02 -- under 2 percent of parts = candidate outlier
local COLOR_STEP = 32 -- colour bucket size per channel
local MAX_LIST = 6

local function bucket(c: Color3): string
	local function q(v: number): number
		return math.min(255, math.floor(v * 255 / COLOR_STEP + 0.5) * COLOR_STEP)
	end
	return string.format("#%02X%02X%02X", q(c.R), q(c.G), q(c.B))
end

local function run(): string
	local root = ROOT or workspace
	local materials: { [string]: number } = {}
	local colors: { [string]: number } = {}
	local examples: { [string]: { string } } = {}
	local total, neon, glass = 0, 0, 0
	local function remember(key: string, inst: Instance)
		local list = examples[key]
		if not list then
			list = {}
			examples[key] = list
		end
		if #list < MAX_LIST then
			table.insert(list, inst:GetFullName())
		end
	end
	for _, inst in root:GetDescendants() do
		if inst:IsA("BasePart") and not inst:IsA("Terrain") and (inst :: BasePart).Transparency < 1 then
			local part = inst :: BasePart
			total += 1
			local m = part.Material.Name
			local c = bucket(part.Color)
			materials[m] = (materials[m] or 0) + 1
			colors[c] = (colors[c] or 0) + 1
			remember("material:" .. m, part)
			remember("color:" .. c, part)
			if part.Material == Enum.Material.Neon then
				neon += 1
			elseif part.Material == Enum.Material.Glass then
				glass += 1
			end
		end
	end
	local function distinct(t: { [string]: number }): number
		local n = 0
		for _ in t do
			n += 1
		end
		return n
	end
	local dm, dc = distinct(materials), distinct(colors)
	local lines = {
		`STYLE AUDIT: {root:GetFullName()} visible parts={total} materials={dm} colour-buckets={dc} neon={neon} glass={glass}`,
	}
	local function rows(label: string, t: { [string]: number }, active: boolean)
		local keys: { string } = {}
		for k in t do
			table.insert(keys, k)
		end
		table.sort(keys, function(a, b)
			return t[a] > t[b]
		end)
		local top: { string } = {}
		for i = 1, math.min(5, #keys) do
			table.insert(top, `{keys[i]} {string.format("%.0f", t[keys[i]] / math.max(total, 1) * 100)}%`)
		end
		table.insert(lines, `top {label}: {table.concat(top, ", ")}`)
		if active then
			for i = #keys, 1, -1 do
				local k = keys[i]
				if t[k] / math.max(total, 1) < MIN_SHARE then
					table.insert(
						lines,
						`  candidate outlier {label} {k}: {t[k]} parts, e.g. {table.concat(
							examples[label .. ":" .. k] or {},
							", "
						)}`
					)
				end
			end
		end
	end
	rows("material", materials, dm > 3)
	rows("color", colors, dc > 5)
	if dm > 6 then
		table.insert(lines, `{dm} materials is a lot: style guides keep a handful`)
	end
	if dc > 12 then
		table.insert(lines, `{dc} colour buckets: tighten the palette (palette-picker)`)
	end
	if neon + glass > 0 then
		table.insert(
			lines,
			`neon/glass parts cost more to render (vault: neon 3/5, glass 3/5 lag in one tester's ratings, indie) - keep them for accents`
		)
	end
	table.insert(lines, "read-only run: nothing changed")
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
