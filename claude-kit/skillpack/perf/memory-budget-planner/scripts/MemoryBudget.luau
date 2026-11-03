--!strict
-- MemoryBudget: per-device client memory budgets and the server memory formula. Pure logic, Lune-tested.
-- Sources (vault):
--   Client ceiling: scripting-and-performance KB: "ejections rise near 66% of memory (~1.3 GB on a 2 GB device; ~1.4 GB crash)" (creator reports).
--   Whole-game target 400-500 MB: optimization-and-streaming KB overview (creator consensus, indie). Used for the 2 GB tier only.
--   Device mix: Creator Docs test-on-hardware: Android ~65% of players; ~60% of Android have 2-4 GB, ~35% 4-8 GB, ~5% over 8 GB (official).
--   Server: Creator Docs performance-optimization/identify: 6.25 GiB + 100 MiB x max players; keep use under 50 percent. Analytics docs: under 3 GB (official).
-- Tier targets for 3 GB and up are heuristics (scaled from the 2 GB figure by usable ceiling); replace them with measured numbers from the Performance Dashboard.
local MemoryBudget = {}

export type Tier = { ramGB: number, ceilingMB: number, targetMB: number }

local EJECT_FRACTION = 0.66
local TARGET_FRACTION_OF_CEILING = 0.33 -- 450 / 1352 for the 2 GB device, applied to larger tiers as a heuristic
MemoryBudget.WARN_AT = 0.75 -- heuristic: warn at 75 percent of the target's ceiling band

function MemoryBudget.clientTier(ramGB: number): Tier
	local ceiling = ramGB * 1024 * EJECT_FRACTION
	local target = if ramGB <= 2 then 450 else math.floor(ceiling * TARGET_FRACTION_OF_CEILING)
	return { ramGB = ramGB, ceilingMB = math.floor(ceiling), targetMB = target }
end

function MemoryBudget.serverTotalMB(maxPlayers: number): number
	return 6.25 * 1024 + 100 * maxPlayers
end

function MemoryBudget.serverTargetMB(maxPlayers: number): number
	return MemoryBudget.serverTotalMB(maxPlayers) * 0.5
end

-- assess: usedMB against a client tier. ok <= target, warn up to the middle of target..ceiling, risk above, crash-zone at ceiling.
function MemoryBudget.assessClient(usedMB: number, tier: Tier): string
	if usedMB >= tier.ceilingMB then
		return "ejection-zone"
	elseif usedMB > tier.targetMB + (tier.ceilingMB - tier.targetMB) * 0.5 then
		return "risk"
	elseif usedMB > tier.targetMB then
		return "over-target"
	end
	return "ok"
end

function MemoryBudget.assessServer(usedMB: number, maxPlayers: number): string
	if usedMB > MemoryBudget.serverTotalMB(maxPlayers) * 0.5 then
		return "over"
	elseif usedMB > MemoryBudget.serverTotalMB(maxPlayers) * 0.4 then
		return "warn"
	end
	return "ok"
end

-- breakdown: categories {name = MB} (Developer Console Memory tab) -> rows sorted by share, so the biggest cut is first.
function MemoryBudget.breakdown(categories: { [string]: number }): { { name: string, mb: number, share: number } }
	local total = 0
	for _, v in categories do
		total += v
	end
	local rows = {}
	for k, v in categories do
		table.insert(rows, { name = k, mb = v, share = if total > 0 then v / total else 0 })
	end
	table.sort(rows, function(a, b)
		if a.mb ~= b.mb then
			return a.mb > b.mb
		end
		return a.name < b.name
	end)
	return rows
end

return MemoryBudget
