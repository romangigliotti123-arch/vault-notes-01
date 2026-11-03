--!strict
-- Cluster: find groups of static parts that are worth merging into one mesh. Pure logic, unit-tested under Lune.
-- Input is a flat list of parts (scripts/dump_parts.luau prints it from Studio). Parts are grouped by grid cell + material + colour;
-- a group of at least `minParts` anchored, non-interactive parts is a candidate: one exported mesh replaces many parts
-- (vault: "combine groups of meshes into one asset late in development, example 8 draw calls to 1"; it locks per-part editing,
-- so merge LATE and keep the source model). Cell size and minParts are the skill's defaults, not platform numbers.
local Cluster = {}

export type Part = {
	name: string,
	x: number,
	y: number,
	z: number,
	material: string,
	color: string, -- hex or any stable string
	anchored: boolean,
	interactive: boolean?, -- touched, clicked, scripted, tagged, or moved at runtime
	meshId: string?, -- non-empty for MeshParts
}
export type Group = { key: string, count: number, saves: number, names: { string } }
export type Result = { groups: { Group }, candidates: number, partsMerged: number, skipped: { [string]: number } }

function Cluster.cellOf(v: number, cell: number): number
	return math.floor(v / cell)
end

function Cluster.find(parts: { Part }, cell: number?, minParts: number?): Result
	local size = cell or 64
	local minCount = minParts or 10
	local buckets: { [string]: { string } } = {}
	local order: { string } = {}
	local skipped = { unanchored = 0, interactive = 0 }
	for _, p in parts do
		if not p.anchored then
			skipped.unanchored += 1
		elseif p.interactive then
			skipped.interactive += 1
		else
			local key = string.format(
				"%d,%d,%d|%s|%s",
				Cluster.cellOf(p.x, size),
				Cluster.cellOf(p.y, size),
				Cluster.cellOf(p.z, size),
				p.material,
				p.color
			)
			local list = buckets[key]
			if not list then
				list = {}
				buckets[key] = list
				table.insert(order, key)
			end
			table.insert(list, p.name)
		end
	end
	local groups: { Group } = {}
	local merged = 0
	for _, key in order do
		local names = buckets[key]
		if #names >= minCount then
			table.insert(groups, { key = key, count = #names, saves = #names - 1, names = names })
			merged += #names - 1
		end
	end
	table.sort(groups, function(a, b)
		if a.count ~= b.count then
			return a.count > b.count
		end
		return a.key < b.key
	end)
	return { groups = groups, candidates = #groups, partsMerged = merged, skipped = skipped }
end

return Cluster
