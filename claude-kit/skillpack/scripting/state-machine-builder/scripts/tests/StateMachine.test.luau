--!nocheck
local t = require("../../../../../systems/_check/harness")
local StateMachine = require("../StateMachine")

local function make(log)
	return StateMachine.new({
		initial = "Idle",
		states = {
			Idle = {
				to = { "Chase" },
				enter = function()
					table.insert(log, "enter Idle")
				end,
			},
			Chase = {
				to = { "Idle", "Attack" },
				enter = function(_, from, target)
					table.insert(log, "enter Chase from " .. tostring(from) .. " target " .. tostring(target))
				end,
				exit = function(_, to)
					table.insert(log, "exit Chase to " .. to)
				end,
			},
			Attack = { to = { "Chase" } },
		},
	}, {})
end

t.test("starts in the initial state and runs its enter hook", function()
	local log = {}
	local m = make(log)
	t.eq(m:Current(), "Idle")
	t.eq(log, { "enter Idle" })
end)

t.test("allowed transitions run exit then enter, with arguments", function()
	local log = {}
	local m = make(log)
	t.truthy(m:Transition("Chase", "player1"))
	t.eq(log[2], "enter Chase from Idle target player1")
	m:Transition("Idle")
	t.eq(log[3], "exit Chase to Idle")
end)

t.test("a transition not in the table is refused and changes nothing", function()
	local m = make({})
	t.falsy(m:Transition("Attack"))
	t.falsy(m:Transition("Nowhere"))
	t.eq(m:Current(), "Idle")
	t.falsy(m:CanTransition("Attack"))
end)

t.test("a transition requested inside a hook is queued, not re-entered", function()
	local order = {}
	local m
	m = StateMachine.new({
		initial = "A",
		states = {
			A = { to = { "B" } },
			B = {
				to = { "C" },
				enter = function()
					table.insert(order, "enter B")
					m:Transition("C")
					table.insert(order, "still in B enter")
				end,
			},
			C = {
				enter = function()
					table.insert(order, "enter C")
				end,
			},
		},
	}, {})
	m:Transition("B")
	t.eq(order, { "enter B", "still in B enter", "enter C" })
	t.eq(m:Current(), "C")
end)

t.test("Update calls the current state's update with dt and runs queued moves after it", function()
	local seen = 0
	local m
	m = StateMachine.new({
		initial = "A",
		states = {
			A = {
				to = { "B" },
				update = function(_, dt)
					seen += dt
					m:Transition("B")
				end,
			},
			B = {},
		},
	}, {})
	m:Update(0.5)
	t.eq(seen, 0.5)
	t.eq(m:Current(), "B")
end)

t.test("validate reports undefined states and the constructor refuses them", function()
	local bad = { initial = "X", states = { A = { to = { "Missing" } } } }
	t.eq(#StateMachine.validate(bad), 2)
	local ok = pcall(StateMachine.new, bad, {})
	t.falsy(ok)
end)

t.test("history keeps the order and onChange fires", function()
	local changes = {}
	local m = StateMachine.new({
		initial = "A",
		states = { A = {}, B = {} },
		onChange = function(from, to)
			table.insert(changes, from .. ">" .. to)
		end,
	}, {})
	m:Transition("B")
	m:Transition("A")
	t.eq(m:History(), { "A", "B", "A" })
	t.eq(changes, { "A>B", "B>A" })
end)

t.done()
