--!strict
-- FocusNav: directional focus choice and focus-trap detection for controller/TV menus. Pure geometry on screen rectangles.
-- Roblox has built-in selection (GuiService.SelectedObject, NextSelection* properties); use this to PLAN the graph and to test it
-- before wiring `NextSelectionUp/Down/Left/Right`, and as a reference when you must write a custom navigator.
--   local nextId = FocusNav.step(items, "start", "right")
--   local problems = FocusNav.audit(items, "start", "close")
local FocusNav = {}

export type Item = { id: string, x: number, y: number, w: number, h: number }
export type Problems = { unreachable: { string }, noExit: { string }, noBack: boolean }

local function centre(i: Item): (number, number)
	return i.x + i.w / 2, i.y + i.h / 2
end

-- Nearest item in `dir` ("up" | "down" | "left" | "right"). Items must lie in the half-plane of the direction; off-axis distance
-- counts double so a button straight to the right beats a nearer one diagonally. nil when nothing is in that direction.
function FocusNav.step(items: { Item }, fromId: string, dir: string): string?
	local from: Item? = nil
	for _, i in items do
		if i.id == fromId then
			from = i
		end
	end
	if not from then
		return nil
	end
	local fx, fy = centre(from)
	local best: string? = nil
	local bestScore = math.huge
	for _, i in items do
		if i.id ~= fromId then
			local cx, cy = centre(i)
			local dx, dy = cx - fx, cy - fy
			local along, off
			if dir == "right" then
				along, off = dx, dy
			elseif dir == "left" then
				along, off = -dx, dy
			elseif dir == "down" then
				along, off = dy, dx
			else
				along, off = -dy, dx
			end
			if along > 0 then
				local score = along + 2 * math.abs(off)
				if score < bestScore then
					bestScore, best = score, i.id
				end
			end
		end
	end
	return best
end

-- Walk the 4-direction graph from `startId`. unreachable = items focus can never reach; noExit = reachable items with no way
-- onward (dead ends are fine only for a lone item); noBack = `backId` is not reachable from the start.
function FocusNav.audit(items: { Item }, startId: string, backId: string): Problems
	local seen: { [string]: boolean } = { [startId] = true }
	local queue = { startId }
	local noExit = {}
	local head = 1
	while head <= #queue do
		local id = queue[head]
		head += 1
		local exits = 0
		for _, dir in { "up", "down", "left", "right" } do
			local n = FocusNav.step(items, id, dir)
			if n then
				exits += 1
				if not seen[n] then
					seen[n] = true
					table.insert(queue, n)
				end
			end
		end
		if exits == 0 and #items > 1 then
			table.insert(noExit, id)
		end
	end
	local unreachable = {}
	for _, i in items do
		if not seen[i.id] then
			table.insert(unreachable, i.id)
		end
	end
	return { unreachable = unreachable, noExit = noExit, noBack = not seen[backId] }
end

return FocusNav
