--!strict
-- Overlap: pure layout checks over flat UI rectangles (testable with Lune). `ui_overlap.luau` collects the rectangles from Instances.
--   local findings = Overlap.analyse(items, { name = "phone", w = 844, h = 390 }, opts)
-- Item kinds: "text" (visible text), "panel" (visible background or image), "button" (interactive). `order` = draw order, higher draws on top.
-- A rule fires only for items that are NOT in an ancestor/descendant relation (a label inside its own panel is fine).
local Overlap = {}

export type Item = {
	path: string,
	kind: string,
	x: number,
	y: number,
	w: number,
	h: number,
	order: number,
	opaque: boolean?, -- background transparency under 0.1
	popup: boolean?, -- item is a modal/popup/banner root (counted for the one-popup rule)
	textPx: number?, -- rendered text height in pixels
	fg: { number }?, -- text colour r,g,b 0-1
	bg: { number }?, -- nearest opaque ancestor background r,g,b 0-1
}
export type Viewport = { name: string, w: number, h: number }
export type Finding = { rule: string, a: string, b: string?, detail: string }
export type Options = {
	minTextPx: number?,
	overlapShare: number?,
	maxPanelShare: number?,
	maxCoverage: number?,
	topInset: number?,
}

local function isRelated(a: string, b: string): boolean
	return a == b or string.sub(a, 1, #b + 1) == b .. "." or string.sub(b, 1, #a + 1) == a .. "."
end

function Overlap.intersection(a: Item, b: Item): number
	local w = math.min(a.x + a.w, b.x + b.w) - math.max(a.x, b.x)
	local h = math.min(a.y + a.h, b.y + b.h) - math.max(a.y, b.y)
	if w <= 0 or h <= 0 then
		return 0
	end
	return w * h
end

local function channel(c: number): number
	if c <= 0.03928 then
		return c / 12.92
	end
	return ((c + 0.055) / 1.055) ^ 2.4
end

local function luminance(c: { number }): number
	return 0.2126 * channel(c[1]) + 0.7152 * channel(c[2]) + 0.0722 * channel(c[3])
end

-- WCAG contrast ratio, 1 to 21.
function Overlap.contrast(a: { number }, b: { number }): number
	local la, lb = luminance(a), luminance(b)
	return (math.max(la, lb) + 0.05) / (math.min(la, lb) + 0.05)
end

local function fmt(n: number): string
	return string.format("%.0f", n)
end

function Overlap.analyse(items: { Item }, vp: Viewport, opts: Options?): { Finding }
	local o: Options = opts or {}
	local minText = o.minTextPx or 14
	local share = o.overlapShare or 0.05
	local maxPanel = o.maxPanelShare or 0.35
	local maxCover = o.maxCoverage or 0.4
	local top = o.topInset or 0
	local out: { Finding } = {}
	local vpArea = vp.w * vp.h
	local covered = 0
	local popups: { string } = {}

	for _, it in items do
		-- off screen (2 px slack); the top inset belongs to the Roblox top bar
		if it.x < -2 or it.y < top - 2 or it.x + it.w > vp.w + 2 or it.y + it.h > vp.h + 2 then
			table.insert(out, {
				rule = "off-screen",
				a = it.path,
				detail = `rect {fmt(it.x)},{fmt(it.y)} {fmt(it.w)}x{fmt(it.h)} leaves the {vp.w}x{vp.h} viewport`,
			})
		end
		local px = it.textPx
		if px ~= nil then
			if px < minText then
				table.insert(
					out,
					{ rule = "small-text", a = it.path, detail = `{fmt(px)}px under {minText}px at {vp.name}` }
				)
			end
			if it.fg and it.bg then
				local ratio = Overlap.contrast(it.fg, it.bg)
				local need = if px >= 24 then 3 else 4.5
				if ratio < need then
					table.insert(out, {
						rule = "low-contrast",
						a = it.path,
						detail = string.format("contrast %.1f:1 under %.1f:1", ratio, need),
					})
				end
			end
		end
		if it.kind == "panel" and not it.popup then
			local a = it.w * it.h
			covered += a
			if a / vpArea > maxPanel then
				table.insert(out, {
					rule = "panel-too-big",
					a = it.path,
					detail = string.format("%.0f%% of the screen", 100 * a / vpArea),
				})
			end
		end
		if it.popup then
			table.insert(popups, it.path)
		end
		-- thumbstick and jump zones (phone-sized viewports only): keep interactive items out of the bottom 45% of the outer 25% strips
		if it.kind == "button" and vp.w <= 1000 then
			local left =
				{ path = "", kind = "zone", x = 0, y = vp.h * 0.55, w = vp.w * 0.25, h = vp.h * 0.45, order = 0 }
			local right = {
				path = "",
				kind = "zone",
				x = vp.w * 0.75,
				y = vp.h * 0.55,
				w = vp.w * 0.25,
				h = vp.h * 0.45,
				order = 0,
			}
			local small = it.w * it.h
			if Overlap.intersection(it, left) > 0.2 * small or Overlap.intersection(it, right) > 0.2 * small then
				table.insert(
					out,
					{ rule = "touch-zone", a = it.path, detail = "button sits in the thumbstick or jump zone" }
				)
			end
		end
	end

	for i = 1, #items do
		for j = i + 1, #items do
			local a, b = items[i], items[j]
			if not isRelated(a.path, b.path) then
				local area = Overlap.intersection(a, b)
				if area > 0 then
					local smaller = math.min(a.w * a.h, b.w * b.h)
					if smaller > 0 and area / smaller > share then
						local top_, under = a, b
						if b.order > a.order then
							top_, under = b, a
						end
						local rule = "overlap"
						local detail = string.format(
							"%s %s covers %.0f%% of %s %s",
							top_.kind,
							top_.path,
							100 * area / smaller,
							under.kind,
							under.path
						)
						if top_.opaque and under.kind ~= "panel" and area / (under.w * under.h) > 0.5 then
							rule = "hidden-behind"
							detail = string.format(
								"%s %s is %.0f%% hidden behind %s",
								under.kind,
								under.path,
								100 * area / (under.w * under.h),
								top_.path
							)
						end
						table.insert(out, { rule = rule, a = a.path, b = b.path, detail = detail })
					end
				end
			end
		end
	end

	if covered / vpArea > maxCover then
		table.insert(out, {
			rule = "ui-coverage",
			a = "HUD",
			detail = string.format("panels cover %.0f%% of the screen", 100 * covered / vpArea),
		})
	end
	if #popups > 1 then
		table.insert(
			out,
			{ rule = "popup-stack", a = popups[1], b = popups[2], detail = `{#popups} popups visible at once` }
		)
	end
	return out
end

return Overlap
