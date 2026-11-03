import { atom, read, update } from 'claude-code'
import type { EngineInterface as Engine, Register } from 'claude-code'

import type { HudNode, Item, NodeStatus, Progress, Snap } from '../types'

const PANE = 'hud-rbxdev-vault'

// Atom refs need literal keys.
const tasksA = atom({ plugin: 'hud-rbxdev-vault', key: 'tasks' } as const, [])
const todosA = atom({ plugin: 'hud-rbxdev-vault', key: 'todos' } as const, [])
const batchA = atom({ plugin: 'hud-rbxdev-vault', key: 'batch' } as const, [])
const nodesA = atom({ plugin: 'hud-rbxdev-vault', key: 'nodes' } as const, [])
const snapA = atom({ plugin: 'hud-rbxdev-vault', key: 'snap' } as const, null)
const enabledA = atom({ plugin: 'hud-rbxdev-vault', key: 'enabled' } as const, false)
const dismissedA = atom({ plugin: 'hud-rbxdev-vault', key: 'dismissed' } as const, false)
const turnA = atom({ plugin: 'hud-rbxdev-vault', key: 'isTurnOn' } as const, false)
const masterA = atom({ plugin: 'hud-rbxdev-vault', key: 'masterStart' } as const, 0)

const GAME_SKILL = /game-dev/i
const GAME_PROMPT = /^\s*\/game-dev/i

const COLOR: Record<NodeStatus, string> = {
  working: 'yellow',
  waiting: 'cyan',
  done: 'green',
  failed: 'red',
  killed: 'magenta',
}

const toNodeStatus = (s: string): NodeStatus =>
  s === 'pending' || s === 'running'
    ? 'working'
    : s === 'completed'
      ? 'done'
      : s === 'failed'
        ? 'failed'
        : s === 'killed'
          ? 'killed'
          : 'waiting'

const isEnded = (s: NodeStatus): boolean => s === 'done' || s === 'failed' || s === 'killed'

const toItemStatus = (s: string): Item['status'] =>
  s === 'completed' ? 'done' : s === 'in_progress' ? 'active' : 'pending'

// 45s, 3m12s, 1h02m
function fmt(ms: number): string {
  const s = Math.max(0, Math.floor(ms / 1000))
  if (s < 60) return `${s}s`
  const m = Math.floor(s / 60)
  if (m < 60) return `${m}m${String(s % 60).padStart(2, '0')}s`
  return `${Math.floor(m / 60)}h${String(m % 60).padStart(2, '0')}m`
}

const pct = (p: Progress): number => (p.total === 0 ? 0 : Math.round((p.done / p.total) * 100))

const clip = (s: string, n: number): string =>
  n <= 1 ? '' : s.length <= n ? s : s.slice(0, n - 1) + '…'

let ticking = false

function ensureTimer($: Engine): void {
  if (ticking) return
  ticking = true
  $.clock.every(1000, () => refresh($))
}

// Roots: agents the main loop spawned (or whose parent is no longer known).
function rootsOf(nodes: HudNode[]): HudNode[] {
  const ids = new Set(nodes.map(n => n.id))
  return nodes.filter(n => n.parentId === undefined || !ids.has(n.parentId))
}

// Recompute the snapshot the pane and the one-line fallback draw from.
async function refresh($: Engine): Promise<void> {
  const now = await $.clock.now()
  const agents = await $.agent.list()

  // Merge the live list into the kept history: the list drops an agent
  // seconds after it ends, the tree keeps it with its total time.
  const prior = await read($, nodesA)
  const byId = new Map(prior.map(n => [n.id, n]))
  const live = new Set<string>()
  for (const a of agents) {
    live.add(a.id)
    const old = byId.get(a.id)
    const status = toNodeStatus(a.status)
    byId.set(a.id, {
      id: a.id,
      parentId: a.parentId,
      name: a.description || a.name || a.type,
      status,
      start: old?.start ?? now,
      end: isEnded(status) ? (old?.end ?? now) : undefined,
    })
  }
  for (const [id, n] of byId) {
    if (!live.has(id) && !isEnded(n.status)) {
      byId.set(id, { ...n, status: 'done', end: n.end ?? now })
    }
  }
  const nodes = [...byId.values()].sort((a, b) => a.start - b.start).slice(-60)
  await update($, nodesA, () => nodes)

  // A batch starts when a worker is spawned while none were working, so old
  // finished workers do not count. 'waiting' counts as finished for the bar.
  const roots = rootsOf(nodes)
  const running = roots.filter(n => n.status === 'working')
  let batch = await read($, batchA)
  const inBatch = new Set(batch)
  if (running.some(n => !inBatch.has(n.id))) {
    const allBatchDone = roots.filter(n => inBatch.has(n.id)).every(n => n.status !== 'working')
    batch = allBatchDone
      ? running.map(n => n.id)
      : [...batch, ...running.filter(n => !inBatch.has(n.id)).map(n => n.id)]
    await update($, batchA, () => batch)
  }
  const workers = roots.filter(n => batch.includes(n.id))
  const workersDone = workers.filter(n => n.status !== 'working').length

  const tasks = await read($, tasksA)
  const todos = await read($, todosA)
  const items = [...tasks, ...todos]
  const tasksDone = items.filter(i => i.status === 'done').length
  const activeItem = items.find(i => i.status === 'active')
  const activeWorker = workers.find(n => n.status === 'working')

  const progress: Progress | null =
    items.length + workers.length === 0
      ? null
      : {
          done: tasksDone + workersDone,
          total: items.length + workers.length,
          tasksDone,
          tasksTotal: items.length,
          workersDone,
          workersTotal: workers.length,
          current: activeItem?.label ?? activeWorker?.name ?? '',
        }

  const isTurnOn = await read($, turnA)
  let masterStart = await read($, masterA)
  if (masterStart === 0) {
    masterStart = now
    await update($, masterA, () => now)
  }
  const snap: Snap = {
    now,
    masterStart,
    masterWorking: isTurnOn || running.length > 0,
    nodes,
    progress,
  }
  const prev = await read($, snapA)
  const isTicking = snap.masterWorking || nodes.some(n => !isEnded(n.status))
  if (
    isTicking ||
    prev === null ||
    JSON.stringify({ ...prev, now: 0 }) !== JSON.stringify({ ...snap, now: 0 })
  ) {
    await update($, snapA, () => snap)
  }
}

async function openPane($: Engine): Promise<void> {
  try {
    await $.ui.open({ id: PANE, title: 'Workflow' })
  } catch {
    // A refused open leaves the one-line fallback.
  }
}

async function autoOpen($: Engine): Promise<void> {
  ensureTimer($)
  if ((await read($, dismissedA)) || (await read($, enabledA))) return
  await update($, enabledA, () => true)
  await openPane($)
  await refresh($)
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const result = await next(e)
    await $.command.register({
      name: 'hud-rbxdev-vault',
      description: 'Toggle the workflow HUD pane (agent tree and progress bar)',
    })
    ensureTimer($)
    await refresh($)
    return result
  })

  on('command.run', { command: 'hud-rbxdev-vault' }, async $ => {
    ensureTimer($)
    const isUp = (await $.ui.panes()).some(p => p.id === PANE)
    if (isUp) {
      await update($, enabledA, () => false)
      await update($, dismissedA, () => true)
      await $.ui.close({ id: PANE })
      return { text: 'Workflow HUD closed. /hud-rbxdev-vault opens it again.' }
    }
    await update($, enabledA, () => true)
    await update($, dismissedA, () => false)
    await openPane($)
    await refresh($)
    return { text: 'Workflow HUD opened.' }
  })

  on('ui.close', async ($, e, next) => {
    const result = await next(e)
    if (e.id === PANE && e.origin.kind === 'person') {
      await update($, enabledA, () => false)
      await update($, dismissedA, () => true)
    }
    return result
  })

  on('turn.start', async ($, e, next) => {
    ensureTimer($)
    if (e.agentId === undefined) {
      await update($, turnA, () => true)
      await update($, masterA, () => 0)
    }
    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    const result = await next(e)
    if (e.agentId === undefined) {
      await update($, turnA, () => false)
      await refresh($)
    }
    return result
  })

  // Auto-open signal 1: a prompt that starts with /game-dev.
  on('prompt.submit', async ($, e, next) => {
    if (GAME_PROMPT.test(e.text)) await autoOpen($)
    return next(e)
  })

  // Auto-open signal 2: the Skill tool called with the game dev workflow.
  on('tool.call', { tool: 'Skill' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny === undefined && GAME_SKILL.test(e.skill)) await autoOpen($)
    return ran
  })

  // Auto-open signal 3: the first Agent spawn while a GAME.md exists.
  on('tool.call', { tool: 'Agent' }, async ($, e, next) => {
    ensureTimer($)
    try {
      if (await $.fs.exists('GAME.md')) await autoOpen($)
    } catch {
      // No filesystem answer: the other two signals still apply.
    }
    const ran = await next(e)
    await refresh($)
    return ran
  })

  on('tool.call', { tool: 'TaskCreate' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny === undefined && ran.isError !== true && ran.result) {
      const t = ran.result.task
      await update($, tasksA, list => [
        ...list,
        { id: t.id, label: t.subject, status: 'pending' as const },
      ])
      await refresh($)
    }
    return ran
  })

  on('tool.call', { tool: 'TaskUpdate' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny === undefined && ran.isError !== true) {
      await update($, tasksA, list =>
        e.status === 'deleted'
          ? list.filter(i => i.id !== e.taskId)
          : list.map(i =>
              i.id === e.taskId
                ? {
                    ...i,
                    label: e.activeForm ?? e.subject ?? i.label,
                    status: e.status ? toItemStatus(e.status) : i.status,
                  }
                : i,
            ),
      )
      await refresh($)
    }
    return ran
  })

  on('tool.call', { tool: 'TodoWrite' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny === undefined && ran.isError !== true) {
      await update($, todosA, () =>
        e.todos.map((t, n) => ({
          id: `todo-${n}`,
          label: t.status === 'in_progress' ? t.activeForm : t.content,
          status: toItemStatus(t.status),
        })),
      )
      await refresh($)
    }
    return ran
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const snap = await read($, snapA)
    const cols = e.props.bodyColumns
    if (snap === null) {
      return <Text dimColor>Waiting for the workflow to start.</Text>
    }

    type Row = { prefix: string; branch: string; node: HudNode | 'master' }
    const rows: Row[] = []
    const roots = rootsOf(snap.nodes)
    const batch = await read($, batchA)
    const shown = roots.filter(n => batch.includes(n.id) || n.status !== 'done')
    const walk = (list: HudNode[], prefix: string): void => {
      list.forEach((n, i) => {
        const last = i === list.length - 1
        rows.push({ prefix, branch: last ? '└─ ' : '├─ ', node: n })
        walk(
          snap.nodes.filter(c => c.parentId === n.id),
          prefix + (last ? '   ' : '│  '),
        )
      })
    }
    rows.push({ prefix: '', branch: '', node: 'master' })
    walk(shown, '')

    const p = snap.progress
    const percent = p === null ? 0 : pct(p)
    const width = Math.max(8, Math.min(24, cols - 8))
    const filled = Math.round((percent / 100) * width)
    const isDone = p !== null && p.total > 0 && p.done === p.total

    return (
      <Box flexDirection="column">
        {rows.map(r => {
          if (r.node === 'master') {
            const w = snap.masterWorking
            return (
              <Box flexDirection="row">
                <Text color={w ? 'yellow' : 'cyan'} bold>
                  {'● '}
                </Text>
                <Text bold>{'Master '}</Text>
                <Text color={w ? 'yellow' : 'cyan'}>{w ? 'working' : 'idle'}</Text>
                {w && <Text dimColor>{` ${fmt(snap.now - snap.masterStart)}`}</Text>}
              </Box>
            )
          }
          const n = r.node
          const time = fmt((n.end ?? snap.now) - n.start)
          const room =
            cols - r.prefix.length - r.branch.length - 2 - n.status.length - time.length - 3
          return (
            <Box flexDirection="row">
              <Text dimColor>{r.prefix + r.branch}</Text>
              <Text color={COLOR[n.status]}>{'● '}</Text>
              <Text>{clip(n.name, room) + ' '}</Text>
              <Text color={COLOR[n.status]}>{n.status}</Text>
              <Text dimColor>{' ' + time}</Text>
            </Box>
          )
        })}
        <Text> </Text>
        {p === null ? (
          <Text dimColor>No plan or workers yet.</Text>
        ) : (
          <Box flexDirection="column">
            <Box flexDirection="row">
              <Text color={isDone ? 'green' : 'cyan'}>{'█'.repeat(filled)}</Text>
              <Text dimColor>{'░'.repeat(width - filled)}</Text>
              <Text bold>{` ${percent}%`}</Text>
            </Box>
            <Text dimColor>
              {`${p.tasksTotal > 0 ? `${p.tasksDone}/${p.tasksTotal} tasks ` : ''}${p.workersTotal > 0 ? `${p.workersDone}/${p.workersTotal} workers` : ''}`.trim()}
            </Text>
            <Text>{isDone ? 'done' : clip(p.current, cols)}</Text>
          </Box>
        )}
      </Box>
    )
  })

  // Narrow terminals: the pane waits undrawn, so a one-line summary shows
  // above the prompt instead, only while the HUD is on and no pane is placed.
  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const snap = await read($, snapA)
    if (e.props.hasSurvey || snap === null || !(await read($, enabledA))) return next(e)
    if ((await $.ui.panes()).some(p => p.id === PANE && p.isPlaced)) return next(e)
    const p = snap.progress
    const activeCount = snap.nodes.filter(n => n.status === 'working').length
    if (p === null && activeCount === 0) return next(e)

    const { Box, Text } = $.ui.resolve(e)
    const percent = p === null ? 0 : pct(p)
    const filled = Math.round((percent / 100) * 12)
    return (
      <Box>
        <Text color="cyan">{'█'.repeat(filled)}</Text>
        <Text dimColor>{'░'.repeat(12 - filled)}</Text>
        <Text bold>{` ${percent}% `}</Text>
        <Text dimColor>{`${activeCount} ${activeCount === 1 ? 'agent' : 'agents'} working`}</Text>
      </Box>
    )
  })
}
