--!strict
-- SafeArea: pure inset maths. Feed it the pixel rects of interactive/important UI (AbsolutePosition/AbsoluteSize read in a Client
-- playtest or the device emulator) and the insets, and it returns what pokes into the unsafe margins.
-- Roblox reports the top-left inset and bottom-right inset of the core UI (GuiService:GetGuiInset returns two Vector2); pass them
-- through `fromGuiInset`. Device cutout sizes are NOT in the vault: read them from the emulator, do not assume numbers.
--   local insets = SafeArea.fromGuiInset({ x = 0, y = 58 }, { x = 0, y = 0 })
--   local issues = SafeArea.check(rects, { w = 844, h = 390 }, insets, 12)
local SafeArea = {}

export type Insets = { left: number, top: number, right: number, bottom: number }
export type Rect = { name: string, x: number, y: number, w: number, h: number, important: boolean? }
export type Issue = { name: string, overflow: Insets, severity: string } -- severity: blocker (important) | minor

function SafeArea.fromGuiInset(topLeft: { x: number, y: number }, bottomRight: { x: number, y: number }): Insets
	return { left = topLeft.x, top = topLeft.y, right = bottomRight.x, bottom = bottomRight.y }
end

-- `pad` adds breathing room inside the safe area (px). Returns one Issue per rect that crosses a margin.
function SafeArea.check(rects: { Rect }, viewport: { w: number, h: number }, insets: Insets, pad: number?): { Issue }
	local p = pad or 0
	local issues: { Issue } = {}
	for _, r in rects do
		local o: Insets = {
			left = math.max(0, insets.left + p - r.x),
			top = math.max(0, insets.top + p - r.y),
			right = math.max(0, r.x + r.w - (viewport.w - insets.right - p)),
			bottom = math.max(0, r.y + r.h - (viewport.h - insets.bottom - p)),
		}
		if o.left > 0 or o.top > 0 or o.right > 0 or o.bottom > 0 then
			table.insert(issues, { name = r.name, overflow = o, severity = if r.important then "blocker" else "minor" })
		end
	end
	return issues
end

-- The smallest nudge (px) that brings the rect inside the margins; positive = move right/down.
function SafeArea.nudge(issue: Issue): { x: number, y: number }
	local o = issue.overflow
	return { x = o.left - o.right, y = o.top - o.bottom }
end

return SafeArea
