--!strict
-- PassCatalogue: build the `passes` table for the kit's Shop system (systems/Shop) from a readable list, and check it.
-- Shop already verifies ownership with Roblox (never trusting the client or wasPurchased), caches it and exposes HasPass.
--   local PassCatalogue = require(script.Parent.PassCatalogue)
--   local passes, notes = PassCatalogue.build({
--       { name = "VIP", id = 0, benefit = "2x daily reward", onOwned = function(userId) ... end }, -- id 0 = SET IN CREATOR HUB
--   })
--   ShopService.Start({ products = products, passes = passes, getData = ..., saveNow = ... })
--   -- anywhere on the server, at the moment the perk is used:  if ShopService.HasPass(player, "VIP") then ... end
local PassCatalogue = {}

export type Entry = {
	name: string,
	id: number, -- Creator Hub gamepass id; 0 = not created yet (skipped with a note)
	benefit: string, -- one line, what the player gets (kept for the shop UI and the design doc)
	coreProgress: boolean?, -- true = the pass gates core progress or required skill: build() refuses it
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

-- the list the shop UI shows: name + benefit, in catalogue order (the client never receives ids or prices from here)
function PassCatalogue.listing(entries: { Entry }): { { name: string, benefit: string } }
	local out = {}
	for _, e in entries do
		table.insert(out, { name = e.name, benefit = e.benefit })
	end
	return out
end

return PassCatalogue
