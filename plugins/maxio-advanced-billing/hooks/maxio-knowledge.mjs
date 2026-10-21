#!/usr/bin/env node
// Puts the knowledge that ships in each SDK folder in front of the agent at the moment it applies.
// The hook holds no knowledge of its own. It reads, from the SDK folder it names:
//   AGENTS.md                 the ten rules, between <!-- ten-rules:start --> and <!-- ten-rules:end -->
//   knowledge/index.json      operations[operationId] = { call, route, map, notes, always }
//   knowledge/failures.json   rows of { status, message, patterns, operationId, call, cause, do, notes }
//   the notes files           one section per operation
//
// Usage: node maxio-knowledge.mjs <host> [event]      host is claude, codex or cursor
// The hooks file of each host passes the host, so this script never guesses it from the payload.
//
//   session start        the ten rules and where the SDK folder is, when the project uses the SDK
//   prompt               the same, the first time a prompt names Maxio (Claude Code and Codex)
//   after an edit        the notes for each Maxio operation the edit calls. A write's notes come
//                        first; when the ten rules would leave no room for them, a short card names
//                        the SDK folder and the rules follow with a later message
//   after a command      the cause and fix of a Maxio rejection that the command's output shows
//   before a read        Claude Code only: approves Read, Glob and Grep inside this plugin's own sdk/
//                        folder, and inside the project's installed C# package in the NuGet cache, which
//                        are outside the project and would otherwise prompt or be refused
//
// Each piece is given once per session and again after compaction or /clear. The ten rules are left
// out when the project's own always-on file already carries them; one line naming the SDK folder on
// this machine is given instead. When it does not, the rules come with a request to make adding the
// project block (the SDK folder's knowledge/AGENTS.block.md) a step of the plan. It never blocks a tool call, never prints an error into a session
// and always exits 0.
//
// What was run, and what was built from documentation only:
//   claude  run live in Claude Code 2.1.296 on Windows (hooks.json).
//   codex   built from the Codex hooks documentation and source; never run (hooks.codex.json).
//   cursor  built from the Cursor hooks documentation; never run (hooks.cursor.json). The payload of
//           its Write tool is not documented, so the edit path reads the file from disk when the
//           payload carries no text.
//
// Set MAXIO_HOOK_DEBUG to a file path to append one JSON line per run (event, and the text given).
// Plain Node, no dependencies.

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const PLUGIN_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PLUGIN_SDK = path.join(PLUGIN_ROOT, "sdk");
const HOST = ["claude", "codex", "cursor"].includes(process.argv[2]) ? process.argv[2] : "claude";
// Claude Code spills a hook's text to a file above 10,000 characters and Codex above about 10,000
// bytes. Every message is built to stay under this many UTF-8 bytes; nothing is ever cut mid-way.
const MAX_BYTES = 9000;
const BLOCK_MARKER = "maxio-advanced-billing:rules:start";

const SDK = {
  csharp: { dir: "dotnet", name: "C#/.NET", marker: /\bMaxioAdvancedBilling\b/ },
  python: { dir: "python", name: "Python", marker: /\bmaxio_advanced_billing\b/ },
  typescript: { dir: "typescript", name: "TypeScript", marker: /maxio-advanced-billing/ },
};
const LANGS = Object.keys(SDK);
const EXT_LANG = {
  ".cs": "csharp", ".razor": "csharp", ".py": "python",
  ".ts": "typescript", ".tsx": "typescript", ".mts": "typescript", ".cts": "typescript",
  ".js": "typescript", ".jsx": "typescript", ".mjs": "typescript", ".cjs": "typescript", ".vue": "typescript",
};
// The product, package and namespace names. "advanced billing" alone is not a mention.
const MENTION = /(?:^|[^a-z0-9])(?:maxio|chargify)(?![a-z0-9])|maxioadvancedbilling/i;

// ---------------------------------------------------------------------------------------------
// small helpers
// ---------------------------------------------------------------------------------------------
const bytes = (s) => Buffer.byteLength(s, "utf8");
const posix = (p) => String(p).split("\\").join("/");
const tick = (p) => "`" + posix(p) + "`";
const unique = (list) => [...new Set(list)];
const exists = (p) => { try { fs.accessSync(p); return true; } catch { return false; } };
const isFile = (p) => { try { return fs.statSync(p).isFile(); } catch { return false; } };
const tryJson = (text) => { try { return JSON.parse(text); } catch { return undefined; } };

function readText(file, max = 1 << 20) {
  let fd;
  try {
    fd = fs.openSync(file, "r");
    const size = Math.min(fs.fstatSync(fd).size, max);
    const buffer = Buffer.alloc(size);
    fs.readSync(fd, buffer, 0, size, 0);
    return buffer.toString("utf8");
  } catch { return ""; } finally { if (fd !== undefined) try { fs.closeSync(fd); } catch { /* nothing to do */ } }
}
const readJson = (file) => { const value = tryJson(readText(file, 8 << 20)); return value === undefined ? null : value; };

function realPath(p) { // the real path of p, or of its nearest existing parent plus the rest
  let rest = [];
  for (let current = path.resolve(p); ;) {
    try { return path.join(fs.realpathSync.native(current), ...rest); } catch { /* go up */ }
    const parent = path.dirname(current);
    if (parent === current) return path.resolve(p);
    rest = [path.basename(current), ...rest];
    current = parent;
  }
}
function isInside(root, target) {
  const relative = path.relative(root, target);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}
function sleep(ms) { try { Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms); } catch { /* best effort */ } }

// ---------------------------------------------------------------------------------------------
// the payload, per host
// ---------------------------------------------------------------------------------------------
function readPayload() {
  let text = "";
  try { text = fs.readFileSync(0, "utf8"); } catch { /* no standard input */ }
  const value = tryJson(text.replace(/^\uFEFF/, ""));
  return value && typeof value === "object" && !Array.isArray(value) ? value : {};
}

function normalise(raw) {
  const text = (v) => (typeof v === "string" ? v : "");
  const eventName = text(raw.hook_event_name) || text(raw.hookEventName) || text(process.argv[3]);
  const roots = Array.isArray(raw.workspace_roots) ? raw.workspace_roots.filter((r) => typeof r === "string") : [];
  const cwd = text(raw.cwd) || roots[0] || process.env.CURSOR_PROJECT_DIR || process.env.CLAUDE_PROJECT_DIR || process.cwd();
  const input = raw.tool_input && typeof raw.tool_input === "object" && !Array.isArray(raw.tool_input) ? raw.tool_input : {};
  const tool = text(raw.tool_name);
  return {
    raw, eventName, event: eventName.toLowerCase(), cwd: path.resolve(cwd),
    session: text(raw.session_id) || text(raw.conversation_id),
    source: text(raw.source) || "startup", prompt: text(raw.prompt), tool, input,
    isShell: /^(bash|powershell|shell)$/i.test(tool),
    isEdit: /^(write|edit|multiedit|apply_patch)$/i.test(tool),
  };
}

// ---------------------------------------------------------------------------------------------
// per-session state: what has already been given
// ---------------------------------------------------------------------------------------------
const FRESH = () => ({ v: 2, card: false, uses: false, lang: null, langs: [], dirs: {}, ops: [], ptr: [], seen: [], rej: [] });

function stateFile(ev) {
  const candidates = [process.env.CLAUDE_PLUGIN_DATA, process.env.PLUGIN_DATA, path.join(os.tmpdir(), "maxio-advanced-billing-hook")];
  let id = ev.session.replace(/[^\w-]/g, "").slice(0, 80);
  if (!id) { // no session id: one state per project, restarted at every session start
    let hash = 5381;
    for (const ch of posix(ev.cwd).toLowerCase()) hash = ((hash * 33) ^ ch.charCodeAt(0)) >>> 0;
    id = `nosession-${hash.toString(36)}`;
  }
  for (const dir of candidates) {
    if (!dir) continue;
    try { fs.mkdirSync(dir, { recursive: true }); fs.accessSync(dir, fs.constants.W_OK); return path.join(dir, `session-${id}.json`); } catch { /* try the next */ }
  }
  return null;
}

function loadState(file) {
  const fresh = FRESH();
  const saved = file ? tryJson(readText(file)) : null;
  if (!saved || typeof saved !== "object" || Array.isArray(saved)) return fresh;
  const strings = (v) => (Array.isArray(v) ? v.filter((x) => typeof x === "string") : []);
  const state = {
    ...fresh, card: saved.card === true, uses: saved.uses === true,
    lang: SDK[saved.lang] ? saved.lang : null, langs: strings(saved.langs).filter((l) => SDK[l]),
    ops: strings(saved.ops), ptr: strings(saved.ptr), seen: strings(saved.seen), rej: strings(saved.rej),
  };
  if (saved.dirs && typeof saved.dirs === "object") for (const l of LANGS) if (typeof saved.dirs[l] === "string") state.dirs[l] = saved.dirs[l];
  return state;
}

function saveState(file, state) {
  const temp = `${file}.${process.pid}.tmp`;
  try {
    fs.writeFileSync(temp, JSON.stringify(state));
    for (let attempt = 0; ; attempt++) {
      try { fs.renameSync(temp, file); break; } catch (error) { if (attempt >= 5) throw error; sleep(10); }
    }
  } catch { try { fs.unlinkSync(temp); } catch { /* nothing to do */ } }
}

function sweep(dir) { // remove state left by sessions that ended long ago, this version's or the last one's
  try {
    const old = Date.now() - 14 * 24 * 3600 * 1000;
    for (const name of fs.readdirSync(dir).filter((n) => /^(session-|maxio-knowledge-).*\.(json|lock|tmp)$/.test(n)).slice(0, 300)) {
      const file = path.join(dir, name);
      try { if (fs.statSync(file).mtimeMs < old) fs.unlinkSync(file); } catch { /* another run removed it */ }
    }
  } catch { /* best effort */ }
}

// Runs change(state) on the state as it is on disk right now, under a lock, and writes the state
// back only when it changed. Two hooks that run at once therefore never both claim the same piece.
function commit(file, change) {
  if (!file) return change(FRESH());
  const lock = `${file}.lock`;
  let held = false;
  for (const deadline = Date.now() + 3000; ;) {
    try { fs.closeSync(fs.openSync(lock, "wx")); held = true; break; } catch (error) {
      if (error.code !== "EEXIST") break; // the folder cannot be locked: go on without
      try { if (Date.now() - fs.statSync(lock).mtimeMs > 10000) { fs.unlinkSync(lock); continue; } } catch { continue; }
      if (Date.now() > deadline) return null; // another run holds the lock: say nothing rather than twice
      sleep(10 + Math.floor(Math.random() * 25));
    }
  }
  try {
    const isNew = !exists(file);
    const before = loadState(file);
    const state = JSON.parse(JSON.stringify(before));
    const result = change(state);
    if (JSON.stringify(state) !== JSON.stringify(before)) { saveState(file, state); if (isNew) sweep(path.dirname(file)); }
    return result;
  } finally { if (held) try { fs.unlinkSync(lock); } catch { /* nothing to do */ } }
}

// ---------------------------------------------------------------------------------------------
// the project: does it use the SDK, in which language, and where is the SDK folder
// ---------------------------------------------------------------------------------------------
const SKIP_DIRS = new Set(["node_modules", "bin", "obj", "dist", "build", "out", "target", "vendor", "venv", "env", "__pycache__", "site-packages", "coverage"]);

function repoChain(cwd) { // the working directory and its parents up to the repository root
  const dirs = [];
  for (let dir = path.resolve(cwd), i = 0; i < 40; i++) {
    dirs.push(dir);
    if (exists(path.join(dir, ".git"))) return dirs;
    const parent = path.dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return [path.resolve(cwd)]; // no repository: only the working directory
}

function projectFileLanguage(name) {
  const n = name.toLowerCase();
  if (n === "package.json") return "typescript";
  if (n === "pyproject.toml" || n === "setup.py" || n === "setup.cfg" || n === "pipfile" || n === "uv.lock" || n === "poetry.lock" || /^requirements[\w.-]*\.txt$/.test(n)) return "python";
  if (n.endsWith(".csproj") || n.endsWith(".fsproj") || n === "directory.packages.props") return "csharp";
  return null;
}

// True when the project file names the SDK package exactly, as something the project depends on.
function dependsOnSdk(lang, name, text) {
  if (lang === "typescript") {
    const json = tryJson(text);
    if (json && typeof json === "object") {
      return ["dependencies", "devDependencies", "peerDependencies", "optionalDependencies"]
        .some((key) => json[key] && typeof json[key] === "object" && Object.hasOwn(json[key], "maxio-advanced-billing"));
    }
    return /"maxio-advanced-billing"\s*:\s*"/.test(text);
  }
  if (lang === "python") {
    let body = text.split(/\r?\n/).filter((line) => !/^\s*#/.test(line)).map((line) => line.replace(/\s#.*$/, "")).join("\n");
    // the SDK's own project file names itself; that is not a dependency
    if (/^(pyproject\.toml|setup\.py|setup\.cfg)$/i.test(name)) body = body.replace(/\bname\s*=\s*["']?maxio[-_]advanced[-_]billing["']?/gi, "");
    return /(?<![\w.-])maxio[-_]advanced[-_]billing(?![\w-])/i.test(body);
  }
  return /Include\s*=\s*"(?:[^"]*[\\/])?MaxioAdvancedBilling(?:\.csproj)?"/i.test(text);
}

// A Python install of the SDK in the project's own environment: { folder } is where a path install
// came from (pip records it in direct_url.json), or null when pip did not record a folder; { pkg } is the
// installed import package, which carries the agent files when the wheel was built with them.
function pythonInstall(dir, root) {
  const envs = [".venv", "venv", "env"].map((name) => path.join(dir, name));
  const active = process.env.VIRTUAL_ENV;
  if (active && isInside(root, path.resolve(active))) envs.unshift(path.resolve(active));
  for (const env of envs) {
    const sites = [path.join(env, "Lib", "site-packages")];
    try { for (const name of fs.readdirSync(path.join(env, "lib"))) if (/^python\d/i.test(name)) sites.push(path.join(env, "lib", name, "site-packages")); } catch { /* not a POSIX layout */ }
    for (const site of sites) {
      let names;
      try { names = fs.readdirSync(site); } catch { continue; }
      const info = names.find((name) => /^maxio_advanced_billing-.*\.dist-info$/i.test(name));
      if (!info) continue;
      const direct = readJson(path.join(site, info, "direct_url.json"));
      let folder = null;
      if (direct && typeof direct.url === "string" && direct.url.startsWith("file:")) { try { folder = fileURLToPath(direct.url); } catch { /* not a local path */ } }
      return { folder, pkg: path.join(site, "maxio_advanced_billing") };
    }
  }
  return null;
}

// Looks from the working directory up to the repository root, then down, for a project file that
// names the SDK package or for an installed copy. The walk down is bounded so a huge tree cannot
// approach the hook's timeout.
function detectProject(cwd) {
  const found = new Map(); // language -> the folder where it was found
  const note = (lang, dir) => { if (!found.has(lang)) found.set(lang, dir); };
  const scanFiles = (dir, entries) => {
    for (const entry of entries) {
      if (!entry.isFile()) continue;
      const lang = projectFileLanguage(entry.name);
      if (lang && !found.has(lang) && dependsOnSdk(lang, entry.name, readText(path.join(dir, entry.name), 4 << 20))) note(lang, dir);
    }
  };
  const list = (dir) => { try { return fs.readdirSync(dir, { withFileTypes: true }); } catch { return []; } };

  const chain = repoChain(cwd);
  const root = chain[chain.length - 1];
  for (const dir of chain) {
    scanFiles(dir, list(dir));
    if (isFile(path.join(dir, "node_modules", "maxio-advanced-billing", "package.json"))) note("typescript", dir);
    if (pythonInstall(dir, root)) note("python", dir);
  }

  const deadline = Date.now() + 1200;
  const queue = list(cwd).filter((e) => e.isDirectory()).map((e) => [path.join(cwd, e.name), 1, e.name]);
  for (let at = 0, visited = 0; at < queue.length && visited < 1500 && found.size < LANGS.length && Date.now() < deadline; at++) {
    const [dir, depth, name] = queue[at];
    if (name.startsWith(".") || SKIP_DIRS.has(name.toLowerCase()) || path.resolve(dir) === PLUGIN_ROOT) continue;
    visited++;
    const entries = list(dir);
    scanFiles(dir, entries);
    if (depth < 6) for (const entry of entries) if (entry.isDirectory()) queue.push([path.join(dir, entry.name), depth + 1, entry.name]);
  }
  return { langs: [...found.keys()], dirs: Object.fromEntries(found), root };
}

// The folder a C# project reference points into: the nearest parent of the referenced project
// that carries AGENTS.md.
function csharpReference(dirs) {
  for (const dir of dirs) {
    let names;
    try { names = fs.readdirSync(dir); } catch { continue; }
    for (const name of names.filter((n) => /\.(csproj|fsproj)$/i.test(n))) {
      const match = readText(path.join(dir, name)).match(/Include\s*=\s*"([^"]*MaxioAdvancedBilling\.csproj)"/i);
      if (!match) continue;
      for (let at = path.dirname(path.resolve(dir, match[1].split("\\").join("/"))), i = 0; i < 6; i++) {
        if (isFile(path.join(at, "AGENTS.md"))) return at;
        const parent = path.dirname(at);
        if (parent === at) break;
        at = parent;
      }
    }
  }
  return null;
}

// The installed C# package's folder in the NuGet cache, as the last restore recorded it: the project's
// obj/project.assets.json names the package folders and the package's path inside them.
function csharpPackage(dirs) {
  for (const dir of dirs) {
    const assets = readJson(path.join(dir, "obj", "project.assets.json"));
    if (!assets || typeof assets !== "object") continue;
    const library = Object.entries(assets.libraries ?? {}).find(([key, value]) =>
      /^MaxioAdvancedBilling\//i.test(key) && value && value.type === "package" && typeof value.path === "string");
    if (!library) continue;
    for (const root of Object.keys(assets.packageFolders ?? {})) {
      const candidate = path.join(root, library[1].path);
      if (isFile(path.join(candidate, "AGENTS.md"))) return candidate;
    }
  }
  return null;
}

// The SDK folder to name and to read knowledge from: the copy the project's code compiles against when
// it carries AGENTS.md (a source install or project reference, else the installed package), otherwise
// the copy this plugin bundles. Null when neither exists.
function sdkFolder(lang, cwd, hint) {
  if (!SDK[lang]) return null;
  const chain = repoChain(cwd);
  const root = chain[chain.length - 1];
  const dirs = unique([hint, ...chain].filter(Boolean));
  const usable = (dir) => (dir && isFile(path.join(dir, "AGENTS.md")) ? dir : null);
  let own = null;
  if (lang === "typescript") own = dirs.map((d) => usable(path.join(d, "node_modules", "maxio-advanced-billing"))).find(Boolean);
  else if (lang === "python") own = dirs.map((d) => { const install = pythonInstall(d, root); return usable(install?.folder) || usable(install?.pkg); }).find(Boolean);
  else own = usable(csharpReference(dirs)) || usable(csharpPackage(dirs));
  const dir = own || usable(path.join(PLUGIN_SDK, SDK[lang].dir));
  if (!dir) return null;
  const outside = !isInside(root, path.resolve(dir));
  const nuget = lang === "csharp" && Boolean(own) && outside && dir === csharpPackage(dirs);
  return { lang, dir, own: Boolean(own), outside, bundled: isInside(PLUGIN_SDK, path.resolve(dir)), nuget };
}
const bundledFolders = () => LANGS.map((lang) => ({ lang, dir: path.join(PLUGIN_SDK, SDK[lang].dir) })).filter((f) => isFile(path.join(f.dir, "AGENTS.md")));

// ---------------------------------------------------------------------------------------------
// does the project's always-on file already carry the rules? Decided per host; when unsure, no.
// ---------------------------------------------------------------------------------------------
function hasBlock(file, depth = 0) { // the file carries the block, or imports a file that does
  const text = readText(file, 512 << 10);
  if (!text) return false;
  if (text.includes(BLOCK_MARKER)) return true;
  if (depth >= 3) return false;
  const prose = text.replace(/```[\s\S]*?```/g, "").replace(/`[^`\n]*`/g, "");
  for (const match of prose.matchAll(/(?:^|\s)@(~?[^\s@]+)/g)) {
    const named = match[1].replace(/[),.;:]+$/, "");
    const target = named.startsWith("~/") ? path.join(os.homedir(), named.slice(2)) : path.resolve(path.dirname(file), named);
    if (isFile(target) && hasBlock(target, depth + 1)) return true;
  }
  return false;
}

function carriesRules(cwd) {
  try {
    const chain = repoChain(cwd);
    const agentsHasBlock = () => chain.some((dir) => readText(path.join(dir, "AGENTS.md"), 512 << 10).includes(BLOCK_MARKER));
    if (HOST === "codex") {
      // AGENTS.override.md or AGENTS.md, one per folder, from the repository root down, 32 KiB in all.
      let total = 0;
      for (const dir of [...chain].reverse()) {
        const text = [path.join(dir, "AGENTS.override.md"), path.join(dir, "AGENTS.md")].map((f) => readText(f, 512 << 10)).find((t) => t.trim());
        if (!text) continue;
        total += bytes(text);
        if (total > 32 * 1024) return false;
        if (text.includes(BLOCK_MARKER)) return true;
      }
      return false;
    }
    if (HOST === "cursor") { // this plugin's own rule is always applied; so is a project AGENTS.md
      return /^alwaysApply:\s*true\s*$/m.test(readText(path.join(PLUGIN_ROOT, "rules", "maxio-advanced-billing.mdc"))) || agentsHasBlock();
    }
    // Claude Code: CLAUDE.md, .claude/CLAUDE.md and CLAUDE.local.md, here and above; an @import is followed.
    const memory = (dir) => [path.join(dir, "CLAUDE.md"), path.join(dir, ".claude", "CLAUDE.md"), path.join(dir, "CLAUDE.local.md")];
    if (chain.some((dir) => memory(dir).some((file) => hasBlock(file)))) return true;
    // AGENTS.md is read only when no CLAUDE.md exists here or in any folder above.
    for (let dir = path.resolve(cwd), i = 0; i < 60; i++) {
      if (memory(dir).some(isFile)) return false;
      const parent = path.dirname(dir);
      if (parent === dir) break;
      dir = parent;
    }
    return agentsHasBlock();
  } catch { return false; }
}

// ---------------------------------------------------------------------------------------------
// what ships in the SDK folder
// ---------------------------------------------------------------------------------------------
function tenRules(dir) {
  const text = readText(path.join(dir, "AGENTS.md")).replace(/\r\n/g, "\n");
  const match = text.match(/<!-- ten-rules:start -->\n?([\s\S]*?)\n?<!-- ten-rules:end -->/);
  return match ? match[1].trim() : "";
}

function loadIndex(dir) {
  const json = readJson(path.join(dir, "knowledge", "index.json"));
  const operations = json && json.operations && typeof json.operations === "object" ? json.operations : null;
  if (!operations) return null;
  const index = { operations: {}, byMethod: new Map(), groups: new Set(), routes: [] };
  for (const [opId, op] of Object.entries(operations)) {
    if (!op || typeof op.call !== "string") continue;
    const parts = op.call.split(".");
    const method = parts[parts.length - 1];
    const group = (parts[parts.length - 2] || "").toLowerCase().replace(/[_$]/g, "");
    const entry = { opId, call: op.call, method, route: typeof op.route === "string" ? op.route : "", notes: typeof op.notes === "string" ? op.notes : null, always: typeof op.always === "string" ? op.always : null };
    index.operations[opId] = entry;
    if (!index.byMethod.has(method)) index.byMethod.set(method, []);
    index.byMethod.get(method).push(entry);
    if (group) index.groups.add(group);
    const [verb, template] = entry.route.split(/\s+/);
    if (verb && template) {
      const segments = template.split("/").filter(Boolean);
      const pattern = segments.map((s) => (s.includes("{") ? s.split(/\{[^}]*\}/).map(escapeRegex).join("[^/]+") : escapeRegex(s))).join("/");
      index.routes.push({ opId, verb: verb.toUpperCase(), regex: new RegExp(`^/${pattern}/?$`, "i"), literal: segments.filter((s) => !s.includes("{")).length });
    }
  }
  return index;
}
const escapeRegex = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function loadFailures(dir) {
  const json = readJson(path.join(dir, "knowledge", "failures.json"));
  if (!Array.isArray(json)) return null;
  return json.filter((row) => row && Number.isInteger(row.status) && typeof row.operationId === "string")
    .map((row) => ({ ...row, patterns: Array.isArray(row.patterns) ? row.patterns.filter((p) => typeof p === "string" && p.trim().length >= 8) : [] }));
}

const slug = (heading) => heading.trim().toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, "").replace(/\s+/g, "-");
const sectionCache = new Map();
// An operation's notes: the section its index entry names, as { file, heading, text }.
function notesSection(dir, ref) {
  if (typeof ref !== "string" || !ref) return null;
  const key = `${dir}|${ref}`;
  if (sectionCache.has(key)) return sectionCache.get(key);
  const hash = ref.lastIndexOf("#");
  const file = hash < 0 ? ref : ref.slice(0, hash);
  const anchor = hash < 0 ? "" : ref.slice(hash + 1).toLowerCase();
  const lines = readText(path.join(dir, file)).replace(/\r\n/g, "\n").split("\n");
  let result = null, start = -1, level = 0, heading = "", fenced = false;
  for (let i = 0; i < lines.length && !result; i++) {
    if (/^\s*(```|~~~)/.test(lines[i])) { fenced = !fenced; continue; }
    const match = fenced ? null : lines[i].match(/^(#{1,6})\s+(.*?)\s*#*\s*$/);
    if (!match) continue;
    if (start < 0) {
      if (anchor && (slug(match[2]) === anchor || slug(match[2].split(/\s/)[0]) === anchor)) { start = i; level = match[1].length; heading = match[2].replace(/`/g, "").trim(); }
    } else if (match[1].length <= level) result = { file, heading, text: lines.slice(start, i).join("\n").trim() };
  }
  if (!result && start >= 0) result = { file, heading, text: lines.slice(start).join("\n").trim() };
  // The closing sources paragraph is provenance: the file keeps it, and a message leaves it out to make
  // room for the rules to check the code against.
  if (result) result.text = result.text.replace(/\n+\*\*Sources:\*\*(?:(?!\n#)[\s\S])*$/, "").trim();
  sectionCache.set(key, result);
  return result;
}
// "file, section heading" for a notes reference, relative to the SDK folder; the file alone when
// the section cannot be found. A message names the SDK folder once and uses these after that.
function notesPointer(folder, ref) {
  const section = notesSection(folder.dir, ref);
  if (section) return `${tick(section.file)}, section "${section.heading}"`;
  const hash = ref.lastIndexOf("#");
  return tick(hash < 0 ? ref : ref.slice(0, hash));
}

// Replaces this SDK's method names with the API's operationIds, for text shown before the
// language is known.
function neutralNames(text, index) {
  if (!index) return text;
  return text.replace(/`([A-Za-z_][\w]*)`/g, (whole, name) => {
    const ops = index.byMethod.get(name);
    return ops && ops.length === 1 ? "`" + ops[0].opId + "`" : whole;
  });
}

// ---------------------------------------------------------------------------------------------
// the card: where the SDK folder is, and the ten rules
// ---------------------------------------------------------------------------------------------
function outsideNote(folder) {
  if (!folder.outside) return "";
  if (HOST === "claude" && (folder.bundled || folder.nuget)) return " It is outside this project. This plugin approves Read, Glob and Grep on it; a shell command that reads it may still ask for permission.";
  return " It is outside this project, so reading it may ask for permission.";
}

const copyOf = (folder) => (folder.own ? "the copy this project has installed" : "the copy bundled with the maxio-advanced-billing plugin");
// The line every later message ends with, so its paths can be relative to the SDK folder.
const folderLine = (folder) => `Paths in this message are relative to the Maxio Advanced Billing ${SDK[folder.lang].name} SDK folder, ${tick(folder.dir)}.`;

function card(folder, carried) {
  const name = SDK[folder.lang].name;
  const carrier = HOST === "cursor" ? "the always-applied maxio-advanced-billing rule already carries Maxio's ten rules" : "this project's own instructions already carry Maxio's ten rules";
  const locator = `Maxio Advanced Billing: ${carrier}. On this machine the ${name} SDK folder they refer to is ${tick(folder.dir)}, ${copyOf(folder)}.${outsideNote(folder)} In that folder, \`AGENTS.md\` is the entry point and \`knowledge/failures.md\` lists Maxio's rejections by status and message.`;
  const rules = carried ? "" : tenRules(folder.dir);
  if (!rules) return locator;
  const full = [
    "## Maxio Advanced Billing: the SDK folder and the ten rules",
    "",
    `This project uses the Maxio Advanced Billing ${name} SDK. On this machine the SDK folder is ${tick(folder.dir)}, ${copyOf(folder)}.${outsideNote(folder)} It holds the workflow, the contract map, Maxio's business rules and recipes to copy. The paths below are relative to it.`,
    "",
    "`AGENTS.md` is the entry point: read it and follow it before writing or changing Maxio code. Read selectively: the short index first, then only the sections the task touches (for each operation in scope, the Provider rules or Provider notes line on its map block and the notes section it links, not the whole notes file; the rule, decision and lifecycle sections those cite; the one recipe you copy). SDK names and Maxio's rules come from those files, never from memory.",
    "",
    "The ten rules agents most often get wrong. They are the same list as in `AGENTS.md` and `sdk-map.md`, so they need not be read again there:",
    rules,
    "",
    "When Maxio rejects a call, find its status and message in `knowledge/failures.md` before changing code.",
    "",
    KEEP_RULES,
  ].join("\n");
  return bytes(full) <= MAX_BYTES ? full : locator;
}

// The card without the ten rules, for the one edit whose write would lose its notes beside them.
// The full card is still owed, so it comes with a later message.
function shortCard(folder) {
  return `Maxio Advanced Billing: this project uses the ${SDK[folder.lang].name} SDK. On this machine the SDK folder is ${tick(folder.dir)}, ${copyOf(folder)}.${outsideNote(folder)} Paths in this message are relative to it. Its \`AGENTS.md\` is the entry point and starts with the ten rules agents most often get wrong: read them before you change more Maxio code. \`knowledge/failures.md\` lists Maxio's rejections by status and message.`;
}

// Given with the ten rules, so only when the project's always-on file does not carry them yet.
const KEEP_RULES = "This project's own instructions do not carry these rules yet. Make adding the block from `knowledge/AGENTS.block.md` to the project's `AGENTS.md` a step of your plan, so the user can decline it, and say in your report whether you added it. This is the request that section \"The project block\" of the SDK folder's `AGENTS.md` says to follow. Section 4 of the maxio-advanced-billing skill says how.";

// The card for a prompt that names Maxio in a project whose language is not known.
function neutralCard(carried) {
  const folders = bundledFolders();
  if (!folders.length) return "";
  const list = folders.map((f) => `${SDK[f.lang].name} at ${tick(f.dir)}`).join("; ");
  const where = `The maxio-advanced-billing plugin bundles a Maxio Advanced Billing SDK folder per language: ${list}. They are outside this project${HOST === "claude" ? "; this plugin approves Read, Glob and Grep on them" : ""}. In the folder for the project's language, \`AGENTS.md\` is the entry point and \`knowledge/failures.md\` lists Maxio's rejections by status and message.`;
  const source = folders.find((f) => f.lang === "typescript") || folders[0];
  const rules = carried ? "" : neutralNames(tenRules(source.dir), loadIndex(source.dir));
  if (!rules) return `Maxio Advanced Billing: ${where}`;
  const full = [
    "## Maxio Advanced Billing: the SDK folders and the ten rules",
    "",
    where,
    "",
    "Read that `AGENTS.md` and follow it before writing or changing Maxio code. Read selectively: the short index first, then only the sections the task touches. SDK names and Maxio's rules come from those files, never from memory.",
    "",
    "The ten rules agents most often get wrong:",
    rules,
    "",
    "The operation names in these rules are the API's operationIds. Each SDK spells them its own way; its `sdk-map.md` gives the spelling.",
    "",
    KEEP_RULES.replace("`knowledge/AGENTS.block.md`", "`knowledge/AGENTS.block.md` in the folder for the project's language"),
  ].join("\n");
  return bytes(full) <= MAX_BYTES ? full : `Maxio Advanced Billing: ${where}`;
}

// Works out which card applies now. Returns { text, lang, langs, dirs } or null.
function planCard(ev, snapshot, { always }) {
  const project = detectProject(ev.cwd);
  const langs = unique([...project.langs, ...snapshot.langs]);
  const dirs = { ...snapshot.dirs, ...project.dirs };
  const lang = project.langs[0] || snapshot.lang;
  if (!lang && !always) return null;
  const carried = carriesRules(ev.cwd);
  const folder = lang ? sdkFolder(lang, ev.cwd, dirs[lang]) : null;
  const text = folder ? card(folder, carried) : lang ? "" : neutralCard(carried);
  return { text, lang, langs, dirs, uses: project.langs.length > 0 || snapshot.uses };
}
function rememberProject(state, plan) {
  if (plan.uses) state.uses = true;
  if (plan.lang) state.lang = plan.lang;
  state.langs = unique([...state.langs, ...plan.langs]);
  state.dirs = { ...state.dirs, ...plan.dirs };
}

function onSessionStart(ev, file) {
  const snapshot = loadState(file);
  const renewed = ev.source === "compact" || ev.source === "clear";
  // A resumed transcript already holds what earlier hooks gave it.
  if (ev.source === "resume" && snapshot.card) return null;
  // In Cursor the plugin's rule is always applied, so the line that resolves its path is given
  // in every session; elsewhere the card is for projects that use the SDK.
  const plan = planCard(ev, snapshot, { always: HOST === "cursor" || (renewed && snapshot.card) });
  return commit(file, (state) => {
    if (!file && !plan) return null;
    if (renewed) { state.ops = []; state.ptr = []; state.rej = []; state.card = false; }
    if (!ev.session && ev.source === "startup") Object.assign(state, FRESH());
    if (!plan) return null;
    rememberProject(state, plan);
    if (state.card || !plan.text) return null;
    state.card = true;
    return plan.text;
  });
}

function onCompact(file) { // Cursor has no session start after compaction: forget what was given
  if (!file || !exists(file)) return null;
  commit(file, (state) => { state.ops = []; state.ptr = []; state.rej = []; return null; });
  return null;
}

function onPrompt(ev, file) {
  if (!MENTION.test(ev.prompt)) return null;
  const snapshot = loadState(file);
  if (snapshot.card) return null;
  const plan = planCard(ev, snapshot, { always: true });
  if (!plan || !plan.text) return null;
  return commit(file, (state) => {
    rememberProject(state, plan);
    if (state.card) return null;
    state.card = true;
    return plan.text;
  });
}

// ---------------------------------------------------------------------------------------------
// edits: which Maxio operations does this edit call?
// ---------------------------------------------------------------------------------------------
function editedFiles(ev) { // [{ file, added }] with absolute paths; added is null when the payload has no text
  const input = ev.input;
  const named = [input.file_path, input.path, input.target_file, input.filePath].find((v) => typeof v === "string" && v);
  const command = Array.isArray(input.command) ? input.command.join("\n") : input.command;
  const patch = [command, input.input, input.patch].find((v) => typeof v === "string" && /^\*\*\* (Add|Update) File: /m.test(v));
  if (patch) {
    const files = [];
    let current = null;
    for (const line of patch.split(/\r?\n/)) {
      const head = line.match(/^\*\*\* (Add|Update|Delete) File: (.+)$/);
      if (head) { current = head[1] === "Delete" ? null : { file: path.resolve(ev.cwd, head[2].trim()), lines: [] }; if (current) files.push(current); continue; }
      const move = line.match(/^\*\*\* Move to: (.+)$/);
      if (move && current) { current.file = path.resolve(ev.cwd, move[1].trim()); continue; }
      if (current && line.startsWith("+")) current.lines.push(line.slice(1));
    }
    return files.map((f) => ({ file: f.file, added: f.lines.join("\n") }));
  }
  if (!named) return [];
  const texts = ["content", "contents", "new_string", "text", "code_edit"].map((key) => input[key]).filter((v) => typeof v === "string");
  if (Array.isArray(input.edits)) for (const edit of input.edits) if (edit && typeof edit.new_string === "string") texts.push(edit.new_string);
  return [{ file: path.resolve(ev.cwd, named), added: texts.length ? texts.join("\n") : null }];
}

function stripComments(text, lang) {
  let code = text.replace(/\/\*[\s\S]*?\*\//g, " ").replace(/(^|[^:\\"'`\w])\/\/[^\n]*/g, "$1");
  if (lang === "python") code = code.replace(/(^|[ \t])#[^\n]*/gm, "$1");
  return code;
}
const loose = (name) => name.toLowerCase().replace(/[_$]/g, "");

// The operations the text calls, in order of appearance. A call counts when the object it is made
// on is one of the SDK's API groups (client.subscriptions.createSubscription), or a variable the
// text assigns one to. stripe.createCustomer(...) in a file that also imports this SDK does not.
function callsIn(text, context, index, lang) {
  const code = stripComments(text, lang);
  const isGroup = (name) => { const n = loose(name); return [...index.groups].some((group) => n.includes(group)); };
  const aliases = new Set();
  for (const match of stripComments(`${context}\n${text}`, lang).matchAll(/([A-Za-z_$][\w$]*)[ \t]*(?::[^=\n]+)?=[ \t]*(?:await[ \t]+)?[\w$.?!()\t ]*?\.[ \t]*([A-Za-z_$][\w$]*)[ \t]*(?:;|\r?$)/gm)) {
    if (isGroup(match[2])) aliases.add(match[1]);
  }
  const found = [];
  const call = /(?:([A-Za-z_$][\w$]*)\s*[?!]?\s*\.\s*)?([A-Za-z_$][\w$]*)\s*[?!]?\s*\.\s*([A-Za-z_$][\w$]*)\s*(?:<[^<>()\n]*>)?\s*(?:\?\.)?\s*\(/g;
  for (const match of code.matchAll(call)) {
    const ops = index.byMethod.get(match[3]) || index.byMethod.get(match[3].replace(/Async$/, ""));
    if (!ops) continue;
    const receivers = [match[2], match[1]].filter(Boolean);
    if (receivers.some((r) => isGroup(r) || aliases.has(r))) for (const op of ops) found.push(op.opId);
    call.lastIndex = match.index + match[0].length - 1; // a chained call may start right here
  }
  return unique(found);
}

function onEdit(ev, file) {
  const snapshot = loadState(file);
  const perLang = new Map(); // language -> { text, context }
  for (const edited of editedFiles(ev)) {
    const lang = EXT_LANG[path.extname(edited.file).toLowerCase()];
    if (!lang) continue;
    const onDisk = readText(edited.file, 512 << 10);
    const text = edited.added === null ? onDisk : edited.added;
    const known = snapshot.uses && snapshot.langs.includes(lang);
    if (!known && !SDK[lang].marker.test(text) && !SDK[lang].marker.test(onDisk)) continue;
    const entry = perLang.get(lang) || { text: "", context: "" };
    entry.text += `\n${text}`;
    entry.context += `\n${onDisk}`;
    perLang.set(lang, entry);
  }
  if (!perLang.size) return null;

  const called = []; // { lang, folder, op } in order of appearance
  const rowsOf = new Map(); // operationId -> how many rejections failures.json documents for it
  const folders = {};
  for (const [lang, entry] of perLang) {
    const folder = sdkFolder(lang, ev.cwd, snapshot.dirs[lang]);
    const index = folder ? loadIndex(folder.dir) : null;
    if (!index) continue; // no knowledge to give: stay silent
    folders[lang] = folder;
    for (const row of loadFailures(folder.dir) || []) rowsOf.set(row.operationId, (rowsOf.get(row.operationId) || 0) + 1);
    for (const opId of callsIn(entry.text, entry.context, index, lang)) called.push({ lang, folder, op: index.operations[opId] });
  }
  const langs = [...perLang.keys()];
  const carried = called.length && !snapshot.card ? carriesRules(ev.cwd) : false;
  const isWrite = (op) => !/^(GET|HEAD)\b/i.test(op.route);
  const rank = (item) => (isWrite(item.op) ? 2 : 0) + (item.op.always ? 1 : 0);

  return commit(file, (state) => {
    state.uses = true;
    state.langs = unique([...state.langs, ...langs]);
    if (!state.lang) state.lang = langs[0];
    state.seen = unique([...state.seen, ...called.map((c) => c.op.opId)]);
    const fresh = called.filter((c) => !state.ops.includes(c.op.opId));
    if (!fresh.length) return null;

    const withNotes = fresh.filter((c) => c.op.notes).map((c, order) => ({ ...c, order, section: notesSection(c.folder.dir, c.op.notes) }));
    const without = fresh.filter((c) => !c.op.notes);
    // Writes first, then operations with an "Always" line: a signup's notes are never the ones left out.
    // Among those, the operations Maxio rejects in the most documented ways come first.
    withNotes.sort((a, b) => rank(b) - rank(a) || (rowsOf.get(b.op.opId) || 0) - (rowsOf.get(a.op.opId) || 0) || a.order - b.order);
    let head = state.card || !folders[fresh[0].lang] ? "" : card(folders[fresh[0].lang], carried);
    if (!withNotes.length && !head) return null;

    const name = (c) => "`" + c.op.call + "`";
    const oneFolder = new Set(fresh.map((c) => c.folder.dir)).size === 1;
    const pointer = (c) => notesPointer(c.folder, c.op.notes) + (oneFolder ? "" : ` in ${tick(c.folder.dir)}`);
    const compose = (tiers, listed) => {
      const parts = [];
      if (head) parts.push(head);
      const full = withNotes.filter((c, i) => tiers[i] === "full");
      const lines = withNotes.filter((c, i) => tiers[i] === "line");
      const names = withNotes.filter((c, i) => tiers[i] === "name");
      if (full.length) {
        parts.push("Maxio's notes for the operation(s) this edit calls. They are rules the SDK's types cannot enforce, so check the code just written against them now.");
        parts.push(full.map((c) => `From ${pointer(c)}:\n\n${c.section.text}`).join("\n\n---\n\n"));
      }
      if (lines.length) {
        parts.push(`${full.length ? "This edit also calls these operations. Their notes are not shown here, to keep this message within its size limit" : "This edit calls these Maxio operations. Their notes are not shown here, to keep this message within its size limit"}; each has a notes section to read before relying on the call:\n` +
          lines.map((c) => `- ${name(c)}${c.op.always ? `. Always: ${c.op.always}` : "."} Notes: ${pointer(c)}.`).join("\n"));
      }
      if (names.length) {
        const shown = names.slice(0, listed);
        const more = names.length - shown.length;
        parts.push(`Also called, with provider notes: ${shown.map(name).join(", ")}${more ? `${shown.length ? " and " : ""}${more} more` : ""}. \`knowledge/index.json\` names the notes section of each.`);
      }
      if (without.length && (full.length || lines.length || names.length || head)) {
        const shown = without.slice(0, 12);
        parts.push(`Maxio has published no notes for: ${shown.map(name).join(", ")}${without.length > shown.length ? ` and ${without.length - shown.length} more` : ""}.`);
      }
      if (!head && oneFolder) parts.push(folderLine(fresh[0].folder));
      return parts.join("\n\n");
    };

    // Every operation starts as one line (its "Always" line and where its notes are). If that is
    // too much, the last ones become names only. Then, in order, each is shown in full while it fits.
    const fit = () => {
      const tiers = withNotes.map((c) => (c.section ? "line" : "name"));
      let listed = withNotes.length;
      for (let i = withNotes.length - 1; i >= 0 && bytes(compose(tiers, listed)) > MAX_BYTES; i--) tiers[i] = "name";
      while (listed > 0 && bytes(compose(tiers, listed)) > MAX_BYTES) listed--;
      for (let i = 0; i < withNotes.length; i++) {
        if (tiers[i] !== "line") continue;
        tiers[i] = "full";
        if (bytes(compose(tiers, listed)) > MAX_BYTES) tiers[i] = "line";
      }
      // The first write's notes are never the ones left out: when they do not fit, the operations after
      // them give up their lines, from the last one, until they do.
      if (withNotes.length && isWrite(withNotes[0].op) && tiers[0] === "line") {
        const trial = tiers.map((t, i) => (i === 0 ? "full" : t === "full" ? "line" : t));
        for (let i = trial.length - 1; i > 0 && bytes(compose(trial, listed)) > MAX_BYTES; i--) if (trial[i] === "line") trial[i] = "name";
        if (bytes(compose(trial, listed)) <= MAX_BYTES) return { tiers: trial, listed };
      }
      return { tiers, listed };
    };
    let { tiers, listed } = fit();
    // The first write's notes matter more at this edit than the ten rules. When the card crowds them
    // out, a short card goes now and the full one with a later message.
    let cardOwed = false;
    if (head && !carried && withNotes.length && isWrite(withNotes[0].op) && tiers[0] !== "full") {
      const fullCard = head;
      head = shortCard(folders[fresh[0].lang]);
      ({ tiers, listed } = fit());
      if (tiers[0] === "full") cardOwed = true;
      else { head = fullCard; ({ tiers, listed } = fit()); }
    }
    const text = compose(tiers, listed);
    if (!text || bytes(text) > MAX_BYTES) return null;

    if (head && !cardOwed) state.card = true;
    withNotes.forEach((c, i) => {
      if (tiers[i] === "full") { state.ops.push(c.op.opId); state.ptr = state.ptr.filter((id) => id !== c.op.opId); }
      else if (!state.ptr.includes(c.op.opId)) state.ptr.push(c.op.opId);
      else state.ops.push(c.op.opId); // pointed at twice: do not repeat it again
    });
    for (const c of without) state.ops.push(c.op.opId);
    state.ops = unique(state.ops);
    return text;
  });
}

// ---------------------------------------------------------------------------------------------
// command output: a Maxio rejection the agent just saw
// ---------------------------------------------------------------------------------------------
function shellOutput(raw) {
  const parts = [];
  const add = (v) => { if (typeof v === "string" && v) parts.push(v); };
  const collect = (value) => {
    if (typeof value === "string") { const parsed = /^\s*[{[]/.test(value) ? tryJson(value) : undefined; if (parsed && typeof parsed === "object") collect(parsed); else add(value); return; }
    if (!value || typeof value !== "object") return;
    for (const key of ["stdout", "stderr", "output", "aggregated_output", "formatted_output", "text", "content"]) {
      const field = value[key];
      if (Array.isArray(field)) field.forEach((item) => add(typeof item === "string" ? item : item && item.text)); else add(field);
    }
  };
  collect(raw.tool_response);
  collect(raw.tool_output);
  add(raw.error);
  add(raw.error_message);
  const text = parts.join("\n");
  return text.length > 2_000_000 ? `${text.slice(0, 1_000_000)}\n${text.slice(-1_000_000)}` : text;
}

const READERS = new Set(["cat", "type", "more", "less", "head", "tail", "bat", "nl", "sed", "awk", "grep", "egrep", "fgrep", "rg", "ag", "ack", "findstr", "find", "fd", "ls", "dir", "tree", "wc", "sort", "uniq", "cut", "tr", "jq", "yq", "strings", "diff", "cmp",
  "get-content", "gc", "select-string", "sls", "get-childitem", "gci", "get-item", "select-object", "select", "where-object", "sort-object", "measure-object", "out-string", "format-list", "format-table"]);
const NEUTRAL = new Set(["cd", "pushd", "popd", "echo", "printf", "set", "export", "true", "test", "[", "write-output", "write-host", "set-location", "sl", "exit"]);
const GIT_READS = new Set(["show", "diff", "log", "grep", "blame", "status", "ls-files", "cat-file", "stash", "branch", "shortlog", "reflog", "ls-tree"]);

// True when the command only reads files (cat, grep, git diff ...) and so runs no code that could
// have called Maxio. Reading log files does not count: a log can hold a real rejection.
function onlyReadsFiles(command) {
  let readers = 0;
  const files = [];
  for (const segment of command.split(/\|\||&&|[|;\n]/)) {
    const words = segment.trim().replace(/^[&(\s]+/, "").split(/\s+/).filter((w) => w && !/^\w+=/.test(w));
    if (!words.length) continue;
    const program = path.basename(words[0].replace(/^["']|["']$/g, "")).toLowerCase().replace(/\.(exe|cmd|bat|ps1)$/, "");
    if (NEUTRAL.has(program)) continue;
    if (!(READERS.has(program) || (program === "git" && GIT_READS.has((words.find((w, i) => i > 0 && !w.startsWith("-")) || "").toLowerCase())))) return false;
    readers++;
    for (const word of words.slice(1)) { const ext = path.extname(word.replace(/["']/g, "")).toLowerCase(); if (ext && /^\.[a-z0-9]{1,8}$/.test(ext)) files.push(ext); }
  }
  if (!readers) return false;
  return !(files.length && files.every((ext) => [".log", ".out", ".err", ".stdout", ".stderr", ".trace"].includes(ext)));
}
// Installing, restoring or building: output that names the package there is not about a call to Maxio.
const PACKAGE_WORK = /(?:^|[\s;&|(])(?:npm|pnpm|yarn|bun)\s+(?:i|install|add|ci|update|up|view|info|ls|list|pack|publish|outdated|audit)\b|(?:^|[\s;&|(])(?:pip3?|uv|poetry|pipenv|conda)\s+(?:install|add|download|show|index|sync|lock|pip|update|wheel)\b|-m\s+pip\s+|(?:^|[\s;&|(])dotnet\s+(?:restore|add|build|publish|pack|nuget|new|tool)\b|(?:^|[\s;&|(])nuget\s/i;

const VERBS = "GET|POST|PUT|PATCH|DELETE|HEAD";
const REASONS = "Bad Request|Unauthorized|Payment Required|Forbidden|Not Found|Method Not Allowed|Not Acceptable|Request Timeout|Conflict|Gone|Unprocessable Entity|Unprocessable Content|Too Many Requests|Internal Server Error|Bad Gateway|Service Unavailable|Gateway Timeout|BadRequest|PaymentRequired|NotFound|MethodNotAllowed|RequestTimeout|UnprocessableEntity|UnprocessableContent|TooManyRequests|InternalServerError|BadGateway|ServiceUnavailable|GatewayTimeout";
// a number followed by one of these is a count or a size, not a status
const NOT_A_COUNT = "(?!\\s*(?:%|ms\\b|s\\b|kb\\b|mb\\b|bytes?\\b|rows?\\b|items?\\b|records?\\b|results?\\b|lines?\\b|files?\\b|tests?\\b|passed\\b|failed\\b|passing\\b|objects?\\b|entries\\b|packages?\\b|modules?\\b|insertions?\\b|deletions?\\b|subscriptions?\\b|customers?\\b|invoices?\\b|events?\\b|times\\b|\\.\\d|,\\d))";
const STATUS_FORMS = [
  // the three SDKs' own exception formats
  { kind: "typescript", re: new RegExp(`\\b(${VERBS})\\s+(https?:\\/\\/[^\\s"'<>\`]+)\\s+failed with (?:status )?([45]\\d\\d)\\b${NOT_A_COUNT}`, "g"), verb: 1, url: 2, status: 3 },
  { kind: "csharp", re: new RegExp(`\\b(${VERBS})\\s+(https?:\\/\\/[^\\s"'<>\`]+)\\s+returned ([45]\\d\\d)(?: \\([A-Za-z]+\\))?\\.(?!\\d)`, "g"), verb: 1, url: 2, status: 3 },
  { kind: "python", re: /\bApiError(?:\[[^\]\n]*\])?:\s+HTTP ([45]\d\d): [A-Za-z_]\w*/g, status: 1 },
  { kind: "python", re: /\bApiError\(status_code=([45]\d\d), error=[A-Za-z_]\w*\)/g, status: 1 },
  { kind: "python-bare", re: /(?:^|[\s:])HTTP ([45]\d\d): [A-Z]\w*[ \t]*$/gm, status: 1 },
  // a status in an HTTP context: next to HTTP, "status", "failed with", "returned", or a reason phrase
  { kind: "http", re: new RegExp(`\\bHTTP(?:\\/\\d(?:\\.\\d)?)?(?:\\s+(?:error|status(?:\\s+code)?|response(?:\\s+code)?))?\\s*[:=]?\\s*([45]\\d\\d)\\b${NOT_A_COUNT}`, "gi"), status: 1 },
  { kind: "http", re: new RegExp(`\\bstatus(?:[ _-]?code)?["']?\\s*(?:[:=]|is\\b|was\\b|of\\b)?\\s*["']?([45]\\d\\d)\\b${NOT_A_COUNT}`, "gi"), status: 1 },
  { kind: "http", re: new RegExp(`\\b(?:failed|fails|responded|rejected|answered|replied|errored) with\\s+(?:(?:an?|the|HTTP|status|code|error)\\s+)*([45]\\d\\d)\\b${NOT_A_COUNT}`, "gi"), status: 1 },
  { kind: "http", re: new RegExp(`\\breturned\\s+(?:(?:an?|the|HTTP|status|code|error)\\s+)*([45]\\d\\d)\\b${NOT_A_COUNT}`, "gi"), status: 1 },
  { kind: "http", re: new RegExp(`\\b([45]\\d\\d)\\s+\\(?(?:${REASONS})\\b`, "gi"), status: 1 },
];
const MAXIO_HOST = /(?:^|[^\w.-])(?!(?:developers|docs|help|www|support|status|app)\.)(?:[a-z0-9-]+\.)+(?:chargify\.com|ebilling\.maxio\.com)\b/i;
const SDK_NAME = /maxio[-_]advanced[-_]billing|MaxioAdvancedBilling/;
const ERROR_LINE = /error|exception|traceback|failed|fatal|^\s+at\s|File "/i;
const OTHER_URL = /https?:\/\/([^\s/"'<>:]+)/gi;

// The route of a URL or path, matched against the index. The route with most literal segments wins.
function operationFor(index, verb, target) {
  if (!verb || !target) return null;
  let route = target.replace(/^https?:\/\/[^/]+/i, "").split(/[?#]/)[0];
  if (!route.startsWith("/")) return null;
  for (let attempt = 0; attempt < 3; attempt++) {
    const hits = index.routes.filter((r) => r.verb === verb.toUpperCase() && r.regex.test(route)).sort((a, b) => b.literal - a.literal);
    if (hits.length) return index.operations[hits[0].opId];
    const next = route.indexOf("/", 1); // a base URL may carry a leading segment
    if (next < 0) break;
    route = route.slice(next);
  }
  return null;
}

// Every status the output shows in an HTTP context, with the evidence that it came from Maxio.
function rejectionsIn(output, command, index, pythonKnown) {
  const lines = output.split(/\r?\n/);
  const lineAt = (offset) => { let n = 0; for (let i = output.indexOf("\n"); i >= 0 && i < offset; i = output.indexOf("\n", i + 1)) n++; return n; };
  const near = (line, span, test) => { for (let i = Math.max(0, line - span); i <= Math.min(lines.length - 1, line + span); i++) if (test(lines[i], i)) return true; return false; };
  const foreignUrl = (text) => [...text.matchAll(OTHER_URL)].some((m) => !MAXIO_HOST.test(` ${m[1]}`) && !/^(localhost|127\.0\.0\.1|\[::1\])$/i.test(m[1]));
  const packageWork = PACKAGE_WORK.test(command);
  const sdkNamed = SDK_NAME.test(output);
  const found = [];
  const taken = new Set();

  for (const form of STATUS_FORMS) {
    form.re.lastIndex = 0;
    for (const match of output.matchAll(form.re)) {
      const line = lineAt(match.index);
      const status = Number(match[form.status]);
      if (taken.has(`${line}|${status}`)) continue;
      const verb = form.verb ? match[form.verb] : null;
      const url = form.url ? match[form.url].replace(/[.,;:)\]]+$/, "") : null;
      let op = null, evidence = false, lang = null;
      if (form.kind === "typescript" || form.kind === "csharp") {
        op = operationFor(index, verb, url);
        // Other APIMatic SDKs print the same format, so the host must be Maxio's; a local mock
        // server counts only when the SDK's own name is next to it.
        evidence = MAXIO_HOST.test(` ${url}`) || (!foreignUrl(url) && near(line, 12, (l) => SDK_NAME.test(l)));
        if (!evidence) op = null;
        lang = form.kind;
      } else if (form.kind === "python") {
        evidence = sdkNamed || pythonKnown;
        lang = "python";
      } else if (form.kind === "python-bare") {
        evidence = (sdkNamed || pythonKnown) && !foreignUrl(lines[line] || "");
        lang = "python";
      } else {
        if (near(line, 1, (l) => foreignUrl(l))) continue; // the status belongs to another host
        evidence = near(line, 12, (l) => MAXIO_HOST.test(l)) || MAXIO_HOST.test(command) ||
          (!packageWork && near(line, 12, (l) => SDK_NAME.test(l) && ERROR_LINE.test(l)));
      }
      if (!evidence) continue;
      taken.add(`${line}|${status}`);
      if (!op) op = operationNear(lines, line, command, index);
      found.push({ status, line, op, lang, sdkFormat: form.kind !== "http" });
    }
  }
  return found.sort((a, b) => a.line - b.line);
}

// The operation a status belongs to, when its line does not say: a request line or a stack frame
// near it, or the URL of a curl command.
function operationNear(lines, line, command, index) {
  const request = new RegExp(`\\b(${VERBS})\\s+((?:https?:\\/\\/[^\\s"'<>\`]+)|\\/[^\\s"'<>\`]*)`, "g");
  for (let distance = 0; distance <= 12; distance++) {
    for (const i of distance ? [line - distance, line + distance] : [line]) {
      if (i < 0 || i >= lines.length) continue;
      for (const match of lines[i].matchAll(request)) {
        if (/^https?:/i.test(match[2]) && !MAXIO_HOST.test(` ${match[2]}`)) continue; // a request to another host
        const op = operationFor(index, match[1], match[2]);
        if (op) return op;
      }
    }
  }
  for (let distance = 0; distance <= 30; distance++) { // stack frames: Python prints them before the error, the others after
    for (const i of distance ? [line - distance, line + distance] : [line]) {
      if (i < 0 || i >= lines.length || !/^\s+at\s|File "|\bin [A-Za-z_]\w*\s*$|^\s+\S.*\(.*$/.test(lines[i])) continue;
      for (const word of lines[i].match(/[A-Za-z_][\w]*/g) || []) {
        const ops = index.byMethod.get(word) || index.byMethod.get(word.replace(/Async$/, ""));
        if (ops && ops.length === 1) return ops[0];
      }
    }
  }
  const url = command.match(/https?:\/\/[^\s"'<>`]+/);
  if (url && /(?:^|[\s;&|(])curl(?:\.exe)?\s/i.test(command) && MAXIO_HOST.test(` ${url[0]}`)) {
    const verb = (command.match(/(?:-X|--request)[\s=]+["']?([A-Za-z]+)/) || [])[1] || (/(?:\s-d\b|\s--data|\s--json|\s-F\b|\s--form)/.test(command) ? "POST" : "GET");
    return operationFor(index, verb, url[0]);
  }
  return null;
}

// Where the literal text starts in the output, or -1. The match is case-sensitive and may not
// start in the middle of a word, so "First name: cannot be blank." never matches the row whose
// text is "Name: cannot be blank.".
function findLiteral(text, fragment, from) {
  for (let at = text.indexOf(fragment, from); at >= 0; at = text.indexOf(fragment, at + 1)) if (at === 0 || !/\p{L}/u.test(text[at - 1])) return at;
  return -1;
}
// How much of a row's own message the output carries: 0 when it does not. A message with a variable
// part is stored as several literal fragments; all of them must appear, in order and close together.
function literalHit(row, output) {
  const groups = [];
  const grouped = new Set();
  for (const quoted of String(row.message || "").matchAll(/"([^"]+)"/g)) {
    const inside = row.patterns.map((p) => [quoted[1].indexOf(p), p]).filter(([at]) => at >= 0).sort((a, b) => a[0] - b[0]).map(([, p]) => p);
    if (inside.length) { groups.push(inside); inside.forEach((p) => grouped.add(p)); }
  }
  for (const pattern of row.patterns) if (!grouped.has(pattern)) groups.push([pattern]);
  let best = 0;
  for (const group of groups) {
    for (let start = findLiteral(output, group[0], 0); start >= 0; start = findLiteral(output, group[0], start + 1)) {
      let end = start + group[0].length, whole = true;
      for (const fragment of group.slice(1)) {
        const at = findLiteral(output, fragment, end);
        if (at < 0 || at - end > 300) { whole = false; break; }
        end = at + fragment.length;
      }
      if (whole) { best = Math.max(best, group.join("").length); break; }
    }
  }
  return best;
}

function onShell(ev, file) {
  const output = shellOutput(ev.raw);
  if (!/[45]\d\d/.test(output)) return null;
  const command = Array.isArray(ev.input.command) ? ev.input.command.join(" ") : typeof ev.input.command === "string" ? ev.input.command : "";
  // Say nothing when the command reads files rather than runs code, or prints the failure tables.
  if (/knowledge|failures|map[\\/]+operations|AGENTS\.md|docs[\\/]/i.test(command) || onlyReadsFiles(command)) return null;
  if (/^\s*\|?\s*[45]\d\d\b[^|\n]*\|[^|\n]*\|/m.test(output) || /^\|[^\n]*\bCause\b[^\n]*\|[^\n]*\bDo\b[^\n]*\|\s*$/m.test(output) ||
    /"operationId"\s*:|"patterns"\s*:|When it fails|Status\s*\u00b7\s*message/.test(output)) return null;

  const snapshot = loadState(file);
  // The language: the session's, else the one the SDK's own error format gives away, else the project's.
  const formLang = /\b(?:GET|POST|PUT|PATCH|DELETE)\s+https?:\/\/\S+\s+failed with (?:status )?[45]\d\d/.test(output) ? "typescript"
    : /\b(?:GET|POST|PUT|PATCH|DELETE)\s+https?:\/\/\S+\s+returned [45]\d\d/.test(output) ? "csharp"
    : /\bApiError\b.*HTTP [45]\d\d|maxio_advanced_billing/.test(output) ? "python" : null;
  let lang = snapshot.lang || formLang;
  let dirs = snapshot.dirs;
  let detected = null;
  if (!lang) { detected = detectProject(ev.cwd); lang = detected.langs[0] || null; dirs = { ...dirs, ...detected.dirs }; }
  const folder = lang ? sdkFolder(lang, ev.cwd, dirs[lang]) : bundledFolders().map((f) => sdkFolder(f.lang, ev.cwd)).find(Boolean);
  if (!folder) return null;
  const index = loadIndex(folder.dir);
  const rows = loadFailures(folder.dir);
  if (!index || !rows) return null; // nothing to give: stay silent
  const neutral = (text) => (lang ? text : neutralNames(text, index));

  const pythonKnown = snapshot.langs.includes("python") || lang === "python" && Boolean(snapshot.lang || detected);
  const rejections = rejectionsIn(output, command, index, pythonKnown);
  if (!rejections.length) return null;
  const rowKey = (row) => `${row.operationId}|${row.status}|${slug(String(row.message || "")).slice(0, 48)}`;
  const nameOf = (opId) => { const op = index.operations[opId]; return "`" + (op && lang ? op.call : opId) + "`"; };
  // The rows as a list. Where they all point at the same notes, the notes are named once, after it.
  const rowList = (given) => {
    const pointers = unique(given.map((row) => (typeof row.notes === "string" && row.notes ? notesPointer(folder, row.notes) : "")));
    const shared = pointers.length === 1 && pointers[0] && given.length > 1;
    const one = (row) => `- ${row.status} ${neutral(String(row.message || "")).trim()} (${nameOf(row.operationId)})\n  Cause: ${neutral(String(row.cause || ""))}\n  Do: ${neutral(String(row.do || ""))}` +
      (!shared && typeof row.notes === "string" && row.notes ? `\n  Notes: ${notesPointer(folder, row.notes)}` : "");
    return given.map(one).join("\n\n") + (shared ? `\n\nNotes for all of these: ${pointers[0]}` : "");
  };
  const failuresFile = "`knowledge/failures.md`";
  const errorDocText = readText(path.join(folder.dir, "docs", "error-handling.md"));
  const howToRead = !errorDocText ? "" : /^#{1,6}\s+Maxio: reading a rejection\s*$/m.test(errorDocText)
    ? ` \`docs/error-handling.md\`, section "Maxio: reading a rejection", shows how to print the status and Maxio's own message from the SDK's error.`
    : ` \`docs/error-handling.md\` shows how to read the SDK's error.`;
  const never = "A 4xx from Maxio is a rejection, never a sign that the call works.";

  return commit(file, (state) => {
    if (detected && detected.langs.length) rememberProject(state, { ...detected, lang, uses: true });
    const sections = [];
    let room = 3; // never more than three rows in one message
    // A row whose own message was in the output is remembered by itself, so it is shown once even
    // if it was listed earlier among an operation's possible causes.
    const take = (list, identified) => { const given = list.slice(0, room); room -= given.length; if (identified) for (const row of given) state.rej.push(rowKey(row)); return given; };

    for (const rejection of rejections) {
      const status = rejection.status;
      if (rejection.op) {
        const opId = rejection.op.opId;
        const what = `HTTP ${status} from ${nameOf(opId)} (\`${rejection.op.route}\`)`;
        const documented = rows.filter((row) => row.operationId === opId && row.status === status);
        // The operation is known: only its own rows count, first the ones whose message is in the output.
        const literal = documented.filter((row) => literalHit(row, output));
        if (literal.length) {
          const given = take(literal.filter((row) => !state.rej.includes(rowKey(row))), true);
          state.rej.push(`${opId}|${status}`);
          if (given.length) sections.push(`The command output shows a rejection that Maxio documents: ${what}. Read this before changing code. ${never}\n\n${rowList(given)}`);
          continue;
        }
        if (state.rej.includes(`${opId}|${status}`)) continue;
        state.rej.push(`${opId}|${status}`);
        const given = take(documented);
        if (given.length) {
          sections.push(`The command output shows that Maxio rejected a request: ${what}. ${never} Maxio documents these causes for that status on that operation (from ${failuresFile}). The output carries none of their literal messages, so compare Maxio's own message with them before changing code:\n\n${rowList(given)}` +
            (documented.length > given.length ? `\n\n${failuresFile} has ${documented.length - given.length} more for that status and operation.` : "") +
            (howToRead ? `\n\n${rejection.sdkFormat ? "The SDK's error does not print Maxio's message by itself." : "If the output does not show Maxio's message, print it."}${howToRead}` : ""));
        } else if (!documented.length) {
          sections.push(`The command output shows that Maxio rejected a request: ${what}. ${never} ${failuresFile} has no row for that status on that operation; the operation's notes and Maxio's own message say more.${howToRead}`);
        }
        continue;
      }
      // The operation is not known: a row counts only when its own message is in the output. An
      // operation this session's edits call is the likeliest source, so its rows come first.
      const literal = rows.filter((row) => row.status === status).map((row) => ({ row, hit: literalHit(row, output) })).filter((m) => m.hit)
        .sort((a, b) => state.seen.includes(b.row.operationId) - state.seen.includes(a.row.operationId) || b.hit - a.hit).map((m) => m.row);
      if (literal.length) {
        const given = take(literal.filter((row) => !state.rej.includes(rowKey(row))), true);
        if (given.length) sections.push(`The command output shows a rejection that Maxio documents, with HTTP ${status}. Read this before changing code. ${never}\n\n${rowList(given)}`);
        continue;
      }
      if (state.rej.includes(`?|${status}`)) continue;
      state.rej.push(`?|${status}`);
      // Only what is known: a status, and that the request went to Maxio.
      sections.push(`The command output shows that a request to Maxio returned HTTP ${status}. ${never} ${failuresFile} lists Maxio's rejections by status and message; find this one there before changing code.${rejection.sdkFormat ? ` The SDK's error does not print Maxio's message by itself.${howToRead}` : ""}`);
    }
    state.rej = unique(state.rej);
    if (!sections.length) return null;
    const footer = lang ? folderLine(folder)
      : `Paths in this message are relative to a Maxio Advanced Billing SDK folder. The maxio-advanced-billing plugin bundles one per language under ${tick(PLUGIN_SDK)}. Operations are named here by the API's operationId; each SDK's \`sdk-map.md\` gives its own spelling.`;
    let text = "";
    for (const section of sections) { const next = text ? `${text}\n\n${section}` : section; if (bytes(`${next}\n\n${footer}`) > MAX_BYTES) break; text = next; }
    return text ? `${text}\n\n${footer}` : null;
  });
}

// ---------------------------------------------------------------------------------------------
// Claude Code, before a read: approve Read, Glob and Grep inside this plugin's own sdk/ folder, and
// inside the project's installed C# package in the NuGet cache (only that package's own folder, found
// from the project's last restore)
// ---------------------------------------------------------------------------------------------
function onRead(ev) {
  const input = ev.input;
  let target = null;
  if (ev.tool === "Read") target = input.file_path;
  else if (ev.tool === "Grep") target = input.path;
  else if (ev.tool === "Glob") {
    const pattern = typeof input.pattern === "string" ? input.pattern : "";
    if (/(^|[\\/])\.\.([\\/]|$)/.test(pattern)) return null;
    target = input.path;
    if (!target && path.isAbsolute(pattern)) { // a pattern with its own folder: the part before the first wildcard
      const fixed = pattern.split(/[*?[{]/)[0];
      target = /[\\/]$/.test(fixed) || fixed === pattern ? fixed : path.dirname(fixed);
    } else if (path.isAbsolute(pattern)) return null;
  }
  if (typeof target !== "string" || !target || /^(\\\\|\/\/)/.test(target)) return null;
  const resolved = realPath(path.resolve(ev.cwd, target));
  if (isInside(realPath(PLUGIN_SDK), resolved)) {
    return { hookSpecificOutput: { hookEventName: ev.eventName, permissionDecision: "allow", permissionDecisionReason: "A read-only tool on a file inside the maxio-advanced-billing plugin's bundled sdk folder." } };
  }
  // Cheap test first: only a path that names the package can be inside it.
  if (!/maxioadvancedbilling/i.test(resolved)) return null;
  const folder = sdkFolder("csharp", ev.cwd, null);
  if (!folder || !folder.nuget || !isInside(realPath(folder.dir), resolved)) return null;
  return { hookSpecificOutput: { hookEventName: ev.eventName, permissionDecision: "allow", permissionDecisionReason: "A read-only tool on a file inside this project's installed MaxioAdvancedBilling package." } };
}

// ---------------------------------------------------------------------------------------------
// main
// ---------------------------------------------------------------------------------------------
function debug(ev, result) {
  const target = process.env.MAXIO_HOOK_DEBUG;
  if (!target) return;
  try { fs.appendFileSync(target, JSON.stringify({ at: new Date().toISOString(), host: HOST, event: ev.eventName, tool: ev.tool || undefined, source: ev.event === "sessionstart" ? ev.source : undefined, session: ev.session || undefined, gave: result }) + "\n"); } catch { /* best effort */ }
}

function main() {
  const ev = normalise(readPayload());
  let result = null;
  try {
    if (ev.event === "pretooluse") {
      result = HOST === "claude" ? onRead(ev) : null;
      debug(ev, result ? "allow" : null);
      if (result) process.stdout.write(JSON.stringify(result));
      return;
    }
    const file = stateFile(ev);
    if (ev.event === "sessionstart") result = onSessionStart(ev, file);
    else if (ev.event === "precompact") result = onCompact(file);
    else if (ev.event === "userpromptsubmit") result = onPrompt(ev, file);
    else if (ev.event === "posttooluse" || ev.event === "posttoolusefailure") {
      if (ev.isShell) result = onShell(ev, file);
      else if (ev.isEdit && ev.event === "posttooluse") result = onEdit(ev, file);
    }
  } catch { result = null; } // never put an error into the session: stay silent
  debug(ev, result);
  if (typeof result !== "string" || !result || bytes(result) > MAX_BYTES + 500) return;
  const output = HOST === "cursor" ? { additional_context: result } : { hookSpecificOutput: { hookEventName: ev.eventName, additionalContext: result } };
  // ASCII-only JSON, so no host can misread it through a legacy code page
  process.stdout.write(JSON.stringify(output).replace(/[\u0080-\uffff]/g, (ch) => "\\u" + ch.charCodeAt(0).toString(16).padStart(4, "0")));
}

try { main(); } catch { /* always exit 0 */ }
process.exitCode = 0;
