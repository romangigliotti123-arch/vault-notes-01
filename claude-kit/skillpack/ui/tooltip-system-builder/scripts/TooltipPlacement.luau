--!strict
local TooltipPlacement = {}

export type Rect = { x: number, y: number, w: number, h: number }
export type Size = { w: number, h: number }
export type Insets = { left: number, top: number, right: number, bottom: number }
export type Spot = { x: number, y: number, side: string }

TooltipPlacement.HOVER_DELAY = 0.3
TooltipPlacement.LONG_PRESS = 0.4

function TooltipPlacement.place(anchor: Rect, tip: Size, viewport: Size, insets: Insets?, gap: number?): Spot
	local ins: Insets = insets or { left = 0, top = 0, right = 0, bottom = 0 }
	local g = gap or 8
	local minX, maxX = ins.left, viewport.w - ins.right - tip.w
	local minY, maxY = ins.top, viewport.h - ins.bottom - tip.h
	local cx = anchor.x + anchor.w / 2 - tip.w / 2
	local cy = anchor.y + anchor.h / 2 - tip.h / 2
	local candidates = {
		{ side = "above", x = cx, y = anchor.y - g - tip.h },
		{ side = "below", x = cx, y = anchor.y + anchor.h + g },
		{ side = "right", x = anchor.x + anchor.w + g, y = cy },
		{ side = "left", x = anchor.x - g - tip.w, y = cy },
	}
	for _, c in candidates do
		local vertical = c.side == "above" or c.side == "below"
		local fits = if vertical then (c.y >= minY and c.y <= maxY) else (c.x >= minX and c.x <= maxX)
		if fits then
			return {
				x = math.clamp(c.x, minX, math.max(minX, maxX)),
				y = math.clamp(c.y, minY, math.max(minY, maxY)),
				side = c.side,
			}
		end
	end
	return {
		x = math.clamp(cx, minX, math.max(minX, maxX)),
		y = math.clamp(cy, minY, math.max(minY, maxY)),
		side = "pinned",
	}
end

function TooltipPlacement.shouldShow(inputKind: string, held: number, dismissed: boolean?): boolean
	if dismissed then
		return false
	end
	if inputKind == "mouse" then
		return held >= TooltipPlacement.HOVER_DELAY
	elseif inputKind == "touch" then
		return held >= TooltipPlacement.LONG_PRESS
	end
	return held >= 0
end

return TooltipPlacement
