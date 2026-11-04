export type Item = { id: string; label: string; status: 'pending' | 'active' | 'done' }

export type RecStatus = 'queued' | 'running' | 'waiting' | 'done' | 'failed' | 'killed'

/** One subagent as the HUD keeps it. start/end are epoch ms; turn is the master turn it belongs to. */
export type Rec = {
  id: string
  parentId?: string
  name: string
  type: string
  model?: string
  status: RecStatus
  start: number
  end?: number
  turn: number
}

/** The Agent call's input, captured when the master sent it. text is capped at 20000 characters. */
export type Prompt = {
  id: string
  toolUseId: string
  text: string
  chars: number
  isTruncated: boolean
  description: string
  type: string
  model?: string
}

/**
 * One request of the person to the master: n counts requests, start is when it began (0 before the first),
 * runStart when the master's current run began (a run ends when the turn completes, a later one may follow
 * when background subagents report back).
 */
export type Turn = { n: number; start: number; runStart: number; end: number; isOn: boolean; lastAgentEnd: number }

export type Eta = { kind: 'none' | 'est' | 'estimating'; ms: number; conf: 'none' | 'ok' | 'low' }

/** Finished-subagent durations (ms), kept across sessions in $.store. */
export type Hist = {
  v: 1
  byClass: Record<string, number[]>
  byType: Record<string, number[]>
  wrap: number[]
}

declare module 'claude-code' {
  interface PluginState {
    'rbx-subagent-hud': {
      tasks: Item[]
      todos: Item[]
      recs: Shaped<Rec[]>
      prompts: Shaped<Prompt[]>
      turn: Shaped<Turn>
      eta: Shaped<Eta>
      tick: number
      now: number
      selected: string | null
      isExpanded: boolean
      enabled: boolean
      dismissed: boolean
    }
  }
}
