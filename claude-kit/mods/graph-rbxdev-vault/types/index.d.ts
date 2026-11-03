/** Compact vault index: paths relative to the vault root, mtimes, and out-links as indexes into paths. */
export type VaultIndex = {
  root: string
  sig: string
  paths: string[]
  mt: number[]
  out: number[][]
}

declare module 'claude-code' {
  interface PluginState {
    'graph-rbxdev-vault': {
      selected: string
      view: 'graph' | 'note'
      query: string
      preview: string
      status: string
      rev: number
      enabled: boolean
      dismissed: boolean
    }
  }
}
