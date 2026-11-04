import { atom, read, update } from 'claude-code'
import type { EngineInterface as Engine, Register, RenderElement } from 'claude-code'

import type { Hist, Rec, RecStatus } from '../types'
import {
  addPrompt,
  aggregateStatus,
  buildRows,
  buildSvg,
  clip,
  counts,
  emptyHist,
  estimate,
  etaLabel,
  fmt,
  grid,
  isActive,
  isEnded,
  lineStyle,
  mergeRecs,
  planItems,
  promptFor,
  recordDuration,
  recordWrap,
  type EndHint,
} from './logic'

const PANE = 'rbx-subagent-hud'
const HIST_KEY = 'hist'
const PREVIEW_CHARS = 600

// Atom refs need literal keys.
const tasksA = atom({ plugin: 'rbx-subagent-hud', key: 'tasks' } as const, [])
const todosA = atom({ plugin: 'rbx-subagent-hud', key: 'todos' } as const, [])
const recsA = atom({ plugin: 'rbx-subagent-hud', key: 'recs' } as const, [], { shape: 'recs-1' })
const promptsA = atom({ plugin: 'rbx-subagent-hud', key: 'prompts' } as const, [], { shape: 'prompts-1' })
const turnA = atom(
  { plugin: 'rbx-subagent-hud', key: 'turn' } as const,
  { n: 0, start: 0, runStart: 0, end: 0, isOn: false, lastAgentEnd: 0 },
  { shape: 'turn-1' },
)
const etaA = atom({ plugin: 'rbx-subagent-hud', key: 'eta' } as const, { kind: 'none', ms: 0, conf: 'none' }, { shape: 'eta-1' })
const tickA = atom({ plugin: 'rbx-subagent-hud', key: 'tick' } as const, 0)
const nowA = atom({ plugin: 'rbx-subagent-hud', key: 'now' } as const, 0)
const selA = atom({ plugin: 'rbx-subagent-hud', key: 'selected' } as const, null)
const expA = atom({ plugin: 'rbx-subagent-hud', key: 'isExpanded' } as const, false)
const enabledA = atom({ plugin: 'rbx-subagent-hud', key: 'enabled' } as const, false)
const dismissedA = atom({ plugin: 'rbx-subagent-hud', key: 'dismissed' } as const, false)

const GAME_SKILL = /game-dev/i
const GAME_PROMPT = /^\s*\/game-dev/i
const QUIET_ORIGINS: ReadonlySet<string> = new Set(['task-notification', 'observer', 'observer-activity', 'peer', 'peer-send-message'])

let ticking = false
let isAnimating = false
let isFreshPrompt = false
let histCache: Hist | null = null
const hints: Record<string, EndHint> = {}

function isHist(v: unknown): v is Hist {
  const h = v as Hist | null
  return (
    typeof h === 'object' &&
    h !== null &&
    h.v === 1 &&
    typeof h.byClass === 'object' &&
    typeof h.byType === 'object' &&
    Array.isArray(h.wrap)
  )
}

async function loadHist($: Engine): Promise<Hist> {
  if (histCache !== null) return histCache
  try {
    const raw = await $.store.get(HIST_KEY)
    histCache = isHist(raw) ? raw : emptyHist()
  } catch {
    histCache = emptyHist()
  }
  return histCache
}

async function saveHist($: Engine, h: Hist): Promise<void> {
  histCache = h
  try {
    await $.store.set(HIST_KEY, h)
  } catch {
    // The estimate still works from memory for this session.
  }
}

function ensureTimer($: Engine): void {
  if (ticking) return
  ticking = true
  let n = 0
  $.clock.every(500, async () => {
    n++
    if (!isAnimating) return
    await update($, tickA, t => t + 1)
    if (n % 2 === 0) await refresh($)
  })
}

async function refresh($: Engine): Promise<void> {
  const now = await $.clock.now()
  const list = await $.agent.list()
  const turn = await read($, turnA)
  const prior = await read($, recsA)
  const recs = mergeRecs(prior, list, now, turn.n, hints)

  let hist = await loadHist($)
  let changedHist = false
  const was = new Map(prior.map(r => [r.id, r.status]))
  for (const r of recs) {
    const before = was.get(r.id)
    if (r.status === 'done' && (before === undefined || !isEnded(before))) {
      hist = recordDuration(hist, r)
      changedHist = true
    }
  }
  if (changedHist) await saveHist($, hist)

  const visible = recs.filter(r => r.turn === turn.n)
  const lastEnd = Math.max(0, ...visible.map(r => r.end ?? 0))
  if (lastEnd !== turn.lastAgentEnd) await update($, turnA, t => ({ ...t, lastAgentEnd: lastEnd }))

  if (JSON.stringify(recs) !== JSON.stringify(prior)) await update($, recsA, () => recs)
  const eta = estimate(visible, hist, now)
  isAnimating = turn.isOn || visible.some(r => isActive(r.status))
  if (isAnimating || (await read($, nowA)) === 0) await update($, nowA, () => now)
  if (JSON.stringify(eta) !== JSON.stringify(await read($, etaA))) await update($, etaA, () => eta)
}

async function openPane($: Engine): Promise<void> {
  try {
    await $.ui.open({ id: PANE, title: 'Subagents', columns: 44 })
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

const toItemStatus = (s: string): 'done' | 'active' | 'pending' =>
  s === 'completed' ? 'done' : s === 'in_progress' ? 'active' : 'pending'

async function select($: Engine, id: string | null): Promise<void> {
  await update($, selA, cur => (id === null || cur === id ? null : id))
  await update($, expA, () => false)
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const result = await next(e)
    await $.command.register({
      name: 'rbx-subagent-hud',
      description: 'Toggle the subagent HUD pane (master agent, subagents, done count, time estimate)',
    })
    ensureTimer($)
    await refresh($)
    return result
  })

  on('command.run', { command: 'rbx-subagent-hud' }, async $ => {
    ensureTimer($)
    const isUp = (await $.ui.panes()).some(p => p.id === PANE)
    if (isUp) {
      await update($, enabledA, () => false)
      await update($, dismissedA, () => true)
      await $.ui.close({ id: PANE })
      return { text: 'Subagent HUD closed. /rbx-subagent-hud opens it again.' }
    }
    await update($, enabledA, () => true)
    await update($, dismissedA, () => false)
    await openPane($)
    await refresh($)
    return { text: 'Subagent HUD opened.' }
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
      const now = await $.clock.now()
      const turn = await read($, turnA)
      const isNew = isFreshPrompt || turn.n === 0
      isFreshPrompt = false
      const n = isNew ? turn.n + 1 : turn.n
      await update($, turnA, t => ({
        n,
        start: isNew ? now : t.start,
        runStart: now,
        end: 0,
        isOn: true,
        lastAgentEnd: isNew ? 0 : t.lastAgentEnd,
      }))
      if (isNew) {
        await update($, recsA, list => list.map(r => (isActive(r.status) ? { ...r, turn: n } : r)))
        const sel = await read($, selA)
        const kept = (await read($, recsA)).some(r => r.id === sel && r.turn === n)
        if (!kept) await update($, selA, () => null)
      }
      isAnimating = true
    }
    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    const result = await next(e)
    const now = await $.clock.now()
    if (e.agentId === undefined) {
      await refresh($)
      const turn = await read($, turnA)
      const group = (await read($, recsA)).filter(r => r.turn === turn.n)
      if (turn.isOn && turn.lastAgentEnd > 0 && group.length > 0 && !group.some(r => isActive(r.status))) {
        const wrap = now - Math.max(turn.lastAgentEnd, turn.runStart)
        await saveHist($, recordWrap(await loadHist($), wrap))
      }
      await update($, turnA, t => ({ ...t, isOn: false, end: now }))
    } else {
      const status: RecStatus = e.reason === 'answer' ? 'done' : e.reason === 'aborted' ? 'killed' : 'failed'
      hints[e.agentId] = { at: now, status }
    }
    await refresh($)
    return result
  })

  on('agent.spawn', async ($, e, next) => {
    ensureTimer($)
    const now = await $.clock.now()
    const res = await next(e)
    if (e.resume !== undefined || !('agentId' in res) || res.agentId === undefined) return res
    const id = res.agentId
    const turn = await read($, turnA)
    if (turn.n === 0) await update($, turnA, () => ({ n: 1, start: now, runStart: now, end: 0, isOn: true, lastAgentEnd: 0 }))
    const n = turn.n === 0 ? 1 : turn.n
    await update($, promptsA, list =>
      addPrompt(list, {
        id,
        toolUseId: e.tool_use_id,
        text: e.prompt,
        chars: 0,
        isTruncated: false,
        description: e.description,
        type: e.subagentType,
        model: e.model ?? res.model,
      }),
    )
    const rec: Rec = {
      id,
      parentId: e.parentAgentId,
      name: e.description || e.subagentType,
      type: e.subagentType,
      model: e.model ?? res.model,
      status: 'running',
      start: now,
      turn: n,
    }
    await update($, recsA, list =>
      list.some(r => r.id === id)
        ? list.map(r => (r.id === id ? { ...r, start: Math.min(r.start, now), model: r.model ?? rec.model } : r))
        : [...list, rec],
    )
    isAnimating = true
    await refresh($)
    return res
  })

  on('prompt.submit', async ($, e, next) => {
    if (e.text.trim() !== '' && e.isMeta !== true && !QUIET_ORIGINS.has(e.origin.kind)) isFreshPrompt = true
    if (GAME_PROMPT.test(e.text)) await autoOpen($)
    return next(e)
  })

  on('tool.call', { tool: 'Skill' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny === undefined && GAME_SKILL.test(e.skill)) await autoOpen($)
    return ran
  })

  on('tool.call', { tool: 'Agent' }, async ($, e, next) => {
    ensureTimer($)
    try {
      if (await $.fs.exists('GAME.md')) await autoOpen($)
    } catch {
      // No filesystem answer: the other two signals still apply.
    }
    return next(e)
  })

  on('tool.call', { tool: 'TaskCreate' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny === undefined && ran.isError !== true && ran.result) {
      const t = ran.result.task
      await update($, tasksA, list => [...list, { id: t.id, label: t.subject, status: 'pending' as const }])
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
                ? { ...i, label: e.activeForm ?? e.subject ?? i.label, status: e.status ? toItemStatus(e.status) : i.status }
                : i,
            ),
      )
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
    }
    return ran
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text, Button } = $.ui.resolve(e)
    const Svg = e.surface === 'terminal' ? null : $.ui.resolve(e).Svg
    const cols = Math.max(12, e.props.bodyColumns)
    const now = await read($, nowA)
    const tick = await read($, tickA)
    const turn = await read($, turnA)
    const eta = await read($, etaA)
    const selId = await read($, selA)
    const isExp = await read($, expA)
    const prompts = await read($, promptsA)
    const recs = (await read($, recsA)).filter(r => r.turn === turn.n)
    const rows = buildRows(recs)
    const c = counts(recs)
    const sel = rows.find(r => r.rec.id === selId)
    const plan = planItems(await read($, tasksA), await read($, todosA))
    const trunk = lineStyle(aggregateStatus(recs), tick, false)
    const label = etaLabel(eta)
    const isBusy = turn.isOn || c.running + c.queued > 0
    const elapsed = turn.start === 0 ? 0 : (isBusy ? now : turn.end) - turn.start

    const header = (
      <Box flexDirection="column">
        <Box flexDirection="row">
          <Text color="cyan" bold>
            {'◆ '}
          </Text>
          <Text bold>{'MASTER '}</Text>
          <Text color={isBusy ? 'yellow' : 'cyan'}>{turn.isOn ? 'working' : isBusy ? 'waiting for agents' : 'idle'}</Text>
          {turn.start > 0 && <Text dimColor>{` ${fmt(elapsed)}`}</Text>}
        </Box>
        {c.total === 0 ? (
          <Text dimColor>No subagents in this turn.</Text>
        ) : (
          <Box flexDirection="row">
            <Text color={c.done === c.total ? 'green' : 'cyan'} bold>{`${c.done}/${c.total} done`}</Text>
            <Text dimColor>{`  ${c.running + c.queued} running  ${c.failed} failed`}</Text>
          </Box>
        )}
        {label !== '' && <Text color="yellow">{clip(label, cols)}</Text>}
        {label === '' && turn.isOn && c.total > 0 && c.running + c.queued === 0 && (
          <Text dimColor>{'master is working on the result'}</Text>
        )}
      </Box>
    )

    const chipRows: RenderElement[] = []
    if (Svg === null) {
      const groups = [...new Set(rows.map(r => r.depth))].sort((a, b) => a - b)
      const perOf = (indent: number): number => Math.max(1, Math.min(4, Math.floor((cols - 2 - indent) / 17)))
      const total = groups.reduce((n, d) => n + grid(rows.filter(r => r.depth === d), perOf(2 * (d - 1))).length, 0)
      let k = 0
      if (rows.length > 0) {
        chipRows.push(
          <Text color={trunk.color} dimColor={trunk.isDim}>
            {'┊'}
          </Text>,
        )
      }
      for (const d of groups) {
        const indent = 2 * (d - 1)
        const per = perOf(indent)
        const w = Math.max(10, Math.floor((cols - 2 - indent) / per))
        for (const row of grid(rows.filter(r => r.depth === d), per)) {
          k++
          const isLast = k === total
          chipRows.push(
            <Box flexDirection="row">
              <Text color="cyan" dimColor>
                {(isLast ? '╰' : '├') + '┄'.repeat(1 + indent)}
              </Text>
              {row.map(r => {
                const st = lineStyle(r.rec.status, tick, r.rec.id === selId)
                return (
                  <Text color={st.color} dimColor={st.isDim}>
                    {(st.isSolid ? '━' : '┄').repeat(w - 1) + ' '}
                  </Text>
                )
              })}
            </Box>,
            <Box flexDirection="row">
              <Text dimColor>{(isLast ? ' ' : '┊') + ' '.repeat(1 + indent)}</Text>
              {row.map(r => {
                const st = lineStyle(r.rec.status, tick, r.rec.id === selId)
                const isSel = r.rec.id === selId
                const name = clip(`${d > 1 ? '↳ ' : ''}${r.index} ${r.rec.name}`, w - 4)
                return (
                  <Box width={w}>
                    <Button key={`agent:${r.rec.id}`} plain onPress={() => select($, r.rec.id)}>
                      <Text color={st.color}>{st.glyph}</Text>
                      <Text color={isSel ? 'cyan' : undefined} bold={isSel}>{` ${name}`}</Text>
                    </Button>
                  </Box>
                )
              })}
            </Box>,
            <Box flexDirection="row">
              <Text dimColor>{(isLast ? ' ' : '┊') + ' '.repeat(1 + indent)}</Text>
              {row.map(r => (
                <Box width={w}>
                  <Button key={`agent:${r.rec.id}:b`} plain dimColor onPress={() => select($, r.rec.id)}>
                    {`  ${clip(`${r.rec.type} ${fmt((r.rec.end ?? now) - r.rec.start)}`, w - 4)}`}
                  </Button>
                </Box>
              ))}
            </Box>,
          )
        }
      }
    }

    const svg =
      Svg === null || rows.length === 0
        ? null
        : buildSvg({
            width: Math.min(420, Math.max(180, cols * 7)),
            rows,
            tick,
            selectedId: selId,
            isMasterOn: isBusy,
          })

    const list =
      Svg === null
        ? null
        : rows.map(r => {
            const st = lineStyle(r.rec.status, tick, r.rec.id === selId)
            const isSel = r.rec.id === selId
            return (
              <Button key={`agent:${r.rec.id}`} plain onPress={() => select($, r.rec.id)}>
                <Text color={st.color}>{st.glyph}</Text>
                <Text color={isSel ? 'cyan' : undefined} bold={isSel}>
                  {` ${'  '.repeat(r.depth - 1)}${r.index}. ${clip(r.rec.name, Math.max(6, cols - 22 - 2 * r.depth))} `}
                </Text>
                <Text dimColor>{`${r.rec.type} ${fmt((r.rec.end ?? now) - r.rec.start)}`}</Text>
              </Button>
            )
          })

    const p = sel === undefined ? undefined : promptFor(prompts, sel.rec)
    const text = p?.text ?? ''
    const isLong = text.length > PREVIEW_CHARS
    const shown = isLong && !isExp ? text.slice(0, PREVIEW_CHARS) + '…' : text
    const card =
      sel === undefined ? null : (
        <Box flexDirection="column" borderStyle="round" borderColor="cyan" paddingX={1}>
          <Box flexDirection="row" justifyContent="space-between">
            <Text bold color="cyan">{`SUBAGENT ${sel.index} PROMPT (from Master Agent)`}</Text>
            <Button key="card-close" role="dismiss" plain onPress={() => select($, null)}>
              {'x close'}
            </Button>
          </Box>
          <Text dimColor>
            {`${sel.rec.name} · ${sel.rec.type}${(p?.model ?? sel.rec.model) ? ' · ' + (p?.model ?? sel.rec.model) : ''} · ${sel.rec.status} ${fmt((sel.rec.end ?? now) - sel.rec.start)}`}
          </Text>
          <Text>{p === undefined ? 'Prompt not captured (this agent started before the HUD loaded).' : shown}</Text>
          {p !== undefined && p.isTruncated && isExp && (
            <Text dimColor>{`(stored first ${text.length} of ${p.chars} characters)`}</Text>
          )}
          <Box flexDirection="row" gap={2}>
            {isLong && (
              <Button key="card-more" plain onPress={() => update($, expA, v => !v)}>
                {isExp ? 'show less' : `show more (${text.length} chars)`}
              </Button>
            )}
            <Button
              key="card-view"
              plain
              dimColor
              onPress={async () => {
                try {
                  await $.ui.view({ agentId: sel.rec.id })
                } catch {
                  // The view switch works only on the person's own input.
                }
              }}
            >
              {'view transcript'}
            </Button>
          </Box>
        </Box>
      )

    const pct = plan.total === 0 ? 0 : Math.round((plan.done / plan.total) * 100)
    const bw = Math.max(8, Math.min(20, cols - 14))
    const filled = Math.round((pct / 100) * bw)

    return (
      <Box flexDirection="column">
        {header}
        {Svg !== null && svg !== null && <Svg source={svg.source} alt={svg.alt} width={svg.width} height={svg.height} />}
        {chipRows}
        {list}
        {card}
        {plan.total > 0 && (
          <Box flexDirection="row">
            <Text color={plan.done === plan.total ? 'green' : 'cyan'}>{'█'.repeat(filled)}</Text>
            <Text dimColor>{'░'.repeat(bw - filled)}</Text>
            <Text dimColor>{` ${pct}% plan ${plan.done}/${plan.total}`}</Text>
          </Box>
        )}
      </Box>
    )
  })

  // Narrow terminals: the pane waits undrawn, so one summary line shows above the prompt.
  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey || !(await read($, enabledA))) return next(e)
    if ((await $.ui.panes()).some(p => p.id === PANE && p.isPlaced)) return next(e)
    const turn = await read($, turnA)
    const recs = (await read($, recsA)).filter(r => r.turn === turn.n)
    if (recs.length === 0) return next(e)

    const { Box, Text } = $.ui.resolve(e)
    const c = counts(recs)
    const label = etaLabel(await read($, etaA))
    return (
      <Box flexDirection="row">
        <Text color="cyan">{'◆ '}</Text>
        <Text color={c.done === c.total ? 'green' : 'cyan'} bold>{`${c.done}/${c.total} done`}</Text>
        {label !== '' && <Text dimColor>{`  ${label}`}</Text>}
      </Box>
    )
  })
}
