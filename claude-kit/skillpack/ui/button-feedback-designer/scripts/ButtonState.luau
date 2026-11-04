--!strict
local ButtonState = {}
ButtonState.__index = ButtonState

export type State = "idle" | "hover" | "pressed" | "disabled" | "loading" | "owned"
export type Button = typeof(setmetatable({} :: { state: State, over: boolean }, ButtonState))

ButtonState.ALL_STATES = { "idle", "hover", "pressed", "disabled", "loading", "owned" }

function ButtonState.new(): Button
	return setmetatable({ state = "idle" :: State, over = false }, ButtonState)
end

local function locked(s: State): boolean
	return s == "disabled" or s == "loading" or s == "owned"
end

function ButtonState.send(self: Button, event: string): boolean
	if event == "disable" then
		self.state = "disabled"
	elseif event == "load" then
		self.state = "loading"
	elseif event == "own" then
		self.state = "owned"
	elseif event == "enable" or event == "done" then
		if locked(self.state) then
			self.state = if self.over then "hover" else "idle"
		end
	elseif locked(self.state) then
		if event == "enter" then
			self.over = true
		elseif event == "leave" then
			self.over = false
		end
	elseif event == "enter" then
		self.over = true
		if self.state == "idle" then
			self.state = "hover"
		end
	elseif event == "leave" then
		self.over = false
		self.state = "idle"
	elseif event == "down" then
		self.state = "pressed"
	elseif event == "up" then
		local fired = self.state == "pressed" and self.over
		self.state = if self.over then "hover" else "idle"
		return fired
	end
	return false
end

function ButtonState.tap(self: Button): boolean
	self:send("enter")
	self:send("down")
	local fired = self:send("up")
	self:send("leave")
	return fired
end

function ButtonState.missingStyles(styles: { [string]: any }): { string }
	local missing = {}
	for _, s in ButtonState.ALL_STATES do
		if styles[s] == nil then
			table.insert(missing, s)
		end
	end
	return missing
end

return ButtonState
