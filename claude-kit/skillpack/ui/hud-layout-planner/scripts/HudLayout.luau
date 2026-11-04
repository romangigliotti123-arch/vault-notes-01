--!strict
local HudLayout = {}

export type Rect = { x: number, y: number, w: number, h: number }
export type Element = { name: string, rect: Rect, priority: string, unlockLevel: number? }
export type Insets = { left: number, top: number, right: number, bottom: number }
export type Options = { insets: Insets?, reserved: { Rect }?, maxCoverage: number? }
export type Issue = { kind: string, name: string, other: string? }

HudLayout.DEFAULT_RESERVED = {
	{ x = 0, y = 0.5, w = 0.3, h = 0.5 },
	{ x = 0.7, y = 0.5, w = 0.3, h = 0.5 },
} :: { Rect }

function HudLayout.overlaps(a: Rect, b: Rect): boolean
	return a.x < b.x + b.w and b.x < a.x + a.w and a.y < b.y + b.h and b.y < a.y + a.h
end

function HudLayout.area(r: Rect): number
	return r.w * r.h
end

local function insideInsets(r: Rect, i: Insets): boolean
	return r.x >= i.left and r.y >= i.top and r.x + r.w <= 1 - i.right and r.y + r.h <= 1 - i.bottom
end

function HudLayout.visibleAt(elements: { Element }, level: number): { Element }
	local out = {}
	for _, e in elements do
		if e.unlockLevel == nil or level >= e.unlockLevel then
			table.insert(out, e)
		end
	end
	return out
end

function HudLayout.coverage(elements: { Element }): number
	local total = 0
	for _, e in elements do
		total += HudLayout.area(e.rect)
	end
	return total
end

function HudLayout.check(elements: { Element }, options: Options?): { Issue }
	local opts: Options = options or {}
	local insets: Insets = opts.insets or { left = 0, top = 0, right = 0, bottom = 0 }
	local reserved: { Rect } = opts.reserved or HudLayout.DEFAULT_RESERVED
	local maxCoverage: number = opts.maxCoverage or 0.25
	local issues: { Issue } = {}
	for i, e in elements do
		if not insideInsets(e.rect, insets) then
			table.insert(issues, { kind = "outside-safe-area", name = e.name })
		end
		for _, zone in reserved do
			if HudLayout.overlaps(e.rect, zone) and e.priority ~= "optional" then
				table.insert(issues, { kind = "in-control-zone", name = e.name })
				break
			end
		end
		for j = i + 1, #elements do
			local o = elements[j]
			if HudLayout.overlaps(e.rect, o.rect) then
				table.insert(issues, { kind = "overlap", name = e.name, other = o.name })
			end
		end
	end
	if HudLayout.coverage(elements) > maxCoverage then
		table.insert(issues, { kind = "too-much-screen", name = "HUD" })
	end
	return issues
end

return HudLayout
