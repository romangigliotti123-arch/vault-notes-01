--!strict
local PassCatalogue = {}

export type Entry = {
	name: string,
	id: number,
	benefit: string,
	coreProgress: boolean?,
	onOwned: ((userId: number) -> ())?,
}
export type Pass = { name: string, onOwned: ((userId: number) -> ())? }

function PassCatalogue.build(entries: { Entry }): ({ [number]: Pass }, { string })
	local passes: { [number]: Pass } = {}
	local notes: { string } = {}
	local names: { [string]: boolean } = {}
	for _, e in entries do
		assert(type(e.name) == "string" and e.name ~= "", "pass needs a name")
		assert(not names[e.name], `duplicate pass name {e.name}`)
		assert(type(e.benefit) == "string" and e.benefit ~= "", `pass {e.name} needs a one-line benefit`)
		assert(not e.coreProgress, `pass {e.name} gates core progress: sell convenience or cosmetics instead`)
		names[e.name] = true
		if e.id == 0 then
			table.insert(notes, `pass {e.name}: id 0 (SET IN CREATOR HUB), skipped`)
		else
			assert(passes[e.id] == nil, `duplicate pass id {e.id}`)
			passes[e.id] = { name = e.name, onOwned = e.onOwned }
		end
	end
	return passes, notes
end

function PassCatalogue.listing(entries: { Entry }): { { name: string, benefit: string } }
	local out = {}
	for _, e in entries do
		table.insert(out, { name = e.name, benefit = e.benefit })
	end
	return out
end

return PassCatalogue
