--!strict
local MenuGraph = {}

export type Screen = { id: string, entry: boolean?, opens: { string }?, back: string?, closable: boolean? }
export type Report = {
	unreachable: { string },
	trapped: { string },
	brokenLinks: { string },
	deep: { string },
	depth: { [string]: number },
}

function MenuGraph.audit(screens: { Screen }, maxDepth: number?): Report
	local limit = maxDepth or 3
	local byId: { [string]: Screen } = {}
	for _, s in screens do
		byId[s.id] = s
	end
	local report: Report = { unreachable = {}, trapped = {}, brokenLinks = {}, deep = {}, depth = {} }
	local queue: { string } = {}
	for _, s in screens do
		if s.entry then
			report.depth[s.id] = 0
			table.insert(queue, s.id)
		end
	end
	local head = 1
	while head <= #queue do
		local id = queue[head]
		head += 1
		local opens: { string } = byId[id].opens or {}
		for _, to in opens do
			if byId[to] == nil then
				table.insert(report.brokenLinks, `{id} -> {to}`)
			elseif report.depth[to] == nil then
				report.depth[to] = report.depth[id] + 1
				table.insert(queue, to)
			end
		end
	end
	for _, s in screens do
		local d = report.depth[s.id]
		if d == nil then
			table.insert(report.unreachable, s.id)
		else
			if d > limit then
				table.insert(report.deep, s.id)
			end
			local hasExit = s.back ~= nil or s.closable == true or #(s.opens or {}) > 0
			if not s.entry and not hasExit then
				table.insert(report.trapped, s.id)
			end
		end
		if s.back ~= nil and byId[s.back] == nil then
			table.insert(report.brokenLinks, `{s.id} back-> {s.back}`)
		end
	end
	table.sort(report.unreachable)
	table.sort(report.trapped)
	table.sort(report.deep)
	table.sort(report.brokenLinks)
	return report
end

return MenuGraph
