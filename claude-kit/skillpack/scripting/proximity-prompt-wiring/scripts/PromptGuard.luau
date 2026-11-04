--!strict
local PromptGuard = {}

export type Pos = { X: number, Y: number, Z: number }
export type Input = {
	player: Pos?,
	prompt: Pos,
	maxDistance: number,
	slack: number?,
	alive: boolean,
}

function PromptGuard.distance(a: Pos, b: Pos): number
	local dx, dy, dz = a.X - b.X, a.Y - b.Y, a.Z - b.Z
	return math.sqrt(dx * dx + dy * dy + dz * dz)
end

function PromptGuard.evaluate(input: Input): (boolean, string?)
	if input.player == nil then
		return false, "no character"
	end
	if not input.alive then
		return false, "dead"
	end
	local limit = input.maxDistance + (input.slack or 3)
	if PromptGuard.distance(input.player, input.prompt) > limit then
		return false, "too far"
	end
	return true, nil
end

export type CooldownsLike = { Try: (self: any, userId: number, action: string, duration: number) -> boolean }
export type Spec = {
	handler: (player: Player) -> (),
	cooldowns: CooldownsLike?,
	action: string?,
	duration: number?,
	slack: number?,
	canUse: ((player: Player) -> (boolean, string?))?,
	onReject: ((player: Player, reason: string) -> ())?,
}

local function toPos(v: Vector3): Pos
	return { X = v.X, Y = v.Y, Z = v.Z }
end

local function promptPosition(prompt: ProximityPrompt): Pos?
	local parent = prompt.Parent
	if parent == nil then
		return nil
	end
	if parent:IsA("BasePart") then
		return toPos(parent.Position)
	elseif parent:IsA("Attachment") then
		return toPos(parent.WorldPosition)
	elseif parent:IsA("Model") then
		return toPos(parent:GetPivot().Position)
	end
	return nil
end

function PromptGuard.bind(prompt: ProximityPrompt, spec: Spec): RBXScriptConnection
	return prompt.Triggered:Connect(function(player: Player)
		local function reject(reason: string)
			if spec.onReject then
				spec.onReject(player, reason)
			end
		end
		local character = player.Character
		local root = character and character:FindFirstChild("HumanoidRootPart")
		local humanoid = character and character:FindFirstChildOfClass("Humanoid")
		local where = promptPosition(prompt)
		if where == nil then
			return reject("prompt has no position")
		end
		local ok, reason = PromptGuard.evaluate({
			player = if root and root:IsA("BasePart") then toPos(root.Position) else nil,
			prompt = where,
			maxDistance = prompt.MaxActivationDistance,
			slack = spec.slack,
			alive = humanoid ~= nil and humanoid.Health > 0,
		})
		if not ok then
			return reject(reason or "rejected")
		end
		if
			spec.cooldowns
			and spec.action
			and not spec.cooldowns:Try(player.UserId, spec.action, spec.duration or 1)
		then
			return reject("cooldown")
		end
		if spec.canUse then
			local allowed, why = spec.canUse(player)
			if not allowed then
				return reject(why or "not allowed")
			end
		end
		spec.handler(player)
	end)
end

return PromptGuard
