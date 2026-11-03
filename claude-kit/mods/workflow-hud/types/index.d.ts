export type Item = { id: string; label: string; status: 'pending' | 'active' | 'done' }

export type NodeStatus = 'working' | 'waiting' | 'done' | 'failed' | 'killed'

/** One agent as the tree draws it. start/end are epoch ms. */
export type HudNode = {
  id: string
  parentId?: string
  name: string
  status: NodeStatus
  start: number
  end?: number
}

export type Progress = {
  done: number
  total: number
  tasksDone: number
  tasksTotal: number
  workersDone: number
  workersTotal: number
  current: string
}

export type Snap = {
  now: number
  masterStart: number
  masterWorking: boolean
  nodes: HudNode[]
  progress: Progress | null
}

declare module 'claude-code' {
  interface PluginState {
    'workflow-hud': {
      tasks: Item[]
      todos: Item[]
      batch: string[]
      nodes: HudNode[]
      snap: Snap | null
      enabled: boolean
      dismissed: boolean
      isTurnOn: boolean
      masterStart: number
    }
  }
}
