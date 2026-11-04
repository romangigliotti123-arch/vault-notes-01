--!strict
local RIG: Model? = nil
local LOAD_TIMEOUT = 5

local RANK: { [string]: number } =
	{ Core = 1, Idle = 2, Movement = 3, Action = 4, Action2 = 5, Action3 = 6, Action4 = 7 }
type Rule = { words: { string }, min: string, max: string, looped: boolean }
local RULES: { Rule } = {
	{ words = { "idle", "stand", "breath" }, min = "Idle", max = "Idle", looped = true },
	{ words = { "walk", "run", "sprint", "swim", "climb" }, min = "Movement", max = "Movement", looped = true },
	{ words = { "jump", "fall", "land" }, min = "Movement", max = "", looped = false },
	{
		words = { "attack", "swing", "punch", "slash", "shoot", "reload", "cast", "emote", "dance", "wave" },
		min = "Action",
		max = "",
		looped = false,
	},
}

local function ruleFor(name: string): Rule?
	local lower = string.lower(name)
	for _, rule in RULES do
		for _, w in rule.words do
			if string.find(lower, w, 1, true) then
				return rule
			end
		end
	end
	return nil
end

local function findAnimator(): Animator?
	if RIG then
		return RIG:FindFirstChildWhichIsA("Animator", true)
	end
	for _, inst in workspace:GetDescendants() do
		if inst:IsA("Animator") then
			return inst
		end
	end
	return nil
end

local function run(): string
	local animator = findAnimator()
	if not animator then
		return "ANIM AUDIT: no Animator found. Run in play mode (server) with a rig in Workspace, or set RIG."
	end
	local lines = { `ANIM AUDIT: rig {animator:GetFullName()}` }
	local checked, issues = 0, 0
	for _, inst in game:GetDescendants() do
		if inst:IsA("Animation") and inst.AnimationId ~= "" then
			local anim = inst :: Animation
			local done, track = false, nil :: AnimationTrack?
			task.spawn(function()
				local ok, result = pcall(function()
					return animator:LoadAnimation(anim)
				end)
				if ok then
					track = result
				end
				done = true
			end)
			local waited = 0
			while not done and waited < LOAD_TIMEOUT do
				waited += task.wait(0.1)
			end
			if track then
				checked += 1
				local priority = track.Priority.Name
				local looped = track.Looped
				local rank = RANK[priority]
				local rule = ruleFor(anim.Name)
				local problems: { string } = {}
				if rule and rank then
					if rank < RANK[rule.min] then
						table.insert(problems, `priority {priority} below {rule.min}`)
					end
					if rule.max ~= "" and rank > RANK[rule.max] then
						table.insert(problems, `priority {priority} above {rule.max}`)
					end
					if rule.looped ~= looped then
						table.insert(problems, if rule.looped then "should loop" else "should not loop")
					end
				elseif not rule and priority == "Core" then
					table.insert(problems, "Core loses to every default animation")
				end
				local verdict = if #problems > 0 then " <- " .. table.concat(problems, "; ") else ""
				local length = string.format("%.2f", track.Length)
				table.insert(lines, `  {anim:GetFullName()}: {priority}, looped={looped}, length={length}s{verdict}`)
				issues += if #problems > 0 then 1 else 0
				track:Destroy()
			else
				table.insert(
					lines,
					`  {anim:GetFullName()}: could not load (not owned by this rig's owner, or id invalid)`
				)
			end
		end
	end
	table.insert(lines, `checked {checked} animations, {issues} with problems; read-only run: nothing changed`)
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
