import { atom, read, update } from 'claude-code'
import type { EngineInterface as Engine, Register } from 'claude-code'

import type { VaultIndex } from '../types'

const PANE = 'rbx-graph'
const SITE = 'https://vault-hhmi60uo.netlify.app/#graph'
const MAX_SIDE = 10
const MAX_RESULTS = 6
const PREVIEW_LINES = 20

// Atom refs need literal keys.
const selectedA = atom({ plugin: 'rbx-graph', key: 'selected' } as const, '')
const viewA = atom({ plugin: 'rbx-graph', key: 'view' } as const, 'graph')
const queryA = atom({ plugin: 'rbx-graph', key: 'query' } as const, '')
const previewA = atom({ plugin: 'rbx-graph', key: 'preview' } as const, '')
const statusA = atom({ plugin: 'rbx-graph', key: 'status' } as const, 'idle')
const revA = atom({ plugin: 'rbx-graph', key: 'rev' } as const, 0)
const enabledA = atom({ plugin: 'rbx-graph', key: 'enabled' } as const, false)
const dismissedA = atom({ plugin: 'rbx-graph', key: 'dismissed' } as const, false)

const SKIP_DIRS = new Set(['node_modules', 'vault.git', 'claude-kit-test'])
const WIKILINK = /(?<!!)\[\[([^\]\n|#]+)(?:#[^\]|\n]*)?(?:\|[^\]\n]*)?\]\]/g

// The derived, in-memory form of the index. Rebuilt from the store when the
// module reloads, so it is a cache and never the only copy.
type Loaded = { idx: VaultIndex; inb: number[][]; names: string[]; lower: string[] }
let loaded: Loaded | undefined
let isBuilding = false

const join = (a: string, b: string): string => (a.endsWith('/') || a.endsWith('\\') ? a + b : a + '/' + b)
const baseName = (p: string): string => (p.split('/').pop() ?? p).replace(/\.md$/i, '')
const clip = (s: string, n: number): string =>
  n <= 1 ? '' : s.length <= n ? s : s.slice(0, n - 1) + '…'

function derive(idx: VaultIndex): Loaded {
  const inb: number[][] = idx.paths.map(() => [])
  idx.out.forEach((targets, i) => {
    for (const t of targets) inb[t]?.push(i)
  })
  const names = idx.paths.map(baseName)
  return { idx, inb, names, lower: names.map(n => n.toLowerCase()) }
}

async function getLoaded($: Engine): Promise<Loaded | undefined> {
  if (loaded) return loaded
  const idx = (await $.store.get('index')) as VaultIndex | undefined
  if (idx && Array.isArray(idx.paths)) loaded = derive(idx)
  return loaded
}

// The same lookup the kit's uninstall skill uses: $CLAUDES_VAULT, then
// ~/Obsidian/claudes-vault, then a search for a folder with Roblox/, Mentor/
// and claude-kit/.
async function isVault($: Engine, d: string): Promise<boolean> {
  try {
    return (await $.fs.exists(join(d, 'Roblox'))) && (await $.fs.exists(join(d, 'Mentor')))
  } catch {
    return false
  }
}

async function findVault($: Engine): Promise<string | undefined> {
  const home = (await $.env.get('USERPROFILE')) ?? (await $.env.get('HOME')) ?? ''
  const fromEnv = await $.env.get('CLAUDES_VAULT')
  const cands = [fromEnv, home ? join(join(home, 'Obsidian'), 'claudes-vault') : undefined]
  for (const c of cands) if (c && (await isVault($, c))) return c
  if (!home) return undefined
  for (const base of ['Downloads', 'Documents', 'Desktop', 'Obsidian', '']) {
    const b = base ? join(home, base) : home
    let kids: string[] = []
    try {
      kids = (await $.fs.list(b)).filter(k => k.kind === 'dir').map(k => join(b, k.name))
    } catch {
      continue
    }
    const level = base === 'Downloads' || base === 'Documents' || base === 'Desktop'
    const list = [...kids]
    if (level) {
      for (const k of kids) {
        try {
          for (const n of await $.fs.list(k)) if (n.kind === 'dir') list.push(join(k, n.name))
        } catch {
          // unreadable folder: skip
        }
      }
    }
    for (const c of list) {
      if ((await isVault($, c)) && (await $.fs.exists(join(c, 'claude-kit')))) return c
    }
  }
  return undefined
}

// Every markdown file with its mtime; listing only, no reads.
async function walk($: Engine, root: string): Promise<{ rel: string; mt: number }[]> {
  const out: { rel: string; mt: number }[] = []
  const stack: string[] = ['']
  while (stack.length > 0) {
    const rel = stack.pop() ?? ''
    let entries
    try {
      entries = await $.fs.list(rel === '' ? root : join(root, rel))
    } catch {
      continue
    }
    for (const e of entries) {
      if (e.name.startsWith('.') || SKIP_DIRS.has(e.name)) continue
      const r = rel === '' ? e.name : rel + '/' + e.name
      if (e.kind === 'dir') stack.push(r)
      else if (e.kind === 'file' && /\.md$/i.test(e.name)) out.push({ rel: r, mt: e.mtimeMs })
    }
  }
  return out.sort((a, b) => (a.rel < b.rel ? -1 : 1))
}

function resolver(paths: string[]): (target: string) => number | undefined {
  const byBase = new Map<string, number>()
  const byFull = new Map<string, number>()
  paths.forEach((p, i) => {
    const full = p.replace(/\.md$/i, '').toLowerCase()
    byFull.set(full, i)
    const b = full.split('/').pop() ?? full
    const old = byBase.get(b)
    if (old === undefined || (paths[old] ?? '').length > p.length) byBase.set(b, i)
  })
  return target => {
    const t = target.trim().replace(/\.md$/i, '').toLowerCase()
    if (t === '') return undefined
    if (t.includes('/')) {
      const exact = byFull.get(t)
      if (exact !== undefined) return exact
      for (const [full, i] of byFull) if (full.endsWith('/' + t)) return i
      return undefined
    }
    return byBase.get(t)
  }
}

// Build or refresh the index. Reads only files whose mtime changed.
async function scan($: Engine, isForced: boolean): Promise<void> {
  if (isBuilding) return
  isBuilding = true
  try {
    await update($, statusA, () => 'Finding the vault...')
    const root = await findVault($)
    if (root === undefined) {
      await update($, statusA, () => 'No vault found. Set CLAUDES_VAULT to its folder.')
      return
    }
    const files = await walk($, root)
    const paths = files.map(f => f.rel)
    const mt = files.map(f => f.mt)
    const sig = `${files.length}:${Math.max(0, ...mt)}`
    const prior = isForced ? undefined : await getLoaded($)
    if (prior && prior.idx.root === root && prior.idx.sig === sig) {
      await update($, statusA, () => 'ready')
      await update($, revA, n => n + 1)
      return
    }

    const resolve = resolver(paths)
    const newIndex = new Map(paths.map((p, i) => [p, i]))
    const oldIndex = new Map((prior?.idx.paths ?? []).map((p, i) => [p, i]))
    const out: number[][] = paths.map(() => [])
    const todo: number[] = []
    paths.forEach((p, i) => {
      const o = oldIndex.get(p)
      if (prior && o !== undefined && prior.idx.mt[o] === mt[i] && prior.idx.root === root) {
        out[i] = (prior.idx.out[o] ?? [])
          .map(j => newIndex.get(prior.idx.paths[j] ?? ''))
          .filter((x): x is number => x !== undefined)
      } else {
        todo.push(i)
      }
    })

    const STEP = 8
    for (let s = 0; s < todo.length; s += STEP) {
      await Promise.all(
        todo.slice(s, s + STEP).map(async i => {
          let text = ''
          try {
            text = await $.fs.read(join(root, paths[i] ?? ''))
          } catch {
            return
          }
          const seen = new Set<number>()
          for (const m of text.matchAll(WIKILINK)) {
            const t = resolve(m[1] ?? '')
            if (t !== undefined && t !== i) seen.add(t)
          }
          out[i] = [...seen]
        }),
      )
      if (s % 400 === 0) await update($, statusA, () => `Indexing ${Math.min(s + STEP, todo.length)}/${todo.length}`)
    }

    const idx: VaultIndex = { root, sig, paths, mt, out }
    await $.store.set('index', idx)
    loaded = derive(idx)
    await update($, statusA, () => 'ready')
    await update($, revA, n => n + 1)
  } catch (err) {
    await update($, statusA, () => `Index failed: ${err instanceof Error ? err.message : 'unknown error'}`)
  } finally {
    isBuilding = false
  }
}

function defaultCenter(l: Loaded): number {
  for (const want of ['readme.md', 'home.md', 'index.md']) {
    const i = l.idx.paths.findIndex(p => p.toLowerCase() === want)
    if (i >= 0) return i
  }
  return 0
}

function centerOf(l: Loaded, selected: string): number {
  const i = selected === '' ? -1 : l.idx.paths.indexOf(selected)
  return i >= 0 ? i : defaultCenter(l)
}

function search(l: Loaded, q: string): number[] {
  const needle = q.trim().toLowerCase()
  if (needle === '') return []
  const starts: number[] = []
  const has: number[] = []
  l.lower.forEach((n, i) => {
    if (n.startsWith(needle)) starts.push(i)
    else if (n.includes(needle)) has.push(i)
  })
  return [...starts, ...has].slice(0, MAX_RESULTS)
}

async function openPane($: Engine): Promise<void> {
  try {
    await $.ui.open({ id: PANE, title: 'Vault graph' })
  } catch {
    // A refused open leaves the one-line hint.
  }
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const result = await next(e)
    await $.command.register({
      name: 'rbx-graph',
      description: 'Toggle a side pane with the link graph of your vault',
    })
    return result
  })

  on('command.run', { command: 'rbx-graph' }, async $ => {
    const isUp = (await $.ui.panes()).some(p => p.id === PANE)
    if (isUp) {
      await update($, enabledA, () => false)
      await $.ui.close({ id: PANE })
      return { text: 'Vault graph closed. /rbx-graph opens it again.' }
    }
    await update($, enabledA, () => true)
    await update($, dismissedA, () => false)
    await openPane($)
    await scan($, false)
    return { text: 'Vault graph opened.' }
  })

  on('ui.close', async ($, e, next) => {
    const result = await next(e)
    if (e.id === PANE) await update($, enabledA, () => false)
    return result
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    if (e.surface === 'mobile') {
      const { Text } = $.ui.resolve(e)
      return <Text dimColor>The vault graph needs the terminal or desktop app.</Text>
    }
    const { Box, Button, Input, Link, Text } = $.ui.resolve(e)
    const cols = e.props.bodyColumns
    const status = await read($, statusA)
    await read($, revA)
    const l = await getLoaded($)

    const close = (
      <Button key="close" label="Close" onPress={() => $.ui.close({ id: PANE })} />
    )
    if (l === undefined) {
      return (
        <Box flexDirection="column">
          <Text dimColor>{status === 'idle' ? 'Press Refresh to index the vault.' : status}</Text>
          <Box flexDirection="row">
            <Button key="refresh" label="Refresh" onPress={() => void scan($, true)} />
            <Text> </Text>
            {close}
          </Box>
        </Box>
      )
    }

    const selected = await read($, selectedA)
    const c = centerOf(l, selected)
    const centerPath = l.idx.paths[c] ?? ''
    const view = await read($, viewA)
    const query = await read($, queryA)

    const go = (i: number) => async () => {
      await update($, selectedA, () => l.idx.paths[i] ?? '')
      await update($, queryA, () => '')
      await update($, viewA, () => 'graph')
    }

    const outs = l.idx.out[c] ?? []
    const ins = l.inb[c] ?? []

    const header = (
      <Box flexDirection="column">
        <Text dimColor>{`links in ${ins.length} · links out ${outs.length} · notes ${l.idx.paths.length}`}</Text>
        <Input
          key="search"
          label="Find"
          placeholder="note name"
          value={query}
          submitLabel="Go"
          onInput={(v: string) => void update($, queryA, () => v)}
          onSubmit={async (v: string) => {
            const top = search(l, v)[0]
            if (top !== undefined) await go(top)()
          }}
        />
        {search(l, query).map(i => (
          <Button key={`s:${i}`} label={clip(l.names[i] ?? '', cols - 6)} plain onPress={go(i)} />
        ))}
      </Box>
    )

    const toolbar = (
      <Box flexDirection="row">
        <Button
          key="toggle"
          label={view === 'graph' ? 'Note' : 'Graph'}
          onPress={async () => {
            if (view === 'note') {
              await update($, viewA, () => 'graph')
              return
            }
            let text = ''
            try {
              text = await $.fs.read(join(l.idx.root, centerPath))
            } catch {
              text = '(could not read this note)'
            }
            await update($, previewA, () => text.split('\n').slice(0, PREVIEW_LINES).join('\n'))
            await update($, viewA, () => 'note')
          }}
        />
        <Text> </Text>
        <Button key="refresh" label="Refresh" onPress={() => void scan($, true)} />
        <Text> </Text>
        {close}
        <Text> </Text>
        <Link href={SITE} label="Open full graph" />
      </Box>
    )

    if (view === 'note') {
      const lines = (await read($, previewA)).split('\n')
      return (
        <Box flexDirection="column">
          {header}
          <Text bold>{clip(centerPath, cols)}</Text>
          {lines.map(line => (
            <Text>{line === '' ? ' ' : clip(line, cols)}</Text>
          ))}
          {toolbar}
        </Box>
      )
    }

    const side = (list: number[], isIn: boolean) =>
      list.slice(0, MAX_SIDE).map((i, n, arr) => {
        const extra = list.length > MAX_SIDE
        const isLast = n === arr.length - 1 && !extra
        const glyph = isIn ? (n === 0 ? '┌─ ' : '├─ ') : isLast ? '└─ ' : '├─ '
        return (
          <Box flexDirection="row">
            <Text dimColor>{glyph}</Text>
            <Button key={`${isIn ? 'in' : 'out'}:${i}`} label={clip(l.names[i] ?? '', cols - 5)} plain onPress={go(i)} />
          </Box>
        )
      })

    return (
      <Box flexDirection="column">
        {header}
        <Text dimColor>{'← links in'}</Text>
        {side(ins, true)}
        {ins.length > MAX_SIDE && <Text dimColor>{`│  +${ins.length - MAX_SIDE} more`}</Text>}
        <Text dimColor>{ins.length > 0 ? '│' : ' '}</Text>
        <Box flexDirection="row">
          <Text color="cyan" bold>{'◉ '}</Text>
          <Text bold>{clip(l.names[c] ?? '', cols - 3)}</Text>
        </Box>
        <Text dimColor>{outs.length > 0 ? '│' : ' '}</Text>
        {side(outs, false)}
        {outs.length > MAX_SIDE && <Text dimColor>{`└─ +${outs.length - MAX_SIDE} more`}</Text>}
        <Text dimColor>{'links out →'}</Text>
        {toolbar}
      </Box>
    )
  })

  // Where the pane is not placed (a narrow terminal) it waits undrawn.
  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey || !(await read($, enabledA))) return next(e)
    if ((await $.ui.panes()).some(p => p.id === PANE && p.isPlaced)) return next(e)
    const { Text } = $.ui.resolve(e)
    return <Text dimColor>widen the window to see the graph</Text>
  })
}
