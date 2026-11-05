import { atom, read, update } from 'claude-code'
import type { EngineInterface as Engine, Register, RenderElement } from 'claude-code'

import type { Hist, Prompt, Rec, RecStatus, Turn } from '../types'
import {
  addPrompt,
  buildRows,
  dotOf,
  progressOf,
  typicalFor,
  type Row,
  type Progress,
  clip,
  counts,
  emptyHist,
  estimate,
  etaLabel,
  fmt,
  isActive,
  isEnded,
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

// ---------------------------------------------------------------------------
// Look and feel. Every colour is a theme key (follows the person's light/dark
// theme); nothing is hard-coded. Change a knob here, nothing else needs to move.
// The pane is plain Box/Text/Button: no Svg, no image, so text is crisp and in
// the app's own font on every surface (terminal included).
// ---------------------------------------------------------------------------
const K = {
  accent: 'claude', // master diamond, selected agent, prompt card border
  title: 'text', // names
  working: 'warning', // "working" / ETA line
  ok: 'success', // done
  bad: 'error', // failed
  rail: 'inactive', // connector line and unfilled bar track
  bar: 'subtle', // running bar fill (neutral); done/failed bars use ok/bad
} as const
const SPACE = { section: 1 } as const // blank rows between header, tree and card
const BAR_CHAR = '━' // bar glyph; '▬' or '█' for a heavier bar
const RAIL_INDENT = 2 // extra columns per nesting level

type UiKit = ReturnType<Engine['ui']['resolve']>

function bar(ui: UiKit, w: number, p: Progress, color: string, tick: number): RenderElement {
  const n = Math.max(1, w)
  if (!p.isKnown) {
    // No history to estimate from: a short segment slides along the track.
    const seg = Math.max(2, Math.floor(n / 5))
    const at = (tick * 2) % (n - seg + 1)
    return (
      <ui.Text>
        <ui.Text color={K.rail}>{BAR_CHAR.repeat(at)}</ui.Text>
        <ui.Text color={color}>{BAR_CHAR.repeat(seg)}</ui.Text>
        <ui.Text color={K.rail}>{BAR_CHAR.repeat(n - seg - at)}</ui.Text>
      </ui.Text>
    )
  }
  const f = Math.round(p.frac * n)
  return (
    <ui.Text>
      <ui.Text color={color}>{BAR_CHAR.repeat(f)}</ui.Text>
      <ui.Text color={K.rail}>{BAR_CHAR.repeat(n - f)}</ui.Text>
    </ui.Text>
  )
}

type HeaderIn = { cols: number; turn: Turn; c: ReturnType<typeof counts>; label: string; isBusy: boolean; elapsed: number }

/** Master status, summary line, ETA and an overall bar. */
function viewHeader(ui: UiKit, hd: HeaderIn): RenderElement {
  const { c, turn } = hd
  const status = turn.isOn ? 'working' : hd.isBusy ? 'waiting for agents' : 'idle'
  const allDone = c.total > 0 && c.done === c.total
  return (
    <ui.Box flexDirection="column">
      <ui.Box flexDirection="row">
        <ui.Text color={K.accent} bold>{'◆ '}</ui.Text>
        <ui.Text bold>{'Master '}</ui.Text>
        <ui.Text color={hd.isBusy ? K.working : K.rail}>{status}</ui.Text>
        {turn.start > 0 && <ui.Text dimColor>{` ${fmt(hd.elapsed)}`}</ui.Text>}
      </ui.Box>
      {c.total === 0 ? (
        <ui.Text dimColor>No subagents in this turn.</ui.Text>
      ) : (
        <ui.Box flexDirection="column">
          <ui.Box flexDirection="row">
            <ui.Text color={allDone ? K.ok : K.title} bold>{`${c.done}/${c.total} done`}</ui.Text>
            <ui.Text dimColor>{`  ${c.running + c.queued} running  ${c.failed} failed`}</ui.Text>
          </ui.Box>
          {bar(ui, hd.cols - 1, { frac: c.done / c.total, isKnown: true }, c.failed > 0 ? K.bad : K.ok, 0)}
        </ui.Box>
      )}
      {hd.label !== '' && <ui.Text color={K.working}>{clip(hd.label, hd.cols)}</ui.Text>}
      {hd.label === '' && turn.isOn && c.total > 0 && c.running + c.queued === 0 && (
        <ui.Text dimColor>{'master is working on the result'}</ui.Text>
      )}
    </ui.Box>
  )
}

type AgentIn = {
  r: Row
  isLast: boolean
  isSel: boolean
  cols: number
  now: number
  tick: number
  prog: Progress
  onPress: () => void
}

/** One subagent: connector rail on the left, then name + time, type/model, and a slim bar. */
function viewAgent(ui: UiKit, a: AgentIn): RenderElement {
  const { rec } = a.r
  const indent = RAIL_INDENT * (a.r.depth - 1)
  const dot = dotOf(rec.status, a.tick)
  const cw = Math.max(8, a.cols - 3 - indent)
  const time = fmt((rec.end ?? a.now) - rec.start)
  const name = clip(`${a.r.index}. ${rec.name}`, Math.max(4, cw - time.length - 4))
  const meta = [rec.type, rec.model].filter(Boolean).join(' · ')
  const barColor = rec.status === 'done' ? K.ok : isEnded(rec.status) ? K.bad : a.isSel ? K.accent : K.bar
  const rail = a.isLast ? '╰╴\n \n ' : '├╴\n│\n│'
  return (
    <ui.Box flexDirection="row" paddingLeft={indent}>
      <ui.Box width={2} flexShrink={0}>
        <ui.Text color={K.rail}>{rail}</ui.Text>
      </ui.Box>
      <ui.Box flexDirection="column" flexGrow={1}>
        <ui.Button key={`agent:${rec.id}`} plain onPress={a.onPress}>
          <ui.Text color={dot.color} dimColor={dot.isDim}>{dot.glyph}</ui.Text>
          <ui.Text color={a.isSel ? K.accent : K.title} bold={a.isSel}>{` ${name} `}</ui.Text>
          <ui.Text dimColor>{time}</ui.Text>
        </ui.Button>
        <ui.Text dimColor>{`  ${clip(meta, cw - 2)}`}</ui.Text>
        {bar(ui, cw - 2, a.prog, barColor, a.tick)}
      </ui.Box>
    </ui.Box>
  )
}

type CardIn = {
  sel: Row
  p: Prompt | undefined
  isExp: boolean
  now: number
  onClose: () => void
  onMore: () => void
  onView: () => void
}

/** The prompt the master sent the selected subagent (collapsible). */
function viewCard(ui: UiKit, k: CardIn): RenderElement {
  const { sel, p } = k
  const text = p?.text ?? ''
  const isLong = text.length > PREVIEW_CHARS
  const shown = isLong && !k.isExp ? text.slice(0, PREVIEW_CHARS) + '…' : text
  const model = p?.model ?? sel.rec.model
  return (
    <ui.Box flexDirection="column" borderStyle="round" borderColor={K.accent} paddingX={1}>
      <ui.Box flexDirection="row" justifyContent="space-between">
        <ui.Text bold color={K.accent}>{`SUBAGENT ${sel.index} PROMPT (from Master Agent)`}</ui.Text>
        <ui.Button key="card-close" role="dismiss" plain onPress={k.onClose}>
          {'x close'}
        </ui.Button>
      </ui.Box>
      <ui.Text dimColor>
        {`${sel.rec.name} · ${sel.rec.type}${model ? ' · ' + model : ''} · ${sel.rec.status} ${fmt((sel.rec.end ?? k.now) - sel.rec.start)}`}
      </ui.Text>
      <ui.Text>{p === undefined ? 'Prompt not captured (this agent started before the HUD loaded).' : shown}</ui.Text>
      {p !== undefined && p.isTruncated && k.isExp && (
        <ui.Text dimColor>{`(stored first ${text.length} of ${p.chars} characters)`}</ui.Text>
      )}
      <ui.Box flexDirection="row" gap={2}>
        {isLong && (
          <ui.Button key="card-more" plain onPress={k.onMore}>
            {k.isExp ? 'show less' : `show more (${text.length} chars)`}
          </ui.Button>
        )}
        <ui.Button key="card-view" plain dimColor onPress={k.onView}>
          {'view transcript'}
        </ui.Button>
      </ui.Box>
    </ui.Box>
  )
}

/** Plan (tasks/todos) progress, one line. */
function viewPlan(ui: UiKit, v: { cols: number; plan: ReturnType<typeof planItems> }): RenderElement {
  const pct = Math.round((v.plan.done / v.plan.total) * 100)
  const bw = Math.max(8, Math.min(20, v.cols - 14))
  return (
    <ui.Box flexDirection="row">
      {bar(ui, bw, { frac: pct / 100, isKnown: true }, v.plan.done === v.plan.total ? K.ok : K.accent, 0)}
      <ui.Text dimColor>{` ${pct}% plan ${v.plan.done}/${v.plan.total}`}</ui.Text>
    </ui.Box>
  )
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
    const ui = $.ui.resolve(e)
    const cols = Math.max(12, e.props.bodyColumns)
    const now = await read($, nowA)
    const tick = await read($, tickA)
    const turn = await read($, turnA)
    const eta = await read($, etaA)
    const selId = await read($, selA)
    const isExp = await read($, expA)
    const prompts = await read($, promptsA)
    const hist = await loadHist($)
    const recs = (await read($, recsA)).filter(r => r.turn === turn.n)
    const rows = buildRows(recs)
    const c = counts(recs)
    const sel = rows.find(r => r.rec.id === selId)
    const plan = planItems(await read($, tasksA), await read($, todosA))
    const isBusy = turn.isOn || c.running + c.queued > 0
    const elapsed = turn.start === 0 ? 0 : (isBusy ? now : turn.end) - turn.start

    return (
      <ui.Box flexDirection="column" gap={SPACE.section}>
        {viewHeader(ui, { cols, turn, c, label: etaLabel(eta), isBusy, elapsed })}
        {rows.length > 0 && (
          <ui.Box flexDirection="column">
            <ui.Text color={K.rail}>{'│'}</ui.Text>
            {rows.map((r, i) =>
              viewAgent(ui, {
                r,
                isLast: i === rows.length - 1,
                isSel: r.rec.id === selId,
                cols,
                now,
                tick,
                prog: progressOf(r.rec.status, (r.rec.end ?? now) - r.rec.start, typicalFor(hist, r.rec)),
                onPress: () => select($, r.rec.id),
              }),
            )}
          </ui.Box>
        )}
        {sel !== undefined &&
          viewCard(ui, {
            sel,
            p: promptFor(prompts, sel.rec),
            isExp,
            now,
            onClose: () => select($, null),
            onMore: () => update($, expA, v => !v),
            onView: async () => {
              try {
                await $.ui.view({ agentId: sel.rec.id })
              } catch {
                // The view switch works only on the person's own input.
              }
            },
          })}
        {plan.total > 0 && viewPlan(ui, { cols, plan })}
      </ui.Box>
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
