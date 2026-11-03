--!strict
-- LodPlan: choose a streaming mode and level-of-detail setting per model from facts about it. Pure logic, unit-tested under Lune.
-- Vault (optimization KB, Creator Docs 2026-10): SLIM on static models only; Persistent sparingly and for always-needed content;
-- Atomic when scripts need all child parts together; Improved streaming behaviour is the workspace default to aim for;
-- keep models small (docs say about 64 studs of extent: live-check the number, it is the docs' wording).
local LodPlan = {}

export type Model = {
	name: string,
	parts: number,
	scripted: boolean?, -- a script reads many of its children at once
	dynamic: boolean?, -- moved, animated or edited at runtime
	essential: boolean?, -- must always exist for every client (spawn, shop, tutorial room)
	extent: number?, -- largest bounding-box side in studs
}
export type Decision = { name: string, streamingMode: string, slim: boolean, notes: { string } }

LodPlan.MAX_EXTENT = 64

function LodPlan.classify(m: Model, maxExtent: number?): Decision
	local limit = maxExtent or LodPlan.MAX_EXTENT
	local notes: { string } = {}
	local mode = "Default"
	if m.essential then
		mode = "Persistent"
		table.insert(notes, "Persistent: never streams out, use sparingly")
	elseif m.scripted then
		mode = "Atomic"
		table.insert(notes, "Atomic: parts load together so the script can WaitForChild only the model")
	end
	local slim = not m.dynamic and not m.essential
	if m.dynamic then
		table.insert(notes, "dynamic: leave level of detail on its default, SLIM is for static models")
	end
	if m.extent and m.extent > limit then
		table.insert(notes, `extent {m.extent} studs: split into smaller models (guide {limit})`)
	end
	if m.parts >= 2000 then
		table.insert(notes, `{m.parts} parts in one model: split before relying on streaming`)
	end
	return { name = m.name, streamingMode = mode, slim = slim, notes = notes }
end

export type Summary = { decisions: { Decision }, persistent: number, atomic: number, slim: number, warnings: { string } }

function LodPlan.plan(models: { Model }, maxExtent: number?): Summary
	local decisions: { Decision } = {}
	local persistent, atomic, slim = 0, 0, 0
	for _, m in models do
		local d = LodPlan.classify(m, maxExtent)
		table.insert(decisions, d)
		if d.streamingMode == "Persistent" then
			persistent += 1
		elseif d.streamingMode == "Atomic" then
			atomic += 1
		end
		if d.slim then
			slim += 1
		end
	end
	local warnings: { string } = {}
	if #models > 0 and persistent / #models > 0.1 then
		table.insert(warnings, `{persistent} of {#models} models Persistent: overuse hurts performance`)
	end
	return { decisions = decisions, persistent = persistent, atomic = atomic, slim = slim, warnings = warnings }
end

return LodPlan
