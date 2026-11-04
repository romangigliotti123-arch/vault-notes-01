--!strict
local ROOT: Instance? = nil
local RATE_CAP = 100
local LIFE_CAP = 20
local LIVE_FLAG = 250
local APPLY_CAP_RATE = false
local MAX_LIST = 10

local ChangeHistoryService = game:GetService("ChangeHistoryService")

local function run(): string
	local roots: { Instance } = if ROOT then { ROOT } else { workspace, game:GetService("ReplicatedStorage") }
	local emitters = 0
	local enabled, totalLive = 0, 0
	local overRate: { ParticleEmitter } = {}
	local flags: { [string]: { string } } = {}
	local function flag(kind: string, inst: Instance)
		local list = flags[kind]
		if not list then
			list = {}
			flags[kind] = list
		end
		table.insert(list, inst:GetFullName())
	end
	local beams, trails = 0, 0
	for _, root in roots do
		for _, inst in root:GetDescendants() do
			if inst:IsA("ParticleEmitter") then
				local e = inst :: ParticleEmitter
				emitters += 1
				local live = e.Rate * math.min(e.Lifetime.Max, LIFE_CAP)
				if e.Enabled then
					enabled += 1
					totalLive += live
					if e.Rate > RATE_CAP then
						table.insert(overRate, e)
						flag(`Rate above {RATE_CAP}/s`, e)
					end
				end
				if e.Lifetime.Max > LIFE_CAP then
					flag(`Lifetime above {LIFE_CAP}s (clamped)`, e)
				end
				if live > LIVE_FLAG then
					flag(`about {LIVE_FLAG}+ live particles from one emitter`, e)
				end
				if e.Texture == "" then
					flag("no Texture (default square)", e)
				end
				if e.LightEmission >= 1 and e.LightInfluence > 0 then
					flag("glow (LightEmission 1) but LightInfluence above 0: it will dim in dark areas", e)
				end
				if e.Enabled and e.Rate > 0 and e.Speed.Max < 1 and e.Lifetime.Max > 5 then
					flag("slow, long-lived and continuous: overdraw trap", e)
				end
			elseif inst:IsA("Beam") then
				beams += 1
			elseif inst:IsA("Trail") then
				trails += 1
			end
		end
	end
	local lines = {
		`PARTICLE AUDIT: emitters={emitters} enabled={enabled} est-live-particles={string.format("%.0f", totalLive)} beams={beams} trails={trails}`,
	}
	for kind, list in flags do
		table.insert(lines, `[{#list}] {kind}`)
		for i = 1, math.min(MAX_LIST, #list) do
			table.insert(lines, `  e.g. {list[i]}`)
		end
	end
	table.insert(
		lines,
		"test each effect at the lowest and the highest Editor Quality Level; one-shot bursts: use Emit(count), not Rate"
	)
	if APPLY_CAP_RATE and #overRate > 0 then
		local recording = ChangeHistoryService:TryBeginRecording("particle-effect-planner cap rate")
		for _, e in overRate do
			e.Rate = RATE_CAP
		end
		if recording then
			ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
		end
		table.insert(lines, `capped Rate to {RATE_CAP} on {#overRate} emitters (one undo step)`)
	else
		table.insert(lines, "read-only run: nothing changed")
	end
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
