--!strict
local SafeArea = {}

export type Insets = { left: number, top: number, right: number, bottom: number }
export type Rect = { name: string, x: number, y: number, w: number, h: number, important: boolean? }
export type Issue = { name: string, overflow: Insets, severity: string }

function SafeArea.fromGuiInset(topLeft: { x: number, y: number }, bottomRight: { x: number, y: number }): Insets
	return { left = topLeft.x, top = topLeft.y, right = bottomRight.x, bottom = bottomRight.y }
end

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

function SafeArea.nudge(issue: Issue): { x: number, y: number }
	local o = issue.overflow
	return { x = o.left - o.right, y = o.top - o.bottom }
end

return SafeArea
